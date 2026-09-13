# HERO.MD — what 21st.dev has for the opening screen

A checklist, following the same rule as `COMPONENTS.MD`: nothing here is built yet, and
nothing gets built until you tick it.

---

## 1. How I looked

Pulled the hero catalogue off 21st.dev — about **130 hero components**, plus the animated-hero
and shader sub-collections — and read them against the opening screen you already have.

**The short version: 21st.dev has very little to offer this particular hero, and I'd rather
say so than pad a list.** Your opening screen is already bespoke and already strong: a
gradient wordmark built from your logo's measured colours, hand-drawn palm fronds, a live
open/closed line, and a letter-by-letter entrance. Most of what's on 21st.dev is either a
generic centred headline (worse than what you have) or a heavy 3D/shader toy (wrong for a
food truck).

**Two things are genuinely worth taking. One of them isn't a component at all** — it came out
of measuring your own hero while I was there, and it's the biggest single improvement
available on the page.

Same practical limits as last time: everything on 21st.dev is written for React and Tailwind,
which your site deliberately doesn't use, so nothing can be pasted in. It's a reference
library, not a parts bin. Every component has a named author and licences vary, so anything
we actually borrow gets checked before it goes live.

---

## 2. Worth doing

### 2.1 Turn the food photo up — **the big one, and it's free**

There is a photograph of your tray behind the hero right now. **You almost certainly can't
see it.** It's set to 12% strength with a near-black wash on top.

I measured what it actually contributes:

| | Brightness | Visible detail |
|---|---|---|
| As it is now (12%) | 25.6 | 28.5 |
| **Photo removed completely** | 19.9 | **29.3** |
| Photo at 34% | 36.3 | 28.3 |

Read the middle row twice. **Deleting the photo entirely makes the screen barely darker, and
very slightly *more* detailed** — because the texture you think is food is actually the palm
fronds and the colour glow. The photo is doing almost nothing.

Turned up to around a third, the tray, plantain, festival and jerk chicken all read clearly,
and the opening screen stops being an abstract dark panel and starts being a picture of your
food. For a business that sells food, that is the whole ball game.

- [ ] **Raise the photo so the food is actually visible.** One number.
- [ ] **Re-balance the dark wash** so the left side, where the words sit, stays dark enough to
      read against while the right side opens up and shows the tray.
- [ ] **Re-check the hollow "CARIBBEAN" line.** It's an outline, so a busy photo behind it is
      exactly what makes outlines hard to read. This needs measuring against the brighter
      background, not eyeballing — it may need a slightly heavier outline or a touch more
      wash directly behind it.
- [x] **Level decided: 26%.** More than double what is there now, and measured rather than
      guessed. Working upward until something broke:

      | Photo | Tagline | Status line | "Jamaican food…" | |
      |---|---|---|---|---|
      | 12% (now) | 5.4:1 | 4.9:1 | 14.3:1 | fine |
      | **26%** | 5.1:1 | **4.6:1** | 13.5:1 | **fine — the ceiling** |
      | 34% | 4.9:1 | 4.4:1 | 12.9:1 | just under |
      | 45% | 4.5:1 | 4.1:1 | 12.0:1 | clearly under |

      Readable text needs 4.5:1. **The limit is not the outline — it is the small grey
      "opens Saturday" line**, which sits bottom-left where the dark wash is thinnest. 26% is
      the last step where everything still clears.

      **A concern I raised and then disproved:** I expected the gold CARIBBEAN outline to fail
      against the mac and cheese and plantain behind it. It does not — worst case is 6.3:1
      even at 45%, against a 3:1 requirement, because the dark wash is strongest exactly where
      that line sits. Worth recording so nobody re-raises it.

      Going brighter than 26% is possible, but only by also changing something else — either
      darkening the wash just behind that bottom-left text, or lifting the grey to a lighter
      tone. Not worth it now; 26% already does the job.

### 2.2 A fine grain over the hero

From **Grain Gradient Hero Section** by Caio Bonato. Theirs runs on a WebGL shader library,
which is far too heavy for us — but the *idea* costs nothing: a very fine film-grain texture
laid over the opening screen.

Two reasons it's worth it:

1. **It suits the brand.** Street food, hand-painted sign, market stall. A slightly grainy,
   printed feel fits that; a glassy digital gradient doesn't.
2. **It fixes a real flaw.** Big soft colour glows like the ones in your hero often show up as
   visible *stripes* on cheaper screens and phones. A fine grain breaks those stripes up. This
   is the standard fix, not a decoration.

