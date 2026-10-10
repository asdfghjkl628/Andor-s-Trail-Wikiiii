---
description: "Duleian panther is an enemy in Andor's Trail (animal) with 220 HP, worth 781 XP, found in Buried citadel, Burial cave. Drops: Meat, Bone, Gold coins, Claws."
---

# ![](../assets/icons/monsters/monsters_tometik4_67.png){ .sprite } Duleian panther

**Found in:** Burial cave: [Brightportwild 11](../maps/brightportwild11.md), Burial cave: [Brightportwild 3](../maps/brightportwild3.md), Burial cave: [Brightportwild 4](../maps/brightportwild4.md), Buried citadel: [Brightport cave 4](../maps/brightport_cave4.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik4_67.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Buried citadel, Burial cave |
| **Class** | Animal |
| **HP** | 220 |
| **XP when defeated** | 781 |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 220 |
| XP when defeated | 781 |
| Damage | 14 to 25 |
| AC | 203 |
| BC | 180 |
| DR | 4 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 12% (×2.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 15% | 1 |
| [Bone](../items/bone.md) | 10% | 1 to 2 |
| [Gold coins](../items/gold.md) | 5% | 3 to 5 |
| [Claws](../items/claws.md) | 40% | 2 to 5 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brightport cave 4](../maps/brightport_cave4.md) | Buried citadel | 1 | – |
| [Brightportwild 10](../maps/brightportwild10.md) | – | 2 | – |
| [Brightportwild 11](../maps/brightportwild11.md) | Burial cave | 6 | – |
| [Brightportwild 12](../maps/brightportwild12.md) | Buried citadel | 3 | – |
| [Brightportwild 14](../maps/brightportwild14.md) | – | 3 | – |
| [Brightportwild 21](../maps/brightportwild21.md) | – | 2 | – |
| [Brightportwild 3](../maps/brightportwild3.md) | Burial cave | 2 | – |
| [Brightportwild 4](../maps/brightportwild4.md) | Burial cave | 8 | – |


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
    | Entry ID | `brightport_cat2` |
    | Type (wiki) | Enemy |
    | Spawn group | `brightport_cat2` |
    | Loot table | `big_cat_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik4:67` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_cat2",
     "name": "Duleian panther",
     "iconID": "monsters_tometik4:67",
     "maxHP": 220,
     "moveCost": 3,
     "monsterClass": "animal",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 14,
      "max": 25
     },
     "droplistID": "big_cat_dl",
     "attackCost": 3,
     "attackChance": 203,
     "criticalSkill": 15,
     "criticalMultiplier": 2.0,
     "blockChance": 180,
     "damageResistance": 4
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_cat2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_cat2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_cat2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_cat2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
