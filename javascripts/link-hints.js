// Hover hints for wiki links: "Way of the Monk (skill)", "Gison (NPC)", "Antidote (item)" and so on.
// The kind comes from the link's address; characters are looked up in assets/linkinfo.json (enemy / NPC / NPC/enemy).
(function () {
  var KIND = { items: 'item', skills: 'skill', quests: 'quest', maps: 'location', conditions: 'condition', versions: 'game version', strategy: 'strategy guide' };
  var chars = null, loading = false;

  function siteRoot() {
    // every page loads this script from <root>/javascripts/link-hints.js
    var s = document.querySelector('script[src*="javascripts/link-hints.js"]');
    return s ? s.src.replace(/javascripts\/link-hints\.js.*$/, '') : null;
  }
  function loadChars() {
    if (chars || loading) return;
    var root = siteRoot();
    if (!root || !window.fetch) return;
    loading = true;
    fetch(root + 'assets/linkinfo.json').then(function (r) { return r.json(); })
      .then(function (d) { chars = d; }).catch(function () { chars = {}; });
  }

  function hint(a) {
    var root = siteRoot();
    if (!root || a.href.indexOf(root) !== 0) return null;
    var rest = a.href.slice(root.length).split('#'), path = rest[0], hash = rest[1] || '';
    var parts = path.split('/').filter(Boolean);
    if (!parts.length) return null;
    var section = parts[0], id = parts[1];
    var kind;
    if (section === 'skills' && id === 'stats') kind = 'stat';
    else if (section === 'monsters' && id && id !== 'index') kind = (chars && chars[id]) || 'character';
    else if (KIND[section] && id && id !== 'index' && !(section === 'skills' && id === 'calculator')) kind = KIND[section];
    else return null;
    if (section === 'quests') { var m = hash.match(/^stage-(\d+)/); if (m) kind += ', stage ' + m[1]; }
    return kind;
  }

  document.addEventListener('mouseover', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a || a.getAttribute('href').charAt(0) === '#') return;
    if (a.hasAttribute('title') && !a.dataset.hint) return;        // keep titles written by the page itself
    if (a.dataset.hint === 'done') return;
    var kind = hint(a);
    if (!kind) { a.dataset.hint = 'done'; return; }
    var text = (a.textContent || '').replace(/\s+/g, ' ').trim();
    if (!text) { var img = a.querySelector('img[alt]'); text = img ? img.alt : ''; }
    a.title = text ? text + ' (' + kind + ')' : kind.charAt(0).toUpperCase() + kind.slice(1);
    // a character's type may still be loading: try again on the next hover
    a.dataset.hint = (kind === 'character' && !chars) ? 'pending' : 'done';
  });
  function init() { if (document.querySelector('a[href*="monsters/"]')) loadChars(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
