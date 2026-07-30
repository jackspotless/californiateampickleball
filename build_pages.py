#!/usr/bin/env python3
from build import page, breadcrumbs, breadcrumb_schema, svg_courtlines, DOMAIN, BRAND, REGISTER_URL, GENERAL_REGISTER_URL, ATPL_URL, INSTAGRAM_URL, INSTAGRAM_WIDGET_SCRIPT, INSTAGRAM_WIDGET_ID, INSTAGRAM_WIDGET_KEY, RULEBOOK_URL, SCORESHEET_URL, FALL_NIGHT_2026_REGISTER_URL, FALL_DAY_2026_REGISTER_URL

# ============================================================= HOME
trail = [("Home", None)]
body = f'''
<section class="hero">
  {svg_courtlines()}
  <div class="container hero-inner">
    <div>
      <span class="eyebrow"><a class="eyebrow-link" href="{ATPL_URL}" target="_blank" rel="noopener">American Team Pickleball League</a> &middot; California</span>
      <h1>Compete Locally.<br>Qualify Nationally.</h1>
      <p class="lede">California Team Pickleball runs organized, division-based team leagues for players who want real competition and a real team behind them. Live now in the Desert / Coachella Valley &mdash; more of California is next.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="/register">Register</a>
        <a class="btn btn-outline" href="/leagues/">See the Leagues</a>
      </div>
    </div>
    <div class="hero-logo-feature">
      <img src="/images/logo.png" width="360" height="360" alt="California Team Pickleball logo">
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">On the Courts</span>
      <h2>Follow along on Instagram.</h2>
      <p>Recent photos from the league and players.</p>
    </div>
    <div data-key="{INSTAGRAM_WIDGET_KEY}" class="ft" id="{INSTAGRAM_WIDGET_ID}"></div>
    <script src="{INSTAGRAM_WIDGET_SCRIPT}"></script>
    <div class="cta-row" style="margin-top: var(--space-3);">
      <a class="btn btn-outline" href="{INSTAGRAM_URL}" target="_blank" rel="noopener">Follow on Instagram</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">How It Works</span>
      <h2>Team pickleball is a different game.</h2>
      <p>Instead of individual open play, you roster a team and compete through a season of matches against other teams in your division. Divisions are split by skill level, age bracket, and gender so every match is competitive, not a mismatch. Standings track all season, and each session ends with a champion.</p>
    </div>
    <div class="stat-strip">
      <div><span class="num">3</span><span class="lbl">Leagues per year</span></div>
      <div><span class="num">2</span><span class="lbl">Desert venues</span></div>
      <div><span class="num">1</span><span class="lbl">Region live today</span></div>
      <div><span class="num">CA</span><span class="lbl">Expanding statewide</span></div>
    </div>
  </div>
</section>

<section class="section section-tight">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Leagues</span>
      <h2>Pick your season.</h2>
      <p>Three leagues run through the year, split by day/night scheduling so you can play around work and life.</p>
    </div>
    <div class="grid-3">
      <a class="league-card" href="/leagues/fall-day">
        <span class="meta">Fall &middot; Daytime</span>
        <h3>Fall Day League</h3>
        <p>Weekday daytime matches through the fall season.</p>
      </a>
      <a class="league-card" href="/leagues/fall-night">
        <span class="meta">Fall &middot; Evening</span>
        <h3>Fall Night League</h3>
        <p>Evening matches for players who work through the day.</p>
      </a>
      <a class="league-card" href="/leagues/winter-night">
        <span class="meta">Winter &middot; Evening</span>
        <h3>Winter Night League</h3>
        <p>The desert's evening season, played through the cooler winter months.</p>
      </a>
    </div>
  </div>
</section>

<section class="section section-tight">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Regions</span>
      <h2>Starting in the desert. Going statewide.</h2>
      <p>California Team Pickleball is built to grow region by region. The Desert / Coachella Valley is live now &mdash; new regions come online as we build them out.</p>
    </div>
    <div class="grid-2">
      <a class="region-card" href="/regions/desert">
        <span class="meta">Active Now</span>
        <h3>Desert &middot; Coachella Valley</h3>
        <p>Palm Desert Resort, Monterey Country Club, and growing.</p>
      </a>
      <div class="region-card" style="cursor: default;">
        <span class="meta">Coming Soon</span>
        <h3>More of California</h3>
        <p>Interested in bringing a league to your area? <a href="/contact">Get in touch</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-tight">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">News</span>
      <h2>From the courts.</h2>
    </div>
    <div class="grid-3">
      <a class="news-card" href="/news/great-ballz-of-fire-champions">
        <span class="meta">Season Recap</span>
        <h3>Great Ballz of Fire Crowned Champions</h3>
        <p>Captain Kevin Howell's squad closes out the season atop the Men's 50+ 4.0 Division.</p>
      </a>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="callout">
      <span class="eyebrow">Sponsorship</span>
      <h2>Sponsor a CTPL season.</h2>
      <p>Sponsorship packages for the upcoming season are in development. If you're interested in supporting California Team Pickleball, <a href="/contact">get in touch</a> and we'll follow up with details.</p>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Common Questions</span>
      <h2>Before you register.</h2>
    </div>
    <div style="max-width: 72ch;">
      <details class="faq-item">
        <summary>Do I need a full team to sign up?</summary>
        <p>Team requirements vary by league and division &mdash; some players join with a team already formed, others sign up individually and get placed. Reach out and we'll point you the right direction for the league you're interested in.</p>
      </details>
      <details class="faq-item">
        <summary>What skill level do I need?</summary>
        <p>Divisions are organized by skill rating, age bracket, and gender so you're matched against comparable competition. If you're not sure where you fit, contact us and we'll help you find the right division.</p>
      </details>
      <details class="faq-item">
        <summary>How much does it cost?</summary>
        <p>Registration is $60 per player for your first team, and $50 per player if you register for a second team in a different division. Some venues may also have a separate site fee paid directly to the venue. No refunds are issued once a player has played, or after 3 weeks into the season.</p>
      </details>
      <details class="faq-item">
        <summary>Where do I register?</summary>
        <p>Registration and season scoring are handled through our league management partner. Head to the <a href="/register" style="color: var(--color-gold);">Register</a> page to get started.</p>
      </details>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="callout">
      <span class="eyebrow">Ready to Play</span>
      <h2>Get on the schedule.</h2>
      <p>Registration is handled through our league management partner. It takes a few minutes.</p>
      <div class="cta-row" style="justify-content: center; margin-top: 1em;">
        <a class="btn btn-primary" href="/register">Register</a>
      </div>
    </div>
  </div>
</section>
'''
schema = [
    {"@context": "https://schema.org", "@type": "SportsOrganization", "@id": f"{DOMAIN}/#organization",
     "name": BRAND, "url": DOMAIN + "/", "telephone": "+19518586070", "email": "jon@desertatpl.com",
     "areaServed": [{"@type": "AdministrativeArea", "name": "Coachella Valley, CA"}],
     "sameAs": []},
    {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": DOMAIN + "/"},
    {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": "Do I need a full team to sign up?", "acceptedAnswer": {"@type": "Answer", "text": "Team requirements vary by league and division. Contact us and we'll point you the right direction."}},
        {"@type": "Question", "name": "What skill level do I need?", "acceptedAnswer": {"@type": "Answer", "text": "Divisions are organized by skill rating, age bracket, and gender. Contact us if you're not sure where you fit."}},
        {"@type": "Question", "name": "How much does it cost?", "acceptedAnswer": {"@type": "Answer", "text": "Registration is $60 per player for a first team and $50 per player for a second team in a different division. A separate site fee may apply at some venues. No refunds after a player has played, or after 3 weeks into the season."}},
        {"@type": "Question", "name": "Where do I register?", "acceptedAnswer": {"@type": "Answer", "text": "Registration and scoring are handled through our league management partner, linked from the Register page."}},
    ]},
]
page("/", f"{BRAND} — Team Pickleball Leagues in California", "Organized, division-based team pickleball leagues in California. Live now in the Desert / Coachella Valley. Register today.", body, schema)

