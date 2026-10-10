---
description: "Hillside vine is an enemy in Andor's Trail (construct) with 108 HP, worth 286 XP, found in Stoutford."
---

# ![](../assets/icons/monsters/monsters_guynmart_10.png){ .sprite } Hillside vine

**Found in:** Stoutford: [Stoutford filler 1](../maps/stoutford_filler_1.md), Stoutford: [Stoutford filler 2](../maps/stoutford_filler_2.md), Stoutford: [Stoutford filler 3](../maps/stoutford_filler_3.md), [Stoutford filler 4](../maps/stoutford_filler_4.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_guynmart_10.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Stoutford |
| **Class** | Construct |
| **HP** | 108 |
| **XP when defeated** | 286 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat

| | |
|---|---|
| Class | Construct |
| HP | 108 |
| XP when defeated | 286 |
| Damage | 4 |
| AC | 350 |
| BC | 50 |
| DR | 10 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Entanglement](../conditions/entanglement.md) (magnitude 1, 3 rounds, 80% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Stoutford filler 1](../maps/stoutford_filler_1.md) | Stoutford | 3 | – |
| [Stoutford filler 2](../maps/stoutford_filler_2.md) | Stoutford | 3 | – |
| [Stoutford filler 3](../maps/stoutford_filler_3.md) | Stoutford | 2 | – |
| [Stoutford filler 4](../maps/stoutford_filler_4.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

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
    | Entry ID | `hill_vine_bottom` |
    | Type (wiki) | Enemy |
    | Spawn group | `` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_guynmart:10` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "hill_vine_bottom",
     "name": "Hillside vine",
     "iconID": "monsters_guynmart:10",
     "maxHP": 108,
     "monsterClass": "construct",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 4,
      "max": 4
     },
     "spawnGroup": "",
     "attackCost": 5,
     "attackChance": 350,
     "blockChance": 50,
     "damageResistance": 10,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "entanglement",
        "magnitude": 1,
        "duration": 3,
        "chance": "80"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hill_vine_bottom.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hill_vine_bottom.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hill_vine_bottom.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hill_vine_bottom.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
