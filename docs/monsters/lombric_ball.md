---
description: "Lombric ball is an enemy in Andor's Trail (animal) with 30 HP, worth 42 XP, found in Bogsten 3, Bogsten 4, Mushroom m 2 3. Drops: Gold coins, Small rock."
---

# ![](../assets/icons/monsters/monsters_rltiles1_138.png){ .sprite } Lombric ball

**Found in:** [Bogsten 3](../maps/bogsten3.md), [Bogsten 4](../maps/bogsten4.md), [Mushroom m 2 3](../maps/mushroom_m2_3.md), [Mushroom m 2 6](../maps/mushroom_m2_6.md) (+3 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_138.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Bogsten 3, Bogsten 4, Mushroom m 2 3 |
| **Class** | Animal |
| **HP** | 30 |
| **XP when defeated** | 42 |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 30 |
| XP when defeated | 42 |
| Damage | 1 to 15 |
| AC | 50 |
| BC | 60 |
| DR | 0 |
| Attacks per turn | 1 (10 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 25% | 1 to 5 |
| [Small rock](../items/rock.md) | 25% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Bogsten 3](../maps/bogsten3.md) | – | 7 | – |
| [Bogsten 4](../maps/bogsten4.md) | – | 7 | – |
| [Mushroom m 2 3](../maps/mushroom_m2_3.md) | – | 9 | – |
| [Mushroom m 2 6](../maps/mushroom_m2_6.md) | – | 4 | – |
| [Mushroom m 2 7](../maps/mushroom_m2_7.md) | – | 1 | – |
| [Mushroom m 2 8](../maps/mushroom_m2_8.md) | – | 2 | – |
| [Mushroom m 3 2](../maps/mushroom_m3_2.md) | – | 4 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added |

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
    | Entry ID | `lombric_ball` |
    | Type (wiki) | Enemy |
    | Spawn group | `lombric_ball` |
    | Loot table | `lombric` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:138` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "lombric_ball",
     "name": "Lombric ball",
     "iconID": "monsters_rltiles1:138",
     "maxHP": 30,
     "maxAP": 10,
     "moveCost": 10,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 1,
      "max": 15
     },
     "spawnGroup": "lombric_ball",
     "droplistID": "lombric",
     "attackCost": 10,
     "attackChance": 50,
     "blockChance": 60
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lombric_ball.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lombric_ball.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lombric_ball.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lombric_ball.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
