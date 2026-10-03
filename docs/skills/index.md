# Stats & Skills

Andor's Trail v0.8.18, read straight from the game's source code. Click a heading to collapse it. For advice on how to spend your points, see [Strategy](../strategy/index.md).

???+ section "Starting stats (level 1)"

    | Stat | Lv 1 | Stat | Lv 1 |
    |---|---|---|---|
    | [Max HP](stats.md#max-hp) | 25 | [Critical skill](stats.md#critical-skill) | 0 |
    | [Max AP](stats.md#max-ap) | 10 | [Critical multiplier](stats.md#critical-multiplier) | – |
    | [Attack chance](stats.md#attack-chance) | 60 | [Attack cost](stats.md#attack-cost) | 4 AP |
    | [Attack damage](stats.md#attack-damage) | 1–1 | [Move cost](stats.md#move-cost) | 6 AP |
    | [Block chance](stats.md#block-chance) | 9 | [Use item cost](stats.md#use-item-cost) | 5 AP |
    | [Damage resistance](stats.md#damage-resistance) | 0 | [Re-equip cost](stats.md#re-equip-cost) | 5 AP |

???+ section "Levelling up"

    | Choice each level-up | Bonus |
    |---|---|
    | Max health | +5 HP |
    | Attack chance | +5 |
    | Attack damage | +1 min & max |
    | Block chance | +3 |

    Pick **one** per level-up; it's permanent. These form your **base stats**, the only values skill requirements check (gear and skills never count).

    **Skill points:** level 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60 (12 by level 50).
    **Experience:** level L → L+1 costs 55 × L².

    | Level | Total XP | XP to next |
    |---|---|---|
    | 2 | 55 | 220 |
    | 5 | 1,650 | 1,375 |
    | 10 | 15,675 | 5,500 |
    | 15 | 55,825 | 12,375 |
    | 20 | 135,850 | 22,000 |
    | 25 | 269,500 | 34,375 |
    | 30 | 470,525 | 49,500 |
    | 40 | 1,129,700 | 88,000 |
    | 50 | 2,223,375 | 137,500 |
    | 60 | 3,861,550 | 198,000 |

???+ section "How combat works"

    Every attack runs four steps. See the [stat glossary](stats.md) for what each stat means.

    **1 · Hit?** `hit % = 50 × (1 + (2/π) × arctan((AC − BC − 50) / 40))`

    | AC − BC | Hit | +5 AC adds |
    |---|---|---|
    | -50 | 12% | +0.6% |
    | +0 | 21% | +1.7% |
    | +25 | 32% | +3.0% |
    | +50 | 50% | +4.0% |
    | +75 | 67% | +2.7% |
    | +100 | 78% | +1.5% |
    | +150 | 87% | +0.5% |
    | +200 | 91% | +0.3% |
    | +300 | 94% | +0.1% |

    **2 · Damage:** random between min and max attack damage.

    **3 · Critical?** Only with critical skill > 0 **and** a weapon that gives a critical multiplier. Ghosts, constructs and demons are immune. `crit % = −5 + 2 × √(5 × critical skill)`, then damage × multiplier.

    | Crit skill | Crit % |
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

    **4 · Armor:** the target's damage resistance is subtracted from the result (minimum 0).

    **Attacks per turn** = max AP ÷ attack cost, rounded down.

???+ section "All skills (45)"

    **Criticals**

    | Skill | Max | Obtained | Summary |
    |---|---|---|---|
    | [Better Criticals](betterCriticals.md) | ∞ | Points | Increased critical damage |
    | [Fracture](crit2.md) | 1 | Points | Chance of bone fracture |
    | [Internal bleeding](crit1.md) | 1 | Points | Chance of internal bleeding |
    | [More Criticals](moreCriticals.md) | ∞ | Points | Increased critical skill |

    **Defense**

    | Skill | Max | Obtained | Summary |
    |---|---|---|---|
    | [Bark Skin](barkSkin.md) | 5 | Points | Damage resistance |
    | [Dodge](dodge.md) | ∞ | Points | Increased block chance |
    | [Evasion](evasion.md) | 4 | Points | Increased chance of fleeing |
    | [Taunt](taunt.md) | 1 | Points | Attacker loses AP on miss |

    **Immunity**

    | Skill | Max | Obtained | Summary |
    |---|---|---|---|
    | [Corpse Eater](eater.md) | ∞ | Points | Recover health points on every kill |
    | [Dark blessing of the Shadow](shadowBless.md) | 1 | Quest only | Resistance against all types of conditions |
    | [Enduring Body](resistancePhysical.md) | 7 | Points | Resistance against physical capacity conditions |
    | [Increased Fortitude](fortitude.md) | ∞ | Points | Gain health on each level up |
    | [Pure Blood](resistanceBlood.md) | 7 | Points | Resistance against blood disorders |
    | [Regeneration](regeneration.md) | ∞ | Points | Gain health every round |
    | [Rejuvenation](rejuvenation.md) | 1 | Points | Chance of effect removal |
    | [Spore poison immunity](sporeImmunity.md) | 1 | Quest only | Full immunity to spore poison |
    | [Strong Mind](resistanceMental.md) | 7 | Points | Resistance against mental conditions |

    **Offense**

    | Skill | Max | Obtained | Summary |
    |---|---|---|---|
    | [Cleave](cleave.md) | ∞ | Points | Recover action points on every kill |
    | [Combat Speed](speed.md) | 2 | Points | Increased maximum action points |
    | [Concussion](concussion.md) | 1 | Points | Chance of concussion |
    | [Hard Hit](weaponDmg.md) | ∞ | Points | Increased attack damage |
    | [Weapon Accuracy](weaponChance.md) | ∞ | Points | Increased attack chance |

    **Proficiency**

    | Skill | Max | Obtained | Summary |
    |---|---|---|---|
    | [Axe proficiency](weaponProficiencyAxe.md) | 3 | Quest, then points | Better at fighting with axes |
    | [Blunt weapon proficiency](weaponProficiencyBlunt.md) | 3 | Quest, then points | Better at fighting with blunt weapons |
    | [Dagger proficiency](weaponProficiencyDagger.md) | 3 | Quest, then points | Better at fighting with daggers |
    | [Heavy armor proficiency](armorProficiencyHeavy.md) | 4 | Quest, then points | Make better use of heavy armor |
    | [Light armor proficiency](armorProficiencyLight.md) | 3 | Quest, then points | Make better use of light armor |
    | [One-handed sword proficiency](weaponProficiency1hsword.md) | 3 | Quest, then points | Better at fighting with one-handed swords |
    | [Pole weapon proficiency](weaponProficiencyPole.md) | 3 | Quest, then points | Better at fighting with pole weapons |
    | [Shield proficiency](armorProficiencyShield.md) | 2 | Quest, then points | Make better use of shields and parrying weapons |
    | [Two-handed sword proficiency](weaponProficiency2hsword.md) | 3 | Quest, then points | Better at fighting with two-handed swords |
    | [Unarmed fighting](weaponProficiencyUnarmed.md) | 3 | Quest, then points | Better at fighting without weapons |
    | [Unarmored fighting](armorProficiencyUnarmored.md) | 3 | Quest, then points | Better at fighting without armor |

    **Specialty**

    | Skill | Max | Obtained | Summary |
    |---|---|---|---|
    | [Fighting style: Dual wield](fightstyleDualWield.md) | 2 | Points | Wield two weapons at the same time |
    | [Fighting style: Two-handed weapon](fightstyle2hand.md) | 2 | Points | Make better use of weapons that require both hands |
    | [Fighting style: Way of the monk](fightstyleUnarmedUnarmored.md) | 3 | Points | Better at fighting unarmed/unarmored |
    | [Fighting style: Weapon and shield](fightstyleWeaponShield.md) | 2 | Points | Better at fighting with weapon and shield |
    | [Specialization: Dual wield](specializationDualWield.md) | 1 | Points | Expert at dual wielding |
    | [Specialization: Two-handed weapon](specialization2hand.md) | 1 | Points | Expert at two-handed weapons |
    | [Specialization: Weapon and shield](specializationWeaponShield.md) | 1 | Points | Expert at fighting with weapon and shield |

    **Utility**

    | Skill | Max | Obtained | Summary |
    |---|---|---|---|
    | [Failure Mastery](lowerExploss.md) | 5 | Points | Decrease amount of lost experience when dying |
    | [Magic Finder](magicfinder.md) | ∞ | Points | Increased chance of finding magic items |
    | [Merchant](barter.md) | 3 | Points | Better shop prices |
    | [Quick Learner](moreExp.md) | ∞ | Points | More experience from monster kills |
    | [Treasure Hunter](coinfinder.md) | ∞ | Points | Higher chance of finding gold |
