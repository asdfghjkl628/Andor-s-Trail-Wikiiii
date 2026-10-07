---
description: "Lizardman corsair is an enemy in Andor's Trail (reptile) with 230 HP, worth 747 XP, found in Brightport, Buried citadel. Drops: Lizardman bone, Pyrite scimitar, Gold coins, Sharpened gem."
---

# ![](../assets/icons/monsters/monsters_johny_5.png){ .sprite } Lizardman corsair

**Found in:** Brightport: [brightport8](../maps/brightport8.md), Brightport: [brightportwild20](../maps/brightportwild20.md), Brightport: [brightportwild7](../maps/brightportwild7.md), Brightport: [waytobrightport16](../maps/waytobrightport16.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_johny_5.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Brightport, Buried citadel |
| **Class** | Reptile |
| **HP** | 230 |
| **XP when defeated** | 747 |
| **Entry ID** | `brightport_redlizard` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Reptile |
| HP | 230 |
| XP when defeated | 747 |
| Damage | 20 to 25 |
| Attack chance | 213 |
| Block chance | 170 |
| Damage resistance | 8 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 15 |
| Critical multiplier | 2.0 |
| Critical hit chance | 12% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Lizardman bone](../items/brightport_bone.md) | 35% | 1 to 2 |
| [Pyrite scimitar](../items/brightport_sword.md) | 1% | 1 |
| [Gold coins](../items/gold.md) | 100% | 4 to 42 |
| [Sharpened gem](../items/gem4.md) | 5% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brightport8](../maps/brightport8.md) | Brightport | 1 | – |
| [brightportwild10](../maps/brightportwild10.md) | – | 1 | – |
| [brightportwild12](../maps/brightportwild12.md) | Buried citadel | 1 | – |
| [brightportwild20](../maps/brightportwild20.md) | Brightport | 2 | – |
| [brightportwild7](../maps/brightportwild7.md) | Brightport | 2 | – |
| [waytobrightport16](../maps/waytobrightport16.md) | Brightport | 3 | – |
| [waytobrightport17](../maps/waytobrightport17.md) | Brightport | 2 | – |
| [waytobrightport18](../maps/waytobrightport18.md) | Brightport | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightport_redlizard` |
    | Spawn group | `brightport_redlizard` |
    | Loot table | `brightport_redlizard` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_johny:5` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_redlizard",
     "name": "Lizardman corsair",
     "iconID": "monsters_johny:5",
     "maxHP": 230,
     "moveCost": 5,
     "monsterClass": "reptile",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 20,
      "max": 25
     },
     "droplistID": "brightport_redlizard",
     "attackCost": 5,
     "attackChance": 213,
     "criticalSkill": 15,
     "criticalMultiplier": 2.0,
     "blockChance": 170,
     "damageResistance": 8
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_redlizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_redlizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_redlizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_redlizard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
