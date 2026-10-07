# Unarmed fighting

*When fighting without a weapon and shield, gain 20 attack chance, 2 damage potential and 5 block chance per skill level.*

<div class="infobox" markdown>

| | |
|---|---|
| **In short** | No weapon or shield: +20 AC, +2 dmg, +5 BC per level ([abbreviations](../glossary.md)) |
| **Category** | Proficiency |
| **Max level** | 3 |
| **Obtained via** | First level from a quest, then skill points |

</div>

## Effect

When fighting without a weapon and shield, gain 20 attack chance, 2 damage potential and 5 block chance per skill level.

## Requirements per skill level

| Skill level | Source |
|---|---|
| 1 | Quest reward |
| 2 | Skill point |
| 3 | Skill point |

<p class="verified">Verified against v0.8.18 game code (`SkillCollection.java`).</p>

The first level can only be learned from a quest (see below). After that, further levels are bought with skill points like any other skill.

## Relevant quest

**Quest:** [Destined for great things](../quests/charwood1.md#stage-75) (reaching stage 75)

**NPC:** [Falothen](../monsters/falothen0.md#v-falothen1) (tradehouse0a)

1. Choose “Sounds good. Teach me how to be better at unarmed fighting. Here are two Oegyth crystals and 5,000 gold as…” — **requires:** hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold → +1 level. NPC: “[Falothen teaches you the unarmed fighting skill]”
2. Choose “Sounds good. Teach me how to be better at unarmed fighting.” → +1 level. NPC: “[Falothen teaches you the unarmed fighting skill]”


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=weaponProficiencyUnarmed.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=weaponProficiencyUnarmed.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `weaponProficiencyUnarmed` |
    | In-game list position | 32 |
    | Level-up type | `firstLevelRequiresQuest` |
    | Category (internal) | `proficiency` |
    | String keys | `skill_title_weapon_prof_unarmed`, `skill_longdescription_weapon_prof_unarmed` |
    | Values in description | `PER_SKILLPOINT_INCREASE_UNARMED_AC` = 20, `PER_SKILLPOINT_INCREASE_UNARMED_DMG` = 2, `PER_SKILLPOINT_INCREASE_UNARMED_BC` = 5 |
    | Granting dialogue nodes | `falothen1_2nd_f3`, `falothen1_7_f2` |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

