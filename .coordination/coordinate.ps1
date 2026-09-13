[CmdletBinding()]
param(
  [ValidateSet('status','claim','release')][string]$Action = 'status',
  [ValidatePattern('^[a-z0-9-]+$')][string]$Resource = 'project-write',
  [string]$Owner,
  [string]$StateDirectory = $PSScriptRoot
)
$ErrorActionPreference = 'Stop'
if ($Action -ne 'status' -and [string]::IsNullOrWhiteSpace($Owner)) { throw 'Owner is required.' }
$dir = [IO.Path]::GetFullPath($StateDirectory)
[IO.Directory]::CreateDirectory($dir) | Out-Null
$gate = $null
try {
  $gate = [IO.File]::Open((Join-Path $dir 'state.gate'), 'OpenOrCreate', 'ReadWrite', 'None')
  $path = Join-Path $dir 'claims.json'
  $claims = @()
  if (Test-Path -LiteralPath $path) { $claims = @(Get-Content -Raw -LiteralPath $path | ConvertFrom-Json) }
  if ($Action -eq 'status') { ConvertTo-Json -InputObject $claims -Depth 5; return }
  $existing = @($claims | Where-Object { $_.resource -eq $Resource })
  if ($Action -eq 'claim') {
    if ($existing.Count -gt 0) { throw ('Resource already reserved by ' + $existing[0].owner) }
    $claims += [pscustomobject]@{resource=$Resource;owner=$Owner;claimedAt=[DateTime]::UtcNow.ToString('o')}
  } else {
    if ($existing.Count -ne 1 -or $existing[0].owner -cne $Owner) { throw 'Release denied: owner does not match.' }
    $claims = @($claims | Where-Object { $_.resource -ne $Resource })
  }
  $temp = Join-Path $dir 'claims.pending.json'
  [IO.File]::WriteAllText($temp, (ConvertTo-Json -InputObject $claims -Depth 5))
  if (Test-Path -LiteralPath $path) { [IO.File]::Replace($temp,$path,(Join-Path $dir 'claims.previous.json')) }
  else { [IO.File]::Move($temp,$path) }
  Write-Output ($Action + ' succeeded: ' + $Resource)
} finally { if ($null -ne $gate) { $gate.Dispose() } }
