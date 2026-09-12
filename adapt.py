# -*- coding: utf-8 -*-
"""Turn a fresh copy of mark-portfolio/build.py into Jade's build.py: same layout, Jade's verified data, teal palette from the resume PDF.
Run:  cp ../mark-portfolio/build.py build.py && python adapt.py && python build.py
Facts: Resukme__EA.pdf (all numbers) + SEO/AEO skill tags from CV Application.docx. Placeholders in the docx stay out."""
import re, pathlib, json
HERE = pathlib.Path(__file__).parent
P = HERE / "build.py"
s = P.read_text(encoding="utf-8")
assert "Mark Edcel" in s, "build.py is not the fresh copy of Mark's"

EMAIL, PHONE = "jademendoza.va@gmail.com", "+63 908 763 2587"
LI = "https://www.linkedin.com/in/jadepatrickmendoza"
BASE = "https://referrernation-web.github.io/jade/"
PDF = "assets/Jade-Patrick-Mendoza-Resume-2026.pdf"
TEAL, TEAL2, TEAL3 = "#176f7d", "#1b8593", "#125866"


def one(old, new, regex=False, flags=re.S):
    global s
    if regex:
        n = len(re.findall(old, s, flags)); assert n == 1, (old[:70], n)
        s = re.sub(old, lambda _: new, s, count=1, flags=flags)
    else:
        n = s.count(old); assert n == 1, (old[:70], n)
        s = s.replace(old, new)


# ---------------------------------------------------------------- images: branded cards (no fake screenshots), placeholder portrait until the Loom frame lands
def images():
    from PIL import Image, ImageDraw, ImageFont
    A = HERE / "assets"
    try:
        F1 = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 70); F2 = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 32); F3 = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 26)
        FB = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 300)
    except Exception:
        F1 = F2 = F3 = FB = ImageFont.load_default()
    cards = {"vicemayor": ("Vice Mayor's office", "Calendar, correspondence, briefings, notes", "LGU MANSALAY · 2023"),
             "infosys": ("Financial accounts, by the book", "High-volume, regulated, precisely recorded", "INFOSYS BPM · 2024–"),
             "alorica": ("Telco account, fast lane", "Billing, promotions, connectivity", "ALORICA / PROBE CX · 2024"),
             "youth": ("Six years of youth programs", "Schedules, logistics, stakeholders", "COMMUNITY YOUTH ORG"),
             "seo": ("SEO / AEO, second track", "Keyword & entity research, schema, WordPress", "IN PRACTICE · CASE STUDIES ON REQUEST")}
    for key, (h, sub, tag) in cards.items():
        im = Image.new("RGB", (1280, 800), (247, 250, 251)); d = ImageDraw.Draw(im)
        for r in range(900, 0, -12):
            k = r / 900; col = (int(247 + (23 - 247) * (1 - k) * .35), int(250 + (111 - 250) * (1 - k) * .35), int(251 + (125 - 251) * (1 - k) * .35))
            d.ellipse([1180 - r, -260 - r * .6, 1180 + r, -260 + r * .6], fill=col)
        for gx in range(0, 1280, 40): d.line([(gx, 0), (gx, 800)], fill=(232, 238, 240))
        for gy in range(0, 800, 40): d.line([(0, gy), (1280, gy)], fill=(232, 238, 240))
        d.rectangle([0, 0, 1280, 16], fill=(23, 111, 125))
        d.text((80, 90), tag, font=F3, fill=(23, 111, 125))
        d.text((80, 300), h, font=F1, fill=(17, 17, 17))
        d.text((80, 400), sub, font=F2, fill=(90, 96, 100))
        d.rounded_rectangle([80, 640, 400, 700], radius=10, fill=(23, 111, 125)); d.text((104, 652), "Open the story  →", font=F2, fill=(255, 255, 255))
        im.save(A / f"thumb-{key}.jpg", quality=86)
    # portrait placeholders (hero poster + about photo) until a frame from Jade's Loom video replaces them
    for name, size in (("hero-poster.jpg", (1280, 720)), ("about-photo.jpg", (720, 720))):
        if (A / name).exists():
            continue
        im = Image.new("RGB", size, (18, 88, 102)); d = ImageDraw.Draw(im)
        for r in range(1200, 0, -14):
            k = r / 1200; col = (int(18 + (27 - 18) * (1 - k)), int(88 + (133 - 88) * (1 - k)), int(102 + (147 - 102) * (1 - k)))
            d.ellipse([size[0] * .7 - r, size[1] * .3 - r, size[0] * .7 + r, size[1] * .3 + r], fill=col)
        d.text((size[0] / 2, size[1] / 2), "JM", font=FB, fill=(255, 255, 255), anchor="mm")
        im.save(A / name, quality=88)


