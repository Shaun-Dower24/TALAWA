# Colour Checklist — Making It Pop, Using the Logo

**Request:** the customer wants the website colours to pop more, using the colours from
the logo.
**Status:** nothing changed yet. This is the plan. Tick items off and I'll make them.
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

- [ ] **Swap the green.** Replace `#35B14A` with the logo's lime `#7A9E03`, and add leaf
      green `#1A6003` alongside it for the darker half. Affects the script lines, the
      "open now" dot, the hygiene badge and the palm fronds.
- [ ] **Add the green-to-gold gradient.** This is the logo's signature move and the site
      does not use it *anywhere* — every heading is flat gold. Putting that gradient on the
      big display headings will be the single most noticeable change, and it is the brand's
      own device rather than something invented.
- [ ] **Correct the gold** from `#FFC91C` to the measured `#FDCB04`. Small change, but it
      is the difference between "roughly the brand colour" and "the brand colour".
- [ ] **Repaint the palm fronds** with leaf and lime green instead of the current greens,
      which came from the old wrong-green family.

### Then these — putting the colour where it earns its keep

- [ ] **The hollow outlined words** (COOKING, MOUTH, THE TRUCK, QUESTIONS, MIGHTY, A
      SATURDAY) currently have a flat gold outline. Give them a gradient outline instead —
      green at the bottom, gold at the top, exactly like the wordmark.
- [ ] **The four big numbers** in the stats row: gradient instead of flat gold.
- [ ] **Borrow the green band device.** In the logo, "CARIBBEAN FOOD" sits on a slanted
      green band. That shape isn't on the site at all. Worth using once — probably under the
      Saturday ticker — so the page carries a piece of the logo's furniture.
- [ ] **The "LIKKLE" outline** in the opening screen: gradient stroke rather than flat gold.
- [ ] **The hot yellow-green** `#F7E003` is brighter than the gold. Save it for one or two
      peak moments — the brightest point of a gradient, or the "OPEN NOW" state — rather
      than spreading it around.

### Leave these exactly as they are

- [ ] **The buttons stay solid gold with black text.** 13:1 contrast — as legible as it gets.
      Gradient buttons look cheap and hurt readability.
- [ ] **The tray labels and leader lines stay flat gold.** They sit on top of a photograph
      and need maximum contrast to stay readable. A gradient there would lose the plot.
- [ ] **Body text stays bone** `#F2ECDF`. Coloured paragraph text is the single fastest way
      to make a site look amateur.
- [ ] **The black ground stays black.** This is where the pop comes from.

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

- [ ] **Decision needed:** leave it, or change it?
      My recommendation: leave it. You need a colour that clearly isn't green or gold to
      mean "not confirmed yet", and most of these markers disappear anyway once the prices
      and reviews go in. It is a working tool, not part of the brand.

---

## 6. If she wants more after all this

If the page still feels too dark once the above is done, the next lever is structural
rather than a colour swap:

- [ ] **Make one section light.** Put the menu, say, on a warm off-white ground with black
      type — one bright block in the middle of all that black. It breaks up the darkness
      properly and makes the black sections either side hit harder.

I'd hold this back until the colour fixes are in, because they may well be enough on their
own. And it is a bigger change: it needs its own design pass rather than a find-and-replace.

---

## 7. How the colours were measured

So the numbers are checkable rather than taken on trust: every pixel in the supplied logo
was converted to hue/saturation/brightness, filtered to the ones bright and saturated enough
to count as real colour, then grouped into families by hue. Each hex above is a
high-saturation representative of its family — not an average, which would have muddied
them, and not my eye, which would have been close but wrong. Contrast figures are standard
WCAG ratios against the site's black.
