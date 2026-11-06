"""
Smoke test for the Mission Para Kali Puja site.
Run before every push:   python3 tests/smoke.py
It serves the folder on a local port, opens the page as a phone and as a laptop,
and checks every feature listed in FEATURES.md. It prints FAIL lines and exits 1 if anything broke.
Needs: pip install playwright (Chromium).
"""
import http.server, os, socketserver, sys, threading
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fails = []
def check(name, ok, info=""):
    print(("ok   " if ok else "FAIL ") + name + (f"  [{info}]" if info and not ok else ""))
    if not ok: fails.append(name)

class Quiet(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=ROOT, **k)
    def log_message(self, *a): pass
srv = socketserver.TCPServer(("127.0.0.1", 0), Quiet); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
URL = f"http://127.0.0.1:{port}/index.html"

with sync_playwright() as p:
    b = p.chromium.launch(args=["--no-sandbox", "--autoplay-policy=no-user-gesture-required"])
    for label, w, h in (("phone", 390, 844), ("laptop", 1440, 900)):
        print(f"\n— {label} {w}×{h}")
        pg = b.new_page(viewport={"width": w, "height": h}); errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(URL + "?lang=bn"); pg.wait_for_timeout(900)
        J = pg.evaluate
        # hero
        check("hero title fits the width", J("document.querySelector('.band h1').scrollWidth <= document.querySelector('.band').clientWidth + 2"))
        check("countdown tiles filled", bool(J("document.getElementById('count').textContent.trim()")))
        # theme: auto → day → night → auto
        seq = []
        for _ in range(3): pg.click("#theme"); seq.append(J("document.documentElement.dataset.mode"))
        check("theme cycles auto/day/night", seq == ["day", "night", "auto"], str(seq))
        # languages
        texts = {}
        for i, l in enumerate(("bn", "en", "hi")):
            pg.click(f".lang button >> nth={i}"); pg.wait_for_timeout(150); texts[l] = J("document.querySelector('#ch-h').textContent")
        check("language switch changes text", len(set(texts.values())) == 3, str(texts))
        pg.click(".lang button >> nth=0"); pg.wait_for_timeout(150)
        # flowers
        n = J("[...document.querySelectorAll('.jaba i')].filter(e=>getComputedStyle(e).display!='none').length")
        check("jaba flowers falling (7 phone / 13 laptop)", n == (7 if w < 760 else 13), str(n))
        check("flowers have three depths", J("document.querySelectorAll('.jaba i.far').length>0 && document.querySelectorAll('.jaba i.near').length>0"))
        # music
        check("music file and button", J("!!document.getElementById('song') && !!document.getElementById('music')"))
        check("music label shows on first visit", J("document.getElementById('mtip').classList.contains('on')") or J("document.getElementById('mtip').textContent.length>0"))
        check("title beat-glow copy is in place", J("(()=>{const h=document.querySelector('.band h1').getBoundingClientRect(),g=document.querySelector('.tglow');if(!g)return false;const r=g.getBoundingClientRect();return Math.abs(h.x-r.x)<2&&Math.abs(h.y-r.y)<2})()"))
        pg.mouse.click(w // 2, h - 150); pg.wait_for_timeout(4000)
        beats = []
        for _ in range(25): beats.append(float(J("document.querySelector('.band').style.getPropertyValue('--beat')||0"))); pg.wait_for_timeout(80)
        check("label speaks when the music starts", J("document.getElementById('mtip').classList.contains('live')"))
        check("music plays and the beat drives the glow", max(beats) > .2, f"max {max(beats)}")
        check("red strip brightens on the beat", "brightness" in J("getComputedStyle(document.querySelector('.marquee')).filter"))
        pg.click("#music"); pg.wait_for_timeout(200)
        check("mute button stops the music", J("document.getElementById('song').paused"))
        check("share preview image set", "og.jpg" in (J("(document.querySelector('meta[property=\"og:image\"]')||{}).content") or ""))
        # schedule
        check("schedule has its rows", J("document.querySelectorAll('#table .row').length") >= 7)
        ics = J("fetch(document.getElementById('cal-ics').href).then(r=>r.text())")
        check("calendar file has all 7 puja times with reminders", ics.count("BEGIN:VEVENT") == 7 and ics.count("TRIGGER:-PT30M") == 7 and "DTSTART:20261108T130000Z" in ics, ics[:120])
        check("Google Calendar link for the puja start", "dates=20261108T130000Z" in J("document.getElementById('cal-g').href"))
        pg.locator("#schedule").scroll_into_view_if_needed(); pg.wait_for_timeout(700)
        check("slim section bar shows below the top", J("document.getElementById('topbar').classList.contains('on')"))
        check("slim bar marks the current section", J("(document.querySelector('#topbar a.cur')||{}).getAttribute?.('href')") == "#schedule", str(J("(document.querySelector('#topbar a.cur')||{}).outerHTML")))
        check("akash prodip hangs in the schedule", J("!!document.querySelector('.sched .lantern svg')"))
        # photo book
        pg.locator("#book").scroll_into_view_if_needed(); pg.wait_for_timeout(1200)
        total = J("document.getElementById('pageno').textContent")
        check("photo book page count", ("১৫" in total) if w < 760 else ("৮" in total), total)
        check("first-time swipe hint shows on the book", J("!!document.querySelector('.hint')"))
        check("music button tucks aside over the book", J("document.getElementById('music').classList.contains('tuck')"))
        check("art page says 'slide to begin'", bool(J("(document.querySelector('.art-pg .go')||{}).textContent")))
        check("art page never moves", J("(()=>{const i=document.querySelector('.art-pg img');return !i.getAnimations().length})()"))
        pg.wait_for_timeout(6600)
        check("book turns by itself while on screen", "২" in J("document.getElementById('pageno').textContent"), J("document.getElementById('pageno').textContent"))
        pg.click("#next"); pg.wait_for_timeout(1100)
        check("next page turns", "৩" in J("document.getElementById('pageno').textContent"), J("document.getElementById('pageno').textContent"))
        check("photo carries year and caption", bool(J("(document.querySelector('#spread .ov .cap')||{}).textContent")))
        check("book photos glide (alternate directions)", J("(()=>{const im=[...document.querySelectorAll('#spread .pg.photo img')];return im.length>0&&im.some(i=>i.getAnimations().length)})()"))
        pg.wait_for_timeout(7000)
        pause_label = J("document.getElementById('bookplay').textContent")
        check("a click stops the book turning by itself", "৩" in J("document.getElementById('pageno').textContent"))
        pg.click("#bookplay"); p0 = J("document.getElementById('pageno').textContent"); pg.wait_for_timeout(13500)
        check("pause button stops the book", J("document.getElementById('pageno').textContent") == p0 and J("document.getElementById('bookplay').getAttribute('aria-pressed')") == "true")
        pg.click("#bookplay"); pg.wait_for_timeout(8200)
        check("play button starts it again", J("document.getElementById('pageno').textContent") != p0, p0)
        # chanda
        pg.locator("#chanda").scroll_into_view_if_needed(); pg.wait_for_timeout(600)
        check("chanda total shown", "৩০,৭৭১" in J("document.getElementById('ch-dl').textContent"))
        c1 = J("document.querySelector('.gfig').textContent"); pg.wait_for_timeout(1200); c2 = J("document.querySelector('.gfig').textContent")
        check("bhar countdown ticks", c1 != c2 or "পুজো" in c1, f"{c1} / {c2}")
        pg.click(".gmore summary"); pg.wait_for_timeout(200)
        check("expenses list has 19 items", J("document.querySelectorAll('.it').length") == 19)
        check("laddu shows donated by Suparna (Mampi) Dey, not counted", "মাম্পি" in J("document.querySelector('.it.gift').textContent") and "১৬,৪২৯" in J("document.querySelector('.gleft').textContent"), J("document.querySelector('.gleft').textContent"))
        links = J("[...document.querySelectorAll('.gspon a')].map(a=>a.getAttribute('href'))")
        check("sponsor line links: phone, contact, group", len(links) == 3 and links[0].startswith("tel:") and links[1] == "#contact" and "whatsapp" in links[2], str(links))
        check("UPI pay: upi link, QR file, WhatsApp receipt message", J("document.querySelector('.pay-btn').href.startsWith('upi://pay?pa=papaisomdeepkundu')") and J("document.getElementById('pay-wa').href.includes('wa.me/919679443301?text=')") and J("document.querySelector('.pay-qr').naturalWidth>0 || document.querySelector('.pay-qr').loading==='lazy'"))
        check("donation bars and special donations", J("document.querySelectorAll('#dist .bar').length") == 4 and J("document.querySelectorAll('.specials li').length") == 3)
        check("diyas and alpona on the white pages", J("document.querySelectorAll('.diya').length") == 3 and J("document.querySelectorAll('.alpona svg').length") == 2)
        # contact + footer
        ppl = J("[...document.querySelectorAll('#people li')].map(l=>l.textContent)")
        check("contacts in order: Robi, Surajit, Somdeep", len(ppl) == 3 and "রবীন্দ্রনাথ" in ppl[0] and "সুরজিৎ" in ppl[1] and "সোমদীপ" in ppl[2], str(ppl))
        check("directions button opens Google Maps", "maps" in J("document.querySelector('.corners .map').href"))
        J("window.open = u => { window.__opened = u; }")
        pg.click(".corners .share"); pg.wait_for_timeout(200)
        opened = J("window.__opened || ''")
        check("share opens WhatsApp with the site link (no share sheet in this browser)", opened.startswith("https://wa.me/?text=") and "MissionParaKaliPujo" in opened, opened[:80])
        check("WhatsApp group link", "chat.whatsapp.com/FfAXltygtUfAkY8qnvqbdy" in J("document.querySelector('.display.wa').href"))
        check("music credit with YouTube link", "youtu" in J("document.querySelector('.credit a').href"))
        check("singer credited (Anuradha Paudwal)", "অনুরাধা" in J("document.querySelector('.credit').textContent"))
        # every image loads
        J("window.scrollTo({top:document.documentElement.scrollHeight,behavior:'instant'})"); pg.wait_for_timeout(1200)
        broken = J("[...document.images].filter(i=>i.complete&&i.naturalWidth===0&&i.getAttribute('src')).map(i=>i.getAttribute('src'))")
        check("no broken images", not broken, str(broken))
        check("flowers rest below the first two panels", "gone" in J("document.querySelector('.jaba').className"))
        check("no script errors", not errs, "; ".join(errs)[:300])
        pg.close()
    b.close()
srv.shutdown()
print("\nALL GOOD" if not fails else f"\n{len(fails)} FAILED: " + ", ".join(fails))
sys.exit(1 if fails else 0)