# ============================================================= ABOUT
trail = [("Home", "/"), ("About", None)]
body = f'''
<section class="page-header">
  <div class="container">
    <div class="breadcrumbs">{breadcrumbs(trail)}</div>
    <h1>About California Team Pickleball</h1>
    <p class="lede">Team-format league play, built region by region across the state.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="prose">
      <p>Founded by Jon and Dana Graham, California Team Pickleball (CTPL) is the California chapter of the <a href="{ATPL_URL}" target="_blank" rel="noopener">American Team Pickleball League (ATPL)</a>. After four successful seasons in the Coachella Valley, CTPL is expanding organized team pickleball leagues to communities across California.</p>
      <p>California Team Pickleball offers structured, competitive team leagues where players compete alongside friends throughout the season. Qualifying divisions earn the opportunity to represent California at the American Team Pickleball League National Championships.</p>

      <h2>What stays the same</h2>
      <p>The desert region keeps its leagues, its venues, and its people. Fall Day, Fall Night, and Winter Night League all continue under Jon Graham's direction. If you played under the Desert ATPL name before, you're still in the right place.</p>

      <h2>What's changing</h2>
      <p>California Team Pickleball is built to expand. The desert is the first region live under the new name, with additional California regions planned as the league grows. As we grow new leagues, league champions will compete in a regional and/or state championship to qualify for the American Team Pickleball National Championship.</p>

      <h2>How the league works</h2>
      <p>Rather than open individual play, players compete as part of a team through a season of scheduled matches against other teams in their division. Divisions are organized by skill level, age bracket, and gender to keep matches competitive. Standings track through the season, and each session crowns a champion.</p>

      <h2>Leadership</h2>
      <p>California Team Pickleball was founded by Jon and Dana Graham. Jon serves as regional director for the Desert / Coachella Valley region and sits on the Board of Directors for the American Team Pickleball League. For league questions, team registration help, or interest in bringing California Team Pickleball to a new area, <a href="/contact">get in touch</a>.</p>
    </div>
  </div>
</section>
'''
schema = [
    {"@context": "https://schema.org", "@type": "AboutPage", "url": DOMAIN + "/about"},
    breadcrumb_schema("/about", trail),
]
page("/about", f"About Us | {BRAND}", "California Team Pickleball began as the Desert ATPL, running team pickleball leagues across the Coachella Valley. Learn about the league and its statewide expansion.", body, schema)

