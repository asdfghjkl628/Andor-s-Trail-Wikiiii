---
description: "Forest beetle is an enemy in Andor's Trail (insect) with 14 HP, worth 38 XP, found in Foaming Flask Tavern, Flagstone Prison, Fallhaven. Drops: Gold coins, Insect shell."
---

# ![](../assets/icons/monsters/monsters_insects_4.png){ .sprite } Forest beetle

**Found in:** Blackwater Mountain: [Wild 6](../maps/wild6.md), Blackwater Mountain: [Wild 7](../maps/wild7.md), Fallhaven: [Gapfiller 1](../maps/gapfiller1.md), Fallhaven: [Gapfiller 2](../maps/gapfiller2.md) (+17 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_insects_4.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Foaming Flask Tavern, Flagstone Prison, Fallhaven |
| **Class** | Insect |
| **HP** | 14 |
| **XP when defeated** | 38 |
| **Entry ID** | `forest_beetle` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Insect |
| HP | 14 |
| XP when defeated | 38 |
| Damage | 2 to 4 |
| Attack chance | 150 |
| Block chance | 60 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 9 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 2 to 4 |
| [Insect shell](../items/shell.md) | 30% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Beekeeper 2](../maps/beekeeper2.md) | Foaming Flask Tavern | 1 | – |
| [Blackwater mountain 0](../maps/blackwater_mountain0.md) | Flagstone Prison | 1 | – |
| [Flagstone 0](../maps/flagstone0.md) | Flagstone Prison | 4 | – |
| [Gapfiller 1](../maps/gapfiller1.md) | Fallhaven | 4 | – |
| [Gapfiller 2](../maps/gapfiller2.md) | Fallhaven | 2 | – |
| [Guynmart wood 1](../maps/guynmart_wood_1.md) | Guynmart Castle | 3 | – |
| [Guynmart wood 10](../maps/guynmart_wood_10.md) | Guynmart Castle | 1 | – |
| [Guynmart wood 11](../maps/guynmart_wood_11.md) | Guynmart Castle | 3 | – |
| [Guynmart wood 12](../maps/guynmart_wood_12.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 13](../maps/guynmart_wood_13.md) | Guynmart Castle | 3 | – |
| [Guynmart wood 3](../maps/guynmart_wood_3.md) | Guynmart Castle | 3 | – |
| [Guynmart wood 6](../maps/guynmart_wood_6.md) | Guynmart Castle | 1 | – |
| [Guynmart wood 9](../maps/guynmart_wood_9.md) | Guynmart Castle | 1 | – |
| [Lakecave 1](../maps/lakecave1.md) | – | 5 | – |
| [Wild 11](../maps/wild11.md) | Fallhaven | 4 | – |
| [Wild 16](../maps/wild16.md) | Flagstone Prison | 7 | – |
| [Wild 17](../maps/wild17.md) | Stoutford | 5 | – |
| [Wild 18](../maps/wild18.md) | Flagstone Prison | 2 | – |
| [Wild 19](../maps/wild19.md) | Stoutford | 2 | – |
| [Wild 6](../maps/wild6.md) | Blackwater Mountain | 4 | – |
| [Wild 7](../maps/wild7.md) | Blackwater Mountain | 3 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Renamed “Forest Beetle” → “Forest beetle” |
| [v0.7.4](../versions/0.7.4.md) | Attack cost: 10 → 9 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `forest_beetle` |
    | Spawn group | `forestbeetle` |
    | Loot table | `insect` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_insects:4` |
    | Defined in | `res/raw/monsterlist_wilderness.json` |

    Raw data:

    ```json
    {
     "id": "forest_beetle",
     "name": "Forest beetle",
     "iconID": "monsters_insects:4",
     "maxHP": 14,
     "monsterClass": "insect",
     "attackDamage": {
      "min": 2,
      "max": 4
     },
     "spawnGroup": "forestbeetle",
     "droplistID": "insect",
     "attackCost": 9,
     "attackChance": 150,
     "blockChance": 60,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=forest_beetle.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
