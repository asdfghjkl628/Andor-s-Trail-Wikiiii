---
description: "Muskrat is an enemy in Andor's Trail (animal) with 100 HP, worth 224 XP, found in Brightport, Buried citadel."
---

# ![](../assets/icons/monsters/monsters_tometik5_26.png){ .sprite } Muskrat

**Found in:** Brightport: [Brightport 8](../maps/brightport8.md), Brightport: [Brightportwild 18](../maps/brightportwild18.md), Brightport: [Brightportwild 7](../maps/brightportwild7.md), Brightport: [Waytobrightport 16](../maps/waytobrightport16.md) (+17 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik5_26.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Brightport, Buried citadel |
| **Class** | Animal |
| **HP** | 100 |
| **XP when defeated** | 224 |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 100 |
| XP when defeated | 224 |
| Damage | 6 to 15 |
| AC | 120 |
| BC | 80 |
| DR | 2 |
| Attacks per turn | 3 (4 AP each, 12 AP) |
| Crit chance | 12% (×0.5) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brightport 8](../maps/brightport8.md) | Brightport | 2 | – |
| [Brightportwild 12](../maps/brightportwild12.md) | Buried citadel | 2 | – |
| [Brightportwild 18](../maps/brightportwild18.md) | Brightport | 3 | – |
| [Brightportwild 19](../maps/brightportwild19.md) | – | 3 | – |
| [Brightportwild 2](../maps/brightportwild2.md) | – | 1 | – |
| [Brightportwild 7](../maps/brightportwild7.md) | Brightport | 3 | – |
| [Waytobrightport 10](../maps/waytobrightport10.md) | – | 3 | – |
| [Waytobrightport 11](../maps/waytobrightport11.md) | – | 3 | – |
| [Waytobrightport 12](../maps/waytobrightport12.md) | – | 5 | – |
| [Waytobrightport 13](../maps/waytobrightport13.md) | – | 8 | – |
| [Waytobrightport 14](../maps/waytobrightport14.md) | – | 5 | – |
| [Waytobrightport 15](../maps/waytobrightport15.md) | – | 2 | – |
| [Waytobrightport 16](../maps/waytobrightport16.md) | Brightport | 5 | – |
| [Waytobrightport 19](../maps/waytobrightport19.md) | Brightport | 4 | – |
| [Waytobrightport 20](../maps/waytobrightport20.md) | Brightport | 5 | – |
| [Waytobrightport 21](../maps/waytobrightport21.md) | Brightport | 1 | – |
| [Waytobrightport 23](../maps/waytobrightport23.md) | Brightport | 1 | – |
| [Waytobrightport 3](../maps/waytobrightport3.md) | – | 1 | – |
| [Waytobrightport 4](../maps/waytobrightport4.md) | – | 2 | – |
| [Waytobrightport 5](../maps/waytobrightport5.md) | – | 4 | – |
| [Waytobrightport 7](../maps/waytobrightport7.md) | – | 5 | – |


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
    | Entry ID | `brightport_squirrel` |
    | Type (wiki) | Enemy |
    | Spawn group | `brightport_squirrel` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik5:26` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_squirrel",
     "name": "Muskrat",
     "iconID": "monsters_tometik5:26",
     "maxHP": 100,
     "maxAP": 12,
     "moveCost": 6,
     "monsterClass": "animal",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 6,
      "max": 15
     },
     "attackCost": 4,
     "attackChance": 120,
     "criticalSkill": 15,
     "criticalMultiplier": 0.5,
     "blockChance": 80,
     "damageResistance": 2
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_squirrel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_squirrel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_squirrel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_squirrel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