# ============================================================= LEAGUES INDEX
trail = [("Home", "/"), ("Leagues", None)]
body = f'''
<section class="page-header">
  <div class="container">
    <div class="breadcrumbs">{breadcrumbs(trail)}</div>
    <h1>Leagues</h1>
    <p class="lede">Three seasons, split by day and night scheduling, run across every active region.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid-3">
      <a class="league-card" href="/leagues/fall-day">
        <span class="meta">Fall &middot; Daytime</span>
        <h3>Fall Day League</h3>
        <p>Weekday daytime matches through the fall season.</p>
      </a>
      <a class="league-card" href="/leagues/fall-night">
        <span class="meta">Fall &middot; Evening</span>
        <h3>Fall Night League</h3>
        <p>Evening matches for players who work through the day.</p>
      </a>
      <a class="league-card" href="/leagues/winter-night">
        <span class="meta">Winter &middot; Evening</span>
        <h3>Winter Night League</h3>
        <p>The desert's evening season, played through the cooler winter months.</p>
      </a>
    </div>
  </div>
</section>
'''
schema = [breadcrumb_schema("/leagues/", trail)]
page("/leagues/", f"Leagues | {BRAND}", "Explore California Team Pickleball's Fall Day, Fall Night, and Winter Night leagues. Organized team play by division and skill level.", body, schema)

# ============================================================= LEAGUE PAGE TEMPLATE
def league_page(slug, name, season_meta, extra_desc, play_time, dates_note, reg_open_note, division_days, venue_name, venue_note, start_date=None, end_date=None, direct_register_url=None, registration_coming_soon=False):
    trail = [("Home", "/"), ("Leagues", "/leagues/"), (name, None)]
    division_rows = "\n        ".join(f"<li><strong>{day}:</strong> {div}</li>" for day, div in division_days)
    reg_href = direct_register_url or "/register"
    reg_attrs = ' target="_blank" rel="noopener"' if direct_register_url else ''
    reg_label = "Registration Coming Soon" if registration_coming_soon else "Register"
    if registration_coming_soon:
        reg_href, reg_attrs = "/contact", ''
        signup_faq = f'Registration for {name} hasn\'t opened yet. <a href="/contact">Contact us</a> and we\'ll let you know as soon as it does.'
    elif direct_register_url:
        signup_faq = f'Registration for {name} goes through our league management partner &mdash; <a href="{direct_register_url}" target="_blank" rel="noopener">register here</a>.'
    else:
        signup_faq = 'Registration is handled through our league management partner. Visit the <a href="/register">Register</a> page to get started.'
    body = f'''
<section class="page-header">
  <div class="container">
    <div class="breadcrumbs">{breadcrumbs(trail)}</div>
    <span class="eyebrow">{season_meta}</span>
    <h1>{name}</h1>
    <p class="lede">{extra_desc}</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>Schedule</h2>
      <p>{dates_note} Play runs {play_time}. {reg_open_note}</p>
      <ul>
        {division_rows}
      </ul>

      <h2>Divisions</h2>
      <p>Within each day above, teams compete in divisions organized by skill level and age bracket, so matches stay competitive across the season. If you're not sure which division fits, we'll help you find it before you register.</p>

      <h2>Where it's played</h2>
      <p>{name} is played at <strong>{venue_name}</strong>, {venue_note}, in the <a href="/regions/desert">Desert / Coachella Valley region</a>.</p>

      <h2>FAQ</h2>
      <details class="faq-item">
        <summary>How do I sign up?</summary>
        <p>{signup_faq}</p>
      </details>
      <details class="faq-item">
        <summary>Can I join without a full team?</summary>
        <p>Requirements vary by season and division &mdash; <a href="/contact">contact us</a> and we'll point you in the right direction.</p>
      </details>
    </div>
    <div class="callout" style="margin-top: var(--space-5);">
      <h2>Ready for {name}?</h2>
      <div class="cta-row" style="justify-content: center; margin-top: 1em;">
        <a class="btn btn-primary" href="{reg_href}"{reg_attrs}>{reg_label}</a>
        <a class="btn btn-outline" style="border-color: var(--color-ink); color: var(--color-ink);" href="/contact">Ask a Question</a>
      </div>
    </div>
  </div>
</section>
'''
    event_schema = {"@context": "https://schema.org", "@type": "SportsEvent", "name": name,
         "organizer": {"@id": DOMAIN + "/#organization"}, "url": DOMAIN + f"/leagues/{slug}",
         "location": {"@type": "Place", "name": venue_name, "address": venue_note}}
    if start_date: event_schema["startDate"] = start_date
    if end_date: event_schema["endDate"] = end_date
    schema = [event_schema, breadcrumb_schema(f"/leagues/{slug}", trail)]
    page(f"/leagues/{slug}", f"{name} | {BRAND}", f"{extra_desc} Register for the {name} today.", body, schema, nav_active=f"/leagues/{slug}")

