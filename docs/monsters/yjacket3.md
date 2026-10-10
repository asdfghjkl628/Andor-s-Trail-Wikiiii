---
description: "Swarming yellowjacket is an enemy in Andor's Trail (insect) with 42 HP, worth 128 XP, found in Lodar 11, Lodar 14, Lodar 4. Drops: Gold coins, Insect wing."
---

# ![](../assets/icons/monsters/monsters_rltiles2_112.png){ .sprite } Swarming yellowjacket

**Found in:** [Lodar 11](../maps/lodar11.md), [Lodar 14](../maps/lodar14.md), [Lodar 4](../maps/lodar4.md), [Lodar 7](../maps/lodar7.md) (+1 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_112.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Lodar 11, Lodar 14, Lodar 4 |
| **Class** | Insect |
| **HP** | 42 |
| **XP when defeated** | 128 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Insect |
| HP | 42 |
| XP when defeated | 128 |
| Damage | 3 to 4 |
| AC | 85 |
| BC | 63 |
| DR | 0 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 15% (×3.0) |

**Its hits:** On target: [Minor sting](../conditions/sting_minor.md) (magnitude 2, 3 rounds, 30% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 2 to 4 |
| [Insect wing](../items/insectwing.md) | 30% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Lodar 11](../maps/lodar11.md) | – | 5 | – |
| [Lodar 14](../maps/lodar14.md) | – | 2 | – |
| [Lodar 4](../maps/lodar4.md) | – | 4 | – |
| [Lodar 7](../maps/lodar7.md) | – | 13 | – |
| [Lodar 8](../maps/lodar8.md) | – | 4 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Minor sting](../conditions/sting_minor.md) (magnitude 2, 3 rounds, 30% chance) → (magnitude 2, 3 rounds, 30% chance) |

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
    | Entry ID | `yjacket3` |
    | Type (wiki) | Enemy |
    | Spawn group | `yjacket1` |
    | Loot table | `wasp` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:112` |
    | Defined in | `res/raw/monsterlist_v070_lodarmaze.json` |

    Raw data:

    ```json
    {
     "id": "yjacket3",
     "name": "Swarming yellowjacket",
     "iconID": "monsters_rltiles2:112",
     "maxHP": 42,
     "moveCost": 5,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 3,
      "max": 4
     },
     "spawnGroup": "yjacket1",
     "droplistID": "wasp",
     "attackCost": 3,
     "attackChance": 85,
     "criticalSkill": 20,
     "criticalMultiplier": 3.0,
     "blockChance": 63,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "sting_minor",
        "magnitude": 2,
        "duration": 3,
        "chance": "30"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=yjacket3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=yjacket3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=yjacket3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=yjacket3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
