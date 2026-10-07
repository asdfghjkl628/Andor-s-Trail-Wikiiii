# ![](../assets/icons/monsters/monsters_tometik4_3.png){ .sprite } Three-eyed bat

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik4_3.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `three_eyed_bat` |
| **Type** | Enemy |
| **Class** | Animal |
| **HP** | 108 |
| **XP when killed** | 356 |
| **Found in** | haunted_underground_1, haunted_underground_2, haunted_underground_3 |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 108 |
| Damage | 16 to 17 |
| Attack chance | 165 |
| Block chance | 189 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Crit chance | 9% |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Bat wing](../items/bat_wing.md) | 25% | 1 to 2 |
| [Bat eye](../items/eye_ball.md) | 25% | 1 to 3 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [haunted_underground_1](../maps/haunted_underground_1.md) | – | 3 | – |
| [haunted_underground_2](../maps/haunted_underground_2.md) | – | 5 | – |
| [haunted_underground_3](../maps/haunted_underground_3.md) | – | 4 | – |
| [haunted_underground_4](../maps/haunted_underground_4.md) | – | 3 | – |
| [haunted_underground_5](../maps/haunted_underground_5.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.3](../versions/0.8.3.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=three_eyed_bat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=three_eyed_bat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=three_eyed_bat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=three_eyed_bat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `three_eyed_bat` |
    | Spawn group | `three_eyed_bat` |
    | Loot table | `three_eyed_bat_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_tometik4:3` |
    | Defined in | `res/raw/monsterlist_haunted_forest.json` |

    Raw data:

    ```json
    {
     "id": "three_eyed_bat",
     "name": "Three-eyed bat",
     "iconID": "monsters_tometik4:3",
     "maxHP": 108,
     "maxAP": 10,
     "moveCost": 3,
     "monsterClass": "animal",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 16,
      "max": 17
     },
     "droplistID": "three_eyed_bat_dl",
     "attackCost": 4,
     "attackChance": 165,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 189
    }
    ```


<small>Data from v0.8.18</small>
