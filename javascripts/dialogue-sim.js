/* Andor's Trail dialogue simulator.
 * Mirrors controller/ConversationController.java:
 *  - a line with no text is a silent check: the first reply whose requirements are all met is taken;
 *  - a line with text shows it, then offers only the replies whose requirements are met ("N" = Next);
 *  - choosing a reply hands over items it requires with inventoryRemove / wearRemove;
 *  - reaching a line applies its effects (quest stages, items, faction, skills...);
 *  - targets X/S/F/R end the conversation (close / shop / fight / NPC leaves).
 * Requirement semantics follow canFulfillRequirement(); unknown types count as met, as in the game.
 */
(function () {
  'use strict';
  var SPECIAL = { X: 'The conversation ends.', S: 'The shop opens.', F: 'A fight starts!', R: 'The NPC leaves.' };

  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function fmt(s) { return String(s || '').replace(/\$playername/g, 'you').replace(/\{(\d+)\}/g, function (_, n) { return Number(n).toLocaleString(); }); }

  function Sim(root, data, npcName) {
    this.root = root; this.d = data; this.npc = npcName;
    this.atoms = this.collect();
    this.reset();
    this.build();
  }

  Sim.prototype.collect = function () {
    var A = { quests: {}, items: {}, wear: {}, kills: {}, faction: {}, skills: {}, counters: {}, flags: {} };
    var self = this;
    function addReq(q) {
      var t = q[0], id = q[1], v = q[2];
      if (t === 'questProgress' || t === 'questLatestProgress') (A.quests[id] = A.quests[id] || {})[v] = 1;
      else if (t === 'inventoryKeep' || t === 'inventoryRemove') A.items[id] = 1;
      else if (t === 'wear' || t === 'wearRemove') A.wear[id] = 1;
      else if (t === 'killedMonster') A.kills[id] = 1;
      else if (t === 'factionScore' || t === 'factionScoreEquals') A.faction[id] = 1;
      else if (t === 'skillLevel') A.skills[id] = 1;
      else if (t === 'usedItem' || t === 'spentGold' || t === 'consumedBonemeals') A.counters[t + ':' + id] = 1;
      else A.flags[self.flagKey(q)] = q;
    }
    Object.keys(this.d.nodes).forEach(function (k) {
      var n = self.d.nodes[k];
      n.r.forEach(function (r) { r[2].forEach(addReq); });
      n.w.forEach(function (w) {
        if (w[0] === 'questProgress' || w[0] === 'removeQuestProgress') (A.quests[w[1]] = A.quests[w[1]] || {})[w[2]] = 1;
        else if (w[0] === 'giveItem') A.items[w[1]] = 1;
        else if (w[0] === 'alignmentChange' || w[0] === 'alignmentSet') A.faction[w[1]] = 1;
        else if (w[0] === 'skillIncrease') A.skills[w[1]] = 1;
      });
    });
    return A;
  };
  Sim.prototype.flagKey = function (q) { return q[0] + '|' + q[1] + '|' + q[2]; };

  Sim.prototype.reset = function () {
    this.s = { quests: {}, items: {}, wear: {}, kills: {}, faction: {}, skills: {}, counters: {}, flags: {} };
  };

  // ------------------------------------------------------------------ names
  Sim.prototype.qName = function (id) { var q = this.d.q[id]; return q ? q[0] + (q[1] ? '' : ' (hidden flag)') : id; };
  Sim.prototype.iName = function (id) {
    if (id === 'gold') return 'gold';
    if (this.d.f[id]) return 'any of: ' + this.d.f[id].map(this.iName, this).join(', ');
    return this.d.i[id] || id;
  };
  Sim.prototype.mName = function (id) { return this.d.mo[id] || id; };
  Sim.prototype.skName = function (id) { return (this.d.sk && this.d.sk[id]) || id; };

  // ------------------------------------------------------------------ rules (canFulfillRequirement)
  Sim.prototype.has = function (q, v) { var s = this.s.quests[q]; return !!(s && s[v]); };
  Sim.prototype.count = function (id) { return Number(this.s.items[id] || 0); };
  Sim.prototype.ok = function (q) {
    var t = q[0], id = q[1], v = Number(q[2] || 0), r, self = this;
    switch (t) {
      case 'questProgress': r = this.has(id, v); break;
      case 'questLatestProgress':
        r = this.has(id, v) && !Object.keys(this.s.quests[id] || {}).some(function (k) { return self.s.quests[id][k] && Number(k) > v; }); break;
      case 'inventoryKeep': case 'inventoryRemove':
        r = this.d.f[id] ? this.d.f[id].some(function (i) { return self.count(i) >= v; }) : this.count(id) >= v; break;
      case 'wear': case 'wearRemove':
        r = this.d.f[id] ? this.d.f[id].some(function (i) { return self.s.wear[i]; }) : !!this.s.wear[id]; break;
      case 'killedMonster': r = Number(this.s.kills[id] || 0) >= v; break;
      case 'factionScore': r = Number(this.s.faction[id] || 0) >= v; break;
      case 'factionScoreEquals': r = Number(this.s.faction[id] || 0) === v; break;
      case 'skillLevel': r = Number(this.s.skills[id] || 0) >= v; break;
      case 'usedItem': case 'spentGold': case 'consumedBonemeals': r = Number(this.s.counters[t + ':' + id] || 0) >= v; break;
      case 'random': case 'timerElapsed': case 'hasActorCondition': case 'date': case 'dateEquals':
      case 'time': case 'timeEquals': case 'skillIncrease':
        r = !!this.s.flags[this.flagKey(q)]; break;
      default: r = true;
    }
    return q[3] ? !r : r;
  };
  Sim.prototype.reqText = function (q) {
    var t = q[0], id = q[1], v = q[2], no = q[3] ? 'NOT ' : '';
    switch (t) {
      case 'questProgress': return no + 'reached stage ' + v + ' of ' + this.qName(id);
      case 'questLatestProgress': return no + 'latest stage of ' + this.qName(id) + ' is ' + v;
      case 'inventoryKeep': return no + 'carrying ' + v + '× ' + this.iName(id);
      case 'inventoryRemove': return no + 'carrying ' + v + '× ' + this.iName(id) + ' (handed over)';
      case 'wear': return no + 'wearing ' + this.iName(id);
      case 'wearRemove': return no + 'wearing ' + this.iName(id) + ' (taken)';
      case 'killedMonster': return no + 'killed ' + v + '× ' + this.mName(id);
      case 'factionScore': return no + 'faction “' + id + '” ≥ ' + v;
      case 'factionScoreEquals': return no + 'faction “' + id + '” = ' + v;
      case 'skillLevel': return no + this.skName(id) + ' level ≥ ' + v;
      case 'random': return 'random chance (' + v + '%) succeeds';
      case 'timerElapsed': return no + v + ' rounds since timer “' + id + '”';
      case 'hasActorCondition': return no + 'affected by ' + id;
      case 'skillIncrease': return no + 'can still learn ' + this.skName(id);
      case 'usedItem': return no + 'used ' + v + '× ' + this.iName(id);
      case 'spentGold': return no + 'spent ' + v + ' gold in total';
      case 'consumedBonemeals': return no + 'eaten ' + v + '+ bonemeals';
      default: return no + t + ' ' + id + ' ' + v;
    }
  };

  // ------------------------------------------------------------------ effects
  Sim.prototype.payFor = function (reply) {
    var self = this, out = [];
    reply[2].forEach(function (q) {
      if (q[3]) return;
      var id = q[1], v = Number(q[2] || 0);
      if (q[0] === 'inventoryRemove') {
        var target = id;
        if (self.d.f[id]) target = self.d.f[id].filter(function (i) { return self.count(i) >= v; })[0] || id;
        self.s.items[target] = Math.max(0, self.count(target) - v);
        out.push('You hand over ' + v + '× ' + self.iName(target) + '.');
      } else if (q[0] === 'wearRemove') {
        var w = self.d.f[id] ? self.d.f[id].filter(function (i) { return self.s.wear[i]; })[0] : id;
        if (w) { self.s.wear[w] = false; out.push('You give up ' + self.iName(w) + '.'); }
      }
    });
    return out;
  };
  Sim.prototype.applyEffects = function (node) {
    var self = this, out = [];
    node.w.forEach(function (w) {
      var t = w[0], id = w[1], v = w[2];
      if (t === 'questProgress') {
        (self.s.quests[id] = self.s.quests[id] || {})[v] = true;
        var log = self.d.q[id] && self.d.q[id][2][String(v)];
        out.push('Quest “' + self.qName(id) + '”: stage ' + v + ' reached' + (log ? ' — “' + log + '”' : '') + '.');
      } else if (t === 'removeQuestProgress') {
        if (self.s.quests[id]) self.s.quests[id][v] = false;
        out.push('Quest “' + self.qName(id) + '”: stage ' + v + ' cleared.');
      } else if (t === 'giveItem') {
        self.s.items[id] = self.count(id) + Number(v || 1); out.push('You receive ' + (v || 1) + '× ' + self.iName(id) + '.');
      } else if (t === 'dropList') out.push('You receive loot (loot table “' + id + '”; contents can be random).');
      else if (t === 'skillIncrease') { self.s.skills[id] = Number(self.s.skills[id] || 0) + Number(v || 1); out.push('You learn ' + self.skName(id) + ' (+' + (v || 1) + ').'); }
      else if (t === 'alignmentChange') { self.s.faction[id] = Number(self.s.faction[id] || 0) + Number(v || 0); out.push('Faction “' + id + '” ' + (v >= 0 ? '+' : '') + v + '.'); }
      else if (t === 'alignmentSet') { self.s.faction[id] = Number(v || 0); out.push('Faction “' + id + '” set to ' + v + '.'); }
      else if (t === 'actorCondition') out.push('You are affected by ' + id + '.');
      else if (t === 'mapchange') out.push('You are moved to ' + (w[3] || id) + '.');
      else if (t === 'spawnAll') out.push('Monsters appear' + (w[3] ? ' on ' + w[3] : '') + '.');
      else if (t === 'removeSpawnArea' || t === 'deactivateSpawnArea') out.push('Monsters are removed' + (w[3] ? ' from ' + w[3] : '') + '.');
      else if (t === 'activateMapObjectGroup' || t === 'deactivateMapObjectGroup') out.push('The map changes' + (w[3] ? ' (' + w[3] + ')' : '') + '.');
      else if (t === 'createTimer') out.push('A timer “' + id + '” starts.');
      else if (t) out.push('Effect: ' + t + ' ' + (id || '') + '.');
    });
    return out;
  };

  // ------------------------------------------------------------------ conversation
  Sim.prototype.talk = function () { this.chat.innerHTML = ''; this.go(this.d.root, 0); };
  Sim.prototype.say = function (cls, text) { var p = el('div', 'ds-line ' + cls, text); this.chat.appendChild(p); return p; };
  Sim.prototype.effects = function (lines) {
    var self = this; lines.forEach(function (t) { self.say('ds-effect', t); });
    if (lines.length) this.renderState();
  };
  Sim.prototype.go = function (pid, hop) {
    if (hop > 60) { this.say('ds-sys', 'Stopped: the conversation loops.'); return; }
    if (SPECIAL[pid]) { this.say('ds-end', SPECIAL[pid]); return; }
    var n = this.d.nodes[pid];
    if (!n) { this.say('ds-end', pid ? 'Continues in a conversation outside this NPC’s data (' + pid + ').' : 'The conversation ends.'); return; }
    this.effects(this.applyEffects(n));
    var self = this;
    if (n.m == null) {                                    // silent check
      for (var i = 0; i < n.r.length; i++) {
        var r = n.r[i];
        if (r[2].every(function (q) { return self.ok(q); })) {
          this.say('ds-sys', 'Silent check: branch ' + (i + 1) + ' of ' + n.r.length + ' taken' +
            (r[2].length ? ' (' + r[2].map(this.reqText, this).join('; ') + ')' : ' (no conditions)') + '.');
          this.effects(this.payFor(r));
          return this.go(r[1], hop + 1);
        }
      }
      this.say('ds-end', 'No branch matched, so the conversation ends.'); return;
    }
    var who = n.n ? this.mName(n.n) : this.npc;
    var b = this.say('ds-npc', ''); b.appendChild(el('b', null, who + ': ')); b.appendChild(document.createTextNode(fmt(n.m)));
    if (!n.r.length) { this.say('ds-end', 'The conversation ends.'); return; }
    var box = el('div', 'ds-opts'); this.chat.appendChild(box);
    var shown = 0;
    n.r.forEach(function (r, i) {
      var avail = r[2].every(function (q) { return self.ok(q); });
      if (!avail && !self.showAll.checked) return;
      var label = r[0] === 'N' ? 'Next' : (r[0] ? fmt(r[0]) : '(continue)');
      var btn = el('button', 'ds-opt' + (avail ? '' : ' ds-locked'), label);
      if (!avail) {
        btn.disabled = true;
        var miss = r[2].filter(function (q) { return !self.ok(q); }).map(self.reqText, self);
        btn.title = 'Unavailable: ' + miss.join('; ');
        btn.appendChild(el('small', null, ' — needs: ' + miss.join('; ')));
      } else {
        shown++;
        btn.onclick = function () {
          box.querySelectorAll('button').forEach(function (x) { x.disabled = true; });
          btn.classList.add('ds-chosen');
          self.say('ds-you', label === 'Next' ? '…' : label);
          self.effects(self.payFor(r));
          self.go(r[1], hop + 1);
          self.chat.lastChild && self.chat.lastChild.scrollIntoView({ block: 'nearest' });
        };
      }
      box.appendChild(btn);
    });
    if (!shown) this.say('ds-end', 'No options are available in this situation, so the conversation ends here.');
  };

  // ------------------------------------------------------------------ situation panel
  Sim.prototype.build = function () {
    var self = this, R = this.root;
    R.innerHTML = '';
    var cols = el('div', 'ds-cols'); R.appendChild(cols);
    this.panel = el('div', 'ds-state'); cols.appendChild(this.panel);
    var right = el('div', 'ds-right'); cols.appendChild(right);
    var bar = el('div', 'ds-bar'); right.appendChild(bar);
    var talk = el('button', 'ds-talk', 'Talk to ' + this.npc); talk.onclick = function () { self.talk(); }; bar.appendChild(talk);
    var reset = el('button', 'ds-reset', 'Reset situation'); reset.onclick = function () { self.reset(); self.renderState(); self.talk(); }; bar.appendChild(reset);
    var lab = el('label', 'ds-showall'); this.showAll = el('input'); this.showAll.type = 'checkbox';
    this.showAll.onchange = function () { self.talk(); };
    lab.appendChild(this.showAll); lab.appendChild(document.createTextNode(' Show unavailable options (and why)')); bar.appendChild(lab);
    this.chat = el('div', 'ds-chat'); right.appendChild(this.chat);
    this.renderState();
    this.talk();
  };
  Sim.prototype.renderState = function () {
    var self = this, P = this.panel, A = this.atoms, S = this.s;
    P.innerHTML = '';
    P.appendChild(el('h4', null, 'Your situation'));
    P.appendChild(el('p', 'ds-hint', 'Only things this conversation actually checks are listed. Change them, then talk again.'));
    function group(title) { var g = el('details', 'ds-group'); g.open = true; g.appendChild(el('summary', null, title)); P.appendChild(g); return g; }
    function num(g, label, get, set) {
      var row = el('label', 'ds-row'); row.appendChild(el('span', null, label));
      var i = el('input'); i.type = 'number'; i.min = '-999'; i.value = get(); i.onchange = function () { set(Number(i.value || 0)); };
      row.appendChild(i); g.appendChild(row);
    }
    function chk(g, label, get, set, title) {
      var row = el('label', 'ds-row ds-chk'); var i = el('input'); i.type = 'checkbox'; i.checked = !!get();
      i.onchange = function () { set(i.checked); }; row.appendChild(i); row.appendChild(el('span', null, label));
      if (title) row.title = title; g.appendChild(row);
    }
    var qs = Object.keys(A.quests).sort(function (a, b) { return (self.d.q[b] ? self.d.q[b][1] : 0) - (self.d.q[a] ? self.d.q[a][1] : 0) || self.qName(a).localeCompare(self.qName(b)); });
    if (qs.length) {
      var g = group('Quest stages reached');
      qs.forEach(function (q) {
        var wrap = el('div', 'ds-quest'); var a = el('a', null, self.qName(q)); a.href = '../../quests/' + q + '/'; wrap.appendChild(a);
        var stages = Object.keys(A.quests[q]).map(Number).sort(function (x, y) { return x - y; });
        var line = el('div', 'ds-stages');
        stages.forEach(function (v) {
          var log = self.d.q[q] ? self.d.q[q][2][String(v)] : '';
          chk(line, String(v), function () { return S.quests[q] && S.quests[q][v]; },
              function (on) { (S.quests[q] = S.quests[q] || {})[v] = on; }, log || ('stage ' + v));
        });
        wrap.appendChild(line); g.appendChild(wrap);
      });
    }
    var items = Object.keys(A.items);
    if (items.length) { var gi = group('Items carried'); items.sort().forEach(function (id) { num(gi, self.iName(id), function () { return S.items[id] || 0; }, function (v) { S.items[id] = v; }); }); }
    var wear = Object.keys(A.wear);
    if (wear.length) { var gw = group('Wearing'); wear.forEach(function (id) {
      var ids = self.d.f[id] || [id];
      ids.forEach(function (x) { chk(gw, self.iName(x), function () { return S.wear[x]; }, function (on) { S.wear[x] = on; }); }); }); }
    var kills = Object.keys(A.kills);
    var dupe = function (ids, nameOf) { var c = {}; ids.forEach(function (i) { c[nameOf(i)] = (c[nameOf(i)] || 0) + 1; });
      return function (i) { return nameOf(i) + (c[nameOf(i)] > 1 ? ' (' + i + ')' : ''); }; };
    var killLabel = dupe(kills, function (i) { return self.mName(i); });
    if (kills.length) { var gk = group('Monsters killed'); kills.forEach(function (id) { num(gk, killLabel(id), function () { return S.kills[id] || 0; }, function (v) { S.kills[id] = v; }); }); }
    var fac = Object.keys(A.faction);
    if (fac.length) { var gf = group('Faction standing'); fac.forEach(function (id) { num(gf, id, function () { return S.faction[id] || 0; }, function (v) { S.faction[id] = v; }); }); }
    var sk = Object.keys(A.skills);
    if (sk.length) { var gs = group('Skill levels'); sk.forEach(function (id) { num(gs, self.skName(id), function () { return S.skills[id] || 0; }, function (v) { S.skills[id] = v; }); }); }
    var ct = Object.keys(A.counters);
    if (ct.length) { var gc = group('Statistics'); ct.forEach(function (k) {
      var p = k.split(':'); num(gc, p[0] === 'spentGold' ? 'gold spent (total)' : p[0] === 'consumedBonemeals' ? 'bonemeals eaten' : 'times used: ' + self.iName(p[1]),
        function () { return S.counters[k] || 0; }, function (v) { S.counters[k] = v; }); }); }
    var fl = Object.keys(A.flags);
    if (fl.length) { var gx = group('Other conditions'); fl.forEach(function (k) {
      var q = A.flags[k].slice(); q[3] = 0;
      chk(gx, self.reqText(q), function () { return S.flags[k]; }, function (on) { S.flags[k] = on; }); }); }
  };

  function init() {
    document.querySelectorAll('.dlg-sim[data-src]').forEach(function (root) {
      if (root.dataset.ready) return; root.dataset.ready = '1';
      root.textContent = 'Loading dialogue…';
      fetch(root.dataset.src).then(function (r) { return r.json(); })
        .then(function (data) { new Sim(root, data, root.dataset.npc || 'NPC'); })
        .catch(function () { root.textContent = 'Could not load the dialogue data.'; });
    });
  }
  if (window.document$ && window.document$.subscribe) window.document$.subscribe(init);
  else if (document.readyState !== 'loading') init(); else document.addEventListener('DOMContentLoaded', init);
})();
