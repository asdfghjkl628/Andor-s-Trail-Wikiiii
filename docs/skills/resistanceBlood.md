# Pure Blood

*Lowers the chance of being afflicted with disorders of the blood by 10 % for every skill level, up to a maximum of 70 %.*

<div class="infobox" markdown>

| | |
|---|---|
| **In short** | −10% chance of blood conditions per level ([abbreviations](../glossary.md)) |
| **Category** | Immunity |
| **Max level** | 7 |
| **Obtained via** | Skill points |
| **Unlocks** | [Rejuvenation](rejuvenation.md) |

</div>

## Effect

Lowers the chance of being afflicted with disorders of the blood by 10 % for every skill level, up to a maximum of 70 %. This includes conditions caused by monster attacks such as Poison or bleeding wounds.

## Requirements per skill level

No requirements: any skill point can go here.

<p class="verified">Verified against v0.8.18 game code (`SkillCollection.java`).</p>

See [Conditions](../conditions/index.md#categories-and-resistance) for the conditions this skill affects.

## Unlocks

- [Rejuvenation](rejuvenation.md): needs this skill at level 3


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=resistanceBlood.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=resistanceBlood.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `resistanceBlood` |
    | In-game list position | 20 |
    | Level-up type | `alwaysShown` |
    | Category (internal) | `immunity` |
    | String keys | `skill_title_resistance_blood_disorder`, `skill_longdescription_resistance_blood_disorder` |
    | Values in description | `PER_SKILLPOINT_INCREASE_RESISTANCE_CHANCE_PERCENT` = 10, `PER_SKILLPOINT_INCREASE_RESISTANCE_CHANCE_PERCENT * MAX_LEVEL_RESISTANCE` = 70 |
    | Granting dialogue nodes | – |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

