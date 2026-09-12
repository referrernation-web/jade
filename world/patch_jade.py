# -*- coding: utf-8 -*-
"""Turn Mark's world engine (fresh copy of mark-portfolio/world/index.html) into Jade's World.
Run:  cp ../../mark-portfolio/world/index.html index.html && python patch_jade.py
Every replacement asserts exactly one hit so drift in the source engine is loud, not silent.
Facts: Resukme__EA.pdf (verified) + SEO/AEO skill tags from CV Application.docx. No invented numbers."""
import re, pathlib, json

P = pathlib.Path(__file__).parent / "index.html"
s = P.read_text(encoding="utf-8")
assert "Mark Edcel" in s, "index.html is not the fresh copy of Mark's engine"
BASE = "https://referrernation-web.github.io/jade/"
EMAIL, PHONE = "jademendoza.va@gmail.com", "+63 908 763 2587"
LI = "https://www.linkedin.com/in/jadepatrickmendoza"
PDF = "../assets/Jade-Patrick-Mendoza-Resume-2026.pdf"
TEAL, TEAL2, TEAL3 = "176f7d", "1b8593", "125866"


def one(old, new, flags=0, regex=False):
    global s
    if regex:
        m = re.findall(old, s, flags)
        assert len(m) == 1, (old[:60], len(m))
        s = re.sub(old, lambda _: new, s, count=1, flags=flags)
    else:
        assert s.count(old) == 1, (old[:60], s.count(old))
        s = s.replace(old, new)


# ---------------------------------------------------------------- head
JSONLD = json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "Person", "@id": BASE + "#person", "name": "Jade Patrick Mendoza", "jobTitle": "Executive Assistant / Executive Virtual Assistant",
     "email": "mailto:" + EMAIL, "telephone": PHONE.replace(" ", ""), "address": {"@type": "PostalAddress", "addressLocality": "Taguig City", "addressRegion": "Metro Manila", "addressCountry": "PH"},
     "url": BASE, "sameAs": [LI], "worksFor": {"@type": "Organization", "name": "Infosys BPM"}, "alumniOf": {"@type": "CollegeOrUniversity", "name": "Clarendon College"},
     "knowsAbout": ["Executive calendar management", "Inbox management", "Meeting preparation", "Financial account operations", "SEO", "Answer Engine Optimization", "WordPress"]},
    {"@type": "WebPage", "@id": BASE + "world/", "url": BASE + "world/", "name": "Jade's World, 3D resume", "about": {"@id": BASE + "#person"}, "isPartOf": {"@id": BASE}}]}, ensure_ascii=False)
one(r"<title>.*?</script>", f"""<title>Jade's World — ride the 3D resume of Jade Patrick Mendoza</title>
<meta name="description" content="Interactive 3D resume of Jade Patrick Mendoza, Executive Assistant and Executive Virtual Assistant from Taguig who also does SEO and AEO: ride a jeepney across the wonders of the world to see the Vice Mayor's office, Infosys BPM, the tools and how to get in touch.">
<link rel="canonical" href="{BASE}world/">
<meta property="og:type" content="website"><meta property="og:title" content="Jade's World — the 3D resume of Jade Patrick Mendoza"><meta property="og:description" content="Jade drives a jeepney across the wonders of the world. Every landmark is one part of the resume: executive support, financial account operations, SEO and AEO, with the facts."><meta property="og:image" content="{BASE}world/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:url" content="{BASE}world/">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="Jade's World — 3D resume"><meta name="twitter:image" content="{BASE}world/og.jpg">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='32' cy='32' r='30' fill='%23{TEAL}'/%3E%3Ctext x='32' y='42' font-family='Arial,sans-serif' font-size='24' font-weight='900' fill='%23ffffff' text-anchor='middle'%3EJM%3C/text%3E%3C/svg%3E">
<script type="application/ld+json">{JSONLD}</script>""", re.S, True)

