# ![](../assets/icons/monsters/monsters_newb_1_570.png){ .sprite } Steelthorn hexileg

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_570.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `steelthorn_hexileg` |
| **Type** | Enemy |
| **Class** | Insect |
| **HP** | 211 |
| **XP when killed** | 514 |
| **Found in** | Flagstone Prison |
| **Introduced** | [v0.8.8](../versions/0.8.8.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 211 |
| Damage | 4 to 6 |
| Attack chance | 120 |
| Block chance | 167 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**On hit:** On target: Venom (magnitude 2, 4 rounds, 25% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Hexi egg](../items/hexi_egg.md) | 8% | 1 to 2 |
| [Gold coins](../items/gold.md) | 9% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [lake_shore_road_5](../maps/lake_shore_road_5.md) | Flagstone Prison | 1 | – |
| [lake_shore_road_6](../maps/lake_shore_road_6.md) | Flagstone Prison | 2 | – |
| [rat_mountain_4](../maps/rat_mountain_4.md) | – | 3 | – |
| [rat_mountain_5](../maps/rat_mountain_5.md) | Flagstone Prison | 5 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=steelthorn_hexileg.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=steelthorn_hexileg.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=steelthorn_hexileg.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=steelthorn_hexileg.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `steelthorn_hexileg` |
    | Spawn group | `steelthorn_hexileg` |
    | Loot table | `steelthorn_hexileg_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_newb_1:570` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "steelthorn_hexileg",
     "name": "Steelthorn hexileg",
     "iconID": "monsters_newb_1:570",
     "maxHP": 211,
     "moveCost": 5,
     "monsterClass": "insect",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 4,
      "max": 6
     },
     "droplistID": "steelthorn_hexileg_dl",
     "attackCost": 3,
     "attackChance": 120,
     "blockChance": 167,
     "damageResistance": 5,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "venom",
        "magnitude": 2,
        "duration": 4,
        "chance": "25"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
