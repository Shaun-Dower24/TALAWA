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

- [x] **Make one section light. Done — the menu.** A menu belongs on paper, so it reads as
      meaningful rather than arbitrary, and it sits mid-page so it breaks the black in the
      middle rather than at an end.

      It needed a genuine design pass, not a background swap. **Gold measures 1.3:1 on a
      paper ground — completely unreadable** — so the whole accent system had to invert:

      | Role | Dark sections | The light menu | Contrast |
      |---|---|---|---|
      | Ground | ink `#0A0908` | paper `#F2ECDF` | — |
      | Panel | `#151311` | `#E8DFC9` | 15.0:1 with ink |
      | Text | bone | ink `#0A0908` | 16.9:1 |
      | Accent (prices, rules) | gold | **leaf green** `#1A6003` | 6.6:1 |
      | Muted (sub-lines) | ash | `#6B6253` | 5.1:1 |
      | Warning (allergies) | scotch `#E8481B` | `#A8300D` | 5.8:1 |

      Every one of those was measured against both the paper and the deeper panel sitting on
      it, and a test now walks every piece of text in the section and fails the build if
      anything drops below AA.

      The leaf-green band device brackets the section top and bottom, so the switch from
      black to paper reads as a deliberate edge rather than an accident.

---

## 7. How the colours were measured

So the numbers are checkable rather than taken on trust: every pixel in the supplied logo
was converted to hue/saturation/brightness, filtered to the ones bright and saturated enough
to count as real colour, then grouped into families by hue. Each hex above is a
high-saturation representative of its family — not an average, which would have muddied
them, and not my eye, which would have been close but wrong. Contrast figures are standard
WCAG ratios against the site's black.
