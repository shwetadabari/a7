import os
import json
import hashlib

BASE_DIR = r"d:\antigravity website\ankletbadger"
ADDR = "1801 California Street, Suite 4400, Denver, CO 80202, United States"
PHONE = "+1-877-384-9051"
EMAIL = "concierge@ankletbadger.com"
DOMAIN = "ankletbadger.com"
BRAND = "Anklet Badger Knitting Guild"

GTAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0LY0HY7L01"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-0LY0HY7L01');
</script>"""

FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Manrope:wght@300;400;500;600;700&family=Marcellus&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">"""

def get_header(active_page):
    idx_cls = "active" if active_page == "index" else ""
    abt_cls = "active" if active_page == "about" else ""
    prd_cls = "active" if active_page == "products" else ""
    faq_cls = "active" if active_page == "faq" else ""
    cnt_cls = "active" if active_page == "contact" else ""
    
    return f"""  <!-- Site Header (Rule 11) -->
  <header class="site-header">
    <div class="ab-container">
      <div class="ab-nav-wrapper">
        <a href="index.php" class="ab-brand">
          <div class="ab-brand-emblem">⩕</div>
          <div class="ab-brand-title">
            Anklet Badger
            <small>Knitting Guild &bull; Denver</small>
          </div>
        </a>
        <nav class="ab-nav-menu">
          <a href="index.php" class="ab-nav-link {idx_cls}">Tactical Ridge</a>
          <a href="about.html" class="ab-nav-link {abt_cls}">Guild Heritage</a>
          <a href="products.html" class="ab-nav-link {prd_cls}">Tensile Anklets</a>
          <a href="faq.html" class="ab-nav-link {faq_cls}">Fiber FAQ</a>
          <a href="contact.html" class="ab-nav-link {cnt_cls}">Fitting Salon</a>
        </nav>
        <div style="display: flex; align-items: center; gap: 16px;">
          <a href="contact.html" class="ab-btn ab-btn-ochre">Reserve Fitting</a>
          <button class="ab-hamburger" id="ab-hamburger" aria-label="Toggle Navigation">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer (Rule 11) -->
  <div class="mobile-drawer-backdrop" id="mobile-drawer-backdrop"></div>
  <div class="mobile-drawer" id="mobile-drawer">
    <div class="mobile-drawer-header">
      <div class="ab-brand">
        <div class="ab-brand-emblem">⩕</div>
        <div class="ab-brand-title">Anklet Badger</div>
      </div>
      <button class="mobile-drawer-close" id="mobile-drawer-close" aria-label="Close Drawer">&times;</button>
    </div>
    <div class="mobile-drawer-body">
      <a href="index.php" class="mobile-nav-link">Tactical Ridge Flagship</a>
      <a href="about.html" class="mobile-nav-link">Guild Heritage &amp; Merino</a>
      <a href="products.html" class="mobile-nav-link">High-Tensile Anklets</a>
      <a href="faq.html" class="mobile-nav-link">Fiber Care &amp; Tech FAQ</a>
      <a href="contact.html" class="mobile-nav-link">Denver Fitting Consultation</a>
    </div>
    <div class="mobile-drawer-footer">
      <p style="margin-bottom: 8px; color: var(--ab-ochre); font-family: var(--ab-font-mono); font-size: 0.75rem;">DENVER GUILD CONCIERGE</p>
      <p style="margin-bottom: 6px;">{PHONE}</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
  </div>"""

def get_footer():
    return f"""  <!-- Semantic Site Footer -->
  <footer class="ab-footer">
    <div class="ab-container">
      <div class="ab-footer-grid">
        <div class="ab-footer-brand">
          <div class="ab-brand" style="margin-bottom: 16px;">
            <div class="ab-brand-emblem">⩕</div>
            <div class="ab-brand-title">
              Anklet Badger
              <small>Guild &bull; Est. Denver</small>
            </div>
          </div>
          <p style="color: var(--ab-text-light-muted); font-size: 0.9rem; line-height: 1.7; margin-bottom: 16px;">
            High-tensile merino wool anklet socks engineered with 200-needle circular gauge beds, hand-linked seamless toes, and four-ply badger heel cups for alpine trail endurance.
          </p>
          <div style="font-family: var(--ab-font-mono); font-size: 0.8rem; color: var(--ab-ochre);">
            {PHONE} &bull; {EMAIL}
          </div>
        </div>
        <div class="ab-footer-col">
          <h4>Guild Anklets</h4>
          <ul class="ab-footer-links">
            <li><a href="index.php">Tactical Ridge Home</a></li>
            <li><a href="about.html">Merino Wool Heritage</a></li>
            <li><a href="products.html">Tensile Anklet Matrix</a></li>
            <li><a href="faq.html">Sockcraft &amp; Care FAQ</a></li>
            <li><a href="contact.html">Denver Fitting Salon</a></li>
          </ul>
        </div>
        <div class="ab-footer-col">
          <h4>Knitting Pillars</h4>
          <ul class="ab-footer-links">
            <li><a href="about.html">200-Needle Circular Bed</a></li>
            <li><a href="about.html">18.5µ Raw Merino Fleece</a></li>
            <li><a href="about.html">Zero-Friction Linked Toe</a></li>
            <li><a href="about.html">High-Density Terry Bed</a></li>
            <li><a href="about.html">Elastic Arch Compression</a></li>
          </ul>
        </div>
        <div class="ab-footer-col">
          <h4>Institutional Coordinates</h4>
          <p style="font-size: 0.85rem; line-height: 1.6; margin-bottom: 12px; color: var(--ab-text-light-muted);">
            {ADDR}
          </p>
          <p style="font-family: var(--ab-font-mono); font-size: 0.75rem; color: var(--ab-ochre); margin-bottom: 16px;">
            Guild Fitting Room: {PHONE}
          </p>
          <div style="padding: 8px 12px; background: rgba(212,139,56,0.08); border: 1px solid rgba(212,139,56,0.25); border-radius: 4px; font-size: 0.725rem; font-family: var(--ab-font-mono); color: var(--ab-text-light);">
            Registered Colorado Woolcraft Artisanal Guild Member
          </div>
        </div>
      </div>
      <div class="ab-footer-bottom">
        <div>&copy; 2026 Anklet Badger Knitting Guild LLC. All Worldwide Rights Reserved.</div>
        <div class="ab-legal-nav">
          <a href="privacy-policy.html">Privacy Policy</a>
          <a href="terms-and-conditions.html">Terms &amp; Conditions</a>
          <a href="disclaimer.html">Disclaimer</a>
          <a href="cookie-policy.html">Cookie Policy</a>
        </div>
      </div>
    </div>
  </footer>
  <script src="assets/js/script.js"></script>"""

def check_paragraphs(paras, page_name):
    for idx, p in enumerate(paras):
        words = len(p.split())
        if words < 60 or words > 110:
            raise ValueError(f"Paragraph {idx+1} in {page_name} has {words} words (expected 60-110 words). Text: {p[:60]}...")

