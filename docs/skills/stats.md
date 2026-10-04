# Stat glossary

What each stat actually does in v0.8.18. Starting values live on [Stats & Skills](index.md).

## Max HP
Your health. Hit 0 and you're done. Raised by the **max health** level-up (+5), by [Fortitude](fortitude.md) (+1 per skill level on every later level-up), and by some gear. Most experienced players get theirs almost entirely from Fortitude; see [Strategy](../strategy/levelling.md) for why.

## Max AP
Action points per combat turn. Attacking, moving and drinking potions all cost AP, and running out mid-fight is a classic way to die. [Combat Speed](speed.md) adds +1 per level, up to 2.

## Attack chance
Your accuracy. It's compared with the target's block chance to decide whether you hit, through a curve with heavy diminishing returns at both ends ([details](index.md)). Raised by the **attack chance** level-up (+5), [Weapon Accuracy](weaponChance.md) (+12 per level), weapons and proficiencies.

## Attack damage
Each hit rolls a random number between your minimum and maximum damage. The **attack damage** level-up adds +1 to both. [Hard Hit](weaponDmg.md) adds +2 to the maximum only, which sounds better than it is: your average goes up by just 1.

## Block chance
Your evasion: the same curve as attack chance, pointed the other way. Raised by the **block chance** level-up (+3), [Dodge](dodge.md) (+9 per level), shields and armor. Only level-up block chance counts toward skill requirements like [Bark Skin](barkSkin.md), so your fancy shield doesn't help there.

## Damage resistance
Subtracted from every hit you take, after critical multipliers. Damage can't go below 0, so it shines against monsters that nibble at you with lots of small hits and does much less against ones that hit like a truck. Raised by [Bark Skin](barkSkin.md) (+1 per level), shields and armor.

## Critical skill
Sets your critical hit chance: `−5 + 2 × √(5 × critical skill)`. The square root means each extra point helps less than the one before. It does **nothing** unless you also have a critical multiplier (from your weapon, or [Way of the Monk](fightstyleUnarmedUnarmored.md)). [More Criticals](moreCriticals.md) raises it by 20% per level.

## Critical multiplier
How hard a critical hit lands (e.g. ×2). Weapons provide it. Bare fists have none, so unarmed heroes can't crit at all, unless they learn [Way of the Monk](fightstyleUnarmedUnarmored.md), which grants ×1.25 per level. [Better Criticals](betterCriticals.md) raises it by 25% per level.

## Attack cost
AP spent per attack: 4 unarmed, or whatever your weapon says. Attacks per turn = max AP ÷ attack cost, rounded down, so a single point here can be worth an entire extra attack every turn, or absolutely nothing.

## Move cost
AP to move one tile during combat. Heavy armor raises it, which is the price of looking like a walking tank.

## Use item cost
AP to use an item, e.g. drinking a potion in the middle of a fight.

## Re-equip cost
AP to change equipment during combat. Possible, but rarely a good use of your turn.
