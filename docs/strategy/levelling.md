# Levelling & skill points

*Written for v0.8.18. The mechanics behind all this are on [Stats & Skills](../skills/index.md).*

??? section "The short version (for the impatient)"

    - **Almost never pick max health at level-up.** Take [Fortitude](../skills/fortitude.md) at level 5 instead.
    - **Hold your level-4 skill point for one level** so it can go into Fortitude.
    - **Put 2 early level-ups into block chance** so [Bark Skin](../skills/barkSkin.md) is ready at level 10.
    - **Spend the rest on attack chance and attack damage**, leaning harder into damage as the game goes on.
    - **Plan skill points backwards from the skills you want.** The big ones are level-gated, and there's no respec.

???+ section "Why Fortitude beats the max health level-up"

    The **max health** level-up gives +5 HP, once. [Fortitude](../skills/fortitude.md) gives +1 HP on **every level-up after you learn it**, per skill level. It isn't retroactive, so the earlier you take it, the more it pays:

    | Fortitude level | Earliest level | Extra HP by level 50 | Equal to this many health level-ups |
    |---|---|---|---|
    | 1 | 5 | +45 | 9 |
    | 2 | 20 | +30 | 6 |
    | 3 | 35 | +15 | 3 |

    One skill point at level 5 ends up worth nine health level-ups, and those nine level-ups are now free to go into stats that skills can't replace. That's the whole reason "never level health" is the standard advice. It's not a meme; it's arithmetic.[^hp]

    The catch: your first skill point shows up at level 4, but Fortitude won't let you in until level 5. **Do not spend that level-4 point on something else.** ~~Your future self will send angry letters.~~ Just hold it for one level.

    Bonus: Fortitude also counts toward [Regeneration](../skills/regeneration.md), which needs Fortitude plus 30 base max HP per Regeneration level. Start at 25 HP, take Fortitude at 5, and you hit 30 base HP at level 10 without ever touching the health level-up.

    [^hp]: The one real exception is a very early, very dangerous stretch where +5 HP *right now* matters more than +45 HP eventually. Even then, most players just grit their teeth and drink potions.

???+ section "Block chance and Bark Skin"

    [Bark Skin](../skills/barkSkin.md) gives +1 damage resistance per level, up to 5. Each level wants character level 10 × its level **and** base block chance of 15 × its level, and only block chance from level-ups counts. You start at 9, and each block chance level-up gives +3:

    | Bark Skin level | Character level | Base block chance | Block chance level-ups needed (total) |
    |---|---|---|---|
    | 1 | 10 | 15 | 2 |
    | 2 | 20 | 30 | 7 |
    | 3 | 30 | 45 | 12 |
    | 4 | 40 | 60 | 17 |
    | 5 | 50 | 75 | 22 |

    Level 1 is a bargain: two block chance level-ups before level 10 and you're in. After that, each level costs five more level-ups *and* a skill point, which gets expensive fast. Decide early how far you're going instead of discovering at level 30 that you're one level-up short. Block chance also has few other sources ([Dodge](../skills/dodge.md), shields, armor), so a stray block chance level-up here and there is rarely wasted.

???+ section "Attack chance vs. attack damage"

    - **Attack chance** (+5 per level-up) lives on the [hit-chance curve](../skills/index.md). It's great while you're around 50 above the enemy's block chance and close to pointless once you're far ahead. It matters most early, before gear and weapon proficiencies start handing out accuracy for free. If you fall behind later, [Weapon Accuracy](../skills/weaponChance.md) gives +12 per skill point.
    - **Attack damage** (+1 to min and max per level-up) never goes out of style. Every point is one more damage on every single hit, and against armored enemies that's the difference between "chip damage" and "no damage". Lean into it more and more as the game goes on.

???+ section "Skill point timeline"

    You get a skill point at levels 4, 8, 12 and so on: 12 by level 50, which is not a lot.[^sp] Most of the good skills have level gates, so plan backwards:

    | Goal | Earliest level | Notes |
    |---|---|---|
    | [Fortitude](../skills/fortitude.md) 1 | 5 | The held level-4 point. |
    | [Bark Skin](../skills/barkSkin.md) 1 | 10 | Needs 2 block chance level-ups. |
    | [Combat Speed](../skills/speed.md) 1 / 2 | 15 / 30 | +1 max AP each. Check your weapon's attack cost first ([why](combat.md)). |
    | A fighting style, levels 1 / 2 | 15 / 30 | Dual wield, two-handed, or weapon & shield. |
    | [Way of the Monk](../skills/fightstyleUnarmedUnarmored.md) 1 / 2 / 3 | 15 / 30 / 45 | Fists only, no armor. A lifestyle choice. |
    | [Internal Bleeding](../skills/crit1.md) | 20 | 5 points: More Criticals 2 + Better Criticals 2 + itself. |
    | [Fracture](../skills/crit2.md) | 40 | 10 points: More Criticals 4 + Better Criticals 4 + Internal Bleeding + itself. |
    | A specialization | 45 | Needs the matching fighting style at level 2. |

    The crit skills do nothing without a weapon that gives a critical multiplier, and ghosts, constructs and demons ignore crits completely. Don't sink 10 points into the crit chain unless you have a crit weapon you plan to marry.

    [^sp]: For comparison, you get 49 level-ups by level 50. Level-ups are cheap; skill points are not. Spend accordingly.
