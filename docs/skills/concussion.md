# Concussion

*When making an attack on a target whose block chance (BC) is at least 50 lower than your attack chance (AC), there is a 15 % chance that the hit will cause a…*

<div class="infobox" markdown>

| | |
|---|---|
| **Category** | Offense |
| **Max level** | 1 |
| **Obtained via** | Skill points |

</div>

## Effect

When making an attack on a target whose block chance (BC) is at least 50 lower than your attack chance (AC), there is a 15 % chance that the hit will cause a concussion on the target. A concussion will severely lower the target's offensive combat abilities, making the target less able to land successful attacks.

## Requirements per skill level

| Skill level | [Combat Speed](speed.md) level | [Weapon Accuracy](weaponChance.md) level | [Hard Hit](weaponDmg.md) level |
|---|---|---|---|
| 1 | 2 | 3 | 5 |

<p class="verified">Verified against v0.8.18 game code (`SkillCollection.java`).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=concussion.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=concussion.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `concussion` |
    | In-game list position | 26 |
    | Level-up type | `alwaysShown` |
    | Category (internal) | `offense` |
    | String keys | `skill_title_concussion`, `skill_longdescription_concussion` |
    | Values in description | `CONCUSSION_THRESHOLD` = 50, `PER_SKILLPOINT_INCREASE_CONCUSSION_CHANCE` = 15 |
    | Granting dialogue nodes | – |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

