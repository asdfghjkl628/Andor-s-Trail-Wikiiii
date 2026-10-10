---
description: "Young allaceph is an enemy in Andor's Trail (demon) with 90 HP, worth 231 XP, found in Waytobrimhavencave 1, Waytobrimhavencave 2. Drops: Gold coins, Glass gem, Regular potion of health, Empty vial."
---

# ![](../assets/icons/monsters/monsters_rltiles2_101.png){ .sprite } Young allaceph

**Found in:** [Waytobrimhavencave 1](../maps/waytobrimhavencave1.md), [Waytobrimhavencave 2](../maps/waytobrimhavencave2.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_101.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Waytobrimhavencave 1, Waytobrimhavencave 2 |
| **Class** | Demon |
| **HP** | 90 |
| **XP when defeated** | 231 |
| **Immune to crits** | Yes |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Demon |
| HP | 90 |
| XP when defeated | 231 |
| Damage | 3 to 7 |
| AC | 80 |
| BC | 105 |
| DR | 1 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 23% (×2.0) |

**Immune to critical hits.**

**Its hits:** Heal HP: 4; On target: [Minor weapon feebleness](../conditions/feebleness_minor.md) (magnitude 2, 3 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 30% | 1 to 20 |
| [Glass gem](../items/gem1.md) | 1% | 1 |
| [Regular potion of health](../items/health.md) | 5% | 1 |
| [Empty vial](../items/vial_empty2.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waytobrimhavencave 1](../maps/waytobrimhavencave1.md) | – | 9 | – |
| [Waytobrimhavencave 2](../maps/waytobrimhavencave2.md) | – | 6 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Minor weapon feebleness](../conditions/feebleness_minor.md) (magnitude 2, 3 rounds, 20% chance) → (magnitude 2, 3 rounds, 20% chance)<br>Renamed “Young Allaceph” → “Young allaceph” |

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
    | Entry ID | `allaceph_1` |
    | Type (wiki) | Enemy |
    | Spawn group | `allaceph_1` |
    | Loot table | `allaceph` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:101` |
    | Defined in | `res/raw/monsterlist_v0611_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "allaceph_1",
     "name": "Young allaceph",
     "iconID": "monsters_rltiles2:101",
     "maxHP": 90,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "demon",
     "attackDamage": {
      "min": 3,
      "max": 7
     },
     "spawnGroup": "allaceph_1",
     "droplistID": "allaceph",
     "attackCost": 3,
     "attackChance": 80,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 105,
     "damageResistance": 1,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 4,
       "max": 4
      },
      "conditionsTarget": [
       {
        "condition": "feebleness_minor",
        "magnitude": 2,
        "duration": 3,
        "chance": "20"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=allaceph_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=allaceph_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=allaceph_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=allaceph_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
