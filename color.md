# Colour Checklist — Making It Pop, Using the Logo

**Request:** the customer wants the website colours to pop more, using the colours from
the logo.
**Status:** **done and live**, apart from two items that turned out to be technically
impossible and one option deliberately held back. See the notes against each.
**Date:** 12 September 2026

---

## 1. First, the honest bit

I measured the actual colours out of the logo file rather than guessing at them — sampled
every bright pixel and grouped them by colour family. Two things came out of that:

**Good news: there's a real, specific problem to fix.** The green on the website is the
*wrong green*. Not slightly off — a different colour family. That is almost certainly why
the site doesn't quite feel like it belongs to the logo.

**One thing worth saying before we start:** **72% of the logo is black.** It pops *because*
it's mostly black, with the colour concentrated in one place and left to do its work. So
"make it pop" shouldn't mean putting colour everywhere — that's the change that usually
makes a page look cheaper, not brighter. The plan below adds colour in specific places and
leaves the black ground alone. If she still wants more afterwards, there's a bigger option
at the bottom of this list.

---

## 2. The real colours, measured from the logo

| Colour | Hex | Where it is in the logo | Safe to use for |
|---|---|---|---|
| **Gold** | `#FDCB04` | The paint splatter, the top of the wordmark | Anything, including small text |
| **Hot yellow-green** | `#F7E003` | The bright middle of the wordmark gradient | Anything — it's the brightest colour in the logo |
| **Lime green** | `#7A9E03` | Lower wordmark, the bright side of the badge | Text and up — fine, but not for tiny print |
| **Leaf green** | `#1A6003` | Deep side of the badge, the band, the palm fronds | **Decoration only — never text** |
| **Black** | `#000000` | 72% of the whole logo | The ground, as now |

### How these compare to what's on the site now

| | On the site now | In the logo | Verdict |
|---|---|---|---|
| Gold | `#FFC91C` | `#FDCB04` | Very close. Logo version is a touch more saturated — worth switching for exactness |
| Green | `#35B14A` | `#7A9E03` / `#1A6003` | **Wrong.** See below |

**The green is the headline problem.** The site's green sits at 130° on the colour wheel —
a minty, blue-leaning emerald. The logo's greens sit at 74° and 105° — yellow-leaning lime
and olive. They are not the same colour, and side by side they clash rather than match.
Fixing this one value will do more than everything else on this list combined.

---

## 3. The checklist

### Do these first — biggest visual change for least risk

- [x] **Swap the green.** Replace `#35B14A` with the logo's lime `#7A9E03`, and add leaf
      green `#1A6003` alongside it for the darker half. Affects the script lines, the
      "open now" dot, the hygiene badge and the palm fronds.
- [x] **Add the green-to-gold gradient.** This is the logo's signature move and the site
      does not use it *anywhere* — every heading is flat gold. Putting that gradient on the
      big display headings will be the single most noticeable change, and it is the brand's
      own device rather than something invented.
- [x] **Correct the gold** from `#FFC91C` to the measured `#FDCB04`. Small change, but it
      is the difference between "roughly the brand colour" and "the brand colour".
- [x] **Repaint the palm fronds** with leaf and lime green instead of the current greens,
      which came from the old wrong-green family.

- [x] **Section eyebrows** (BY THE NUMBERS, REVIEWS, SATURDAYS…) were grey. Now lime —
      puts the logo's green on every section for nothing. Added during the build.

### Then these — putting the colour where it earns its keep

- [x] ~~**The hollow outlined words** — gradient outline.~~ **Not possible, and not wanted
      after all.** CSS cannot put a gradient on a text outline; I tested four techniques and
      the nearest one just fills the letters solid, losing the hollow effect entirely. More
      to the point, seeing it rendered settled the design question: the hollow gold word
      *above* or *below* a solid one is what makes those headings work. Filling them would
      have flattened the page into one long gradient. **Left hollow deliberately.**