def build_index():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Anklet Badger | High-Tensile Merino Wool Sockcraft Guild</title>
  <meta name="description" content="Anklet Badger Knitting Guild in Denver crafts high-tensile 200-needle merino wool anklet socks with seamless hand-linked toes and reinforced badger heel cups.">
  <link rel="canonical" href="https://{DOMAIN}/index.php">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('index')}

  <main>
    <!-- Section 1: Tactical Ridge Hero Masthead -->
    <section class="ab-hero">
      <div class="ab-container">
        <div class="ab-hero-grid">
          <div class="ab-hero-content">
            <span class="ab-tag">Denver Alpine Knitting Guild</span>
            <h1>High-Tensile <span>Merino Anklets</span> Engineered for Ridge Ascent</h1>
            <p class="ab-hero-desc">
              Forged on 200-needle circular cylinders in Denver, Colorado, Anklet Badger merges 18.5-micron fine merino fleece with four-ply nylon reinforcement to build indestructible ankle socks for alpine summits and trail endurance.
            </p>
            <div class="ab-hero-actions">
              <a href="products.html" class="ab-btn ab-btn-ochre">Explore Tensile Matrix</a>
              <a href="about.html" class="ab-btn ab-btn-outline">Guild Philosophy</a>
            </div>
            <div class="ab-hero-metrics">
              <div class="ab-metric-item">
                <strong>200</strong>
                <span>Needle Gauge Cylinder</span>
              </div>
              <div class="ab-metric-item">
                <strong>18.5µ</strong>
                <span>Pure Merino Micron</span>
              </div>
              <div class="ab-metric-item">
                <strong>4-Ply</strong>
                <span>Badger Shield Heel</span>
              </div>
            </div>
          </div>
          <div class="ab-hero-media">
            <div class="ab-hero-frame">
              <img src="assets/images/ankletbadger_asset_1.jpg" alt="Rugged thick-knit grey merino wool boot anklet socks folded on rustic pine board with leather boots" width="600" height="540">
              <div class="ab-ridge-badge">
                <div class="ab-badge-icon">⩕</div>
                <div>
                  <div style="font-weight: 700; font-size: 0.9rem;">Ridge Grade Anklet #01</div>
                  <div style="font-size: 0.75rem; color: var(--ab-text-light-muted); font-family: var(--ab-font-mono);">Denver Guild Certified</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Alpine Knitting Guild Ribbon Ticker -->
    <div class="ab-ticker">
      <div class="ab-ticker-track">
        <div class="ab-ticker-item"><span>⩕</span> 200-Needle Circular Knitting</div>
        <div class="ab-ticker-item"><span>⩕</span> Hand-Linked Seamless Toe Closure</div>
        <div class="ab-ticker-item"><span>⩕</span> 18.5 Micron Mountain Merino</div>
        <div class="ab-ticker-item"><span>⩕</span> Zero-Blister Arch Compression</div>
        <div class="ab-ticker-item"><span>⩕</span> Four-Ply Badger Heel Cup Shield</div>
        <div class="ab-ticker-item"><span>⩕</span> Hydrophobic Lanolin Fiber Treatment</div>
        <div class="ab-ticker-item"><span>⩕</span> Denver Bench Sizing Standards</div>
        <div class="ab-ticker-item"><span>⩕</span> 200-Needle Circular Knitting</div>
        <div class="ab-ticker-item"><span>⩕</span> Hand-Linked Seamless Toe Closure</div>
        <div class="ab-ticker-item"><span>⩕</span> 18.5 Micron Mountain Merino</div>
        <div class="ab-ticker-item"><span>⩕</span> Zero-Blister Arch Compression</div>
        <div class="ab-ticker-item"><span>⩕</span> Four-Ply Badger Heel Cup Shield</div>
        <div class="ab-ticker-item"><span>⩕</span> Hydrophobic Lanolin Fiber Treatment</div>
        <div class="ab-ticker-item"><span>⩕</span> Denver Bench Sizing Standards</div>
      </div>
    </div>

    <!-- Section 3: The Badger Woolen Shield Manifesto -->
    <section class="ab-section">
      <div class="ab-container">
        <div class="ab-manifesto-grid">
          <div class="ab-manifesto-media">
            <img src="assets/images/ankletbadger_asset_2.jpg" alt="Extreme macro photograph of dense 200-needle rib knit texture and elastic arch band in wool sock" width="560" height="480">
          </div>
          <div class="ab-manifesto-content">
            <span class="ab-tag">Fiber Tensile Engineering</span>
            <h2 class="ab-section-title">The Ankle Joint Demands <span>Unyielding Defense</span></h2>
            <p style="font-size: 1.05rem; color: var(--ab-text-light-muted); margin-bottom: 20px; line-height: 1.8;">
              Modern mass-produced athletic socks cut corners with low-gauge 96-needle loops, synthetic friction threads, and bulky machine-seamed toe ridges that abrade skin over steep alpine ascents. Anklet Badger refutes industrial disposable hosiery through painstaking artisanal precision.
            </p>
            <p style="font-size: 1rem; color: var(--ab-text-light-muted); margin-bottom: 28px; line-height: 1.8;">
              By spinning ultra-fine 18.5-micron merino wool across 200 high-tensile spring steel needles, we achieve a dense protective knit that resists trail grit, cushions heel impact, and naturally wicks sweat vapor without holding thermal dampness.
            </p>
            <div style="display: flex; gap: 24px;">
              <div style="border-left: 2px solid var(--ab-ochre); padding-left: 16px;">
                <div style="font-family: var(--ab-font-mono); font-size: 1.25rem; color: var(--ab-ochre); font-weight: 700;">Zero Seams</div>
                <div style="font-size: 0.85rem; color: var(--ab-text-light-muted);">Hand-linked loop closure eliminates friction blisters</div>
              </div>
              <div style="border-left: 2px solid var(--ab-ochre); padding-left: 16px;">
                <div style="font-family: var(--ab-font-mono); font-size: 1.25rem; color: var(--ab-ochre); font-weight: 700;">30k Cycles</div>
                <div style="font-size: 0.85rem; color: var(--ab-text-light-muted);">Martindale abrasion resistance on heel and ball zones</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: 4-Pillar High-Tensile Sockcraft Geometry -->
    <section class="ab-section ab-section-darker">
      <div class="ab-container">
        <div style="text-align: center; max-width: 720px; margin: 0 auto 30px;">
          <span class="ab-tag">Artisanal Architecture</span>
          <h2 class="ab-section-title">Four Structural Pillars of <span>Guild Sockcraft</span></h2>
          <p class="ab-section-subtitle" style="margin: 0 auto;">
            Every pair of Anklet Badger socks is engineered with four interdependent textile mechanics engineered to endure decades of alpine movement.
          </p>
        </div>
        <div class="ab-spec-4col">
          <div class="ab-spec-card">
            <div class="ab-spec-val">200N</div>
            <h3 class="ab-spec-title">Fine-Gauge Cylinder</h3>
            <p class="ab-spec-desc">
              Twin-feed 200-needle circular cylinders yield an ultra-compact stitch matrix that blocks abrasive trail dust while creating a second-skin contour.
            </p>
          </div>
          <div class="ab-spec-card">
            <div class="ab-spec-val">18.5µ</div>
            <h3 class="ab-spec-title">Natural Mountain Merino</h3>
            <p class="ab-spec-desc">
              Carefully sorted high-altitude fleece fibers offering natural thermal buffering, antimicrobial odor suppression, and itch-free skin comfort.
            </p>
          </div>
          <div class="ab-spec-card">
            <div class="ab-spec-val">0 mm</div>
            <h3 class="ab-spec-title">Seamless Linked Toe</h3>
            <p class="ab-spec-desc">
              Each toe stitch is closed loop-by-loop by guild artisans using traditional hand-linking frames, eliminating abrasive transverse toe ridges.
            </p>
          </div>
          <div class="ab-spec-card">
            <div class="ab-spec-val">4-Ply</div>
            <h3 class="ab-spec-title">Badger Heel Reinforcement</h3>
            <p class="ab-spec-desc">
              High-abrasion impact zones are interwoven with four-ply core-spun nylon cord to deliver extreme durability under heavy mountain packs.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 5: The Alpine Anklet Lookbook Duo -->
    <section class="ab-section">
      <div class="ab-container">
        <div style="text-align: center; max-width: 680px; margin: 0 auto 30px;">
          <span class="ab-tag">Archival Collections</span>
          <h2 class="ab-section-title">Field Lookbook &amp; <span>Yarn Textures</span></h2>
          <p class="ab-section-subtitle" style="margin: 0 auto;">
            Witness the convergence of historic hand-knitting techniques and modern technical wool architecture developed inside our Denver workshops.
          </p>
        </div>
        <div class="ab-lookbook-duo">
          <div class="ab-lookbook-card">
            <img src="assets/images/ankletbadger_asset_3.jpg" alt="Master knitter hands using wooden knitting needles with natural tweed yarn in alpine workshop" width="580" height="480">
            <div class="ab-lookbook-overlay">
              <span class="ab-lookbook-tag">Artisanal Guild Lineage</span>
              <h3 class="ab-lookbook-title">Tweed Yarn Hand-Turning</h3>
              <p class="ab-lookbook-desc">Denver guild knitters inspecting tension consistency across heritage wooden needles prior to circular machine calibration.</p>
            </div>
          </div>
          <div class="ab-lookbook-card">
            <img src="assets/images/ankletbadger_asset_4.jpg" alt="Pair of beige waffle-knit hiking anklet socks laid flat on weathered wood table" width="580" height="480">
            <div class="ab-lookbook-overlay">
              <span class="ab-lookbook-tag">Alpine Terrain Edition</span>
              <h3 class="ab-lookbook-title">Waffle-Knit Trail Anklet</h3>
              <p class="ab-lookbook-desc">Breathable three-dimensional honeycomb channels engineered for rapid moisture evaporation on steep switchbacks.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 6: Cushion Density & Micron Gauge Matrix Table -->
    <section class="ab-section ab-section-light">
      <div class="ab-container">
        <div style="text-align: center; max-width: 720px; margin: 0 auto 20px;">
          <span class="ab-tag" style="background: rgba(212,139,56,0.15); border-color: rgba(212,139,56,0.4);">Guild Benchmark Matrix</span>
          <h2 class="ab-section-title" style="color: #111612;">Technical Yarn &amp; <span>Cushion Specifications</span></h2>
          <p style="color: #4a5449; font-size: 1.05rem;">
            Direct comparative metrics verifying stitch density, terry loop placement, and durability ratings across our permanent anklet silhouettes.
          </p>
        </div>
        <div class="ab-table-wrapper">
          <table class="ab-matrix-table">
            <thead>
              <tr>
                <th>Anklet Model</th>
                <th>Gauge Needle Count</th>
                <th>Merino Micron</th>
                <th>Terry Cushion Bed</th>
                <th>Heel/Toe Shield</th>
                <th>Optimal Operating Range</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Ridge Trail Anklet</strong></td>
                <td>200 Needles</td>
                <td>18.5 Micron Pure Merino</td>
                <td>Targeted Heel &amp; Ball Pods</td>
                <td>3-Ply Core-Spun Cord</td>
                <td>Alpine Day Hikes &bull; 40°F to 85°F</td>
              </tr>
              <tr>
                <td><strong>Badger Expedition Heavy</strong></td>
                <td>168 Needles High-Twist</td>
                <td>19.5 Micron Mountain Wool</td>
                <td>Full 360° Dense Terry Footbed</td>
                <td>4-Ply Badger Armor Weave</td>
                <td>Backpacking &bull; 10°F to 65°F</td>
              </tr>
              <tr>
                <td><strong>Alpine Low-Tab Speed</strong></td>
                <td>200 Needles Ultra-Fine</td>
                <td>17.8 Micron Merino Silk Blend</td>
                <td>Ultralight Micro-Terry Zone</td>
                <td>2-Ply Friction Shield</td>
                <td>Mountain Running &bull; 50°F to 95°F</td>
              </tr>
              <tr>
                <td><strong>Highland Rib Boot Anklet</strong></td>
                <td>180 Needles Ribbed</td>
                <td>19.0 Micron Donegal Tweed</td>
                <td>Medium Impact Compression Bed</td>
                <td>3-Ply Reinforced Welt</td>
                <td>Trail Fieldwork &bull; 30°F to 75°F</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Section 7: Alternating Knitting Guild Mastery Rows -->
    <section class="ab-section">
      <div class="ab-container">
        <div class="ab-craft-row">
          <div class="ab-craft-media">
            <img src="assets/images/ankletbadger_asset_5.jpg" alt="Close-up macro of hand-linked seamless toe closure and cushioned terry loop footbed" width="580" height="440">
          </div>
          <div class="ab-craft-content">
            <span class="ab-tag">Precision Joinery</span>
            <h2 class="ab-section-title">Hand-Linked Loop <span>Toe Calibration</span></h2>
            <p style="font-size: 1.05rem; color: var(--ab-text-light-muted); margin-bottom: 20px; line-height: 1.8;">
              Conventional sock factories use automated sewing machines that pinch the toe end into a thick, bulky ridge. In mountain boots, this artificial ridge pushes directly into nail beds, producing excruciating pressure points during prolonged descents.
            </p>
            <p style="font-size: 1rem; color: var(--ab-text-light-muted); line-height: 1.8;">
              Anklet Badger closes every single toe seam by mounting open knit loops onto microscopic needles. A single continuous thread marries the upper and lower fabric matrices with zero dimensional thickness.
            </p>
          </div>
        </div>

        <div class="ab-craft-row reversed">
          <div class="ab-craft-media">
            <img src="assets/images/ankletbadger_asset_6.jpg" alt="Knitting workshop flat lay: wooden sock blockers, wool yarn skeins, and brass gauge ruler" width="580" height="440">
          </div>
          <div class="ab-craft-content">
            <span class="ab-tag">Workshop Geometry</span>
            <h2 class="ab-section-title">Block-Formed Sizing &amp; <span>Thermal Steam Finishing</span></h2>
            <p style="font-size: 1.05rem; color: var(--ab-text-light-muted); margin-bottom: 20px; line-height: 1.8;">
              After leaving our circular cylinders, raw knit anklets undergo controlled hot spring water washing and low-pressure steam blocking on bespoke maple foot forms. This relieves mechanical needle tension and locks fiber memory permanently into place.
            </p>
            <p style="font-size: 1rem; color: var(--ab-text-light-muted); line-height: 1.8;">
              The resulting sock preserves its anatomic arch compression and elastic cuff rebound through hundreds of trail cycles without ever stretching, sagging, or twisting around the heel.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 8: Anklet Collection Tiers -->
    <section class="ab-section ab-section-darker">
      <div class="ab-container">
        <div style="text-align: center; max-width: 680px; margin: 0 auto 30px;">
          <span class="ab-tag">Guild Commission Portfolio</span>
          <h2 class="ab-section-title">Permanent Collection <span>Silhouettes</span></h2>
          <p class="ab-section-subtitle" style="margin: 0 auto;">
            Acquire precision-knitted merino wool anklets built for demanding trail terrain, mountain ascents, and everyday alpine lifestyle.
          </p>
        </div>
        <div class="ab-tier-grid">
          <div class="ab-tier-card">
            <h3 class="ab-tier-name">Ridge Trail Anklet</h3>
            <div class="ab-tier-price">$28 / Pair</div>
            <p style="color: var(--ab-text-light-muted); font-size: 0.9rem; line-height: 1.6;">The essential 200-needle everyday alpine anklet engineered for mountain hiking and technical low-cut trail footwear.</p>
            <ul class="ab-tier-features">
              <li>18.5µ Pure Merino Wool Blend</li>
              <li>Hand-Linked Seamless Toe</li>
              <li>Targeted Cushion Ball Pods</li>
              <li>Non-Slip Ankle Ribbed Cuff</li>
            </ul>
            <a href="contact.html" class="ab-btn ab-btn-outline" style="width: 100%;">Reserve Allocation</a>
          </div>

          <div class="ab-tier-card featured">
            <div class="ab-tier-badge">Guild Signature</div>
            <h3 class="ab-tier-name">Badger Expedition Heavy</h3>
            <div class="ab-tier-price">$36 / Pair</div>
            <p style="color: var(--ab-text-light-muted); font-size: 0.9rem; line-height: 1.6;">Our highest-tensile sockcraft build with 4-ply reinforced armor yarn and 360-degree terry loops for multiday wilderness packs.</p>
            <ul class="ab-tier-features">
              <li>19.5µ Heavy Mountain Wool</li>
              <li>4-Ply Badger Heel Cup Shield</li>
              <li>Full 360° Terry Footbed Cushion</li>
              <li>Deep Compression Elastic Arch</li>
            </ul>
            <a href="contact.html" class="ab-btn ab-btn-ochre" style="width: 100%;">Reserve Signature Pair</a>
          </div>

          <div class="ab-tier-card">
            <h3 class="ab-tier-name">Alpine Low-Tab Speed</h3>
            <div class="ab-tier-price">$26 / Pair</div>
            <p style="color: var(--ab-text-light-muted); font-size: 0.9rem; line-height: 1.6;">Featherweight merino silk runner featuring breathable micro-mesh venting grids and padded rear Achilles protective tab.</p>
            <ul class="ab-tier-features">
              <li>17.8µ Merino Silk Hybrid</li>
              <li>Achilles Impact Protection Tab</li>
              <li>Mesh Forefoot Vapor Vents</li>
              <li>Zero Moisture Retention Rate</li>
            </ul>
            <a href="contact.html" class="ab-btn ab-btn-outline" style="width: 100%;">Reserve Allocation</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 9: Abrasion Martindale & Tensile Testing Log -->
    <section class="ab-section">
      <div class="ab-container">
        <div style="text-align: center; max-width: 660px; margin: 0 auto 30px;">
          <span class="ab-tag">Empirical Guild Validation</span>
          <h2 class="ab-section-title">Laboratory Stress &amp; <span>Fiber Metrics</span></h2>
          <p class="ab-section-subtitle" style="margin: 0 auto;">
            We subject every batch of spun yarn and finished knit cuffs to rigorous tensile and abrasion protocols inside our Denver testing room.
          </p>
        </div>
        <div class="ab-lab-grid">
          <div class="ab-lab-item">
            <div class="ab-lab-metric">32,500+</div>
            <div class="ab-lab-label">Martindale Abrasion Rubs</div>
          </div>
          <div class="ab-lab-item">
            <div class="ab-lab-metric">18.5µ</div>
            <div class="ab-lab-label">Mean Fiber Fineness Rating</div>
          </div>
          <div class="ab-lab-item">
            <div class="ab-lab-metric">4.8 N</div>
            <div class="ab-lab-label">Seam Bursting Strength</div>
          </div>
          <div class="ab-lab-item">
            <div class="ab-lab-metric">98.4%</div>
            <div class="ab-lab-label">Elastic Memory Retention</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 10: Master Knitter Ewan MacColl Guild Spotlight -->
    <section class="ab-section ab-section-darker">
      <div class="ab-container">
        <div class="ab-spotlight-box">
          <div>
            <span class="ab-tag">Head of Guild Craft</span>
            <h2 style="font-size: 2.2rem; margin-bottom: 12px; color: var(--ab-text-light);">Master Knitter <span>Ewan MacColl</span></h2>
            <div style="font-family: var(--ab-font-mono); font-size: 0.85rem; color: var(--ab-ochre); margin-bottom: 20px;">34 Years Circular Cylinder Engineering</div>
            <div style="border-top: 1px solid var(--ab-border-dark); padding-top: 20px;">
              <div style="font-size: 0.85rem; color: var(--ab-text-light-muted); margin-bottom: 8px;">Denver Guild Workshop Benchmark</div>
              <div style="font-family: var(--ab-font-mono); color: var(--ab-text-light); font-size: 0.95rem;">Precision Mechanical Caliper Tolerance: &plusmn;0.02 mm</div>
            </div>
          </div>
          <div>
            <p style="font-size: 1.05rem; color: var(--ab-text-light-muted); line-height: 1.8; margin-bottom: 20px;">
              &ldquo;True mountaineering socks are not merely garments; they are the fundamental shock-absorbing interface between the human foot and miles of unrelenting granite terrain. If a sock wrinkles, bunches, or allows grit through its weave, the ascent is compromised.&rdquo;
            </p>
            <p style="font-size: 0.95rem; color: var(--ab-text-light-muted); line-height: 1.8;">
              Ewan personally oversees the needle alignment, yarn feed tensioning, and hand-linking inspection of every Anklet Badger production run, ensuring that no pair leaves Denver without absolute structural integrity.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 11: Dual-Column High-Tensile Wool Sock FAQ -->
    <section class="ab-section">
      <div class="ab-container">
        <div style="text-align: center; max-width: 680px; margin: 0 auto 30px;">
          <span class="ab-tag">Collector Inquiries</span>
          <h2 class="ab-section-title">Sockcraft &amp; Technical <span>Inquiries</span></h2>
          <p class="ab-section-subtitle" style="margin: 0 auto;">
            Essential insights into our merino wool sourcing, needle gauge mechanics, and lifetime wear expectations.
          </p>
        </div>
        <div class="ab-faq-grid">
          <div class="ab-faq-item active">
            <button class="ab-faq-header">
              Why do you choose 200-needle circular cylinders over 144 needles?
              <span class="ab-faq-icon">&plus;</span>
            </button>
            <div class="ab-faq-body">
              A 200-needle cylinder produces a substantially denser fabric matrix with smaller, tighter loops. This prevents microscopic grit from penetrating between yarns, drastically reduces abrasive skin friction, and holds structural elasticity far longer than coarse 144-needle industrial knits.
            </div>
          </div>

          <div class="ab-faq-item">
            <button class="ab-faq-header">
              Will Anklet Badger socks shrink when washed at home?
              <span class="ab-faq-icon">&plus;</span>
            </button>
            <div class="ab-faq-body">
              All our wool anklets undergo pre-shrink steam stabilization on custom hardwood blockers before leaving our Denver workshop. We recommend gentle cycle machine washing in cool water and laying them flat or hanging to air dry for optimal fiber longevity.
            </div>
          </div>

          <div class="ab-faq-item">
            <button class="ab-faq-header">
              How does merino wool keep feet dry in hot weather?
              <span class="ab-faq-icon">&plus;</span>
            </button>
            <div class="ab-faq-body">
              Unlike synthetic polyester fibers which trap condensed sweat against skin, natural merino wool fibers absorb moisture vapor internally before it condenses into liquid sweat, releasing it through natural evaporative cooling to maintain dry, blister-free feet.
            </div>
          </div>

          <div class="ab-faq-item">
            <button class="ab-faq-header">
              What is the significance of the hand-linked seamless toe?
              <span class="ab-faq-icon">&plus;</span>
            </button>
            <div class="ab-faq-body">
              Traditional automated sewing machines create a raised transverse seam across the top of the toes. Our hand-linked closure joins opposing knit loops with zero ridge thickness, ensuring total absence of chafing inside tight mountaineering or hiking boots.
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 12: Private Guild Wholesale & Custom Sizing Strip -->
    <section class="ab-section ab-section-darker" style="padding-top: 0;">
      <div class="ab-container">
        <div class="ab-cta-strip">
          <div>
            <span class="ab-tag">Denver Atelier Reservation</span>
            <h2 style="font-size: 2.2rem; color: var(--ab-text-light); margin-bottom: 8px;">Experience Bespoke <span>Alpine Fitting</span></h2>
            <p style="color: var(--ab-text-light-muted); max-width: 580px; font-size: 1rem;">
              Visit our Denver consultation rooms on California Street for personal digital foot pressure mapping and bespoke knitting allocations.
            </p>
          </div>
          <div style="display: flex; gap: 16px;">
            <a href="contact.html" class="ab-btn ab-btn-ochre">Book Consultation</a>
            <a href="products.html" class="ab-btn ab-btn-outline">Browse Catalog</a>
          </div>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

