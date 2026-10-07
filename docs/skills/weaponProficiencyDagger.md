# Dagger proficiency

*For each skill level, increases attack chance when using daggers and shortswords by 30 % of the item's base attack chance, increases block chance by 30 % of the…*

<div class="infobox" markdown>

| | |
|---|---|
| **Category** | Proficiency |
| **Max level** | 3 |
| **Obtained via** | First level from a quest, then skill points |

</div>

## Effect

For each skill level, increases attack chance when using daggers and shortswords by 30 % of the item's base attack chance, increases block chance by 30 % of the item's base block chance, and increases critical skill by 10 % of the item's base critical skill.

## Requirements per skill level

| Skill level | Source |
|---|---|
| 1 | Quest reward |
| 2 | Skill point |
| 3 | Skill point |

<p class="verified">Verified against v0.8.18 game code (`SkillCollection.java`).</p>

The first level can only be learned from a quest (see below). After that, further levels are bought with skill points like any other skill.

## Relevant quest

**Quest:** [Destined for great things](../quests/charwood1.md#stage-72) (reaching stage 72)

**NPC:** [Falothen](../monsters/falothen0.md#v-falothen1) (tradehouse0a)

1. Choose “Sounds good. Teach me how to fight with daggers. Here are two Oegyth crystals and 5,000 gold as payment.” — **requires:** hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold → +1 level. NPC: “[Falothen teaches you the dagger skill]”
2. Choose “Sounds good. Teach me how to fight with daggers.” → +1 level. NPC: “[Falothen teaches you the dagger skill]”


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=weaponProficiencyDagger.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=weaponProficiencyDagger.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `weaponProficiencyDagger` |
    | In-game list position | 27 |
    | Level-up type | `firstLevelRequiresQuest` |
    | Category (internal) | `proficiency` |
    | String keys | `skill_title_weapon_prof_dagger`, `skill_longdescription_weapon_prof_dagger` |
    | Values in description | `PER_SKILLPOINT_INCREASE_WEAPON_PROF_AC_PERCENT` = 30, `PER_SKILLPOINT_INCREASE_WEAPON_PROF_BC_PERCENT` = 30, `PER_SKILLPOINT_INCREASE_WEAPON_PROF_CS_PERCENT` = 10 |
    | Granting dialogue nodes | `falothen1_2nd_d3`, `falothen1_7_d2` |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

