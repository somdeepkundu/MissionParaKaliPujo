# Features checklist

Everything the site does today. Before every push, run `python3 tests/smoke.py`: it checks each item marked ✓ on a phone and a laptop
and stops with `FAIL` if anything has gone missing. Items without ✓ need a quick look by eye.

## Top of the page
- ✓ Big title "মিশন পাড়া / কালীপুজো ২০২৬" fitted to the screen width
- ✓ Countdown tiles, panjika button, arati and night-bhog times, WhatsApp group tile
- ✓ Theme button: অটো (by India time: day 6 am–5:30 pm) → দিন → রাত
- ✓ Language switch: বাংলা · हिन्दी · English (everything switches, including projected expenses)
- Bengali and Hindi big text has no letter-spacing (Safari draws broken letters otherwise)

## Getting around
- ✓ Slim bar of section links (নির্ঘণ্ট · ছবি · চাঁদা · যোগাযোগ + share) appears once the top is scrolled past; ✓ marks the section you are in
- ✓ Share button (bar and Contact): the phone's share sheet, or WhatsApp with the link where there is none
- ✓ Schedule: "ক্যালেন্ডারে রাখুন" file with all 7 puja times and 30-minute reminders; ✓ Google Calendar link for the puja start
- ✓ Contact: "পথ দেখান · Google Maps" button
- Faint notes (donor names hidden, expense note, music credit) a little larger and darker; bigger copy / pause buttons