# ---------------------------------------------------------------- seo text, hud, load card
one(r'<section class="seo".*?</section>', f"""<section class="seo" aria-label="Resume text version">
<h1>Jade Patrick Mendoza — Executive Assistant / Executive Virtual Assistant, SEO and AEO (Taguig City, open to remote work)</h1>
<p>Interactive 3D resume. Each landmark is one section. <a href="../">Classic resume</a> · <a href="{PDF}">Resume PDF</a> · <a href="{LI}">LinkedIn</a>.</p>
<h2>Manila — About</h2><p>Detail-oriented administrative professional experienced in supporting executive operations, managing high-volume communications and coordinating time-sensitive follow-through. Hands-on experience supporting a Vice Mayor, 2+ years in customer and financial account operations, and 6 years of community leadership. Second track: SEO and Answer Engine Optimization for WordPress sites.</p>
<h2>Banaue — Journey</h2><ul><li>Bachelor of Science in Information Systems, Clarendon College</li><li>6 years Youth Leader, Community Youth Organization</li><li>Jul–Dec 2023 Executive Assistant to the Vice Mayor, Local Government Unit of Mansalay, Oriental Mindoro</li><li>Feb–Jun 2024 Customer Service Representative, Telco account, Alorica / Probe CX</li><li>Jul 2024–present Senior Process Executive, Infosys BPM (financial accounts)</li></ul>
<h2>Giza — Expertise</h2><ul><li>Executive calendar, inbox and correspondence management</li><li>Meeting preparation, notes and action-item follow-through</li><li>Financial account operations with regulatory controls and data integrity</li><li>SEO / AEO: keyword and entity research, on-page optimization, schema, WordPress</li></ul>
<h2>Paris — Tools</h2><p>Google Workspace, Microsoft Outlook, Microsoft Teams, Salesforce CRM, Google Drive, Dropbox, Microsoft Copilot and AI tools, WordPress, Yoast SEO, Rank Math, Google Search Console, Google Analytics, SEMrush, Ahrefs.</p>
<h2>Boracay — Work highlights</h2><ul><li>Vice Mayor's office: daily calendar, official correspondence, briefing materials, meeting notes and research summaries</li><li>Infosys BPM: high-volume financial account communications, regulatory adherence, precise records, mentoring new hires with Training and Quality</li><li>Alorica / Probe CX: billing, promotion and connectivity concerns for a telco account</li><li>Community youth programs: planning, logistics and stakeholder coordination over six years</li></ul>
<h2>Rome — Strengths</h2><p>Discretion and data integrity · High-volume accuracy · Anticipates next steps · Calm under pressure · Clear written communication · Independent follow-through · Confidential information handling · Stakeholder communication · Remote work and self-management. Languages: English, Tagalog.</p>
<h2>New York — Contact</h2><p>Open to remote work. Fort Bonifacio, Taguig City, Philippines. <a href="mailto:{EMAIL}">{EMAIL}</a> · {PHONE} · <a href="{LI}">LinkedIn</a>.</p>
</section>""", re.S, True)
one('<div id="hud"><b>Mark <span>Edcel</span></b><small>Full-Stack Dev · SEO · AEO<br>Makati → US · CA · AU</small></div>',
    '<div id="hud"><b>Jade <span>Patrick</span></b><small>Exec. Assistant · SEO · AEO<br>Taguig → remote</small></div>')
one('H center on Kimpoy · B bark', 'H center on the jeepney · B honk')
one(r'<div id="load"><div class="card">\n<h1>.*?</p>', """<div id="load"><div class="card">
<h1>Jade's <span>World</span></h1>
<p>Jade drives a jeepney across the wonders of the world. Every landmark is one part of the resume. Drive in and the sign opens. Plow through the letters, bowl the pins, kick the coconuts.</p>""", re.S, True)

