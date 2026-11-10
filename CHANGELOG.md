# Changelog

Every published version, newest first (from the git history). Good points to go back to:
`3294d46` (first site), `926caaa` (5 Nov night, before the big layout change), `f86631c` (golden layout, beat glow restored, checks added).

To bring back an older version of the page: `git checkout <id> -- index.html`, then commit.

## 2026-11-11

- Photo book: "Cooking the bhog" now marked 2025.
- Drawings: a5 (the thatched house, group A) replaced with a fresh flat scan.
- Falling jaba flowers removed (markup, CSS, JS, beat gust); restore from commit d7af3f5.
- Adaptive photos: every photo also saved at 640 px and 1200 px (name@640.jpg / name@1200.jpg, list in img/sizes.json); the page gives each <img> a srcset, so phones download the small copy and large screens the full original. Originals untouched. Blurred book backdrop reuses the downloaded copy; full poster loads only when opened.
- Falling jaba flowers removed (markup, CSS, JS and the beat gust); restore point commit d7af3f5. Speed: heavy photos recompressed (~1.3 MB less), full-size poster no longer downloaded until opened.
- Drawings, group A (a1–a7): each paper perspective-corrected onto a true A-size sheet (1:1.414), nothing trimmed; paper whitened, colours lifted slightly. a7 from a fresh flat scan.
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
- Chanda updated: ₹34,726 from 66 receipts (added cash 54–59 of 6 Nov and online 61–67). Distribution bands and "still needed" (₹12,474) updated.

## 2026-11-06

- Printing donated by Somdeep Kundu: ✓ দান in the expense list (Other) and in special donations
- Schedule: "বসে আঁকো" drawing competition card (date, venue, groups, paper, contact) with the poster in the page language, full size on tap
- Expenses: the next three still-needed items shown openly with sponsor links; "বিস্তারিত" became a clear "সব খরচ দেখুন ও স্পনসর করুন" button
- Laddu donated by Suparna (Mampi) Dey: marked ✓ দান in the expense list, left out of the amount needed (₹47,200; ₹16,429 to go), added to special donations
- Easier to use: slim section bar, share button, add to calendar (all times, reminders) + Google Calendar, directions button, photo book pause/play, faint notes easier to read
- Chanda: give by UPI to Somdeep Kundu (QR on laptops, button on phones), then WhatsApp name and amount for the digital receipt
- Front-page photos (pandal, bhog, drawing) move slowly and gently again; photo book unchanged
- Photo book: moving photos back, about twice as fast (≈80 px/s, short rests); neighbouring photos glide in opposite directions; book turns every 6.5 s so each glide finishes
- `14e60ce` Photo book: whole photos with a soft blurred fill (replaced next); singer credit
- `94c2052` Photo book: group photos glided right to left (replaced next by whole photos)
- `77d453a` Music label each time the music starts (বাংলা → हिन्दी → English); switch in the same order
- `3336cca` Changelog: restore points by commit id
- `f86631c` Beat glow back on the title, red strip and music button; flowers' glow breathes again; features checklist, changelog and smoke test added
- `e9ebd4f` Softer, smaller music label
- `b123651` First visit: a quiet 'Shyama Sangeet on / off' label beside the music button
- `3ea274c` Quiet Bengali touches on the white pages: alpona, akash prodip, clay diyas; pause loops off screen
- `bd021d6` Golden-ratio spacing; captions inside photos; two-photo spreads; sliding photos; swipe hint; lighter images and effects

## 2026-11-05

- `926caaa` Photo book: 'Slide to begin…' on the first page; music button tucks aside over the book
- `6fe9550` Contacts: Surajit above Somdeep
- `a28752b` Spelling: Rabindranath
- `25b6e87` Rabindronath (Robi) Banerjee
- `1fc9669` Projected expenses in Bengali, English and Hindi
- `432f7f6` Theme names: Auto, Day, Night
- `5aaa526` Theme: auto by India time, Daylight, Amavasya night
- `f5ef430` Flowers in three depths, with a faint glow behind that breathes and swells on the beat
- `7a169bb` Fix broken Bengali/Hindi big text on Safari: no letter-spacing there
- `9a46581` Flowers: gentle gust on the beat drop; fall only over the first two panels
- `19c5a44` Jaba flowers: more on wide screens, larger, drifting sideways
- `e38b4db` Remove the unused 'year not known' text
- `17d881c` Trigger Pages rebuild
- `5bfb33a` Photo book: no 'year not known' label
- `f02a90c` Title, red strip and music button glow with the bass while music plays
- `5720007` Music with a big mute button, and falling jaba flowers
- `ccc5f6d` Special donations: Rudrani De (Sasa), Udayan Sengupta (Bile da)
- `7eda90f` Big group link back to its old wording
- `23d00ee` Call it the community WhatsApp group
- `ace8d50` Live countdown to the puja in place of the percentage
- `4a00246` Boxes are the sound system: move to Power & sound
- `bf99a1b` Bring back the Bengali / English / Hindi switch; expenses stay in English
- `cf11a21` Itemised expenses with covered/still-needed dots and a sponsor link per item
- `237dee5` Sponsor line: Rabi Banerjee, Contact, WhatsApp group
- `8d73fb8` Projected expenses as a clay bhar; breakdown on tap; sponsor contacts
- `74d68c2` Projected expenses: a jar that fills with chanda collected
- `462a2f6` English only; hide tap hint; small hidden-names note
- `d6744d4` Donation statistics: drop the due row and the by-day list; add special donations
- `678f206` Chanda: bar charts by gift size and by day; tap a bar for count and total, no names
- `a928b8b` Show schedule and chanda lines: fade-in now runs after they are drawn
- `598c2ed` Fix share-preview URLs to the live site path so the WhatsApp image loads
- `9609007` Chanda: receipts 46-53 (5 Nov), total 30,771
- `57dcea9` Gentle drift on the book's photos; artwork stays still
- `87df16b` Show the normal arrow over plain text; hand only on links and buttons
- `9352c08` Use Anek Devanagari for the Hindi text
- `ab761e0` Add English, Bengali and Hindi language switch; WhatsApp group link with year
- `d32756a` Add a subtle earthy grain texture across the page
- `5e9838d` Footer: keep committee name only

## 2026-11-04

- `40a9f25` Update WhatsApp group link
- `fcaef62` Add 2022 photos to photo book
- `e31c2a3` Add 2020 photos to photo book
- `3294d46` Mission Para Kali Puja 2026 website
