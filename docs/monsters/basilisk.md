---
description: "Basilisk is an enemy in Andor's Trail (reptile) with 40 HP, worth 60 XP, found in Flagstone Prison, Foaming Flask Tavern, Blackwater Mountain. Drops: Gold coins, Glass gem, Claws."
---

# ![](../assets/icons/monsters/monsters_rats_4.png){ .sprite } Basilisk

**Found in:** Blackwater Mountain: [Snakecave 2](../maps/snakecave2.md), Flagstone Prison: [Flagstone 0](../maps/flagstone0.md), Flagstone Prison: [Flagstone 2](../maps/flagstone2.md), Flagstone Prison: [Flagstone filler east 1](../maps/flagstone_filler_east_1.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rats_4.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Flagstone Prison, Foaming Flask Tavern, Blackwater Mountain |
| **Class** | Reptile |
| **HP** | 40 |
| **XP when defeated** | 60 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 40 |
| XP when defeated | 60 |
| Damage | 3 to 9 |
| AC | 40 |
| BC | 50 |
| DR | 2 |
| Attacks per turn | 1 (7 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 4 to 8 |
| [Glass gem](../items/gem1.md) | 25% | 1 |
| [Claws](../items/claws.md) | 30% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Flagstone 0](../maps/flagstone0.md) | Flagstone Prison | 2 | – |
| [Flagstone 2](../maps/flagstone2.md) | Flagstone Prison | 1 | – |
| [Flagstone 3](../maps/flagstone3.md) | – | 2 | – |
| [Flagstone filler east 1](../maps/flagstone_filler_east_1.md) | Flagstone Prison | 1 | – |
| [Road 4](../maps/road4.md) | Foaming Flask Tavern | 1 | – |
| [Road 4 gargoylecave](../maps/road4_gargoylecave.md) | – | 1 | – |
| [Snakecave 2](../maps/snakecave2.md) | Blackwater Mountain | 1 | – |
| [Snakecave 3](../maps/snakecave3.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.8.15](../versions/0.8.15.md) | Chance of appearing mirrored: added (25) |

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
    | Entry ID | `basilisk` |
    | Type (wiki) | Enemy |
    | Spawn group | `cavesnake2_boss` |
    | Loot table | `cavecritter` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rats:4` |
    | Defined in | `res/raw/monsterlist_crossglen_animals.json` |

    Raw data:

    ```json
    {
     "id": "basilisk",
     "name": "Basilisk",
     "iconID": "monsters_rats:4",
     "maxHP": 40,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 3,
      "max": 9
     },
     "spawnGroup": "cavesnake2_boss",
     "droplistID": "cavecritter",
     "attackCost": 7,
     "attackChance": 40,
     "blockChance": 50,
     "damageResistance": 2,
     "horizontalFlipChance": 25
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=basilisk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=basilisk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=basilisk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=basilisk.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