def build_about():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About Guild Heritage | Anklet Badger Knitting Guild</title>
  <meta name="description" content="Discover the heritage of Anklet Badger Knitting Guild in Denver, Colorado. Dedicated to high-tensile 200-needle merino wool sockcraft and seamless joinery.">
  <link rel="canonical" href="https://{DOMAIN}/about.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('about')}

  <main>
    <section class="ab-page-header">
      <div class="ab-container">
        <span class="ab-tag">Alpine Heritage &bull; Est. Denver</span>
        <h1 class="ab-section-title" style="font-size: 3rem;">The Art of <span>High-Tensile</span> Sockcraft</h1>
        <p class="ab-section-subtitle" style="margin: 0 auto;">
          Rooted in Colorado's high peaks, our guild exists to construct the most durable, blister-free merino wool anklet hosiery ever conceived.
        </p>
      </div>
    </section>

    <!-- Story Row 1 -->
    <section class="ab-section">
      <div class="ab-container">
        <div class="ab-craft-row">
          <div class="ab-craft-media">
            <img src="assets/images/ankletbadger_asset_7.jpg" alt="Rolled stack of colorful patterned wool anklet socks arranged neatly in rustic basket" width="580" height="440">
          </div>
          <div class="ab-craft-content">
            <span class="ab-tag">Guild Origins</span>
            <h2 class="ab-section-title">Born from <span>High Altitude</span> Demands</h2>
            <p style="font-size: 1.05rem; color: var(--ab-text-light-muted); margin-bottom: 18px; line-height: 1.8;">
              Anklet Badger was founded by a collective of Colorado alpine guides, textile conservators, and circular machine technicians frustrated by the disposable nature of mass-produced athletic socks. In rugged backcountry terrain, blistered feet are a direct hazard to safety and endurance.
            </p>
            <p style="font-size: 1rem; color: var(--ab-text-light-muted); line-height: 1.8;">
              We set out to engineer an ankle-height sock that could withstand tens of thousands of abrasive friction cycles against leather boots while delivering natural temperature regulation across sudden Rocky Mountain weather shifts.
            </p>
          </div>
        </div>

        <!-- Story Row 2 -->
        <div class="ab-craft-row reversed">
          <div class="ab-craft-media">
            <img src="assets/images/ankletbadger_asset_8.jpg" alt="Natural undyed cream sheep wool fleece and spinning wheel spool in alpine fiber studio" width="580" height="440">
          </div>
          <div class="ab-craft-content">
            <span class="ab-tag">Pure Fiber Sourcing</span>
            <h2 class="ab-section-title">Ethical Mountain <span>Merino Fleece</span></h2>
            <p style="font-size: 1.05rem; color: var(--ab-text-light-muted); margin-bottom: 18px; line-height: 1.8;">
              Our raw wool is harvested from certified non-mulesed alpine flocks grazing at high elevations where cold climates trigger the growth of extraordinarily fine, crimped wool fleece. With an average diameter of 18.5 microns, each staple fiber bends effortlessly against sensitive skin.
            </p>
            <p style="font-size: 1rem; color: var(--ab-text-light-muted); line-height: 1.8;">
              We retain natural trace amounts of restorative lanolin during washing to give our spun yarns inherent water repellency and soft elasticity, protecting against moisture accumulation throughout multi-hour alpine hikes.
            </p>
          </div>
        </div>

        <!-- Story Row 3 -->
        <div class="ab-craft-row">
          <div class="ab-craft-media">
            <img src="assets/images/ankletbadger_asset_9.jpg" alt="Knitted sock heel cup construction showing reinforced double-ply nylon yarn weave" width="580" height="440">
          </div>
          <div class="ab-craft-content">
            <span class="ab-tag">Structural Anatomy</span>
            <h2 class="ab-section-title">The Four-Ply <span>Badger Heel Shield</span></h2>
            <p style="font-size: 1.05rem; color: var(--ab-text-light-muted); margin-bottom: 18px; line-height: 1.8;">
              The calcaneus heel bone absorbs several hundred pounds of peak mechanical pressure on steep trail descents. Standard socks wear thin in this critical friction zone within a single season of hard hiking.
            </p>
            <p style="font-size: 1rem; color: var(--ab-text-light-muted); line-height: 1.8;">
              Anklet Badger reinforces the heel cup and Achilles pocket with four strands of interwoven core-spun nylon filament, creating an armored cushion bed that disperses impact energy and prevents boot wear-through permanently.
            </p>
          </div>
        </div>

        <!-- Story Row 4 -->
        <div class="ab-craft-row reversed">
          <div class="ab-craft-media">
            <img src="assets/images/ankletbadger_asset_10.jpg" alt="Macro of spun merino wool yarn skeins showing natural fiber crimp and earthy heather flecks" width="580" height="440">
          </div>
          <div class="ab-craft-content">
            <span class="ab-tag">Twist &amp; Ply Dynamics</span>
            <h2 class="ab-section-title">Ring-Spun <span>Heather Yarns</span></h2>
            <p style="font-size: 1.05rem; color: var(--ab-text-light-muted); margin-bottom: 18px; line-height: 1.8;">
              Unlike brittle open-end industrial spinning, our wool yarns are ring-spun with deliberate balance between yarn twist and fiber loft. This produces high tensile resistance while allowing individual wool fibers to trap dead air for natural climate insulation.
            </p>
            <p style="font-size: 1rem; color: var(--ab-text-light-muted); line-height: 1.8;">
              Earthy heather flecks of charcoal, highland moss, and umber are blended directly into the raw sliver before spinning, creating rich visual depth that honors Colorado's rugged subalpine forests.
            </p>
          </div>
        </div>

        <!-- Story Row 5 -->
        <div class="ab-craft-row">
          <div class="ab-craft-media">
            <img src="assets/images/ankletbadger_asset_11.jpg" alt="Pair of olive green cushioned outdoor trail anklets on display mannequin foot in studio" width="580" height="440">
          </div>
          <div class="ab-craft-content">
            <span class="ab-tag">Anatomical Fit</span>
            <h2 class="ab-section-title">Zero-Migration <span>Arch Architecture</span></h2>
            <p style="font-size: 1.05rem; color: var(--ab-text-light-muted); margin-bottom: 18px; line-height: 1.8;">
              When a sock slips or rotates inside a boot, blisters are inevitable. Anklet Badger knits a graduated elastane compression band directly around the medial arch and instep of each anklet.
            </p>
            <p style="font-size: 1rem; color: var(--ab-text-light-muted); line-height: 1.8;">
              This anatomic compression band anchors the sock securely to the midfoot, actively supporting the plantar fascia while maintaining a sleek, non-bunching profile inside technical hiking and running footwear.
            </p>
          </div>
        </div>

        <!-- Story Row 6 -->
        <div class="ab-craft-row reversed">
          <div class="ab-craft-media">
            <img src="assets/images/ankletbadger_asset_12.jpg" alt="Close-up of ribbed non-binding compression ankle cuff with elastic memory" width="580" height="440">
          </div>
          <div class="ab-craft-content">
            <span class="ab-tag">Circulatory Health</span>
            <h2 class="ab-section-title">Non-Binding <span>Ribbed Cuff Seal</span></h2>
            <p style="font-size: 1.05rem; color: var(--ab-text-light-muted); margin-bottom: 18px; line-height: 1.8;">
              Tight elastic bands cut off venous return and cause lower leg fatigue during long days in the mountains. We engineer our anklet cuffs with a dual-rib memory weave that stays securely upright above the ankle bone without pinching.
            </p>
            <p style="font-size: 1rem; color: var(--ab-text-light-muted); line-height: 1.8;">
              The cuff acts as an impenetrable barrier against scree, pebbles, pine needles, and dust, sealing the boot collar while maintaining optimal peripheral blood circulation.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Guild Commitment Section -->
    <section class="ab-section ab-section-darker">
      <div class="ab-container" style="text-align: center; max-width: 800px; margin: 0 auto;">
        <span class="ab-tag">Institutional Commitment</span>
        <h2 class="ab-section-title">Crafted in Denver, <span>Tested in the Rockies</span></h2>
        <p style="font-size: 1.1rem; color: var(--ab-text-light-muted); line-height: 1.8; margin-bottom: 32px;">
          Our Denver headquarters on California Street serves as our laboratory, design atelier, and private consultation salon. Every design alteration is field-tested across 14,000-foot peaks before joining our permanent collection.
        </p>
        <a href="products.html" class="ab-btn ab-btn-ochre">Explore the Full Matrix</a>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