# ---------------------------------------------------------------- panels
DATA = r"""var DATA={
home:{k:'MANILA · HOME',t:'Hi, I’m Jade Patrick Mendoza',h:'<p>Executive Assistant and Executive Virtual Assistant from Taguig City. I support executive operations, manage high-volume communications and keep time-sensitive follow-through moving: hands-on experience supporting a Vice Mayor, 2+ years in customer and financial account operations, and 6 years of community leadership. Second track: SEO and Answer Engine Optimization for WordPress sites.</p><div class="stat"><div><b>2+</b><small>years in customer &amp; financial account operations</small></div><div><b>6</b><small>years of community youth leadership</small></div><div><b>1</b><small>Vice Mayor supported, LGU Mansalay</small></div><div><b>EN · TL</b><small>English and Tagalog</small></div></div><p>Ride to each landmark: <b>Banaue</b> (journey), <b>Giza</b> (expertise), <b>Paris</b> (tools), <b>Boracay</b> (work highlights), <b>Rome</b> (strengths), <b>New York</b> (contact).</p><a class="cta" href="#" data-go="contact">Hire me</a><a class="cta alt2" href="PDFPATH" target="_blank" rel="noopener">Resume PDF</a><a class="cta alt2" href="../">Classic resume</a>'},
journey:{k:'BANAUE RICE TERRACES · JOURNEY',t:'From youth leader to executive support',h:'<p>“Trusted to anticipate needs, handle confidential information, prepare decision-ready materials and keep priorities moving across distributed teams.”</p><ul class="tl"><li><i>College</i><b>BS Information Systems, Clarendon College</b>Systems thinking that became process discipline.</li><li><i>6 years</i><b>Youth Leader, Community Youth Organization</b>Led and organized community youth programs: schedules, logistics, resources, stakeholders.</li><li><i>2023</i><b>Executive Assistant to the Vice Mayor · LGU Mansalay, Oriental Mindoro</b>Jul–Dec 2023. Calendar, official correspondence, briefing materials, meeting notes, research summaries.</li><li><i>2024</i><b>Customer Service Representative, Telco · Alorica / Probe CX</b>Feb–Jun 2024. Billing, promotion and connectivity concerns in a fast-paced environment.</li><li><i>2024–</i><b>Senior Process Executive · Infosys BPM</b>Jul 2024–present. High-volume financial account communications, regulatory controls, precise records, mentoring new hires.</li></ul>'},
expertise:{k:'GIZA · EXPERTISE',t:'Four pyramids, four things I do',h:'<h4>01 Executive calendar &amp; inbox</h4><p>Daily calendar and appointments across meetings, official functions and engagements. Monitor email and correspondence, surface priority items, draft timely responses on behalf of the office.</p><h4>02 Meeting prep &amp; follow-through</h4><p>Reports, briefing materials and meeting documents for decision-making. Detailed notes, action-item tracking and coordinated updates that close open requests.</p><h4>03 Financial account operations</h4><p>High-volume inbound communications on financial accounts, transactions and service requests, resolved within regulatory requirements, internal controls and documented procedures.</p><h4>04 SEO &amp; AEO</h4><p>Keyword and entity research, on-page optimization, FAQ and article schema, WordPress technical health, Search Console and Analytics reporting. Case studies on request.</p>'},
skills:{k:'PARIS · TOOLS',t:'Tools and systems I work with',h:'<h4>Executive support</h4><div class="tags"><span>Google Workspace</span><span>Outlook</span><span>Microsoft Teams</span><span>Google Drive</span><span>Dropbox</span><span>Salesforce CRM</span><span>Microsoft Copilot</span><span>AI tools</span></div><h4>Core competencies</h4><div class="tags"><span>Calendar &amp; scheduling</span><span>Inbox management</span><span>Meeting preparation</span><span>Document &amp; report prep</span><span>Travel &amp; logistics</span><span>Research &amp; summarization</span><span>Confidential handling</span><span>Stakeholder communication</span></div><h4>SEO / AEO</h4><div class="tags"><span>WordPress</span><span>Yoast SEO</span><span>Rank Math</span><span>Search Console</span><span>Google Analytics</span><span>SEMrush</span><span>Ahrefs</span><span>Schema markup</span><span>AI Overviews</span><span>E-E-A-T</span></div><h4>Languages</h4><div class="tags"><span>English</span><span>Tagalog</span></div>'},
projects:{k:'BORACAY BOARDWALK · WORK HIGHLIGHTS',t:'The work behind the resume',h:''},
certs:{k:'ROME · STRENGTHS',t:'Nine strengths in the Colosseum',h:'<p>Professional strengths and core competencies from the resume, one banner each.</p><h4>Professional strengths</h4><p>Discretion and data integrity · High-volume accuracy · Anticipates next steps · Calm under pressure · Clear written communication · Independent follow-through</p><h4>Core competencies</h4><p>Executive calendar &amp; scheduling · Inbox &amp; correspondence management · Meeting preparation &amp; follow-through · Document &amp; report preparation · Travel and logistics coordination · Online research &amp; summarization · Confidential information handling · Stakeholder communication · Remote work &amp; self-management</p><h4>Education</h4><p>Bachelor of Science in Information Systems, Clarendon College.</p>'},
contact:{k:'NEW YORK · CONTACT',t:'Let’s keep your priorities moving',h:'<p><b>Status:</b> open to remote work, executive assistant and executive virtual assistant roles.<br><b>Region:</b> Fort Bonifacio, Taguig City, Philippines · remote worldwide.</p><p><b>EMAILADDR</b><br>PHONENUM</p><form class="form" id="cform" action="https://formsubmit.co/ajax/EMAILADDR" method="POST"><input type="hidden" name="_subject" value="Jade&#39;s World contact"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false"><input type="text" name="_honey" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px"><label>NAME</label><input name="name" required placeholder="Your name"><label>EMAIL</label><input name="email" type="email" required placeholder="you@company.com"><label>MESSAGE</label><textarea name="message" required placeholder="The role, the hours, what needs handling."></textarea><button class="cta" type="submit">Send message</button></form><a class="cta alt2" href="PDFPATH" target="_blank" rel="noopener">Download resume (PDF)</a><a class="cta alt2" href="mailto:EMAILADDR">Email</a><a class="cta alt2" href="LIURL" target="_blank" rel="noopener">LinkedIn</a>'}
};
""".replace("PDFPATH", PDF).replace("EMAILADDR", EMAIL).replace("PHONENUM", PHONE).replace("LIURL", LI)
one(r"var DATA=\{\n.*?\n\};\n", DATA, re.S, True)

