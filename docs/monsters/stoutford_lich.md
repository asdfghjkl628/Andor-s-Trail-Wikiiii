# ![](../assets/icons/monsters/monsters_liches_0.png){ .sprite } Eliszylae

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_liches_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `stoutford_lich` |
| **Type** | Enemy |
| **Class** | Undead |
| **HP** | 135 |
| **XP when killed** | 296 |
| **Found in** | Stoutford |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 135 |
| Damage | 1 to 6 |
| Attack chance | 80 |
| Block chance | 90 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 2 AP |
| Attacks per turn | 5 |
| Move cost | 5 AP |
| Critical skill | 40 |
| Critical multiplier | 2.0 |
| Crit chance | 23% |

**On hit:** Heal HP: 2 to 4; On target: Minor weapon feebleness (magnitude 2, 2 rounds, 15% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Demon heart](../items/eliszylae_heart.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 150 to 200 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [stoutford_cellar2](../maps/stoutford_cellar2.md) | Stoutford | 1 | – |


## Quests that count kills

- [Rumblings](../quests/rumblings.md#stage-50) with stepping on a trigger on [stoutford_cellar2](../maps/stoutford_cellar2.md) checks that you've killed at least 1


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `stoutford_lich` |
    | Spawn group | `stoutford_lich` |
    | Loot table | `eliszylae_droplist` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_liches:0` |
    | Defined in | `res/raw/monsterlist_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_lich",
     "name": "Eliszylae",
     "iconID": "monsters_liches:0",
     "maxHP": 135,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 1,
      "max": 6
     },
     "spawnGroup": "stoutford_lich",
     "droplistID": "eliszylae_droplist",
     "attackCost": 2,
     "attackChance": 80,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 90,
     "damageResistance": 2,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 2,
       "max": 4
      },
      "conditionsTarget": [
       {
        "condition": "feebleness_minor",
        "magnitude": 2,
        "duration": 2,
        "chance": "15"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
