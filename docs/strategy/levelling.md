# Levelling & skill points

*Written for v0.8.18. The mechanics behind this page are explained on [Stats & Skills](../skills/index.md).*

??? section "The short version"

    - **Almost never pick max health at level-up.** Take [Fortitude](../skills/fortitude.md) at level 5 instead.
    - **Hold your level-4 skill point for one level**, so it can go into Fortitude at level 5.
    - **Put 2 early level-ups into block chance**, so [Bark Skin](../skills/barkSkin.md) is available at level 10.
    - **Spend the rest of your level-ups on attack chance and attack damage**, leaning toward damage as the game goes on.
    - **Plan your skill points backwards from the skills you want**, because the big ones have level gates.

???+ section "Why Fortitude beats the max health level-up"

    Choosing **max health** at level-up gives +5 HP once. [Fortitude](../skills/fortitude.md) gives +1 HP on **every level-up after you learn it**, per skill level. It's not retroactive, so the earlier you take it, the more it gives:

    | Fortitude level | Earliest level | Extra HP by level 50 | Equal to this many health level-ups |
    |---|---|---|---|
    | 1 | 5 | +45 | 9 |
    | 2 | 20 | +30 | 6 |
    | 3 | 35 | +15 | 3 |

    One skill point at level 5 is worth nine health level-ups by the late game, which frees those nine level-ups for stats that have no skill-based substitute. That's why "never level health" is the common advice.

    Your first skill point arrives at level 4, but Fortitude's first level needs character level 5. **Don't spend the level-4 point on something else.** Hold it for one level.

    Fortitude also counts toward [Regeneration](../skills/regeneration.md), which needs Fortitude plus base max HP of 30 per Regeneration level. Starting from 25 HP with Fortitude at level 5, you reach 30 base HP at level 10 without ever picking health.

???+ section "Block chance and Bark Skin"

    [Bark Skin](../skills/barkSkin.md) gives +1 damage resistance per level (max 5). Each level needs character level 10 × its level **and** base block chance of 15 × its level, and only block chance from level-ups counts toward that. You start with 9, and each block chance level-up gives +3:

    | Bark Skin level | Character level needed | Base block chance needed | Block chance level-ups needed (total) |
    |---|---|---|---|
    | 1 | 10 | 15 | 2 |
    | 2 | 20 | 30 | 7 |
    | 3 | 30 | 45 | 12 |
    | 4 | 40 | 60 | 17 |
    | 5 | 50 | 75 | 22 |

    The first level is cheap: two block chance level-ups before level 10. Each later level costs five more level-ups *plus* a skill point, so decide early how far you want to go. Block chance also has few other sources ([Dodge](../skills/dodge.md), shields, armor), which makes the occasional block chance level-up worthwhile even beyond Bark Skin.

???+ section "Attack chance vs. attack damage"

    - **Attack chance** (+5 per level-up) follows the [hit-chance curve](../skills/index.md): it pays off most while your accuracy minus the enemy's block chance is around 50, and very little once you're far ahead. It's most valuable early, before gear and weapon proficiencies start adding accuracy for free. [Weapon Accuracy](../skills/weaponChance.md) gives +12 per skill point if you need more later.
    - **Attack damage** (+1 to min and max per level-up) never loses value: every point is one more damage on every hit. It also matters more against armored enemies, because their damage resistance is subtracted from each hit. Lean toward damage as the game goes on.

???+ section "Skill point timeline"

    You get a skill point at levels 4, 8, 12 … (12 by level 50), and many skills have level gates. Plan backwards from what you want:

    | Goal | Earliest character level | Notes |
    |---|---|---|
    | [Fortitude](../skills/fortitude.md) 1 | 5 | Use the held level-4 point. |
    | [Bark Skin](../skills/barkSkin.md) 1 | 10 | Needs 2 block chance level-ups. |
    | [Combat Speed](../skills/speed.md) 1 / 2 | 15 / 30 | +1 max AP each; check your weapon's attack cost first ([why](combat.md)). |
    | A fighting style, levels 1 / 2 | 15 / 30 | Dual wield, two-handed, or weapon & shield. |
    | [Way of the Monk](../skills/fightstyleUnarmedUnarmored.md) 1 / 2 / 3 | 15 / 30 / 45 | Unarmed, unarmored fighting. |
    | [Internal Bleeding](../skills/crit1.md) | 20 | Needs 5 points: More Criticals 2 + Better Criticals 2 + itself. |
    | A specialization | 45 | Needs the matching fighting style at level 2. |
    | [Fracture](../skills/crit2.md) | 40 | Needs 10 points: More Criticals 4 + Better Criticals 4 + Internal Bleeding + itself. |

    The crit skills only do anything if your weapon gives a critical multiplier, and ghosts, constructs and demons ignore crits entirely. Don't start the crit chain without a crit weapon you plan to keep.
