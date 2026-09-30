/**
 * ANKLET BADGER KNITTING GUILD — SCRIPT ENGINE
 * Handles Mobile Drawer Navigation, Accordion Interactions, and Guild Inquiry
 */

document.addEventListener('DOMContentLoaded', function () {
  // Mobile Drawer Toggle (Rule 11)
  const hamburger = document.getElementById('ab-hamburger');
  const drawer = document.getElementById('mobile-drawer');
  const backdrop = document.getElementById('mobile-drawer-backdrop');
  const closeBtn = document.getElementById('mobile-drawer-close');

  function openDrawer() {
    if (drawer) drawer.classList.add('active');
    if (backdrop) backdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    if (drawer) drawer.classList.remove('active');
    if (backdrop) backdrop.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (hamburger) hamburger.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  if (backdrop) backdrop.addEventListener('click', closeDrawer);

  // Accordion Toggles
  const faqItems = document.querySelectorAll('.ab-faq-item');
  faqItems.forEach(item => {
    const header = item.querySelector('.ab-faq-header');
    if (header) {
      header.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        faqItems.forEach(i => i.classList.remove('active'));
        if (!isActive) item.classList.add('active');
      });
    }
  });

  // Guild Sizing & Consultation Form Handling
  const form = document.getElementById('ab-consultation-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const btn = form.querySelector('button[type="submit"]');
      btn.innerText = 'Transmitting Guild Inquiry...';
      btn.disabled = true;

      setTimeout(() => {
        form.innerHTML = `
          <div style="padding: 32px; background: rgba(212,139,56,0.08); border: 1px solid var(--ab-border); border-radius: var(--ab-radius-md); text-align: center;">
            <div style="font-size: 2.2rem; margin-bottom: 12px; color: var(--ab-ochre);">✓</div>
            <h3 style="font-size: 1.4rem; margin-bottom: 8px;">Alpine Guild Inquiry Logged</h3>
            <p style="color: var(--ab-text-light-muted); font-size: 0.95rem; line-height: 1.6;">
              Thank you. Your bespoke merino wool anklet request has been received by our Denver guild concierge. We will contact you within 24 hours.
            </p>
          </div>
        `;
      }, 700);
    });
  }
});
