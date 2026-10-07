---
description: "Walking corpse is an enemy in Andor's Trail (undead) with 90 HP, worth 98 XP, found in Flagstone Prison. Drops: Gold coins, Ruby gem, Regular potion of health, Iron sword."
---

# ![](../assets/icons/monsters/monsters_zombie1_0.png){ .sprite } Walking corpse

**Found in:** Flagstone Prison: [flagstone1](../maps/flagstone1.md), Flagstone Prison: [flagstone2](../maps/flagstone2.md), Flagstone Prison: [flagstone_inner](../maps/flagstone_inner.md), [flagstone3](../maps/flagstone3.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_zombie1_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Flagstone Prison |
| **Class** | Undead |
| **HP** | 90 |
| **XP when defeated** | 98 |
| **Entry ID** | `walking_corpse` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 90 |
| XP when defeated | 98 |
| Damage | 2 to 4 |
| Attack chance | 30 |
| Block chance | 30 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 9 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 40 |
| Critical multiplier | 2.0 |
| Critical hit chance | 23% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 5 to 23 |
| [Ruby gem](../items/gem2.md) | 25% | 1 |
| [Regular potion of health](../items/health.md) | 25% | 1 |
| [Iron sword](../items/ironsword1.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [flagstone1](../maps/flagstone1.md) | Flagstone Prison | 1 | – |
| [flagstone2](../maps/flagstone2.md) | Flagstone Prison | 3 | – |
| [flagstone3](../maps/flagstone3.md) | – | 3 | – |
| [flagstone_inner](../maps/flagstone_inner.md) | Flagstone Prison | 8 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change |
| [v0.7.4](../versions/0.7.4.md) | attackCost: 10 → 9 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `walking_corpse` |
    | Spawn group | `undead1` |
    | Loot table | `undead1` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_zombie1:0` |
    | Defined in | `res/raw/monsterlist_wilderness.json` |

    Raw data:

    ```json
    {
     "id": "walking_corpse",
     "name": "Walking corpse",
     "iconID": "monsters_zombie1:0",
     "maxHP": 90,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 2,
      "max": 4
     },
     "spawnGroup": "undead1",
     "droplistID": "undead1",
     "attackCost": 9,
     "attackChance": 30,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 30,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=walking_corpse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=walking_corpse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=walking_corpse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=walking_corpse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
