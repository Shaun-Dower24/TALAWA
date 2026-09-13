# STRIP.MD — components for the band beneath the hero

**A1, A2 and B1 are built** — the first three recommendations approved in the
previous conversation. The other unchecked ideas remain optional.

"The strip" is three things stacked: the **gold scrolling ticker**, the thin **green stripe**,
and the **three-fact row** under it.

Searched: Marquees (113), Stats & KPIs (153), Announcements (71). Copy is out of scope here —
noted separately at the bottom.

---

## A. The gold ticker

### A1. Fade the ends — **my strongest recommendation**
*Progressive blur* by Julien Thibeaut · also *Blurred Marquee* by grootstudio

The band currently **hard-cuts at both edges**, slicing words mid-letter. In the screenshot
"EVERY SATURDAY" is chopped through on the left and "4PM TIL SOL—" on the right. It reads as
a fault, not as movement. Fading each end makes words dissolve instead.

- [x] Built as stationary gold gradients at each end, **not** a blur filter. The fade
      scales from 28px on phones to a maximum of 96px on wide screens.

### A2. A slow shine travelling across the gold
*Animated Shiny Text* by Dillion Verma

The band is the **largest area of flat colour on the whole page**. A slow highlight moving
across it would make it read like painted metal or an enamel sign rather than a flat swatch —
which is the right reference for a food trailer.

- [x] Built as a soft, 28-second highlight underneath the black lettering. It pauses
      with the ticker on hover and is hidden for reduced-motion visitors.

### A3. Alternate solid and hollow words
*Infinite Marquee* by framecn

**Hollow lettering is already your motif** — CARIBBEAN in the hero, and the second word of
every section heading (FIND *THE TRUCK*, WHAT'S *COOKING*). The ticker is the only place that
ignores it.

- [ ] Risk: the band is 84px tall on desktop but only **49px on a phone**, where outlined caps
      may read as weak rather than deliberate. Worth mocking up both ways before deciding.

### A4. Tilt the band
*Infinite Ribbon* by Edwin Vakayil

Your logo puts "CARIBBEAN FOOD" on a **slanted green band**, so a tilt would be lifted from
your own branding rather than invented.

- [ ] Risk: a tilted full-width band leaves triangular gaps at the corners to fill, and it
      fights the strict horizontal rhythm of everything below. Could be great, could look like
      a mistake. Lowest priority of the four.

### Already built — checked, nothing to take
- **Speeds up as you scroll** — *Scroll Based Velocity* (Dillion Verma), *Scroll Velocity Text*
  (Cnippet). Already in.
- **Pauses when you point at it** — *Infinite Slider with custom hover speed* (Julien
  Thibeaut). Already in.

---

## B. The three-fact row

Before this pass: three equal columns, plain label above plain value, thin dividers between.
On a desktop each fact used only about **40% of its column**, so the row read mostly as empty
space — 209px of it, and 296px on a phone.

### B1. Give it a proper typographic treatment
*Bold Stats* by ui layout · *Stats (info-and-numbers / info / metric)* by Méschac Irung

Several clean three-up rows that set the value large and confident instead of the current
modest size. **No cards, no boxes** — which matters, because boxed cards would fight the rest
of the page and you have just had me strip badge-boxes out.

- [x] Built with larger Archivo values and tighter letter spacing. The three equal
      desktop columns and thin dividers remain; on phones the labels sit beside the
      values. At 1440px the values are 56px; at 390px they are 29px and the whole row
      is 238px tall. No cards or boxes; the wording stays unchanged.

### B2. Break the equal-column grid
*Stats Bento* / *Feature Bento* / *About Bento* by ui layout

Instead of three identical columns with dead space, an uneven arrangement where one fact is
given more room than the others. Directly fixes the emptiness rather than decorating it.

- [ ] Bigger structural change than B1. Worth seeing side by side.

### B3. Each fact rolls into place
*Text Roll — stats row* by Cnippet

The values flip/roll in as the row comes into view. Movement without gimmick, and it matches
the letter-by-letter entrance the hero already uses.

- [ ] Must switch itself off for reduced-motion visitors.

### B4. Counting numbers — **only if the row carries numbers**
*Count Up* (unlumen) · *Number Ticker* (Daniel Petho) · *Shuffle Number* (reuno-ui) ·
*Animated Blur Number* (Serafim)

**Already built** on the stats section further down the page, so reusing it here costs nothing.
But it only makes sense if this row ends up showing a number worth counting to.

- [ ] Parked until the copy is settled.

### B5. A light travelling down the dividers
*Grid Beam* by cult/ui

The row already has vertical dividing lines. A slow beam running down them is a quiet way to
give the row life without adding anything to read.

- [ ] Subtle, cheap, easy to overdo. Lower priority.

---

## C. What I would not take

- [ ] **3D Marquee, Gooey Marquee, Marquee Along SVG Path, Great UI Diagonal Marquee Carousel.**
      Gimmicks that draw attention to the strip instead of to what it says.
- [ ] **Every logo-cloud variant** — Logo Marquee, Logo Cloud 3/4/15, Brand Scroller, Logo
      Carousel, Stepped Logo Marquee, MultiLogoScroller and about twenty more. These exist to
      show which companies use your software.
- [ ] **All testimonial marquees.** Your reviews section is built and waiting for real reviews.
- [ ] **The whole Announcements category.** 71 components and they are almost all dismissible
      SaaS banners, cookie bars and "upgrade now" prompts. Your band is permanent trading
      information, not a notification. *Animated Shiny Text* (A2) was the only thing worth
      taking out of it.
- [ ] **Text Scramble / scrambled stats.** Scrambling letters is one of the clearest
      machine-built tells, and you have just had me strip that quality out of the site.
- [ ] **Every stat component built as a card** — Stat Card, Glowing Card, Shine Border Stats
      Card, Progress Card and the rest. Boxes around three short facts is exactly the badge
      styling you asked me to remove.

---

## D. My order, if you want one

1. **A1 — fade the ticker ends. Built.**
2. **A2 — slow shine on the gold. Built.**
3. **B1 — bolder typographic row. Built.**
4. **A3 — hollow words in the ticker.** Worth mocking up; genuinely might not work at phone size.
5. **B2 / B3 / B5 / A4.** Only if you want to keep going.

---

## E. Noted, for when you come back to copy

Not a component issue, so parked — but the row currently repeats what the hero strap and the
ticker have both already said ("Saturday", "4–8pm", "Man in the Moon"). Whichever component
that row ends up using, it will land better once it's saying something new.

---

## F. Verification — 13 September 2026

- Chrome checked at 320, 390, 640, 860, 861, 1024, 1440, 1878 and 2560px.
- Confirmed the local Archivo 900 font was actually loaded before measuring text.
  Every value fits inside its available width, including both sides of the 860px
  layout breakpoint. Checked text ranges against their cells rather than relying
  on page scroll width, which can hide clipped content.
- Hover pauses both the ticker and shine; leaving resumes both. Reduced motion
  stops the ticker, hides the shine and leaves every fact visible.
- Visually checked the desktop and phone layouts. Desktop checked from a fresh
  load with normal scrolling so the existing tray pin had time to initialise.
- The local 21st UI review reported no findings. No new runtime dependencies.

The earlier hero/font fix was already committed and is unchanged by this pass.