PROJECTS = r"""var PROJECTS=[
['Vice Mayor’s Office','vicemayor','Executive Assistant, LGU Mansalay, Oriental Mindoro (Jul–Dec 2023): calendar, official correspondence, briefing materials, meeting notes, research summaries.',LIURL,['2023','Executive Assistant to the Vice Mayor','LGU Mansalay, Oriental Mindoro']],
['Infosys BPM','infosys','Senior Process Executive (Jul 2024–present): high-volume financial account communications, regulatory controls, precise records, mentoring new hires with Training and Quality.',LIURL,['2024–','Senior Process Executive','Infosys BPM · financial accounts']],
['Alorica / Probe CX','alorica','Customer Service Representative, telco account (Feb–Jun 2024): billing, promotion and connectivity concerns; product recommendations; proactive guidance.',LIURL,['2024','Customer Service Representative','Alorica / Probe CX · telco']],
['Youth Leadership','youth','Six years leading community youth programs: planning, communication, schedules, logistics, resources and event activities.',LIURL,['6 yrs','Youth Leader','Community Youth Organization']],
['SEO / AEO track','seo','Keyword and entity research, on-page optimization, FAQ and article schema, WordPress technical health, GSC and GA reporting. Case studies on request.',LIURL,['2nd track','SEO / AEO for WordPress','case studies on request']]];
""".replace("LIURL", "'" + LI + "'")
one(r"var PROJECTS=\[\n.*?\]\]\];\n", PROJECTS, re.S, True)
one(r"DATA\.projects\.h=.*?\n",
    "DATA.projects.h=PROJECTS.map(function(p){return '<div class=\"pj\"><img src=\"../assets/img/thumb-'+p[1]+'.webp\" alt=\"\"><div><b>'+p[0]+'</b><small>'+p[2]+'</small></div></div>'}).join('')+'<p>Every line above comes from the resume. References and case studies on request.</p><a class=\"cta alt2\" href=\"" + PDF + "\" target=\"_blank\" rel=\"noopener\">Resume PDF ↗</a>';\n",
    re.S, True)
# boards on the boardwalk: open the LinkedIn profile instead of a client site
one("pad(bx+i*8,s.z-1.2,2.4,1.4,'OPEN '+pj[0].toUpperCase(),function(){window.open(pj[3],'_blank','noopener')})",
    "pad(bx+i*8,s.z-1.2,2.4,1.4,'ABOUT '+pj[0].toUpperCase(),function(){openP('projects')})")

