---
description: "Plaguestrider is an enemy in Andor's Trail (insect) with 62 HP, worth 215 XP, found in mountainlake0, waytolake0, waytolake1. Drops: Gold coins, Poison gland, Dead spider."
---

# ![](../assets/icons/monsters/monsters_rltiles2_151.png){ .sprite } Plaguestrider

**Found in:** [mountainlake0](../maps/mountainlake0.md), [waytolake0](../maps/waytolake0.md), [waytolake1](../maps/waytolake1.md), [waytolake10](../maps/waytolake10.md) (+5 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_151.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | mountainlake0, waytolake0, waytolake1 |
| **Class** | Insect |
| **HP** | 62 |
| **XP when defeated** | 215 |
| **Entry ID** | `plaguesp_5` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 62 |
| XP when defeated | 215 |
| Damage | 2 to 6 |
| Attack chance | 80 |
| Block chance | 150 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 60 |
| Critical multiplier | 3.0 |
| Critical hit chance | 29% |

**On hit:** On target: Insect contagion (magnitude 4, 5 rounds, 70% chance); Blistering skin (magnitude 3, 5 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 3 |
| [Poison gland](../items/gland.md) | 1% | 1 |
| [Dead spider](../items/spider.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mountainlake0](../maps/mountainlake0.md) | – | 2 | – |
| [waytolake0](../maps/waytolake0.md) | – | 3 | – |
| [waytolake1](../maps/waytolake1.md) | – | 10 | – |
| [waytolake10](../maps/waytolake10.md) | – | 2 | – |
| [waytolake12](../maps/waytolake12.md) | – | 3 | – |
| [waytolake2](../maps/waytolake2.md) | – | 10 | – |
| [waytolake3](../maps/waytolake3.md) | – | 4 | – |
| [waytolake6](../maps/waytolake6.md) | – | 6 | – |
| [waytolake9](../maps/waytolake9.md) | – | 5 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 70, "c… → {"conditionsTarget": [{"chance": "70", … |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `plaguesp_5` |
    | Spawn group | `plaguespider_2` |
    | Loot table | `plaguespider` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:151` |
    | Defined in | `res/raw/monsterlist_v0611_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "plaguesp_5",
     "name": "Plaguestrider",
     "iconID": "monsters_rltiles2:151",
     "maxHP": 62,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 2,
      "max": 6
     },
     "spawnGroup": "plaguespider_2",
     "droplistID": "plaguespider",
     "attackCost": 3,
     "attackChance": 80,
     "criticalSkill": 60,
     "criticalMultiplier": 3.0,
     "blockChance": 150,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "contagion",
        "magnitude": 4,
        "duration": 5,
        "chance": "70"
       },
       {
        "condition": "blister",
        "magnitude": 3,
        "duration": 5,
        "chance": "20"
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plaguesp_5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plaguesp_5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plaguesp_5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plaguesp_5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
