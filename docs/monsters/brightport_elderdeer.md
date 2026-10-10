---
description: "Elder deer is an enemy in Andor's Trail (animal) with 293 HP, worth 800 XP, found in Brightport, Burial cave, Buried citadel. Drops: Deer antlers, Raw venison, Gold coins."
---

# ![](../assets/icons/monsters/monsters_johny_13.png){ .sprite } Elder deer

**Found in:** Brightport: [Brightportwild 18](../maps/brightportwild18.md), Burial cave: [Brightportwild 3](../maps/brightportwild3.md), Buried citadel: [Brightportwild 6](../maps/brightportwild6.md), [Brightportwild 19](../maps/brightportwild19.md) (+6 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_johny_13.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Brightport, Burial cave, Buried citadel |
| **Class** | Animal |
| **HP** | 293 |
| **XP when defeated** | 800 |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 293 |
| XP when defeated | 800 |
| Damage | 8 to 22 |
| AC | 192 |
| BC | 229 |
| DR | 8 |
| Attacks per turn | 1 (8 AP each, 14 AP) |
| Crit chance | 12% (×1.5) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Deer antlers](../items/brightport_deer.md) | 8% | 1 |
| [Raw venison](../items/brightport_rawmeat.md) | 15% | 1 to 2 |
| [Gold coins](../items/gold.md) | 100% | 12 to 25 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brightportwild 18](../maps/brightportwild18.md) | Brightport | 1 | – |
| [Brightportwild 19](../maps/brightportwild19.md) | – | 5 | – |
| [Brightportwild 21](../maps/brightportwild21.md) | – | 1 | – |
| [Brightportwild 3](../maps/brightportwild3.md) | Burial cave | 4 | – |
| [Brightportwild 5](../maps/brightportwild5.md) | – | 5 | – |
| [Brightportwild 6](../maps/brightportwild6.md) | Buried citadel | 1 | – |
| [Brightportwild 8](../maps/brightportwild8.md) | – | 3 | – |
| [Brightportwild 9](../maps/brightportwild9.md) | – | 3 | – |
| [Waytobrightport 10](../maps/waytobrightport10.md) | – | 3 | – |
| [Waytobrightport 9](../maps/waytobrightport9.md) | – | 3 | – |


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
    | Entry ID | `brightport_elderdeer` |
    | Type (wiki) | Enemy |
    | Spawn group | `brightport_elderdeer` |
    | Loot table | `brightport_elderdeer` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_johny:13` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_elderdeer",
     "name": "Elder deer",
     "iconID": "monsters_johny:13",
     "maxHP": 293,
     "maxAP": 14,
     "moveCost": 7,
     "monsterClass": "animal",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 8,
      "max": 22
     },
     "droplistID": "brightport_elderdeer",
     "attackCost": 8,
     "attackChance": 192,
     "criticalSkill": 15,
     "criticalMultiplier": 1.5,
     "blockChance": 229,
     "damageResistance": 8
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_elderdeer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_elderdeer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_elderdeer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_elderdeer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