# ---------------------------------------------------------------- banners (Rome): strengths + competencies instead of certificates
STR = [["STRENGTH", "Discretion and data integrity", "Professional strength", LI], ["STRENGTH", "High-volume accuracy", "Professional strength", LI],
       ["STRENGTH", "Anticipates next steps", "Professional strength", LI], ["STRENGTH", "Calm under pressure", "Professional strength", LI],
       ["STRENGTH", "Clear written communication", "Professional strength", LI], ["STRENGTH", "Independent follow-through", "Professional strength", LI],
       ["COMPETENCY", "Executive calendar & scheduling", "Core competency", LI], ["COMPETENCY", "Inbox & correspondence management", "Core competency", LI],
       ["COMPETENCY", "Meeting preparation & follow-through", "Core competency", LI], ["COMPETENCY", "Document & report preparation", "Core competency", LI],
       ["COMPETENCY", "Travel and logistics coordination", "Core competency", LI], ["COMPETENCY", "Online research & summarization", "Core competency", LI],
       ["COMPETENCY", "Confidential information handling", "Core competency", LI], ["COMPETENCY", "Stakeholder communication", "Core competency", LI],
       ["COMPETENCY", "Remote work & self-management", "Core competency", LI], ["EDUCATION", "BS Information Systems", "Clarendon College", LI],
       ["LANGUAGE", "English", "Professional", LI], ["LANGUAGE", "Tagalog", "Native", LI]]
one(r"var CERTS=\[\[.*?\]\];\n", "var CERTS=" + json.dumps(STR, ensure_ascii=False) + ";\n", re.S, True)

# ---------------------------------------------------------------- voice + rider lines, pads, letters, resume
one(r"var VOT=\{.*?\};\n", """var VOT={home:"Welcome to Manila. I'm Jade Patrick Mendoza, executive assistant and executive virtual assistant from Taguig. Drive the jeepney to any landmark and I'll show you what I do.",journey:"Banaue. Six years leading community youth programs, then the Vice Mayor's office in Mansalay, a telco account at Alorica, and now financial accounts at Infosys BPM.",expertise:"Giza. Four things I do: executive calendar and inbox, meeting preparation and follow-through, financial account operations with regulatory controls, and SEO and AEO for WordPress sites.",skills:"Paris. The tools: Google Workspace, Outlook and Teams, Salesforce CRM, Drive and Dropbox, Copilot, and on the SEO side WordPress, Search Console, Analytics, SEMrush and Ahrefs.",projects:"The boardwalk. Five boards: the Vice Mayor's office, Infosys, Alorica, six years of youth leadership, and the SEO and AEO track.",certs:"Rome. Eighteen banners: professional strengths, core competencies, education and languages. Click a banner to open my LinkedIn.",contact:"New York. Open to remote work. Send a message on a pad, or email me. I read every message."};
""", re.S, True)
one(r"var DL=\{.*?\};", "var DL={home:'Manila first. Home base, and where the jeepney is parked.',journey:'Banaue. Youth leader, then the Vice Mayor’s office, then Infosys.',expertise:'Four pyramids. Calendar, meetings, financial accounts, SEO.',skills:'The tools I open every morning.',projects:'The boards. Every line is from the resume.',certs:'Eighteen banners. Strengths, competencies, education.',contact:'Send a message here. I answer fast.'};", re.S, True)
one("""[['EMAIL','mailto:markedcel06@gmail.com'],['LINKEDIN','https://www.linkedin.com/in/mark-edcel-lopez-513509216/'],['ONLINEJOBS.PH','https://www.onlinejobs.ph/jobseekers/info/4576592'],['GITHUB','https://github.com/referrernation-web']]""",
    f"""[['EMAIL','mailto:{EMAIL}'],['LINKEDIN','{LI}'],['RESUME PDF','{PDF}'],['CLASSIC PAGE','../']]""")
one("window.open('../assets/Mark-Edcel-Lopez-Resume-2026.pdf','_blank','noopener')", f"window.open('{PDF}','_blank','noopener')")
one("['M','A','R','K'].forEach(function(ch,i){addProp('box',-4.5+i*3,4,{ch:ch})});", "['J','A','D','E'].forEach(function(ch,i){addProp('box',-4.5+i*3,4,{ch:ch})});")
one("q.fillText('HERO REEL',256,130);", "q.fillText('INTRO REEL',256,130);")
one("v.src='../video/heroreel.mp4';", "v.src='../video/intro.mp4';")
# voice lines may have no mp3 yet: show the subtitle for a few seconds instead of failing silently
one("a.play().catch(function(){subEl.classList.remove('on')})", "a.play().catch(function(){voCur=null;setTimeout(function(){subEl.classList.remove('on')},Math.min(9000,2500+VOT[id].length*45))})")

