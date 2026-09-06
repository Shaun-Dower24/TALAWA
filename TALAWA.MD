# Talawa Caribbean Food — Website Design Proposal

**Status:** proposal, nothing built yet. Read this, pick a direction, then we build.
**Date:** September 2026

---

## 1. What this document is

You asked for ideas before any code gets written. This is that — what the site should
look like, how it should feel, what goes on it, and what I need from you to make it.

I've written it so you can read it without being a developer. There's one technical
section right at the end (section 12) that you can safely skip — it's notes for whoever
builds it, which will be me.

---

## 2. The one thing this site has to do

The site you liked — Straight From Yard (Wray & Nephew) — is a beautiful piece of brand
theatre. But it has no job. Nobody has to *do* anything at the end of it.

Talawa's site has exactly one job:

> **Get a hungry person to the truck on Saturday — or make them save it for next week.**

That changes things. Everything beautiful on this site has to sit *on top of* the useful
stuff, never in front of it. Someone standing in the street at 4pm on a Saturday with one
bar of signal needs to know what's on, where you are, and how much, in about three seconds.

So the rule I'm designing to: **it should look like a record sleeve and work like a menu.**

---

## 3. What I'm taking from the site you liked

I went through their page properly. Here's what's actually good about it and worth stealing:

- **Black background, one loud colour.** Everything is black, and one colour (yellow) does
  all the shouting. Very cheap way to look expensive.
- **Massive type.** Words the size of the whole screen. Some filled in solid, some just an
  outline. The contrast between the two is what makes it look designed rather than just big.
- **Letters that arrive one at a time.** Headlines don't just appear — each letter rises
  and stretches into place a fraction after the one before. Costs nothing, feels expensive.
- **A hand-drawn underline** that draws itself under links when you hover. Small, charming.
- **Torn paper edges** between sections instead of straight lines.
- **A grain texture** over the whole page, very subtle, that stops it looking like clean
  flat digital nothing.
- **The scrolling ticker band** announcing what's on.
- **A round spinning stamp** ("Jamaica, 1891") that rotates as you scroll.
- **The drag-along photo gallery** — you grab it and pull it sideways, with the text
  sitting still next to it.
- **Solid colour label blocks** holding the hard facts.

And here's what I'd leave behind:

- The age gate — obviously not needed.
- The 3D rum glass. It's a genuinely impressive bit of engineering and it would make your
  site slower on exactly the phones your customers use. Not worth it.
- The loading screen. A takeaway site should be *instant*. Making someone wait to look at
  a menu is the wrong trade.
- The trail of photos that follows your mouse. Lovely, but used everywhere it gets silly.
  I'd use it once, on "Find Us", and nowhere else.

---

## 4. The brand read — and why the name is a gift

**Talawa** is Jamaican Patois. It comes from the saying **"wi likkle but wi tallawah"** —
*we're small, but we're mighty.* Small in size, big in strength. It's one of the
best-known phrases in Jamaican English.

You are a one-trailer operation in a pub car park putting out food that beats places ten
times your size.

**The name already is the brand story.** Nothing has to be invented, nothing has to be
exaggerated, and it's true. That's rare and it's worth building the whole site on.

> *Small but mighty.*

