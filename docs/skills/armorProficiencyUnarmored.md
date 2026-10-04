# Unarmored fighting

*While fighting without having any piece of armor equipped, gain 10 block chance per skill level.*

<div class="infobox" markdown>

| | |
|---|---|
| **Category** | Proficiency |
| **Max level** | 3 |
| **Obtained via** | First level from a quest, then skill points |

</div>

## Effect

While fighting without having any piece of armor equipped, gain 10 block chance per skill level. Items made of cloth are not considered as being armor.

## Requirements per skill level

| Skill level | Source |
|---|---|
| 1 | Quest reward |
| 2 | Skill point |
| 3 | Skill point |

The first level can only be learned from a quest (see below). After that, further levels are bought with skill points like any other skill.

## Relevant quest

**Quest:** [Destined for great things](../quests/charwood1.md#stage-94) (reaching stage 94)

**NPC:** [Fayvara](../monsters/fayvara1.md) (tradehouse0a)

1. Choose “Sounds good. Teach me about unarmored combat. Here are two Oegyth crystals and 6,000 gold as payment.” — **requires:** hand over 2× [Oegyth crystal](../items/oegyth.md); pay 6,000 gold → +1 level. NPC: “[Fayvara teaches you the unarmored combat skill]”
2. Choose “Sounds good. Teach me about unarmored combat.” → +1 level. NPC: “[Fayvara teaches you the unarmored combat skill]”


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=armorProficiencyUnarmored.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=armorProficiencyUnarmored.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `armorProficiencyUnarmored` |
    | In-game list position | 35 |
    | Level-up type | `firstLevelRequiresQuest` |
    | Category (internal) | `proficiency` |
    | String keys | `skill_title_armor_prof_unarmored`, `skill_longdescription_armor_prof_unarmored` |
    | Values in description | `PER_SKILLPOINT_INCREASE_UNARMORED_BC` = 10 |
    | Granting dialogue nodes | `fayvara1_2nd_u3`, `fayvara1_7_u2` |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

