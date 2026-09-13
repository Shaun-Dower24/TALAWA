# STRIP.MD — the band beneath the hero

Same rule as `HERO.MD` and `COMPONENTS.MD`: nothing here is built, and nothing gets built
until you tick it.

"The strip" is three things stacked: the **gold scrolling ticker**, the thin **green stripe**
under it, and the **When / Hours / Where row** below that.

---

## 1. The finding that isn't a component

I went through all 113 marquee components on 21st.dev. Before any of that matters, there's
something wrong with this strip that no component fixes.

**The same three facts are stated three times in a row, within about 300 pixels of scrolling:**

| Where | What it says |
|---|---|
| Bottom of the hero | Jamaican food · Stevenage · **Every Saturday, 4–8pm** |
| The gold ticker | **Every Saturday** · **4pm til sold out** · **Man in the Moon** |
| The row below it | WHEN **Saturday** — HOURS **4–8pm** — WHERE **Man in the Moon** |

A customer reads "Saturday" three times and "Man in the Moon" twice before they've scrolled
past the first screen. The row at the bottom is doing no work: by the time anyone reaches it,
they already know.

That's not a small thing. That row takes up a **209px band on a desktop and 296px on a phone**
— a third of a phone screen — to repeat what was just said twice.

- [ ] **Give the When/Hours/Where row a different job.** It's prime space directly under the
      hero and it should tell people something they don't already know. Everything you've
      confirmed that *isn't* already said up there:
      - **Free parking** in the pub car park
      - **Card and cash** both fine
      - **5** food hygiene rating
      These are the three things someone actually wonders before setting off, and none of
      them appears anywhere near the top of the page at the moment.
- [ ] **Or cut the row entirely** and let the ticker carry it. Faster, and the tray section
      starts sooner. Less to look at, which isn't automatically worse.

My recommendation is the first. The second is the safer one if in doubt.

---

## 2. Worth doing — the one real component idea

### 2.1 Soften the ends of the ticker

Right now the ticker **hard-cuts at both edges**. In the screenshot the word "EVERY SATURDAY"
is sliced clean through mid-letter at the left, and "4PM TIL SOL—" at the right. It reads as
a mistake rather than as movement.

From **Progressive blur** by Julien Thibeaut (also in *Blurred Marquee* by grootstudio): fade
the strip out at each end so words dissolve instead of being guillotined.

- [ ] **Fade both ends of the gold band.** Words should melt out rather than be cut off.
- [ ] Build it as a simple gradient over each end, **not** their blur filter — a real blur
      across a moving strip is expensive on phones, and at this size a plain fade looks the
      same.
- [ ] The fade has to be gold, matching the band, not a dark fade — the band is the light
      thing on a dark page.

This is small, cheap, and fixes something that currently looks unfinished.

---

## 3. Worth considering — your call

### 3.1 Alternate solid and hollow words in the ticker

From **Infinite Marquee** by framecn — a looping strip where some words are solid and some
are outlined.

It would tie the strip to the rest of the site, because **hollow lettering is already your
motif**: CARIBBEAN in the hero, and the second word of every section heading
(FIND *THE TRUCK*, WHAT'S *COOKING*). The ticker is currently the only place that ignores it.

Honest risk: the band is only 84px tall on a desktop and **49px on a phone**, and outlined
letters at that size on a moving strip could read as thin and weak rather than deliberate.
I'd want to show it to you rather than just do it.

- [ ] Show two versions side by side and decide.

### 3.2 Tilt the band slightly

From **Infinite Ribbon** by Edwin Vakayil. Your logo has "CARIBBEAN FOOD" sitting on a
**slanted green band** — so a small tilt would be lifted straight from your own branding
rather than invented.

Honest risk: a tilted full-width band leaves triangular gaps at the top and bottom corners
that have to be filled, and it fights the strict horizontal rhythm of everything below it.
Could look brilliant, could look like a mistake.

- [ ] Worth a mock-up before committing either way. Lower priority than the rest.

---

## 4. Already built — checked, nothing to take

Two things I'd have recommended are in there already, from the earlier pass:

- **Speeds up as you scroll.** *Scroll Based Velocity* (Dillion Verma), *Scroll Velocity Text*
  (Cnippet) — the band already reads your scroll speed and moves faster the harder you flick.
- **Pauses when you point at it.** *Infinite Slider with custom hover speed* (Julien Thibeaut)
  — already there.

---

## 5. What I would not take

- [ ] **3D Marquee, Gooey Marquee, Marquee Along SVG Path, Great UI Diagonal Marquee.**
      Gimmicks. They'd draw attention to the strip rather than to what it says.
- [ ] **Every logo-cloud variant** — Logo Marquee, Logo Cloud, Brand Scroller, Logo Carousel,
      Stepped Logo Marquee and about twenty more. These are for showing off which companies
      use your software. You sell food from a trailer.
- [ ] **All the testimonial marquees.** Your reviews section is built and waiting for real
      reviews; a scrolling wall of them at the top of the page would be the wrong shape and
      would make the emptiness louder.
- [ ] **Anything that turns the strip into a call-to-action block** (the various CTA-with-
      Marquee variants). The strip's job is a glance, not a decision.

---

## 6. What I need from you

- [ ] **The big one: what should the When/Hours/Where row say?** My recommendation is
      parking, payment and the hygiene 5. Or say the word and I'll remove it.
- [ ] Fade the ends of the ticker? (Recommendation: yes.)
- [ ] Want to see the hollow-word ticker mocked up? (Recommendation: worth a look.)
- [ ] Want to see the tilted band mocked up? (Recommendation: later, if at all.)

---

## 7. If you only do one thing

Stop the row under the ticker repeating what the two things above it just said. Everything
else on this page is fighting to earn its space; that row currently isn't.
