#!/usr/bin/env python3
"""
California Team Pickleball — site generator.
Produces all HTML pages from shared header/footer templates.
Re-run after any nav, footer, or schema change to keep every page in sync.
"""
import os, json

DOMAIN = "https://caliteampickleball.com"
BRAND = "California Team Pickleball"
PHONE_DISPLAY = "(951) 858-6070"
PHONE_TEL = "+19518586070"
EMAIL = "jon@desertatpl.com"  # TODO: confirm if a @caliteampickleball.com address will be set up post-rebrand
REGISTER_URL = "https://ctpl.pickleballscores.com"  # TODO: swap for direct registration link once Jon creates one
CSSV = "20260715"
OUT = "/home/claude/ctpl"

NAV_LEAGUES = [
    ("/leagues/fall-day", "Fall Day League"),
    ("/leagues/fall-night", "Fall Night League"),
    ("/leagues/winter-night", "Winter Night League"),
]
NAV_REGIONS = [
    ("/regions/desert", "Desert / Coachella Valley"),
]

def svg_courtlines():
    # Decorative pickleball court-line motif used behind hero content.
    return '''<svg class="hero-courtlines" width="100%" height="100%" viewBox="0 0 1200 600" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <rect x="40" y="40" width="1120" height="520" fill="none" stroke="#F6F3EC" stroke-width="2"/>
  <line x1="600" y1="40" x2="600" y2="560" stroke="#F6F3EC" stroke-width="2"/>
  <line x1="40" y1="220" x2="1160" y2="220" stroke="#F6F3EC" stroke-width="2"/>
  <line x1="40" y1="380" x2="1160" y2="380" stroke="#F6F3EC" stroke-width="2"/>
  <circle cx="600" cy="300" r="3" fill="#F6F3EC"/>
</svg>'''

def social_icon(name, href):
    icons = {
        "facebook": '<path d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"/>',
        "instagram": '<path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/>',
    }
    return f'''<a href="{href}" target="_blank" rel="noopener" aria-label="{name.title()}">
      <svg width="18" height="18" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">{icons[name]}</svg>
      <span>{name.title()}</span>
    </a>'''

def head(path, title, description, schema_blocks):
    canonical = DOMAIN + path
    og_image = f"{DOMAIN}/images/og-default.png"
    schema_json = "\n".join(f'<script type="application/ld+json">{json.dumps(s)}</script>' for s in schema_blocks)
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="index,follow">
<link rel="canonical" href="{canonical}">

<meta name="theme-color" content="#1C4E52">
<link rel="icon" type="image/png" href="/images/favicon.png">
<link rel="apple-touch-icon" href="/images/favicon.png">

<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;700;800&family=Work+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">

<link rel="stylesheet" href="/css/style.css?v={CSSV}">
{schema_json}'''

def header(active_path):
    def cur(p):
        return ' aria-current="page"' if p == active_path else ''
    def in_section(prefix):
        return active_path.startswith(prefix)

    leagues_items = "\n      ".join(
        f'<a href="{href}"{cur(href)}>{label}</a>' for href, label in NAV_LEAGUES
    )
    regions_items = "\n      ".join(
        f'<a href="{href}"{cur(href)}>{label}</a>' for href, label in NAV_REGIONS
    )
    leagues_open = " is-open" if in_section("/leagues/") and active_path not in ("/leagues/",) else ""

    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container">
    <a class="brand" href="/">
      <svg class="brand-mark" width="34" height="34" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <rect x="3" y="3" width="34" height="34" rx="4" fill="#1C4E52"/>
        <line x1="20" y1="6" x2="20" y2="34" stroke="#F6F3EC" stroke-width="2"/>
        <line x1="6" y1="14" x2="34" y2="14" stroke="#F6F3EC" stroke-width="2"/>
        <line x1="6" y1="26" x2="34" y2="26" stroke="#F6F3EC" stroke-width="2"/>
        <circle cx="20" cy="20" r="2.5" fill="#E3A73B"/>
      </svg>
      <span class="brand-full">California Team Pickleball</span>
      <span class="brand-short">CTPL</span>
    </a>
    <nav class="primary-nav" id="primary-nav" aria-label="Primary">
      <div class="nav-item has-dropdown">
        <a href="/leagues/"{cur('/leagues/')}>Leagues</a>
        <div class="nav-dropdown" role="menu">
          {leagues_items}
          <div class="nav-dropdown-divider"></div>
          <a href="/leagues/" class="nav-dropdown-all">View all leagues</a>
        </div>
      </div>
      <div class="nav-item has-dropdown">
        <a href="/regions/"{cur('/regions/')}>Regions</a>
        <div class="nav-dropdown" role="menu">
          {regions_items}
          <div class="nav-dropdown-divider"></div>
          <a href="/regions/" class="nav-dropdown-all">View all regions</a>
        </div>
      </div>
      <a href="/news/"{cur('/news/')}>News</a>
      <a href="/about"{cur('/about')}>About</a>
      <a href="/contact"{cur('/contact')}>Contact</a>
      <a href="/register" class="nav-cta">Register a Team</a>
    </nav>
    <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="primary-nav">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>
  </div>
</header>'''