league_page(
    "fall-day", "Fall Day League", "Fall Season",
    "Daytime team pickleball for players who'd rather play before the sun gets high than after work.",
    play_time="8:00&ndash;10:00am",
    dates_note="The Fall Day League season runs October 14 &ndash; December 17.",
    reg_open_note="Registration opens September 1.",
    division_days=[("Wednesday", "Mixed Doubles"), ("Thursday", "Gender Doubles (Men's &amp; Women's)")],
    venue_name="Monterey Country Club",
    venue_note="41500 Monterey Ave., Palm Desert, CA 92260",
    start_date="2026-10-14", end_date="2026-12-17",
    direct_register_url=FALL_DAY_2026_REGISTER_URL,
)
league_page(
    "fall-night", "Fall Night League", "Fall Season",
    "Evening team pickleball for players fitting the season around a workday.",
    play_time="6:00&ndash;8:00pm",
    dates_note="The Fall Night League season runs October 12 &ndash; December 16.",
    reg_open_note="Registration opens September 1.",
    division_days=[("Monday", "Women's Doubles"), ("Tuesday", "Men's Doubles"), ("Wednesday", "Mixed Doubles")],
    venue_name="Palm Desert Resort",
    venue_note="77333 Country Club Dr., Palm Desert, CA 92211",
    start_date="2026-10-12", end_date="2026-12-16",
    direct_register_url=FALL_NIGHT_2026_REGISTER_URL,
)
league_page(
    "winter-night", "Winter Night League", "Winter Season",
    "The desert's cooler-weather evening season &mdash; competitive team pickleball played after dark through winter.",
    play_time="6:00&ndash;8:00pm",
    dates_note="Winter Night League season dates are TBD &mdash; check back or contact us for the latest.",
    reg_open_note="Registration is coming soon.",
    division_days=[("Monday", "Women's Doubles"), ("Tuesday", "Men's Doubles"), ("Wednesday", "Mixed Doubles")],
    venue_name="Palm Desert Resort",
    venue_note="77333 Country Club Dr., Palm Desert, CA 92211",
    registration_coming_soon=True,
)

# ============================================================= REGIONS INDEX
trail = [("Home", "/"), ("Regions", None)]
body = f'''
<section class="page-header">
  <div class="container">
    <div class="breadcrumbs">{breadcrumbs(trail)}</div>
    <h1>Regions</h1>
    <p class="lede">California Team Pickleball is built to grow region by region. Here's where we play today.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid-2">
      <a class="region-card" href="/regions/desert">
        <span class="meta">Active Now</span>
        <h3>Desert &middot; Coachella Valley</h3>
        <p>Palm Desert Resort, Monterey Country Club, and growing. All three leagues run here.</p>
      </a>
      <div class="region-card" style="cursor: default;">
        <span class="meta">Coming Soon</span>
        <h3>More of California</h3>
        <p>Want to bring California Team Pickleball to your area? <a href="/contact">Get in touch</a> &mdash; we're building out the next region.</p>
      </div>
    </div>
  </div>
</section>
'''
schema = [breadcrumb_schema("/regions/", trail)]
page("/regions/", f"Regions | {BRAND}", "See where California Team Pickleball runs leagues today, starting in the Desert / Coachella Valley, with more California regions on the way.", body, schema)

# ============================================================= DESERT REGION PAGE
trail = [("Home", "/"), ("Regions", "/regions/"), ("Desert / Coachella Valley", None)]
body = f'''
<section class="page-header">
  <div class="container">
    <div class="breadcrumbs">{breadcrumbs(trail)}</div>
    <span class="eyebrow">Active Region</span>
    <h1>Desert &middot; Coachella Valley</h1>
    <p class="lede">The founding region of California Team Pickleball, formerly Desert ATPL, led by regional director Jon Graham.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="prose">
      <p>The Desert / Coachella Valley region is where it all started. All three California Team Pickleball leagues &mdash; Fall Day, Fall Night, and Winter Night &mdash; run here, with teams competing across skill, age, and gender divisions all season.</p>
    </div>

    <div class="section-head" style="margin-top: var(--space-5);">
      <span class="eyebrow">Where We Play</span>
      <h2>Home venues</h2>
    </div>
    <div class="venue-list">
      <div class="venue-item">
        <h3>Palm Desert Resort</h3>
        <span class="meta">77333 Country Club Dr., Palm Desert, CA 92211</span>
      </div>
      <div class="venue-item">
        <h3>Monterey Country Club</h3>
        <span class="meta">41500 Monterey Ave., Palm Desert, CA 92260</span>
      </div>
    </div>

    <div class="section-head" style="margin-top: var(--space-5);">
      <span class="eyebrow">Leagues Here</span>
      <h2>Play in the desert</h2>
    </div>
    <div class="grid-3">
      <a class="league-card" href="/leagues/fall-day"><span class="meta">Fall &middot; Daytime</span><h3>Fall Day League</h3></a>
      <a class="league-card" href="/leagues/fall-night"><span class="meta">Fall &middot; Evening</span><h3>Fall Night League</h3></a>
      <a class="league-card" href="/leagues/winter-night"><span class="meta">Winter &middot; Evening</span><h3>Winter Night League</h3></a>
    </div>

    <div class="callout" style="margin-top: var(--space-5);">
      <h2>Play in the desert region</h2>
      <div class="cta-row" style="justify-content: center; margin-top: 1em;">
        <a class="btn btn-primary" href="/register">Register</a>
      </div>
    </div>
  </div>
</section>
'''
schema = [
    {"@context": "https://schema.org", "@type": "SportsOrganization", "name": f"{BRAND} — Desert / Coachella Valley",
     "parentOrganization": {"@id": DOMAIN + "/#organization"},
     "areaServed": {"@type": "AdministrativeArea", "name": "Coachella Valley, CA"}},
    breadcrumb_schema("/regions/desert", trail),
]
page("/regions/desert", f"Desert / Coachella Valley League | {BRAND}", "Team pickleball leagues in the Desert / Coachella Valley, playing at Palm Desert Resort and Monterey Country Club. The founding region of California Team Pickleball.", body, schema)

