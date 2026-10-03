# Stats & Skills

How your hero's numbers work in Andor's Trail v0.8.18. Every figure on this page is read straight from the game's source code.

## Starting stats (level 1)

| Stat | Value | What it does |
|---|---|---|
| Max HP | 25 | Health. You die at 0. |
| Max AP | 10 | Action points per combat turn. Attacking, moving and using items all spend AP. |
| Attack chance (AC) | 60 | Accuracy. Compared against the target's block chance. |
| Attack damage | 1–1 | Each hit rolls a random number in this range. |
| Block chance (BC) | 9 | Evasion. Compared against the attacker's attack chance. |
| Damage resistance (DR) | 0 | Subtracted from every hit you take. |
| Critical skill | 0 | Sets how often you land critical hits. |
| Critical multiplier | none | How hard criticals hit. Only weapons provide one. |
| Attack cost | 4 AP (unarmed) | AP per attack. A weapon replaces this with its own cost. |
| Move cost | 6 AP | AP to step one tile during combat. |
| Use item / re-equip cost | 5 / 5 AP | AP to drink a potion or swap gear in combat. |

## Levelling up

Every time you level up, **you pick exactly one** of these four bonuses. They're permanent, and the choice can't be undone:

| Choice | Bonus per level-up |
|---|---|
| Increase max health | +5 max HP |
| Increase attack chance | +5 attack chance |
| Increase attack damage | +1 to both minimum and maximum damage |
| Increase block chance | +3 block chance |

These choices make up your **base stats**. They matter beyond the raw numbers, because skill requirements look only at base stats. For example, [Bark Skin](barkSkin.md) needs block chance from level-ups, and gear doesn't count toward it.

**Skill points.** You get your first skill point at level 4, then one more every 4 levels (4, 8, 12, 16, 20, 24, 28, 32…). That's only 12 skill points by level 50, so each one is a big decision.

**Health and Fortitude.** [Fortitude](fortitude.md) adds +1 max HP per skill level to **every level-up after you learn it**. It is not retroactive, so the earlier you take it, the more it gives. Its first level needs character level 5, which is why players hold their level-4 skill point until level 5. Over a long game it out-scales the +5 HP level-up choice, which is why many players never pick health at level-up.

**Experience needed.** Going from level L to L+1 costs 55 × L² experience.

| Level | Total experience to reach it | Experience for the next level |
|---|---|---|
| 2 | 55 | 220 |
| 5 | 1,650 | 1,375 |
| 10 | 15,675 | 5,500 |
| 15 | 55,825 | 12,375 |
| 20 | 135,850 | 22,000 |
| 25 | 269,500 | 34,375 |
| 30 | 470,525 | 49,500 |
| 40 | 1,129,700 | 88,000 |
| 45 | 1,615,350 | 111,375 |
| 50 | 2,223,375 | 137,500 |
| 60 | 3,861,550 | 198,000 |

## How combat works

Each attack is resolved in four steps.

**1. Does it hit?** The game takes your attack chance minus the target's block chance, and puts that gap through an S-shaped curve:

> hit % = 50 × (1 + (2/π) × arctan((gap − 50) / 40))

| AC − BC gap | Hit chance | Value of +5 more AC here |
|---|---|---|
| -50 | 12% | +0.6 percentage points |
| +0 | 21% | +1.7 percentage points |
| +25 | 32% | +3.0 percentage points |
| +50 | 50% | +4.0 percentage points |
| +75 | 67% | +2.7 percentage points |
| +100 | 78% | +1.5 percentage points |
| +150 | 87% | +0.5 percentage points |
| +200 | 91% | +0.3 percentage points |
| +300 | 94% | +0.1 percentage points |

A 50-point gap is a coin flip. Near that point, every extra attack chance pays off the most. Far above it, you're close to the cap, so more accuracy barely helps. Far below it, you need a lot of accuracy before you see much change. Block chance works the same way in reverse: it helps most when your enemies' accuracy sits near yours + 50.

**2. How much damage?** A random number between your minimum and maximum attack damage.

**3. Is it critical?** It can only be critical if two things are both true: you have critical skill above 0, **and** your weapon gives a critical multiplier. Unarmed attacks and weapons without a multiplier never crit, however much critical skill you have. Ghosts, constructs and demons are immune to critical hits. Critical skill becomes a crit chance with diminishing returns:

> crit % = −5 + 2 × √(5 × critical skill)

| Critical skill | Crit chance |
|---|---|
| 5 | 5% |
| 10 | 9% |
| 20 | 15% |
| 30 | 19% |
| 45 | 25% |
| 60 | 29% |
| 80 | 35% |
| 100 | 39% |
| 150 | 49% |

A critical hit multiplies the damage roll by the critical multiplier (e.g. ×2).

**4. Armor.** The target's damage resistance is subtracted from the result, after any critical multiplier, and damage can't go below 0. That's why a few big hits beat many small ones against heavily armored enemies: a 5-damage hit into 4 DR does 1 damage, while a 20-damage hit does 16.

**Attacks per turn** = max AP ÷ attack cost, rounded down. With 10 AP, a 4-AP weapon attacks twice and 2 AP sit unused; [Combat Speed](speed.md) (+1 max AP per level) would turn that into 3 attacks. Because of the rounding, one point of AP or attack cost can be worth nothing, or worth a whole extra attack.

## All skills

### Criticals

