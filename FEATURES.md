# Features checklist

Everything the site does today. Before every push, run `python3 tests/smoke.py`: it checks each item marked ✓ on a phone and a laptop
and stops with `FAIL` if anything has gone missing. Items without ✓ need a quick look by eye.

## Top of the page
- ✓ Big title "মিশন পাড়া / কালীপুজো ২০২৬" fitted to the screen width
- ✓ Countdown tiles, panjika button, arati and night-bhog times, WhatsApp group tile
- ✓ Theme button: অটো (by India time: day 6 am–5:30 pm) → দিন → রাত
- ✓ Language switch: বাংলা · हिन्दी · English (everything switches, including projected expenses)
- Bengali and Hindi big text has no letter-spacing (Safari draws broken letters otherwise)

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
- Bhog photo with caption inside, slowly sliding
- ✓ Akash prodip hanging by its string, swaying, soft glow

## Photo book
- ✓ Every page is a photo with year (marigold) and caption on it; ✓ photos glide (≈80 px/s, short rests), one left→right, the next right→left; Maa's artwork first, never moves
- ✓ Laptop: two photos per spread, 3D page turn ~0.75 s (8 spreads). Phone: one photo per page (15 pages), quick slide right to left
- ✓ Turns by itself every ~6.5 s while on screen (back to the start after the last page); ✓ any touch, click or key leaves it alone for 12 s
- The next two pages are loaded ahead, so a turn never shows an empty page
- ✓ First time only: fingertip hint + page lift; "Slide to begin →" on the art page
- ✓ Music button tucks aside while the book is on screen
- Last page: "More photos?" with the WhatsApp link, then a red "জয় মা কালী" page on laptops

## Chanda (white)
- ✓ Total ₹30,771, receipts, days; the drawing with caption inside; ✓ three clay diyas with live flames under it
- ✓ UPI-তে চাঁদা দিন: pay Somdeep Kundu (papaisomdeepkundu@okaxis) — QR code on laptops, "Open in a UPI app" button on phones, copy button; then WhatsApp Somdeep (ready message) with name and amount for the digital receipt
- ✓ Clay bhar fills to the share collected; live countdown to the puja; ₹ still needed
- ✓ Details: 19 expense items in 5 groups, dots for covered / part / still needed, "Sponsor this → WhatsApp Robi da" with a ready message
- ✓ Sponsor line: Rabindranath (Robi) Banerjee (phone), Contact, community WhatsApp group
- ✓ Donation statistics (4 bands, no names) and special donations (Murti — Rudrani De (Sasa); night bhog — Udayan Sengupta (Bile da))
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