# ============================================================= NEWS INDEX
trail = [("Home", "/"), ("News", None)]
body = f'''
<section class="page-header">
  <div class="container">
    <div class="breadcrumbs">{breadcrumbs(trail)}</div>
    <h1>News</h1>
    <p class="lede">Season recaps, standings, and stories from the courts.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid-3">
      <a class="news-card" href="/news/great-ballz-of-fire-champions">
        <span class="meta">Season Recap</span>
        <h3>Great Ballz of Fire Crowned Champions</h3>
        <p>Captain Kevin Howell's squad closes out the season atop the Men's 50+ 4.0 Division.</p>
      </a>
    </div>
  </div>
</section>
'''
schema = [breadcrumb_schema("/news/", trail)]
page("/news/", f"News | {BRAND}", "Season recaps, champions, and updates from California Team Pickleball leagues.", body, schema)

# ============================================================= NEWS POST
trail = [("Home", "/"), ("News", "/news/"), ("Great Ballz of Fire Crowned Champions", None)]
body = f'''
<section class="page-header">
  <div class="container">
    <div class="breadcrumbs">{breadcrumbs(trail)}</div>
    <span class="eyebrow">Season Recap</span>
    <h1>Great Ballz of Fire Crowned Champions</h1>
    <p style="color: var(--color-ink-soft); font-family: var(--font-mono); font-size: 0.9rem; margin-top: 0.4em;">Published December 12, 2025</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <article class="prose">
      <p>Great Ballz of Fire, captained by Kevin Howell, closed out the fall season as champions of the Men's 50+ 4.0 Division &mdash; a title earned while playing under the Desert ATPL banner, the desert region's league before its rebrand to California Team Pickleball.</p>
      <p>The team carried strong chemistry and consistent play through the season, setting the pace in their division from early on. Congratulations to the whole roster on a well-earned championship.</p>
      <p>Want your team's name here next season? <a href="/register">Register for an upcoming league</a> and get on the schedule.</p>
    </article>
  </div>
</section>
'''
schema = [
    {"@context": "https://schema.org", "@type": "BlogPosting", "headline": "Great Ballz of Fire Crowned Champions",
     "author": {"@type": "Organization", "name": BRAND}, "datePublished": "2025-12-12",
     "image": DOMAIN + "/images/og-default.png"},
    breadcrumb_schema("/news/great-ballz-of-fire-champions", trail),
]
page("/news/great-ballz-of-fire-champions", f"Great Ballz of Fire Crowned Champions | {BRAND}", "Great Ballz of Fire, captained by Kevin Howell, are champions of the Men's 50+ 4.0 Division in the desert region's fall season.", body, schema)

# ============================================================= RULES & FORMS
trail = [("Home", "/"), ("Rules & Forms", None)]
body = f'''
<section class="page-header">
  <div class="container">
    <div class="breadcrumbs">{breadcrumbs(trail)}</div>
    <h1>Rules &amp; Forms</h1>
    <p class="lede">Official rulebook and match score sheet for the Desert Division.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="venue-list">
      <div class="venue-item">
        <h3>Desert Division Rulebook</h3>
        <span class="meta" style="color: var(--color-clay);">PDF &middot; Desert Division</span>
        <p style="margin: 0.6em 0 1em; color: var(--color-ink-soft);">Official rules, divisions of play, scoring, playoffs, and player eligibility for the Desert Division.</p>
        <a class="btn btn-outline" style="border-color: var(--color-ink); color: var(--color-ink);" href="{RULEBOOK_URL}" target="_blank" rel="noopener">Open Full-Size / Download</a>
      </div>
      <div class="venue-item">
        <h3>Match Score Sheet</h3>
        <span class="meta" style="color: var(--color-clay);">PDF &middot; Fillable / Printable</span>
        <p style="margin: 0.6em 0 1em; color: var(--color-ink-soft);">Official round-by-round score sheet for captains to record match results.</p>
        <a class="btn btn-outline" style="border-color: var(--color-ink); color: var(--color-ink);" href="{SCORESHEET_URL}" target="_blank" rel="noopener">Open Full-Size / Download</a>
      </div>
    </div>

    <h2 style="margin-top: var(--space-5);">Rulebook Preview</h2>
    <div class="pdf-preview">
      <iframe src="{RULEBOOK_URL}" title="Desert Division Rulebook preview"></iframe>
      <div class="pdf-preview-fallback">
        <p>PDF preview isn't supported on this device.</p>
        <a class="btn btn-primary" href="{RULEBOOK_URL}" target="_blank" rel="noopener">Open Rulebook (PDF)</a>
      </div>
    </div>

    <h2 style="margin-top: var(--space-5);">Score Sheet Preview</h2>
    <div class="pdf-preview">
      <iframe src="{SCORESHEET_URL}" title="Match Score Sheet preview"></iframe>
      <div class="pdf-preview-fallback">
        <p>PDF preview isn't supported on this device.</p>
        <a class="btn btn-primary" href="{SCORESHEET_URL}" target="_blank" rel="noopener">Open Score Sheet (PDF)</a>
      </div>
    </div>

    <div class="prose" style="margin-top: var(--space-5);">
      <p>Have a question about rules or scoring in the meantime? <a href="/contact">Contact us</a> and we'll help directly.</p>
    </div>
  </div>
</section>
'''
schema = [{"@context": "https://schema.org", "@type": "WebPage", "name": "Rules & Forms"}, breadcrumb_schema("/rules-forms", trail)]
page("/rules-forms", f"Rules & Forms | {BRAND}", "Official Desert Division rulebook and match score sheet for California Team Pickleball.", body, schema)

