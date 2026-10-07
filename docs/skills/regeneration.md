# Regeneration

*Gain +1 health points (HP) on every round per skill level when no monsters are directly adjacent.*

<div class="infobox" markdown>

| | |
|---|---|
| **In short** | +1 HP per round when no enemy is adjacent, per level ([abbreviations](../glossary.md)) |
| **Category** | Immunity |
| **Max level** | Unlimited |
| **Obtained via** | Skill points |

</div>

## Effect

Gain +1 health points (HP) on every round per skill level when no monsters are directly adjacent.

## Requirements per skill level

| Skill level | Base max HP | [Increased Fortitude](fortitude.md) level |
|---|---|---|
| 1 | 30 | 1 |
| 2 | 60 | 2 |
| 3 | 90 | 3 |
| 4 | 120 | 4 |
| 5 | 150 | 5 |
| … | +30 per level | +1 per level |

<p class="verified">Verified against v0.8.18 game code (`SkillCollection.java`).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=regeneration.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=regeneration.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `regeneration` |
    | In-game list position | 15 |
    | Level-up type | `alwaysShown` |
    | Category (internal) | `immunity` |
    | String keys | `skill_title_regeneration`, `skill_longdescription_regeneration` |
    | Values in description | `PER_SKILLPOINT_INCREASE_REGENERATION` = 1 |
    | Granting dialogue nodes | – |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

