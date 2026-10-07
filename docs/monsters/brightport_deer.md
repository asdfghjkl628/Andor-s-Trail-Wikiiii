---
description: "Virulent forest deer is an enemy in Andor's Trail (animal) with 240 HP, worth 587 XP, found in Brightport. Drops: Gold coins, Deer antlers, Raw venison."
---

# ![](../assets/icons/monsters/monsters_johny_12.png){ .sprite } Virulent forest deer

**Found in:** Brightport: [brightportwild18](../maps/brightportwild18.md), Brightport: [brightportwild7](../maps/brightportwild7.md), Brightport: [waytobrightport16](../maps/waytobrightport16.md), Brightport: [waytobrightport18](../maps/waytobrightport18.md) (+8 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_johny_12.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Brightport |
| **Class** | Animal |
| **HP** | 240 |
| **XP when defeated** | 587 |
| **Entry ID** | `brightport_deer` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 240 |
| XP when defeated | 587 |
| Damage | 8 to 19 |
| Attack chance | 182 |
| Block chance | 154 |
| Damage resistance | 8 |
| Max AP | 14 |
| Attack cost | 8 AP |
| Attacks per turn | 1 |
| Move cost | 7 AP |
| Critical skill | 15 |
| Critical multiplier | 1.0 |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: [Brainworm infection](../conditions/brightport_worm.md) (magnitude 1, 3 rounds, 40% chance)

**On death:** On self: [Brainworm infection](../conditions/brightport_worm.md) (magnitude 2, 4 rounds, 70% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 4 to 16 |
| [Deer antlers](../items/brightport_deer.md) | 5% | 0 to 1 |
| [Raw venison](../items/brightport_rawmeat.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brightportwild1](../maps/brightportwild1.md) | – | 2 | – |
| [brightportwild18](../maps/brightportwild18.md) | Brightport | 5 | – |
| [brightportwild19](../maps/brightportwild19.md) | – | 1 | – |
| [brightportwild2](../maps/brightportwild2.md) | – | 2 | – |
| [brightportwild7](../maps/brightportwild7.md) | Brightport | 5 | – |
| [waytobrightport12](../maps/waytobrightport12.md) | – | 5 | – |
| [waytobrightport14](../maps/waytobrightport14.md) | – | 3 | – |
| [waytobrightport15](../maps/waytobrightport15.md) | – | 4 | – |
| [waytobrightport16](../maps/waytobrightport16.md) | Brightport | 6 | – |
| [waytobrightport18](../maps/waytobrightport18.md) | Brightport | 3 | – |
| [waytobrightport19](../maps/waytobrightport19.md) | Brightport | 9 | – |
| [waytobrightport5](../maps/waytobrightport5.md) | – | 8 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightport_deer` |
    | Spawn group | `brightport_deer` |
    | Loot table | `brightport_sickdeer` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_johny:12` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_deer",
     "name": "Virulent forest deer",
     "iconID": "monsters_johny:12",
     "maxHP": 240,
     "maxAP": 14,
     "moveCost": 7,
     "monsterClass": "animal",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 8,
      "max": 19
     },
     "droplistID": "brightport_sickdeer",
     "attackCost": 8,
     "attackChance": 182,
     "criticalSkill": 15,
     "criticalMultiplier": 1.0,
     "blockChance": 154,
     "damageResistance": 8,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "brightport_worm",
        "magnitude": 1,
        "duration": 3,
        "chance": "40"
       }
      ]
     },
     "deathEffect": {
      "conditionsSource": [
       {
        "condition": "brightport_worm",
        "magnitude": 2,
        "duration": 4,
        "chance": "70"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_deer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_deer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_deer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_deer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
