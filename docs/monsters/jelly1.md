---
description: "Olive ooze is an enemy in Andor's Trail (construct) with 20 HP, worth 137 XP, found in Crossroads Guardhouse. Drops: Gold coins, Mundane ring, Polished ring, Mundane necklace."
---

# ![](../assets/icons/monsters/monsters_tometik2_4.png){ .sprite } Olive ooze

**Found in:** Crossroads Guardhouse: [Roadbeforecrossroads 1](../maps/roadbeforecrossroads1.md), Crossroads Guardhouse: [Roadcave 0](../maps/roadcave0.md), [Roadcave 1](../maps/roadcave1.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik2_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Crossroads Guardhouse |
| **Class** | Construct |
| **HP** | 20 |
| **XP when defeated** | 137 |
| **Immune to crits** | Yes |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Construct |
| HP | 20 |
| XP when defeated | 137 |
| Damage | 5 to 9 |
| AC | 120 |
| BC | 35 |
| DR | 4 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 9% (×2.0) |

**Immune to critical hits.**

**Its hits:** On target: [Corrosive slime](../conditions/slime.md) (magnitude 1, 3 rounds, 40% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 20% | 0 to 2 |
| [Mundane ring](../items/ring1.md) | 5% | 1 |
| [Polished ring](../items/ring2.md) | 5% | 1 |
| [Mundane necklace](../items/junk_necklace0.md) | 5% | 1 |
| [Polished necklace](../items/junk_necklace1.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Roadbeforecrossroads 1](../maps/roadbeforecrossroads1.md) | Crossroads Guardhouse | 3 | – |
| [Roadcave 0](../maps/roadcave0.md) | Crossroads Guardhouse | 11 | – |
| [Roadcave 1](../maps/roadcave1.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Corrosive slime](../conditions/slime.md) (magnitude 1, 3 rounds, 40% chance) → (magnitude 1, 3 rounds, 40% chance)<br>Renamed “Olive Ooze” → “Olive ooze” |

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
    | Entry ID | `jelly1` |
    | Type (wiki) | Enemy |
    | Spawn group | `jelly1` |
    | Loot table | `jelly` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:4` |
    | Defined in | `res/raw/monsterlist_v070_roadcave.json` |

    Raw data:

    ```json
    {
     "id": "jelly1",
     "name": "Olive ooze",
     "iconID": "monsters_tometik2:4",
     "maxHP": 20,
     "moveCost": 5,
     "monsterClass": "construct",
     "attackDamage": {
      "min": 5,
      "max": 9
     },
     "spawnGroup": "jelly1",
     "droplistID": "jelly",
     "attackCost": 5,
     "attackChance": 120,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 35,
     "damageResistance": 4,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "slime",
        "magnitude": 1,
        "duration": 3,
        "chance": "40"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jelly1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jelly1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jelly1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jelly1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
