# Codex and Claude Code: Jade handoff

## Scope and responsibilities

Codex coordinates and checks the result. Claude Fable is the preferred collaborator.
Assignments are proposals until the receiving session acknowledges them. Never claim
that an open Claude Desktop conversation has received a CLI consultation.

The initial safe mode is one project writer at a time. Claim `project-write` before
editing project content, and release only after saving a handoff. Read-only review
can run concurrently. For future parallel implementation, use isolated Git worktrees
and one integrator; do not change branches in a colleague's checkout.

Use one unique Owner string per session, not just "Claude" or "Codex".
Run `.coordination/coordinate.ps1 -Action claim -Resource project-write -Owner SESSION`.
If denied, review read-only or coordinate with the recorded owner. No automatic
expiry or stealing locks: a crash requires checking the previous process first.
Release with the same Owner and `-Action release`.

Before any paid generation, claim `media-render` and check HANDOFF.md and provider
status. Record the source checksum, destination, job ID, and status in HANDOFF.md
before relinquishing ownership. If a submission response is lost, reconcile the
provider's jobs instead of submitting again. Hold an unresolved render reservation
until reconciliation. Project writes still require project-write.

## Review and continuity

Record the latest source, changed files, outstanding checks, and actual output in
HANDOFF.md. The other agent reviews the artifact and tests relevant behavior.
Limit repeated review to three rounds, then report the unresolved cause. A green
code test alone does not prove an avatar looks natural: inspect the actual preview.
Never mark an assignment accepted or an output published without evidence.

The coordination script serializes claims and checks owner-matched release.
These are cooperative locks: they do not intercept arbitrary app writes, UI actions,
or connector calls. Existing sessions must acknowledge this protocol. No permission
bypass, background monitoring, or automatic paid generation is installed here.

## Design references

- https://github.com/ching-kuo/claude-codex (bounded independent review)
- https://github.com/Dusttoo/orka (ownership, isolation, review gates)
- https://github.com/cgeene/commandcenter (durable task status)

This is a small Windows-native adaptation, not an installation of those projects.
