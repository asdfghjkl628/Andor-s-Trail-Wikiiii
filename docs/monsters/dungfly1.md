---
description: "Giant dungfly is an enemy in Andor's Trail (insect) with 16 HP, worth 44 XP, found in Loneford, Crossroads Guardhouse. Drops: Gold coins, Insect wing."
---

# ![](../assets/icons/monsters/monsters_rltiles2_168.png){ .sprite } Giant dungfly

**Found in:** Crossroads Guardhouse: [Roadbeforecrossroads 1](../maps/roadbeforecrossroads1.md), Loneford: [Lodar 0](../maps/lodar0.md), Loneford: [Lodar 1](../maps/lodar1.md), Loneford: [Lodar 2](../maps/lodar2.md) (+6 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_168.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Loneford, Crossroads Guardhouse |
| **Class** | Insect |
| **HP** | 16 |
| **XP when defeated** | 44 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Insect |
| HP | 16 |
| XP when defeated | 44 |
| Damage | 4 to 5 |
| AC | 55 |
| BC | 20 |
| DR | 1 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 17% (×2.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 2 to 4 |
| [Insect wing](../items/insectwing.md) | 30% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Lodar 0](../maps/lodar0.md) | Loneford | 23 | – |
| [Lodar 1](../maps/lodar1.md) | Loneford | 5 | – |
| [Lodar 11](../maps/lodar11.md) | – | 6 | – |
| [Lodar 14](../maps/lodar14.md) | – | 5 | – |
| [Lodar 2](../maps/lodar2.md) | Loneford | 24 | – |
| [Lodar 3](../maps/lodar3.md) | – | 5 | – |
| [Lodar 4](../maps/lodar4.md) | – | 24 | – |
| [Lodar 5](../maps/lodar5.md) | Loneford | 10 | – |
| [Lodar 9](../maps/lodar9.md) | – | 10 | – |
| [Roadbeforecrossroads 1](../maps/roadbeforecrossroads1.md) | Crossroads Guardhouse | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `dungfly1` |
    | Type (wiki) | Enemy |
    | Spawn group | `forestfly1` |
    | Loot table | `wasp` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_rltiles2:168` |
    | Defined in | `res/raw/monsterlist_v070_lodarmaze.json` |

    Raw data:

    ```json
    {
     "id": "dungfly1",
     "name": "Giant dungfly",
     "iconID": "monsters_rltiles2:168",
     "maxHP": 16,
     "moveCost": 5,
     "monsterClass": "insect",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 4,
      "max": 5
     },
     "spawnGroup": "forestfly1",
     "droplistID": "wasp",
     "attackCost": 3,
     "attackChance": 55,
     "criticalSkill": 25,
     "criticalMultiplier": 2.0,
     "blockChance": 20,
     "damageResistance": 1
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dungfly1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dungfly1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dungfly1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dungfly1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
