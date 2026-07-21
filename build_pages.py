#!/usr/bin/env python3
from build import page, breadcrumbs, breadcrumb_schema, svg_courtlines, DOMAIN, BRAND, REGISTER_URL, ATPL_URL, INSTAGRAM_URL

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
        <a class="btn btn-primary" href="/register">Register a Team</a>
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
    <div id="ft-insta-app"></div>
    <script type="module">import App from "https://cdn.fouita.com/public/instagram-feed.js?11";new App({{target: document.getElementById("ft-insta-app"),props:{{"settings":{{"layout":"carousel","source":"insta","selected":"uname","header":true,"autoplay":true,"zigzag":false,"cols":4,"cardHeight":300,"gap":0,"direction":"down","height":700,"bgColor":"","txtColor":""}}}}}});</script>
    <div id="ft-insta-brd"><a href="https://fouita.com/website-widgets/instagram-feed" target="_blank">Embed Instagram Feed</a><a href="https://fouita.com" target="_blank">with Fouita</a></div>
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
        <p>Pricing is set each season and shown when you register. Contact us if you'd like current pricing before you sign up.</p>
      </details>
      <details class="faq-item">
        <summary>Where do I register?</summary>
        <p>Registration and season scoring are handled through our league management partner. Head to the <a href="/register" style="color: var(--color-gold);">Register a Team</a> page to get started.</p>
      </details>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="callout">
      <span class="eyebrow">Ready to Play</span>
      <h2>Get your team on the schedule.</h2>
      <p>Registration is handled through our league management partner. It takes a few minutes.</p>
      <div class="cta-row" style="justify-content: center; margin-top: 1em;">
        <a class="btn btn-primary" href="/register">Register a Team</a>
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
        {"@type": "Question", "name": "How much does it cost?", "acceptedAnswer": {"@type": "Answer", "text": "Pricing is set each season and shown when you register."}},
        {"@type": "Question", "name": "Where do I register?", "acceptedAnswer": {"@type": "Answer", "text": "Registration and scoring are handled through our league management partner, linked from the Register a Team page."}},
    ]},
]
page("/", f"{BRAND} — Team Pickleball Leagues in California", "Organized, division-based team pickleball leagues in California. Live now in the Desert / Coachella Valley. Register your team today.", body, schema)

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
      <p>California Team Pickleball is built to expand. The desert is the first region live under the new name, with additional California regions planned as the league grows. Each region runs its own leagues and divisions locally, with a shared statewide identity.</p>

      <h2>How the league works</h2>
      <p>Rather than open individual play, players compete as part of a team through a season of scheduled matches against other teams in their division. Divisions are organized by skill level, age bracket, and gender to keep matches competitive. Standings track through the season, and each session crowns a champion.</p>

      <h2>Leadership</h2>
      <p>California Team Pickleball was founded by Jon and Dana Graham. Jon serves as regional director for the Desert / Coachella Valley region. For league questions, team registration help, or interest in bringing California Team Pickleball to a new area, <a href="/contact">get in touch</a>.</p>
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
def league_page(slug, name, season_meta, schedule_note, extra_desc):
    trail = [("Home", "/"), ("Leagues", "/leagues/"), (name, None)]
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
      <p>{schedule_note} Exact match dates and enrollment windows are announced each season &mdash; check current status when you register, or <a href="/contact">contact us</a> for the latest.</p>

      <h2>Divisions</h2>
      <p>Teams compete in divisions organized by skill level, age bracket, and gender, so matches stay competitive across the season. If you're not sure which division fits, we'll help you find it before you register.</p>

      <h2>Where it's played</h2>
      <p>{name} currently runs in the <a href="/regions/desert">Desert / Coachella Valley region</a>, at venues including Palm Desert Resort and Monterey Country Club.</p>

      <h2>FAQ</h2>
      <details class="faq-item">
        <summary>How do I sign up?</summary>
        <p>Registration is handled through our league management partner. Visit the <a href="/register">Register a Team</a> page to get started.</p>
      </details>
      <details class="faq-item">
        <summary>Can I join without a full team?</summary>
        <p>Requirements vary by season and division &mdash; <a href="/contact">contact us</a> and we'll point you in the right direction.</p>
      </details>
    </div>
    <div class="callout" style="margin-top: var(--space-5);">
      <h2>Ready for {name}?</h2>
      <div class="cta-row" style="justify-content: center; margin-top: 1em;">
        <a class="btn btn-primary" href="/register">Register a Team</a>
        <a class="btn btn-outline" style="border-color: var(--color-ink); color: var(--color-ink);" href="/contact">Ask a Question</a>
      </div>
    </div>
  </div>
