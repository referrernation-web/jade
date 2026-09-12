import base64, pathlib
A = pathlib.Path(__file__).parent / "assets"

def b64(p):
    f = A / p
    return base64.b64encode(f.read_bytes()).decode() if f.exists() else ""

def webp(p, maxw=1280, q=80):
    """Convert assets/<p> to assets/img/<stem>.webp and return the relative URL ('' if missing)."""
    from PIL import Image
    f = A / p
    if not f.exists():
        return ""
    outdir = A / "img"; outdir.mkdir(exist_ok=True)
    o = outdir / (f.stem + ".webp")
    if not o.exists() or o.stat().st_mtime < f.stat().st_mtime:
        im = Image.open(f).convert("RGB")
        if im.width > maxw:
            im = im.resize((maxw, int(im.height * maxw / im.width)), Image.LANCZOS)
        im.save(o, "WEBP", quality=q, method=6)
    return "assets/img/" + o.name

PHOTO = ""
HERO = webp("hero-poster.jpg", 1280, 82)
ABOUT = webp("about-photo.jpg", 720, 82)
INTRO = "video/intro.mp4" if (pathlib.Path(__file__).parent / "video" / "intro.mp4").exists() else ""
THUMBS = {k: webp("thumb-" + k + ".jpg", 1280, 78) for k in ["vicemayor", "infosys", "alorica", "youth", "seo"]}

EXPERTISE = [
    ("01", "Executive Calendar &amp; Inbox",
     "Daily calendar and appointments across meetings, official functions and engagements. Monitoring email and correspondence, surfacing priority items and drafting timely responses on behalf of the office."),
    ("02", "Meeting Prep &amp; Follow-Through",
     "Reports, briefing materials and meeting documents that support decision-making. Detailed notes, action-item tracking and coordinated updates that close open requests."),
    ("03", "Financial Account Operations",
     "High-volume inbound communications on financial accounts, transactions and service requests, resolved within regulatory requirements, internal controls and documented procedures. Precise records, strong data integrity."),
    ("04", "SEO &amp; AEO for WordPress",
     "Keyword and entity research, on-page optimization, FAQ and article schema, WordPress technical health, Search Console and Analytics reporting. Second track, case studies on request."),
]

SKILL_GROUPS = [
    ("Executive Support", [
        ("google", "Google Workspace"), ("mono:OL", "Outlook"), ("mono:MT", "Microsoft Teams"),
        ("googledrive", "Google Drive"), ("dropbox", "Dropbox"), ("salesforce", "Salesforce CRM")]),
    ("AI &amp; Productivity", [
        ("mono:CP", "Microsoft Copilot"), ("openai", "ChatGPT"), ("anthropic", "Claude"),
        ("googlesheets", "Sheets"), ("googledocs", "Docs"), ("notion", "Notes &amp; SOPs")]),
    ("SEO &amp; Analytics", [
        ("googlesearchconsole", "Search Console"), ("googleanalytics", "Google Analytics"), ("semrush", "SEMrush"),
        ("mono:AH", "Ahrefs"), ("json", "Schema markup"), ("googlechrome", "AI Overviews")]),
    ("WordPress", [
        ("wordpress", "WordPress"), ("yoast", "Yoast SEO"), ("mono:RM", "Rank Math"),
        ("elementor", "Elementor"), ("mono:PL", "Plugins &amp; themes"), ("cloudflare", "Site speed")]),
]

FEATURED = [
    ("EXECUTIVE ASSISTANT • LOCAL GOVERNMENT", "Office of the Vice Mayor, Mansalay",
     "Managed the Vice Mayor&rsquo;s daily calendar across meetings, official functions and community engagements. Monitored official email and correspondence, surfaced priority items and drafted responses on behalf of the office.",
     "Reports, briefing materials and meeting documents for executive decisions &mdash; Jul&ndash;Dec 2023",
     ["Calendar", "Correspondence", "Briefings", "Meeting notes"], "vicemayor", "#journey"),
    ("SENIOR PROCESS EXECUTIVE • FINANCIAL ACCOUNTS", "Infosys BPM",
     "High-volume inbound communications on financial accounts, transactions and service requests, resolved within regulatory requirements, internal controls and documented procedures.",
     "Precise records, strong data integrity; mentoring new hires with Training and Quality &mdash; Jul 2024 to present",
     ["Financial accounts", "Compliance", "Records", "Mentoring"], "infosys", "#journey"),
    ("CUSTOMER SERVICE • TELCO ACCOUNT", "Alorica / Probe CX",
     "Resolved billing, promotion and connectivity concerns in a fast-paced environment. Recommended products and services based on customer needs and account context.",
     "Proactive guidance that prevented recurring issues &mdash; Feb&ndash;Jun 2024",
     ["Billing", "Connectivity", "Recommendations", "Customer care"], "alorica", "#journey"),
    ("YOUTH LEADER • COMMUNITY", "Community Youth Organization",
     "Led and organized community youth programs over six years: schedules, logistics, resources and event activities, with planning, communication and stakeholder coordination built along the way.",
     "Six years of sustained leadership commitment",
     ["Planning", "Logistics", "Stakeholders", "Events"], "youth", "#journey"),
    ("SEO / AEO • SECOND TRACK", "SEO and Answer Engine Optimization",
     "Keyword and entity research, on-page optimization for WordPress (meta tags, headings, internal links, FAQ and article schema), technical health and Search Console reporting. Content structured for direct-answer extraction and E-E-A-T signals.",
     "Case studies and client references available on request",
     ["WordPress", "Schema", "GSC", "AI Overviews"], "seo", "#skills"),
]

SYSLOG = [
    ("Education", "Bachelor of Science in Information Systems &middot; Clarendon College", "BSIS", "#journey"),
    ("Languages", "English and Tagalog", "EN / TL", "#journey"),
    ("Location", "Fort Bonifacio, Taguig City &middot; open to remote work", "Remote", "#contact"),
    ("Resume", "Executive Assistant / Executive Virtual Assistant &middot; PDF", "PDF", "assets/Jade-Patrick-Mendoza-Resume-2026.pdf"),
]




CERTS = [
    ("STRENGTH", "01", "Discretion and data integrity", "Professional strength", "https://www.linkedin.com/in/jadepatrickmendoza"),
    ("STRENGTH", "02", "High-volume accuracy", "Professional strength", "https://www.linkedin.com/in/jadepatrickmendoza"),
    ("STRENGTH", "03", "Anticipates next steps", "Professional strength", "https://www.linkedin.com/in/jadepatrickmendoza"),
    ("STRENGTH", "04", "Calm under pressure", "Professional strength", "https://www.linkedin.com/in/jadepatrickmendoza"),
    ("STRENGTH", "05", "Clear written communication", "Professional strength", "https://www.linkedin.com/in/jadepatrickmendoza"),
    ("STRENGTH", "06", "Independent follow-through", "Professional strength", "https://www.linkedin.com/in/jadepatrickmendoza"),
    ("COMPETENCY", "07", "Executive calendar &amp; scheduling", "Core competency", "https://www.linkedin.com/in/jadepatrickmendoza"),
    ("COMPETENCY", "08", "Inbox &amp; correspondence management", "Core competency", "https://www.linkedin.com/in/jadepatrickmendoza"),
    ("COMPETENCY", "09", "Meeting preparation &amp; follow-through", "Core competency", "https://www.linkedin.com/in/jadepatrickmendoza"),
    ("COMPETENCY", "10", "Document &amp; report preparation", "Core competency", "https://www.linkedin.com/in/jadepatrickmendoza"),
    ("COMPETENCY", "11", "Travel and logistics coordination", "Core competency", "https://www.linkedin.com/in/jadepatrickmendoza"),
    ("COMPETENCY", "12", "Online research &amp; summarization", "Core competency", "https://www.linkedin.com/in/jadepatrickmendoza"),
    ("COMPETENCY", "13", "Confidential information handling", "Core competency", "https://www.linkedin.com/in/jadepatrickmendoza"),
    ("COMPETENCY", "14", "Stakeholder communication", "Core competency", "https://www.linkedin.com/in/jadepatrickmendoza"),
    ("COMPETENCY", "15", "Remote work &amp; self-management", "Core competency", "https://www.linkedin.com/in/jadepatrickmendoza"),
    ("EDUCATION", "16", "BS Information Systems", "Clarendon College", "https://www.linkedin.com/in/jadepatrickmendoza"),
]


def pills(items):
    return "".join('<span class="pill">' + i + "</span>" for i in items)


ROT = ["r1", "r2", "r3", "r4"]
expertise_html = "".join(
    '<article class="pin ' + ROT[i] + (' solid' if i == 0 else '') + '" data-rv="' + ('right' if i % 2 == 0 else 'left') + '"><span class="ledge"></span><span class="tack"></span><div class="xnum">' + n + "</div><h3>" + t + "</h3><p>" + d + "</p></article>"
    for i, (n, t, d) in enumerate(EXPERTISE))

skills_html = ""
for gname, icons in SKILL_GROUPS:
    cells = "".join(
        '<div class="icon hv" data-rv="zoom"><img src="' + (("data:image/svg+xml;utf8," + __import__("urllib.parse").parse.quote('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><circle cx="24" cy="24" r="21" fill="none" stroke="#ffffff" stroke-width="3"/><text x="24" y="30" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="17" font-weight="700" fill="#ffffff">' + slug[5:] + '</text></svg>')) if slug.startswith("mono:") else "https://cdn.simpleicons.org/" + slug + "/ffffff") + '" alt="' + label +
        '" loading="lazy" onerror="this.parentNode.classList.add(&quot;noico&quot;)"><span>' + label + "</span></div>"
        for slug, label in icons)
    skills_html += '<div class="sgroup"><h3>' + gname + '</h3><div class="igrid">' + cells + "</div></div>"

LQ = {k: __import__("patch8_lqip").lqip(A / ("thumb-" + k + ".jpg")) for k in ["vicemayor", "infosys", "alorica", "youth", "seo"]}
feat_html = ""
for cat, title, desc, ev, tags, thumb, url in FEATURED:
    shot = ('<div class="shot"><img class="lq" src="data:image/jpeg;base64,' + LQ[thumb] + '" data-src="' + THUMBS[thumb] + '" alt="' + title + '" loading="lazy" decoding="async"></div>'
            if thumb and THUMBS.get(thumb) else '<div class="shot noimg"><span>' + url.replace("https://", "") + "</span></div>")
    slug = (thumb or url.replace("https://", "").split(".")[0])
    feat_html += ('<article class="proj glow tilt" data-slug="' + slug + '" data-title="' + title + '" data-cat="' + cat + '" data-desc="' + desc.replace('"', '&quot;') + '" data-ev="' + ev.replace('"', '&quot;') + '" data-tags="' + ", ".join(tags) + '" data-url="' + url + '" tabindex="0" role="button" aria-haspopup="dialog">' + shot + '<div class="cat">' + cat + "</div><h3>" + title + "</h3><p>" + desc +
                  '</p><div class="ev">' + ev + '</div><div class="tags">' + pills(tags) +
                  '</div><span class="visit">Open case study &rarr;</span></article>')

syslog_html = "".join(
    '<a class="lrow hv" href="' + url + '" target="_blank" rel="noopener"><div><b>' + t + "</b><span>" + d +
    '</span></div><em>' + tag + "</em></a>"
    for t, d, tag, url in SYSLOG)

