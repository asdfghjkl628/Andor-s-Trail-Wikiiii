/* Andor's Trail dialogue simulator.
 * Follows controller/ConversationController.java:
 *  - a line with no text is a silent check: the first branch whose requirements are all met is taken;
 *  - a line with text is shown with the replies whose requirements are met ("N" = Next);
 *  - choosing a reply hands over items required with inventoryRemove / wearRemove;
 *  - reaching a line applies its effects (journal, items, ...);
 *  - X / S / F / R end the conversation (close / shop / fight with the current speaker / NPC leaves);
 *  - switchToNPC hands the conversation (and any fight) to another character.
 * Nothing has to be set up in advance: whenever the game would check something the simulator doesn't know yet
 * (quest progress, items, kills, a dice roll...), it asks, and remembers the answer. Every answer and choice can be undone.
 */
(function () {
  'use strict';
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function fmt(s) { return String(s || '').replace(/\$playername/g, 'you').replace(/\{(\d+)\}/g, function (_, n) { return Number(n).toLocaleString(); }); }
  function cut(s, n) { s = fmt(s).replace(/\s+/g, ' ').trim(); return s.length <= n ? s : s.slice(0, n - 1).replace(/\s+\S*$/, '') + '…'; }

  function Sim(root, data, npcName, npcId) {
    this.root = root; this.d = data; this.npc = npcName; this.npcId = npcId;
    this.decisions = [];
    this.build();
    this.run();
  }

  // ------------------------------------------------------------------ names and plain-language conditions
  Sim.prototype.qName = function (id) { var q = this.d.q[id]; return q ? q[0] : id.replace(/_/g, ' '); };
  Sim.prototype.qLog = function (id, v) { var q = this.d.q[id]; return q && q[1] ? (q[2][String(v)] || '') : ''; };
  Sim.prototype.iName = function (id) {
    if (id === 'gold') return 'gold';
    if (this.d.f[id]) return 'one of: ' + this.d.f[id].map(this.iName, this).join(', ');
    return this.d.i[id] || id;
  };
  Sim.prototype.mName = function (id) { return this.d.mo[id] || id; };
  Sim.prototype.skName = function (id) { return (this.d.sk && this.d.sk[id]) || id; };
  Sim.prototype.cName = function (id) { return (this.d.c && this.d.c[id]) || id.replace(/_/g, ' '); };
  Sim.prototype.stageText = function (q, v) {
    var log = this.qLog(q, v);
    return log ? '“' + cut(log, 90) + '”' : 'step ' + v;
  };
  // one requirement, worded for a player; positive = whether to describe it as true (true) or as its opposite
  Sim.prototype.say1 = function (q, positive) {
    var t = q[0], id = q[1], v = q[2], neg = !!q[3] !== !positive;
    var Q = '<i>' + this.qName(id) + '</i>';
    switch (t) {
      case 'questProgress':
        return neg ? Q + ' has not reached ' + this.stageText(id, v) + ' yet' : Q + ': you have reached ' + this.stageText(id, v);
      case 'questLatestProgress':
        return Q + (neg ? ': your latest entry is not ' : ': your latest entry is ') + this.stageText(id, v);
      case 'inventoryKeep': return 'you ' + (neg ? "don't have " : 'have ') + (id === 'gold' ? Number(v).toLocaleString() + ' gold' : v + '× ' + this.iName(id));
      case 'inventoryRemove': return neg ? "you don't have " + (id === 'gold' ? Number(v).toLocaleString() + ' gold' : v + '× ' + this.iName(id))
        : (id === 'gold' ? 'you have ' + Number(v).toLocaleString() + ' gold (you pay it)' : 'you have ' + v + '× ' + this.iName(id) + ' (you hand it over)');
      case 'wear': return 'you are ' + (neg ? 'not ' : '') + 'wearing ' + this.iName(id);
      case 'wearRemove': return neg ? 'you are not wearing ' + this.iName(id) : 'you give up the ' + this.iName(id) + ' you are wearing';
      case 'killedMonster': return 'you have ' + (neg ? 'not yet ' : '') + 'killed ' + (Number(v) > 1 ? v + '× ' : '') + this.mName(id);
      case 'factionScore': return 'your standing with “' + id.replace(/_/g, ' ') + '” is ' + (neg ? 'below ' : 'at least ') + v;
      case 'factionScoreEquals': return 'the story counter “' + id.replace(/_/g, ' ') + '” is ' + (neg ? 'not ' : '') + v;
      case 'skillLevel': return 'your ' + this.skName(id) + ' is ' + (neg ? 'below level ' : 'level ') + v + (neg ? '' : '+');
      case 'skillIncrease': return 'you can ' + (neg ? 'no longer ' : 'still ') + 'learn ' + this.skName(id);
      case 'random': return neg ? 'the dice roll fails' : 'the dice roll succeeds (' + v + '% chance)';
      case 'timerElapsed':
        var mins = Math.round(Number(v) * 6 / 60), since = (this.d.tm && this.d.tm[id]) || 'an earlier event';
        return (neg ? 'less than ' : 'at least ') + v + ' rounds' + (mins >= 1 ? ' (about ' + mins + ' min outside combat)' : '') + ' have passed since ' + since;
      case 'hasActorCondition': return 'you are ' + (neg ? 'not ' : '') + 'affected by ' + this.cName(id);
      case 'usedItem': return 'you have ' + (neg ? 'not ' : '') + 'used ' + (Number(v) > 1 ? v + '× ' : '') + this.iName(id);
      case 'consumedBonemeals': return 'you have ' + (neg ? 'not ' : '') + 'used ' + v + '+ bonemeal potions';
      case 'spentGold': return 'you have ' + (neg ? 'not ' : '') + 'spent ' + Number(v).toLocaleString() + ' gold in total';
      case 'date': case 'dateEquals': case 'time': case 'timeEquals':
        return (neg ? 'not ' : '') + 'the right date or time on your device';
      default: return (neg ? 'not ' : '') + t + ' ' + (id || '') + ' ' + (v || '');
    }
  };
  Sim.prototype.sayAll = function (reqs) {
    var self = this;
    return reqs.map(function (q) { return self.say1(q, true); }).join(', and ');
  };

  // ------------------------------------------------------------------ state: facts learned from effects or from your answers
  Sim.prototype.key = function (q) { return q[0] === 'random' ? null : q[0].replace('inventoryRemove', 'inventoryKeep').replace('wearRemove', 'wear') + '|' + q[1] + '|' + q[2]; };
  Sim.prototype.val = function (q) {             // true / false / undefined (unknown), negate applied
    var t = q[0], id = q[1], v = Number(q[2] || 0), s = this.s, r;
    if (t === 'random') return undefined;
    if (t === 'questProgress' && s.stage[id] && v in s.stage[id]) r = s.stage[id][v];
    else if (t === 'questLatestProgress' && s.latest[id] != null) r = s.latest[id] === v;
    else if ((t === 'factionScore' || t === 'factionScoreEquals') && s.fac[id] != null) r = t === 'factionScore' ? s.fac[id] >= v : s.fac[id] === v;
    else { var k = this.key(q); if (k in s.facts) r = s.facts[k]; }
    if (r === undefined) return undefined;
    return q[3] ? !r : r;
  };
  Sim.prototype.assume = function (q, truth) {   // record that requirement q evaluated to `truth`
    if (q[0] === 'random') return;
    var raw = q[3] ? !truth : truth, id = q[1], v = Number(q[2] || 0);
    if (q[0] === 'questProgress') { (this.s.stage[id] = this.s.stage[id] || {})[v] = raw; }
    else if (q[0] === 'questLatestProgress') { if (raw) this.s.latest[id] = v; }
    else this.s.facts[this.key(q)] = raw;
    var label = this.say1(q, truth);
    if (this.s.assumed.indexOf(label) < 0) this.s.assumed.push(label);
  };
  Sim.prototype.evalReqs = function (reqs) {     // {state: 'yes'|'no'|'ask', unknown: [...]}
    var unknown = [];
    for (var i = 0; i < reqs.length; i++) {
      var r = this.val(reqs[i]);
      if (r === false) return { state: 'no', unknown: [] };
      if (r === undefined) unknown.push(reqs[i]);
    }
    return { state: unknown.length ? 'ask' : 'yes', unknown: unknown };
  };
  Sim.prototype.payFor = function (reply) {
    var self = this;
    reply[2].forEach(function (q) {
      if (q[3]) return;
      if (q[0] === 'inventoryRemove') {
        delete self.s.facts[self.key(q)];
        self.say('ds-effect', q[1] === 'gold' ? 'You pay ' + Number(q[2]).toLocaleString() + ' gold.' : 'You hand over ' + q[2] + '× ' + self.iName(q[1]) + '.');
      } else if (q[0] === 'wearRemove') {
        self.s.facts[self.key(q)] = false; self.say('ds-effect', 'You give up ' + self.iName(q[1]) + '.');
      }
    });
  };
  Sim.prototype.applyEffects = function (node) {
    var self = this, s = this.s;
    node.w.forEach(function (w) {
      var t = w[0], id = w[1], v = w[2], hidden = self.d.q[id] && !self.d.q[id][1];
      if (t === 'questProgress') {
        (s.stage[id] = s.stage[id] || {})[v] = true; s.latest[id] = Number(v);
        var log = self.qLog(id, v);
        if (log) self.say('ds-effect ds-journal', '📖 ' + self.qName(id) + ': “' + fmt(log) + '”');
      } else if (t === 'removeQuestProgress') { (s.stage[id] = s.stage[id] || {})[v] = false; }
      else if (t === 'giveItem') {
        Object.keys(s.facts).forEach(function (k) { if (k.indexOf('inventoryKeep|' + id + '|') === 0) delete s.facts[k]; });
        s.facts['inventoryKeep|' + id + '|' + (v || 1)] = true;
        self.say('ds-effect', 'You receive ' + (id === 'gold' ? Number(v).toLocaleString() + ' gold' : (v || 1) + '× ' + self.iName(id)) + '.');
      } else if (t === 'dropList') self.say('ds-effect', 'You receive a reward (random loot).');
      else if (t === 'skillIncrease') self.say('ds-effect', 'You learn ' + self.skName(id) + '.');
      else if (t === 'alignmentChange') { if (s.fac[id] != null) s.fac[id] += Number(v || 0); }
      else if (t === 'alignmentSet') s.fac[id] = Number(v || 0);
      else if (t === 'actorCondition') self.say('ds-effect', Number(v) === -99 ? 'You are cured of ' + self.cName(id) + '.' : 'You are affected by ' + self.cName(id) + '.');
      else if (t === 'mapchange') self.say('ds-effect', 'You are moved elsewhere.');
      else if (t === 'spawnAll') self.say('ds-effect', 'Something appears nearby.');
      else if (t === 'removeSpawnArea' || t === 'deactivateSpawnArea') self.say('ds-effect', 'Someone leaves the area.');
      else if (t === 'createTimer') s.facts['timer:' + id] = true;
    });
  };

  // ------------------------------------------------------------------ running the conversation (replayed from your recorded decisions)
  Sim.prototype.reset = function () { this.s = { stage: {}, latest: {}, fac: {}, facts: {}, assumed: [] }; this.k = 0; this.speaker = this.npc; };
  Sim.prototype.say = function (cls, text, html) { var p = el('div', 'ds-line ' + cls); if (html) p.innerHTML = text; else p.textContent = text; this.chat.appendChild(p); return p; };
  Sim.prototype.next = function () { return this.k < this.decisions.length ? this.decisions[this.k++] : null; };
  Sim.prototype.run = function () {
    this.reset(); this.chat.innerHTML = '';
    var pid = this.d.root, hop = 0;
    while (pid != null && hop++ < 80) pid = this.step(pid);
    if (hop >= 80) this.say('ds-sys', 'Stopped: the conversation loops.');
    this.undoBtn.disabled = !this.decisions.length;
    this.renderAssumed();
    var last = this.chat.lastChild; if (last && this.decisions.length) last.scrollIntoView({ block: 'nearest' });
  };
  // returns the next phrase id, or null when the conversation stops (ended, or waiting for you)
  Sim.prototype.step = function (pid) {
    var self = this;
    if (pid === 'X' || pid === '' ) { this.say('ds-end', 'The conversation ends.'); return null; }
    if (pid === 'S') { this.say('ds-end', this.speaker + '’s shop opens.'); return null; }
    if (pid === 'F') { this.say('ds-end ds-fight', '⚔ A fight with ' + this.speaker + ' starts!'); return null; }
    if (pid === 'R') { this.say('ds-end', this.speaker + ' leaves.'); return null; }
    var n = this.d.nodes[pid];
    if (!n) { this.say('ds-end', 'The conversation continues elsewhere.'); return null; }
    if (n.n) this.speaker = this.mName(n.n);
    this.applyEffects(n);
    if (n.m == null) return this.silent(n);
    var b = this.say('ds-npc', ''); b.appendChild(el('b', null, this.speaker + ': ')); b.appendChild(document.createTextNode(fmt(n.m)));
    if (!n.r.length) { this.say('ds-end', 'The conversation ends.'); return null; }
    var opts = [];
    n.r.forEach(function (r, i) { var e = self.evalReqs(r[2]); if (e.state !== 'no') opts.push({ r: r, i: i, e: e }); });
    if (!opts.length) { this.say('ds-end', 'You have nothing to answer here, so the conversation ends.'); return null; }
    var d = this.next(), o = d && opts.filter(function (x) { return x.i === d.i; })[0];
    if (d && !o) this.decisions.length = this.k - 1;  // a recorded choice that no longer applies: ask again
    if (o) {                                         // replay a recorded choice
      o.e.unknown.forEach(function (q) { self.assume(q, true); });
      var label = o.r[0] === 'N' ? '…' : (o.r[0] ? fmt(o.r[0]) : '…');
      this.say('ds-you', label);
      this.payFor(o.r);
      return o.r[1];
    }
    var box = el('div', 'ds-opts'); this.chat.appendChild(box);
    opts.forEach(function (o) {
      var label = o.r[0] === 'N' ? 'Next' : (o.r[0] ? fmt(o.r[0]) : '(continue)');
      var btn = el('button', 'ds-opt', label);
      if (o.e.state === 'ask') btn.appendChild(el('small', 'ds-if', 'only if ' + o.e.unknown.map(function (q) { return self.say1(q, true); }).join(', and ').replace(/<\/?i>/g, '')));
      btn.onclick = function () { self.decisions.push({ i: o.i }); self.run(); };
      box.appendChild(btn);
    });
    return null;
  };
  // silent check: take the first branch that applies; ask you when it depends on something unknown
  Sim.prototype.silent = function (n) {
    var self = this, cands = [];
    for (var i = 0; i < n.r.length; i++) {
      var e = this.evalReqs(n.r[i][2]);
      if (e.state === 'no') continue;
      cands.push({ r: n.r[i], i: i, e: e });
      if (e.state === 'yes') break;
    }
    if (!cands.length) { this.say('ds-end', 'Nothing more to say right now; the conversation ends.'); return null; }
    var take = function (c) {
      cands.forEach(function (o) {                 // branches before the one taken did not apply
        if (o === c) return;
        if (o.e.unknown.length === 1) self.assume(o.e.unknown[0], false);
      });
      c.e.unknown.forEach(function (q) { self.assume(q, true); });
      self.payFor(c.r);
      return c.r[1];
    };
    var open = cands[cands.length - 1].e.state === 'ask';   // no default branch: if nothing applies, the conversation ends
    if (cands.length === 1 && !open) return take(cands[0]);
    var d = this.next();
    if (d) {
      if (d.i === -1 && open) { cands.forEach(function (o) { if (o.e.unknown.length === 1) self.assume(o.e.unknown[0], false); });
        this.say('ds-end', this.speaker + ' has nothing to say to you right now.'); return null; }
      var c = cands.filter(function (x) { return x.i === d.i; })[0]; if (c) return take(c); this.decisions.length = this.k - 1;
    }
    var q = el('div', 'ds-ask'); this.chat.appendChild(q);
    q.appendChild(el('div', 'ds-asktitle', 'What happens next depends on your game. Which is true for you?'));
    if (cands.length > 2) q.appendChild(el('div', 'ds-hint', 'If more than one is true, pick the first one: the game checks them in this order.'));
    cands.forEach(function (c, j) {
      var txt = c.e.state === 'yes' && j === cands.length - 1 && cands.length > 1 ? 'None of the above' : self.sayAll(c.e.unknown);
      var btn = el('button', 'ds-opt ds-choice'); btn.innerHTML = txt.charAt(0).toUpperCase() + txt.slice(1);
      btn.onclick = function () { self.decisions.push({ i: c.i }); self.run(); };
      q.appendChild(btn);
    });
    if (open) { var nb = el('button', 'ds-opt ds-choice', 'None of these'); nb.onclick = function () { self.decisions.push({ i: -1 }); self.run(); }; q.appendChild(nb); }
    return null;
  };
  Sim.prototype.renderAssumed = function () {
    var a = this.s.assumed;
    this.assumedBox.innerHTML = '';
    if (!a.length) { this.assumedBox.style.display = 'none'; return; }
    this.assumedBox.style.display = '';
    var det = el('details'); det.appendChild(el('summary', null, 'Your answers so far (' + a.length + ')'));
    var ul = el('ul'); a.forEach(function (t) { var li = el('li'); li.innerHTML = t.charAt(0).toUpperCase() + t.slice(1); ul.appendChild(li); });
    det.appendChild(ul); this.assumedBox.appendChild(det);
  };

  Sim.prototype.build = function () {
    var self = this, R = this.root;
    R.innerHTML = '';
    var bar = el('div', 'ds-bar'); R.appendChild(bar);
    this.undoBtn = el('button', 'ds-undo', '↶ Undo'); this.undoBtn.onclick = function () { self.decisions.pop(); self.run(); }; bar.appendChild(this.undoBtn);
    var restart = el('button', 'ds-reset', '⟲ Start over'); restart.onclick = function () { self.decisions = []; self.run(); }; bar.appendChild(restart);
    this.assumedBox = el('div', 'ds-assumed'); R.appendChild(this.assumedBox);
    this.chat = el('div', 'ds-chat'); R.appendChild(this.chat);
  };

  function init() {
    document.querySelectorAll('.dlg-sim[data-src]').forEach(function (root) {
      if (root.dataset.ready) return; root.dataset.ready = '1';
      root.textContent = 'Loading dialogue…';
      fetch(root.dataset.src).then(function (r) { return r.json(); })
        .then(function (data) { new Sim(root, data, root.dataset.npc || 'NPC', root.dataset.id); })
        .catch(function () { root.textContent = 'Could not load the dialogue data.'; });
    });
  }
  if (window.document$ && window.document$.subscribe) window.document$.subscribe(init);
  else if (document.readyState !== 'loading') init(); else document.addEventListener('DOMContentLoaded', init);
})();
