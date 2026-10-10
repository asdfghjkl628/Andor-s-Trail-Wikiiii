---
description: "Gilded dust is an enemy in Andor's Trail (construct) with 235 HP, worth 655 XP, found in Undertell 03, Undertell 04. Drops: Emerald shard, Emerald, Gold coins, Undertell diamond."
---

# ![](../assets/icons/monsters/monsters_tometik10_25.png){ .sprite } Gilded dust

**Found in:** [Undertell 03](../maps/undertell_03.md), [Undertell 04](../maps/undertell_04.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik10_25.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Undertell 03, Undertell 04 |
| **Class** | Construct |
| **HP** | 235 |
| **XP when defeated** | 655 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Combat

| | |
|---|---|
| Class | Construct |
| HP | 235 |
| XP when defeated | 655 |
| Damage | 6 |
| AC | 190 |
| BC | 196 |
| DR | 11 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Gilded burden](../conditions/gilded_burden.md) (magnitude 1, 1 round, 18% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Emerald shard](../items/emerald_shard.md) | 1% | 1 to 2 |
| [Emerald](../items/undertell_emerald.md) | 0.1% | 1 |
| [Gold coins](../items/gold.md) | 45% | 15 to 18 |
| [Undertell diamond](../items/undertell_diamond.md) | 1% | 1 |
| [Raw sapphire](../items/raw_sapphire.md) | 1% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Undertell 03](../maps/undertell_03.md) | – | 2 | – |
| [Undertell 04](../maps/undertell_04.md) | – | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

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
    | Entry ID | `gilded_dust` |
    | Type (wiki) | Enemy |
    | Spawn group | `gilded_dust` |
    | Loot table | `gilded_dust_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik10:25` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "gilded_dust",
     "name": "Gilded dust",
     "iconID": "monsters_tometik10:25",
     "maxHP": 235,
     "maxAP": 10,
     "moveCost": 4,
     "monsterClass": "construct",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 6,
      "max": 6
     },
     "droplistID": "gilded_dust_dl",
     "attackCost": 4,
     "attackChance": 190,
     "blockChance": 196,
     "damageResistance": 11,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "gilded_burden",
        "magnitude": 1,
        "duration": 1,
        "chance": "18"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gilded_dust.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gilded_dust.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gilded_dust.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gilded_dust.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
