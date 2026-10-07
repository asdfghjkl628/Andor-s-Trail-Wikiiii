# Cleave

*Gives +3 action points (AP) on every kill per skill level.*

<div class="infobox" markdown>

| | |
|---|---|
| **In short** | +3 AP per kill per level ([abbreviations](../glossary.md)) |
| **Category** | Offense |
| **Max level** | Unlimited |
| **Obtained via** | Skill points |
| **Also from quests** | Yes |

</div>

## Effect

Gives +3 action points (AP) on every kill per skill level.

## Requirements per skill level

| Skill level | [Weapon Accuracy](weaponChance.md) level | [Hard Hit](weaponDmg.md) level |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| … | +1 per level | +1 per level |

<p class="verified">Verified against v0.8.18 game code (`SkillCollection.java`).</p>

## Relevant quest

**Quest:** [The exploded star](../quests/mg2_exploded_star.md#stage-62) (reaching stage 62)

**NPC:** [Pangitain](../monsters/brv_fortune_teller.md) (brimhaven_fortune_teller)

1. Choose “Sounds great - I choose this one. [Touch the item]” — **requires:** hand over 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md) → +1 level. NPC: “A good choice. Do you feel it already?”


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=cleave.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=cleave.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `cleave` |
    | In-game list position | 11 |
    | Level-up type | `alwaysShown` |
    | Category (internal) | `offense` |
    | String keys | `skill_title_cleave`, `skill_longdescription_cleave` |
    | Values in description | `PER_SKILLPOINT_INCREASE_CLEAVE_AP` = 3 |
    | Granting dialogue nodes | `brv_fortune_back_68b` |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