certs_html = "".join(
    '<div class="flip" data-rv="drop"><div class="finner hv"><div class="fface ffront"><div class="ftop"><span class="chip">' + chip +
    '</span><span class="cnum">' + n + '</span></div><h4>' + title + '</h4><div class="issued"><small>ISSUED SYSTEM NODE</small>' + issuer +
    '</div></div><div class="fface fback"><div class="ftop"><span class="shield">&#9673;</span><small>SECURED NODE</small></div><small class="vo">VERIFICATION OBJECT</small><h4>' + title +
    '</h4><a class="viewc" href="' + url + '" target="_blank" rel="noopener">View Certificate &#8599;</a><div class="fbot"><small>SYS ID: #' + n + '</small><b>VERIFIED</b></div></div></div></div>'
    for chip, n, title, issuer, url in CERTS)

CSS = """
:root{--bg:#fff;--surf:#fff;--line:#e6e6ea;--txt:#111;--mut:#666;--acc:#176f7d;--grn:#16a34a}
html[data-theme=light]{--bg:#f7f6f4;--surf:#fff;--line:#e5e2dc;--txt:#111;--mut:#6b6b6b;--acc:#176f7d;--grn:#16a34a}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:#fff;color:#111;font:400 16px/1.6 Inter,ui-sans-serif,system-ui,sans-serif;-webkit-font-smoothing:antialiased;overflow-x:hidden}
body::after{content:"";position:fixed;inset:0;z-index:99;pointer-events:none;opacity:.045;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)' opacity='0.7'/%3E%3C/svg%3E")}
.wrap{max-width:1200px;margin:0 auto;padding:0 32px}
.mono{font:500 11px/1 'JetBrains Mono',ui-monospace,monospace;letter-spacing:.18em;text-transform:uppercase}
.red{color:var(--acc)}
a{color:inherit;text-decoration:none}
.glow{position:relative}
.glow::before{content:"";position:absolute;inset:-1px;border-radius:inherit;padding:1px;background:conic-gradient(from var(--a,0deg),#ff3d81,#ffb020,#3dff8f,#2ec9ff,#8a5cff,#ff3d81);-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;animation:spin 6s linear infinite;opacity:.7;pointer-events:none}
.glow::after{content:"";position:absolute;inset:-6px;border-radius:inherit;background:conic-gradient(from var(--a,0deg),#ff3d81,#ffb020,#3dff8f,#2ec9ff,#8a5cff,#ff3d81);filter:blur(18px);opacity:.14;z-index:-1;animation:spin 6s linear infinite;pointer-events:none}
@property --a{syntax:"<angle>";inherits:false;initial-value:0deg}
@keyframes spin{to{--a:360deg}}
.glass{background:rgba(255,255,255,.55);-webkit-backdrop-filter:blur(14px) saturate(160%);backdrop-filter:blur(14px) saturate(160%);border:1px solid rgba(255,255,255,.65);box-shadow:0 8px 30px rgba(0,0,0,.08)}
.glass-red{background:rgba(23,111,125,.78);-webkit-backdrop-filter:blur(14px) saturate(160%);backdrop-filter:blur(14px) saturate(160%);border:1px solid rgba(255,255,255,.45);box-shadow:0 8px 30px rgba(23,111,125,.25);color:#fff}
.glass-dark{background:rgba(0,0,0,.28);-webkit-backdrop-filter:blur(14px) saturate(140%);backdrop-filter:blur(14px) saturate(140%);border:1px solid rgba(255,255,255,.3)}
@supports not ((backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px))){.glass{background:rgba(255,255,255,.94)}.glass-red{background:#1b8593}.glass-dark{background:rgba(0,0,0,.55)}}
.proofband{background:var(--acc);color:#fff;overflow:hidden;padding:14px 0;border-top:1px solid rgba(255,255,255,.3)}
.proofband .mq-track{display:flex;gap:44px;width:max-content;animation:sc 46s linear infinite}
.proofband:hover .mq-track{animation-play-state:paused}
.pf{display:inline-flex;align-items:baseline;gap:10px;font:500 12px/1 'JetBrains Mono',monospace;letter-spacing:.06em;white-space:nowrap;color:rgba(255,255,255,.9)}
.pf b{font:900 20px/1 Inter,sans-serif;letter-spacing:-.02em;color:#fff}
@keyframes sc{to{transform:translateX(-50%)}}
.csd{border:0;padding:0;background:transparent;max-width:min(920px,92vw);width:100%}
::view-transition-old(csimg),::view-transition-new(csimg){animation-duration:.45s}
::view-transition-group(csimg){animation-timing-function:cubic-bezier(.2,.7,.2,1)}
.csd::backdrop{background:rgba(17,17,17,.55);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}
.csdIn{position:relative;border-radius:22px;overflow:hidden;background:rgba(255,255,255,.86);color:#111;display:grid;grid-template-columns:1.1fr .9fr}
.csdShot{background:#f2f2f5;min-height:280px}.csdShot img{width:100%;height:100%;object-fit:cover;object-position:top;display:block}.csdShot.noimg{display:flex;align-items:center;justify-content:center;font:500 13px/1 'JetBrains Mono',monospace;color:#666}
.csdBody{padding:30px 30px 30px 26px;display:flex;flex-direction:column;gap:12px}.csdBody h3{font-size:26px;font-weight:800;letter-spacing:-.02em}.csdBody p{color:#555;font-size:14px}.csdBody .btn{align-self:flex-start;margin-top:8px}
.csdX{position:absolute;top:12px;right:14px;z-index:2;width:36px;height:36px;border-radius:50%;border:1px solid #e3e3ea;background:#fff;font-size:20px;cursor:pointer}
.proj[role=button]{cursor:pointer}
@media(max-width:760px){.csdIn{grid-template-columns:1fr}}
.tilt{transition:transform .18s ease,box-shadow .18s ease;will-change:transform}
.tilt:hover{box-shadow:0 18px 40px rgba(0,0,0,.10)}
.btn,.hire,.unmute,.viewc{transition:transform .18s ease,box-shadow .18s ease}
.btn:hover,.hire:hover,.viewc:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(23,111,125,.28)}
.hero .spot{position:absolute;inset:0;z-index:1;pointer-events:none;background:radial-gradient(420px circle at var(--mx,50%) var(--my,50%),rgba(23,111,125,.16),transparent 62%);mix-blend-mode:multiply}
@media(prefers-reduced-motion:reduce){.tilt,.btn,.hire{transition:none}.hero .spot{display:none}}
.rv{opacity:0;transform:translateY(22px);transition:opacity .65s ease,transform .65s cubic-bezier(.2,.7,.2,1)}
.rv.in{opacity:1;transform:none}
.rv[data-rv=left]{transform:translateX(-46px)}.jt.rv{transition-delay:0ms!important}.rv[data-rv=right]{transform:translateX(46px)}.rv[data-rv=zoom]{transform:scale(.82)}
.rv[data-rv=drop]{transform:translateY(-220px);transition:none}
.rv.in[data-rv=left],.rv.in[data-rv=right],.rv.in[data-rv=zoom]{transform:none}
.rv[data-rv=drop].in{animation:dropBounce 1.15s cubic-bezier(.28,.84,.42,1) forwards}
@keyframes dropBounce{0%{opacity:0;transform:translateY(-220px)}55%{opacity:1;transform:translateY(0)}72%{transform:translateY(-16px)}86%{transform:translateY(0)}94%{transform:translateY(-5px)}100%{opacity:1;transform:translateY(0)}}
.btn:active,.hire:active,.unmute:active,.viewc:active,.proj:active,.icon:active,.arrows button:active{transform:scale(.97)!important}
.cue{position:absolute;left:50%;bottom:22px;transform:translateX(-50%);z-index:3;width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#111;background:rgba(255,255,255,.6);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.8);animation:bounceY 1.6s infinite}
@keyframes bounceY{0%,100%{transform:translate(-50%,0)}50%{transform:translate(-50%,-10px)}}
.flabel{position:absolute;z-index:3;font:500 10px/1.5 'JetBrains Mono',monospace;letter-spacing:.14em;color:#444;animation:softpulse 2.4s ease-in-out infinite;text-transform:uppercase}
.flabel.tr{top:92px;right:36px;text-align:right}.flabel.bl{bottom:60px;left:36px}
@keyframes softpulse{0%,100%{opacity:.45}50%{opacity:1}}
nav{transition:background .4s,box-shadow .4s,border-color .4s}
nav .wrap{transition:height .3s}
nav.scrolled{background:rgba(255,255,255,.82);box-shadow:0 6px 30px rgba(0,0,0,.08);border-bottom-color:rgba(0,0,0,.06)}
nav.scrolled .wrap{height:56px}
.nlinks{position:relative}
.nlinks a::after{display:none}
.slide{position:absolute;bottom:-6px;height:2px;background:var(--acc);border-radius:2px;transition:left .35s cubic-bezier(.2,.7,.2,1),width .35s cubic-bezier(.2,.7,.2,1);left:0;width:0}
.hv{transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease,background .25s ease}
.hv:hover{transform:translateY(-3px) scale(1.015);border-color:rgba(23,111,125,.35);box-shadow:0 14px 34px rgba(23,111,125,.10)}
.hv::before{transition:opacity .25s}
.icon.hv:hover img{transform:scale(1.12);filter:invert(1) drop-shadow(0 8px 14px rgba(0,0,0,.18))}
.icon img{transition:transform .25s,filter .25s}
.cgrid{cursor:grab;user-select:none}.cgrid.dragging{cursor:grabbing;scroll-snap-type:none}.cgrid.dragging .flip{pointer-events:none}
@supports (animation-timeline: view()){
.lz .shead h2{border-bottom:0;background:linear-gradient(var(--acc),var(--acc)) no-repeat 0 100%/0% 4px;animation:draww linear both;animation-timeline:view();animation-range:entry 10% entry 60%}
@keyframes draww{to{background-size:100% 4px}}
.proofband .mq-track{animation:sc 46s linear infinite,none}
.pf b{animation:pop linear both;animation-timeline:view();animation-range:entry 0% entry 40%}
@keyframes pop{from{transform:scale(.7);opacity:.2}to{transform:none;opacity:1}}
.shot img{animation:parallaxy linear both;animation-timeline:view();animation-range:entry 0% exit 100%}
@keyframes parallaxy{from{object-position:50% 0%}to{object-position:50% 100%}}
}
@media(prefers-reduced-motion:reduce){.rv[data-rv]{transform:none;animation:none}.cue,.flabel{animation:none}.lz .shead h2,.pf b,.shot img{animation:none}}
.prog{position:absolute;left:0;top:0;height:3px;width:0;background:var(--acc);transition:width .1s linear}
.nlinks a{position:relative;padding-bottom:3px}
.nlinks a::after{content:"";position:absolute;left:0;right:100%;bottom:-2px;height:2px;background:var(--acc);transition:right .25s}
.nlinks a.active{color:#111}.nlinks a.active::after{right:0}
.skip{position:absolute;left:-999px;top:8px;z-index:100;background:var(--acc);color:#fff;padding:8px 14px;border-radius:8px}
.skip:focus{left:12px}
:focus-visible{outline:3px solid var(--acc);outline-offset:3px;border-radius:6px}
@media(prefers-reduced-motion:reduce){.rv{opacity:1;transform:none;transition:none}.glow::before,.glow::after,.unmute,.mq-track,.cursor{animation:none!important}html{scroll-behavior:auto}}
nav{position:fixed;top:0;left:0;right:0;z-index:50;background:rgba(255,255,255,.55);-webkit-backdrop-filter:blur(16px) saturate(160%);backdrop-filter:blur(16px) saturate(160%);border-bottom:1px solid rgba(255,255,255,.7);box-shadow:0 4px 24px rgba(0,0,0,.05);color:#111}
html[data-theme=light] nav{background:rgba(247,246,244,.8);border-color:var(--line)}
nav .wrap{display:flex;align-items:center;gap:22px;height:64px}
.logo{font-weight:800;font-size:17px}
.logo i{color:var(--acc);font-style:normal}
.nlinks{display:flex;gap:24px;margin-left:auto;font-size:13px;color:#555}
.nlinks a:hover{color:var(--txt)}
.hire{margin-left:18px;background:var(--acc);color:#fff;border-radius:99px;padding:8px 18px;font-size:13px;font-weight:600}
html[data-theme=light] .hire{background:#111;color:#fff}
.tgl{margin-left:10px;border:1px solid rgba(255,255,255,.25);background:transparent;color:var(--txt);border-radius:99px;width:34px;height:34px;cursor:pointer;font-size:15px}
html[data-theme=light] .tgl{border-color:var(--line)}
.hero{position:relative;min-height:100svh;display:flex;align-items:center;overflow:hidden;background:#f4f4f6}
.hero video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0}
.hero .shade{position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(255,255,255,.92) 0%,rgba(255,255,255,.72) 42%,rgba(255,255,255,.05) 100%)}
.hero .hcontent{position:relative;z-index:2;padding:110px 0 90px}
.hero h1{color:#111;font-size:clamp(38px,5.4vw,64px);font-weight:900;line-height:1.06;letter-spacing:-.02em;margin-bottom:18px;max-width:680px}
.hero h1 .rot{color:var(--acc);display:inline-block;min-width:8ch;white-space:nowrap;transition:opacity .3s,filter .3s}
.hero h1 .rot.sw{opacity:0;filter:blur(8px)}
.hero h1 .rot .dud{opacity:.35}
.kt span{display:inline-block;opacity:0;transform:translateY(.6em) rotate(3deg);animation:rise .7s cubic-bezier(.2,.7,.2,1) forwards}
@keyframes rise{to{opacity:1;transform:none}}
.uline{display:block;height:4px;width:0;background:var(--acc);border-radius:2px;margin-top:10px;animation:draw 1.1s .9s cubic-bezier(.2,.7,.2,1) forwards}
@keyframes draw{to{width:10ch}}
@media(prefers-reduced-motion:reduce){.kt span{opacity:1;transform:none;animation:none}.uline{width:10ch;animation:none}}
.hero p.sub{color:#333;font-size:16px;max-width:470px;margin-bottom:30px}
.cta{display:flex;gap:12px}
.btn{border-radius:99px;padding:12px 26px;font-size:14px;font-weight:600}
.btn.light{background:var(--acc);color:#fff}
.btn.ghosty{background:rgba(255,255,255,.55);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.75);color:#111;box-shadow:0 6px 20px rgba(0,0,0,.06)}
.unmute{animation:pulse 1.6s ease-in-out infinite;position:absolute;right:34px;bottom:30px;z-index:3;display:flex;align-items:center;gap:8px;background:rgba(23,111,125,.85);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.5);color:#fff;border-radius:99px;padding:10px 18px;font:600 12px/1 'JetBrains Mono',monospace;letter-spacing:.12em;cursor:pointer}
.ainote{position:absolute;left:34px;bottom:24px;z-index:3;color:#777;font:400 10px/1 'JetBrains Mono',monospace;letter-spacing:.1em}
section{padding:100px 0}
.lz{--bg:#fff;--surf:#fff;--line:#e3e3ea;--txt:#111;--mut:#666;background:#fff;color:#111;background-image:linear-gradient(rgba(128,128,128,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(128,128,128,.045) 1px,transparent 1px);background-size:80px 80px}
.lz .pill{background:rgba(255,255,255,.6);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);color:#444}
.lz .icon img{filter:invert(1)}
.lz .shot{border-color:#e3e3ea;background:#f2f2f5}
.lz .ev{background:rgba(23,111,125,.06)}
.lz .shead h2{display:inline-block;border-bottom:4px solid rgba(23,111,125,.35)}
.lz .glow::before{opacity:.35}.lz .glow::after{opacity:.06}
#about{background:var(--acc);color:#fff}
#about .hello{color:#fff}
#about h2{color:#fff}
#about>div>div>p{color:rgba(255,255,255,.92)}
#about .stat{background:rgba(255,255,255,.14);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);border-color:rgba(255,255,255,.4);box-shadow:0 8px 24px rgba(0,0,0,.12)}#about .stat b{color:#fff}#about .stat span{color:rgba(255,255,255,.85)}
#about .pcard{border-color:rgba(255,255,255,.4);box-shadow:0 20px 50px rgba(0,0,0,.25)}
#about .stat.glow::before,#about .stat.glow::after{display:none}
.shead{margin-bottom:48px}
.shead .mono{display:block;color:var(--acc);margin-bottom:14px}
.shead h2{font-size:clamp(28px,3.4vw,42px);font-weight:800;letter-spacing:-.02em}
.shead p{color:var(--mut);max-width:640px;margin-top:12px}
.center{text-align:center}
.center p{margin-left:auto;margin-right:auto}
.about{display:grid;grid-template-columns:320px 1fr;gap:56px;align-items:center}
.pcard{position:relative;border-radius:18px;overflow:hidden;border:1px solid var(--line)}
.pcard img{width:100%;display:block}
.badge{position:absolute;left:12px;right:12px;bottom:12px;display:flex;align-items:center;gap:8px;background:rgba(0,0,0,.45);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.15);border-radius:10px;padding:8px 11px;font:500 10px/1 'JetBrains Mono',monospace;letter-spacing:.1em;color:var(--grn)}
.dot{width:7px;height:7px;border-radius:50%;background:var(--grn);box-shadow:0 0 10px var(--grn)}
.hello{font-family:Caveat,cursive;font-size:34px;color:var(--acc)}
.about h2{font-size:clamp(28px,3vw,40px);font-weight:800;margin:6px 0 16px}
.about>div>p{color:var(--mut);max-width:640px}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:28px}
.stat{background:var(--surf);border:1px solid var(--line);border-radius:12px;padding:14px 15px}
.stat b{display:block;font-size:20px;font-weight:800}
.stat span{font:400 10px/1.4 'JetBrains Mono',monospace;color:var(--mut)}
.jquote{max-width:760px;margin:0 auto 54px;padding:26px 30px;border-radius:18px;text-align:center}
.jquote p{font-family:Caveat,cursive;font-size:30px;line-height:1.25;color:#111}
.jquote footer{margin-top:10px;font:400 11px/1.6 'JetBrains Mono',monospace;letter-spacing:.1em;color:var(--mut);text-transform:uppercase}
.jline{list-style:none;position:relative;max-width:900px;margin:0 auto;padding:10px 0}
.jline::before{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:linear-gradient(var(--acc),rgba(23,111,125,.15));transform:translateX(-50%)}
.jt{position:relative;width:50%;padding:0 44px 44px 0}
.jt:nth-child(even){margin-left:50%;padding:0 0 44px 44px}
.jdot{position:absolute;top:22px;right:-9px;width:18px;height:18px;border-radius:50%;background:#fff;border:4px solid var(--acc);box-shadow:0 0 0 6px rgba(23,111,125,.12)}
.jt:nth-child(even) .jdot{right:auto;left:-9px}
.jcard{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px 22px;box-shadow:0 10px 30px rgba(0,0,0,.05)}
.jyear{display:inline-block;font:700 11px/1 'JetBrains Mono',monospace;letter-spacing:.14em;color:var(--acc);border:1px solid rgba(23,111,125,.3);border-radius:99px;padding:6px 10px;margin-bottom:10px}
.jcard h3{font-size:17px;font-weight:800;line-height:1.3;margin-bottom:6px}
.jcard p{font-size:13.5px;color:var(--mut);line-height:1.6}
@media(max-width:760px){.jline::before{left:14px}.jt,.jt:nth-child(even){width:100%;margin-left:0;padding:0 0 30px 40px}.jdot,.jt:nth-child(even) .jdot{left:5px;right:auto}}
.roadmap{display:grid;grid-template-columns:1fr 1.15fr;gap:48px;align-items:start}
.rleft{position:sticky;top:96px}
.pilltag{display:inline-block;border:1px solid var(--line);background:#fff;border-radius:99px;padding:8px 16px;font-size:13px;font-weight:600;margin-bottom:22px;box-shadow:0 4px 14px rgba(0,0,0,.05)}
.rleft h2{font-size:clamp(34px,4.2vw,54px);font-weight:900;line-height:1.05;letter-spacing:-.03em;margin-bottom:18px}
.rleft p{color:var(--mut);font-size:17px;max-width:460px}
.rleft .note{text-align:left;margin-top:30px}
.rright{position:relative;display:flex;flex-direction:column;gap:88px;padding:20px 0 20px}
.rpath{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;overflow:visible}
.pin{position:relative;width:min(330px,88%);background:#fff;border:1px solid var(--line);border-radius:22px;padding:34px 26px 28px;box-shadow:0 18px 40px rgba(0,0,0,.08);transition:transform .35s cubic-bezier(.2,.7,.2,1),box-shadow .35s}
.pin.r1,.pin.r3{align-self:flex-end;transform:rotate(var(--rot))}.pin.r2,.pin.r4{align-self:flex-start;transform:rotate(var(--rot))}
.pin:hover{box-shadow:0 26px 60px rgba(0,0,0,.14)}
.pin.solid{background:var(--acc);color:#fff;border-color:var(--acc);box-shadow:0 22px 50px rgba(23,111,125,.35)}
.pin.solid .xnum,.pin.solid h3{color:#fff}.pin.solid p{color:rgba(255,255,255,.92)}
.tack{position:absolute;top:12px;left:50%;transform:translateX(-50%);width:18px;height:18px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#fff,#bdbdc4 60%,#8a8a92);box-shadow:0 3px 6px rgba(0,0,0,.25),inset 0 0 0 3px rgba(255,255,255,.35)}
.pin .xnum{font:italic 700 16px/1 Georgia,serif;letter-spacing:.06em;margin-bottom:12px}
.pin h3{font-size:24px;font-weight:800;line-height:1.15;margin-bottom:12px;letter-spacing:-.02em}
.pin p{font-size:15px;line-height:1.7;color:#555}

.pin.r1{--rot:2deg}.pin.r2{--rot:-2deg}.pin.r3{--rot:1deg}.pin.r4{--rot:-1deg}
.pin.rv{opacity:0;transition:opacity .7s ease,transform .7s cubic-bezier(.2,.7,.2,1)}
.pin.rv[data-rv=right]{transform:translateX(90px) rotate(var(--rot))}.pin.rv[data-rv=left]{transform:translateX(-90px) rotate(var(--rot))}
.pin.rv.in,.pin.rv.in[data-rv=right],.pin.rv.in[data-rv=left]{opacity:1;transform:rotate(var(--rot))}
.pin.rv.in:hover{transform:rotate(0)}
@media(max-width:980px){.roadmap{grid-template-columns:1fr}.rleft{position:static}.rright{gap:44px}}
@media(max-width:640px){.pin,.pin.r1,.pin.r2,.pin.r3,.pin.r4{--rot:0deg;align-self:center!important;width:100%}.rpath{display:none}}
.bigk{margin-top:auto;padding-top:18px;display:flex;align-items:baseline;gap:10px}.bigk b{font-size:64px;font-weight:900;line-height:1;color:var(--acc);letter-spacing:-.04em}.bigk small{font:500 11px/1 'JetBrains Mono',monospace;color:var(--mut);letter-spacing:.14em;text-transform:uppercase}
.pipe{display:flex;align-items:center;gap:8px;margin-top:16px;flex-wrap:wrap}.pipe span{font:600 10px/1 'JetBrains Mono',monospace;letter-spacing:.14em;border:1px solid var(--line);border-radius:99px;padding:7px 12px;background:#fff}.pipe i{flex:1;min-width:24px;height:2px;background:linear-gradient(90deg,var(--acc),rgba(23,111,125,.15));position:relative}.pipe i::after{content:"";position:absolute;right:-1px;top:-3px;width:8px;height:8px;border-radius:50%;background:var(--acc)}
.xcard{background:var(--surf);border:1px solid var(--line);border-radius:16px;padding:26px 22px}
.xnum{font:700 15px/1 'JetBrains Mono',monospace;color:var(--acc);margin-bottom:14px}
.xcard h3{font-size:17px;font-weight:700;margin-bottom:10px}
.xcard p{font-size:13px;color:var(--mut);line-height:1.6}
.note{font-family:Caveat,cursive;font-size:30px;color:var(--acc);text-align:center;margin-top:44px}
.sgroup{margin-bottom:40px}
.sgroup h3{font-size:15px;font-weight:700;color:var(--mut);margin-bottom:18px;text-align:center;letter-spacing:.04em;text-transform:uppercase}
.igrid{display:flex;flex-wrap:wrap;justify-content:center;gap:14px}
.icon{width:132px;background:var(--surf);border:1px solid var(--line);border-radius:14px;padding:18px 10px;display:flex;flex-direction:column;align-items:center;gap:10px;transition:transform .2s,border-color .2s}
.icon:hover{transform:translateY(-4px);border-color:var(--acc)}
.icon img{width:44px;height:44px;object-fit:contain}
html[data-theme=light] .icon img{filter:invert(1)}
.icon span{font:500 11px/1.2 'JetBrains Mono',monospace;color:var(--mut);text-align:center}
.icon.noico img{display:none}
.pgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.proj{background:var(--surf);border:1px solid var(--line);border-radius:16px;padding:16px;display:flex;flex-direction:column}
.shot{border-radius:11px;overflow:hidden;border:1px solid var(--line);margin-bottom:15px;aspect-ratio:720/380;background:#0a0a0a}
.shot img{width:100%;height:100%;object-fit:cover;object-position:top;display:block;opacity:.94;transition:filter .5s}.shot img.lq{filter:blur(14px);transform:scale(1.06)}
.shot.noimg{display:flex;align-items:center;justify-content:center;background:radial-gradient(circle at 50% 40%,rgba(23,111,125,.12),transparent 68%)}
.shot.noimg span{font:500 13px/1 'JetBrains Mono',monospace;color:var(--mut)}
.cat{font:600 10px/1 'JetBrains Mono',monospace;letter-spacing:.16em;color:var(--acc);margin-bottom:9px}
.proj h3{font-size:19px;font-weight:700;margin-bottom:8px}
.proj>p{font-size:13px;color:var(--mut);line-height:1.55;flex:1}
.ev{margin-top:12px;border-left:2px solid var(--acc);background:rgba(23,111,125,.07);border-radius:0 8px 8px 0;padding:9px 12px;font-size:12px;font-weight:600}
.tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.pill{border:1px solid var(--line);background:var(--bg);border-radius:99px;padding:5px 11px;font:500 10px/1 'JetBrains Mono',monospace;color:var(--mut);white-space:nowrap}
.visit{margin-top:14px;font:600 12px/1 'JetBrains Mono',monospace;color:var(--acc)}
.syslog{margin-top:64px}
.syslog h3{font-size:20px;font-weight:800;margin-bottom:18px}
.lrow{display:flex;align-items:center;justify-content:space-between;gap:16px;border:1px solid var(--line);border-radius:12px;background:var(--surf);padding:14px 18px;margin-bottom:10px;transition:border-color .2s}
.lrow:hover{border-color:var(--acc)}
.lrow b{display:block;font-size:14.5px}
.lrow span{font-size:12px;color:var(--mut)}
.lrow em{font:500 10px/1 'JetBrains Mono',monospace;font-style:normal;color:var(--acc);border:1px solid var(--line);border-radius:99px;padding:5px 11px;white-space:nowrap}
.logline{margin-top:16px;font:400 11px/1 'JetBrains Mono',monospace;color:var(--mut)}
.cursor{display:inline-block;width:7px;height:12px;background:var(--acc);vertical-align:-2px;animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(23,111,125,.55)}50%{box-shadow:0 0 0 12px rgba(23,111,125,0)}}
#certifications{background:#fff;color:#111;background-image:linear-gradient(#f0f0f3 1px,transparent 1px),linear-gradient(90deg,#f0f0f3 1px,transparent 1px);background-size:72px 72px}
#certifications .shead h2{color:#111;display:inline-block;border-bottom:4px solid rgba(23,111,125,.35)}
#certifications .shead{display:flex;align-items:flex-end;justify-content:space-between;text-align:left}
.arrows{display:flex;gap:10px}.arrows button{width:46px;height:46px;border-radius:50%;border:1px solid #ddd;background:#fff;color:#111;font-size:20px;cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.06)}
.cgrid{display:flex;gap:22px;overflow-x:auto;scroll-snap-type:x mandatory;padding:26px 4px 34px;scrollbar-width:none}
.cgrid::-webkit-scrollbar{display:none}
.flip{perspective:1100px;min-height:230px;flex:0 0 300px;scroll-snap-align:start}
.finner{position:relative;width:100%;height:100%;min-height:230px;border-radius:18px;transform-style:preserve-3d;transition:transform .6s}
.flip:hover .finner{transform:rotateY(180deg)}
.fface{position:absolute;inset:0;border-radius:18px;background:#fff;border:1px solid #e6e6ea;padding:20px;backface-visibility:hidden;display:flex;flex-direction:column;box-shadow:0 10px 30px rgba(0,0,0,.06)}
.ftop{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}
.fface h4{color:#111}
.issued{margin-top:auto;padding-top:12px;border-top:1px solid #eee;font-size:13px;color:#333}.issued small{display:block;font:500 9px/1 'JetBrains Mono',monospace;letter-spacing:.14em;color:#888;margin-bottom:4px}
.fback{background:#0b0b0d;color:#fff;border-color:#222;justify-content:center;gap:10px;transform:rotateY(180deg)}
.fback h4{color:#fff;flex:0;text-align:center;font-size:14px}
.fback small{font:500 9px/1 'JetBrains Mono',monospace;letter-spacing:.14em;color:#888}
.fback .vo{text-align:center}
.shield{color:var(--acc);font-size:16px}
.viewc{align-self:center;background:var(--acc);color:#fff;border-radius:99px;padding:10px 18px;font-weight:700;font-size:13px}
.fbot{display:flex;justify-content:space-between;align-items:center;margin-top:auto}.fbot b{font:700 10px/1 'JetBrains Mono',monospace;color:var(--acc);letter-spacing:.15em}

.chip{font:600 9px/1 'JetBrains Mono',monospace;letter-spacing:.14em;color:var(--acc);border:1px solid var(--line);border-radius:99px;padding:4px 9px}
.cnum{font:500 12px/1 'JetBrains Mono',monospace;color:#999}
.fface h4{font-size:15px;font-weight:700;line-height:1.35;flex:1}
.fface p{font-size:11.5px;color:var(--mut)}
.ver{font:700 13px/1 'JetBrains Mono',monospace;color:var(--grn);letter-spacing:.2em}
.fback a{font:600 11px/1 'JetBrains Mono',monospace;color:var(--acc)}
.fback a.viewc{color:#fff;font:700 13px/1 Inter,sans-serif}
.certnote{text-align:center;font-family:Caveat,cursive;font-size:24px;color:#777}
.introwrap{position:relative;max-width:860px;margin:0 auto;border-radius:16px;overflow:hidden;background:var(--surf);border:1px solid var(--line)}
.introwrap iframe{display:block;width:100%;aspect-ratio:16/9;border:0}
.loomfacade{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;width:100%;aspect-ratio:16/9;border:0;background:linear-gradient(135deg,#fff,#f3f3f6);cursor:pointer;font:600 14px/1 Inter,sans-serif;color:#111}.playbtn{width:72px;height:72px;border-radius:50%;background:var(--acc);color:#fff;display:flex;align-items:center;justify-content:center;font-size:26px;box-shadow:0 12px 30px rgba(23,111,125,.35)}
.intronote{text-align:center;margin-top:14px;font:400 12px/1.6 'JetBrains Mono',monospace;color:var(--mut)}
.contact{position:relative;overflow:hidden;background:#fff;color:#111}
.ghost{position:absolute;top:8px;left:50%;transform:translateX(-50%);font-size:clamp(70px,12vw,150px);font-weight:900;letter-spacing:-.04em;color:transparent;-webkit-text-stroke:1px #e6e6ea;white-space:nowrap;pointer-events:none}
.cgrid2{position:relative;display:grid;grid-template-columns:1.1fr .9fr;gap:0;margin-top:90px;background:var(--acc);border-radius:18px;overflow:hidden}
.form{padding:44px}.cinfo{padding:44px;background:rgba(0,0,0,.22);-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);border-left:1px solid rgba(255,255,255,.25)}
.form label{display:block;font:500 10px/1 'JetBrains Mono',monospace;letter-spacing:.14em;color:rgba(255,255,255,.8);margin:16px 0 7px;text-transform:uppercase}
.form .mono{color:#fff}
.form input,.form textarea{width:100%;background:transparent;border:0;border-bottom:1px solid rgba(255,255,255,.55);border-radius:0;color:#fff;padding:10px 2px;font:400 15px/1.5 Inter,sans-serif;outline:none}.form ::placeholder{color:rgba(255,255,255,.75)}
.form textarea{min-height:120px;resize:vertical}
.form button{margin-top:26px;background:#fff;color:#000;border:0;border-radius:99px;padding:12px 30px;font-weight:700;font-size:14px;cursor:pointer}
.form .consent{display:flex;gap:9px;align-items:flex-start;margin-top:18px;font:400 11px/1.6 'JetBrains Mono',monospace;letter-spacing:0;text-transform:none;color:rgba(255,255,255,.85);cursor:pointer}
.form .consent input{width:15px;height:15px;margin-top:2px;accent-color:#000;flex:0 0 auto}
.cinfo{font:400 12.5px/1.9 'JetBrains Mono',monospace;color:rgba(255,255,255,.85)}
.cinfo b{display:block;color:#fff;margin-bottom:4px;font-weight:600}
.cinfo .st{color:#fff;font-weight:700}
.cinfo>div{margin-bottom:22px}
.bigname{font-size:clamp(52px,10vw,118px);font-weight:900;letter-spacing:-.045em;line-height:.9;text-align:center;margin-top:70px;color:#111}
.foot{display:flex;justify-content:space-between;gap:16px;margin-top:44px;padding:20px 0 26px;border-top:1px solid var(--line);font:400 11.5px/1.7 'JetBrains Mono',monospace;color:var(--mut);flex-wrap:wrap}
.foot a{border-bottom:1px solid var(--line)}
@media(max-width:980px){.nlinks{display:none}.about,.cgrid2{grid-template-columns:1fr}.pgrid{grid-template-columns:1fr}.cgrid{grid-template-columns:1fr 1fr}.stats{grid-template-columns:1fr 1fr}.pcard{max-width:320px}
.pwrap{max-width:320px}.pcard{transform:rotate(-3deg);transition:transform .5s cubic-bezier(.2,.7,.2,1),box-shadow .5s}.pcard:hover{transform:rotate(0) scale(1.03);box-shadow:0 30px 60px rgba(0,0,0,.3)}
.dot{animation:pulse 1.6s ease-in-out infinite}@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.35;transform:scale(.7)}}
.atext.rv{transition-delay:200ms!important}}
"""

HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="preload" as="image" href=\"""" + HERO + """">
<title>Jade Patrick Mendoza &mdash; Executive Assistant | Executive Virtual Assistant &amp; SEO/AEO</title>
<meta name="description" content="Executive Assistant and Executive Virtual Assistant from Taguig City: calendar, inbox and meeting support for a Vice Mayor, financial account operations at Infosys BPM, six years of community leadership, plus SEO and AEO for WordPress. Open to remote work.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23000'/%3E%3Ctext x='28' y='44' font-family='Arial,sans-serif' font-size='26' font-weight='800' fill='%23fff' text-anchor='middle'%3EJM%3C/text%3E%3C/svg%3E">
<meta name="theme-color" content="#176f7d">
<meta property="og:type" content="website">
<meta property="og:title" content="Jade Patrick Mendoza &mdash; Executive Assistant / Executive Virtual Assistant">
<meta property="og:description" content="Executive support, financial account operations and SEO/AEO. Taguig City, open to remote work.">
<meta property="og:url" content="https://referrernation-web.github.io/jade/">
<meta property="og:image" content="https://referrernation-web.github.io/jade/assets/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&family=Caveat:wght@600&display=swap" rel="stylesheet">
<style>""" + CSS + """
/* ---- Clay + Skeuo layer (patch14) ---- */
:root{--clay-bg:linear-gradient(145deg,#ffffff 0%,#f3f3f7 100%);--clay-sh:0 18px 34px rgba(17,17,17,.10),0 4px 10px rgba(17,17,17,.06),inset 0 -6px 12px rgba(0,0,0,.06),inset 0 3px 6px rgba(255,255,255,.95);--clay-sh-hover:0 26px 46px rgba(23,111,125,.16),0 6px 14px rgba(0,0,0,.06),inset 0 -6px 12px rgba(0,0,0,.05),inset 0 3px 6px #fff}
.stat,.icon,.proj,.jcard,.fface,.pin,.pcard,.csdIn,.lrow{background:var(--clay-bg);border:1px solid rgba(255,255,255,.9);box-shadow:var(--clay-sh)}
.stat,.icon,.jcard,.lrow{border-radius:22px}.proj,.pin,.fface{border-radius:26px}
.stat.glow,.proj.glow,.icon.glow{border-color:rgba(255,255,255,.9)}
.hv:hover,.proj.tilt:hover,.pin.rv.in:hover{box-shadow:var(--clay-sh-hover);border-color:rgba(255,255,255,1)}
.pin.solid{background:linear-gradient(145deg,#1b8593,#125866);border-color:rgba(255,255,255,.25);box-shadow:0 22px 44px rgba(23,111,125,.35),inset 0 -8px 14px rgba(0,0,0,.28),inset 0 3px 6px rgba(255,255,255,.28)}
#about .stat{background:linear-gradient(145deg,rgba(255,255,255,.22),rgba(255,255,255,.10));border-color:rgba(255,255,255,.45);box-shadow:0 18px 34px rgba(0,0,0,.18),inset 0 -6px 12px rgba(0,0,0,.18),inset 0 3px 6px rgba(255,255,255,.35)}
.btn,.hire,.unmute,.viewc,.arrows button,.pilltag{box-shadow:0 10px 20px rgba(17,17,17,.12),inset 0 -4px 8px rgba(0,0,0,.18),inset 0 3px 5px rgba(255,255,255,.35)}
.btn.light,.hire{background:linear-gradient(180deg,#1b8593,#125866)}
.btn:not(.light){background:linear-gradient(180deg,#fff,#ececf1);color:#111}
.btn:active,.hire:active,.viewc:active{box-shadow:0 3px 8px rgba(17,17,17,.12),inset 0 4px 8px rgba(0,0,0,.22);transform:translateY(1px) scale(.98)!important}
.pill{background:linear-gradient(180deg,#fff,#f0f0f4);border-color:#fff;box-shadow:0 3px 6px rgba(0,0,0,.08),inset 0 -2px 3px rgba(0,0,0,.06),inset 0 1px 2px #fff;color:#444}
.icon img{filter:drop-shadow(0 6px 8px rgba(0,0,0,.18))}
.xnum,.cat{text-shadow:0 1px 0 #fff}
/* sticky notes (skeuomorphic) */
.note,.jquote{position:relative;font-family:Caveat,cursive;color:#3a2a00;background:linear-gradient(180deg,#fff5b0,#ffe98a);box-shadow:0 12px 22px rgba(0,0,0,.14),inset 0 -12px 18px rgba(0,0,0,.06);border:0;border-radius:4px 4px 6px 4px/4px 4px 10px 4px;display:inline-block;padding:16px 26px 20px;transform:rotate(-1.5deg)}
.note{font-size:28px;margin:44px auto 0;left:50%;transform:translateX(-50%) rotate(-1.5deg)}
.rleft .note{left:0;transform:rotate(1.5deg);margin-top:30px}
.jquote{display:block;max-width:760px;margin:0 auto 54px;transform:rotate(-1deg);backdrop-filter:none;-webkit-backdrop-filter:none}
.jquote p{color:#3a2a00}.jquote footer{color:#7a5a00}
.note::before,.jquote::before{content:"";position:absolute;top:-12px;left:50%;width:110px;height:26px;transform:translateX(-50%) rotate(-2deg);background:rgba(255,255,255,.55);border:1px solid rgba(0,0,0,.05);box-shadow:0 2px 4px rgba(0,0,0,.08);backdrop-filter:blur(2px)}
.note::after,.jquote::after{content:"";position:absolute;right:0;bottom:0;width:0;height:0;border-style:solid;border-width:0 0 22px 22px;border-color:transparent transparent #fff transparent;filter:drop-shadow(-2px -2px 2px rgba(0,0,0,.08))}
.jquote.rv.in,.note.rv.in{transform:rotate(-1deg)}
/* clay tack on pins gets a clay ball */
.tack{background:radial-gradient(circle at 35% 30%,#fff 0,#cfe8ec 35%,#176f7d 70%,#0c3d47 100%);box-shadow:0 4px 8px rgba(0,0,0,.28),inset 0 -3px 5px rgba(0,0,0,.25)}
@media(prefers-reduced-motion:reduce){.note,.jquote{transform:none}}

/* ---- Journey: spatial root-tree (patch15) ---- */
.jwrap{position:relative;max-width:960px;margin:0 auto;perspective:1400px}
.jtree{position:absolute;inset:0;width:100%;height:100%;overflow:visible;pointer-events:none;z-index:0}
.jtree #jtrunk{fill:none;stroke:url(#jg);stroke-width:7;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:1;transition:stroke-dashoffset 2.2s cubic-bezier(.2,.7,.2,1)}
.jtree #jbr path{fill:none;stroke:#176f7d;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:1;transition:stroke-dashoffset 1s cubic-bezier(.2,.7,.2,1)}
.jtree #jtw path{fill:none;stroke:#5fa9b5;stroke-width:1.6;stroke-linecap:round;opacity:.8;stroke-dasharray:1;stroke-dashoffset:1;transition:stroke-dashoffset .8s ease}
.jwrap.grow #jtrunk,.jwrap.grow #jbr path,.jwrap.grow #jtw path{stroke-dashoffset:0}
.jline{position:relative;z-index:1;max-width:none;padding:24px 0}
.jline::before{display:none}
.jt{padding:0 96px 58px 0}.jt:nth-child(even){padding:0 0 58px 96px}
.jdot{right:85px;width:22px;height:22px;border:5px solid var(--acc);background:radial-gradient(circle at 35% 30%,#fff,#dcefF2 60%,#bfe0e5);box-shadow:0 4px 8px rgba(23,111,125,.25),0 0 0 6px rgba(23,111,125,.10)}
.jt:nth-child(even) .jdot{left:85px}
.jcard{transform:rotateY(7deg);transform-origin:right center;transition:transform .5s cubic-bezier(.2,.7,.2,1),box-shadow .5s}
.jt:nth-child(even) .jcard{transform:rotateY(-7deg);transform-origin:left center}
.jt:hover .jcard{transform:rotateY(0) translateZ(24px) scale(1.02);box-shadow:var(--clay-sh-hover)}
@media(max-width:760px){.jt,.jt:nth-child(even){padding:0 0 34px 44px}.jcard,.jt:nth-child(even) .jcard{transform:none}.jdot,.jt:nth-child(even) .jdot{left:3px}}
@media(prefers-reduced-motion:reduce){.jtree #jtrunk,.jtree #jbr path,.jtree #jtw path{stroke-dashoffset:0;transition:none}.jcard,.jt:nth-child(even) .jcard{transform:none}}

/* ---- green glass tree + white leaves (patch16) ---- */
.jtree #jhalo{fill:none;stroke:#1fa3b3;stroke-width:22;stroke-linecap:round;opacity:.22;filter:url(#jglow)}
.jtree #jtrunk{stroke:url(#jg);stroke-width:8;opacity:.78}
.jtree #jbr path{stroke:#176f7d;opacity:.75}
.jtree #jtw path{stroke:#5fa9b5;opacity:.8}
.jtree .leaf{fill:rgba(255,255,255,.95);stroke:rgba(23,111,125,.75);stroke-width:1.4;transform-box:fill-box;transform-origin:0% 50%;transform:scale(0);transition:transform .6s cubic-bezier(.34,1.4,.4,1);filter:drop-shadow(0 3px 5px rgba(12,61,71,.22))}
.jtree .leaf.v{fill:rgba(255,255,255,.7)}
.jwrap.grow .leaf{transform:scale(1)}
.jdot{border-color:#176f7d;background:radial-gradient(circle at 35% 30%,#fff,#dcefF2 60%,#bfe0e5);box-shadow:0 4px 8px rgba(23,111,125,.28),0 0 0 6px rgba(23,111,125,.12)}
.jcard{border-color:rgba(255,255,255,.95)}
.jt .jcard::before{content:"";position:absolute;top:-10px;right:18px;width:34px;height:20px;border-radius:0 100% 0 100%;background:linear-gradient(135deg,#fff,#eef7f8);border:1px solid rgba(23,111,125,.35);box-shadow:0 2px 4px rgba(12,61,71,.15);transform:rotate(-20deg)}
.jt:nth-child(even) .jcard::before{right:auto;left:18px;transform:rotate(20deg) scaleX(-1)}
.jyear{color:var(--acc);border-color:rgba(23,111,125,.3)}

/* ---- Spatial UI layer (patch17) ---- */
@media (hover:hover) and (prefers-reduced-motion:no-preference){
.hero{perspective:1200px}
[data-depth]{transform:translate3d(calc(var(--px,0)*var(--d,0)*1px),calc(var(--py,0)*var(--d,0)*1px),0);transition:transform .25s cubic-bezier(.2,.7,.2,1);will-change:transform}
.hero .flabel,.hero .ainote{transform:translate3d(calc(var(--px,0)*14px),calc(var(--py,0)*14px),0);transition:transform .3s}
.hero .cue{transform:translate(-50%,0) translate3d(calc(var(--px,0)*10px),calc(var(--py,0)*10px),0)}
.sheen{position:relative}
.sheen::after{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;background:radial-gradient(260px circle at var(--mx,50%) var(--my,50%),rgba(255,255,255,.55),rgba(255,255,255,0) 60%);opacity:0;transition:opacity .3s;mix-blend-mode:screen;z-index:2}
.sheen:hover::after{opacity:1}
.pin.solid.sheen::after{background:radial-gradient(260px circle at var(--mx,50%) var(--my,50%),rgba(255,255,255,.35),rgba(255,255,255,0) 60%)}
.hv:hover,.hv:focus-visible{transform:translate3d(0,-6px,0) scale(1.02);box-shadow:0 30px 60px rgba(23,111,125,.18),0 8px 18px rgba(0,0,0,.08),inset 0 -6px 12px rgba(0,0,0,.05),inset 0 3px 6px #fff;border-color:#fff}
.rv[data-rv=z]{transform:perspective(1200px) rotateX(7deg) translateZ(-70px);transform-origin:50% 100%}
.rv.in[data-rv=z]{transform:none}
.badge,.flabel.tr{animation:sfloat 4.2s ease-in-out infinite}
@keyframes sfloat{0%,100%{translate:0 0}50%{translate:0 -4px}}
::view-transition-old(root){animation:vt-out .45s cubic-bezier(.2,.7,.2,1) both}
::view-transition-new(root){animation:vt-in .45s cubic-bezier(.2,.7,.2,1) both}
@keyframes vt-out{to{transform:scale(.97);opacity:.6}}
@keyframes vt-in{from{transform:scale(1.03);opacity:0}}
}
.stat,.proj,.pin,.jcard,.icon,.fface,.pcard,.lrow{box-shadow:var(--clay-sh),inset 1px 1px 0 rgba(255,255,255,.95)}
.badge{position:absolute;left:-10px;bottom:-12px;box-shadow:0 12px 24px rgba(0,0,0,.35),0 2px 4px rgba(0,0,0,.2)}
.pcard{overflow:visible}.pcard img{border-radius:18px}
.flabel.tr{right:-6px;top:84px}
body.modal-open .hero video,body.modal-open .proofband{filter:blur(6px) saturate(.8)}
.dock{position:fixed;top:auto;right:auto;left:50%;bottom:18px;transform:translateX(-50%);border-bottom:0;z-index:60;display:flex;gap:2px;padding:6px;border-radius:99px;background:rgba(255,255,255,.62);-webkit-backdrop-filter:blur(18px) saturate(160%);backdrop-filter:blur(18px) saturate(160%);border:1px solid rgba(255,255,255,.85);box-shadow:0 20px 50px rgba(0,0,0,.16),0 2px 6px rgba(0,0,0,.06),inset 0 1px 0 #fff}
.dock a{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;gap:1px;width:64px;padding:7px 0 6px;border-radius:99px;color:#444;font:600 12px/1 Inter,system-ui,sans-serif;transition:color .25s,transform .25s}
.dock a>span{font-size:9px;letter-spacing:.04em;opacity:.85}
.dock a:hover{transform:translateY(-4px) scale(1.06);color:#111}
.dock a.active{color:#fff}
.dsel{position:absolute;top:6px;left:6px;height:calc(100% - 12px);width:64px;border-radius:99px;background:linear-gradient(180deg,#1b8593,#125866);box-shadow:0 8px 18px rgba(23,111,125,.35),inset 0 1px 0 rgba(255,255,255,.35);transition:left .4s cubic-bezier(.2,.7,.2,1),width .4s;z-index:0}
@media(max-width:980px){.dock{display:none}}
@media(prefers-reduced-motion:reduce){.dock a:hover{transform:none}.badge,.flabel.tr{animation:none}}

/* ---- mascot game (patch18) ---- */
.pin .ledge{position:absolute;left:6px;right:6px;top:-7px;height:11px;border-radius:8px;background:linear-gradient(180deg,#fff,#efe3e5);border:1px solid rgba(255,255,255,.95);box-shadow:0 5px 10px rgba(23,111,125,.18),inset 0 -3px 5px rgba(0,0,0,.08),inset 0 1px 0 #fff;transform:rotate(calc(var(--rot,0deg)*-1))}
.pin.solid .ledge{background:linear-gradient(180deg,#1b8593,#176f7d);border-color:rgba(255,255,255,.35)}
.pin .tack{top:-13px;z-index:2}
#mg{position:absolute;inset:0;pointer-events:none;z-index:5;overflow:visible}
.mg-spr{position:absolute;background-repeat:no-repeat;will-change:transform;backface-visibility:hidden;transform-style:preserve-3d;image-rendering:auto;contain:layout style}
.mg-sh{position:absolute;background:radial-gradient(ellipse,rgba(12,61,71,.28),transparent 70%);border-radius:50%;width:64px;height:11px;transform:translateX(-50%)}
.mg-tag{position:absolute;left:0;top:0;background:rgba(255,255,255,.94);border:1px solid rgba(23,111,125,.3);border-radius:99px;padding:4px 10px;font:700 10px/1 'JetBrains Mono',monospace;color:var(--acc);box-shadow:0 8px 18px rgba(0,0,0,.12);white-space:nowrap;opacity:0;transition:opacity .4s;will-change:transform}
#mg.tagon .mg-tag{opacity:1}
.mg-dust,.mg-spark{position:absolute;width:7px;height:7px;border-radius:50%;background:rgba(95,169,181,.5);animation:mgpuff .5s ease-out forwards;pointer-events:none}
.mg-spark{width:4px;height:4px;background:rgba(200,140,90,.85)}
@keyframes mgpuff{to{transform:translate(var(--dx),var(--dy,-14px)) scale(.2);opacity:0}}
@media(max-width:700px){#mg{display:none}}

.mg-bub{position:absolute;left:0;top:0;max-width:220px;background:rgba(255,255,255,.96);border:1px solid rgba(23,111,125,.3);border-radius:14px 14px 14px 4px;padding:8px 11px;font:600 12px/1.35 Inter,system-ui,sans-serif;color:#111;box-shadow:0 10px 24px rgba(0,0,0,.14);opacity:0;transform:translateY(6px);transition:opacity .25s,transform .25s;pointer-events:none;will-change:transform}
.mg-bub.on{opacity:1;transform:translateY(0)}
.mg-tag{pointer-events:auto;cursor:pointer}
.mg-bub.pup{border-radius:14px 14px 4px 14px;font-size:11px;padding:6px 9px}.mg-tag2{font-size:9px;padding:3px 8px;pointer-events:none;cursor:default}
.mg-play-off{display:inline-flex;align-items:center;gap:8px;margin-top:14px;padding:9px 16px;border-radius:99px;border:1px solid rgba(23,111,125,.3);background:linear-gradient(180deg,#fff,#f3eef0);color:var(--acc);font:700 12px/1 'JetBrains Mono',monospace;letter-spacing:.06em;cursor:pointer;box-shadow:0 8px 18px rgba(23,111,125,.12),inset 0 1px 0 #fff}
.mg-play-off:hover{transform:translateY(-2px)}
.mg-play-off.on{background:linear-gradient(180deg,#1b8593,#125866);color:#fff}
@media(max-width:700px){.mg-play-off{display:none}}
</style></head><body>

<a class="skip" href="#about">Skip to content</a>
<nav><div class="prog" id="prog"></div><div class="wrap">
  <span class="logo">Jade Mendoza<i> .</i></span>
  <div class="nlinks"><a href="#home">Home</a><a href="#about">About</a><a href="#journey">Journey</a><a href="#expertise">Expertise</a><a href="#skills">Skills</a><a href="#projects">Projects</a><a href="#certifications">Certifications</a><a href="#contact">Contact</a><span class="slide" id="slide"></span></div>
  <a class="hire" href="#contact">Hire Me</a>
  
</div></nav>
<nav class="dock" id="dock" aria-label="Sections"><a href="#home" title="Home">&#8962;<span>Home</span></a><a href="#about" title="About">&#9786;<span>About</span></a><a href="#journey" title="Journey">&#10148;<span>Journey</span></a><a href="#expertise" title="Expertise">&#9733;<span>Expertise</span></a><a href="#skills" title="Skills">&#9881;<span>Skills</span></a><a href="#projects" title="Projects">&#9638;<span>Projects</span></a><a href="#certifications" title="Certifications">&#10004;<span>Certs</span></a><a href="#contact" title="Contact">&#9993;<span>Contact</span></a><span class="dsel" id="dsel"></span></nav>

<header class="hero" id="home">
  <video id="reel" data-depth="-6"\"""" + (" src=\"" + INTRO + "\"" if INTRO else "") + """ poster=\"""" + HERO + """" muted autoplay loop playsinline preload="metadata"></video>
  <div class="shade"></div><div class="spot" id="spot"></div>
  <div class="wrap hcontent" data-depth="8">
    <h1><span class="kt" id="kt">Hi, I&rsquo;m Jade, an</span><br><span class="rot" id="rot" aria-live="polite">Executive Assistant</span><span class="uline"></span></h1>
    <p class="sub">I keep executive operations moving: calendars, inboxes, briefings and follow-through, with the discretion of financial account work. Second track: SEO and AEO for WordPress sites.</p>
    <div class="cta"><a class="btn light" href="#projects">View My Work</a><a class="btn ghosty" href="world/" title="3D resume: drive a jeepney across the wonders of the world">&#127758; Ride the 3D World</a><a class="btn ghosty" href="assets/Jade-Patrick-Mendoza-Resume-2026.pdf" target="_blank" rel="noopener">Resume PDF</a></div>
  </div>
  <span class="flabel tr">// Executive Assistant &middot; SEO &middot; AEO<br>Open to remote work</span>
  <span class="flabel bl">// Taguig City &rarr; remote<br>English &middot; Tagalog</span>
  <a class="cue" href="#about" aria-label="Scroll down">&#8964;</a>
  <span class="ainote">""" + ("APPLICATION INTRO &middot; RESUME FACTS BELOW" if INTRO else "INTRO VIDEO IN PRODUCTION &middot; RESUME FACTS BELOW") + """</span>
  """ + ('<button class="unmute" id="unmute">&#128266; UNMUTE INTRO</button>' if INTRO else "") + """
</header>

<div class="proofband" aria-label="Evidence highlights"><div class="mq-track"><span class="pf"><b>2+</b>years in customer &amp; financial account operations</span><span class="pf"><b>6</b>years of community youth leadership</span><span class="pf"><b>Vice Mayor</b>executive assistant, LGU Mansalay, 2023</span><span class="pf"><b>Infosys BPM</b>senior process executive, 2024 to present</span><span class="pf"><b>EN &middot; TL</b>English and Tagalog</span><span class="pf"><b>BSIS</b>Clarendon College</span><span class="pf"><b>Remote</b>Taguig City, open to remote work</span><span class="pf"><b>2+</b>years in customer &amp; financial account operations</span><span class="pf"><b>6</b>years of community youth leadership</span><span class="pf"><b>Vice Mayor</b>executive assistant, LGU Mansalay, 2023</span><span class="pf"><b>Infosys BPM</b>senior process executive, 2024 to present</span><span class="pf"><b>EN &middot; TL</b>English and Tagalog</span><span class="pf"><b>BSIS</b>Clarendon College</span><span class="pf"><b>Remote</b>Taguig City, open to remote work</span></div></div>
<section id="about"><div class="wrap about">
  <div class="pwrap" data-rv="drop"><div class="pcard glow">
    <img src=\"""" + ABOUT + """" alt="Jade Patrick Mendoza" loading="lazy" decoding="async" width="720" height="720">
    <div class="badge"><span class="dot"></span>OPEN TO REMOTE WORK</div>
  </div></div>
  <div class="atext" data-rv="left">
    <span class="hello">Hello!</span>
    <h2>I&rsquo;m Jade Patrick Mendoza</h2>
    <p>A detail-oriented administrative professional in Taguig City, experienced in supporting executive operations, managing high-volume communications and coordinating time-sensitive follow-through. Hands-on experience supporting a Vice Mayor, 2+ years in customer and financial account operations, and 6 years of community leadership. Trusted to anticipate needs, handle confidential information, prepare decision-ready materials and keep priorities moving across distributed teams.</p>
    <div class="stats">
      <div class="stat glow hv" data-rv="drop"><b data-count="2" data-suffix="+">2+</b><span>years in customer &amp; financial account operations</span></div>
      <div class="stat glow hv" data-rv="drop"><b data-count="6">6</b><span>years of community youth leadership</span></div>
      <div class="stat glow hv" data-rv="drop"><b data-count="1">1</b><span>Vice Mayor supported, LGU Mansalay</span></div>
      <div class="stat glow"><b>EN &middot; TL</b><span>English and Tagalog</span></div>
    </div>
  </div>
</div></section>

<section id="journey" class="lz"><div class="wrap">
  <div class="shead center"><span class="mono">CAREER JOURNEY</span><h2>From Youth Leader to Executive Support</h2>
  <p>Community programs first, then a Vice Mayor&rsquo;s office, then regulated financial accounts. The same habit at every stop: anticipate, document, follow through.</p></div>
  <blockquote class="jquote glass" data-rv="zoom"><p>&ldquo;Trusted to anticipate needs, handle confidential information, prepare decision-ready materials and keep priorities moving across distributed teams.&rdquo;</p><footer>&mdash; the summary line on the resume, and the standard for every task</footer></blockquote>
  <div class="jwrap"><svg class="jtree" id="jtree" aria-hidden="true"><defs><linearGradient id="jg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#176f7d"/><stop offset="1" stop-color="#8fc4cc"/></linearGradient><filter id="jglow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="6"/></filter></defs><path id="jhalo" d=""/><path id="jtrunk" d=""/><g id="jbr"></g><g id="jtw"></g><g id="jlv"></g></svg><ol class="jline"><li class="jt" data-rv="left"><span class="jdot"></span><div class="jcard hv"><span class="jyear">College</span><h3>BS Information Systems, Clarendon College</h3><p>Systems thinking that became process discipline.</p></div></li><li class="jt" data-rv="right"><span class="jdot"></span><div class="jcard hv"><span class="jyear">6 years</span><h3>Youth Leader, Community Youth Organization</h3><p>Led and organized community youth programs: schedules, logistics, resources, event activities and stakeholder coordination.</p></div></li><li class="jt" data-rv="left"><span class="jdot"></span><div class="jcard hv"><span class="jyear">2023</span><h3>Executive Assistant to the Vice Mayor, LGU Mansalay, Oriental Mindoro</h3><p>Jul&ndash;Dec 2023. Daily calendar, official correspondence, briefing materials, meeting notes and research summaries for the office.</p></div></li><li class="jt" data-rv="right"><span class="jdot"></span><div class="jcard hv"><span class="jyear">2024</span><h3>Customer Service Representative, Telco Account, Alorica / Probe CX</h3><p>Feb&ndash;Jun 2024. Billing, promotion and connectivity concerns; product recommendations; proactive guidance.</p></div></li><li class="jt" data-rv="left"><span class="jdot"></span><div class="jcard hv"><span class="jyear">2024&ndash;</span><h3>Senior Process Executive, Infosys BPM</h3><p>Jul 2024 to present. High-volume financial account communications under regulatory controls, precise records, mentoring new hires with Training and Quality.</p></div></li><li class="jt" data-rv="right"><span class="jdot"></span><div class="jcard hv"><span class="jyear">Next</span><h3>SEO &amp; AEO, second track</h3><p>Keyword and entity research, on-page optimization, schema and WordPress technical health. Case studies on request.</p></div></li></ol></div>
  <div class="note">Next: your calendar.</div>
</div></section>

<section id="expertise" class="lz"><div class="wrap roadmap">
  <div class="rleft">
    <span class="pilltag">My Expertise</span>
    <h2>Keeping Executive Operations Moving</h2>
    <p>Calendar, inbox, meetings and follow-through, handled with the accuracy of financial account work. One assistant, four things covered.</p>
    <div class="note">Anticipate, document, follow through.</div>
    <button class="mg-play" id="mgplay" type="button">&#9654; WATCH JADE PLAY</button>
  </div>
  <div class="rright" id="rright">
    <svg class="rpath" id="rpath" aria-hidden="true"><defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#111"/></marker></defs><path id="rline" d="" fill="none" stroke="#111" stroke-width="1.5" stroke-dasharray="5 6" marker-end="url(#arr)"/></svg>
    """ + expertise_html + """
  </div>
</div></section>

<section id="skills" class="lz"><div class="wrap">
  <div class="shead center"><span class="mono">TECHNICAL STACK</span><h2>Tools &amp; Systems I Work With</h2>
  <p>Executive support, AI productivity and the SEO stack for WordPress sites.</p></div>
  """ + skills_html + """
</div></section>

<section id="projects" class="lz"><div class="wrap">
  <div class="shead center"><span class="mono">FEATURED WORK</span><h2>Work That Defines the Journey</h2>
  <p>Each card is a role from the resume: what the office needed, what I did, what it produced.</p></div>
  <div class="pgrid">""" + feat_html + """</div>
  <div class="syslog">
    <h3>Education, Languages &amp; Logistics</h3>
    """ + syslog_html + """
    <div class="logline">Reviewing priorities continuous<span class="cursor"></span></div>
  </div>
</div></section>

<section id="certifications"><div class="wrap">
  <div class="shead"><div><span class="mono">SYSTEM BADGES</span><h2>Strengths &amp; Competencies</h2></div><div class="arrows"><button id="cprev" aria-label="Previous">&#8249;</button><button id="cnext" aria-label="Next">&#8250;</button></div></div>
  <div class="cgrid" id="cgrid">""" + certs_html + """</div>
  <div class="certnote">Hover a card to flip and verify &bull; Total of """ + str(len(CERTS)) + """ strengths and competencies from the resume.</div>
</div></section>

<section id="intro" class="lz"><div class="wrap">
  <div class="shead center"><span class="mono">INTRO TRANSMISSION</span><h2>Meet Me in Forty Seconds</h2></div>
  <div class="introwrap glow" id="loomwrap">""" + ('<video src="' + INTRO + '" poster="' + HERO + '" controls playsinline preload="metadata" style="width:100%;height:100%;object-fit:cover;background:#000"></video>' if INTRO else '<button class="loomfacade" id="loomplay" aria-label="Intro video in production" type="button" disabled><span class="playbtn">&#9654;</span><span>Application intro: in production</span></button>') + """</div>
  <p class="intronote">""" + ("Who I am, what I handle, and what to do next." if INTRO else "Recording this week. The resume above does not wait.") + """</p>
</div></section>

<dialog id="csd" class="csd" aria-labelledby="csdTitle"><div class="csdIn glass"><button class="csdX" id="csdX" aria-label="Close">&times;</button><div class="csdShot" id="csdShot"></div><div class="csdBody"><div class="cat" id="csdCat"></div><h3 id="csdTitle"></h3><p id="csdDesc"></p><div class="ev" id="csdEv"></div><div class="tags" id="csdTags"></div><a class="btn light" id="csdUrl">See the journey &rarr;</a></div></div></dialog>
<section class="contact" id="contact"><div class="wrap">
  <div class="ghost">CONTACT</div>
  <div class="cgrid2">
    <form class="form" id="cform" action="https://formsubmit.co/jademendoza.va@gmail.com" method="POST">
      <span class="mono red">REACH ME</span>
      <input type="hidden" name="_subject" value="Inquiry &mdash; referrernation-web.github.io/jade">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_next" value="https://referrernation-web.github.io/jade/#contact">
      <label for="fn">Name</label><input id="fn" name="name" required placeholder="Your name">
      <label for="fe">Email</label><input id="fe" name="email" type="email" required placeholder="you@company.com">
      <label for="fm">Message</label><textarea id="fm" name="message" required placeholder="The role, the hours, what needs handling."></textarea>
      <label class="consent"><input type="checkbox" required checked> I give permission to be contacted at this email address.</label>
      <button type="submit">Send</button>
    </form>
    <div class="cinfo">
      <div><b>// Executive Assistant</b>Executive Virtual Assistant<br>SEO &amp; AEO, second track</div>
      <div><b>// Status</b><span class="st">Open to remote work</span><br>Fort Bonifacio, Taguig City, Philippines</div>
      <div><b>// Direct</b><a href="mailto:jademendoza.va@gmail.com">jademendoza.va@gmail.com</a><br>+63 908 763 2587</div>
      <div><b>// Resume</b><a href="assets/Jade-Patrick-Mendoza-Resume-2026.pdf" target="_blank" rel="noopener">Download PDF</a></div>
      <div><b>// Verify</b><a href="https://www.linkedin.com/in/jadepatrickmendoza" target="_blank" rel="noopener">LinkedIn</a></div>
    </div>
  </div>
  <div class="bigname">JADE MENDOZA</div>
  <div class="foot">
    <div>Contact Transmission<br>jademendoza.va@gmail.com &middot; +63 908 763 2587</div>
    <div><a href="https://www.linkedin.com/in/jadepatrickmendoza">LinkedIn</a> &middot; <a href="assets/Jade-Patrick-Mendoza-Resume-2026.pdf">Resume PDF</a> &middot; <a href="world/">3D World</a></div>
    <div>&copy; 2026 Jade Patrick Mendoza &middot; v1 &middot; September 2026</div>
  </div>
</div></section>

<script>
(function(){var v=document.getElementById('reel'),b=document.getElementById('unmute');if(!v||!b)return;function tg(){v.muted=!v.muted;if(!v.muted){v.currentTime=0;v.play();}b.innerHTML=v.muted?'&#128266; UNMUTE REEL':'&#128263; MUTE REEL';b.style.animation=v.muted?'':'none';}b.onclick=tg;v.onclick=tg;var once=function(e){if(e&&e.target&&(e.target===b||b.contains(e.target)))return;if(v.muted){tg();}document.removeEventListener('pointerdown',once,true);document.removeEventListener('keydown',once,true);};document.addEventListener('pointerdown',once,true);document.addEventListener('keydown',once,true);})();
(function(){var R=['Executive Assistant','Executive Virtual Assistant','Financial Account Specialist','SEO / AEO Specialist'],el=document.getElementById('rot'),i=0,rm=matchMedia('(prefers-reduced-motion:reduce)').matches;var G='ABCDEFGHJKLMNPQRSTUVWXYZ';function scramble(to){var from=el.textContent,len=Math.max(from.length,to.length),q=[],t0=performance.now(),tok=(el._tok=(el._tok||0)+1);for(var k=0;k<len;k++){var st=Math.random()*160,en=st+120+Math.random()*180;q.push({t:to[k]||'',s:st,e:en,c:''});}function step(){if(el._tok!==tok)return;var ms=performance.now()-t0,out='',done=0;for(var k=0;k<q.length;k++){var it=q[k];if(ms>=it.e){done++;out+=it.t;}else if(ms>=it.s){if(!it.c||Math.random()<.35)it.c=G[Math.floor(Math.random()*G.length)];out+='<span class="dud">'+it.c+'</span>';}else out+=(from[k]||'');}if(done<q.length&&ms<650){el.innerHTML=out;setTimeout(step,30);}else el.textContent=to;}step();}
setInterval(function(){i=(i+1)%R.length;if(rm){el.textContent=R[i];}else scramble(R[i]);},3600);})();
(function(){var els=document.querySelectorAll('.pwrap,.atext,.xcard,.pin,.jt,.jquote,.proj,.icon,.flip,.lrow,.stat,.shead,.introwrap,.cgrid2');var i=0;els.forEach(function(e){e.classList.add('rv');e.style.transitionDelay=((i++%6)*60)+'ms';});if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in')});return;}var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target);}});},{rootMargin:'0px 0px -8% 0px',threshold:.08});els.forEach(function(e){io.observe(e)});})();
(function(){if(matchMedia('(prefers-reduced-motion:reduce)').matches)return;var els=document.querySelectorAll('[data-count]');var io=new IntersectionObserver(function(en){en.forEach(function(x){if(!x.isIntersecting)return;var b=x.target;io.unobserve(b);var to=parseFloat(b.dataset.count),dec=parseInt(b.dataset.dec||'0'),pre=b.dataset.prefix||'',suf=b.dataset.suffix||'',t0=null;var fin=pre+(dec?to.toFixed(dec):Math.round(to).toLocaleString())+suf;function tick(t){if(!t0)t0=t;var p=Math.min(1,(t-t0)/1300);var e=1-Math.pow(1-p,3);var v=to*e;b.textContent=pre+(dec?v.toFixed(dec):Math.round(v).toLocaleString())+suf;if(p<1)requestAnimationFrame(tick);else b.textContent=fin;}requestAnimationFrame(tick);setTimeout(function(){b.textContent=fin;},1600);});},{threshold:.6});els.forEach(function(e){io.observe(e)});})();
(function(){var rm=matchMedia('(prefers-reduced-motion:reduce)').matches,hov=matchMedia('(hover:hover)').matches;
document.querySelectorAll('.stat,.proj,.pin,.jcard,.icon,.fface,.pcard,.glass,.lrow').forEach(function(el){el.classList.add('sheen')});
document.querySelectorAll('section>.wrap,.contact>.wrap').forEach(function(w){if(!w.closest('.hero')){w.classList.add('rv');w.setAttribute('data-rv','z');}});
var zio=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');zio.unobserve(x.target);}})},{threshold:.06});document.querySelectorAll('.rv[data-rv=z]').forEach(function(w){zio.observe(w)});
if(hov&&!rm){var h=document.querySelector('.hero'),root=document.documentElement,raf=0,px=0,py=0;document.querySelectorAll('[data-depth]').forEach(function(el){el.style.setProperty('--d',el.getAttribute('data-depth'))});
h.addEventListener('mousemove',function(e){var r=h.getBoundingClientRect();px=((e.clientX-r.left)/r.width-.5)*2;py=((e.clientY-r.top)/r.height-.5)*2;if(!raf)raf=requestAnimationFrame(function(){root.style.setProperty('--px',px.toFixed(3));root.style.setProperty('--py',py.toFixed(3));raf=0;});});
h.addEventListener('mouseleave',function(){root.style.setProperty('--px',0);root.style.setProperty('--py',0);});
document.addEventListener('mousemove',function(e){var el=e.target.closest&&e.target.closest('.sheen');if(!el)return;var r=el.getBoundingClientRect();el.style.setProperty('--mx',((e.clientX-r.left)/r.width*100).toFixed(1)+'%');el.style.setProperty('--my',((e.clientY-r.top)/r.height*100).toFixed(1)+'%');},{passive:true});}
var dock=document.getElementById('dock'),dsel=document.getElementById('dsel');if(dock){var da=[].slice.call(dock.querySelectorAll('a'));function setD(id){da.forEach(function(a){var on=a.getAttribute('href')==='#'+id;a.classList.toggle('active',on);if(on){dsel.style.left=a.offsetLeft+'px';dsel.style.width=a.offsetWidth+'px';}});}
var secs=[].slice.call(document.querySelectorAll('section[id],header[id]'));var sio=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting)setD(x.target.id)})},{rootMargin:'-45% 0px -50% 0px'});secs.forEach(function(s){sio.observe(s)});setD('home');}
var dlg=document.getElementById('csd');if(dlg){new MutationObserver(function(){document.body.classList.toggle('modal-open',dlg.open)}).observe(dlg,{attributes:true,attributeFilter:['open']});}
if(!rm){var layers=[].slice.call(document.querySelectorAll('.jtree,.rpath'));var tick=0;function par(){tick=0;var vh=innerHeight;layers.forEach(function(l){var r=l.parentElement.getBoundingClientRect();var p=(r.top+r.height/2-vh/2)/vh;l.style.transform='translate3d(0,'+(p*28).toFixed(1)+'px,0)';});}window.addEventListener('scroll',function(){if(!tick)tick=requestAnimationFrame(par)},{passive:true});par();}
})();
(function(){var imgs=document.querySelectorAll('img.lq[data-src]');var io=new IntersectionObserver(function(en){en.forEach(function(x){if(!x.isIntersecting)return;var im=x.target;var full=new Image();full.onload=function(){im.src=im.dataset.src;im.classList.remove('lq');};full.src=im.dataset.src;io.unobserve(im);});},{rootMargin:'200px'});imgs.forEach(function(i){io.observe(i)});})();
(function(){var d=document.getElementById('csd');if(!d||!d.showModal)return;var cards=document.querySelectorAll('.proj[data-slug]');function open(c){document.getElementById('csdCat').textContent=c.dataset.cat;document.getElementById('csdTitle').textContent=c.dataset.title;document.getElementById('csdDesc').innerHTML=c.dataset.desc;document.getElementById('csdEv').innerHTML=c.dataset.ev;document.getElementById('csdTags').innerHTML=c.dataset.tags.split(', ').map(function(t){return '<span class="pill">'+t+'</span>'}).join('');var u=document.getElementById('csdUrl');u.href=c.dataset.url;var sh=document.getElementById('csdShot');var ci=c.querySelector('.shot img');if(ci){sh.className='csdShot';sh.innerHTML='<img src="'+(ci.dataset.src||ci.src)+'" alt="">';}else{sh.className='csdShot noimg';sh.textContent=c.dataset.url.replace('https://','');}var ci2=c.querySelector('.shot img');function go(){d.showModal();}if(document.startViewTransition&&ci2&&!matchMedia('(prefers-reduced-motion:reduce)').matches){ci2.style.viewTransitionName='csimg';var vt=document.startViewTransition(function(){ci2.style.viewTransitionName='';go();var mi=document.querySelector('#csdShot img');if(mi)mi.style.viewTransitionName='csimg';});vt.finished.then(function(){var mi=document.querySelector('#csdShot img');if(mi)mi.style.viewTransitionName='';});}else go();history.replaceState(null,'','#project-'+c.dataset.slug);}
cards.forEach(function(c){c.addEventListener('click',function(e){if(e.target.closest('a'))return;open(c)});c.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();open(c)}});});
function close(){d.close();if(location.hash.indexOf('#project-')===0)history.replaceState(null,'',' ');}
document.getElementById('csdX').onclick=close;d.addEventListener('click',function(e){if(e.target===d)close()});d.addEventListener('close',function(){if(location.hash.indexOf('#project-')===0)history.replaceState(null,'',' ')});
var m=location.hash.match(/^#project-([a-z0-9]+)/);if(m){var c=document.querySelector('.proj[data-slug="'+m[1]+'"]');if(c)setTimeout(function(){open(c)},300);}})();
(function(){if(matchMedia('(prefers-reduced-motion:reduce)').matches||!matchMedia('(hover:hover)').matches)return;document.querySelectorAll('.tilt').forEach(function(el){el.addEventListener('mousemove',function(e){var r=el.getBoundingClientRect();var x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;el.style.transform='perspective(900px) rotateX('+(-y*6)+'deg) rotateY('+(x*6)+'deg) translateY(-3px)';});el.addEventListener('mouseleave',function(){el.style.transform='';});});var h=document.querySelector('.hero'),sp=document.getElementById('spot');if(h&&sp){h.addEventListener('mousemove',function(e){var r=h.getBoundingClientRect();sp.style.setProperty('--mx',((e.clientX-r.left)/r.width*100)+'%');sp.style.setProperty('--my',((e.clientY-r.top)/r.height*100)+'%');});}})();
(function(){var g=document.getElementById('cgrid');var step=322;function nxt(){if(g.scrollLeft+g.clientWidth>=g.scrollWidth-4){g.scrollTo({left:0,behavior:'smooth'});}else{g.scrollBy({left:step,behavior:'smooth'});}}document.getElementById('cprev').onclick=function(){g.scrollBy({left:-step,behavior:'smooth'});rest();};document.getElementById('cnext').onclick=function(){nxt();rest();};var t=null,paused=false;function start(){if(matchMedia('(prefers-reduced-motion:reduce)').matches)return;clearInterval(t);t=setInterval(function(){if(!paused)nxt();},2800);}function rest(){clearInterval(t);start();}(function(){var down=false,sx=0,sl=0,vx=0,lx=0,lt=0,raf=null;function onDown(e){if(e.pointerType==='mouse'&&e.button!==0)return;down=true;g.classList.add('dragging');sx=e.clientX;sl=g.scrollLeft;lx=e.clientX;lt=performance.now();vx=0;cancelAnimationFrame(raf);paused=true;}function onMove(e){if(!down)return;var dx=e.clientX-sx;var target=sl-dx;var max=g.scrollWidth-g.clientWidth;var over=target<0?target:(target>max?target-max:0);g.scrollLeft=over?(over<0?0:max):target;g.style.transform=over?('translateX('+(-over*0.35)+'px)'):'';var now=performance.now();vx=(e.clientX-lx)/Math.max(1,now-lt);lx=e.clientX;lt=now;}function onUp(){if(!down)return;down=false;g.classList.remove('dragging');g.style.transition='transform .35s cubic-bezier(.2,.7,.2,1)';g.style.transform='';setTimeout(function(){g.style.transition=''},380);var v=-vx*16;function step(){v*=.92;g.scrollLeft+=v;if(Math.abs(v)>.4)raf=requestAnimationFrame(step);else paused=false;}raf=requestAnimationFrame(step);}g.addEventListener('pointerdown',onDown);window.addEventListener('pointermove',onMove,{passive:true});window.addEventListener('pointerup',onUp);window.addEventListener('pointercancel',onUp);g.addEventListener('click',function(e){if(Math.abs(vx)>.2)e.preventDefault()},true);})();
g.addEventListener('mouseenter',function(){paused=true});g.addEventListener('mouseleave',function(){paused=false});g.addEventListener('touchstart',function(){paused=true},{passive:true});g.addEventListener('touchend',function(){paused=false},{passive:true});start();})();
</script>
</body></html>"""

import re as _re
try:
    import htmlmin, rjsmin, rcssmin
    def _min_css(m): return "<style>" + rcssmin.cssmin(m.group(1)) + "</style>"
    def _min_js(m):
        return "<script>" + rjsmin.jsmin(m.group(1)) + "</script>"
    H2 = _re.sub(r"<style>(.*?)</style>", _min_css, HTML, flags=_re.S)
    H2 = _re.sub(r"<script>(.*?)</script>", _min_js, H2, flags=_re.S)
    H2 = htmlmin.minify(H2, remove_comments=True, remove_empty_space=True, reduce_boolean_attributes=False)
except Exception as e:
    print("minify skipped:", e); H2 = HTML
out = pathlib.Path(__file__).parent / "index.html"
out.write_text(H2, encoding="utf-8")
print("written", len(H2) // 1024, "KB (raw", len(HTML) // 1024, "KB)")
