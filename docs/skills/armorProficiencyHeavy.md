# Heavy armor proficiency

*For every skill level, increases the block chance of every piece of heavy armor being worn by 20 % of their original block chances.*

<div class="infobox" markdown>

| | |
|---|---|
| **Category** | Proficiency |
| **Max level** | 4 |
| **Obtained via** | First level from a quest, then skill points |

</div>

## Effect

For every skill level, increases the block chance of every piece of heavy armor being worn by 20 % of their original block chances. Pieces of heavy armor have their movement penalties reduced by 25 % per skill level, their attack speed penalties reduced by 25 % per skill level, and their item use cost penalties reduced by 25 % per skill level. Heavy armors include metal armors, chain mail and plate mail.

## Requirements per skill level

| Skill level | Source |
|---|---|
| 1 | Quest reward |
| 2 | Skill point |
| 3 | Skill point |
| 4 | Skill point |

<p class="verified">Verified against v0.8.18 game code (`SkillCollection.java`).</p>

The first level can only be learned from a quest (see below). After that, further levels are bought with skill points like any other skill.

## Relevant quest

**Quest:** [Destined for great things](../quests/charwood1.md#stage-93) (reaching stage 93)

**NPC:** [Fayvara](../monsters/fayvara1.md) (tradehouse0a)

1. Choose “Sounds good. Teach me about heavy armors. Here are two Oegyth crystals and 6,000 gold as payment.” — **requires:** hand over 2× [Oegyth crystal](../items/oegyth.md); pay 6,000 gold → +1 level. NPC: “[Fayvara teaches you the heavy armor skill]”
2. Choose “Sounds good. Teach me about heavy armors.” → +1 level. NPC: “[Fayvara teaches you the heavy armor skill]”


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=armorProficiencyHeavy.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=armorProficiencyHeavy.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `armorProficiencyHeavy` |
    | In-game list position | 37 |
    | Level-up type | `firstLevelRequiresQuest` |
    | Category (internal) | `proficiency` |
    | String keys | `skill_title_armor_prof_heavy`, `skill_longdescription_armor_prof_heavy` |
    | Values in description | `PER_SKILLPOINT_INCREASE_HEAVY_ARMOR_BC_PERCENT` = 20, `PER_SKILLPOINT_INCREASE_HEAVY_ARMOR_MOVECOST_PERCENT` = 25, `PER_SKILLPOINT_INCREASE_HEAVY_ARMOR_ATKCOST_PERCENT` = 25, `PER_SKILLPOINT_INCREASE_HEAVY_ARMOR_USECOST_PERCENT` = 25 |
    | Granting dialogue nodes | `fayvara1_2nd_h3`, `fayvara1_7_h2` |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

