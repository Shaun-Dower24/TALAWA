# 21st.dev — What's Worth Taking

**Status:** proposal, nothing built. Read it, tell me which ones you want.
**Date:** September 2026

---

## 1. What 21st.dev actually is

It's a library of **12,000+ ready-made website building blocks** — testimonial sections,
FAQ dropdowns, photo galleries, buttons, backgrounds — made by designers and shared
publicly. You browse them, see a live preview, and copy the code into your own site.

Two things about it matter for us:

1. **It's built for a different kind of website than yours.** Everything on there is
   written for React and Tailwind — a way of building sites that suits big apps with
   logins and dashboards. Your site is a single plain page, which is why it loads instantly.
2. **You don't install it, you copy it.** The code lands in your project and it's yours.
   Their own advice is literally: *copy the description, paste it into Claude Code, and let
   it rebuild the thing to fit your setup.*

That second point is the whole answer, and I'll come back to it.

---

## 2. The one decision to make first

If we used 21st.dev components **as-is**, we'd have to add four pieces of machinery to your
site — React, Tailwind, Framer Motion and a build step. In plain terms: roughly
**150–250KB of extra code before a single word of Talawa appears on screen**, and the site
would stop being one file you can open and start being a project that has to be compiled.

Your whole site is currently **52KB**.

Here's why that matters more for you than for most businesses: your customer is standing in
a pub car park on a phone with one bar of signal, deciding whether to walk over. Every extra
second is someone who doesn't. Making the site four times heavier to gain a nicer-looking
FAQ dropdown is a bad trade.

**My recommendation: use 21st.dev as a reference, not as a dependency.**

I look at how the good ones are built, then rebuild the four or five worth having in the
same plain code your site already uses. You get the improvement, the site stays fast, and
there's nothing new to maintain. This is exactly what their "paste it into Claude Code" route
is designed for.

*The alternative — rebuilding the site properly on React — only makes sense if you later want
online ordering with accounts and order history. If that day comes, we do it deliberately, not
by accident because we liked a dropdown.*

Everything below assumes the recommended route.

---

## 2a. Build status

**Ten of the eleven are built and on the site.** All of Tier 1 and the first three of
Tier 2 — rebuilt in the site's own plain code rather than pulled in as React components,
exactly as section 2 recommends. The page is still one file and still has no build step.

| # | Item | Status |
|---|---|---|
| 3.1 | Customer reviews | Built — structure only, waiting on your reviews |
| 3.2 | Questions section | Built — 4 of 9 answered, 5 waiting on you |
| 3.3 | Open-now badge | Built and working |
| 3.4 | Bottom bar on phones | Built and working |
| 4.1 | Tap a photo to enlarge | Built and working |
| 4.2 | Arrow keys and snapping | Built and working |
| 4.3 | Ticker pauses on hover | Built |
| 4.4 | Counting numbers | Built — four true figures; ratings and years still welcome |
| 4.5 | Real map | Wired and waiting — one config line away from live |
| 5.1 | Mailing list | Built — one config line from live; consent wording done |
| 5.2 | Confirmation pop-ups | Later — needs online ordering first |

The two that remain are deliberately deferred, not stuck.

**On the map:** the address now lives in a single `VENUE` block at the top of the page's
script. Fill in street, town, postcode and phone, and the directions link, the call button,
the address list and the map caption all wire themselves up — tested with a dummy postcode.
A live, tappable map cannot render inside the preview (its security settings block outside
map tiles), so the drawing stands in there; on the real site it becomes a proper map.

**On the numbers:** every figure shown is one I can stand behind — counted off the menu
boards and the opening hours. Nothing invented. A star rating, years trading or trays served
would all fit the row when you have them.

**On the mailing list:** the form, the validation, the spam trap and the UK-compliant consent
wording are all done and tested. It needs an email service behind it — paste that service's
form URL into the `LIST` block and it goes live. Until then it refuses to pretend: submitting
says plainly that nothing was sent and the address went nowhere. A privacy notice still needs
writing before it takes a single real address.

---

## 3. Worth doing — these fix real gaps

### 3.1 Customer reviews — **BUILT** ⭐ *the biggest gap on the site*
**On 21st.dev: 161 testimonial components.** Good ones: *Testimonials with Marquee*,
*Infinite Moving Cards*, *Stagger Testimonials*.

**Your site currently has no reviews on it at all.** For a food business that's the single
biggest thing missing. Someone deciding whether to drive fifteen minutes for jerk chicken
wants to see that other people are glad they did. Photos make them hungry; other people's
words make them get in the car.

The version I'd build: a slow-scrolling wall of short quotes, using the same gold ticker
language already on your page, so it looks like it belongs rather than bolted on.

**What I need from you:** your Google and Facebook reviews. Real ones only — screenshots or
copy-paste is fine. If you don't have many yet, that's worth knowing too, because getting
them is then the highest-value thing you could do this month.

### 3.2 A proper questions section — **BUILT**
**On 21st.dev: 191 FAQ blocks, 234 accordions.**

Right now the only thing answering customer questions is one line about allergies. The
questions that actually stop someone travelling are things like: *is there anything
vegetarian, can I pre-order, do you take card, what time do you sell out, whereabouts in
the car park are you.*

