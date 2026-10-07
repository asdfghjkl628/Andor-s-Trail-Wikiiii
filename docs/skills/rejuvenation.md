# Rejuvenation

*Every round (6 seconds), there is a 20 % chance that one of the active negative actor conditions will be lowered by one magnitude.*

<div class="infobox" markdown>

| | |
|---|---|
| **In short** | 20% chance per round to weaken one harmful condition ([abbreviations](../glossary.md)) |
| **Category** | Immunity |
| **Max level** | 1 |
| **Obtained via** | Skill points |

</div>

## Effect

Every round (6 seconds), there is a 20 % chance that one of the active negative actor conditions will be lowered by one magnitude. This applies to all temporary effect types that affect the body; mental conditions such as Dazed, physical capacity conditions such as Fatigue and also blood disorders such as poison.

## Requirements per skill level

| Skill level | [Pure Blood](resistanceBlood.md) level | [Strong Mind](resistanceMental.md) level | [Enduring Body](resistancePhysical.md) level |
|---|---|---|---|
| 1 | 3 | 3 | 3 |

<p class="verified">Verified against v0.8.18 game code (`SkillCollection.java`).</p>

See [Conditions](../conditions/index.md#categories-and-resistance) for the conditions this skill affects.


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=rejuvenation.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=rejuvenation.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `rejuvenation` |
    | In-game list position | 24 |
    | Level-up type | `alwaysShown` |
    | Category (internal) | `immunity` |
    | String keys | `skill_title_rejuvenation`, `skill_longdescription_rejuvenation` |
    | Values in description | `PER_SKILLPOINT_INCREASE_REJUVENATION_CHANCE` = 20 |
    | Granting dialogue nodes | – |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