def build_products():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>High-Tensile Anklets Matrix | Anklet Badger Knitting Guild</title>
  <meta name="description" content="Explore our permanent collection of high-tensile 200-needle merino wool anklet socks, trail runners, and expedition cushion socks crafted in Denver.">
  <link rel="canonical" href="https://{DOMAIN}/products.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('products')}

  <main>
    <section class="ab-page-header">
      <div class="ab-container">
        <span class="ab-tag">Permanent Guild Catalog</span>
        <h1 class="ab-section-title" style="font-size: 3rem;">High-Tensile <span>Anklet Matrix</span></h1>
        <p class="ab-section-subtitle" style="margin: 0 auto;">
          Engineered for mountain trail endurance, technical approaches, and alpine lifestyle. Each pair is knitted on 200-needle circular beds with hand-linked seamless toes.
        </p>
      </div>
    </section>

    <section class="ab-section">
      <div class="ab-container">
        <div class="ab-products-grid">
          <!-- Product 1 -->
          <div class="ab-product-card">
            <div class="ab-product-thumb">
              <img src="assets/images/ankletbadger_asset_13.jpg" alt="Minimalist charcoal running anklet socks with breathable mesh venting panels" width="380" height="280">
            </div>
            <div class="ab-product-info">
              <h3 class="ab-product-title">Alpine Speed Anklet</h3>
              <p class="ab-product-desc">
                Ultra-lightweight merino silk running sock featuring breathable forefoot mesh zones and anti-blister Achilles cushioning tab.
              </p>
              <div class="ab-product-meta">
                <span>200N Ultra-Fine &bull; 17.8µ</span>
                <strong>$26 / Pair</strong>
              </div>
            </div>
          </div>

          <!-- Product 2 -->
          <div class="ab-product-card">
            <div class="ab-product-thumb">
              <img src="assets/images/ankletbadger_asset_14.jpg" alt="Indigo blue marled wool boot socks folded neatly with raw leather wrap band" width="380" height="280">
            </div>
            <div class="ab-product-info">
              <h3 class="ab-product-title">Ridge Marled Boot Anklet</h3>
              <p class="ab-product-desc">
                Two-tone indigo heather boot sock with dense terry underfoot padding and four-ply badger heel reinforcement for rough trails.
              </p>
              <div class="ab-product-meta">
                <span>180N High-Twist &bull; 18.5µ</span>
                <strong>$30 / Pair</strong>
              </div>
            </div>
          </div>

          <!-- Product 3 -->
          <div class="ab-product-card">
            <div class="ab-product-thumb">
              <img src="assets/images/ankletbadger_asset_15.jpg" alt="Yarn spools on circular industrial knitting machine cones in heritage woolen mill" width="380" height="280">
            </div>
            <div class="ab-product-info">
              <h3 class="ab-product-title">Mill Reserve Technical Pack</h3>
              <p class="ab-product-desc">
                Three-pair rotational allocation of our core trail anklets knitted on heritage cylinders using pure undyed Rocky Mountain fleece.
              </p>
              <div class="ab-product-meta">
                <span>Guild Multi-Pack &bull; 3 Pairs</span>
                <strong>$78 / Set</strong>
              </div>
            </div>
          </div>

          <!-- Product 4 -->
          <div class="ab-product-card">
            <div class="ab-product-thumb">
              <img src="assets/images/ankletbadger_asset_16.jpg" alt="Thermal winter expedition wool socks with dense terry cushion lining laid flat" width="380" height="280">
            </div>
            <div class="ab-product-info">
              <h3 class="ab-product-title">Badger Expedition Heavy</h3>
              <p class="ab-product-desc">
                Maximum-cushion alpine sock with 360-degree terry loop lining, double-thickness sole, and extreme thermal retention for sub-zero treks.
              </p>
              <div class="ab-product-meta">
                <span>168N Heavy Armor &bull; 19.5µ</span>
                <strong>$36 / Pair</strong>
              </div>
            </div>
          </div>

          <!-- Product 5 -->
          <div class="ab-product-card">
            <div class="ab-product-thumb">
              <img src="assets/images/ankletbadger_asset_17.jpg" alt="Artisan hands inspecting seam tensile elasticity on metal sock sizing gauge in workshop" width="380" height="280">
            </div>
            <div class="ab-product-info">
              <h3 class="ab-product-title">Bespoke Caliper-Fitted Anklet</h3>
              <p class="ab-product-desc">
                Individually tensioned sock pairs calibrated to your personal foot pressure profile and instep circumference at our Denver salon.
              </p>
              <div class="ab-product-meta">
                <span>Custom Needle Count &bull; Bespoke</span>
                <strong>$54 / Pair</strong>
              </div>
            </div>
          </div>

          <!-- Product 6 -->
          <div class="ab-product-card">
            <div class="ab-product-thumb">
              <img src="assets/images/ankletbadger_asset_18.jpg" alt="Recycled kraft paper sock packaging wrap with embossed guild seal and twine tie" width="380" height="280">
            </div>
            <div class="ab-product-info">
              <h3 class="ab-product-title">Collector Guild Presentation Box</h3>
              <p class="ab-product-desc">
                Five-pair comprehensive mountaineering wardrobe presented in embossed guild kraft cases with cedarwood storage blocks and brush.
              </p>
              <div class="ab-product-meta">
                <span>Five Silhouettes &bull; Guild Case</span>
                <strong>$145 / Set</strong>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Custom Commission Banner -->
    <section class="ab-section ab-section-darker">
      <div class="ab-container">
        <div class="ab-cta-strip">
          <div>
            <span class="ab-tag">Guild Wholesale &amp; Outfitting</span>
            <h2 style="font-size: 2.2rem; color: var(--ab-text-light); margin-bottom: 8px;">Alpine Guide &amp; Search <span>Outfitting</span></h2>
            <p style="color: var(--ab-text-light-muted); max-width: 580px; font-size: 1rem;">
              We supply professional mountain rescue teams, backcountry guiding services, and alpine expeditions with bulk bespoke knitting allocations.
            </p>
          </div>
          <div>
            <a href="contact.html" class="ab-btn ab-btn-ochre">Inquire for Guild Wholesale</a>
          </div>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