- [x] **The four big numbers** in the stats row: gradient instead of flat gold.
- [x] **Borrow the green band device.** In the logo, "CARIBBEAN FOOD" sits on a slanted
      green band. That shape isn't on the site at all. Worth using once — probably under the
      Saturday ticker — so the page carries a piece of the logo's furniture.
- [x] ~~**The "LIKKLE" outline**: gradient stroke.~~ Same technical limit. It turned out
      better this way regardless — hollow gold LIKKLE sitting above the gradient-filled
      BUT TALAWA is the single strongest moment on the page, precisely because one is
      hollow and one is filled.
- [x] **The hot yellow-green** `#F7E003` is brighter than the gold. Save it for one or two
      peak moments — the brightest point of a gradient, or the "OPEN NOW" state — rather
      than spreading it around.

### Leave these exactly as they are

- [x] **The buttons stay solid gold with black text.** 13:1 contrast — as legible as it gets.
      Gradient buttons look cheap and hurt readability.
- [x] **The tray labels and leader lines stay flat gold.** They sit on top of a photograph
      and need maximum contrast to stay readable. A gradient there would lose the plot.
- [x] **Body text stays bone** `#F2ECDF`. Coloured paragraph text is the single fastest way
      to make a site look amateur.
- [x] **The black ground stays black.** This is where the pop comes from.

---

## 4. Two hard rules to respect

These aren't style preferences, they're legibility limits. I measured them.

1. **Leaf green `#1A6003` must never carry text.** It only reaches 2.6:1 against black —
   well under the 4.5:1 minimum. It's for fills, bands, fronds and gradient ends only.
2. **Lime green `#7A9E03` reaches 6.4:1** — fine for normal text and headings, but not for
   the small print. Gold and the hot yellow-green are safe everywhere.

If a colour choice would break either rule, I'll say so rather than quietly doing it.

---

## 5. One thing that isn't a logo colour

The orange-red used for warnings — `#E8481B`, on the "to confirm" and "answer needed"
markers — is **not from the logo.** I introduced it so unverified information stands out.

- [x] **Decided:** left as it is.
      My recommendation: leave it. You need a colour that clearly isn't green or gold to
      mean "not confirmed yet", and most of these markers disappear anyway once the prices
      and reviews go in. It is a working tool, not part of the brand.

---

## 6. The structural change — also done

- [x] **Make one section light. Done — first the menu, now the reviews.**

      > **Partly superseded.** The menu section is still light, but the board panel inside
      > it has since gone back to black (see the blackboard entry below), so the inverted
      > accents below no longer apply *inside* the menu — only to its eyebrow, heading and
      > margins. The scheme is otherwise unchanged and still live: it is what the
      > **reviews** section runs on in full.

      A menu belongs on paper, so the menu got paper, and it sat mid-page so it broke the
      black in the middle rather than at an end.

      It needed a genuine design pass, not a background swap. **Gold measures 1.3:1 on a
      paper ground — completely unreadable** — so the whole accent system had to invert:

      | Role | Dark sections | The light section | Contrast |
      |---|---|---|---|
      | Ground | ink `#0A0908` | paper `#E9DDC4` | — |
      | Panel | `#151311` | `#DDCFAB` | 12.9:1 with ink |
      | Text | bone | ink `#0A0908` | 14.8:1 |
      | Accent (prices, rules) | gold | **leaf green** `#1A6003` | 5.0:1 |
      | Muted (sub-lines) | ash | `#544B3E` | 5.5:1 |
      | Warning (allergies) | scotch `#E8481B` | `#96290A` | 5.2:1 |

      *(Ratios shown against the panel, which is the tighter of the two grounds.)*

      **Softened after a first look.** The first version used plain bone `#F2ECDF`, which
      was too stark a jolt out of the black. The ground is now warmer and deeper — but
      that could not be done alone: deepening it pushed the muted tone to 3.9:1 and the
      warning to 4.4:1 on the panel, both below AA. All three moved together.

      Every one of those was measured against both the paper and the deeper panel sitting on
      it, and a test now walks every piece of text in the section and fails the build if
      anything drops below AA.

      The leaf-green band device brackets the section top and bottom, so the switch from
      black to paper reads as a deliberate edge rather than an accident.

