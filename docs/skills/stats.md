# Stat glossary

What each stat does in Andor's Trail v0.8.18. Starting values are on [Stats & Skills](index.md).

## Max HP
Your health. You die at 0. Raised by the **max health** level-up choice (+5), by [Fortitude](fortitude.md) (+1 per skill level on every later level-up), and by some gear.

## Max AP
Action points per combat turn. Attacking, moving and using items all spend AP. [Combat Speed](speed.md) adds +1 per level (max 2).

## Attack chance
Your accuracy. Compared with the target's block chance to decide whether you hit; see [how combat works](index.md). Raised by the **attack chance** level-up (+5), [Weapon Accuracy](weaponChance.md) (+12 per level), weapons and proficiencies.

## Attack damage
Each hit deals a random amount between your minimum and maximum damage. The **attack damage** level-up adds +1 to both; [Hard Hit](weaponDmg.md) adds +2 to the maximum only.

## Block chance
Your evasion. Compared with the attacker's attack chance. Raised by the **block chance** level-up (+3), [Dodge](dodge.md) (+9 per level), shields and armor. Only level-up block chance counts toward skill requirements such as [Bark Skin](barkSkin.md).

## Damage resistance
Subtracted from every hit you take, after critical multipliers. Damage can't go below 0, so it's strongest against many weak hits. Raised by [Bark Skin](barkSkin.md) (+1 per level), shields and armor.

## Critical skill
Sets your critical hit chance: `−5 + 2 × √(5 × critical skill)`. Does nothing unless your weapon also gives a critical multiplier. [More Criticals](moreCriticals.md) increases it by 20% per level.

## Critical multiplier
How much a critical hit multiplies damage (e.g. ×2). Only weapons provide one; you have none unarmed. [Better Criticals](betterCriticals.md) increases it by 25% per level.

## Attack cost
AP spent per attack. Unarmed it's 4; a weapon replaces it with its own cost. Attacks per turn = max AP ÷ attack cost, rounded down, so a single point here can mean an extra attack every turn.

## Move cost
AP to move one tile during combat. Heavy armor can raise it.

## Use item cost
AP to use an item (e.g. drink a potion) during combat.

## Re-equip cost
AP to change equipment during combat.