# ============================================================= REGISTER
trail = [("Home", "/"), ("Register", None)]
body = f'''
<section class="page-header">
  <div class="container">
    <div class="breadcrumbs">{breadcrumbs(trail)}</div>
    <h1>Register</h1>
    <p class="lede">Registration, scheduling, and season scoring for California Team Pickleball are all handled through our league management partner.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="callout">
      <span class="eyebrow">Continue to Registration</span>
      <h2>You'll be redirected to our registration partner.</h2>
      <p>Click below to view current leagues, divisions, and sign up. This opens in our league management system.</p>
      <div class="cta-row" style="justify-content: center; margin-top: 1.2em;">
        <a class="btn btn-primary" href="{GENERAL_REGISTER_URL}" target="_blank" rel="noopener">Go to Registration &rarr;</a>
      </div>
    </div>
    <div class="prose" style="margin-top: var(--space-5);">
      <h2>Registering for a specific league?</h2>
      <p>Direct links go straight to that league's registration form. Leagues without a direct link yet route through the general registration page above &mdash; check back or contact us.</p>
      <ul>
        <li><a href="{FALL_DAY_2026_REGISTER_URL}" target="_blank" rel="noopener">Fall Day League 2026</a></li>
        <li><a href="{FALL_NIGHT_2026_REGISTER_URL}" target="_blank" rel="noopener">Fall Night League 2026</a></li>
      </ul>
    </div>
    <div class="prose" style="margin-top: var(--space-5);">
      <h2>Not sure where to start?</h2>
      <p>If you're new to team pickleball, aren't sure which division fits, or want help finding a team, <a href="/contact">contact Jon Graham</a> before you register and we'll point you in the right direction.</p>
    </div>
  </div>
</section>
'''
schema = [breadcrumb_schema("/register", trail)]
page("/register", f"Register | {BRAND}", "Register for California Team Pickleball leagues. Registration and scoring are handled through our league management partner.", body, schema)

# ============================================================= CONTACT
trail = [("Home", "/"), ("Contact", None)]
body = f'''
<section class="page-header">
  <div class="container">
    <div class="breadcrumbs">{breadcrumbs(trail)}</div>
    <h1>Contact</h1>
    <p class="lede">Questions about leagues, divisions, or registration &mdash; reach out directly.</p>
  </div>
</section>
<section class="section">
  <div class="container grid-2">
    <div class="prose">
      <h2>Reach Jon directly</h2>
      <p><a href="tel:+19518586070" style="font-weight:700; color: var(--color-court); font-size:1.2rem;">(951) 858-6070</a><br>
      <a href="mailto:jon@desertatpl.com">jon@desertatpl.com</a></p>
      <p>Jon Graham is the regional director for the Desert / Coachella Valley region and the best first stop for league questions, division placement, and registration help.</p>
      <h2>Looking to register?</h2>
      <p>Head to <a href="/register">Register</a> to sign up directly through our league management partner.</p>
    </div>
    <div>
      <form class="contact-form" name="contact" method="POST" data-netlify="true" action="/thank-you">
        <input type="hidden" name="form-name" value="contact">
        <p style="display:none">
          <label>Don't fill this out: <input name="bot-field"></label>
        </p>
        <div class="form-row">
          <label for="name">Your name</label>
          <input type="text" id="name" name="name" required>
        </div>
        <div class="form-row">
          <label for="phone">Phone</label>
          <input type="tel" id="phone" name="phone" required>
        </div>
        <div class="form-row">
          <label for="email">Email</label>
          <input type="email" id="email" name="email" required>
        </div>
        <div class="form-row">
          <label for="league">Which league?</label>
          <select id="league" name="league">
            <option value="">Select a league...</option>
            <option value="Fall Day League">Fall Day League</option>
            <option value="Fall Night League">Fall Night League</option>
            <option value="Winter Night League">Winter Night League</option>
            <option value="Not sure">Not sure yet</option>
          </select>
        </div>
        <div class="form-row">
          <label for="message">Message</label>
          <textarea id="message" name="message" rows="4"></textarea>
        </div>
        <button type="submit" class="btn btn-primary btn-block">Send message</button>
      </form>
    </div>
  </div>
</section>
'''
schema = [{"@context": "https://schema.org", "@type": "ContactPage", "url": DOMAIN + "/contact"}, breadcrumb_schema("/contact", trail)]
page("/contact", f"Contact | {BRAND}", "Contact California Team Pickleball for league questions, division placement, or registration help in the Desert / Coachella Valley region.", body, schema)

# ============================================================= THANK YOU
body = f'''
<section class="section" style="padding-top: var(--space-6);">
  <div class="container" style="text-align:center;">
    <span class="eyebrow" style="justify-content:center;">Message Sent</span>
    <h1 style="margin-top:0.3em;">Thanks &mdash; we've got it.</h1>
    <p class="lede" style="margin: 0.8em auto 1.6em; color: var(--color-ink-soft);">Jon will follow up shortly. In the meantime, feel free to browse the leagues or head straight to registration.</p>
    <div class="cta-row" style="justify-content:center;">
      <a class="btn btn-primary" href="/register">Register</a>
      <a class="btn btn-outline" style="border-color: var(--color-ink); color: var(--color-ink);" href="/">Back to Home</a>
    </div>
  </div>
</section>
'''
page("/thank-you", f"Message Sent | {BRAND}", "Thanks for reaching out to California Team Pickleball.", body, [], noindex=True)

