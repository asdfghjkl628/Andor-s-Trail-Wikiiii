/* Andor's Trail build calculator.
 * Stat pipeline ported from the game (ActorStatsController.recalculatePlayerStats):
 *   reset to base traits (incl. level-ups) -> ItemController.applyInventoryEffects
 *     (main weapon sets attack cost & crit multiplier; weapon; shield/off-hand; fighting styles; armor & jewelry; proficiencies)
 *   -> SkillController.applySkillEffects -> ItemController.applyDamageModifier -> caps.
 * Active conditions (potions, curses) are not simulated.
 */
(function () {
  'use strict';
  var D, C;   // data, constants
  var f32 = Math.fround;
  function pct(v, pos, neg) {                 // SkillController.getPercentage(int,...)
    if (v === 0) return 0;
    return Math.floor(f32((v * (v > 0 ? pos : neg)) / 100));
  }
  function pctF(v, pos, neg) { if (v === 0) return 0; return f32(f32(v * (v > 0 ? pos : neg)) / 100); }
  function K(name) { return C[name] || 0; }

  // ------------------------------------------------------------------ base traits & level-ups
  function fortitudeBonus(b) {
    var n = b.skills.fortitude || 0, total = 0;
    for (var k = 1; k <= n; k++) {
      var at = (b.fortAt && b.fortAt[k - 1]) || D.fortEarliest(k);
      total += Math.max(0, b.level - at) * D.lv.fort;
    }
    return total;
  }
  function baseTraits(b) {
    var B = D.base, p = b.picks;
    return {
      maxHP: B.maxHP + p.hp * D.lv.hp + fortitudeBonus(b), maxAP: B.maxAP,
      attackChance: B.attackChance + p.ac * D.lv.ac, dmin: B.dmin + p.dmg * D.lv.dmg, dmax: B.dmax + p.dmg * D.lv.dmg,
      blockChance: B.blockChance + p.bc * D.lv.bc, damageResistance: B.damageResistance,
      moveCost: B.moveCost, attackCost: B.attackCost, useItemCost: B.useItemCost, reequipCost: B.reequipCost,
      criticalSkill: B.criticalSkill, criticalMultiplier: B.criticalMultiplier
    };
  }

  // ------------------------------------------------------------------ the pipeline
  function compute(b) {
    var s = baseTraits(b), wd = { min: 0, max: 0 }, lv = function (id) { return b.skills[id] || 0; };
    var item = function (slot) { var id = b.eq[slot]; return id ? D.items[id] : null; };
    var cat = function (it) { return D.cats[it.cat] || {}; };
    var isWeapon = function (it) { return !!(it && cat(it).slot === 'weapon'); };
    var isShield = function (it) { return !!(it && cat(it).slot === 'shield'); };
    var isTwoHand = function (it) { return isWeapon(it) && cat(it).size === 'large'; };
    var st = function (it) { return (it && it.s) || null; };
    var weight = function (slot) { var it = item(slot); return !!(it && cat(it).size && cat(it).size !== 'none'); };
    var unarmored = function () { return !['head', 'body', 'hand', 'feet'].some(weight); };
    var profLevel = function (it) { var p = cat(it).prof; return p ? lv(p) : 0; };
    var main = item('weapon'), off = item('shield');
    var dual = !!(main && off && isWeapon(main) && isWeapon(off));
    var addAtkCost = function (a) { if (!a) return; s.attackCost += a; if (s.attackCost <= 0) s.attackCost = 1; };
    var addMoveCost = function (a) { if (!a) return; s.moveCost += a; if (s.moveCost <= 0) s.moveCost = 1; };
    function applyAbility(x, it) {            // ActorStatsController.applyAbilityEffects
      if (!x) return;
      s.maxHP += x.hp; s.maxAP += x.ap; addMoveCost(x.mv); addAtkCost(x.atk);
      if (x.re) { s.reequipCost += x.re; if (s.reequipCost < 0) s.reequipCost = 0; }
      if (x.use) { s.useItemCost += x.use; if (s.useItemCost < 0) s.useItemCost = 0; }
      s.attackChance += x.ac; s.criticalSkill += x.cs; s.dmin += x.dmin; s.dmax += x.dmax;
      s.blockChance += x.bc; s.damageResistance += x.dr;
      if (isWeapon(it)) { wd.min += x.dmin; wd.max += x.dmax; }
    }
    function applySlot(slot) {
      var it = item(slot); if (!it) return;
      if (slot === 'shield' && dual) return;   // off-hand weapon stats are blended in by the fighting style
      applyAbility(st(it), it);
    }
    var addPAC = function (it, p, n) { if (st(it)) s.attackChance += pct(st(it).ac, p, n); };
    var addPBC = function (it, p, n) { if (st(it)) s.blockChance += pct(st(it).bc, p, n); };
    var addPCS = function (it, p, n) { if (st(it)) s.criticalSkill += pct(st(it).cs, p, n); };
    function addPDmg(it, p, n) {
      if (!st(it)) return;
      var mx = pct(st(it).dmax, p, n), mn = pct(st(it).dmin, p, n);
      s.dmax += mx; s.dmin = Math.min(s.dmin + mn, s.dmax);
      if (isWeapon(it)) { wd.max += mx; wd.min = Math.min(wd.min + mn, wd.max); }
    }

    // ---- ItemController.applyInventoryEffects
    var mainWeapon = main || (isWeapon(off) ? off : null);
    if (mainWeapon) { s.attackCost = 0; s.criticalMultiplier = st(mainWeapon) ? st(mainWeapon).cm : 0; }
    applySlot('weapon'); applySlot('shield');
    // -- SkillController.applySkillEffectsFromFightingStyles
    var monk = lv('fightstyleUnarmedUnarmored');
    if (monk > 0 && unarmored() && !main && !off) {
      s.blockChance += K('PER_SKILLPOINT_INCREASE_UNARMED_UNARMORED_BC') * monk;
      s.damageResistance += K('PER_SKILLPOINT_INCREASE_UNARMED_UNARMORED_DR') * monk;
      s.attackChance += K('PER_SKILLPOINT_INCREASE_UNARMED_UNARMORED_AC') * monk;
      s.dmax += K('PER_SKILLPOINT_INCREASE_UNARMED_UNARMORED_DMG_MAX') * monk;
      s.criticalMultiplier = f32(1 + f32(K('PER_SKILLPOINT_INCREASE_UNARMED_UNARMORED_CM_PERCENT') / 100) * monk);
    }
    if (main && !off && isTwoHand(main)) {
      addPDmg(main, lv('fightstyle2hand') * K('PER_SKILLPOINT_INCREASE_FIGHTSTYLE_2HAND_DMG_PERCENT'), 0);
      addPDmg(main, lv('specialization2hand') * K('PER_SKILLPOINT_INCREASE_SPECIALIZATION_2HAND_DMG_PERCENT'), 0);
      addPAC(main, lv('specialization2hand') * K('PER_SKILLPOINT_INCREASE_SPECIALIZATION_2HAND_AC_PERCENT'), 0);
    }
    if (main && off && isWeapon(main) && isShield(off)) {
      var fs = lv('fightstyleWeaponShield'), sp = lv('specializationWeaponShield');
      addPAC(main, fs * K('PER_SKILLPOINT_INCREASE_FIGHTSTYLE_WEAPON_AC_PERCENT'), 0);
      addPBC(off, fs * K('PER_SKILLPOINT_INCREASE_FIGHTSTYLE_SHIELD_BC_PERCENT'), 0);
      addPAC(main, sp * K('PER_SKILLPOINT_INCREASE_SPECIALIZATION_WEAPON_AC_PERCENT'), 0);
      addPDmg(main, sp * K('PER_SKILLPOINT_INCREASE_SPECIALIZATION_WEAPON_DMG_PERCENT'), 0);
    }
    if (dual) {
      var dw = lv('fightstyleDualWield'), percent;
      if (st(off)) {
        var am = st(main) ? st(main).atk : 0, ao = st(off).atk, cmM = st(main) ? st(main).cm : 0, cmO = st(off).cm;
        if (dw === 2) { percent = K('DUALWIELD_EFFICIENCY_LEVEL2'); s.attackCost = Math.max(am, ao); s.criticalMultiplier = Math.max(cmM, pctF(cmO, percent, 0)); }
        else if (dw === 1) { percent = K('DUALWIELD_EFFICIENCY_LEVEL1'); s.attackCost = Math.max(am, ao) + pct(Math.min(am, ao), K('DUALWIELD_LEVEL1_OFFHAND_AP_COST_PERCENT'), 0); s.criticalMultiplier = Math.max(cmM, pctF(cmO, percent, 0)); }
        else { percent = K('DUALWIELD_EFFICIENCY_LEVEL0'); s.attackCost = am + ao; s.criticalMultiplier = Math.max(cmM, pctF(cmO, percent, 0)); }
        var pl = profLevel(off);
        addPAC(off, pct(K('PER_SKILLPOINT_INCREASE_WEAPON_PROF_AC_PERCENT') * pl, percent, 0), 0);
        addPBC(off, pct(K('PER_SKILLPOINT_INCREASE_WEAPON_PROF_BC_PERCENT') * pl, percent, 0), 0);
        addPCS(off, pct(K('PER_SKILLPOINT_INCREASE_WEAPON_PROF_CS_PERCENT') * pl, percent, 0), 0);
        addPAC(off, percent, 100); addPBC(off, percent, 100); addPDmg(off, percent, 100); addPCS(off, percent, 100);
        s.maxHP += pct(st(off).hp, percent, 100); s.damageResistance += pct(st(off).dr, percent, 100); s.maxAP += pct(st(off).ap, percent, 100);
        s.moveCost += pct(st(off).mv, 100, percent); s.reequipCost += pct(st(off).re, 100, percent); s.useItemCost += pct(st(off).use, 100, percent);
      }
      var sd = lv('specializationDualWield');
      addPAC(main, sd * K('PER_SKILLPOINT_INCREASE_SPECIALIZATION_DUALWIELD_AC_PERCENT'), 0); addPBC(main, sd * K('PER_SKILLPOINT_INCREASE_SPECIALIZATION_DUALWIELD_BC_PERCENT'), 0);
      addPAC(off, sd * K('PER_SKILLPOINT_INCREASE_SPECIALIZATION_DUALWIELD_AC_PERCENT'), 0); addPBC(off, sd * K('PER_SKILLPOINT_INCREASE_SPECIALIZATION_DUALWIELD_BC_PERCENT'), 0);
    }
    ['head', 'body', 'hand', 'feet', 'neck', 'leftring', 'rightring'].forEach(applySlot);
    // -- SkillController.applySkillEffectsFromItemProficiencies
    if (mainWeapon) {
      var wl = profLevel(mainWeapon);
      addPAC(mainWeapon, K('PER_SKILLPOINT_INCREASE_WEAPON_PROF_AC_PERCENT') * wl, 0);
      addPBC(mainWeapon, K('PER_SKILLPOINT_INCREASE_WEAPON_PROF_BC_PERCENT') * wl, 0);
      addPCS(mainWeapon, K('PER_SKILLPOINT_INCREASE_WEAPON_PROF_CS_PERCENT') * wl, 0);
    }
    var ua = lv('weaponProficiencyUnarmed');
    if (ua > 0 && !weight('weapon') && !weight('shield')) {
      s.attackChance += K('PER_SKILLPOINT_INCREASE_UNARMED_AC') * ua;
      s.dmax += K('PER_SKILLPOINT_INCREASE_UNARMED_DMG') * ua; s.dmin = Math.min(s.dmin + K('PER_SKILLPOINT_INCREASE_UNARMED_DMG') * ua, s.dmax);
      s.blockChance += K('PER_SKILLPOINT_INCREASE_UNARMED_BC') * ua;
    }
    if (isShield(off)) s.damageResistance += K('PER_SKILLPOINT_INCREASE_SHIELD_PROF_DR') * profLevel(off);
    var uarm = lv('armorProficiencyUnarmored');
    if (uarm > 0 && unarmored()) s.blockChance += K('PER_SKILLPOINT_INCREASE_UNARMORED_BC') * uarm;
    var la = lv('armorProficiencyLight'), ha = lv('armorProficiencyHeavy');
    ['head', 'body', 'hand', 'feet'].forEach(function (slot) {
      var it = item(slot); if (!it || !st(it)) return;
      var p = cat(it).prof;
      if (p === 'armorProficiencyLight' && la > 0) addPBC(it, K('PER_SKILLPOINT_INCREASE_LIGHT_ARMOR_BC_PERCENT') * la, 0);
      else if (p === 'armorProficiencyHeavy' && ha > 0) {
        addPBC(it, K('PER_SKILLPOINT_INCREASE_HEAVY_ARMOR_BC_PERCENT') * ha, 0);
        s.moveCost -= pct(st(it).mv, K('PER_SKILLPOINT_INCREASE_HEAVY_ARMOR_MOVECOST_PERCENT') * ha, 0);
        s.attackCost -= pct(st(it).atk, K('PER_SKILLPOINT_INCREASE_HEAVY_ARMOR_ATKCOST_PERCENT') * ha, 0);
        s.useItemCost -= pct(st(it).use, K('PER_SKILLPOINT_INCREASE_HEAVY_ARMOR_USECOST_PERCENT') * ha, 0);
      }
    });
    // ---- SkillController.applySkillEffects
    s.attackChance += K('PER_SKILLPOINT_INCREASE_WEAPON_CHANCE') * lv('weaponChance');
    s.dmax += K('PER_SKILLPOINT_INCREASE_WEAPON_DAMAGE_MAX') * lv('weaponDmg');
    s.dmin = Math.min(s.dmin + K('PER_SKILLPOINT_INCREASE_WEAPON_DAMAGE_MIN') * lv('weaponDmg'), s.dmax);
    s.blockChance += K('PER_SKILLPOINT_INCREASE_DODGE') * lv('dodge');
    s.damageResistance += K('PER_SKILLPOINT_INCREASE_BARKSKIN') * lv('barkSkin');
    if (s.criticalSkill !== 0 && s.criticalSkill > 0)
      s.criticalSkill += Math.trunc(s.criticalSkill * K('PER_SKILLPOINT_INCREASE_MORE_CRITICALS_PERCENT') * lv('moreCriticals') / 100);
    if (s.criticalMultiplier !== 0 && s.criticalMultiplier !== 1)
      s.criticalMultiplier = f32(s.criticalMultiplier + f32(f32(f32(s.criticalMultiplier * K('PER_SKILLPOINT_INCREASE_BETTER_CRITICALS_PERCENT')) * lv('betterCriticals')) / 100));
    s.maxAP += K('PER_SKILLPOINT_INCREASE_SPEED') * lv('speed');
    // ---- ItemController.applyDamageModifier (scales non-weapon damage only)
    var m1 = main && st(main) ? st(main).nwdm : -1, m2 = (off && isWeapon(off) && st(off)) ? st(off).nwdm : -1, mod = 100;
    if (m1 >= 0 && m2 >= 0) mod = lv('fightstyleDualWield') === 2 ? Math.max(m1, m2) : lv('fightstyleDualWield') === 1 ? Math.trunc((m1 + m2) / 2) : Math.min(m1, m2);
    else if (m1 <= 0 && m2 >= 0) mod = m2;
    else if (m2 <= 0 && m1 >= 0) mod = m1;
    if (mod !== 100) {
      var f = f32((mod - 100) / 100);
      s.dmin += Math.round(f32((s.dmin - wd.min) * f)); s.dmax += Math.round(f32((s.dmax - wd.max) * f));
    }
    // ---- caps
    if (s.attackChance < 0) s.attackChance = 0;
    if (s.dmax < 0) { s.dmax = 0; s.dmin = 0; }
    s.weaponDamage = wd; s.nonWeaponDamageModifier = mod;
    s.critChance = critChance(s.criticalSkill);
    s.canCrit = s.criticalSkill !== 0 && s.criticalMultiplier !== 0 && s.criticalMultiplier !== 1;
    s.attacksPerTurn = s.attackCost > 0 ? Math.floor(s.maxAP / s.attackCost) : 0;
    s.wield = !main && !off ? 'unarmed' : dual ? 'dual wield' : (main && !off && isTwoHand(main)) ? 'two-handed' : (main && isShield(off)) ? 'weapon & shield' : 'one-handed';
    return s;
  }
  function critChance(cs) { if (cs <= 0) return 0; var v = Math.trunc(-5 + 2 * Math.sqrt(5 * cs)); return v < 0 ? 0 : v; }

  // ------------------------------------------------------------------ combat (CombatController)
  function hitChance(ac, bc) { return Math.trunc(50 * (1 + f32(2 / Math.PI) * f32(Math.atan(f32((ac - bc - 50) / 40))))); }
  function avgPerHit(a, t) {
    var n = a.dmax - a.dmin + 1, nc = 0, cr = 0, cc = (a.canCrit && !t.immune) ? a.critChance : 0;
    if (n < 1) n = 1;
    for (var i = 0; i < n; i++) nc += Math.max(0, i + a.dmin - t.damageResistance) / n;
    if (cc > 0) for (var j = 0; j < n; j++) cr += Math.max(0, Math.floor((j + a.dmin) * a.criticalMultiplier) - t.damageResistance) / n;
    return hitChance(a.attackChance, t.blockChance) * ((1 - cc / 100) * nc + cc * cr / 100) / 100;
  }
  function turnsToKill(a, t) {
    var crit = a.canCrit && !t.immune;
    if ((crit ? a.dmax * a.criticalMultiplier : a.dmax) <= t.damageResistance) return 999;
    var dpt = avgPerHit(a, t) * a.attacksPerTurn;
    if (dpt <= 0) return 100;
    return Math.ceil(t.maxHP / dpt);
  }
  function monsterActor(m) {
    var cs = m[10] || 0, cm = m[11] || 0;
    return { name: m[1], maxHP: m[2], attackChance: m[3], blockChance: m[4], damageResistance: m[5], dmin: m[6], dmax: m[7],
             maxAP: m[8], attackCost: m[9], criticalSkill: cs, criticalMultiplier: cm, immune: ['ghost', 'construct', 'demon'].indexOf(m[12]) >= 0,
             canCrit: cs !== 0 && cm !== 0 && cm !== 1, critChance: critChance(cs), attacksPerTurn: m[9] ? Math.floor(m[8] / m[9]) : 0 };
  }

  // ------------------------------------------------------------------ skills: points & requirements
  function skillPoints(level) { return level >= D.lv.first ? Math.floor((level - D.lv.first) / D.lv.every) + 1 : 0; }
  function skillCost(sk, n) { return sk.type === 'onlyByQuests' ? 0 : sk.type === 'firstLevelRequiresQuest' ? Math.max(0, n - 1) : n; }
  function problems(b) {
    var out = [], bt = baseTraits(b);
    var statOf = { maxHP: bt.maxHP, maxAP: bt.maxAP, attackChance: bt.attackChance, blockChance: bt.blockChance,
                   damageResistance: bt.damageResistance, criticalSkill: bt.criticalSkill };
    D.skills.forEach(function (sk) {
      var n = b.skills[sk.id] || 0;
      for (var k = 1; k <= n; k++) {
        sk.reqs.forEach(function (r) {
          if (r[0] === 'level' && b.level < k * r[1] + r[2]) out.push(sk.name + ' ' + k + ' needs character level ' + (k * r[1] + r[2]));
          var STAT = { maxHP: 'max HP', maxAP: 'max AP', attackChance: 'attack chance', blockChance: 'block chance', damageResistance: 'damage resistance', criticalSkill: 'critical skill' };
          if (r[0] === 'stat' && (statOf[r[1]] || 0) < k * r[2] + r[3]) out.push(sk.name + ' ' + k + ' needs ' + (k * r[2] + r[3]) + ' base ' + (STAT[r[1]] || r[1]) + ' from level-ups (you have ' + (statOf[r[1]] || 0) + ')');
          if (r[0] === 'skill' && (b.skills[r[1]] || 0) < k * r[2]) out.push(sk.name + ' ' + k + ' needs ' + D.skillName[r[1]] + ' ' + (k * r[2]));
        });
      }
    });
    return Array.from(new Set(out));
  }

  // ------------------------------------------------------------------ UI
  var SLOTS = [['weapon', 'Weapon'], ['shield', 'Off-hand'], ['head', 'Head'], ['body', 'Body'], ['hand', 'Hands'], ['feet', 'Feet'],
               ['neck', 'Neck'], ['leftring', 'Ring 1'], ['rightring', 'Ring 2']];
  function el(t, c, x) { var e = document.createElement(t); if (c) e.className = c; if (x != null) e.textContent = x; return e; }
  function emptyBuild() { return { level: 1, picks: { hp: 0, ac: 0, dmg: 0, bc: 0 }, skills: {}, eq: {}, fortAt: [], mon: '' }; }

  function App(root, data) {
    D = data; C = data.c;
    D.skillName = {}; D.skills.forEach(function (s) { D.skillName[s.id] = s.name; });
    D.fortEarliest = function (k) { var r = (D.skills.filter(function (s) { return s.id === 'fortitude'; })[0] || { reqs: [] }).reqs.filter(function (x) { return x[0] === 'level'; })[0]; return r ? k * r[1] + r[2] : 1; };
    this.root = root; this.b = this.load() || emptyBuild();
    this.build();
  }
  App.prototype.load = function () {
    try { if (location.hash.length > 3) return JSON.parse(decodeURIComponent(escape(atob(location.hash.slice(1))))); } catch (e) {}
    return null;
  };
  App.prototype.save = function () {
    try { history.replaceState(null, '', '#' + btoa(unescape(encodeURIComponent(JSON.stringify(this.b))))); } catch (e) {}
  };
  App.prototype.build = function () {
    var self = this, R = this.root; R.innerHTML = '';
    var grid = el('div', 'bc-grid'); R.appendChild(grid);
    var left = el('div', 'bc-col'), right = el('div', 'bc-col'); grid.appendChild(left); grid.appendChild(right);
    // level & level-ups
    var lvBox = el('section', 'bc-box'); left.appendChild(lvBox); lvBox.appendChild(el('h4', null, 'Level & level-ups'));
    this.inputs = {};
    var row = function (box, label, key, get, set, min, max) {
      var r = el('label', 'bc-row'); r.appendChild(el('span', null, label));
      var i = el('input'); i.type = 'number'; i.min = min; i.max = max; i.value = get();
      i.oninput = function () { set(Math.max(min, Math.min(max, Number(i.value || 0)))); self.update(); };
      r.appendChild(i); box.appendChild(r); self.inputs[key] = i; return i;
    };
    row(lvBox, 'Character level', 'level', function () { return self.b.level; }, function (v) { self.b.level = v; }, 1, 200);
    [['hp', 'Max health (+' + D.lv.hp + ' HP)'], ['ac', 'Attack chance (+' + D.lv.ac + ')'], ['dmg', 'Attack damage (+' + D.lv.dmg + ')'], ['bc', 'Block chance (+' + D.lv.bc + ')']]
      .forEach(function (p) { row(lvBox, p[1], 'pick_' + p[0], function () { return self.b.picks[p[0]]; }, function (v) { self.b.picks[p[0]] = v; }, 0, 199); });
    this.pickInfo = el('p', 'bc-note'); lvBox.appendChild(this.pickInfo);
    // equipment
    var eqBox = el('section', 'bc-box'); left.appendChild(eqBox); eqBox.appendChild(el('h4', null, 'Equipment'));
    this.selects = {};
    SLOTS.forEach(function (sl) {
      var r = el('label', 'bc-row'); r.appendChild(el('span', null, sl[1]));
      var s = el('select'); s.appendChild(new Option('— none —', ''));
      var opts = Object.keys(D.items).filter(function (id) {
        var it = D.items[id], c = D.cats[it.cat] || {};
        if (sl[0] === 'shield') return c.slot === 'shield' || (c.slot === 'weapon' && (c.size === 'light' || c.size === 'std'));
        if (sl[0] === 'leftring' || sl[0] === 'rightring') return c.slot === 'leftring' || c.slot === 'rightring' || c.slot === 'ring';
        return c.slot === sl[0];
      }).sort(function (a, b) { return D.items[a].n.localeCompare(D.items[b].n); });
      opts.forEach(function (id) { s.appendChild(new Option(D.items[id].n + (D.items[id].r && D.items[id].r !== 'ordinary' ? ' (' + D.items[id].r + ')' : ''), id)); });
      s.value = self.b.eq[sl[0]] || '';
      s.onchange = function () {
        self.b.eq[sl[0]] = s.value || undefined;
        var w = self.b.eq.weapon && D.items[self.b.eq.weapon];
        if (sl[0] === 'weapon' && w && (D.cats[w.cat] || {}).size === 'large') { self.b.eq.shield = undefined; self.selects.shield.value = ''; }
        if (sl[0] === 'shield' && s.value && w && (D.cats[w.cat] || {}).size === 'large') { self.b.eq.weapon = undefined; self.selects.weapon.value = ''; }
        self.update();
      };
      r.appendChild(s); eqBox.appendChild(r); self.selects[sl[0]] = s;
    });
    eqBox.appendChild(el('p', 'bc-note', 'A two-handed weapon empties the off-hand, as in the game. Off-hand weapons must be light or standard-sized.'));
    // skills
    var skBox = el('section', 'bc-box'); left.appendChild(skBox); skBox.appendChild(el('h4', null, 'Skills'));
    this.spInfo = el('p', 'bc-note'); skBox.appendChild(this.spInfo);
    var list = el('div', 'bc-skills'); skBox.appendChild(list);
    D.skills.forEach(function (sk) {
      var r = el('label', 'bc-row'); var nm = el('span', null, sk.name + (sk.type === 'onlyByQuests' ? ' ⓠ' : sk.type === 'firstLevelRequiresQuest' ? ' ⓠ+' : ''));
      nm.title = sk.sum || ''; r.appendChild(nm);
      var i = el('input'); i.type = 'number'; i.min = 0; i.max = sk.max || 99; i.value = self.b.skills[sk.id] || 0;
      i.oninput = function () { var v = Math.max(0, Math.min(sk.max || 99, Number(i.value || 0))); if (v) self.b.skills[sk.id] = v; else delete self.b.skills[sk.id]; self.update(); };
      r.appendChild(i); list.appendChild(r);
    });
    skBox.appendChild(el('p', 'bc-note', 'ⓠ = quest reward only (free).  ⓠ+ = first level from a quest (free), further levels cost skill points.'));
    // results
    var res = el('section', 'bc-box bc-results'); right.appendChild(res); res.appendChild(el('h4', null, 'Your stats'));
    this.out = el('div'); res.appendChild(this.out);
    this.warn = el('div', 'bc-warn'); res.appendChild(this.warn);
    var vs = el('section', 'bc-box'); right.appendChild(vs); vs.appendChild(el('h4', null, 'Against a monster'));
    var ms = el('select'); ms.appendChild(new Option('— pick an enemy —', ''));
    D.mons.slice().sort(function (a, b) { return a[1].localeCompare(b[1]) || a[2] - b[2]; })
      .forEach(function (m) { ms.appendChild(new Option(m[1] + ' (HP ' + m[2] + ')', m[0])); });
    ms.value = this.b.mon || ''; ms.onchange = function () { self.b.mon = ms.value; self.update(); };
    vs.appendChild(ms); this.vsOut = el('div', 'bc-vs'); vs.appendChild(this.vsOut);
    var bar = el('div', 'bc-bar'); right.appendChild(bar);
    var share = el('button', null, 'Copy link to this build'); share.onclick = function () { self.save(); (navigator.clipboard && navigator.clipboard.writeText(location.href)); share.textContent = 'Link copied'; setTimeout(function () { share.textContent = 'Copy link to this build'; }, 1500); };
    var reset = el('button', null, 'Reset'); reset.onclick = function () { self.b = emptyBuild(); self.save(); self.build(); };
    bar.appendChild(share); bar.appendChild(reset);
    this.update();
  };
  App.prototype.update = function () {
    var b = this.b, s = compute(b);
    var used = b.picks.hp + b.picks.ac + b.picks.dmg + b.picks.bc, avail = b.level - 1;
    this.pickInfo.textContent = 'Level-ups used: ' + used + ' of ' + avail + (used > avail ? ' — too many!' : '') +
      ((b.skills.fortitude || 0) ? ' · Fortitude assumed learned at the earliest allowed level(s).' : '');
    var spent = D.skills.reduce(function (a, sk) { return a + skillCost(sk, b.skills[sk.id] || 0); }, 0), have = skillPoints(b.level);
    this.spInfo.textContent = 'Skill points: ' + spent + ' spent of ' + have + ' available at level ' + b.level + (spent > have ? ' — too many!' : '');
    var avg = (s.dmin + s.dmax) / 2;
    var rows = [['Max HP', s.maxHP], ['Max AP', s.maxAP], ['Attack chance', s.attackChance], ['Attack damage', s.dmin + '–' + s.dmax + ' (avg ' + avg.toFixed(1) + ')'],
      ['Block chance', s.blockChance], ['Damage resistance', s.damageResistance], ['Critical skill', s.criticalSkill],
      ['Critical multiplier', s.criticalMultiplier ? '×' + (+s.criticalMultiplier.toFixed(3)) : '–'],
      ['Crit chance', s.canCrit ? s.critChance + '%' : 'none' + (s.criticalSkill ? ' (no multiplier)' : '')],
      ['Attack cost', s.attackCost + ' AP'], ['Attacks per turn', s.attacksPerTurn], ['Move cost', s.moveCost + ' AP'],
      ['Use item cost', s.useItemCost + ' AP'], ['Re-equip cost', s.reequipCost + ' AP'], ['Fighting mode', s.wield]];
    if (s.nonWeaponDamageModifier !== 100) rows.push(['Non-weapon damage modifier', s.nonWeaponDamageModifier + '%']);
    var t = '<table><tbody>' + rows.map(function (r) { return '<tr><td>' + r[0] + '</td><td>' + r[1] + '</td></tr>'; }).join('') + '</tbody></table>';
    var conds = [];
    Object.keys(b.eq).forEach(function (k) { var it = b.eq[k] && D.items[b.eq[k]]; if (it && it.cond) conds = conds.concat(it.cond); });
    if (conds.length) t += '<p class="bc-note">Equipment also grants: ' + conds.join(', ') + ' (not included above).</p>';
    this.out.innerHTML = t;
    var probs = problems(b);
    if (used > avail) probs.unshift('More level-up choices than levels gained (' + used + ' > ' + avail + ').');
    if (spent > have) probs.unshift('More skill points spent than available (' + spent + ' > ' + have + ').');
    this.warn.innerHTML = probs.length ? '<b>This build is not possible as entered:</b><ul>' + probs.slice(0, 12).map(function (p) { return '<li>' + p + '</li>'; }).join('') + '</ul>' : '';
    var m = D.mons.filter(function (x) { return x[0] === b.mon; })[0];
    if (m) {
      var M = monsterActor(m), you = { maxHP: s.maxHP, attackChance: s.attackChance, blockChance: s.blockChance, damageResistance: s.damageResistance,
        dmin: s.dmin, dmax: s.dmax, criticalMultiplier: s.criticalMultiplier, canCrit: s.canCrit, critChance: s.critChance, attacksPerTurn: s.attacksPerTurn, immune: false };
      var hy = hitChance(you.attackChance, M.blockChance), hm = hitChance(M.attackChance, you.blockChance);
      var dy = avgPerHit(you, M) * you.attacksPerTurn, dm = avgPerHit(M, you) * M.attacksPerTurn;
      var ky = turnsToKill(you, M), km = turnsToKill(M, you);
      this.vsOut.innerHTML = '<table><thead><tr><th></th><th>You</th><th>' + M.name + '</th></tr></thead><tbody>' +
        '<tr><td>Hit chance</td><td>' + hy + '%</td><td>' + hm + '%</td></tr>' +
        '<tr><td>Crit chance</td><td>' + (you.canCrit && !M.immune ? you.critChance + '%' : (M.immune ? 'immune' : '–')) + '</td><td>' + (M.canCrit ? M.critChance + '%' : '–') + '</td></tr>' +
        '<tr><td>Average damage per turn</td><td>' + dy.toFixed(1) + '</td><td>' + dm.toFixed(1) + '</td></tr>' +
        '<tr><td>Turns to kill the other</td><td>' + (ky >= 999 ? 'never (can\'t get through armor)' : ky) + '</td><td>' + (km >= 999 ? 'never' : km) + '</td></tr>' +
        '</tbody></table><p class="bc-note">Uses the game\'s own average-damage and turns-to-kill formulas (CombatController.java). Averages, not a guarantee.</p>';
    } else this.vsOut.innerHTML = '';
    this.save();
  };

  function init() {
    document.querySelectorAll('.build-calc[data-src]').forEach(function (root) {
      if (root.dataset.ready) return; root.dataset.ready = '1'; root.textContent = 'Loading…';
      fetch(root.dataset.src).then(function (r) { return r.json(); }).then(function (d) { new App(root, d); })
        .catch(function () { root.textContent = 'Could not load the calculator data.'; });
    });
  }
  window.ATCalc = { compute: compute, setData: function (d) { D = d; C = d.c; D.skillName = {}; d.skills.forEach(function (s) { D.skillName[s.id] = s.name; });
    D.fortEarliest = function (k) { var r = (d.skills.filter(function (s) { return s.id === 'fortitude'; })[0] || { reqs: [] }).reqs.filter(function (x) { return x[0] === 'level'; })[0]; return r ? k * r[1] + r[2] : 1; }; },
    hitChance: hitChance, avgPerHit: avgPerHit, turnsToKill: turnsToKill, monsterActor: monsterActor, problems: problems, skillPoints: skillPoints };
  if (window.document$ && window.document$.subscribe) window.document$.subscribe(init);
  else if (document.readyState !== 'loading') init(); else document.addEventListener('DOMContentLoaded', init);
})();
