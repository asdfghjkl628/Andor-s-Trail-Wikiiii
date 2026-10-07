# ![](../assets/icons/monsters/monsters_arulirs_14.png){ .sprite } Demonic Arulir

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_arulirs_14.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `arulir_8` |
| **Type** | Enemy |
| **Class** | Giant |
| **HP** | 750 |
| **XP when killed** | 970 |
| **Found in** | arulircave6 |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 750 |
| Damage | 4 to 20 |
| Attack chance | 110 |
| Block chance | 32 |
| Damage resistance | 14 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 50 |
| Critical multiplier | 3.0 |
| Crit chance | 26% |

**On hit:** On target: Stunned (magnitude 1, 4 rounds, 30% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Arulir skin](../items/arulir_skin.md) | 10% | 1 |
| [Gold coins](../items/gold.md) | 70% | 10 to 60 |
| [Hunter's Sword](../items/hunters_sword.md) | 0.1% | 1 |
| [Blue Crystals](../items/crystal_blue.md) | 3% | 1 |
| [Red Crystals](../items/crystal_red.md) | 3% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [arulircave6](../maps/arulircave6.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arulir_8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arulir_8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arulir_8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arulir_8.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `arulir_8` |
    | Spawn group | `arulir_4` |
    | Loot table | `arulir_demonic` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_arulirs:14` |
    | Defined in | `res/raw/monsterlist_arulir_mountain.json` |

    Raw data:

    ```json
    {
     "id": "arulir_8",
     "name": "Demonic Arulir",
     "iconID": "monsters_arulirs:14",
     "maxHP": 750,
     "maxAP": 10,
     "moveCost": 10,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 4,
      "max": 20
     },
     "spawnGroup": "arulir_4",
     "droplistID": "arulir_demonic",
     "attackCost": 5,
     "attackChance": 110,
     "criticalSkill": 50,
     "criticalMultiplier": 3.0,
     "blockChance": 32,
     "damageResistance": 14,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "stunned",
        "magnitude": 1,
        "duration": 4,
        "chance": "30"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
