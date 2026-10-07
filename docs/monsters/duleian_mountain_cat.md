---
description: "Duleian mountain cat is an enemy in Andor's Trail (animal) with 97 HP, worth 390 XP, found in Burial cave. Drops: Meat, Bone, Gold coins, Claws."
---

# ![](../assets/icons/monsters/monsters_tometik4_70.png){ .sprite } Duleian mountain cat

**Found in:** Burial cave: [brightportwild3](../maps/brightportwild3.md), [brightportwild1](../maps/brightportwild1.md), [brightportwild2](../maps/brightportwild2.md), [cabin_norcity_road3](../maps/cabin_norcity_road3.md) (+1 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik4_70.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Burial cave |
| **Class** | Animal |
| **HP** | 97 |
| **XP when defeated** | 390 |
| **Entry ID** | `duleian_mountain_cat` |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 97 |
| XP when defeated | 390 |
| Damage | 7 to 19 |
| Attack chance | 225 |
| Block chance | 101 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 4 AP |
| Critical skill | 15 |
| Critical multiplier | 2.5 |
| Critical hit chance | 12% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

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
| [brightportwild1](../maps/brightportwild1.md) | – | 7 | – |
| [brightportwild2](../maps/brightportwild2.md) | – | 3 | – |
| [brightportwild3](../maps/brightportwild3.md) | Burial cave | 2 | – |
| [cabin_norcity_road3](../maps/cabin_norcity_road3.md) | – | 4 | – |
| [cabin_norcity_road4](../maps/cabin_norcity_road4.md) | – | 6 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |
| [v0.8.8](../versions/0.8.8.md) | attackDamage: {"max": 24, "min": 7} → {"max": 19, "min": 7}; criticalMultiplier: 3.0 → 2.5 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `duleian_mountain_cat` |
    | Spawn group | `duleian_mountain_cat` |
    | Loot table | `big_cat_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik4:70` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "duleian_mountain_cat",
     "name": "Duleian mountain cat",
     "iconID": "monsters_tometik4:70",
     "maxHP": 97,
     "moveCost": 4,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 7,
      "max": 19
     },
     "spawnGroup": "duleian_mountain_cat",
     "droplistID": "big_cat_dl",
     "attackCost": 3,
     "attackChance": 225,
     "criticalSkill": 15,
     "criticalMultiplier": 2.5,
     "blockChance": 101
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=duleian_mountain_cat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=duleian_mountain_cat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=duleian_mountain_cat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=duleian_mountain_cat.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
