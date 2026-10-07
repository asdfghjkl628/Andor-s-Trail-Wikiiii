# Shield proficiency

*Increase damage resistance by 1 per skill level while having a shield or parrying weapon equipped.*

<div class="infobox" markdown>

| | |
|---|---|
| **In short** | With a shield or parrying weapon: +1 DR per level ([abbreviations](../glossary.md)) |
| **Category** | Proficiency |
| **Max level** | 2 |
| **Obtained via** | First level from a quest, then skill points |

</div>

## Effect

Increase damage resistance by 1 per skill level while having a shield or parrying weapon equipped.

## Requirements per skill level

| Skill level | Source |
|---|---|
| 1 | Quest reward |
| 2 | Skill point |

<p class="verified">Verified against v0.8.18 game code (`SkillCollection.java`).</p>

The first level can only be learned from a quest (see below). After that, further levels are bought with skill points like any other skill.

## Relevant quest

**Quest:** [Destined for great things](../quests/charwood1.md#stage-91) (reaching stage 91)

**NPC:** [Fayvara](../monsters/fayvara0.md#v-fayvara1) (tradehouse0a)

1. Choose “Sounds good. Teach me about shields. Here are two Oegyth crystals and 6,000 gold as payment.” — **requires:** hand over 2× [Oegyth crystal](../items/oegyth.md); pay 6,000 gold → +1 level. NPC: “[Fayvara teaches you the shield skill]”
2. Choose “Sounds good. Teach me about shields and parrying weapons.” → +1 level. NPC: “[Fayvara teaches you the shield skill]”


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=armorProficiencyShield.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=armorProficiencyShield.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `armorProficiencyShield` |
    | In-game list position | 34 |
    | Level-up type | `firstLevelRequiresQuest` |
    | Category (internal) | `proficiency` |
    | String keys | `skill_title_armor_prof_shield`, `skill_longdescription_armor_prof_shield` |
    | Values in description | `PER_SKILLPOINT_INCREASE_SHIELD_PROF_DR` = 1 |
    | Granting dialogue nodes | `fayvara1_2nd_s3`, `fayvara1_7_s2` |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