## Music and motion
- ✓ Shyama Sangeet "আমার মায়ের চরণ বুকে ধরেছি" starts on the first tap; big red button mutes / plays; choice remembered
- ✓ First visit only: small "শ্যামাসংগীত চালু / বন্ধ" label beside the button
- ✓ Every time the music starts: "শ্যামাসংগীত চলছে · থামাতে এখানে চাপুন" with three moving marigold bars, ~4.5 s; not when it quietly resumes after a tab switch
- The label speaks in turn: বাংলা → हिन्दी → English (Hindi uses the phone's own font unless the page is in Hindi)
- ✓ Beat glow while music plays: gold glow behind "কালীপুজো ২০২৬", red strip brightens, red halo on the button, glow behind the flowers
- Beat drop: flowers lean gently for a moment (at most once every 7 s)
- ✓ Falling jaba flowers in three depths (7 on a phone, 13 on a laptop), only over the first two panels, faint breathing glow behind them
- Music pauses when the tab is hidden; everything still with "reduce motion"

## Invitation (white)
- Title, invitation text and four dates beside the pandal photo (1 : 1.618)
- Caption inside the photo; photo moves slowly and gently (front-page photos are calmer than the photo book)
- ✓ Faint alpona lotus behind, turning very slowly, drifting with the scroll

## Schedule (white)
- ✓ Two days of rows; the current row lights up, the next one says "এর পরে"
- ✓ বসে আঁকো card: 9 Nov 10 am, Gora Da's house, groups ক/খ/গ, paper provided, call Somdeep; ✓ poster in the page language (bn / en / hi), ✓ opens full size
- Bhog photo with caption inside, slowly sliding
- ✓ Akash prodip hanging by its string, swaying, soft glow

## Photo book
- ✓ Every page is a photo with year (marigold) and caption on it; ✓ photos glide (≈80 px/s, short rests), one left→right, the next right→left; Maa's artwork first, never moves
- ✓ Laptop: two photos per spread, 3D page turn ~0.75 s (8 spreads). Phone: one photo per page (15 pages), quick slide right to left
- ✓ Pause / play button beside the page number; ✓ turns by itself every ~6.5 s while on screen (back to the start after the last page); ✓ any touch, click or key leaves it alone for 12 s
- The next two pages are loaded ahead, so a turn never shows an empty page
- ✓ First time only: fingertip hint + page lift; "Slide to begin →" on the art page
- ✓ Music button tucks aside while the book is on screen
- Last page: "More photos?" with the WhatsApp link, then a red "জয় মা কালী" page on laptops

## Chanda (white)
- ✓ Total ₹30,771, receipts, days; the drawing with caption inside; ✓ three clay diyas with live flames under it
- ✓ UPI-তে চাঁদা দিন: pay Somdeep Kundu (papaisomdeepkundu@okaxis) — QR code on laptops, "Open in a UPI app" button on phones, copy button; then WhatsApp Somdeep (ready message) with name and amount for the digital receipt
- ✓ Clay bhar fills to the share collected; live countdown to the puja; ₹ still needed
- ✓ Next three still-needed items always visible, each with a sponsor link
- ✓ "সব খরচ দেখুন ও স্পনসর করুন" button: 20 expense items in 5 groups, dots for covered / part / still needed / ✓ donated (donated items shown with the giver and left out of the amount needed), "Sponsor this → WhatsApp Robi da" with a ready message
- ✓ Sponsor line: Rabindranath (Robi) Banerjee (phone), Contact, community WhatsApp group
- ✓ Donation statistics (4 bands, no names) and special donations (Murti — Rudrani De (Sasa); night bhog — Udayan Sengupta (Bile da); laddu — Suparna (Mampi) Dey; printing — Somdeep Kundu)
- Note: donor names deliberately hidden; murti and night bhog not counted in expenses
- ✓ Faint alpona in the corner

## Contact and footer
- ✓ Contacts in order: Rabindranath (Robi) Banerjee, Surajeet Chell, Somdeep Kundu
- ✓ "Join the WhatsApp group (2026)" big link; Google Maps link
- ✓ Music credit: song, ✓ singer (কণ্ঠ: অনুরাধা পড়োয়াল), YouTube link; committee line; big wordmark

## Speed
- Photos at most 1600 px; Maa's artwork 77 KB; book photos load only near the book
- Every looping animation pauses off screen; only transform / opacity / filter change each frame
- ✓ No broken images, no script errors; ✓ share preview image (og.jpg)

## 2026-11-11

- Drawings: group A (a1–a6) redone as flat scan-style crops: straightened to the paper edges, seat background removed, paper whitened, colours lifted slightly.
- Drawings: a7 (the night-sky drawing, group A) replaced with a clean flat scan.
- Drawings: c3 (the swirl drawing, group C) replaced with a clean flat scan, upright.

## 2026-11-10

- Final chanda: ₹52,883 from 102 receipts (last ones 77–80 added).
- Countdown to next Kali Puja (Thu 28 Oct 2027, 6:30 pm assumed; SITE.nextPuja): the bhar shows days/hours/minutes/seconds "until next Kali Puja", and the top line reads "See you next year · N days to go".
- Photo deck: 8 photos of the games, sindoor khela and bisarjan added at the front (3 languages).

## 2026-11-09

- Photo deck retitled from "Tonight, 2026 · Puja night" to "8–9 November 2026 · This year's puja" (puja is over); live dot removed.
- Photo deck: two bhog photos (eating together, serving) added at the front.
- Drawings slideshow: the two Shivling drawings (a2, c2) are never shown one after the other (SITE.artApart), including across the loop.
- New section #anko "ছোটদের আঁকা" (Sit & Draw 2026 drawings): plays by itself in random order with a slow drift (zoom in or out) and crossfade; whole drawing always visible; filter by group ক/খ/গ (no ranking); swipe, arrows, thumbnails; tap for full size; share button sends …/#anko to WhatsApp. Drawings perspective-corrected from the photos and lightly cleaned (paper whitened, colours lifted), in photos/2026/art/.
- Sit & Draw 2026 photo: shown in the spotlight band as "Happening now" (until 1 pm) and added to the front of the photo deck.
- Restore point before this change: branch `layout-before-sitdraw` (commit e3c746a). To go back: `git checkout layout-before-sitdraw -- index.html`.
- Time-boxed notices (SITE.notices): yesterday's prasad note retired; today's Sit & Draw note (3 languages) shows under the hero until 1 pm IST.
- Spotlight (SITE.spotlight): the Sit & Draw card is lifted to just under the hero until 1 pm IST on 9 Nov, then returns to its place in the schedule by itself.

## 2026-11-08

- Hero now shuffles between 3 photos of this year each visit (arati crowd, full Maa, close-up), each with its own ~4s move: push in toward Maa through the crowd, zoom to her face, or pull back from her eyes; all brighten from dim.
- Tonight deck: gate and lit lane photos first, credited to Dipam (camera watermark cropped).
- Tonight deck: +3 photos (hom fire, chanting & hom, elders).
- New "Tonight, 2026" section after the schedule: a deck of this year's photos (polaroid stack). Drag or tap to send the top card back; deals in when scrolled into view; keyboard arrows too. Photos in photos/2026/.
- Puja-evening notice under the hero (3 languages, pulsing dot): bring prasad thali now; auto-hides at 8 pm IST.
- Founding year corrected to 1993 (34th puja); hero line and photo book subtitle.
- Hero cinematic reworked: 4s zoom IN (done before most people scroll) toward Maa's face while the image brightens from dim.
- Hero: new full Maa photo (img/maa-2026-hero.jpg) with a cinematic rise-from-dark slow push-in and soft vignette; the close-up moved into the intro photo (replacing the daylight pandal, which stays in the book).
- Front photo is now this year's Maa (img/maa-2026.jpg); the old lamps photo stays in the photo book.
- Costing note under the bhar (3 languages): estimates are mostly from last year; several heads will rise this year.
- Receipts 74–76 added: chanda ₹50,782 from 98 receipts.
- Book B (receipts 1B–24B) added: chanda ₹50,081 from 95 receipts; goal reached. 8B (₹3,300, Rudrani De, Protima) left out of the site total since the murti is already shown as donated.

## 2026-11-07

- Chanda ₹38,726 from 73 receipts (added 60, 72, 73); still needed ₹8,074.
- Chanda ₹37,326 from 70 receipts (added cash 68); still needed ₹9,474.
- Chanda ₹36,576 from 69 receipts (added UPI 69–71 of 7 Nov); still needed ₹10,224.
- 20th year: "Since 2007 · our 20th puja" line under the hero name; photo book subtitle now says since 2007 (was 2016).
- Poster viewer rebuilt as a plain overlay (was <dialog>), so the full-size poster shows on iPad Safari; Esc / tap outside / ✕ close it.
- Chanda slips (₹400) marked donated by Somdeep; still needed now ₹12,074.
- Sponsor line now reads "Chanda slips, printing etc." — Somdeep Kundu.
- Chanda total ₹34,726 / 66 receipts; bhar shows ₹12,474 still needed.

