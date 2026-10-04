# Increased Fortitude

*On every subsequent level-up, maximum health points (HP) will be raised by 1 per skill level.*

<div class="infobox" markdown>

| | |
|---|---|
| **Category** | Immunity |
| **Max level** | Unlimited |
| **Obtained via** | Skill points |
| **Also from quests** | Yes |
| **Unlocks** | [Regeneration](regeneration.md) |

</div>

## Effect

On every subsequent level-up, maximum health points (HP) will be raised by 1 per skill level. This is not applied retroactively, only subsequent level-ups will be affected.

## Requirements per skill level

| Skill level | Character level |
|---|---|
| 1 | 5 |
| 2 | 20 |
| 3 | 35 |
| 4 | 50 |
| 5 | 65 |
| … | +15 per level |

<p class="verified">Verified against v0.8.18 game code (`SkillCollection.java`).</p>
## Unlocks

- [Regeneration](regeneration.md): needs this skill at level 1

## Relevant quest

**Quest:** [The exploded star](../quests/mg2_exploded_star.md#stage-62) (reaching stage 62)

**NPC:** [Pangitain](../monsters/brv_fortune_teller.md) (brimhaven_fortune_teller)

1. Choose “Sounds great - I choose this one. [Touch the item]” — **requires:** hand over 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md) → +1 level. NPC: “A good choice. Do you feel it already?”


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=fortitude.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=fortitude.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `fortitude` |
    | In-game list position | 13 |
    | Level-up type | `alwaysShown` |
    | Category (internal) | `immunity` |
    | String keys | `skill_title_fortitude`, `skill_longdescription_fortitude` |
    | Values in description | `PER_SKILLPOINT_INCREASE_FORTITUDE_HEALTH` = 1 |
    | Granting dialogue nodes | `brv_fortune_back_62b` |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

