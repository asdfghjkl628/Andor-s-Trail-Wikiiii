# Stat glossary

The effect of each character statistic in v0.8.18. Starting values live on [Stats & Skills](index.md).

## Max HP
Your maximum health. When current HP reaches 0, the character is defeated. Raised by the **max health** level-up (+5), by [Fortitude](fortitude.md) (+1 per skill level on every later level-up), and by some equipment. See [Strategy](../strategy/levelling.md) for a comparison of Fortitude and health level-ups.

## Max AP
Action points per combat turn. Attacking, moving and using items all cost AP. [Combat Speed](speed.md) adds +1 per level, up to 2.

## Attack chance
Your accuracy. It is compared with the target's block chance to determine whether an attack hits, using a curve with diminishing returns at both ends ([details](index.md)). Raised by the **attack chance** level-up (+5), [Weapon Accuracy](weaponChance.md) (+12 per level), weapons and proficiencies.

## Attack damage
Each hit rolls a random number between your minimum and maximum damage. The **attack damage** level-up adds +1 to both. [Hard Hit](weaponDmg.md) adds +2 to the maximum only, which raises average damage by 1.

## Block chance
Your evasion. It is compared with the attacker's attack chance using the same curve. Raised by the **block chance** level-up (+3), [Dodge](dodge.md) (+9 per level), shields and armor. Only block chance from level-ups counts toward skill requirements such as [Bark Skin](barkSkin.md); block chance from shields and armor does not.

## Damage resistance
Subtracted from every hit you take, after critical multipliers. Damage cannot go below 0, so damage resistance is most effective against enemies that deal many small hits and less effective against enemies that deal large hits. Raised by [Bark Skin](barkSkin.md) (+1 per level), shields and armor.

## Critical skill
Determines your critical hit chance: `−5 + 2 × √(5 × critical skill)`. Because of the square root, each additional point adds less than the previous one. It has **no effect** unless you also have a critical multiplier (from your weapon, or [Way of the Monk](fightstyleUnarmedUnarmored.md)). [More Criticals](moreCriticals.md) raises it by 20% per level.

## Critical multiplier
How hard a critical hit lands (e.g. ×2). Weapons provide it. Unarmed attacks have none, so an unarmed character cannot land critical hits unless they learn [Way of the Monk](fightstyleUnarmedUnarmored.md), which grants ×1.25 per level. [Better Criticals](betterCriticals.md) raises it by 25% per level.

## Attack cost
AP spent per attack: 4 unarmed, or whatever your weapon says. Attacks per turn = max AP ÷ attack cost, rounded down, so reducing attack cost by one point either adds a full attack per turn or has no effect, depending on the values involved.

## Move cost
AP to move one tile during combat. Heavy armor increases it.

## Use item cost
AP to use an item, e.g. drinking a potion in the middle of a fight.

## Re-equip cost
AP to change equipment during combat. Changing equipment during combat is possible but uses AP that could otherwise be spent attacking.