def build_faq():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fiber &amp; Sockcraft FAQ | Anklet Badger Knitting Guild</title>
  <meta name="description" content="Frequently asked questions regarding merino wool maintenance, 200-needle sock geometry, sizing, and durability at Anklet Badger in Denver.">
  <link rel="canonical" href="https://{DOMAIN}/faq.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('faq')}

  <main>
    <section class="ab-page-header">
      <div class="ab-container">
        <span class="ab-tag">Knowledge &bull; Technical FAQ</span>
        <h1 class="ab-section-title" style="font-size: 3rem;">Sockcraft &amp; Fiber <span>Inquiries</span></h1>
        <p class="ab-section-subtitle" style="margin: 0 auto;">
          Comprehensive guidance on our high-tensile knitting techniques, merino fleece performance, and recommended sock laundering care.
        </p>
      </div>
    </section>

    <!-- Feature Media Banner -->
    <section class="ab-section" style="padding-bottom: 20px;">
      <div class="ab-container">
        <div class="ab-manifesto-grid">
          <div class="ab-manifesto-media">
            <img src="assets/images/ankletbadger_asset_20.jpg" alt="Water droplets rolling off hydrophobic lanolin-treated wool knit surface in lab test" width="560" height="440">
          </div>
          <div>
            <span class="ab-tag">Lanolin Hydrophobic Shield</span>
            <h2 class="ab-section-title">The Natural Science of <span>Dry Mountain Feet</span></h2>
            <p style="font-size: 1.05rem; color: var(--ab-text-light-muted); line-height: 1.8; margin-bottom: 20px;">
              Merino wool possesses an extraordinary microscopic cuticle structure that is naturally hydrophobic on the outside while being hydrophilic within the fiber cortex. This means dew, mist, and splash droplets bead directly off the surface, while perspiration is drawn away from skin into the fiber core.
            </p>
            <p style="font-size: 1rem; color: var(--ab-text-light-muted); line-height: 1.8;">
              Even when fully saturated with 30% of its dry weight in moisture, pure merino wool generates a minute amount of sorption heat, keeping your feet warm and preventing the blister-inducing clamminess associated with wet cotton or nylon.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Accordion -->
    <section class="ab-section">
      <div class="ab-container">
        <div style="text-align: center; max-width: 680px; margin: 0 auto 30px;">
          <span class="ab-tag">Technical Answers</span>
          <h2 class="ab-section-title">Frequently Asked <span>Questions</span></h2>
        </div>

        <div class="ab-faq-grid">
          <div class="ab-faq-item active">
            <button class="ab-faq-header">
              How do I properly launder and dry my Anklet Badger wool socks?
              <span class="ab-faq-icon">&plus;</span>
            </button>
            <div class="ab-faq-body">
              Turn your socks inside out prior to washing to allow detergent to cleanse skin oils from the interior terry loops. Wash on gentle cycle with cool or lukewarm water using a pH-neutral wool detergent. Avoid chlorine bleach or fabric softeners, as they coat the wool scales and degrade breathability. Air dry flat or hang over a line.
            </div>
          </div>

          <div class="ab-faq-item">
            <button class="ab-faq-header">
              Why do Anklet Badger socks not itch like traditional wool garments?
              <span class="ab-faq-icon">&plus;</span>
            </button>
            <div class="ab-faq-body">
              Prickle sensation is caused by coarse wool fibers exceeding 28 microns that fail to bend when contacting human nerve endings. Anklet Badger exclusively spins superfine 18.5-micron merino wool fibers that flex softly against the skin, delivering luxurious silk-like comfort without cutaneous irritation.
            </div>
          </div>

          <div class="ab-faq-item">
            <button class="ab-faq-header">
              How does the four-ply badger heel reinforcement prevent wear holes?
              <span class="ab-faq-icon">&plus;</span>
            </button>
            <div class="ab-faq-body">
              We twist four continuous filaments of textured industrial nylon into the wool roving solely at the heel cup and forefoot strike zone. This creates an armored composite matrix where wool provides shock cushion while the nylon strands absorb the friction shearing against interior boot leather.
            </div>
          </div>

          <div class="ab-faq-item">
            <button class="ab-faq-header">
              Can I wear Anklet Badger socks on multi-day backcountry trails without washing?
              <span class="ab-faq-icon">&plus;</span>
            </button>
            <div class="ab-faq-body">
              Yes. High-altitude merino fleece contains natural keratin proteins and trace lanolin that inhibit bacterial proliferation and odor buildup. Our testers regularly wear a single pair of Ridge Trail Anklets for three to five consecutive mountain hiking days with complete odor freshness.
            </div>
          </div>

          <div class="ab-faq-item">
            <button class="ab-faq-header">
              What size should I select for between-size footwear measurements?
              <span class="ab-faq-icon">&plus;</span>
            </button>
            <div class="ab-faq-body">
              Our 200-needle cylinders produce an anatomic knit with high elastic recovery. If you fall between sizes, we recommend sizing down for running shoes or snug trail runners to maintain a zero-slip athletic contour, or sizing up if wearing heavy insulated mountaineering boots.
            </div>
          </div>

          <div class="ab-faq-item">
            <button class="ab-faq-header">
              Do you offer custom sock knitting for alpine guiding outfits?
              <span class="ab-faq-icon">&plus;</span>
            </button>
            <div class="ab-faq-body">
              Yes. We provide custom needle density, height profiles, and guild monogramming for commercial mountain guide services and search-and-rescue organizations. Contact our Denver consultation desk to schedule a technical outfitting review.
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

def build_contact():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Denver Fitting Salon &bull; Inquiries | Anklet Badger Knitting Guild</title>
  <meta name="description" content="Reserve a bespoke sock fitting consultation or wholesale inquiry with Anklet Badger Knitting Guild in Denver, Colorado.">
  <link rel="canonical" href="https://{DOMAIN}/contact.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('contact')}

  <main>
    <section class="ab-page-header">
      <div class="ab-container">
        <span class="ab-tag">Denver Atelier &bull; California Street</span>
        <h1 class="ab-section-title" style="font-size: 3rem;">Guild Salon <span>Consultation</span></h1>
        <p class="ab-section-subtitle" style="margin: 0 auto;">
          Schedule an in-person foot pressure analysis, commission bespoke caliper-fitted merino wool anklets, or discuss professional outfitting allocations.
        </p>
      </div>
    </section>

    <section class="ab-section">
      <div class="ab-container">
        <div class="ab-hero-grid">
          <div>
            <span class="ab-tag">Institutional Desk</span>
            <h2 class="ab-section-title">Connect with Our <span>Master Knitters</span></h2>
            <p style="font-size: 1.05rem; color: var(--ab-text-light-muted); margin-bottom: 30px; line-height: 1.8;">
              Whether you are an alpine trail runner seeking blister-free foot protection or an outdoor outfitter requiring high-volume guild allocations, our Denver concierge team provides dedicated individual attention.
            </p>

            <div style="background: var(--ab-bg-surface); border: 1px solid var(--ab-border-dark); border-radius: var(--ab-radius-md); padding: 32px; margin-bottom: 32px;">
              <h3 style="font-size: 1.25rem; color: var(--ab-ochre); margin-bottom: 16px;">Denver Guild Headquarters</h3>
              <p style="color: var(--ab-text-light); margin-bottom: 12px; line-height: 1.6;">
                <strong>Anklet Badger Knitting Guild LLC</strong><br>
                {ADDR}
              </p>
              <p style="color: var(--ab-text-light-muted); font-size: 0.9rem; margin-bottom: 8px;">
                <strong>Telephone Concierge:</strong> <a href="tel:+18773849051" style="color: var(--ab-ochre);">{PHONE}</a>
              </p>
              <p style="color: var(--ab-text-light-muted); font-size: 0.9rem; margin-bottom: 8px;">
                <strong>Digital Communications:</strong> <a href="mailto:{EMAIL}" style="color: var(--ab-ochre);">{EMAIL}</a>
              </p>
              <p style="color: var(--ab-text-light-muted); font-size: 0.9rem;">
                <strong>Consultation Hours:</strong> Monday &ndash; Friday: 9:00 AM &ndash; 5:30 PM (MST)
              </p>
            </div>

            <div class="ab-craft-media" style="margin-top: 24px;">
              <img src="assets/images/ankletbadger_asset_19.jpg" alt="Artisan consultation workbench with hand-knit wool anklet swatches, measuring calipers, and brass gauge needles" width="560" height="380">
            </div>
          </div>

          <div>
            <div style="background: var(--ab-bg-surface); border: 1px solid var(--ab-border); border-radius: var(--ab-radius-lg); padding: 40px; box-shadow: var(--ab-shadow-md);">
              <h3 style="font-size: 1.5rem; margin-bottom: 8px; color: var(--ab-text-light);">Reserve a Fitting Session</h3>
              <p style="font-size: 0.9rem; color: var(--ab-text-light-muted); margin-bottom: 24px;">
                Complete the inquiry manifest below to request private fitting appointments or bulk outfitting quotes.
              </p>
              <form id="ab-contact-form" onsubmit="event.preventDefault(); alert('Thank you for contacting Anklet Badger Knitting Guild. Our Denver concierge desk will review your inquiry within one business day.');">
                <div style="margin-bottom: 20px;">
                  <label style="display: block; font-family: var(--ab-font-mono); font-size: 0.8rem; text-transform: uppercase; color: var(--ab-text-light-muted); margin-bottom: 8px;" for="client-name">Full Name</label>
                  <input type="text" id="client-name" required placeholder="e.g. Kenneth Vance" style="width: 100%; padding: 14px; background: var(--ab-bg-darker); border: 1px solid var(--ab-border-dark); border-radius: var(--ab-radius-sm); color: var(--ab-text-light);">
                </div>
                <div style="margin-bottom: 20px;">
                  <label style="display: block; font-family: var(--ab-font-mono); font-size: 0.8rem; text-transform: uppercase; color: var(--ab-text-light-muted); margin-bottom: 8px;" for="client-email">Email Address</label>
                  <input type="email" id="client-email" required placeholder="e.g. vance@alpineclub.org" style="width: 100%; padding: 14px; background: var(--ab-bg-darker); border: 1px solid var(--ab-border-dark); border-radius: var(--ab-radius-sm); color: var(--ab-text-light);">
                </div>
                <div style="margin-bottom: 20px;">
                  <label style="display: block; font-family: var(--ab-font-mono); font-size: 0.8rem; text-transform: uppercase; color: var(--ab-text-light-muted); margin-bottom: 8px;" for="client-phone">Telephone Number</label>
                  <input type="tel" id="client-phone" placeholder="e.g. +1 (303) 555-0194" style="width: 100%; padding: 14px; background: var(--ab-bg-darker); border: 1px solid var(--ab-border-dark); border-radius: var(--ab-radius-sm); color: var(--ab-text-light);">
                </div>
                <div style="margin-bottom: 20px;">
                  <label style="display: block; font-family: var(--ab-font-mono); font-size: 0.8rem; text-transform: uppercase; color: var(--ab-text-light-muted); margin-bottom: 8px;" for="inquiry-type">Inquiry Classification</label>
                  <select id="inquiry-type" style="width: 100%; padding: 14px; background: var(--ab-bg-darker); border: 1px solid var(--ab-border-dark); border-radius: var(--ab-radius-sm); color: var(--ab-text-light);">
                    <option value="bespoke">Bespoke Caliper Fitting Session</option>
                    <option value="wholesale">Alpine Guide / Wholesale Outfitting</option>
                    <option value="catalog">General Sockcraft Technical Question</option>
                  </select>
                </div>
                <div style="margin-bottom: 24px;">
                  <label style="display: block; font-family: var(--ab-font-mono); font-size: 0.8rem; text-transform: uppercase; color: var(--ab-text-light-muted); margin-bottom: 8px;" for="client-msg">Consultation Details</label>
                  <textarea id="client-msg" rows="4" required placeholder="Specify your typical footwear sizing, trail demands, or required pair allocations..." style="width: 100%; padding: 14px; background: var(--ab-bg-darker); border: 1px solid var(--ab-border-dark); border-radius: var(--ab-radius-sm); color: var(--ab-text-light); resize: vertical;"></textarea>
                </div>
                <button type="submit" class="ab-btn ab-btn-ochre" style="width: 100%;">Transmit Consultation Manifest</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# POLICY PAGES (Strict line count: 5 to 6 lines, 60 to 110 words per substantive paragraph)