# ---------------------------------------------------------------- the mount: a kit jeepney replaces the procedural dog; Jade = the rider
# no kimpoy rig: the jeep is added to DOG once kit.glb is in; the procedural dog body is hidden. ponytail: one merged mesh, no spinning wheels.
one("GL.load('models/kimpoy-rig.glb?v='+FIGV,function(gl){var root=gl.scene,mesh=null;root.traverse(function(m){if(m.isSkinnedMesh)mesh=m});if(!mesh)return;",
    "(function addJeep(){if(!KIT.jeep){setTimeout(addJeep,150);return}var g=KIT.jeep.clone(),ka=g.attributes.color,cc=new THREE.Color(0x" + TEAL + ");"
    "if(ka){var arr=new Float32Array(ka.count*3);for(var i=0;i<ka.count;i++){var a=ka.itemSize>3?ka.getW(i):1,t=a>.95?1:0;arr[i*3]=ka.getX(i)*(1+t*(cc.r-1));arr[i*3+1]=ka.getY(i)*(1+t*(cc.g-1));arr[i*3+2]=ka.getZ(i)*(1+t*(cc.b-1))}g.setAttribute('color',new THREE.BufferAttribute(arr,3))}"
    "var jm=new THREE.Mesh(g,new THREE.MeshStandardMaterial({vertexColors:true,roughness:.6,metalness:.1}));jm.castShadow=true;var sc=3.6/5;jm.scale.set(sc,sc,sc);jm.rotation.y=-Math.PI/2;jm.position.set(0,-.25,0);jm.userData.jeep=true;DOG.add(jm);FIG.jeep=jm;"
    "var hats=Object.keys(HATM).map(function(k){return HATM[k]});DOG.children.forEach(function(ch){if(ch!==jm&&!ch.userData.rider&&!ch.userData.dianna&&hats.indexOf(ch)<0)ch.visible=false})})();\n"
    " GL.load('models/none-kimpoy.glb?v='+FIGV,function(gl){var root=gl.scene,mesh=null;root.traverse(function(m){if(m.isSkinnedMesh)mesh=m});if(!mesh)return;")
one("GL.load('models/dianna-anim.glb?v='+FIGV,function(gl){setupDianna(gl,gl.animations)},undefined,function(){GL.load('models/dianna-rig.glb?v='+FIGV,",
    "GL.load('models/jade-anim.glb?v='+FIGV,function(gl){setupDianna(gl,gl.animations)},undefined,function(){GL.load('models/jade-rig.glb?v='+FIGV,")
# no rigged Jade yet: give the procedural rider a seat so dismount / walk / call-the-jeep still work (FIG.dia = dummy inside the group, no bones to pose)
one("function(gl){setupDianna(gl,null)},undefined,function(){})});",
    "function(gl){setupDianna(gl,null)},undefined,function(){procSeat()})});"
    " function procSeat(){if(FIG.onSeat)return;var Dg=DOG.children.filter(function(c){return c.userData.dianna})[0];if(!Dg)return;var seat=new THREE.Object3D();seat.position.copy(Dg.position);DOG.add(seat);Dg.position.set(0,0,0);seat.add(Dg);Dg.userData.rider=true;var dummy=new THREE.Object3D();Dg.add(dummy);FIG.dia=dummy;FIG.seat=seat;FIG.diaYs=0;FIG.diaZs=0;FIG.onSeat=true;RIDE.on=true;RIDE.ph='ride';mountUI()}")
# procedural rider recoloured to Jade while the Rodin/UniRig figure is pending: tan skin, short black hair, teal polo, dark slacks
one("var JKM=new THREE.MeshStandardMaterial({map:TEX('dianna-jacket.jpg',1,false),roughness:.75,metalness:0});",
    "var JKM=new THREE.MeshStandardMaterial({color:0x" + TEAL2 + ",roughness:.8,metalness:0});var SKM=new THREE.MeshStandardMaterial({color:0xc68a5a,roughness:.7,metalness:0});")
