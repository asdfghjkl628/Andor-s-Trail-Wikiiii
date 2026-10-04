# Fighting style: Dual wield

*Gives benefits when fighting with two weapons at the same time, one in the main hand and one in the off-hand.*

<div class="infobox" markdown>

| | |
|---|---|
| **Category** | Specialty |
| **Max level** | 2 |
| **Obtained via** | Skill points |
| **Unlocks** | [Specialization: Dual wield](specializationDualWield.md) |

</div>

## Effect

Gives benefits when fighting with two weapons at the same time, one in the main hand and one in the off-hand.



Without this skill, only 25 % of a weapon's qualities may be used when equipped in the off-hand. This includes attack chance, critical skill, damage potential and block chance. Without this skill, attack cost (AP cost) of making an attack is the sum of the attack cost of the main weapon and that of the weapon used in the off-hand. The lower of both damage modifiers will be used.



With one level of this skill, 50 % of the off-hand's weapon's qualities may be used, and the attack cost is the highest attack cost of both weapons plus 50 % of the lowest attack cost of both weapons. The average of both damage modifiers will be used.



With two levels of this skill, 100 % of the off-hand's weapon's qualities may be used, and the attack cost equals the highest of the attack costs of the two equipped weapons. The highest damage modifier will be used.

## Requirements per skill level

| Skill level | Character level |
|---|---|
| 1 | 15 |
| 2 | 30 |

<p class="verified">Verified against v0.8.18 game code (`SkillCollection.java`).</p>
## Unlocks

- [Specialization: Dual wield](specializationDualWield.md): needs this skill at level 2


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=fightstyleDualWield.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=fightstyleDualWield.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `fightstyleDualWield` |
    | In-game list position | 38 |
    | Level-up type | `alwaysShown` |
    | Category (internal) | `specialty` |
    | String keys | `skill_title_fightstyle_dualwield`, `skill_longdescription_fightstyle_dualwield` |
    | Values in description | `DUALWIELD_EFFICIENCY_LEVEL0` = 25, `DUALWIELD_EFFICIENCY_LEVEL1` = 50, `DUALWIELD_LEVEL1_OFFHAND_AP_COST_PERCENT` = 50, `DUALWIELD_EFFICIENCY_LEVEL2` = 100 |
    | Granting dialogue nodes | – |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