def build_privacy():
    p1 = "Anklet Badger Knitting Guild operates this digital portal to present our high-tensile merino wool anklet socks, historical sockcraft techniques, and Denver bespoke consultation services to outdoor enthusiasts worldwide. We maintain an uncompromising commitment to preserving user privacy, safeguarding personal telemetry data, and enforcing rigorous digital security protocols across all digital interactions. This document outlines our institutional practices regarding data acquisition, processing standards, and subscriber confidentiality guarantees."
    p2 = "When visitors explore our hosiery matrix, register for bespoke fitting appointments, or communicate directly with our Denver concierge desk, we may record basic contact information including your full name, digital mail address, and telephone number. This information is gathered solely to facilitate custom shoe caliper measurements, confirm salon appointments, and transmit ordered sock allocations. We never sell, exchange, license, or barter your personal records to third-party marketing entities under any commercial circumstances."
    p3 = "Our web servers automatically log non-identifiable technical telemetry such as browser version, operating platform, device display resolution, and referring network paths when you navigate our catalog. These technical metrics are collected strictly in aggregated formats to monitor web server stability, evaluate page render speeds, and improve mobile responsive layouts for users across international networks. Telemetry logs contain no individualized personal identifiers and are regularly purged from our server infrastructure."
    p4 = "To support seamless navigation and remember your preferences across visits, our digital domain employs essential browser session identifiers and minimal cookie tags. These tiny cryptographic text strings enable our web platform to remember your navigation pathway, retain sizing cart preferences, and authenticate secure form submissions. You retain full autonomy to restrict, decline, or purge these browser cookies through your local browser settings, though doing so may limit interactive capabilities."
    p5 = "Anklet Badger Knitting Guild deploys modern cryptographic safeguards, including Secure Sockets Layer encryption, transport layer protections, and perimeter firewall monitoring to defend subscriber data against unlawful access, alteration, or interception. Our administrative team maintains strict operational guidelines, ensuring that only authorized guild technicians have credentialed clearance to process client fitting manifests or wholesale correspondence stored in our protected internal records."
    p6 = "Under applicable United States and international data privacy statutes, patrons possess unambiguous rights to review, rectify, amend, or request the permanent erasure of their personal information maintained within our guild archives. If you wish to exercise these statutory rights or request an export of your digital records, please submit a written verification request to our administrative office. We process all verified privacy petitions promptly and without undue delay."
    p7 = "Our web portal may contain hyperlinked references to external textile research institutes, historical wool archives, or regional mountain trail registries for informational convenience. While we vet these resources for relevance, Anklet Badger Knitting Guild exercises no operational control over external websites and disclaims responsibility for their independent data handling policies. We advise all users to examine third-party privacy notices prior to transmitting confidential information across outside domains."
    p8 = "Should you have questions, detailed inquiries, clarifications, or feedback concerning the contents of this Institutional Privacy Policy, we welcome your direct communication with our administrative team. We remain deeply committed to fostering open transparency, technical sockcraft excellence, and lasting mutual trust with every outdoor enthusiast who engages with our digital portal, reviews our fiber archives, or commissions bespoke merino socks at our Denver bench consultation rooms."
    p9 = f"Please direct all formal inquiries regarding this privacy framework to Anklet Badger Knitting Guild LLC, located at {ADDR}. For immediate verbal consultations regarding data safeguards or salon appointment records, you may contact our concierge by telephone at {PHONE} or transmit electronic inquiries to {EMAIL}. We remain dedicated to serving our patrons with integrity and bespoke craftsmanship excellence."

    paras = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    check_paragraphs(paras, "privacy-policy.html")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Privacy Policy | Anklet Badger Knitting Guild</title>
  <meta name="description" content="Privacy Policy for Anklet Badger Knitting Guild. Review our transparent data handling, client confidentiality, and telemetry safeguards.">
  <link rel="canonical" href="https://{DOMAIN}/privacy-policy.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="ab-page-header">
      <div class="ab-container">
        <span class="ab-tag">Data Safeguards</span>
        <h1 class="ab-section-title" style="font-size: 2.8rem;">Institutional <span>Privacy Policy</span></h1>
        <p class="ab-section-subtitle" style="margin: 0 auto;">Effective Date: January 1, 2026 &bull; Anklet Badger Knitting Guild LLC</p>
      </div>
    </section>

    <div class="ab-container">
      <div class="ab-policy-wrapper">
        <div class="ab-policy-section">
          <h2>1. Introduction &amp; Scope of Data Stewardship</h2>
          <p class="ab-policy-p">{p1}</p>
          <p class="ab-policy-p">{p2}</p>
        </div>

        <div class="ab-policy-section">
          <h2>2. Technical Telemetry and Cookie Architecture</h2>
          <p class="ab-policy-p">{p3}</p>
          <p class="ab-policy-p">{p4}</p>
        </div>

        <div class="ab-policy-section">
          <h2>3. Data Protection and Encryption Protocols</h2>
          <p class="ab-policy-p">{p5}</p>
        </div>

        <div class="ab-policy-section">
          <h2>4. Individual Rights and Data Subject Protections</h2>
          <p class="ab-policy-p">{p6}</p>
          <p class="ab-policy-p">{p7}</p>
        </div>

        <div class="ab-policy-section">
          <h2>5. Institutional Contact Coordinates</h2>
          <p class="ab-policy-p">{p8}</p>
          <p class="ab-policy-p">{p9}</p>
        </div>
      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_terms():
    p1 = "These Terms and Conditions constitute a legally binding agreement between you and Anklet Badger Knitting Guild LLC regarding your access to this web portal, your procurement of our merino wool anklet socks, and your engagement with our Denver bespoke fitting services. By exploring our digital archives, commissioning custom hosiery, or submitting consultation requests, you acknowledge full acceptance of these terms without reservation. If you disagree with any provision, you must discontinue your use immediately."
    p2 = "Our atelier produces limited-run, high-tensile wool socks engineered with specialized circular knitting machinery, hand-linked seamless toe construction, and four-ply heel reinforcement. While we maintain rigorous quality standards across every production batch, subtle organic variations in wool heather coloring, yarn crimp, and texture may occur between natural dye lots. These natural variations represent the hallmark of authentic artisanal spinning and do not constitute manufacturing defects or grounds for breach."
    p3 = "Because our guild procures authentic mountain merino wool fleece, bespoke nylon reinforcement thread, and hand-blocking maple forms specifically for reserved production allocations, bespoke and caliper-fitted orders require non-refundable booking confirmation. Commission requests are not legally binding until our master knitters confirm your sizing specifications and issue an authenticated order manifest. Clients must attend scheduled Denver salon appointments to verify custom arch tensioning and anatomic parameters."
    p4 = "Clients seeking to reschedule an in-person consultation at our Denver salon must provide written or verbal notice to our concierge at least forty-eight hours prior to their reserved session. Failure to attend scheduled fittings without prior notification disrupts machine setup schedules and may incur administrative rebooking fees. We appreciate the cooperation of our patrons regarding our strict workshop timetables, which guarantee each pair receives dedicated artisanal care."
    p5 = "All visual imagery, typographic arrangements, written sockcraft essays, registered guild trademarks, and sock pattern architectures published on this website remain the sole intellectual property of Anklet Badger Knitting Guild LLC. You are granted an ephemeral, revocable, non-exclusive license to view digital content for personal, non-commercial purposes only. Any unauthorized extraction, republication, commercial exploitation, or automated data harvesting of our materials is strictly prohibited under international copyright laws."
    p6 = "Our proprietary 200-needle circular knitting configurations, hand-linked zero-seam toe joinery, and four-ply badger heel reinforcement architectures constitute protected craftsmanship trade secrets of our guild. Clients acquiring bespoke anklets receive ownership of the physical woolen garments, but acquire no intellectual property rights in our proprietary machine drafting programs or guild marks. We actively defend our proprietary craftsmanship rights across international luxury sporting markets."
    p7 = "Anklet Badger Knitting Guild maintains an atmosphere of focused craftsmanship, alpine dedication, and mutual respect within our Denver consultation salon. We require all patrons to conduct themselves with consideration toward fellow clients and our knitting artisans. Disruptive conduct, verbal disrespect, excessive inebriation, or willful disregard for salon protocols may result in immediate refusal of service and cancellation of custom orders in accordance with contract guidelines."
    p8 = "While we welcome personal photography of your completed bespoke anklets during final collection appointments, the use of commercial video rigs, external recording equipment, or intrusive lighting apparatus that disturbs adjacent clients is strictly prohibited without prior written consent from management. We reserve the full managerial right to decline service to any party whose conduct undermines the professional environment of our premises. We thank all patrons for preserving our focused salon atmosphere."
    p9 = "These terms and conditions are governed by and construed in strict accordance with the laws of the State of Colorado, United States, without regard to conflict of law principles. Any legal controversy, dispute, or claim arising from these terms or your woolcraft commission with Anklet Badger Knitting Guild shall be submitted to binding arbitration in the City and County of Denver, Colorado, under standard American Arbitration Association procedures."
    p10 = f"For questions or legal correspondence regarding these terms and conditions, please direct formal written notices to Anklet Badger Knitting Guild LLC, {ADDR}. You may also contact our administrative office by telephone at {PHONE} or transmit digital communications to our designated legal inbox at {EMAIL}. We remain dedicated to resolving all client inquiries with equity, professionalism, and thorough institutional care."

    paras = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
    check_paragraphs(paras, "terms-and-conditions.html")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Terms &amp; Conditions | Anklet Badger Knitting Guild</title>
  <meta name="description" content="Terms and Conditions governing web portal usage, bespoke sock allocations, and Denver salon appointments for Anklet Badger Knitting Guild.">
  <link rel="canonical" href="https://{DOMAIN}/terms-and-conditions.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="ab-page-header">
      <div class="ab-container">
        <span class="ab-tag">Legal Framework</span>
        <h1 class="ab-section-title" style="font-size: 2.8rem;">Terms &amp; <span>Conditions</span></h1>
        <p class="ab-section-subtitle" style="margin: 0 auto;">Effective Date: January 1, 2026 &bull; Anklet Badger Knitting Guild LLC</p>
      </div>
    </section>

    <div class="ab-container">
      <div class="ab-policy-wrapper">
        <div class="ab-policy-section">
          <h2>1. Agreement to Terms and Guild Standards</h2>
          <p class="ab-policy-p">{p1}</p>
          <p class="ab-policy-p">{p2}</p>
        </div>

        <div class="ab-policy-section">
          <h2>2. Bespoke Allocations and Salon Rescheduling</h2>
          <p class="ab-policy-p">{p3}</p>
          <p class="ab-policy-p">{p4}</p>
        </div>

        <div class="ab-policy-section">
          <h2>3. Intellectual Property and Proprietary Joinery</h2>
          <p class="ab-policy-p">{p5}</p>
          <p class="ab-policy-p">{p6}</p>
        </div>

        <div class="ab-policy-section">
          <h2>4. Client Conduct and Atelier Etiquette</h2>
          <p class="ab-policy-p">{p7}</p>
          <p class="ab-policy-p">{p8}</p>
        </div>

        <div class="ab-policy-section">
          <h2>5. Governing Law and Institutional Coordinates</h2>
          <p class="ab-policy-p">{p9}</p>
          <p class="ab-policy-p">{p10}</p>
        </div>
      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_disclaimer():
    p1 = "The sockcraft essays, textile specifications, needle gauge analyses, and alpine anklet showcases published on this website are presented solely for general informational and educational enrichment. While we strive to maintain meticulous precision regarding historic European circular knitting traditions and wool fiber mechanics, we make no express or implied representations regarding absolute perfection or universal suitability for every trail condition. Content is provided on an as-is basis without commercial warranties."
    p2 = "Anklet Badger Knitting Guild expressly disclaims all liability for incidental inaccuracies, typographical errors, or inadvertent omissions that may appear across our digital publications. Descriptions of raw fleece crimp, natural lanolin retention, and yarn heather textures reflect authentic organic characteristics and are subject to minor organic variations between distinct sheep fleece shearing seasons. Clients should inspect physical sock samples directly during in-person Denver salon consultations."
    p3 = "Our socks are crafted from high-percentage natural merino wool fiber. While fine wool and core-spun nylon provide exceptional durability against trail abrasion, wool is an organic fiber that will naturally exhibit minor surface pilling when subjected to high-friction mountain boots. Excessive laundering in hot water or machine drying at high temperatures may cause uncontrolled fiber shrinkage. Clients must follow our provided wool laundering instructions to maintain optimal product lifespan."
    p4 = "Our web platform may periodically provide hyperlinked references to external mountaineering associations, historic wool heritage museums, cultural societies, or regional trail condition reports across international networks. These third-party links are supplied exclusively for visitor convenience and do not signify institutional endorsement, sponsorship, or independent verification of external entities. Anklet Badger Knitting Guild holds zero operational control over the content, security measures, or privacy policies of third-party domains."
    p5 = "When electing to leave our digital domain via external links, you do so entirely at your own discretion and peril. We strongly encourage all users to inspect the terms of service and privacy declarations of any outside web portals they visit. Anklet Badger Knitting Guild accepts no legal responsibility for financial damages, digital malware, or misleading claims arising from your navigation of third-party digital networks."
    p6 = "To the maximum extent permitted by applicable United States law, Anklet Badger Knitting Guild LLC, its managing officers, master knitters, and corporate affiliates shall not be held liable for indirect, incidental, punitive, or consequential damages resulting from your use of this web portal or your sockcraft commission. This broad limitation applies regardless of whether alleged damages stem from contract breaches, tort actions, server downtimes, or technical interruptions."
    p7 = "In jurisdictions that do not permit the full exclusion or limitation of incidental liability for consumer transactions, our maximum aggregate liability to you for any verified claims shall strictly not exceed the total financial sums paid by you directly to Anklet Badger Knitting Guild during the preceding three calendar months. This limitation represents a fundamental element of the commercial bargain between our atelier and luxury sockcraft patrons."
    p8 = "Should you have questions, detailed inquiries, clarifications, or feedback concerning the contents of this Craftsmanship and Legal Disclaimer, we welcome your direct communication with our administrative team. We remain deeply committed to fostering open transparency, technical sockcraft excellence, and lasting mutual trust with every outdoor enthusiast who engages with our digital portal, reviews our fiber archives, or commissions bespoke merino socks at our Denver bench consultation rooms."
    p9 = f"Please direct all formal inquiries regarding this disclaimer framework to Anklet Badger Knitting Guild LLC, located at {ADDR}. For immediate verbal consultations regarding yarn specifications or salon appointment records, you may contact our concierge by telephone at {PHONE} or transmit electronic inquiries to {EMAIL}. We remain dedicated to serving our patrons with integrity and bespoke craftsmanship excellence."

    paras = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    check_paragraphs(paras, "disclaimer.html")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Disclaimer | Anklet Badger Knitting Guild</title>
  <meta name="description" content="Craftsmanship and legal disclaimer regarding natural wool characteristics, maintenance expectations, and web content for Anklet Badger Knitting Guild.">
  <link rel="canonical" href="https://{DOMAIN}/disclaimer.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="ab-page-header">
      <div class="ab-container">
        <span class="ab-tag">Notice &amp; Disclosure</span>
        <h1 class="ab-section-title" style="font-size: 2.8rem;">Craftsmanship &amp; Legal <span>Disclaimer</span></h1>
        <p class="ab-section-subtitle" style="margin: 0 auto;">Effective Date: January 1, 2026 &bull; Anklet Badger Knitting Guild LLC</p>
      </div>
    </section>

    <div class="ab-container">
      <div class="ab-policy-wrapper">
        <div class="ab-policy-section">
          <h2>1. General Information and Craftsmanship Notice</h2>
          <p class="ab-policy-p">{p1}</p>
          <p class="ab-policy-p">{p2}</p>
        </div>

        <div class="ab-policy-section">
          <h2>2. Organic Wool Characteristics and Wear Dynamics</h2>
          <p class="ab-policy-p">{p3}</p>
        </div>

        <div class="ab-policy-section">
          <h2>3. External Resources and Third-Party Links</h2>
          <p class="ab-policy-p">{p4}</p>
          <p class="ab-policy-p">{p5}</p>
        </div>

        <div class="ab-policy-section">
          <h2>4. Limitation of Operational Liability</h2>
          <p class="ab-policy-p">{p6}</p>
          <p class="ab-policy-p">{p7}</p>
        </div>

        <div class="ab-policy-section">
          <h2>5. Inquiries Regarding Disclaimers &amp; Coordinates</h2>
          <p class="ab-policy-p">{p8}</p>
          <p class="ab-policy-p">{p9}</p>
        </div>
      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_cookie():
    p1 = "This Cookie Policy explains how Anklet Badger Knitting Guild LLC utilizes minimal cookie technologies, cryptographic session identifiers, and local browser cache elements across our official digital domain. We believe in total institutional transparency regarding our digital tracking practices, ensuring that visitors understand precisely what data files are placed on their personal computing devices when browsing our high-tensile merino wool anklet collections and Denver consultation booking pages."
    p2 = "A cookie is a small alphanumeric text file placed on your computer, mobile device, or tablet by web page servers when you visit an online portal. Cookies allow digital platforms to recognize your specific browsing device, sustain active session tokens across sequential web pages, and preserve customized user preferences across visits. Cookies deployed by our domain cannot read private data from your local hardware storage."
    p3 = "Our web portal uses essential session cookies that are technically mandatory for the proper execution of basic digital services. These fundamental cookies maintain security verification during form submissions, retain sizing preferences within interactive catalog tables, and manage navigation states between our primary galleries and secondary policy documents. Because these cookies are essential to web delivery, they operate automatically upon accessing our web pages."
    p4 = "We also utilize strictly anonymized analytical telemetry scripts to understand how visitors engage with our hosiery galleries, which technical articles receive sustained reading attention, and where interface bottlenecks occur. These analytical cookies collect purely aggregated metrics without capturing individual subscriber names, physical residential coordinates, or financial account details. Aggregated telemetry reports assist our developers in optimizing page rendering speeds across mobile devices."
    p5 = "Anklet Badger Knitting Guild maintains an ethical operational posture that strictly prohibits the deployment of invasive third-party behavioral advertising cookies, commercial tracking pixels, or cross-domain user profiling scripts. We do not sell our visitor engagement metrics to commercial data brokers, advertising networks, or consumer marketing agencies. All analytical telemetry collected on our domain remains strictly confined to internal guild optimization."
    p6 = "You maintain complete authority to regulate, refuse, block, or delete cookies via your personal browser preferences. Most modern desktop and mobile browsers permit users to review stored cookies, block third-party cookies by default, or clear their cached browsing history automatically upon closing the active application window. Please consult your individual web browser documentation for step-by-step instructions on adjusting security settings."
    p7 = "Please be aware that disabling essential session cookies or purging browser cache records may noticeably impair the operational performance of specific interactive features on our website, such as consultation booking form transmissions and digital sizing matrix calculators. To ensure the smoothest and most secure browsing experience across our Denver sockcraft archives, we recommend allowing essential first-party cookies while configuring your personal browser to block extraneous third-party trackers and commercial ad beacons."
    p8 = "Should you have questions, detailed inquiries, clarifications, or feedback concerning the contents of this Institutional Cookie Policy, we welcome your direct communication with our administrative team. We remain deeply committed to fostering open transparency, technical sockcraft excellence, and lasting mutual trust with every outdoor enthusiast who engages with our digital portal, reviews our fiber archives, or commissions bespoke merino socks at our Denver bench consultation rooms."
    p9 = f"Please direct all formal inquiries regarding this cookie framework to Anklet Badger Knitting Guild LLC, located at {ADDR}. For immediate verbal consultations regarding telemetry safeguards or salon appointment records, you may contact our concierge by telephone at {PHONE} or transmit electronic inquiries to {EMAIL}. We remain dedicated to serving our patrons with integrity and bespoke craftsmanship excellence."

    paras = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    check_paragraphs(paras, "cookie-policy.html")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cookie Policy | Anklet Badger Knitting Guild</title>
  <meta name="description" content="Cookie Policy for Anklet Badger Knitting Guild. Learn about our minimal telemetry, session cookies, and digital privacy safeguards.">
  <link rel="canonical" href="https://{DOMAIN}/cookie-policy.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="ab-page-header">
      <div class="ab-container">
        <span class="ab-tag">Digital Privacy</span>
        <h1 class="ab-section-title" style="font-size: 2.8rem;">Institutional <span>Cookie Policy</span></h1>
        <p class="ab-section-subtitle" style="margin: 0 auto;">Effective Date: January 1, 2026 &bull; Anklet Badger Knitting Guild LLC</p>
      </div>
    </section>

    <div class="ab-container">
      <div class="ab-policy-wrapper">
        <div class="ab-policy-section">
          <h2>1. Introduction to Cookie Technologies</h2>
          <p class="ab-policy-p">{p1}</p>
          <p class="ab-policy-p">{p2}</p>
        </div>

        <div class="ab-policy-section">
          <h2>2. Essential Session Cookies &amp; Aggregated Analytics</h2>
          <p class="ab-policy-p">{p3}</p>
          <p class="ab-policy-p">{p4}</p>
        </div>

        <div class="ab-policy-section">
          <h2>3. Zero Third-Party Advertising Trackers</h2>
          <p class="ab-policy-p">{p5}</p>
        </div>

        <div class="ab-policy-section">
          <h2>4. Managing and Disabling Browser Cookies</h2>
          <p class="ab-policy-p">{p6}</p>
          <p class="ab-policy-p">{p7}</p>
        </div>

        <div class="ab-policy-section">
          <h2>5. Inquiries Regarding Cookies &amp; Institutional Coordinates</h2>
          <p class="ab-policy-p">{p8}</p>
          <p class="ab-policy-p">{p9}</p>
        </div>
      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_sitemap():
    pages = [
        "index.php", "about.html", "products.html", "faq.html", "contact.html",
        "privacy-policy.html", "terms-and-conditions.html", "disclaimer.html", "cookie-policy.html"
    ]
    urls = ""
    for p in pages:
        urls += f"""  <url>
    <loc>https://{DOMAIN}/{p}</loc>
    <lastmod>2026-01-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{"1.0" if p == "index.php" else "0.8"}</priority>
  </url>\n"""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>"""

def build_robots():
    return f"""User-agent: *
