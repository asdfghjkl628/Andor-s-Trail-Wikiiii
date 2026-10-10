---
description: "Forest deer is an enemy in Andor's Trail (animal) with 212 HP, worth 449 XP, found in Brightport. Drops: Deer antlers, Raw venison, Gold coins."
---

# ![](../assets/icons/monsters/monsters_johny_11.png){ .sprite } Forest deer

**Found in:** Brightport: [Brightportwild 18](../maps/brightportwild18.md), Brightport: [Waytobrightport 18](../maps/waytobrightport18.md), Brightport: [Waytobrightport 20](../maps/waytobrightport20.md), [Waytobrightport 11](../maps/waytobrightport11.md) (+3 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_johny_11.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Brightport |
| **Class** | Animal |
| **HP** | 212 |
| **XP when defeated** | 449 |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 212 |
| XP when defeated | 449 |
| Damage | 6 to 16 |
| AC | 168 |
| BC | 148 |
| DR | 6 |
| Attacks per turn | 1 (8 AP each, 14 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Deer antlers](../items/brightport_deer.md) | 2% | 1 |
| [Raw venison](../items/brightport_rawmeat.md) | 15% | 1 |
| [Gold coins](../items/gold.md) | 100% | 3 to 18 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brightportwild 18](../maps/brightportwild18.md) | Brightport | 1 | – |
| [Waytobrightport 11](../maps/waytobrightport11.md) | – | 2 | – |
| [Waytobrightport 13](../maps/waytobrightport13.md) | – | 5 | – |
| [Waytobrightport 18](../maps/waytobrightport18.md) | Brightport | 2 | – |
| [Waytobrightport 20](../maps/waytobrightport20.md) | Brightport | 4 | – |
| [Waytobrightport 5](../maps/waytobrightport5.md) | – | 1 | – |
| [Waytobrightport 7](../maps/waytobrightport7.md) | – | 7 | – |


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
    | Entry ID | `brightport_sickdeer` |
    | Type (wiki) | Enemy |
    | Spawn group | `brightport_sickdeer` |
    | Loot table | `brightport_deer` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_johny:11` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_sickdeer",
     "name": "Forest deer",
     "iconID": "monsters_johny:11",
     "maxHP": 212,
     "maxAP": 14,
     "moveCost": 7,
     "monsterClass": "animal",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 6,
      "max": 16
     },
     "droplistID": "brightport_deer",
     "attackCost": 8,
     "attackChance": 168,
     "criticalSkill": 10,
     "criticalMultiplier": 1.0,
     "blockChance": 148,
     "damageResistance": 6
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_sickdeer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_sickdeer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_sickdeer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_sickdeer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
