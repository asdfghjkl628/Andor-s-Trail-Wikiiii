---
description: "Young spitting serpent is an enemy in Andor's Trail (reptile) with 50 HP, worth 123 XP, found in Lake Laeroth. Drops: Serpent meat, Gold coins."
---

# ![](../assets/icons/monsters/monsters_snakes_5.png){ .sprite } Young spitting serpent

**Found in:** Lake Laeroth: [laerothisland0](../maps/laerothisland0.md), Lake Laeroth: [laerothisland1](../maps/laerothisland1.md), Lake Laeroth: [laerothisland2](../maps/laerothisland2.md), Lake Laeroth: [laerothisland3](../maps/laerothisland3.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_snakes_5.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Lake Laeroth |
| **Class** | Reptile |
| **HP** | 50 |
| **XP when defeated** | 123 |
| **Entry ID** | `spit_serpent_2` |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 50 |
| XP when defeated | 123 |
| Damage | 1 to 7 |
| Attack chance | 100 |
| Block chance | 60 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: Blindness (magnitude 1, 3 rounds, 10% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Serpent meat](../items/serpent_meat.md) | 5% | 1 |
| [Gold coins](../items/gold.md) | 30% | 1 to 5 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [laerothisland0](../maps/laerothisland0.md) | Lake Laeroth | 10 | – |
| [laerothisland1](../maps/laerothisland1.md) | Lake Laeroth | 8 | – |
| [laerothisland2](../maps/laerothisland2.md) | Lake Laeroth | 10 | – |
| [laerothisland3](../maps/laerothisland3.md) | Lake Laeroth | 5 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `spit_serpent_2` |
    | Spawn group | `serpent_1` |
    | Loot table | `serpent_2` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_snakes:5` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "spit_serpent_2",
     "name": "Young spitting serpent",
     "iconID": "monsters_snakes:5",
     "maxHP": 50,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 1,
      "max": 7
     },
     "spawnGroup": "serpent_1",
     "droplistID": "serpent_2",
     "attackCost": 5,
     "attackChance": 100,
     "blockChance": 60,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "blindness",
        "magnitude": 1,
        "duration": 3,
        "chance": "10"
       }
      ]
     }
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spit_serpent_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spit_serpent_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spit_serpent_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=spit_serpent_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