images()

# ---------------------------------------------------------------- data blocks
one(r'PHOTO = b64\("mark-photo.jpg"\)\nHERO = .*?\nABOUT = .*?\n', 'PHOTO = ""\nHERO = webp("hero-poster.jpg", 1280, 82)\nABOUT = webp("about-photo.jpg", 720, 82)\nINTRO = "video/intro.mp4" if (pathlib.Path(__file__).parent / "video" / "intro.mp4").exists() else ""\n', True)
KEYS = ["vicemayor", "infosys", "alorica", "youth", "seo"]
one(r'THUMBS = \{k: webp\("thumb-" \+ d \+ "\.jpg", 1280, 78\) for k, d in \{.*?\}\.items\(\)\}\n',
    'THUMBS = {k: webp("thumb-" + k + ".jpg", 1280, 78) for k in ' + json.dumps(KEYS) + '}\n', True)
one(r'EXPERTISE = \[\n.*?\n\]\n', '''EXPERTISE = [
    ("01", "Executive Calendar &amp; Inbox",
     "Daily calendar and appointments across meetings, official functions and engagements. Monitoring email and correspondence, surfacing priority items and drafting timely responses on behalf of the office."),
    ("02", "Meeting Prep &amp; Follow-Through",
     "Reports, briefing materials and meeting documents that support decision-making. Detailed notes, action-item tracking and coordinated updates that close open requests."),
    ("03", "Financial Account Operations",
     "High-volume inbound communications on financial accounts, transactions and service requests, resolved within regulatory requirements, internal controls and documented procedures. Precise records, strong data integrity."),
    ("04", "SEO &amp; AEO for WordPress",
     "Keyword and entity research, on-page optimization, FAQ and article schema, WordPress technical health, Search Console and Analytics reporting. Second track, case studies on request."),
]
''', True)
one(r'SKILL_GROUPS = \[\n.*?\n\]\n', '''SKILL_GROUPS = [
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
''', True)
one(r'FEATURED = \[\n.*?\n\]\n', '''FEATURED = [
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
''', True)
one(r'SYSLOG = \[\n.*?\n\]\n', '''SYSLOG = [
    ("Education", "Bachelor of Science in Information Systems &middot; Clarendon College", "BSIS", "#journey"),
    ("Languages", "English and Tagalog", "EN / TL", "#journey"),
    ("Location", "Fort Bonifacio, Taguig City &middot; open to remote work", "Remote", "#contact"),
    ("Resume", "Executive Assistant / Executive Virtual Assistant &middot; PDF", "PDF", "PDFPATH"),
]
'''.replace("PDFPATH", PDF), True)
CERTS = [("STRENGTH", "Discretion and data integrity", "Professional strength", LI), ("STRENGTH", "High-volume accuracy", "Professional strength", LI),
         ("STRENGTH", "Anticipates next steps", "Professional strength", LI), ("STRENGTH", "Calm under pressure", "Professional strength", LI),
         ("STRENGTH", "Clear written communication", "Professional strength", LI), ("STRENGTH", "Independent follow-through", "Professional strength", LI),
         ("COMPETENCY", "Executive calendar &amp; scheduling", "Core competency", LI), ("COMPETENCY", "Inbox &amp; correspondence management", "Core competency", LI),
         ("COMPETENCY", "Meeting preparation &amp; follow-through", "Core competency", LI), ("COMPETENCY", "Document &amp; report preparation", "Core competency", LI),
         ("COMPETENCY", "Travel and logistics coordination", "Core competency", LI), ("COMPETENCY", "Online research &amp; summarization", "Core competency", LI),
         ("COMPETENCY", "Confidential information handling", "Core competency", LI), ("COMPETENCY", "Stakeholder communication", "Core competency", LI),
         ("COMPETENCY", "Remote work &amp; self-management", "Core competency", LI), ("EDUCATION", "BS Information Systems", "Clarendon College", LI)]
