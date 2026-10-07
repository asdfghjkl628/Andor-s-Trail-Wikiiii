---
description: "Muskrat is an enemy in Andor's Trail (animal) with 100 HP, worth 224 XP, found in Brightport, Buried citadel."
---

# ![](../assets/icons/monsters/monsters_tometik5_26.png){ .sprite } Muskrat

**Found in:** Brightport: [brightport8](../maps/brightport8.md), Brightport: [brightportwild18](../maps/brightportwild18.md), Brightport: [brightportwild7](../maps/brightportwild7.md), Brightport: [waytobrightport16](../maps/waytobrightport16.md) (+17 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik5_26.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Brightport, Buried citadel |
| **Class** | Animal |
| **HP** | 100 |
| **XP when defeated** | 224 |
| **Entry ID** | `brightport_squirrel` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 100 |
| XP when defeated | 224 |
| Damage | 6 to 15 |
| Attack chance | 120 |
| Block chance | 80 |
| Damage resistance | 2 |
| Max AP | 12 |
| Attack cost | 4 AP |
| Attacks per turn | 3 |
| Move cost | 6 AP |
| Critical skill | 15 |
| Critical multiplier | 0.5 |
| Critical hit chance | 12% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brightport8](../maps/brightport8.md) | Brightport | 2 | – |
| [brightportwild12](../maps/brightportwild12.md) | Buried citadel | 2 | – |
| [brightportwild18](../maps/brightportwild18.md) | Brightport | 3 | – |
| [brightportwild19](../maps/brightportwild19.md) | – | 3 | – |
| [brightportwild2](../maps/brightportwild2.md) | – | 1 | – |
| [brightportwild7](../maps/brightportwild7.md) | Brightport | 3 | – |
| [waytobrightport10](../maps/waytobrightport10.md) | – | 3 | – |
| [waytobrightport11](../maps/waytobrightport11.md) | – | 3 | – |
| [waytobrightport12](../maps/waytobrightport12.md) | – | 5 | – |
| [waytobrightport13](../maps/waytobrightport13.md) | – | 8 | – |
| [waytobrightport14](../maps/waytobrightport14.md) | – | 5 | – |
| [waytobrightport15](../maps/waytobrightport15.md) | – | 2 | – |
| [waytobrightport16](../maps/waytobrightport16.md) | Brightport | 5 | – |
| [waytobrightport19](../maps/waytobrightport19.md) | Brightport | 4 | – |
| [waytobrightport20](../maps/waytobrightport20.md) | Brightport | 5 | – |
| [waytobrightport21](../maps/waytobrightport21.md) | Brightport | 1 | – |
| [waytobrightport23](../maps/waytobrightport23.md) | Brightport | 1 | – |
| [waytobrightport3](../maps/waytobrightport3.md) | – | 1 | – |
| [waytobrightport4](../maps/waytobrightport4.md) | – | 2 | – |
| [waytobrightport5](../maps/waytobrightport5.md) | – | 4 | – |
| [waytobrightport7](../maps/waytobrightport7.md) | – | 5 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightport_squirrel` |
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


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


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
