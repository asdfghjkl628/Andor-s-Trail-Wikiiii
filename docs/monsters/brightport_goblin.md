---
description: "Charwood goblin hogrider is an enemy in Andor's Trail (animal) with 280 HP, worth 623 XP, found in Charwood. Drops: Gold coins, Iron mace, Broken wooden buckler, Ointment of bleeding wounds."
---

# ![](../assets/icons/monsters/monsters_newb_1_48.png){ .sprite } Charwood goblin hogrider

**Found in:** Charwood: [Waytobrightport 0](../maps/waytobrightport0.md), [Waytobrightport 1](../maps/waytobrightport1.md), [Waytobrightport 2](../maps/waytobrightport2.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_48.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Charwood |
| **Class** | Animal |
| **HP** | 280 |
| **XP when defeated** | 623 |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 280 |
| XP when defeated | 623 |
| Damage | 15 to 27 |
| AC | 200 |
| BC | 110 |
| DR | 4 |
| Attacks per turn | 2 (6 AP each, 12 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 30% | 1 to 20 |
| [Iron mace](../items/mace_iron.md) | 1% | 1 |
| [Broken wooden buckler](../items/broken_buckler.md) | 1% | 1 |
| [Ointment of bleeding wounds](../items/pot_bleeding_ointment.md) | 5% | 1 |
| [Raw perch](../items/rawperch.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waytobrightport 0](../maps/waytobrightport0.md) | Charwood | 6 | – |
| [Waytobrightport 1](../maps/waytobrightport1.md) | – | 1 | – |
| [Waytobrightport 2](../maps/waytobrightport2.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added |

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
    | Entry ID | `brightport_goblin` |
    | Type (wiki) | Enemy |
    | Spawn group | `brightport_goblin` |
    | Loot table | `charwdg` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_newb_1:48` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_goblin",
     "name": "Charwood goblin hogrider",
     "iconID": "monsters_newb_1:48",
     "maxHP": 280,
     "maxAP": 12,
     "moveCost": 3,
     "monsterClass": "animal",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 15,
      "max": 27
     },
     "droplistID": "charwdg",
     "attackCost": 6,
     "attackChance": 200,
     "criticalSkill": 5,
     "criticalMultiplier": 1.0,
     "blockChance": 110,
     "damageResistance": 4
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_goblin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_goblin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_goblin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_goblin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
