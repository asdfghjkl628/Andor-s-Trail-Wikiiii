# ![](../assets/icons/monsters/monsters_karvis1_0.png){ .sprite } Ancient kobold

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_karvis1_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `kobold3` |
| **Type** | Enemy |
| **Class** | Humanoid |
| **HP** | 70 |
| **XP when killed** | 273 |
| **Found in** | guynmart_wood_18, guynmart_wood_18b |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 70 |
| Damage | 1 to 10 |
| Attack chance | 140 |
| Block chance | 80 |
| Damage resistance | 12 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Crit chance | 9% |

**On hit:** On target: Confusion (magnitude 1, 3 rounds, 5% chance); Confusion (magnitude 1, 6 rounds, 1% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 5% | 1 to 5 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [guynmart_wood_18](../maps/guynmart_wood_18.md) | – | 3 | – |
| [guynmart_wood_18b](../maps/guynmart_wood_18b.md) | – | 3 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kobold3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kobold3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kobold3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kobold3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `kobold3` |
    | Spawn group | `kobold3` |
    | Loot table | `kobold` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_karvis1:0` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "kobold3",
     "name": "Ancient kobold",
     "iconID": "monsters_karvis1:0",
     "maxHP": 70,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 1,
      "max": 10
     },
     "droplistID": "kobold",
     "attackCost": 3,
     "attackChance": 140,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 80,
     "damageResistance": 12,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "confusion",
        "magnitude": 1,
        "duration": 3,
        "chance": "5"
       },
       {
        "condition": "confusion",
        "magnitude": 1,
        "duration": 6,
        "chance": "1"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