- [ ] **Add a fine grain over the hero only**, not the whole page.
- [ ] Build it with a few lines of built-in browser drawing, **not** the shader library they
      use — no extra download, no battery cost.
- [ ] Keep it subtle enough that you notice the page feels warmer, not that there's a texture
      on it.

---

## 3. Worth considering — I'd want your call

### 3.1 Letters that react to the mouse

From **Variable Font Proximity Hero** by Cnippet: the letters of the headline get bolder as
the mouse moves near them, and thin out again as it moves away.

It would fit unusually well, because **the hard part is already done** — your wordmark is
already built as one separate letter at a time (that's what makes the gold-to-green gradient
and the entrance animation work). The effect would ride on machinery that already exists.

Two honest problems:

- **It does nothing on a phone.** There's no mouse. Most people finding a food truck are on a
  phone, so this is effort spent on the smaller half of your audience.
- **It needs a heavier font download.** Right now the site asks for two fixed weights of your
  headline font. This effect needs the full range, which is a bigger file on every visit —
  including for the phone users who get no benefit from it.

- [ ] Decide: a genuinely nice desktop touch, or effort in the wrong place?
      **My lean: skip it for now.** Revisit if the site ever gets a lot of desktop traffic.

### 3.2 A very slow drift on the photo

If the photo comes up in strength (2.1), giving it an extremely slow drift — a barely
perceptible push over 30 seconds or so — makes the opening screen feel alive without anything
loading or playing.

To be clear about your standing instruction: **this is not video and not tied to scrolling.**
It's a still photograph moving very slightly on its own. If it reads as gimmicky at all, it
goes.

- [ ] Decide whether this is welcome or whether the hero should sit still.
- [ ] If yes: it must switch itself off for visitors who've asked their device to reduce
      motion. Non-negotiable, and cheap.

---

## 4. What I would not take, and why this is the important part

The hero category on 21st.dev is full of things that would actively make your site worse.

- [ ] **Every scroll-locked and scroll-scrubbed video hero.** There are a lot of them —
      Scroll-Locked Video Hero, Animated Video on Scroll, Cinematic Product Scroll, Scroll
      Media Expansion, Smooth Scroll Hero, Story Scroll, Glass Video Hero. **You ruled these
      out in your very first message and I've held that line the whole way through.** Nothing
      here changes my mind: they're heavy, they fight the scroll wheel, and we already fixed
      one scrolling bug on this site caused by exactly that class of library.
- [ ] **Anything 3D, shader, particle or galaxy.** Spline Scene, Galaxy Interactive Hero, GLSL
      Hills, Particle Hero, Shader Hero and a hundred more. Megabytes of library, noticeable
      battery drain on a phone, and they say "tech startup", not "Jamaican food truck in a pub
      car park".
- [ ] **Typing and typewriter effects.** These are the single clearest tell of a machine-built
      landing page — and you've just had me strip that exact quality out of the site. Adding
      one back would undo that work.
- [ ] **Aurora / mesh / animated gradient backgrounds.** Same tell, and redundant: your hero
      glow is already built from your logo's real colours, measured off the actual file.
- [ ] **Anything that replaces the wordmark lockup.** TALAWA over CARIBBEAN is two days old,
      it's built from your logo, and it's the best thing on the page. The generic centred
      headlines on 21st.dev are a clear downgrade.

---

## 5. Still true from before

- Nothing invented goes on the page: no made-up reviews, prices, or details.
- Everything I claim gets measured, and the measurement goes in the file so you can check it.
- The site stays one plain fast page with no framework and no build step.

---

## 6. What I need from you

- [x] **2.1 — the photo. Recommended: raise it to 26% and change nothing else.** Measured
      ceiling; see the table above. Shaun has confirmed the photo stays in the hero.
- [ ] **2.2 — the grain. Recommended: yes.** Small, suits the brand, and fixes real banding.
- [x] **3.1 — mouse-reactive letters. Recommended: no.** Nothing on a phone, heavier font
      download for everyone.
- [x] **3.2 — the slow drift. Recommended: no.** With the photo properly visible it is not
      needed, and the hero already has its letter-by-letter entrance. Holding still is the
      stronger choice.
- [ ] **Still outstanding from before, unrelated to the hero:** prices and dish descriptions,
      your Google/Facebook reviews, the Facebook handle, and roughly what time you sell out.

---

## 7. If you only do one thing

Turn the photo up. It costs one number, it needs no new code, and it's the difference between
an opening screen that looks like a design and one that looks like your food.