Include **"do you do catering or parties?"** with a plain **no, Saturdays only** as the
answer. Confirmed: you don't do catering. It still earns its place, because a stated no
stops the enquiry before it reaches you — leaving it out just means people ask anyway.

A tidy list of questions that expand when tapped.

**There's a second reason this one is worth more than it looks.** A properly built FAQ is
the part of a website Google and AI assistants quote directly. When someone asks their phone
"is there Jamaican food near me on a Saturday", this is the bit that gets read out. For a
local business that's worth more than any visual flourish on the page.

**What I need from you:** the six or eight questions you get asked most, and your answers.

### 3.3 An "Open now" badge — **BUILT**
**On 21st.dev: 605 badge components.**

A small pill in the corner that reads **OPEN NOW** on a Saturday between 4 and 8, and
**OPENS SATURDAY 4PM** the rest of the week. It works itself out from the clock.

This is the good half of the "Six Til Sold Out" idea from the original proposal, without the
fragile half. It answers the very first question anyone has, instantly.

### 3.4 A better bottom bar on phones — **BUILT**
**On 21st.dev: 49 "dock" components.**

You've currently got two flat buttons stuck to the bottom on mobile. That's prime real
estate — always visible, always thumb-reachable. It could carry the open/closed status
alongside Call and Directions and still be less cluttered than it sounds.

---

## 4. Nice improvements — do after the above

### 4.1 Tap a photo to see it bigger — **BUILT**
**Galleries: 272. Pop-ups: 328.** Right now tapping a photo does nothing. On a food site
people expect to be able to look closely. Basic, and slightly embarrassing to be missing.

### 4.2 Arrow keys and snapping on the gallery — **BUILT**
**Carousels: 239.** The drag-along rail works, but you can't use it with a keyboard, and it
doesn't settle neatly on a photo. Fixing that helps anyone not using a mouse.

### 4.3 Check our scrolling ticker against theirs — **BUILT**
**Marquees: 113.** I wrote yours by hand. Magic UI's version is the one everyone copies, and
it handles two things mine doesn't: pausing when you hover, and stopping entirely for people
who've asked their phone to reduce motion. Worth a look.

### 4.4 Counting numbers — **BUILT**
**Stats: 153.** Something like *"Trading since 2023 · 4.9 stars · 60 trays a Saturday"* with
the figures counting up as you reach them. **Only if the numbers are real** — tell me the
true ones or we skip it.

### 4.5 A real map — **PART BUILT**
**Maps: 51.** The map on the site now is drawn by me. Once you send the postcode it becomes
a real one you can tap for directions.

---

## 5. Later, if the business goes that way

### 5.1 "Tell me when the truck's out" — **BUILT**
**Forms: 1522.** An email or WhatsApp list people join to get a nudge on Saturday morning.

For a Saturday-only trader this is genuinely valuable — it catches the people who meant to
come and forgot, which is a bigger group than you'd think. But it needs somewhere to store
the addresses and proper consent wording, so it's a separate job rather than part of this one.

### 5.2 Little confirmation pop-ups — **LATER**
**Toasts: 79.** Only matters once people can order through the site. Parked.

---

## 6. What I would NOT take — and why this is the important bit

A library of 12,000 components is mostly temptation. Most of the value here is in saying no.

**The flashy backgrounds.** Shaders, liquid metal, animated gradients, glowing particle
fields — 365 of them and some are genuinely beautiful. All wrong for you. They're heavy on
older phones, and more importantly they'd compete with your food photography. Your tray photo
should be the most interesting thing on the screen. Black, gold and real pictures of real
food *is* the design; anything swirling behind it makes it look like a tech startup that
happens to sell chicken.

**The ready-made hero sections.** 1152 of them. Yours is built on an actual idea — *likkle
but talawa*, small but mighty, which is what your name means. Swapping that for a nicely
gradient-ed template would be a downgrade no matter how polished it looks.

**Vapour text, ASCII art headlines.** Completely the wrong register for Jamaican home cooking.

**Pricing tables, AI chatbots, dashboards, login screens, calendars, sidebars.** Not
applicable to a food truck.

**Tabs.** Already built — that's the "How to order" switcher.

---

## 7. Practical notes

- **Cost:** free to browse. The free account allows 2 component copies a day, which is plenty
  if we're using them as reference.
- **Licensing:** every component has a named author and the licences vary. Worth checking
  before anything goes on a commercial site rather than assuming it's free to use.
- **There's a plug-in** (an "MCP server") that lets Claude Code pull components straight in.
  Only relevant if you decide to go the React route.

---

## 8. Where it stands

All four of the original priorities are built, plus three more. Nothing else is worth
building until content arrives — the reviews wall and five of the nine questions are empty
containers, and a third placeholder section (the counting numbers) would only cheapen the
rest.

**The next move is yours, not mine.**

---

## 9. What I need from you

- [ ] Your Google / Facebook reviews (screenshots or copy-paste)
- [ ] The 6–8 questions you get asked most, with your answers
- [ ] Any real numbers worth showing (years trading, star rating, trays on a good Saturday)
- [ ] **Still outstanding from before:** prices, town, full address, postcode, the rest of the
      phone number, and your Instagram and Facebook handles
