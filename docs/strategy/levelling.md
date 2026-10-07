---
description: "How to allocate level-ups and skill points in Andor's Trail v0.8.18: Fortitude versus health level-ups, block chance for Bark Skin, attack chance versus damage, and a skill point timeline."
---

# Levelling & skill points

*Written for v0.8.18. The underlying mechanics are described on [Stats & Skills](../skills/index.md).*

??? section "Summary"

    - **Avoid the max health level-up.** Learn [Fortitude](../skills/fortitude.md) at level 5 instead.
    - **Keep the level-4 skill point unspent until level 5** so that it can be used on Fortitude.
    - **Take two block chance level-ups early** so that [Bark Skin](../skills/barkSkin.md) is available at level 10.
    - **Spend the remaining level-ups on attack chance and attack damage**, with more emphasis on damage later in the game.
    - **Plan skill points around the skills you intend to learn.** Many skills require a minimum character level, and skill points cannot be reallocated.

???+ section "Fortitude compared with the max health level-up"

    The **max health** level-up gives +5 HP once. [Fortitude](../skills/fortitude.md) gives +1 HP per skill level on **every level-up after it is learned**. It is not retroactive, so learning it earlier yields more HP:

    | Fortitude level | Earliest level | Extra HP by level 50 | Equivalent number of health level-ups |
    |---|---|---|---|
    | 1 | 5 | +45 | 9 |
    | 2 | 20 | +30 | 6 |
    | 3 | 35 | +15 | 3 |

    A single skill point spent at level 5 provides as much HP by level 50 as nine health level-ups, and those nine level-ups can instead be used for statistics that skills cannot replace. This is the reasoning behind the common recommendation not to choose the health level-up.

    The first skill point is awarded at level 4, but Fortitude requires character level 5. Keeping the level-4 point unspent for one level allows it to be used on Fortitude as early as possible.

    The exception is a difficult early section of the game in which +5 HP immediately is more useful than +45 HP over the long term. Healing potions are the usual alternative in that situation.

    Fortitude also contributes to [Regeneration](../skills/regeneration.md), which requires Fortitude and 30 base max HP per Regeneration level. A character starting with 25 HP who learns Fortitude at level 5 reaches 30 base HP at level 10 without any health level-ups.

???+ section "Block chance and Bark Skin"

    [Bark Skin](../skills/barkSkin.md) gives +1 damage resistance per level, up to level 5. Each level requires a character level of 10 × the skill level **and** a base block chance of 15 × the skill level. Only block chance from level-ups counts. Characters start with 9 block chance, and each block chance level-up adds +3:

    | Bark Skin level | Character level | Base block chance | Block chance level-ups needed (total) |
    |---|---|---|---|
    | 1 | 10 | 15 | 2 |
    | 2 | 20 | 30 | 7 |
    | 3 | 30 | 45 | 12 |
    | 4 | 40 | 60 | 17 |
    | 5 | 50 | 75 | 22 |

    The first level is inexpensive: two block chance level-ups before level 10 are sufficient. Each further level costs five more level-ups and a skill point. It is advisable to decide early how many levels of Bark Skin to aim for, so that the required level-ups are taken in time. Block chance has few other sources ([Dodge](../skills/dodge.md), shields and armor), so additional block chance level-ups are rarely wasted.

???+ section "Attack chance compared with attack damage"

    - **Attack chance** (+5 per level-up) follows the [hit chance curve](../skills/index.md). It is most valuable when your attack chance is about 50 above the enemy's block chance, and gives little benefit once you are far ahead. It matters most early in the game, before equipment and weapon proficiencies provide accuracy. [Weapon Accuracy](../skills/weaponChance.md) gives +12 attack chance per skill point if more is needed later.
    - **Attack damage** (+1 to minimum and maximum per level-up) remains useful throughout the game. Each point adds one damage to every hit, which is significant against enemies with high damage resistance. Its relative value increases as the game progresses.

???+ section "Skill point timeline"

    Skill points are awarded at levels 4, 8, 12 and every four levels thereafter: 12 by level 50, compared with 49 level-ups over the same period. Many important skills require a minimum character level, so it helps to plan in advance:

    | Goal | Earliest level | Notes |
    |---|---|---|
    | [Fortitude](../skills/fortitude.md) 1 | 5 | Uses the level-4 skill point. |
    | [Bark Skin](../skills/barkSkin.md) 1 | 10 | Requires two block chance level-ups. |
    | [Combat Speed](../skills/speed.md) 1 / 2 | 15 / 30 | +1 max AP per level. Whether this adds attacks depends on your weapon's attack cost ([details](combat.md)). |
    | A fighting style, levels 1 / 2 | 15 / 30 | Dual wield, two-handed, or weapon and shield. |
    | [Way of the Monk](../skills/fightstyleUnarmedUnarmored.md) 1 / 2 / 3 | 15 / 30 / 45 | Requires fighting with no weapon and no armor. |
    | [Internal Bleeding](../skills/crit1.md) | 20 | 5 points in total: More Criticals 2, Better Criticals 2 and Internal Bleeding. |
    | [Fracture](../skills/crit2.md) | 40 | 10 points in total: More Criticals 4, Better Criticals 4, Internal Bleeding and Fracture. |
    | A specialization | 45 | Requires the matching fighting style at level 2. |

    The critical hit skills have no effect without a critical multiplier (from a weapon, or from [Way of the Monk](../skills/fightstyleUnarmedUnarmored.md) when fighting unarmed), and ghosts, constructs and demons are immune to critical hits. The full critical hit chain costs 10 skill points, so it is best suited to a character who intends to use a weapon with a critical multiplier for the rest of the game.