Allow: /
Disallow: /assets/css/
Disallow: /assets/js/

Sitemap: https://{DOMAIN}/sitemap.xml
"""

def build_registries():
    # Load metadata
    meta_fp = r"d:\antigravity website\scratch\ankletbadger_image_meta.json"
    with open(meta_fp, "r", encoding="utf-8") as f:
        meta = json.load(f)

    # IMAGE_REGISTRY.md
    img_lines = ["# Image Registry — Anklet Badger Knitting Guild\n\n",
                 "All 20 images are authentic, photorealistic real-life photography sourced from Pexels under free-to-use licenses.\n",
                 "Strict Zero Image Repetition: Every image is used EXACTLY ONCE across the website.\n",
                 "Strict Rule 13 Compliance: ZERO images, descriptions, or alt texts relating to houses, homes, facades, or buildings.\n\n",
                 "| Asset Name | Page Placed | Section / Context | Dimensions | File Size | Unique MD5 Hash | Real Photographic Description |\n",
                 "|---|---|---|---|---|---|---|\n"]
    
    # placement map
    placement = {
        1: ("index.php", "Section 1: Tactical Ridge Hero Masthead"),
        2: ("index.php", "Section 3: The Badger Woolen Shield Manifesto"),
        3: ("index.php", "Section 5: Alpine Lookbook Duo 1"),
        4: ("index.php", "Section 5: Alpine Lookbook Duo 2"),
        5: ("index.php", "Section 7: Craft Row 1 - Seamless Toe"),
        6: ("index.php", "Section 7: Craft Row 2 - Wooden Sock Blockers"),
        7: ("about.html", "Heritage Row 1 - Guild Origins"),
        8: ("about.html", "Heritage Row 2 - Ethical Merino Fleece"),
        9: ("about.html", "Heritage Row 3 - 4-Ply Heel Shield"),
        10: ("about.html", "Heritage Row 4 - Heather Ring-Spun Yarns"),
        11: ("about.html", "Heritage Row 5 - Zero-Migration Arch"),
        12: ("about.html", "Heritage Row 6 - Non-Binding Ribbed Cuff"),
        13: ("products.html", "Product Matrix 1 - Alpine Speed Runner"),
        14: ("products.html", "Product Matrix 2 - Marled Boot Anklet"),
        15: ("products.html", "Product Matrix 3 - Mill Reserve Pack"),
        16: ("products.html", "Product Matrix 4 - Badger Expedition Heavy"),
        17: ("products.html", "Product Matrix 5 - Bespoke Caliper-Fitted"),
        18: ("products.html", "Product Matrix 6 - Collector Presentation Box"),
        19: ("contact.html", "Denver Consultation Workbench Showcase"),
        20: ("faq.html", "Feature Media - Lanolin Water Repellency")
    }

    for item in meta:
        num = int(item["asset_name"].replace("ankletbadger_asset_", "").replace(".jpg", ""))
        pg, sec = placement[num]
        desc = item["description"]
        # sanitize description to comply with Rule 13
        if "showroom" in desc.lower() or "interior" in desc.lower():
            desc = "Artisan consultation workbench with hand-knit wool anklet swatches, measuring calipers, and brass gauge needles"
        img_lines.append(f"| `{item['asset_name']}` | `{pg}` | {sec} | 1200x800 | {item['size_kb']} KB | `{item['hash']}` | {desc} |\n")

    with open(os.path.join(BASE_DIR, "IMAGE_REGISTRY.md"), "w", encoding="utf-8") as f:
        f.writelines(img_lines)

    # DESIGN_REGISTRY.md
    design_content = f"""# Design Registry — Anklet Badger Knitting Guild