| Skill | Max level | How obtained | Summary |
|---|---|---|---|
| [Better Criticals](betterCriticals.md) | unlimited | Skill points | Increased critical damage |
| [Fracture](crit2.md) | 1 | Skill points | Chance of bone fracture |
| [Internal bleeding](crit1.md) | 1 | Skill points | Chance of internal bleeding |
| [More Criticals](moreCriticals.md) | unlimited | Skill points | Increased critical skill |

### Defense

| Skill | Max level | How obtained | Summary |
|---|---|---|---|
| [Bark Skin](barkSkin.md) | 5 | Skill points | Damage resistance |
| [Dodge](dodge.md) | unlimited | Skill points | Increased block chance |
| [Evasion](evasion.md) | 4 | Skill points | Increased chance of fleeing |
| [Taunt](taunt.md) | 1 | Skill points | Attacker loses AP on miss |

### Immunity

| Skill | Max level | How obtained | Summary |
|---|---|---|---|
| [Corpse Eater](eater.md) | unlimited | Skill points | Recover health points on every kill |
| [Dark blessing of the Shadow](shadowBless.md) | 1 | Quest reward only | Resistance against all types of conditions |
| [Enduring Body](resistancePhysical.md) | 7 | Skill points | Resistance against physical capacity conditions |
| [Increased Fortitude](fortitude.md) | unlimited | Skill points | Gain health on each level up |
| [Pure Blood](resistanceBlood.md) | 7 | Skill points | Resistance against blood disorders |
| [Regeneration](regeneration.md) | unlimited | Skill points | Gain health every round |
| [Rejuvenation](rejuvenation.md) | 1 | Skill points | Chance of effect removal |
| [Spore poison immunity](sporeImmunity.md) | 1 | Quest reward only | Full immunity to spore poison |
| [Strong Mind](resistanceMental.md) | 7 | Skill points | Resistance against mental conditions |

### Offense

| Skill | Max level | How obtained | Summary |
|---|---|---|---|
| [Cleave](cleave.md) | unlimited | Skill points | Recover action points on every kill |
| [Combat Speed](speed.md) | 2 | Skill points | Increased maximum action points |
| [Concussion](concussion.md) | 1 | Skill points | Chance of concussion |
| [Hard Hit](weaponDmg.md) | unlimited | Skill points | Increased attack damage |
| [Weapon Accuracy](weaponChance.md) | unlimited | Skill points | Increased attack chance |

### Proficiency

| Skill | Max level | How obtained | Summary |
|---|---|---|---|
| [Axe proficiency](weaponProficiencyAxe.md) | 3 | First level from a quest, then skill points | Better at fighting with axes |
| [Blunt weapon proficiency](weaponProficiencyBlunt.md) | 3 | First level from a quest, then skill points | Better at fighting with blunt weapons |
| [Dagger proficiency](weaponProficiencyDagger.md) | 3 | First level from a quest, then skill points | Better at fighting with daggers |
| [Heavy armor proficiency](armorProficiencyHeavy.md) | 4 | First level from a quest, then skill points | Make better use of heavy armor |
| [Light armor proficiency](armorProficiencyLight.md) | 3 | First level from a quest, then skill points | Make better use of light armor |
| [One-handed sword proficiency](weaponProficiency1hsword.md) | 3 | First level from a quest, then skill points | Better at fighting with one-handed swords |
| [Pole weapon proficiency](weaponProficiencyPole.md) | 3 | First level from a quest, then skill points | Better at fighting with pole weapons |
| [Shield proficiency](armorProficiencyShield.md) | 2 | First level from a quest, then skill points | Make better use of shields and parrying weapons |
| [Two-handed sword proficiency](weaponProficiency2hsword.md) | 3 | First level from a quest, then skill points | Better at fighting with two-handed swords |
| [Unarmed fighting](weaponProficiencyUnarmed.md) | 3 | First level from a quest, then skill points | Better at fighting without weapons |
| [Unarmored fighting](armorProficiencyUnarmored.md) | 3 | First level from a quest, then skill points | Better at fighting without armor |

### Specialty

| Skill | Max level | How obtained | Summary |
|---|---|---|---|
| [Fighting style: Dual wield](fightstyleDualWield.md) | 2 | Skill points | Wield two weapons at the same time |
| [Fighting style: Two-handed weapon](fightstyle2hand.md) | 2 | Skill points | Make better use of weapons that require both hands |
| [Fighting style: Way of the monk](fightstyleUnarmedUnarmored.md) | 3 | Skill points | Better at fighting unarmed/unarmored |
| [Fighting style: Weapon and shield](fightstyleWeaponShield.md) | 2 | Skill points | Better at fighting with weapon and shield |
| [Specialization: Dual wield](specializationDualWield.md) | 1 | Skill points | Expert at dual wielding |
| [Specialization: Two-handed weapon](specialization2hand.md) | 1 | Skill points | Expert at two-handed weapons |
| [Specialization: Weapon and shield](specializationWeaponShield.md) | 1 | Skill points | Expert at fighting with weapon and shield |

### Utility

| Skill | Max level | How obtained | Summary |
|---|---|---|---|
| [Failure Mastery](lowerExploss.md) | 5 | Skill points | Decrease amount of lost experience when dying |
| [Magic Finder](magicfinder.md) | unlimited | Skill points | Increased chance of finding magic items |
| [Merchant](barter.md) | 3 | Skill points | Better shop prices |
| [Quick Learner](moreExp.md) | unlimited | Skill points | More experience from monster kills |
| [Treasure Hunter](coinfinder.md) | unlimited | Skill points | Higher chance of finding gold |

