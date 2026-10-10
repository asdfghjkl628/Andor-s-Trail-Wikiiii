---
description: "Flamejaw tunnelbeast is an enemy in Andor's Trail (reptile) with 237 HP, worth 530 XP, found in Flagstone Prison. Drops: Healthier worm meat, Gold coins."
---

# ![](../assets/icons/monsters/monsters_newb_1_561.png){ .sprite } Flamejaw tunnelbeast

**Found in:** Flagstone Prison: [Lake shore road 5](../maps/lake_shore_road_5.md), Flagstone Prison: [Rat mountain 1](../maps/rat_mountain_1.md), Flagstone Prison: [Rat mountain 2](../maps/rat_mountain_2.md), Flagstone Prison: [Rat mountain 3](../maps/rat_mountain_3.md) (+1 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_561.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Flagstone Prison |
| **Class** | Reptile |
| **HP** | 237 |
| **XP when defeated** | 530 |
| **Introduced** | [v0.8.8](../versions/0.8.8.md) |

</div>

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 237 |
| XP when defeated | 530 |
| Damage | 7 to 10 |
| AC | 150 |
| BC | 131 |
| DR | 5 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 15% (×2.15) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Healthier worm meat](../items/better_worm_meat.md) | 9% | 1 to 2 |
| [Gold coins](../items/gold.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Lake shore road 5](../maps/lake_shore_road_5.md) | Flagstone Prison | 1 | – |
| [Rat mountain 1](../maps/rat_mountain_1.md) | Flagstone Prison | 4 | – |
| [Rat mountain 2](../maps/rat_mountain_2.md) | Flagstone Prison | 3 | – |
| [Rat mountain 3](../maps/rat_mountain_3.md) | Flagstone Prison | 2 | – |
| [Rat mountain 6](../maps/rat_mountain_6.md) | – | 5 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added |

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
    | Entry ID | `flamejaw_tunnelbeast` |
    | Type (wiki) | Enemy |
    | Spawn group | `flamejaw_tunnelbeast` |
    | Loot table | `flamejaw_tunnelbeast_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:561` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "flamejaw_tunnelbeast",
     "name": "Flamejaw tunnelbeast",
     "iconID": "monsters_newb_1:561",
     "maxHP": 237,
     "moveCost": 4,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 7,
      "max": 10
     },
     "droplistID": "flamejaw_tunnelbeast_dl",
     "attackCost": 3,
     "attackChance": 150,
     "criticalSkill": 20,
     "criticalMultiplier": 2.15,
     "blockChance": 131,
     "damageResistance": 5
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=flamejaw_tunnelbeast.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=flamejaw_tunnelbeast.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=flamejaw_tunnelbeast.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=flamejaw_tunnelbeast.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