- [x] **A second light section — the reviews. Done, at Shaun's request.**

      **I had advised against it and I was wrong.** My argument was that the review cards are
      all placeholders, so putting them on paper would only make the emptiness louder. Seen
      on screen, it doesn't: a wall of testimonials is a thing people expect to read off
      paper, and the section now reads as a page waiting to be filled rather than a hole.

      It reuses the menu's light scheme exactly — same paper, same panel, same ink, accent
      and muted tones — so it is a second instance of one system rather than a second design.
      Two things needed deciding fresh:

      | Element | Problem on paper | Fix | Contrast |
      |---|---|---|---|
      | The star icons | gold measures **1.1:1** — invisible | burnt amber `#8A5A00` | 3.8:1 (graphics need 3:1) |
      | The `PLACEHOLDER` chips | bright scotch shouted | the muted warning `#96290A` | 5.2:1 |

      Two bugs that only a look caught, not a passing test:

      - The edge fades on the card rail faded to **black**, because they were written when
        the section was black. They now fade to paper.
      - The "average rating" placeholder is an em dash set at 4.4rem in a 900-weight display
        face — which paints as a **solid bar**. In accent green on paper it stopped reading
        as a blank and started reading as a filled-in value, like a bar chart. It is now the
        muted tone, and marked `tbc-num` in the markup so it goes green by itself the day a
        real average replaces it.

      The same contrast walker now covers both light sections, not just the menu.

- [x] **The menu becomes a blackboard on paper.** Shaun's call, and the best version of the
      three. The **section** keeps the paper ground; the **board panel inside it** goes back
      to black. So the eyebrow, the "WHAT'S COOKING" heading and the margins are cream, and
      the menu itself is a black board sitting on them.

      It settles an argument the all-paper version was quietly losing. Putting a menu on
      paper is the obvious move, but a food truck's menu is not a printed card — it is a
      board propped in a hatch. The eyebrow above it has said **"THE BOARD"** since the
      first build, and only now does the design say the same thing.

      It is also the cheapest of the three versions to maintain: the board keeps every
      dark-palette value it always had — gold headings, bone dishes, gold prices, scotch
      allergy box — so nothing inside it needs a light counterpart, and the ten
      menu-specific light overrides stay deleted.

      One thing carries over from the all-paper spell. The rules under
      **MAINS / SIDES / KIDS** were gold originally and green on paper; they stay green on
      the black board, under headings that are gold again. Gold over green is the wordmark's
      own gradient in miniature.

      **It could not be the same green.** The paper version used leaf `#1A6003`, which
      measures **2.6:1 on black** — and a 2px rule is a graphic, needing 3:1. So the rule
      uses the lime `#7A9E03` at **6.4:1**, the same green as every section eyebrow. A test
      asserts both the value and the ratio that forced it.

      **An accidental gain:** because the board now sits inside a section marked light, the
      contrast walker sweeps it too. It resolves 31 pieces of text onto the black board and
      23 onto the paper, and every one clears AA — worst on the board is the scotch
      "Allergies" label at 4.7:1, worst on paper is a review source line at 5.0:1. The dark
      palette had never actually been measured this way before.

      Five bands again: one under the ticker, two bracketing each light section.

---

## 7. How the colours were measured

So the numbers are checkable rather than taken on trust: every pixel in the supplied logo
was converted to hue/saturation/brightness, filtered to the ones bright and saturated enough
to count as real colour, then grouped into families by hue. Each hex above is a
high-saturation representative of its family — not an average, which would have muddied
them, and not my eye, which would have been close but wrong. Contrast figures are standard
WCAG ratios against the site's black.