</section>
'''
    schema = [
        {"@context": "https://schema.org", "@type": "SportsEvent", "name": name,
         "organizer": {"@id": DOMAIN + "/#organization"}, "url": DOMAIN + f"/leagues/{slug}",
         "location": {"@type": "Place", "name": "Desert / Coachella Valley, CA"}},
        breadcrumb_schema(f"/leagues/{slug}", trail),
    ]
    page(f"/leagues/{slug}", f"{name} | {BRAND}", f"{extra_desc} Register your team for the {name} today.", body, schema, nav_active=f"/leagues/{slug}")

league_page("fall-day", "Fall Day League", "Fall Season", "Weekday daytime matches through the fall.", "Daytime team pickleball for players who'd rather play before the sun gets high than after work.")
league_page("fall-night", "Fall Night League", "Fall Season", "Evening matches through the fall season.", "Evening team pickleball for players fitting the season around a workday.")
league_page("winter-night", "Winter Night League", "Winter Season", "Evening matches through the winter months.", "The desert's cooler-weather evening season &mdash; competitive team pickleball played after dark through winter.")

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
        <span class="meta">Palm Desert, CA</span>
      </div>
      <div class="venue-item">
        <h3>Monterey Country Club</h3>
        <span class="meta">Palm Desert, CA</span>
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
        <a class="btn btn-primary" href="/register">Register a Team</a>
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
     "author": {"@type": "Organization", "name": BRAND}, "datePublished": "2025-12-01",
     "image": DOMAIN + "/images/og-default.png"},
    breadcrumb_schema("/news/great-ballz-of-fire-champions", trail),
]
page("/news/great-ballz-of-fire-champions", f"Great Ballz of Fire Crowned Champions | {BRAND}", "Great Ballz of Fire, captained by Kevin Howell, are champions of the Men's 50+ 4.0 Division in the desert region's fall season.", body, schema)

# ============================================================= REGISTER
trail = [("Home", "/"), ("Register a Team", None)]
body = f'''
<section class="page-header">
  <div class="container">
    <div class="breadcrumbs">{breadcrumbs(trail)}</div>
    <h1>Register a Team</h1>
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
        <a class="btn btn-primary" href="{REGISTER_URL}" target="_blank" rel="noopener">Go to Registration &rarr;</a>
      </div>
    </div>
    <div class="prose" style="margin-top: var(--space-5);">
      <h2>Not sure where to start?</h2>
      <p>If you're new to team pickleball, aren't sure which division fits, or want help finding a team, <a href="/contact">contact Jon Graham</a> before you register and we'll point you in the right direction.</p>
    </div>
  </div>
</section>
'''
schema = [breadcrumb_schema("/register", trail)]
page("/register", f"Register a Team | {BRAND}", "Register your team for California Team Pickleball leagues. Registration and scoring are handled through our league management partner.", body, schema)

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
      <p>Head to <a href="/register">Register a Team</a> to sign up directly through our league management partner.</p>
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
      <a class="btn btn-primary" href="/register">Register a Team</a>
      <a class="btn btn-outline" style="border-color: var(--color-ink); color: var(--color-ink);" href="/">Back to Home</a>
    </div>
  </div>
</section>
'''
page("/thank-you", f"Message Sent | {BRAND}", "Thanks for reaching out to California Team Pickleball.", body, [])
# thank-you needs noindex — patched after generation below

# ============================================================= PRIVACY / TERMS (placeholder — see README)
privacy_body = f'''
<section class="page-header">
  <div class="container">
    <h1>Privacy Policy</h1>
    <p class="lede">Last updated: [DATE]</p>
  </div>
</section>
<section class="section">
  <div class="container prose">
    <p><em>This is placeholder legal text pending review. Do not treat as final &mdash; replace with the client's reviewed policy before launch. See README.</em></p>
    <h2>Information we collect</h2>
    <p>When you contact us or register for a league through our website, we may collect your name, phone number, email address, and any information you provide in a message or form.</p>
    <h2>How we use it</h2>
    <p>We use this information to respond to inquiries, communicate about leagues and registration, and manage league operations. We do not sell your information.</p>
    <h2>Third parties</h2>
    <p>Team registration and season scoring are handled by our league management partner (Tenniscores / PickleballScores), which has its own privacy practices. Website form submissions are processed through Netlify.</p>
    <h2>Contact</h2>
    <p>Questions about this policy can be sent to <a href="mailto:jon@desertatpl.com">jon@desertatpl.com</a>.</p>
  </div>
</section>
'''
page("/privacy", f"Privacy Policy | {BRAND}", "Privacy policy for California Team Pickleball.", privacy_body, [{"@context":"https://schema.org","@type":"WebPage","name":"Privacy Policy"}])

terms_body = f'''
<section class="page-header">
  <div class="container">
    <h1>Terms of Service</h1>
    <p class="lede">Last updated: [DATE]</p>
  </div>
</section>
<section class="section">
  <div class="container prose">
    <p><em>This is placeholder legal text pending review. Do not treat as final &mdash; replace with the client's reviewed terms before launch. See README.</em></p>
    <h2>League participation</h2>
    <p>Team and individual registration for California Team Pickleball leagues is handled through our league management partner. Participation is subject to that platform's terms as well as any league-specific rules communicated at registration.</p>
    <h2>Website use</h2>
    <p>This website is provided for informational purposes about California Team Pickleball leagues, divisions, and registration. Content is subject to change without notice.</p>
    <h2>Contact</h2>
    <p>Questions about these terms can be sent to <a href="mailto:jon@desertatpl.com">jon@desertatpl.com</a>.</p>
  </div>
</section>
'''
page("/terms", f"Terms of Service | {BRAND}", "Terms of service for California Team Pickleball.", terms_body, [{"@context":"https://schema.org","@type":"WebPage","name":"Terms of Service"}])

print("All pages generated.")