# ============================================================= PRIVACY / TERMS
privacy_body = f'''
<section class="page-header">
  <div class="container">
    <h1>Privacy Policy</h1>
    <p class="lede">Last updated: July 29, 2026</p>
  </div>
</section>
<section class="section">
  <div class="container prose">
    <p>This Privacy Policy describes how California Team Pickleball ("CTPL," "we," "us," or "our") collects, uses, and discloses information in connection with your use of caliteampickleball.com (the "Site"). It does not apply to information collected offline, through our league management partner's platform, or through any other third-party service, each of which is governed by its own privacy policy.</p>

    <h2>1. Information We Collect</h2>
    <p><strong>Information you provide directly.</strong> If you submit our contact form, we collect the name, phone number, email address, league of interest, and message content you provide. This submission is processed through Netlify Forms, our website hosting provider's form-handling service.</p>
    <p><strong>Information collected automatically.</strong> As with most websites, our hosting provider (Netlify) automatically logs standard technical data for each visit to the Site, including IP address, browser type, device information, referring/exit pages, and timestamps. This data is used for site administration, security, performance monitoring, and aggregate analytics, and is not used to identify individual visitors beyond what is inherent in that technical data.</p>
    <p><strong>Information we do not collect.</strong> We do not collect payment card information, government-issued identification, or other sensitive personal information through the Site. Team and player registration, payment processing, and season scoring take place entirely on our league management partner's platform at <a href="{REGISTER_URL}" target="_blank" rel="noopener">ctpl.pickleballscores.com</a> (Tenniscores). Any information you submit there is governed exclusively by that platform's privacy policy and terms, not this one.</p>

    <h2>2. How We Use Information</h2>
    <p>We use the information described above to: respond to inquiries submitted through the contact form; provide information about leagues, divisions, and registration; maintain, secure, and improve the Site; and comply with applicable legal obligations. We do not use contact form submissions for advertising or marketing purposes beyond responding to your specific inquiry, unless you separately opt in to further communication.</p>

    <h2>3. How We Share Information</h2>
    <p>We do not sell, rent, or trade your personal information. We may share information only in the following limited circumstances: with service providers who process data on our behalf and under our instructions (e.g., Netlify for form processing and hosting); when required by law, subpoena, or other legal process; to protect the rights, property, or safety of CTPL, our players, or the public; or in connection with a merger, reorganization, or transfer of league operations, subject to the same protections described here.</p>

    <h2>4. Third-Party Services</h2>
    <p>The Site incorporates a limited number of third-party services, each governed by its own privacy policy, which we do not control:</p>
    <ul>
      <li><strong>Google Fonts</strong> &mdash; typefaces are served from Google's infrastructure, which may log the request (including IP address) independently of this Site.</li>
      <li><strong>Fouita</strong> &mdash; our homepage Instagram feed is rendered via Fouita's embedded widget, which retrieves content from Instagram and may set its own cookies or similar technologies to function.</li>
      <li><strong>Tenniscores / PickleballScores</strong> &mdash; our league management partner, used for registration, payment, scheduling, and scoring, linked from the Register and Scores &amp; Schedule pages.</li>
      <li><strong>Netlify</strong> &mdash; our website host and contact form processor.</li>
    </ul>
    <p>We do not display third-party advertising on the Site and do not work with any advertising networks.</p>

    <h2>5. Cookies and Tracking Technologies</h2>
    <p>The Site itself does not set first-party tracking or advertising cookies. The third-party services listed in Section 4 may set their own cookies or similar technologies as part of their normal operation; those are governed by each provider's respective policy. Most browsers allow you to block or delete cookies through their settings; doing so may affect the functionality of embedded content such as the Instagram feed.</p>

    <h2>6. Data Retention</h2>
    <p>Contact form submissions are retained only as long as reasonably necessary to respond to your inquiry and for our internal recordkeeping, after which they may be deleted. Standard hosting log data is retained according to Netlify's own data retention practices.</p>

    <h2>7. Data Security</h2>
    <p>We use industry-standard measures appropriate to the nature of the information collected, including transmitting the Site over HTTPS. No method of transmission or storage is completely secure, and we cannot guarantee absolute security.</p>

    <h2>8. Children's Privacy</h2>
    <p>All CTPL league participants must be 18 years of age or older; the Site is not directed to children, and we do not knowingly collect personal information from anyone under the age of 13. If you believe a child has provided us with personal information, please contact us and we will promptly remove it.</p>

    <h2>9. Your Choices and Rights</h2>
    <p>You may decline to submit information through our contact form; doing so simply means we won't be able to respond to an inquiry you haven't made. You may control cookies through your browser settings as described in Section 5. If you would like to request access to, correction of, or deletion of personal information you've submitted to us directly, contact us using the information in Section 12 and we will respond as required by applicable law.</p>

    <h2>10. Do Not Track</h2>
    <p>The Site does not currently respond to browser "Do Not Track" signals, as no common industry standard for interpreting them has been adopted.</p>

    <h2>11. Changes to This Policy</h2>
    <p>We may revise this Privacy Policy from time to time. Material changes will be reflected by an updated "Last updated" date at the top of this page. Continued use of the Site after changes take effect constitutes acceptance of the revised policy.</p>

    <h2>12. Contact Us</h2>
    <p>Questions about this Privacy Policy can be directed to <a href="mailto:jon@desertatpl.com">jon@desertatpl.com</a>.</p>
  </div>
</section>
'''
page("/privacy", f"Privacy Policy | {BRAND}", "Privacy policy for California Team Pickleball.", privacy_body, [{"@context":"https://schema.org","@type":"WebPage","name":"Privacy Policy"}])