def footer():
    league_links = "\n            ".join(f'<li><a href="{href}">{label}</a></li>' for href, label in NAV_LEAGUES)
    region_links = "\n            ".join(f'<li><a href="{href}">{label}</a></li>' for href, label in NAV_REGIONS)
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-nap">
      <div>
        <h4>Contact</h4>
        <div class="footer-nap-phone"><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div>
        <address>
          <a href="mailto:{EMAIL}">{EMAIL}</a><br>
          Regional Director: Jon Graham
        </address>
      </div>
      <div>
        <h4>Where We Play</h4>
        <p style="color: rgba(246,243,236,0.75); margin: 0;">Active now in the Desert / Coachella Valley region. Additional California regions launching soon.</p>
      </div>
      <div>
        <h4>Follow</h4>
        <div class="footer-social">
          {social_icon("facebook", "#")}
          {social_icon("instagram", "#")}
        </div>
      </div>
    </div>

    <div class="footer-grid">
      <div>
        <h4>California Team Pickleball</h4>
        <p class="footer-blurb">Organized team-format pickleball leagues, by division and skill level. Built region by region across California, starting in the desert.</p>
      </div>
      <div>
        <h4>Leagues</h4>
        <ul>
          {league_links}
        </ul>
      </div>
      <div>
        <h4>Regions</h4>
        <ul>
          {region_links}
        </ul>
      </div>
      <div>
        <h4>Site</h4>
        <ul>
          <li><a href="/about">About</a></li>
          <li><a href="/news/">News</a></li>
          <li><a href="/contact">Contact</a></li>
          <li><a href="/register">Register a Team</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <span>&copy; 2026 California Team Pickleball. All rights reserved.</span>
      <span><a href="/privacy">Privacy Policy</a> &middot; <a href="/terms">Terms of Service</a></span>
    </div>
  </div>
  <div class="footer-credit">Created by <a href="https://baseline-seo.com" target="_blank" rel="noopener">Baseline SEO</a></div>
</footer>'''

def breadcrumbs(trail):
    # trail: list of (label, path) tuples, path=None for current page
    parts = []
    for label, path in trail:
        if path:
            parts.append(f'<a href="{path}">{label}</a>')
        else:
            parts.append(f'<span aria-current="page">{label}</span>')
    return " / ".join(parts)

def breadcrumb_schema(path, trail):
    items = []
    for i, (label, p) in enumerate(trail, start=1):
        item = {"@type": "ListItem", "position": i, "name": label}
        item["item"] = DOMAIN + (p if p else path)
        items.append(item)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

def page(path, title, description, body, schema_blocks=None, nav_active=None):
    schema_blocks = schema_blocks or []
    active = nav_active if nav_active is not None else path
    html = f'''<!doctype html>
<html lang="en">
<head>
{head(path, title, description, schema_blocks)}
</head>
<body>
{header(active)}
<main id="main">
{body}
</main>
{footer()}
<script src="/js/main.js?v={CSSV}" defer></script>
</body>
</html>
'''
    fs_path = os.path.join(OUT, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(OUT, path.strip("/") + ".html")
    os.makedirs(os.path.dirname(fs_path), exist_ok=True)
    with open(fs_path, "w") as f:
        f.write(html)
    print("wrote", fs_path)

print("build.py loaded — see build_pages.py for page content + execution")
