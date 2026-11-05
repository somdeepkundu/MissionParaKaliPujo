# মিশন পাড়া কালীপুজো ২০২৬

Website for Mission Para Kali Puja, Upper Mission Para, Adra.
Sunday 8 November 2026, Dipanwita Amavasya.

**Live:** https://somdeepkundu.github.io/MissionParaKaliPujo/

## Updating the site

Everything that changes lives in one block near the bottom of `index.html`,
marked `EDIT HERE`:

- `chanda.total`, `chanda.receipts`, `updated`: the chanda figures and the date
- `schedule`: times and events (start/end are India time; they light up "now" and "next")
- `committee`: names and phone numbers
- `photos`: the photo book, in order. Put the file in `photos/<year>/` and add a line.
  Use `year: ""` when the year is not known.

To preview a moment on puja night, open the page with `?demo=2026-11-08T21:10`.

## Before every push

1. `python3 tests/smoke.py` must end with `ALL GOOD` (it checks every feature in `FEATURES.md` on a phone and a laptop).
2. Add a line to `CHANGELOG.md` if you changed what people see.

## Files

- `index.html`: the whole page
- `og.jpg`: the picture WhatsApp shows when the link is shared
- `img/`: hero pictures, the hibiscus logo, Ma's face from the receipt
- `photos/`: the photo book
- `fonts/`: Anek Bangla (SIL Open Font License)
- `music/`: the Shyama Sangeet clip (credit in the footer)
- `FEATURES.md`, `CHANGELOG.md`, `tests/smoke.py`: what the site does, what changed, and the check that nothing went missing

Made by Somdeep Kundu.
