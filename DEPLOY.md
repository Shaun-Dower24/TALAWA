# Putting the site on Netlify

The site is a plain static page — no build step, nothing to compile. Netlify
serves the `mockup/` folder as the site root, which `netlify.toml` already
tells it to do. You should not have to configure anything.

## One-time setup (about two minutes)

1. Go to **[app.netlify.com](https://app.netlify.com)** and sign in with GitHub.
2. **Add new site → Import an existing project → GitHub.**
3. Pick **`Shaun-Dower24/TALAWA`**.
4. The branch should be **`claude/talawa-website-design-orcvgk`** (it is the
   repo's default branch, so it should already be selected).
5. Leave the build command empty and the publish directory as `mockup` —
   `netlify.toml` sets both. Click **Deploy**.

That's it. Netlify gives you a URL like `something-random-123.netlify.app`.

**From then on, every change I push deploys itself.** No further steps.

## Giving it a proper name

In Netlify: **Site configuration → Change site name** → e.g. `talawa-caribbean`,
giving you `talawa-caribbean.netlify.app`.

When you're ready for a real domain (`talawacaribbean.co.uk` or similar), buy it
anywhere and point it at Netlify under **Domain management**. A real domain is
worth more than the design for showing up in Stevenage searches.

## Before it stops being a preview

Right now the site is **deliberately hidden from Google**. That is on purpose:
prices are blank and the review cards are placeholders, and that is not the
version you want Stevenage to find. Two things to undo at launch:

- `mockup/robots.txt` — delete the `Disallow` lines
- `mockup/index.html` — delete the `<meta name="robots" content="noindex...">`
  tag near the top

Both are commented in place so they are easy to find. Ask me and I'll do it.

## Still outstanding before launch

- Prices and dish descriptions
- Google and Facebook reviews for the reviews section
- The Facebook handle
- What time the food usually sells out (the last unanswered FAQ)
- A privacy notice, before the mailing list takes a single real address
- An email service connected to the mailing list (`LIST.endpoint` in the page)