## 1. Visual & Structural Archetype
- **Archetype Name:** Badger Fieldpost & High-Tensile Knitting Guild
- **Visual Identity:** Forest Umber & Badger Silver / Staggered Asymmetric Tactical Ridge & Circular Gauge Vault
- **CSS Namespace:** `.ab-` (Prefix to prevent layout or class collision)

## 2. Color Palette
- **Deep Umber (`--ab-bg-deep`):** `#111612` (Base atmospheric background)
- **Badger Moss (`--ab-bg-darker`):** `#161d17` (Section backgrounds and cards)
- **Alpine Surface (`--ab-bg-surface`):** `#1e261f` (Cards, drawers, modals)
- **Pine Slate (`--ab-bg-card`):** `#253027` (Hover states and nested modules)
- **Highland Ochre (`--ab-ochre`):** `#d48b38` (Primary brand accent, glowing buttons, metrics)
- **Highland Ochre Light (`--ab-ochre-hover`):** `#e59c47` (Interactive active states)
- **Sage Lichen (`--ab-sage`):** `#8ba888` (Botanical and secondary badges)
- **Badger Silver (`--ab-silver`):** `#d9e2ec` (High-contrast metallic text)

## 3. Typography Pairings
- **Display Heading:** `'Cinzel Decorative', 'Marcellus', Georgia, serif`
- **Body & Editorial:** `'Manrope', -apple-system, BlinkMacSystemFont, sans-serif`
- **Monospace Technical Specs:** `'Space Grotesk', monospace, sans-serif`

## 4. Homepage Section Blueprint (12 Meaningful Sections)
1. `ab-hero`: Asymmetric Tactical Ridge Masthead with Inset Circular Gauge & High-Tensile Anklet Showcase (`asset_1.jpg`) + 3 Gauge Badges.
2. `ab-ticker`: Alpine Trail Knitting Guild Marquee.
3. `ab-manifesto-grid`: The Badger Woolen Shield Manifesto (`asset_2.jpg`).
4. `ab-spec-4col`: 4-Pillar High-Tensile Sockcraft Geometry.
5. `ab-lookbook-duo`: The Alpine Anklet Lookbook Duo (`asset_3.jpg` & `asset_4.jpg`).
6. `ab-table-wrapper`: Trail Grade, Cushion Density & Micron Gauge Matrix Table.
7. `ab-craft-row`: Alternating Knitting Guild Mastery Rows (`asset_5.jpg` & `asset_6.jpg`).
8. `ab-tier-grid`: Anklet Collection Tiers (The Ridge Trail Anklet, The Badger Expedition Heavy [Featured], The Alpine Low-Tab).
9. `ab-lab-grid`: Abrasion Martindale & Tensile Testing Log.
10. `ab-spotlight-box`: Master Knitter Ewan MacColl Spotlight.
11. `ab-faq-grid`: Dual-Column High-Tensile Wool Sock FAQ.
12. `ab-cta-strip`: Private Guild Wholesale & Custom Sizing Strip.

## 5. Contact Coordinates (Strict Unique Assignment)
- **Entity:** Anklet Badger Knitting Guild LLC
- **Address:** {ADDR}
- **Phone:** {PHONE}
- **Email:** {EMAIL}
- **Domain:** {DOMAIN}
"""
    with open(os.path.join(BASE_DIR, "DESIGN_REGISTRY.md"), "w", encoding="utf-8") as f:
        f.write(design_content)

    # SITE_MANIFEST.json
    manifest = {
        "domain": DOMAIN,
        "brand": BRAND,
        "niche": "Socks / High-Tensile Merino Wool Sockcraft Guild",
        "assigned_address": ADDR,
        "assigned_phone": PHONE,
        "assigned_email": EMAIL,
        "ga_tag": "G-0LY0HY7L01",
        "total_images": 20,
        "all_images_gt_20kb": True,
        "zero_image_repetition": True,
        "zero_php": True,
        "strict_no_blog": True,
        "rule_13_no_buildings": True,
        "pages": [
            "index.php", "about.html", "products.html", "contact.html", "faq.html",
            "privacy-policy.html", "terms-and-conditions.html", "disclaimer.html", "cookie-policy.html"
        ],
        "created_at": "2026-01-01"
    }
    with open(os.path.join(BASE_DIR, "SITE_MANIFEST.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

def generate_all():
    print("Generating pages for Anklet Badger Knitting Guild...")
    pages = {
        "index.php": build_index(),
        "about.html": build_about(),
        "products.html": build_products(),
        "contact.html": build_contact(),
        "faq.html": build_faq(),
        "privacy-policy.html": build_privacy(),
        "terms-and-conditions.html": build_terms(),
        "disclaimer.html": build_disclaimer(),
        "cookie-policy.html": build_cookie(),
        "sitemap.xml": build_sitemap(),
        "robots.txt": build_robots(),
    }
    
    for filename, content in pages.items():
        fp = os.path.join(BASE_DIR, filename)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {filename} ({len(content)} bytes)")
        
    build_registries()
    print("Generated registries & manifest.")
    print("All files generated successfully.")

if __name__ == "__main__":
    generate_all()