one(r'CERTS = \[\n.*?\n\]\n', "CERTS = [\n" + "".join(f'    ({json.dumps(c)}, "{i+1:02d}", {json.dumps(t)}, {json.dumps(d)}, {json.dumps(u)}),\n' for i, (c, t, d, u) in enumerate(CERTS)) + "]\n", True)
one(r'LQ = \{k: .*?\n', 'LQ = {k: __import__("patch8_lqip").lqip(A / ("thumb-" + k + ".jpg")) for k in ' + json.dumps(KEYS) + '}\n', True)

# ---------------------------------------------------------------- head
one(r'<title>.*?</title>', '<title>Jade Patrick Mendoza &mdash; Executive Assistant | Executive Virtual Assistant &amp; SEO/AEO</title>', True)
one(r'<meta name="description" content=".*?">', '<meta name="description" content="Executive Assistant and Executive Virtual Assistant from Taguig City: calendar, inbox and meeting support for a Vice Mayor, financial account operations at Infosys BPM, six years of community leadership, plus SEO and AEO for WordPress. Open to remote work.">', True)
one(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Jade Patrick Mendoza &mdash; Executive Assistant / Executive Virtual Assistant">', True)
one(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="Executive support, financial account operations and SEO/AEO. Taguig City, open to remote work.">', True)
s = s.replace("https://referrernation-web.github.io/portfolio/", BASE)
s = s.replace('<link rel="preload" as="image" href="assets/spr/d-run.webp" media="(min-width:981px)"><link rel="preload" as="image" href="assets/spr/p-run.webp" media="(min-width:981px)">', "")
one("font-size='32' font-weight='800' fill='%23fff' text-anchor='middle'%3EM%3C/text%3E%3Ccircle cx='48' cy='44' r='6' fill='%23ff2a2a'/%3E", "font-size='26' font-weight='800' fill='%23fff' text-anchor='middle'%3EJM%3C/text%3E")
one('<meta name="theme-color" content="#000000">', f'<meta name="theme-color" content="{TEAL}">')

# ---------------------------------------------------------------- nav + hero
one('<span class="logo">Mark Edcel<i> .</i></span>', '<span class="logo">Jade Mendoza<i> .</i></span>')
one('<video id="reel" data-depth="-6" src="video/heroreel.mp4" poster=\\"""" + HERO + """" muted autoplay loop playsinline preload="metadata"></video>',
    '<video id="reel" data-depth="-6"\\"""" + (" src=\\"" + INTRO + "\\"" if INTRO else "") + """ poster=\\"""" + HERO + """" muted autoplay loop playsinline preload="metadata"></video>')
one('<h1><span class="kt" id="kt">Hi, I&rsquo;m a</span><br><span class="rot" id="rot" aria-live="polite">Full-Stack Developer</span><span class="uline"></span></h1>',
    '<h1><span class="kt" id="kt">Hi, I&rsquo;m Jade, an</span><br><span class="rot" id="rot" aria-live="polite">Executive Assistant</span><span class="uline"></span></h1>')
one('<p class="sub">I build fast, scalable websites and web apps in WordPress, Node.js and React, then own the technical SEO and AI-search visibility that makes them rank.</p>',
    '<p class="sub">I keep executive operations moving: calendars, inboxes, briefings and follow-through, with the discretion of financial account work. Second track: SEO and AEO for WordPress sites.</p>')
one('<a class="btn light" href="#projects">View My Work</a><a class="btn ghosty" href="#contact">Contact Me</a><a class="btn ghosty" href="world/" title="3D resume: ride Kimpoy with Dianna across the wonders of the world">&#127758; Ride the 3D World</a>',
    f'<a class="btn light" href="#projects">View My Work</a><a class="btn ghosty" href="world/" title="3D resume: drive a jeepney across the wonders of the world">&#127758; Ride the 3D World</a><a class="btn ghosty" href="{PDF}" target="_blank" rel="noopener">Resume PDF</a>')
one('<span class="flabel tr">// Full-Stack &middot; SEO &middot; AEO<br>Available now</span>', '<span class="flabel tr">// Executive Assistant &middot; SEO &middot; AEO<br>Open to remote work</span>')
one('<span class="flabel bl">// Makati &rarr; US &middot; CA &middot; AU<br>ET / PT overlap</span>', '<span class="flabel bl">// Taguig City &rarr; remote<br>English &middot; Tagalog</span>')
one('<span class="ainote">AI-GENERATED REEL &middot; REAL RESULTS BELOW</span>', '<span class="ainote">""" + ("APPLICATION INTRO &middot; RESUME FACTS BELOW" if INTRO else "INTRO VIDEO IN PRODUCTION &middot; RESUME FACTS BELOW") + """</span>')
one('<button class="unmute" id="unmute">&#128266; UNMUTE REEL</button>', '""" + (\'<button class="unmute" id="unmute">&#128266; UNMUTE INTRO</button>\' if INTRO else "") + """')
one("var R=['Full-Stack Developer','WordPress Developer','SEO Specialist','AEO Specialist']", "var R=['Executive Assistant','Executive Virtual Assistant','Financial Account Specialist','SEO / AEO Specialist']")

# ---------------------------------------------------------------- proof band
one(r'<div class="proofband" aria-label="Evidence highlights"><div class="mq-track">.*?</div></div>',
    '<div class="proofband" aria-label="Evidence highlights"><div class="mq-track">' + 2 * ('<span class="pf"><b>2+</b>years in customer &amp; financial account operations</span><span class="pf"><b>6</b>years of community youth leadership</span><span class="pf"><b>Vice Mayor</b>executive assistant, LGU Mansalay, 2023</span><span class="pf"><b>Infosys BPM</b>senior process executive, 2024 to present</span><span class="pf"><b>EN &middot; TL</b>English and Tagalog</span><span class="pf"><b>BSIS</b>Clarendon College</span><span class="pf"><b>Remote</b>Taguig City, open to remote work</span>') + '</div></div>', True)

# ---------------------------------------------------------------- about
one('alt="Mark Edcel Lopez" loading="lazy" decoding="async" width="720" height="720">', 'alt="Jade Patrick Mendoza" loading="lazy" decoding="async" width="720" height="720">')
one('<div class="badge"><span class="dot"></span>OPEN TO OPPORTUNITIES</div>', '<div class="badge"><span class="dot"></span>OPEN TO REMOTE WORK</div>')
one('<h2>I&rsquo;m Mark Edcel Lopez</h2>', '<h2>I&rsquo;m Jade Patrick Mendoza</h2>')
one(r'<p>A full-stack developer based in Makati.*?</p>', '<p>A detail-oriented administrative professional in Taguig City, experienced in supporting executive operations, managing high-volume communications and coordinating time-sensitive follow-through. Hands-on experience supporting a Vice Mayor, 2+ years in customer and financial account operations, and 6 years of community leadership. Trusted to anticipate needs, handle confidential information, prepare decision-ready materials and keep priorities moving across distributed teams.</p>', True)
one(r'<div class="stats">\n.*?\n    </div>', '''<div class="stats">
      <div class="stat glow hv" data-rv="drop"><b data-count="2" data-suffix="+">2+</b><span>years in customer &amp; financial account operations</span></div>
      <div class="stat glow hv" data-rv="drop"><b data-count="6">6</b><span>years of community youth leadership</span></div>
      <div class="stat glow hv" data-rv="drop"><b data-count="1">1</b><span>Vice Mayor supported, LGU Mansalay</span></div>
      <div class="stat glow"><b>EN &middot; TL</b><span>English and Tagalog</span></div>
    </div>''', True)

# ---------------------------------------------------------------- journey
one('<div class="shead center"><span class="mono">HUMBLE BEGINNINGS</span><h2>From Service Crew to Search Engineer</h2>\n  <p>Every success story has humble beginnings. Mine started behind a pizza counter.</p></div>',
    '<div class="shead center"><span class="mono">CAREER JOURNEY</span><h2>From Youth Leader to Executive Support</h2>\n  <p>Community programs first, then a Vice Mayor&rsquo;s office, then regulated financial accounts. The same habit at every stop: anticipate, document, follow through.</p></div>')
one(r'<blockquote class="jquote glass" data-rv="zoom"><p>.*?</p><footer>.*?</footer></blockquote>',
    '<blockquote class="jquote glass" data-rv="zoom"><p>&ldquo;Trusted to anticipate needs, handle confidential information, prepare decision-ready materials and keep priorities moving across distributed teams.&rdquo;</p><footer>&mdash; the summary line on the resume, and the standard for every task</footer></blockquote>', True)
JT = [("College", "BS Information Systems, Clarendon College", "Systems thinking that became process discipline."),
      ("6 years", "Youth Leader, Community Youth Organization", "Led and organized community youth programs: schedules, logistics, resources, event activities and stakeholder coordination."),
      ("2023", "Executive Assistant to the Vice Mayor, LGU Mansalay, Oriental Mindoro", "Jul&ndash;Dec 2023. Daily calendar, official correspondence, briefing materials, meeting notes and research summaries for the office."),
      ("2024", "Customer Service Representative, Telco Account, Alorica / Probe CX", "Feb&ndash;Jun 2024. Billing, promotion and connectivity concerns; product recommendations; proactive guidance."),
      ("2024&ndash;", "Senior Process Executive, Infosys BPM", "Jul 2024 to present. High-volume financial account communications under regulatory controls, precise records, mentoring new hires with Training and Quality."),
      ("Next", "SEO &amp; AEO, second track", "Keyword and entity research, on-page optimization, schema and WordPress technical health. Case studies on request.")]
jt_html = "".join(f'<li class="jt" data-rv="{"left" if i % 2 == 0 else "right"}"><span class="jdot"></span><div class="jcard hv"><span class="jyear">{y}</span><h3>{t}</h3><p>{d}</p></div></li>' for i, (y, t, d) in enumerate(JT))
one(r'<ol class="jline">.*?</ol>', '<ol class="jline">' + jt_html + '</ol>', True)
one('<div class="note">The journey continues.</div>', '<div class="note">Next: your calendar.</div>')

# ---------------------------------------------------------------- expertise / skills / projects / certs / intro
one('<h2>Building Sites That Rank in Google &amp; AI</h2>\n    <p>Combining WordPress engineering, technical SEO and Answer Engine Optimization to create sites that get found, cited and hired.</p>\n    <div class="note">Turning rankings into revenue!</div>\n    <button class="mg-play" id="mgplay" type="button">&#9654; WATCH DIANNA PLAY</button>',
    '<h2>Keeping Executive Operations Moving</h2>\n    <p>Calendar, inbox, meetings and follow-through, handled with the accuracy of financial account work. One assistant, four things covered.</p>\n    <div class="note">Anticipate, document, follow through.</div>\n    <button class="mg-play" id="mgplay" type="button">&#9654; WATCH JADE PLAY</button>')
one('<h2>Technologies I Work With</h2>\n  <p>Full-stack WordPress, search and AI-visibility tooling I use daily.</p>', '<h2>Tools &amp; Systems I Work With</h2>\n  <p>Executive support, AI productivity and the SEO stack for WordPress sites.</p>')
one('<h2>Projects That Define My Journey</h2>\n  <p>Production client sites and AEO programs. Every number names its evidence.</p>', '<h2>Work That Defines the Journey</h2>\n  <p>Each card is a role from the resume: what the office needed, what I did, what it produced.</p>')
one('<h3>System Logs &amp; Other Engagements</h3>', '<h3>Education, Languages &amp; Logistics</h3>')
one('<div class="logline">Reviewing client engagements continuous<span class="cursor"></span></div>', '<div class="logline">Reviewing priorities continuous<span class="cursor"></span></div>')
one('<h2>Professional Credentials</h2>', '<h2>Strengths &amp; Competencies</h2>')
one('Total of """ + str(len(CERTS)) + """ certificates running.', 'Total of """ + str(len(CERTS)) + """ strengths and competencies from the resume.')
one('<a class="btn light" id="csdUrl" target="_blank" rel="noopener">Visit live site &rarr;</a>', '<a class="btn light" id="csdUrl">See the journey &rarr;</a>')
one(r'<section id="intro" class="lz"><div class="wrap">.*?</div></section>',
    '<section id="intro" class="lz"><div class="wrap">\n  <div class="shead center"><span class="mono">INTRO TRANSMISSION</span><h2>Meet Me in Forty Seconds</h2></div>\n  <div class="introwrap glow" id="loomwrap">""" + (\'<video src="\' + INTRO + \'" poster="\' + HERO + \'" controls playsinline preload="metadata" style="width:100%;height:100%;object-fit:cover;background:#000"></video>\' if INTRO else \'<button class="loomfacade" id="loomplay" aria-label="Intro video in production" type="button" disabled><span class="playbtn">&#9654;</span><span>Application intro: in production</span></button>\') + """</div>\n  <p class="intronote">""" + ("Who I am, what I handle, and what to do next." if INTRO else "Recording this week. The resume above does not wait.") + """</p>\n</div></section>', True)

# ---------------------------------------------------------------- contact + footer
one('action="https://formsubmit.co/markedcel06@gmail.com"', f'action="https://formsubmit.co/{EMAIL}"')
one('<input type="hidden" name="_subject" value="Portfolio inquiry &mdash; referrernation-web.github.io">', '<input type="hidden" name="_subject" value="Inquiry &mdash; referrernation-web.github.io/jade">')
one('placeholder="Tell me about your site and what it should rank for."', 'placeholder="The role, the hours, what needs handling."')
one(r'<div class="cinfo">\n.*?\n    </div>', f'''<div class="cinfo">
      <div><b>// Executive Assistant</b>Executive Virtual Assistant<br>SEO &amp; AEO, second track</div>
      <div><b>// Status</b><span class="st">Open to remote work</span><br>Fort Bonifacio, Taguig City, Philippines</div>
      <div><b>// Direct</b><a href="mailto:{EMAIL}">{EMAIL}</a><br>{PHONE}</div>
      <div><b>// Resume</b><a href="{PDF}" target="_blank" rel="noopener">Download PDF</a></div>
      <div><b>// Verify</b><a href="{LI}" target="_blank" rel="noopener">LinkedIn</a></div>
    </div>''', True)
one('<div class="bigname">MARK EDCEL</div>', '<div class="bigname">JADE MENDOZA</div>')
one(r'<div class="foot">\n.*?\n  </div>', f'''<div class="foot">
    <div>Contact Transmission<br>{EMAIL} &middot; {PHONE}</div>
    <div><a href="{LI}">LinkedIn</a> &middot; <a href="{PDF}">Resume PDF</a> &middot; <a href="world/">3D World</a></div>
    <div>&copy; 2026 Jade Patrick Mendoza &middot; v1 &middot; September 2026</div>
  </div>''', True)

# ---------------------------------------------------------------- scripts: drop the Loom embed and the mascot game (no sprites for Jade yet)
one(r"\(function\(\)\{var b=document\.getElementById\('loomplay'\);.*?\n", "", True)
one("(function(){var v=document.getElementById('reel'),b=document.getElementById('unmute');", "(function(){var v=document.getElementById('reel'),b=document.getElementById('unmute');if(!v||!b)return;")
one('        \'<div class="icon hv" data-rv="zoom"><img src="https://cdn.simpleicons.org/\' + slug + \'/ffffff" alt="\' + label +', '        \'<div class="icon hv" data-rv="zoom"><img src="\' + (("data:image/svg+xml;utf8," + __import__("urllib.parse").parse.quote(\'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><circle cx="24" cy="24" r="21" fill="none" stroke="#ffffff" stroke-width="3"/><text x="24" y="30" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="17" font-weight="700" fill="#ffffff">\' + slug[5:] + \'</text></svg>\')) if slug.startswith("mono:") else "https://cdn.simpleicons.org/" + slug + "/ffffff") + \'" alt="\' + label +')
one(r"\(function\(\)\{var DBG=/mgdebug/.*?\n(?=\(function\(\)\{var imgs=document\.querySelectorAll\('img\.lq)", "", True)
s = s.replace(".mg-play", ".mg-play-off")

# ---------------------------------------------------------------- palette: maroon family -> teal family, light shell stays
PAL = [("#8a1c2b", TEAL), ("#a02538", TEAL2), ("#7a1424", TEAL3), ("#9d2436", TEAL2), ("#d8293f", "#1fa3b3"), ("#b23445", TEAL2), ("#5e0e1b", "#0c3d47"),
       ("#c2606c", "#5fa9b5"), ("#d08a95", "#8fc4cc"), ("#b8404f", "#1fa3b3"), ("#e6b3bb", "#bfe0e5"), ("#f4d5da", "#dcefF2"), ("#f0c2c9", "#cfe8ec"), ("#f8e9ec", "#eef7f8"),
       ("138,28,43", "23,111,125"), ("90,20,30", "12,61,71"), ("160,90,100", "95,169,181"), ("#ff2a2a", "#1fa3b3"), ("#d40f1f", TEAL), ("#e5322d", TEAL2)]
for a, b in PAL:
    s = s.replace(a, b)

left = [m for m in re.findall(r"Mark|Makati|Dianna|Kimpoy|Coggno|Bytown|markedcel|Papa", s)]
print("adapted; leftovers:", len(left), sorted(set(left)))
P.write_text(s, encoding="utf-8")
