(() => {
  const existing = document.getElementById('language-switcher-style');
  if (existing) return;

  const languages = [
    { code: 'en', label: 'English' },
    { code: 'pt-BR', label: 'Português' }
  ];

  const stored = typeof localStorage !== 'undefined' ? localStorage.getItem('preferredLanguage') : null;
  const browserLang = (navigator.language || 'pt-BR').toLowerCase();
  const initialCandidate = (stored || browserLang).toString();
  const initial = languages.find((lang) => lang.code.toLowerCase() === initialCandidate.toLowerCase())
    ? initialCandidate
    : (browserLang.startsWith('en') ? 'en' : 'pt-BR');

  const style = document.createElement('style');
  style.id = 'language-switcher-style';
  style.textContent = `
    .language-switcher{position:fixed;top:14px;right:14px;z-index:2000;font-family:inherit;}
    .language-toggle{display:inline-flex;align-items:center;gap:0.45rem;padding:0.55rem 0.75rem;border-radius:12px;border:1px solid #d7c8f5;background:#fff;box-shadow:0 10px 20px rgba(31,18,51,.12);color:#1c1233;font-weight:700;cursor:pointer;transition:box-shadow .12s ease, transform .08s ease;min-width:140px;justify-content:space-between;}
    .language-toggle:hover{box-shadow:0 14px 26px rgba(31,18,51,.16);transform:translateY(-1px);}
    .language-toggle:focus-visible{outline:3px solid rgba(102,0,153,.35);outline-offset:2px;}
    .language-toggle .lang-icon{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:8px;background:linear-gradient(135deg,#660099,#9d3bff);color:#fff;font-size:0.95rem;}
    .language-toggle .lang-label{flex:1;text-align:left;padding:0 0.35rem;font-size:0.95rem;}
    .language-toggle .lang-caret{font-size:0.9rem;color:#605c7a;}
    .language-menu{list-style:none;margin:0;padding:0.4rem 0;position:absolute;right:0;top:calc(100% + 6px);background:#fff;border:1px solid #d7c8f5;border-radius:12px;box-shadow:0 14px 32px rgba(31,18,51,.16);min-width:180px;display:none;}
    .language-switcher.open .language-menu{display:block;}
    .language-menu button{width:100%;border:0;background:transparent;padding:0.55rem 0.9rem;text-align:left;font-size:0.96rem;display:flex;align-items:center;gap:0.5rem;color:#1c1233;cursor:pointer;}
    .language-menu button:hover,.language-menu button:focus-visible{background:#f4e6ff;outline:none;}
    .language-menu .lang-dot{width:10px;height:10px;border-radius:50%;background:#d7c8f5;border:1px solid #b7a4e4;}
    .language-menu button[aria-selected="true"] .lang-dot{background:#660099;border-color:#660099;}
    @media (max-width: 640px){.language-switcher{top:10px;right:10px;}}
  `;
  document.head.appendChild(style);

  const container = document.createElement('div');
  container.className = 'language-switcher';

  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'language-toggle';
  button.setAttribute('aria-haspopup', 'listbox');
  button.setAttribute('aria-expanded', 'false');

  const icon = document.createElement('span');
  icon.className = 'lang-icon';
  icon.setAttribute('aria-hidden', 'true');
  icon.textContent = 'A·Z';

  const label = document.createElement('span');
  label.className = 'lang-label';

  const caret = document.createElement('span');
  caret.className = 'lang-caret';
  caret.setAttribute('aria-hidden', 'true');
  caret.textContent = '▾';

  button.append(icon, label, caret);

  const menu = document.createElement('ul');
  menu.className = 'language-menu';
  menu.setAttribute('role', 'listbox');

  const setLanguage = (code) => {
    const normalized = code === 'en' ? 'en' : 'pt-BR';
    document.documentElement.lang = normalized;
    try {
      localStorage.setItem('preferredLanguage', normalized);
    } catch (err) {
      // ignore storage failures
    }
    label.textContent = languages.find((lang) => lang.code === normalized)?.label || normalized;
    menu.querySelectorAll('button').forEach((btn) => {
      const selected = btn.dataset.lang === normalized;
      btn.setAttribute('aria-selected', selected ? 'true' : 'false');
    });
    container.classList.remove('open');
    button.setAttribute('aria-expanded', 'false');
  };

  languages.forEach((lang) => {
    const item = document.createElement('li');
    const option = document.createElement('button');
    option.type = 'button';
    option.dataset.lang = lang.code;
    option.setAttribute('role', 'option');
    option.innerHTML = `<span class="lang-dot" aria-hidden="true"></span><span>${lang.label}</span>`;
    option.addEventListener('click', () => setLanguage(lang.code));
    item.appendChild(option);
    menu.appendChild(item);
  });

  const toggleMenu = () => {
    const isOpen = container.classList.toggle('open');
    button.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    if (isOpen) {
      const selected = menu.querySelector('button[aria-selected="true"]');
      (selected || menu.querySelector('button'))?.focus({ preventScroll: true });
    }
  };

  button.addEventListener('click', toggleMenu);

  document.addEventListener('click', (event) => {
    if (!container.contains(event.target)) {
      container.classList.remove('open');
      button.setAttribute('aria-expanded', 'false');
    }
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      container.classList.remove('open');
      button.setAttribute('aria-expanded', 'false');
      button.focus({ preventScroll: true });
    }
  });

  container.append(button, menu);

  const target = document.querySelector('header') || document.body;
  target.appendChild(container);

  setLanguage(initial);
})();