one("JK.position.set(0,.52,0);JK.scale.set(1.3,1.42,1.12);D.add(JK);", "JK.position.set(0,.52,0);JK.scale.set(1.1,1.3,.95);D.add(JK);")
one("bx(.62,.12,.52,0x1d3aa8,0,.24,0,D);", "bx(.62,.12,.52,0x22262e,0,.24,0,D);")
one("var hd=new THREE.Mesh(new THREE.SphereGeometry(.07,7,6),mat(0xf1c9a5));", "var hd=new THREE.Mesh(new THREE.SphereGeometry(.07,7,6),SKM);")
one("var ft=new THREE.Mesh(new THREE.SphereGeometry(.07,7,6),mat(0xf1c9a5));", "var ft=new THREE.Mesh(new THREE.SphereGeometry(.07,7,6),mat(0x1a1a1f));")
one("var DHM=new THREE.MeshStandardMaterial({map:TEX('dianna-head.jpg',1,false),roughness:.8,metalness:0});", "var DHM=SKM;")
one("var HRM=new THREE.MeshStandardMaterial({map:TEX('dianna-hair.jpg',1,false),roughness:.9,metalness:0});", "var HRM=new THREE.MeshStandardMaterial({color:0x15120f,roughness:.9,metalness:0});")
one("var BH=new THREE.Mesh(new THREE.BoxGeometry(.64,.7,.2),HRM);BH.position.set(0,-.2,-.3);HAIR.add(BH);", "")
one("[[-.33,0],[.33,0]].forEach(function(q){var st=new THREE.Mesh(new THREE.BoxGeometry(.14,.6,.2),HRM);st.position.set(q[0],-.12,-.05);HAIR.add(st)});", "")
# procedural dog materials: no fur textures shipped (the dog is hidden anyway)
one("var FURM=new THREE.MeshStandardMaterial({map:TEX('kimpoy-fur.jpg',1.2),roughness:1,metalness:0});", "var FURM=new THREE.MeshStandardMaterial({color:0x" + TEAL + ",roughness:.6,metalness:0});")
one("var SHELLM=window.SHELLM=new THREE.MeshStandardMaterial({map:TEX('fur-shell.png',2.4),transparent:true,alphaTest:.3,depthWrite:false,roughness:1,side:THREE.DoubleSide,color:0x8a847a});",
    "var SHELLM=window.SHELLM=new THREE.MeshStandardMaterial({transparent:true,opacity:.0,depthWrite:false,roughness:1,side:THREE.DoubleSide,color:0x8a847a});")
one("var HEADM=new THREE.MeshStandardMaterial({map:TEX('kimpoy-head.jpg',1,false),roughness:1,metalness:0});", "var HEADM=new THREE.MeshStandardMaterial({color:0x" + TEAL + ",roughness:.6,metalness:0});")
# rider seat height on the jeepney roof (procedural rider group sits at D.position)
one("var D=new THREE.Group();D.position.set(0,1.5,-.25);D.userData.dianna=true;DOG.add(D);", "var D=new THREE.Group();D.position.set(0,1.85,-.15);D.userData.dianna=true;DOG.add(D);")

# ---------------------------------------------------------------- palette + names
s = s.replace("8a1c2b", TEAL).replace("d8293f", TEAL2)
s = s.replace("Mark's", "Jade's").replace("Mark&#39;s", "Jade&#39;s").replace("Mark\\'s", "Jade\\'s").replace("Mark Edcel Lopez", "Jade Patrick Mendoza")
s = s.replace("markedcel06@gmail.com", EMAIL).replace("https://www.linkedin.com/in/mark-edcel-lopez-513509216/", LI)
s = s.replace("referrernation-web.github.io/portfolio", "referrernation-web.github.io/jade")
s = s.replace("Kimpoy!", "Jeepney!").replace("Kimpoy", "the jeepney").replace("Dianna", "Jade").replace("bark", "honk").replace("Bark", "Honk")
s = s.replace("BABA (G)", "GET OFF (G)").replace("SAKAY (G)", "GET ON (G)").replace("SIPOL (G)", "CALL JEEP (G)")
left = re.findall(r"Mark\b|Makati|Coggno|Bytown|markedcel|Papa", s)
print("patched; leftovers:", len(left), sorted(set(left)), "| size", len(s) // 1024, "KB")
P.write_text(s, encoding="utf-8")
