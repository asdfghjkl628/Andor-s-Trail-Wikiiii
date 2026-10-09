---
description: "Korvan the leader of the wolves is an enemy in Andor's Trail (animal) with 50 HP, worth 78 XP, found in Crossroads Guardhouse. Drops: Jakrar's woodcutting axe, Gold coins, Animal hair, Meat."
---

# ![](../assets/icons/monsters/monsters_rltiles2_108.png){ .sprite } Korvan the leader of the wolves

**Found in:** Crossroads Guardhouse: [Roadbeforecrossroads](../maps/roadbeforecrossroads.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_108.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Crossroads Guardhouse |
| **Class** | Animal |
| **HP** | 50 |
| **XP when defeated** | 78 |
| **Entry ID** | `wolf_leader` |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 50 |
| XP when defeated | 78 |
| Damage | 4 to 7 |
| Attack chance | 130 |
| Block chance | 35 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Jakrar's woodcutting axe](../items/jakrar_axe.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 50 |
| [Animal hair](../items/hair.md) | 100% | 1 |
| [Meat](../items/meat.md) | 100% | 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Roadbeforecrossroads](../maps/roadbeforecrossroads.md) | Crossroads Guardhouse | 1 | – |

## Quests that count defeats

- [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-35) with stepping on a trigger on [Roadbeforecrossroads](../maps/roadbeforecrossroads.md) checks that this enemy has been defeated.


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `wolf_leader` |
    | Spawn group | `wolf_leader` |
    | Loot table | `jakrar_axe_drop` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_rltiles2:108` |
    | Defined in | `res/raw/monsterlist_pathway_fallhaven.json` |

    Raw data:

    ```json
    {
     "id": "wolf_leader",
     "name": "Korvan the leader of the wolves",
     "iconID": "monsters_rltiles2:108",
     "maxHP": 50,
     "moveCost": 3,
     "unique": 1,
     "monsterClass": "animal",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 4,
      "max": 7
     },
     "spawnGroup": "wolf_leader",
     "droplistID": "jakrar_axe_drop",
     "attackCost": 5,
     "attackChance": 130,
     "blockChance": 35
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wolf_leader.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wolf_leader.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wolf_leader.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wolf_leader.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
