---
description: "Creeping fungus is an enemy in Andor's Trail (construct) with 65 HP, worth 157 XP, found in Loneford. Drops: Gold coins, Mushroom spores."
---

# ![](../assets/icons/monsters/monsters_ld2_30.png){ .sprite } Creeping fungus

**Found in:** Loneford: [waterwayb1](../maps/waterwayb1.md), [waterwaya2](../maps/waterwaya2.md), [waterwaya3](../maps/waterwaya3.md), [waterwaya5](../maps/waterwaya5.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld2_30.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Loneford |
| **Class** | Construct |
| **HP** | 65 |
| **XP when defeated** | 157 |
| **Immune to critical hits** | Yes |
| **Entry ID** | `waterwayamushroom` |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Construct |
| HP | 65 |
| XP when defeated | 157 |
| Damage | 3 to 7 |
| Attack chance | 115 |
| Block chance | 70 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Critical hit chance | 9% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons cannot receive critical hits.

**On hit:** On target: Spore contagion (magnitude 1, 4 rounds, 15% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 60% | 10 to 20 |
| [Mushroom spores](../items/spore_mush.md) | 15% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [waterwaya2](../maps/waterwaya2.md) | – | 9 | – |
| [waterwaya3](../maps/waterwaya3.md) | – | 2 | – |
| [waterwaya5](../maps/waterwaya5.md) | – | 4 | – |
| [waterwaya6](../maps/waterwaya6.md) | – | 4 | – |
| [waterwayb1](../maps/waterwayb1.md) | Loneford | 1 | – |
| [waterwayb2](../maps/waterwayb2.md) | – | 2 | – |
| [waterwayb3](../maps/waterwayb3.md) | – | 3 | – |
| [waterwayb4](../maps/waterwayb4.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `waterwayamushroom` |
    | Spawn group | `waterwayamushroom` |
    | Loot table | `waterwayamushroom` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:30` |
    | Defined in | `res/raw/monsterlist_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "waterwayamushroom",
     "name": "Creeping fungus",
     "iconID": "monsters_ld2:30",
     "maxHP": 65,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 3,
      "max": 7
     },
     "spawnGroup": "waterwayamushroom",
     "droplistID": "waterwayamushroom",
     "attackCost": 4,
     "attackChance": 115,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 70,
     "damageResistance": 0,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "contagion2",
        "magnitude": 1,
        "duration": 4,
        "chance": "15"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waterwayamushroom.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waterwayamushroom.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waterwayamushroom.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waterwayamushroom.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
