---
description: "Revenant is an enemy in Andor's Trail (undead) with 115 HP, worth 279 XP, found in Waterwayacave 2, Waterwayacave 3, Waterwayacave 4. Drops: Gold coins, Curved dagger, Rotten meat, Whip of binding."
---

# ![](../assets/icons/monsters/monsters_rltiles2_37.png){ .sprite } Revenant

**Found in:** [Waterwayacave 2](../maps/waterwayacave2.md), [Waterwayacave 3](../maps/waterwayacave3.md), [Waterwayacave 4](../maps/waterwayacave4.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_37.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Waterwayacave 2, Waterwayacave 3, Waterwayacave 4 |
| **Class** | Undead |
| **HP** | 115 |
| **XP when defeated** | 279 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 115 |
| XP when defeated | 279 |
| Damage | 3 to 8 |
| AC | 130 |
| BC | 120 |
| DR | 1 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Flesh rot](../conditions/flesh_rot.md) (magnitude 2, 3 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 6 to 11 |
| [Curved dagger](../items/daggr_curv.md) | 6% | 1 |
| [Rotten meat](../items/meat2.md) | 5% | 1 to 2 |
| [Whip of binding](../items/whip_bind.md) | 0.1% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waterwayacave 2](../maps/waterwayacave2.md) | – | 4 | – |
| [Waterwayacave 3](../maps/waterwayacave3.md) | – | 9 | – |
| [Waterwayacave 4](../maps/waterwayacave4.md) | – | 15 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |
| [v0.7.11](../versions/0.7.11.md) | Loot table added |

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
    | Entry ID | `revenant` |
    | Type (wiki) | Enemy |
    | Spawn group | `revenant` |
    | Loot table | `revenant_2` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_rltiles2:37` |
    | Defined in | `res/raw/monsterlist_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "revenant",
     "name": "Revenant",
     "iconID": "monsters_rltiles2:37",
     "maxHP": 115,
     "moveCost": 4,
     "monsterClass": "undead",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 3,
      "max": 8
     },
     "spawnGroup": "revenant",
     "droplistID": "revenant_2",
     "attackCost": 3,
     "attackChance": 130,
     "blockChance": 120,
     "damageResistance": 1,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "flesh_rot",
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=revenant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=revenant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=revenant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=revenant.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
