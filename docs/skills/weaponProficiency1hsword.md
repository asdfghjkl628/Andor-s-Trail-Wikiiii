# One-handed sword proficiency

*For each skill level, increases attack chance of rapiers, longswords and broadswords by 30 % of the item's base attack chance, increases block chance by 30 % of the…*

<div class="infobox" markdown>

| | |
|---|---|
| **In short** | Longswords, broadswords, rapiers: +30% of weapon AC and BC, +10% of its CS, per level ([abbreviations](../glossary.md)) |
| **Category** | Proficiency |
| **Max level** | 3 |
| **Obtained via** | First level from a quest, then skill points |

</div>

## Effect

For each skill level, increases attack chance of rapiers, longswords and broadswords by 30 % of the item's base attack chance, increases block chance by 30 % of the item's base block chance, and increases critical skill by 10 % of the item's base critical skill.

## Requirements per skill level

| Skill level | Source |
|---|---|
| 1 | Quest reward |
| 2 | Skill point |
| 3 | Skill point |

<p class="verified">Verified against v0.8.18 game code (`SkillCollection.java`).</p>

The first level can only be learned from a quest (see below). After that, further levels are bought with skill points like any other skill.

## Relevant quest

**Quest:** [Destined for great things](../quests/charwood1.md#stage-70) (reaching stage 70)

**NPC:** [Falothen](../monsters/falothen0.md#v-falothen1) (tradehouse0a)

1. Choose “Sounds good. Teach me how to fight with one-handed swords. Here are two Oegyth crystals and 5,000 gold as…” — **requires:** hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold → +1 level. NPC: “[Falothen teaches you the one-handed sword skill]”
2. Choose “Sounds good. Teach me how to fight with one-handed swords.” → +1 level. NPC: “[Falothen teaches you the one-handed sword skill]”


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=weaponProficiency1hsword.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=weaponProficiency1hsword.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `weaponProficiency1hsword` |
    | In-game list position | 28 |
    | Level-up type | `firstLevelRequiresQuest` |
    | Category (internal) | `proficiency` |
    | String keys | `skill_title_weapon_prof_1hsword`, `skill_longdescription_weapon_prof_1hsword` |
    | Values in description | `PER_SKILLPOINT_INCREASE_WEAPON_PROF_AC_PERCENT` = 30, `PER_SKILLPOINT_INCREASE_WEAPON_PROF_BC_PERCENT` = 30, `PER_SKILLPOINT_INCREASE_WEAPON_PROF_CS_PERCENT` = 10 |
    | Granting dialogue nodes | `falothen1_2nd_1hs3`, `falothen1_7_1hs2` |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