terms_body = f'''
<section class="page-header">
  <div class="container">
    <h1>Terms of Service</h1>
    <p class="lede">Last updated: July 29, 2026</p>
  </div>
</section>
<section class="section">
  <div class="container prose">
    <p>These Terms of Service ("Terms") govern your use of caliteampickleball.com (the "Site"), operated by California Team Pickleball ("CTPL," "we," "us," or "our"). By using the Site, you agree to these Terms. If you do not agree, please do not use the Site.</p>

    <h2>1. Use of the Site</h2>
    <p>The Site is provided for informational purposes about CTPL leagues, divisions, venues, rules, and registration. You may not use the Site for any unlawful purpose, to interfere with its normal operation, or to attempt to gain unauthorized access to any part of the Site or its underlying systems.</p>

    <h2>2. League Registration &amp; Participation</h2>
    <p>Team and player registration, payment, and season scoring are handled entirely through our league management partner's platform at <a href="{REGISTER_URL}" target="_blank" rel="noopener">ctpl.pickleballscores.com</a> (Tenniscores), not on this Site. Registration is subject to that platform's own terms, our published league rules (see the <a href="/rules-forms">Rules &amp; Forms</a> page), and any liability waiver or release presented at the time of registration. This Site does not itself process registration, payment, or waiver acceptance.</p>

    <h2>3. Assumption of Risk</h2>
    <p>Pickleball and other physical league activities carry an inherent risk of injury. Participation in any CTPL league, match, or event is voluntary, and participants assume all risks associated with that participation. This Site's content, including schedules, rules, and venue information, is provided for informational purposes only and does not itself constitute or replace the liability waiver executed through our registration partner, which participants must separately accept before playing.</p>

    <h2>4. Fees, Payment &amp; Refunds</h2>
    <p>League fees are set and collected through our registration partner and are described on individual league pages and at the point of registration. Refunds are governed by the policy in effect at the time of registration; as a general matter, no refunds are issued once a player has played in a match, or after the refund window specified in our league rules has passed.</p>

    <h2>5. Code of Conduct</h2>
    <p>Participants are expected to follow the sportsmanship and conduct standards described in our league rules, available on the <a href="/rules-forms">Rules &amp; Forms</a> page. Violations may result in sanctions up to and including suspension from league play, as determined by the League Coordinator or Rules Committee, without refund.</p>

    <h2>6. Intellectual Property</h2>
    <p>The Site's text, graphics, logos, and design are owned by CTPL or used under license, and are protected by applicable intellectual property laws. You may view and share Site content for personal, non-commercial purposes. You may not reproduce, modify, distribute, or otherwise use Site content for commercial purposes without our prior written consent.</p>

    <h2>7. Third-Party Links &amp; Services</h2>
    <p>The Site links to and embeds content from third-party services, including our registration partner, Instagram (via an embedded feed), and our web hosting provider. We do not control and are not responsible for the content, policies, or practices of any third-party service. Your use of those services is governed by their own terms.</p>

    <h2>8. Disclaimer of Warranties</h2>
    <p>The Site and its content are provided "as is" and "as available," without warranties of any kind, express or implied, including but not limited to accuracy, completeness, or fitness for a particular purpose. Schedules, dates, venues, and other league details are subject to change; we do not guarantee that information on the Site is current at all times.</p>

    <h2>9. Limitation of Liability</h2>
    <p>To the fullest extent permitted by law, CTPL and its organizers, directors, and volunteers will not be liable for any indirect, incidental, special, or consequential damages arising from your use of the Site or participation in any CTPL league or event, including but not limited to personal injury, except where such liability cannot be excluded under applicable law.</p>

    <h2>10. Indemnification</h2>
    <p>You agree to indemnify and hold harmless CTPL, its organizers, directors, and volunteers from any claims, damages, or expenses (including reasonable attorneys' fees) arising from your use of the Site, your participation in league activities, or your violation of these Terms.</p>

    <h2>11. Governing Law</h2>
    <p>These Terms are governed by the laws of the State of California, without regard to its conflict-of-law principles.</p>

    <h2>12. Changes to These Terms</h2>
    <p>We may update these Terms from time to time. Material changes will be reflected by an updated "Last updated" date at the top of this page. Continued use of the Site after changes take effect constitutes acceptance of the revised Terms.</p>

    <h2>13. Contact</h2>
    <p>Questions about these Terms can be sent to <a href="mailto:jon@desertatpl.com">jon@desertatpl.com</a>.</p>
  </div>
</section>
'''
page("/terms", f"Terms of Service | {BRAND}", "Terms of service for California Team Pickleball.", terms_body, [{"@context":"https://schema.org","@type":"WebPage","name":"Terms of Service"}])

print("All pages generated.")
