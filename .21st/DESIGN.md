# TALAWA design context

The site is one static HTML page in `mockup/index.html`, with inline CSS and
JavaScript. Existing GSAP effects provide motion. No framework or build step.

Colours and fonts come from the existing truck identity: ink `#0A0908`, gold
`#FDCB04`, bone `#F2ECDF`, and the existing green tokens. Archivo carries the
large values, DM Mono the labels, and Work Sans the body copy. Fonts are local.

The approved strip direction is A1, A2 and B1 in `STRIP.MD`: fixed gold end fades,
a subtle 28-second shine underneath the ticker lettering, and larger Archivo
fact values. Desktop keeps three equal columns and thin dividers; phones place
labels beside values. Preserve the copy and green stripe.

Use existing page primitives. Avoid cards, badge boxes, blur filters and new
runtime dependencies. Reduced motion must stop decoration while leaving all
business information readable. Measure layout with the actual loaded fonts.
