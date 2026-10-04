# Evasion

*For every skill level, reduces both the chance of failed flee attempts by 5 % and the chance that an adjacent monster will attack by 5 %.*

<div class="infobox" markdown>

| | |
|---|---|
| **Category** | Defense |
| **Max level** | 4 |
| **Obtained via** | Skill points |
| **Also from quests** | Yes |
| **Unlocks** | [Taunt](taunt.md) |

</div>

## Effect

For every skill level, reduces both the chance of failed flee attempts by 5 % and the chance that an adjacent monster will attack by 5 %.

## Requirements per skill level

No requirements: any skill point can go here.

<p class="verified">Verified against v0.8.18 game code (`SkillCollection.java`).</p>

## Unlocks

- [Taunt](taunt.md): needs this skill at level 2

## Relevant quest

**Quest:** [Yellow is it](../quests/ratdom_quest.md#stage-210) (reaching stage 210)

**NPC:** [Whootibarfag](../monsters/whootibarfag.md) (blackwater_mountain55)

1. Choose “[You hold your breath - from tension, and because of his bad breath.]” → +1 level. NPC: “Whootibarfag let you in on the secret of the rat escape. This increases your ability to flee and escape.”


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=evasion.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=evasion.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `evasion` |
    | In-game list position | 14 |
    | Level-up type | `alwaysShown` |
    | Category (internal) | `defense` |
    | String keys | `skill_title_evasion`, `skill_longdescription_evasion` |
    | Values in description | `PER_SKILLPOINT_INCREASE_EVASION_FLEE_CHANCE_PERCENTAGE` = 5, `PER_SKILLPOINT_INCREASE_EVASION_MONSTER_ATTACK_CHANCE_PERCENTAGE` = 5 |
    | Granting dialogue nodes | `whootibarfag_230` |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

