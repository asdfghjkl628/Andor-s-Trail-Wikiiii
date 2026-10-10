---
description: "Hardershell beetle is an enemy in Andor's Trail (insect) with 54 HP, worth 163 XP, found in Foaming Flask Tavern, Guynmart Castle. Drops: Gold coins, Insect shell."
---

# ![](../assets/icons/monsters/monsters_guynmart_0.png){ .sprite } Hardershell beetle

**Found in:** Foaming Flask Tavern: [Beekeeper 1](../maps/beekeeper1.md), Guynmart Castle: [Gamjee well exit a](../maps/gamjee_well_exit_a.md), [Gamjee well 1 2](../maps/gamjee_well_1_2.md), [Gamjee well 1 4](../maps/gamjee_well_1_4.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_guynmart_0.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Foaming Flask Tavern, Guynmart Castle |
| **Class** | Insect |
| **HP** | 54 |
| **XP when defeated** | 163 |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Combat

| | |
|---|---|
| Class | Insect |
| HP | 54 |
| XP when defeated | 163 |
| Damage | 1 to 7 |
| AC | 60 |
| BC | 70 |
| DR | 14 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 12 |
| [Insect shell](../items/shell.md) | 30% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Beekeeper 1](../maps/beekeeper1.md) | Foaming Flask Tavern | 7 | – |
| [Gamjee well 1 2](../maps/gamjee_well_1_2.md) | – | 2 | – |
| [Gamjee well 1 4](../maps/gamjee_well_1_4.md) | – | 1 | – |
| [Gamjee well 2 1](../maps/gamjee_well_2_1.md) | – | 1 | – |
| [Gamjee well 4 1](../maps/gamjee_well_4_1.md) | – | 1 | – |
| [Gamjee well exit](../maps/gamjee_well_exit.md) | – | 3 | – |
| [Gamjee well exit a](../maps/gamjee_well_exit_a.md) | Guynmart Castle | 1 | – |
| [Gamjee well jail cells](../maps/gamjee_well_jail_cells.md) | – | 3 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

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
    | Entry ID | `hardershell_beetle` |
    | Type (wiki) | Enemy |
    | Spawn group | `` |
    | Loot table | `beetle2` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:0` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "hardershell_beetle",
     "name": "Hardershell beetle",
     "iconID": "monsters_guynmart:0",
     "maxHP": 54,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 1,
      "max": 7
     },
     "spawnGroup": "",
     "droplistID": "beetle2",
     "attackCost": 5,
     "attackChance": 60,
     "blockChance": 70,
     "damageResistance": 14
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hardershell_beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hardershell_beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hardershell_beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hardershell_beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
