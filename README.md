# California Team Pickleball — Site Build

Static HTML/CSS/JS, generated via `build.py` + `build_pages.py` (Python generator
pattern — re-run `python3 build_pages.py` after any content or nav change to keep
every page in sync). Deploys to Netlify with Pretty URLs; canonical pattern is
extensionless throughout (see `netlify.toml` for the `.html` → extensionless
redirect).

## Why this build deviates from the standard Baseline home-service template

This client is a multi-region sports league, not a single-location home service
business. The standard "5 services × 10 cities" model doesn't map cleanly, so:

- **"Services"** → **Leagues** (Fall Day, Fall Night, Winter Night)
- **"Service areas"** → **Regions** (Desert / Coachella Valley live now; built so
  additional regions can be added as their own pages later without restructuring)
- Word counts on league/region pages are intentionally lighter (300–400 words)
  than the 800–1500 word floor in the standard template. There isn't yet enough
  confirmed format/rules detail from Jon to respons­ibly hit that floor without
  padding or inventing specifics. Expand these pages once Jon supplies real
  format details, pricing, and season dates — flagged below.
- Schema uses `SportsOrganization` / `SportsEvent` instead of `LocalBusiness`,
  since this isn't a single physical storefront with hours and an address.

## Placeholder / TODO — confirm before launch

- **Brand:** Colors, fonts, and logo are all placeholder (see `css/style.css`
  design tokens at the top of the file — everything lives in CSS custom
  properties for a one-file swap). Placeholder favicon/OG image are generated
  flat color squares in `images/` — replace with real logo assets.
- **Registration link:** `/register` points to `https://ctpl.pickleballscores.com`
  (the site root). Jon has not yet created a direct registration link — swap
  `REGISTER_URL` in `build.py` once he does, then re-run the generator.
- **Venues:** Palm Desert Resort and Monterey Country Club are listed with city
  "Palm Desert, CA" as a reasonable default — confirm exact addresses with Jon
  for full NAP accuracy and to add `geo` coordinates to schema.
- **League format/rules:** Division structure, exact scoring format, and season
  dates are described in general terms pending confirmation from Jon. Update
  `build_pages.py` league_page() calls once confirmed, and expand word count
  toward the standard floor at that point.
- **Pricing:** Not published on the site (FAQ answer defers to "shown at
  registration" / contact). Add if Jon wants public pricing per the brand's
  "no gated pricing" philosophy — currently there's no number to publish.
- **News:** The one live post ("Great Ballz of Fire Crowned Champions") is a
  paraphrase of copy from the outgoing Desert ATPL site, rebranded and
  reworded, with a placeholder `datePublished` (2025-12-01) — confirm real date.
- **Legal pages:** `/privacy` and `/terms` are placeholder boilerplate, clearly
  marked inline. This is a new organization with no prior legal text to take
  verbatim (unlike a typical client migration) — these need real legal review
  before launch, not just a copy-paste swap.
- **Social profiles:** Facebook/Instagram icons in the footer currently link to
  `#`. Add real profile URLs once Jon shares them (or remove icons for
  platforms that don't exist).
- **Email:** Using `jon@desertatpl.com` throughout since that's the only
  address on file. Flag whether a `@caliteampickleball.com` address will be
  set up post-rebrand and swap if so.

## Ownership / accounts still to set up

Per the standard Baseline account-ownership model: register `caliteampickleball.com`
on the client's registrar, create GitHub + Netlify accounts in the client's name,
add Baseline as collaborator, set up GA4 + GSC once ready. None of this is done
yet — this is a content/structure build, not a deployed site.

## File structure

```
/
├── index.html, about.html, contact.html, register.html, thank-you.html
├── privacy.html, terms.html, 404.html
├── leagues/ (index + fall-day, fall-night, winter-night)
├── regions/ (index + desert)
├── news/ (index + great-ballz-of-fire-champions)
├── css/style.css   — all design tokens at top
├── js/main.js      — nav toggle / dropdown behavior
├── images/         — placeholder favicon + og-default only
├── build.py        — shared header/footer/schema template functions
├── build_pages.py  — per-page content, run this to regenerate the site
├── netlify.toml, robots.txt, sitemap.xml
```
