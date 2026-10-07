# ![](../assets/icons/monsters/monsters_rltiles1_83.png){ .sprite } Tunlon

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_83.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `tunlon2` |
| **Type** | Enemy |
| **Class** | Humanoid |
| **HP** | 73 |
| **XP when killed** | 292 |
| **Found in** | Blackwater Mountain |
| **Introduced** | [v0.8.10](../versions/0.8.10.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 73 |
| Damage | 9 to 17 |
| Attack chance | 200 |
| Block chance | 90 |
| Damage resistance | 10 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 4 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Crit chance | 9% |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 1000 to 2000 |
| [Quarterstaff](../items/qtrstaff.md) | 100% | 1 |
| [Green Pepper](../items/green_pepper.md) | 70% | 1 to 2 |
| [Yellow Pepper](../items/yellow_pepper.md) | 60% | 1 to 2 |
| [Red Pepper](../items/red_pepper.md) | 50% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [bwmfill3](../maps/bwmfill3.md) | Blackwater Mountain | 1 | appears later in a quest |


## Version history

| Version | Change |
|---|---|
| [v0.8.10](../versions/0.8.10.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tunlon2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tunlon2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tunlon2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tunlon2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `tunlon2` |
    | Spawn group | `tunlon2` |
    | Loot table | `tunlon2` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_rltiles1:83` |
    | Defined in | `res/raw/monsterlist_bwmfill.json` |

    Raw data:

    ```json
    {
     "id": "tunlon2",
     "name": "Tunlon",
     "iconID": "monsters_rltiles1:83",
     "maxHP": 73,
     "maxAP": 10,
     "moveCost": 4,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 9,
      "max": 17
     },
     "spawnGroup": "tunlon2",
     "droplistID": "tunlon2",
     "attackCost": 5,
     "attackChance": 200,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 90,
     "damageResistance": 10
    }
    ```


<small>Data from v0.8.18</small>
