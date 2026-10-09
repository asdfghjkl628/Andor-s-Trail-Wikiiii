---
description: "Hardshell beetle is an enemy in Andor's Trail (insect) with 25 HP, worth 87 XP, found in Greenscale tribe, Foaming Flask Tavern, Fallhaven. Drops: Gold coins, Insect shell."
---

# ![](../assets/icons/monsters/monsters_insects_4.png){ .sprite } Hardshell beetle

**Found in:** Brightport: [Waterway forest 2](../maps/waterway_forest2.md), Fallhaven: [Roadbeforecrossroads 7](../maps/roadbeforecrossroads7.md), Fallhaven: [Wild 13](../maps/wild13.md), Foaming Flask Tavern: [Road 1](../maps/road1.md) (+16 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_insects_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Greenscale tribe, Foaming Flask Tavern, Fallhaven |
| **Class** | Insect |
| **HP** | 25 |
| **XP when defeated** | 87 |
| **Entry ID** | `hardshell_beetle` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 25 |
| XP when defeated | 87 |
| Damage | 0 to 5 |
| Attack chance | 50 |
| Block chance | 40 |
| Damage resistance | 9 |
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
| [Gold coins](../items/gold.md) | 70% | 0 to 12 |
| [Insect shell](../items/shell.md) | 30% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brightportwild 16](../maps/brightportwild16.md) | Greenscale tribe | 2 | – |
| [Brightportwild 17](../maps/brightportwild17.md) | Greenscale tribe | 2 | – |
| [Cabin norcity road 1](../maps/cabin_norcity_road1.md) | – | 1 | – |
| [Cabin norcity road 2](../maps/cabin_norcity_road2.md) | – | 2 | – |
| [Cabin norcity road 4](../maps/cabin_norcity_road4.md) | – | 3 | – |
| [Galmore 10a](../maps/galmore_10a.md) | – | 2 | – |
| [Lake shore road 9](../maps/lake_shore_road_9.md) | – | 3 | – |
| [Lodarhouse 0](../maps/lodarhouse0.md) | – | 6 | – |
| [Road 1](../maps/road1.md) | Foaming Flask Tavern | 3 | – |
| [Road 3](../maps/road3.md) | Foaming Flask Tavern | 1 | – |
| [Road 4](../maps/road4.md) | Foaming Flask Tavern | 1 | – |
| [Road 5](../maps/road5.md) | – | 1 | – |
| [Roadbeforecrossroads 7](../maps/roadbeforecrossroads7.md) | Fallhaven | 5 | – |
| [Roadbeforecrossroads 8](../maps/roadbeforecrossroads8.md) | Foaming Flask Tavern | 3 | – |
| [Waterway forest 2](../maps/waterway_forest2.md) | Brightport | 2 | – |
| [Way to sullengard east 4 bridge](../maps/way_to_sullengard_east4_bridge.md) | – | 1 | – |
| [Waytobrightport 8](../maps/waytobrightport8.md) | – | 2 | – |
| [Wild 13](../maps/wild13.md) | Fallhaven | 1 | – |
| [Wild 14 cave](../maps/wild14_cave.md) | Foaming Flask Tavern | 5 | – |
| [Wild 15](../maps/wild15.md) | Foaming Flask Tavern | 2 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `hardshell_beetle` |
    | Spawn group | `beetle2` |
    | Loot table | `beetle2` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_insects:4` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "hardshell_beetle",
     "name": "Hardshell beetle",
     "iconID": "monsters_insects:4",
     "maxHP": 25,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 0,
      "max": 5
     },
     "spawnGroup": "beetle2",
     "droplistID": "beetle2",
     "attackCost": 5,
     "attackChance": 50,
     "blockChance": 40,
     "damageResistance": 9
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hardshell_beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hardshell_beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hardshell_beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hardshell_beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
