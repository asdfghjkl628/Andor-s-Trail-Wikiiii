# Light armor proficiency

*For every skill level, increases the block chance of every piece of light armor being worn by 30 % of their original block chances.*

<div class="infobox" markdown>

| | |
|---|---|
| **Category** | Proficiency |
| **Max level** | 3 |
| **Obtained via** | First level from a quest, then skill points |

</div>

## Effect

For every skill level, increases the block chance of every piece of light armor being worn by 30 % of their original block chances. Light armors include leather, light metal and hide armors.

## Requirements per skill level

| Skill level | Source |
|---|---|
| 1 | Quest reward |
| 2 | Skill point |
| 3 | Skill point |

<p class="verified">Verified against v0.8.18 game code (`SkillCollection.java`).</p>

The first level can only be learned from a quest (see below). After that, further levels are bought with skill points like any other skill.

## Relevant quest

**Quest:** [Destined for great things](../quests/charwood1.md#stage-92) (reaching stage 92)

**NPC:** [Fayvara](../monsters/fayvara0.md#v-fayvara1) (tradehouse0a)

1. Choose “Sounds good. Teach me about light armors. Here are two Oegyth crystals and 6,000 gold as payment.” — **requires:** hand over 2× [Oegyth crystal](../items/oegyth.md); pay 6,000 gold → +1 level. NPC: “[Fayvara teaches you the light armor skill]”
2. Choose “Sounds good. Teach me about light armors.” → +1 level. NPC: “[Fayvara teaches you the light armor skill]”


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=armorProficiencyLight.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=armorProficiencyLight.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `armorProficiencyLight` |
    | In-game list position | 36 |
    | Level-up type | `firstLevelRequiresQuest` |
    | Category (internal) | `proficiency` |
    | String keys | `skill_title_armor_prof_light`, `skill_longdescription_armor_prof_light` |
    | Values in description | `PER_SKILLPOINT_INCREASE_LIGHT_ARMOR_BC_PERCENT` = 30 |
    | Granting dialogue nodes | `fayvara1_2nd_l3`, `fayvara1_7_l2` |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

