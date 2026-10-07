---
description: "Death cob is an enemy in Andor's Trail (undead) with 179 HP, worth 417 XP, found in Sullengard. Drops: Gold coins, Mushroom spores."
---

# ![](../assets/icons/monsters/monsters_rltiles1_4.png){ .sprite } Death cob

**Found in:** Sullengard: [sullengard5](../maps/sullengard5.md), Sullengard: [sullengard6](../maps/sullengard6.md), Sullengard: [sullengard7](../maps/sullengard7.md), [sullengard10](../maps/sullengard10.md) (+5 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Sullengard |
| **Class** | Undead |
| **HP** | 179 |
| **XP when defeated** | 417 |
| **Entry ID** | `deathcob` |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 179 |
| XP when defeated | 417 |
| Damage | 9 to 23 |
| Attack chance | 90 |
| Block chance | 90 |
| Damage resistance | 11 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Critical hit chance | 9% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 60% | 10 to 20 |
| [Mushroom spores](../items/spore_mush.md) | 15% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [sullengard10](../maps/sullengard10.md) | – | 1 | – |
| [sullengard3](../maps/sullengard3.md) | – | 2 | – |
| [sullengard4](../maps/sullengard4.md) | – | 2 | – |
| [sullengard5](../maps/sullengard5.md) | Sullengard | 3 | – |
| [sullengard6](../maps/sullengard6.md) | Sullengard | 2 | – |
| [sullengard7](../maps/sullengard7.md) | Sullengard | 4 | – |
| [sullengard8](../maps/sullengard8.md) | – | 3 | – |
| [sullengard9](../maps/sullengard9.md) | – | 4 | – |
| [way_to_sullengard_west_6](../maps/way_to_sullengard_west_6.md) | – | 5 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `deathcob` |
    | Spawn group | `deathcob` |
    | Loot table | `waterwayamushroom` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:4` |
    | Defined in | `res/raw/monsterlist_hilltown.json` |

    Raw data:

    ```json
    {
     "id": "deathcob",
     "name": "Death cob",
     "iconID": "monsters_rltiles1:4",
     "maxHP": 179,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 9,
      "max": 23
     },
     "spawnGroup": "deathcob",
     "droplistID": "waterwayamushroom",
     "attackCost": 3,
     "attackChance": 90,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 90,
     "damageResistance": 11
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=deathcob.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=deathcob.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=deathcob.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=deathcob.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
