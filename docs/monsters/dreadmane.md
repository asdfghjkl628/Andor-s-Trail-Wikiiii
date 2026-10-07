---
description: "Dreadmane is an enemy in Andor's Trail (animal) with 235 HP, worth 709 XP, found in Mt. Galmore. Drops: Meat, Gold coins."
---

# ![](../assets/icons/monsters/monsters_newb_1_281.png){ .sprite } Dreadmane

**Found in:** Mt. Galmore: [galmore_45](../maps/galmore_45.md), Mt. Galmore: [galmore_55](../maps/galmore_55.md), Mt. Galmore: [galmore_56](../maps/galmore_56.md), Mt. Galmore: [galmore_57](../maps/galmore_57.md) (+10 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_281.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Mt. Galmore |
| **Class** | Animal |
| **HP** | 235 |
| **XP when defeated** | 709 |
| **Entry ID** | `dreadmane` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 235 |
| XP when defeated | 709 |
| Damage | 15 to 21 |
| Attack chance | 187 |
| Block chance | 166 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 3 AP |
| Critical skill | 11 |
| Critical multiplier | 2.0 |
| Critical hit chance | 9% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 20% | 1 to 3 |
| [Gold coins](../items/gold.md) | 10% | 1 to 21 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_45](../maps/galmore_45.md) | Mt. Galmore | 2 | – |
| [galmore_55](../maps/galmore_55.md) | Mt. Galmore | 13 | – |
| [galmore_56](../maps/galmore_56.md) | Mt. Galmore | 2 | – |
| [galmore_57](../maps/galmore_57.md) | Mt. Galmore | 12 | – |
| [galmore_63](../maps/galmore_63.md) | Mt. Galmore | 12 | – |
| [galmore_64](../maps/galmore_64.md) | Mt. Galmore | 10 | – |
| [galmore_65](../maps/galmore_65.md) | Mt. Galmore | 10 | – |
| [galmore_66](../maps/galmore_66.md) | Mt. Galmore | 5 | – |
| [galmore_67](../maps/galmore_67.md) | Mt. Galmore | 8 | – |
| [galmore_73](../maps/galmore_73.md) | Mt. Galmore | 11 | – |
| [galmore_74](../maps/galmore_74.md) | Mt. Galmore | 6 | – |
| [galmore_75](../maps/galmore_75.md) | Mt. Galmore | 1 | – |
| [galmore_76](../maps/galmore_76.md) | Mt. Galmore | 2 | – |
| [galmore_77](../maps/galmore_77.md) | Mt. Galmore | 17 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `dreadmane` |
    | Spawn group | `dreadmane` |
    | Loot table | `canine_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:281` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "dreadmane",
     "name": "Dreadmane",
     "iconID": "monsters_newb_1:281",
     "maxHP": 235,
     "moveCost": 3,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 15,
      "max": 21
     },
     "droplistID": "canine_dl",
     "attackCost": 3,
     "attackChance": 187,
     "criticalSkill": 11,
     "criticalMultiplier": 2.0,
     "blockChance": 166,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dreadmane.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dreadmane.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dreadmane.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dreadmane.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
