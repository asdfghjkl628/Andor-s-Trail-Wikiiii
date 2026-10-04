# Weapon Accuracy

*Increases attack chance by 12 percentage points for each skill level.*

<div class="infobox" markdown>

| | |
|---|---|
| **Category** | Offense |
| **Max level** | Unlimited |
| **Obtained via** | Skill points |
| **Also from quests** | Yes |
| **Unlocks** | [Cleave](cleave.md), [Concussion](concussion.md) |

</div>

## Effect

Increases attack chance by 12 percentage points for each skill level.

## Requirements per skill level

No requirements: any skill point can go here.

<p class="verified">Verified against v0.8.18 game code (`SkillCollection.java`).</p>
## Unlocks

- [Cleave](cleave.md): needs this skill at level 1
- [Concussion](concussion.md): needs this skill at level 3

## Relevant quest

**Quest:** [The exploded star](../quests/mg2_exploded_star.md#stage-62) (reaching stage 62)

**NPC:** [Pangitain](../monsters/brv_fortune_teller.md) (brimhaven_fortune_teller)

1. Choose “Sounds great - I choose this one. [Touch the item]” — **requires:** hand over 10× [Piece of bright shining crystal](../items/mg2_exploded_star.md) → +1 level. NPC: “A good choice. Do you feel it already?”

**Quest:** [galmore_nondisplayed](../quests/galmore_nondisplayed.md#stage-51) (reaching stage 51)

**Source:** a scripted event, not a regular conversation

1. Choose “(continue)” — **requires:** not yet reached stage 51 of [galmore_nondisplayed](../quests/galmore_nondisplayed.md) → +1 level. NPC: “You brush aside the branches and find an old chest tucked behind the tree. Inside lies a weathered tome, bound in…”


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Trivia**: real-world facts, references, development history</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=weaponChance.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/skills?filename=weaponChance.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Skill ID | `weaponChance` |
    | In-game list position | 1 |
    | Level-up type | `alwaysShown` |
    | Category (internal) | `offense` |
    | String keys | `skill_title_weapon_chance`, `skill_longdescription_weapon_chance` |
    | Values in description | `PER_SKILLPOINT_INCREASE_WEAPON_CHANCE` = 12 |
    | Granting dialogue nodes | `brv_fortune_back_61b`, `galmore_23_unknown_book_10` |
    | Source files | `model/ability/SkillCollection.java`, `activity/SkillInfoActivity.java`, `res/values/strings.xml` |

