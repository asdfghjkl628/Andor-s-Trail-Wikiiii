---
description: "Seraphina's bodyguard is an enemy in Andor's Trail (humanoid) with 52 HP, worth 101 XP, found in Prim, Vilegard, Brimhaven. Drops: Small empty vial, Gold coins, Tiny knife."
---

# ![](../assets/icons/monsters/monsters_ld1_87.png){ .sprite } Seraphina's bodyguard

**Found in:** Brimhaven: [Waterway 6](../maps/waterway6.md), Brimhaven: [Waytobrimhaven 3](../maps/waytobrimhaven3.md), Loneford: [Waytobrimhaven 1](../maps/waytobrimhaven1.md), Prim: [Blackwater mountain 12](../maps/blackwater_mountain12.md) (+3 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_87.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Prim, Vilegard, Brimhaven |
| **Class** | Humanoid |
| **HP** | 52 |
| **XP when defeated** | 101 |
| **Entry ID** | `tt_guys` |
| **Introduced** | [v0.8.13](../versions/0.8.13.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 52 |
| XP when defeated | 101 |
| Damage | 8 to 15 |
| Attack chance | 90 |
| Block chance | 40 |
| Damage resistance | 1 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small empty vial](../items/vial_empty1.md) | 100% | 0 to 1 |
| [Gold coins](../items/gold.md) | 100% | 10 to 100 |
| [Tiny knife](../items/tiny_knife.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 12](../maps/blackwater_mountain12.md) | Prim | 5 | Appears later, during a quest |
| [Sullengard 3](../maps/sullengard3.md) | – | 5 | Appears later, during a quest |
| [Vilegard south](../maps/vilegard_s.md) | Vilegard | 5 | Appears later, during a quest |
| [Waterway 6](../maps/waterway6.md) | Brimhaven | 5 | Appears later, during a quest |
| [Waytobrimhaven 1](../maps/waytobrimhaven1.md) | Loneford | 5 | Appears later, during a quest |
| [Waytobrimhaven 3](../maps/waytobrimhaven3.md) | Brimhaven | 5 | Appears later, during a quest |
| [Wild 21](../maps/wild21.md) | Stoutford | 5 | Appears later, during a quest |


## Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `tt_guys` |
    | Spawn group | `tt_guys` |
    | Loot table | `tt_guys` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_ld1:87` |
    | Defined in | `res/raw/monsterlist_troubling_times.json` |

    Raw data:

    ```json
    {
     "id": "tt_guys",
     "name": "Seraphina's bodyguard",
     "iconID": "monsters_ld1:87",
     "maxHP": 52,
     "maxAP": 10,
     "moveCost": 10,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 8,
      "max": 15
     },
     "spawnGroup": "tt_guys",
     "droplistID": "tt_guys",
     "attackCost": 5,
     "attackChance": 90,
     "blockChance": 40,
     "damageResistance": 1
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_guys.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_guys.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_guys.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_guys.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
