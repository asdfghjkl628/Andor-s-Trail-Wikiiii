# ![](../assets/icons/monsters/monsters_rltiles2_29.png){ .sprite } Young gornaud

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_29.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `young_gornaud` |
| **Type** | Enemy |
| **Class** | Giant |
| **HP** | 70 |
| **XP when killed** | 146 |
| **Found in** | Stoutford, Blackwater Mountain, Prim |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 70 |
| Damage | 0 to 15 |
| Attack chance | 70 |
| Block chance | 50 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**On hit:** On target: Dazed (magnitude 1, 5 rounds, 20% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 30 |
| [Meat](../items/meat.md) | 5% | 1 |
| [Animal hair](../items/hair.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain1](../maps/blackwater_mountain1.md) | Stoutford | 2 | – |
| [blackwater_mountain15](../maps/blackwater_mountain15.md) | Blackwater Mountain | 5 | – |
| [blackwater_mountain16](../maps/blackwater_mountain16.md) | Blackwater Mountain | 5 | – |
| [blackwater_mountain2](../maps/blackwater_mountain2.md) | – | 6 | – |
| [blackwater_mountain3](../maps/blackwater_mountain3.md) | – | 1 | – |
| [blackwater_mountain4](../maps/blackwater_mountain4.md) | – | 1 | – |
| [blackwater_mountain4a](../maps/blackwater_mountain4a.md) | – | 3 | – |
| [blackwater_mountain5](../maps/blackwater_mountain5.md) | – | 3 | – |
| [blackwater_mountain53](../maps/blackwater_mountain53.md) | Blackwater Mountain | 3 | – |
| [blackwater_mountain56](../maps/blackwater_mountain56.md) | Blackwater Mountain | 6 | – |
| [blackwater_mountain5a](../maps/blackwater_mountain5a.md) | – | 4 | – |
| [blackwater_mountain7](../maps/blackwater_mountain7.md) | Prim | 5 | – |
| [blackwater_mountain9](../maps/blackwater_mountain9.md) | Prim | 2 | – |
| [bwmfill1](../maps/bwmfill1.md) | Blackwater Mountain | 2 | – |
| [bwmfill2](../maps/bwmfill2.md) | Blackwater Mountain | 1 | – |
| [bwmfill4](../maps/bwmfill4.md) | Blackwater Mountain | 1 | – |
| [bwmfill5](../maps/bwmfill5.md) | Blackwater Mountain | 1 | – |
| [bwmfill6](../maps/bwmfill6.md) | Blackwater Mountain | 1 | – |
| [bwmfill7](../maps/bwmfill7.md) | Blackwater Mountain | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 20, "c… → {"conditionsTarget": [{"chance": "20", … |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=young_gornaud.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=young_gornaud.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=young_gornaud.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=young_gornaud.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `young_gornaud` |
    | Spawn group | `gornaud_1` |
    | Loot table | `gornaud_1` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:29` |
    | Defined in | `res/raw/monsterlist_v069_monsters.json` |

    Raw data:

    ```json
    {
     "id": "young_gornaud",
     "name": "Young gornaud",
     "iconID": "monsters_rltiles2:29",
     "maxHP": 70,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 0,
      "max": 15
     },
     "spawnGroup": "gornaud_1",
     "droplistID": "gornaud_1",
     "attackCost": 5,
     "attackChance": 70,
     "blockChance": 50,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "dazed",
        "magnitude": 1,
        "duration": 5,
        "chance": "20"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
