# ![](../assets/icons/monsters/monsters_tometik8_21.png){ .sprite } Mindless disgrace

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik8_21.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `mindless_disgrace` |
| **Type** | Enemy |
| **Class** | Undead |
| **HP** | 275 |
| **XP when killed** | 740 |
| **Found in** | haunted_house, haunted_house_basement, haunted_underground_1 |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 275 |
| Damage | 13 to 17 |
| Attack chance | 180 |
| Block chance | 143 |
| Damage resistance | 0 |
| Max AP | 12 |
| Attack cost | 3 AP |
| Attacks per turn | 4 |
| Move cost | 3 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Crit chance | 9% |

**When hit:** On target: Mind fog (magnitude 3, 4 rounds, 25% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 65% | 10 to 19 |
| [Tonic of blood](../items/tonic_of_blood.md) | 15% | 1 |
| [Death mace](../items/death_mace.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [haunted_house](../maps/haunted_house.md) | – | 2 | – |
| [haunted_house_basement](../maps/haunted_house_basement.md) | – | 5 | – |
| [haunted_underground_1](../maps/haunted_underground_1.md) | – | 1 | – |
| [haunted_underground_3](../maps/haunted_underground_3.md) | – | 1 | – |
| [haunted_underground_4](../maps/haunted_underground_4.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.3](../versions/0.8.3.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mindless_disgrace.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mindless_disgrace.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mindless_disgrace.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mindless_disgrace.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `mindless_disgrace` |
    | Spawn group | `mindless_disgrace` |
    | Loot table | `mindless_disgrace_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik8:21` |
    | Defined in | `res/raw/monsterlist_haunted_forest.json` |

    Raw data:

    ```json
    {
     "id": "mindless_disgrace",
     "name": "Mindless disgrace",
     "iconID": "monsters_tometik8:21",
     "maxHP": 275,
     "maxAP": 12,
     "moveCost": 3,
     "monsterClass": "undead",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 13,
      "max": 17
     },
     "droplistID": "mindless_disgrace_dl",
     "attackCost": 3,
     "attackChance": 180,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 143,
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "mind_fog",
        "magnitude": 3,
        "duration": 4,
        "chance": "25"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
