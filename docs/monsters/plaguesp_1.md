---
description: "Puny plaguecrawler is an enemy in Andor's Trail (insect) with 55 HP, worth 192 XP, found in Waytolake 0, Waytolake 1, Waytolake 2. Drops: Gold coins, Poison gland, Dead spider."
---

# ![](../assets/icons/monsters/monsters_rltiles2_61.png){ .sprite } Puny plaguecrawler

**Found in:** [Waytolake 0](../maps/waytolake0.md), [Waytolake 1](../maps/waytolake1.md), [Waytolake 2](../maps/waytolake2.md), [Waytolake 4](../maps/waytolake4.md) (+3 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_61.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Waytolake 0, Waytolake 1, Waytolake 2 |
| **Class** | Insect |
| **HP** | 55 |
| **XP when defeated** | 192 |
| **Entry ID** | `plaguesp_1` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 55 |
| XP when defeated | 192 |
| Damage | 1 to 6 |
| Attack chance | 80 |
| Block chance | 140 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 60 |
| Critical multiplier | 3.0 |
| Critical hit chance | 29% |

**On hit:** On target: [Insect contagion](../conditions/contagion.md) (magnitude 1, 5 rounds, 70% chance); [Blistering skin](../conditions/blister.md) (magnitude 1, 5 rounds, 20% chance)


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
| [Waytolake 0](../maps/waytolake0.md) | – | 6 | – |
| [Waytolake 1](../maps/waytolake1.md) | – | 3 | – |
| [Waytolake 2](../maps/waytolake2.md) | – | 2 | – |
| [Waytolake 4](../maps/waytolake4.md) | – | 1 | – |
| [Waytolake 7](../maps/waytolake7.md) | – | 3 | – |
| [Waytolake 7b](../maps/waytolake7b.md) | – | 8 | – |
| [Waytolake 9](../maps/waytolake9.md) | – | 5 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Blistering skin](../conditions/blister.md) (magnitude 1, 5 rounds, 20% chance) → (magnitude 1, 5 rounds, 20% chance)<br>On hit, condition on target: [Insect contagion](../conditions/contagion.md) (magnitude 1, 5 rounds, 70% chance) → (magnitude 1, 5 rounds, 70% chance)<br>Renamed “Puny Plaguecrawler” → “Puny plaguecrawler” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `plaguesp_1` |
    | Spawn group | `plaguespider_1` |
    | Loot table | `plaguespider` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:61` |
    | Defined in | `res/raw/monsterlist_v0611_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "plaguesp_1",
     "name": "Puny plaguecrawler",
     "iconID": "monsters_rltiles2:61",
     "maxHP": 55,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 1,
      "max": 6
     },
     "spawnGroup": "plaguespider_1",
     "droplistID": "plaguespider",
     "attackCost": 3,
     "attackChance": 80,
     "criticalSkill": 60,
     "criticalMultiplier": 3.0,
     "blockChance": 140,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "contagion",
        "magnitude": 1,
        "duration": 5,
        "chance": "70"
       },
       {
        "condition": "blister",
        "magnitude": 1,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plaguesp_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plaguesp_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plaguesp_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plaguesp_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