*(Worth confirming with the owner that this is the meaning they intended when they named
it — if the name came from somewhere else entirely, tell me and I'll rework it.)*

---

## 5. Three directions

### Direction 1 — "LIKKLE BUT TALAWA" ⭐ **My recommendation**

The site is built on the phrase. Here's what you actually see, top to bottom:

**The opening.** Pure black. Off-centre and quite small, the word **LIKKLE** draws itself
in — outline only, no fill, like it's being written. Half a second of nothing. Then
**BUT TALAWA** slams in underneath at the full width of the screen, in gold, the letters
punching up into place one after another. Underneath, small and neat:
`JAMAICAN FOOD · [YOUR TOWN] · EVERY SATURDAY 4–8PM`.

Behind all of it, barely there, a very dark crop of the jerk chicken photo. Palm leaves
hang in from the top corners and drift slightly when you move the mouse. No video, no
loading screen — it's there the instant the page opens.

As you start to scroll, the translation writes itself in, in a brush script:
*"likkle but talawa — small, but mighty."*

**The Saturday band.** A full-width gold stripe with black text scrolling across it:
`EVERY SATURDAY · 4PM TIL SOLD OUT · MAN IN THE MOON ·` — and it speeds up slightly as
you scroll faster, which is a small thing that people always notice. Underneath, three
big facts, huge: **SAT** / **4–8PM** / **MAN IN THE MOON**.

**The Tray.** This is the centrepiece and the bit people will screenshot. Your actual
foil tray photo fills the whole screen. The page holds still while you scroll, and one
at a time, six labels draw themselves in, each with a little hand-drawn line pointing at
the right part of the plate — *Rice & Peas · Sweet Plantain · Jerk Chicken · Festival ·
Slaw · Mac & Cheese.* Then the labels fade away and one line lands in the middle:

> **One tray. No corners cut.**

**The Menu.** Real text — not a photo of the chalkboard, not a PDF. This matters more
than it sounds: a photo of a menu is invisible to Google, unreadable to anyone using a
screen reader, and unsearchable. Set on a scorched-paper panel, three columns — MAINS /
SIDES / KIDS — each line wiping in with a chalk underline drawing across it, prices in
gold on the right. The allergy notice sits underneath in a bordered box, worded exactly
as it is on the truck.

**The Truck.** The drag-along gallery. Your truck photo, the tray, the new photos you'll
take, and 3–5 short silent clips (chicken turning on the grill, festival hitting the oil,
a tray being handed over). Grab and pull. The text sits still beside it.

**Find Us.** Huge outlined **FIND US**. A map image that opens Google Maps when tapped
(not a heavy embedded map — those are slow), the pub name, postcode, a note about parking,
and two fat buttons: **Directions** and **Call**. The round spinning stamp sits in the
corner reading `★ 5 HYGIENE RATING ★ FRESH · VIBRANT · AUTHENTIC ★`.

**Follow.** A line in the brush script, your Instagram and Facebook with the drawing
underline, hygiene rating, and the practical footer bits.

**Why I'd pick this one:** it's honest — nothing is invented or exaggerated. It puts the
useful information *inside* the good-looking bit rather than making people scroll past
the art to reach the menu. And the tray sequence gives you one genuinely memorable moment
without a single frame of video.

---

### Direction 2 — "SIX TIL SOLD OUT" (the Saturday clock)

The whole site is a countdown. The opening screen is a live counter ticking down to the
next Saturday at 4pm, enormous, with the truck behind it. Scrolling walks you through the
service hour by hour — the grill lights at 4, the queue builds at 5, half the board's gone
by 7, and **SOLD OUT** stamps across the screen in red at 8. Menu items visibly sell out
as you scroll past them.

**Good:** real urgency, and a reason to come back to the site every week.

**Bad:** it's a gimmick, not a brand. The moment your hours change, or you cancel a
Saturday, the site is actively lying to people. And "SOLD OUT" theatre can genuinely talk
someone out of driving over.

**My call:** take the countdown only, drop it into Direction 1 as a small feature near the
top, and leave the rest.

---

### Direction 3 — "STRAIGHT OUTTA THE TRAILER" (the magazine piece)

The opposite of the reference site. Warm off-white paper instead of black, heavy black
type, food photographed huge and left uncropped, loads of breathing room, a quote from the
owner across a full page. Calm, expensive, more Sunday supplement than flyer.

**Good:** it would look like nothing else in the takeaway world, and it ages well.

**Bad:** it lives or dies on the photography — realistically you'd need a half-day with a
proper food photographer before it would work at all. And it throws away the black, green
and gold brand kit you've already paid a designer for. It's also a colder read than this
food deserves.

---

## 6. Art direction

### Colours

Pulled from your existing logo and banner, so the site matches the truck.

| Name | Colour | Where it's used |
|---|---|---|
| Ink | `#080807` | The main background |
| Ink 2 | `#101010` | Panels sitting slightly forward |
| Gold | `#FFC91C` | The main accent — headlines, buttons, the ticker band |
| Deep gold | `#E0A400` | Edges and shadows on the gold |
| Green | `#35B14A` | From the logo — big type and graphics only |
| Deep green | `#0C5C2B` | The darker half of the logo ring |
| Bone | `#F2ECDF` | Body text and paper panels |
| Scotch bonnet | `#E8481B` | Spice markers and "sold out" only — used sparingly |

One note on the green: it's beautiful but it doesn't have quite enough contrast against
black to be legible as small body text. So green gets used for big headlines and graphics,
never for paragraphs. Gold and bone do the readable work. *(Exact values to be sampled
from your original logo files at build time — these are read off the images you sent.)*

### Type

Three typefaces, four jobs:

- **The big shouty one:** Archivo, at its widest and heaviest setting, all caps. This is
  the closest freely-available match to the ultra-wide face the Wray site uses. It carries
  every headline.
- **The handwritten one:** Caveat Brush — for the Patois asides and the slanted little
  callout lines. The Talawa logo script itself gets used as artwork, never re-typed.
- **The label one:** DM Mono, capitals, letters spaced out. This is what makes the price
  lists and fact blocks look authoritative rather than casual.
- **The reading one:** Work Sans, for actual paragraphs.

All four load from your own server rather than Google's — faster, and no cookie/privacy
complications.

### How it should feel to move

**Heavy and confident. Never bouncy.** Nothing springs or wobbles. Everything slides in
and settles, like a tray being put down on a counter. Slow-ish — around a second — and it
stops dead rather than jiggling.

---

## 7. The page, section by section

It's one single page. A food truck does not need five pages, and one page loads faster
and is easier for you to keep updated.

1. **Opening** — the LIKKLE BUT TALAWA moment
2. **Saturday band** — when and where, in letters you can read from across the room
3. **The Tray** — the annotated plate
4. **The Menu** — mains, sides, kids, prices, allergy notice
5. **The Truck** — drag-along gallery of photos and short clips
6. **Find Us** — map, address, parking, Directions and Call buttons, **and the ordering block**
7. **Follow** — socials, hygiene rating, footer

### About the ordering block

You said you're not sure yet how you want people to order. That's completely fine — I'll
build that block as a swappable panel so it can become any of these later **without
redesigning the page**:

- *Just turn up* — "no need to order ahead, come find us"
- *Ring or DM to pre-order* — big tap-to-call and WhatsApp buttons
- *Order and pay online* — a proper ordering system

The third one is a much bigger piece of work (it needs payment handling and a way for you
to see orders coming in), so if you head that way it's a separate conversation. The first
two I can do as part of this build.

### On phones

Most of your customers are on a phone, often standing outside. So:

- A permanent bar sticks to the bottom of the screen once you scroll past the opening:
  **Call** and **Directions**, always one thumb away.
- The heavy scroll effects get simplified on small screens so nothing stutters.
- The whole thing has to be usable one-handed.

---

## 8. The moving parts, in plain English

Everything here is done with code, not video — so it's fast, and it works even on a bad
connection.

- Smooth, slightly weighted scrolling
- Headlines where the letters arrive one at a time
- Outlined headlines that fill in with gold as you reach them
- A hand-drawn line that draws itself under links
- Torn-paper edges between sections
- A very subtle grain over the whole page
- The gold ticker band that reacts to how fast you scroll
- The pinned tray with its labels drawing in
- The drag-along gallery, with the photos leaning slightly as you fling it
- A round stamp that spins as you scroll
- Palm leaves that drift with your mouse (desktop only)
- The sticky Call/Directions bar on phones

**Accessibility:** anyone whose phone or computer is set to "reduce motion" (common for
people who get motion sickness) gets the whole site with all the movement switched off,
and nothing missing. That's not a nice-to-have, it's the right way to build it.

---

## 9. Video — what we're doing

You've ruled out the scroll-controlled video, which I agree with — it's heavy, it's slow
on phones, and it's become a bit of a cliché.

What we *are* using: **3–5 short silent clips, 3–5 seconds each, on a loop, in the
gallery only.** Same as the reference site does. They're small, they only load when you
scroll to them, and only the one you're looking at plays.

**These must be real footage from your truck.** Not generated. I'll come back to why in
the next section.

---

## 10. Higgsfield — what I'd use it for, and what I wouldn't

You've got 270 credits on a starter plan. Here's my honest read on where that's worth
spending.

### What I'd use it for — decoration and clean-up only

1. **Palm leaf cut-outs** — 3 versions, isolated on black, for the corners and the drifting
   background layers
2. **Smoke and steam wisps** — 2 versions, to lay over the grill shots
3. **Scorched paper texture** — the background of the menu panel
4. **Crumpled foil texture** — for card backgrounds and the frame around the tray section
5. **Gold paint splatter** — matched to your existing banner artwork
6. **Ash and grain overlay** — the texture that goes over the whole page
7. **Sharpening your three existing photos** — they're phone shots and will look soft
   blown up to full screen
8. **Cutting the tray out of its background** so it can sit on anything

That's roughly 8–12 generations. **I'll work out the exact credit cost and check with you
before spending a single one**, and show you what it actually cost afterwards. (Worth
knowing: around 15% of these jobs just fail for no reason at the server end — they don't
charge you, they just need running again.)

### What I would not use it for — and why

**No AI-generated food. None.**

Your entire advantage over a chain is that you're real. A customer who sees a perfect
glossy jerk chicken on the site and gets handed a tray that looks different — even if the
tray is *better* — has been let down, and that's the review you get. Beyond that, food
photography that isn't your food is the kind of thing that quietly erodes trust in a
small local business, and it's a genuine advertising-standards grey area in the UK.

Same goes for the clips. **A real, slightly wobbly phone video of your actual chicken on
your actual grill will outperform anything generated.** Every time. People can tell.

So: generate the wallpaper, photograph the food.

---

## 11. What I need from you

### Facts to confirm

I've read most of this off the photos you sent, but I'm not publishing a price or a phone
number I've squinted at.

- [ ] **Your town / area** — and the full address and postcode of the Man in the Moon pub
- [ ] **The phone number** — I can make out `07841 4…` on the board but not the rest
- [ ] **The full menu and prices.** From the boards I can read: *Mains* — boneless curry
      goat, boneless jerk chicken, jerk chicken burger. *Sides* — fried dumplings, mac &
      cheese, coleslaw, plantain, chips. *Kids* — chicken nuggets and chips, boneless jerk
      chicken with rice or chips. Please confirm and send the actual prices.
- [ ] **The hours.** The board says every Saturday 4pm–8pm — still right?
- [ ] **Instagram and Facebook handles**
- [ ] **The hygiene rating** — I can see a green sticker in the truck photo. If it's a 5,
      that goes on the site prominently. It's one of the strongest trust signals you have.
- [ ] **Trading name**, and whether there's a limited company / VAT number for the footer
- [ ] **The domain name** you want, and whether you've bought it yet
- [ ] **Any line you actually say to customers** — a greeting, a catchphrase, something
      you put on the board. Real lines beat written-for-you lines every time.

### Photos and clips to take

Half an hour on a Saturday with a phone gets all of this. Landscape for most of it, and
please don't use portrait mode / fake blur on the food.

**Photos (10–15):**
- The tray from directly above, on a plain dark surface, in daylight — the hero shot
- Each side on its own: rice & peas, plantain, mac & cheese, slaw, festival, dumplings
- Jerk chicken close enough to see the char
- Sauce being poured or spooned
- The truck from the front, from the side, and at dusk with the lights on
- Hands passing a tray over the counter
- The queue, if there is one
- The owner at the hatch — a real face sells a small food business better than anything

**Clips (3–5, five seconds each, hold the phone still):**
- Chicken turning on the grill, steam coming off
- Festival or dumplings going into the oil
- A tray being built, side by side
- Sauce going on
- Handing a tray over

---

## 12. Technical notes (skip this if you like)

*For the build, not for you.*

- Single static page: `index.html`, `styles.css`, `main.js`. No framework, no build step —
  which means no dependency rot and anyone can maintain it in five years.
- GSAP + ScrollTrigger for the motion, Lenis for the smooth scroll, both stored locally
  rather than loaded from a CDN.
- Images served as AVIF with WebP fallback, sized explicitly so nothing jumps around while
  loading, lazy-loaded below the fold.
- Fonts self-hosted, subset to Latin, hero face preloaded.
- Performance budget: largest element painted under 2 seconds on 4G, layout shift under
  0.05, first-visit download under 900KB.
- **Build order matters:** the background/ambient scroll effects must be created *after*
  the pinned sections. Creation order is refresh order — get it backwards and everything
  after a pinned section silently sits in the wrong place.
- Verification: a `?jump=` parameter so any point on the page can be screenshotted and
  checked automatically, plus a smoothness test measuring the worst frame rather than the
  average (average frame rate hides stutter).
- `prefers-reduced-motion` fully honoured. Keyboard navigable. Real alt text on every image.
- **Structured data** — `FoodEstablishment` markup with opening hours, menu and location.
  This is what Google and AI assistants read when someone asks "Jamaican food near me" on
  a Saturday afternoon. For a business like this it's probably worth more than the entire
  visual design. Worth a dedicated pass before launch.

---

## 13. What I've assumed

Flagging these so nothing goes live on a guess:

1. **"Talawa" means "small but mighty"** — from *"wi likkle but wi tallawah"*. The whole
   recommended direction rests on this. Confirm it.
2. **Menu and prices** read off photographs of the boards. Unconfirmed.
3. **Every Saturday, 4–8pm, at the Man in the Moon** — read off the boards. Unconfirmed.
4. **Colour values** sampled by eye from the images you sent, not from the original logo
   files. I'd like the originals if you have them.
5. **You are the one taking the photos.** If you'd rather pay a food photographer for a
   half-day, Direction 3 becomes viable and the whole site gets better.

---

## 14. Next step

Tell me which direction you want — my recommendation is **Direction 1, "Likkle But
Talawa"**, with the countdown borrowed from Direction 2. Send over the facts in section 11
and whatever photos you have, and I'll build it.

If you'd rather see it before committing, I can put together a single static mock-up of
just the opening screen and the tray section, so you can look at the real thing rather
than a description.
