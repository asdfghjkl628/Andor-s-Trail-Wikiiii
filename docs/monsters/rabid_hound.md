---
description: "Rabid hound is an enemy in Andor's Trail (animal) with 40 HP, worth 65 XP, found in Stoutford, Guynmart Castle, Crossroads Guardhouse. Drops: Gold coins, Glass gem, Meat."
---

# ![](../assets/icons/monsters/monsters_rltiles2_108.png){ .sprite } Rabid hound

**Found in:** Brimhaven: [Waytobrimhaven 3](../maps/waytobrimhaven3.md), Brimhaven: [Waytobrimhaven 5](../maps/waytobrimhaven5.md), Brimhaven: [Waytobrimhaven 6](../maps/waytobrimhaven6.md), Crossroads Guardhouse: [Roadbeforecrossroads 1](../maps/roadbeforecrossroads1.md) (+11 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles2_108.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Stoutford, Guynmart Castle, Crossroads Guardhouse |
| **Class** | Animal |
| **HP** | 40 |
| **XP when defeated** | 65 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 40 |
| XP when defeated | 65 |
| Damage | 3 to 9 |
| AC | 110 |
| BC | 30 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 3 to 6 |
| [Glass gem](../items/gem1.md) | 5% | 1 |
| [Meat](../items/meat.md) | 30% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 1](../maps/blackwater_mountain1.md) | Stoutford | 2 | – |
| [Guynmart](../maps/guynmart.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 1](../maps/guynmart_wood_1.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 12](../maps/guynmart_wood_12.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 13](../maps/guynmart_wood_13.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 2](../maps/guynmart_wood_2.md) | Guynmart Castle | 1 | – |
| [Guynmart wood 3](../maps/guynmart_wood_3.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 9](../maps/guynmart_wood_9.md) | Guynmart Castle | 2 | – |
| [Roadbeforecrossroads 1](../maps/roadbeforecrossroads1.md) | Crossroads Guardhouse | 1 | – |
| [Waterwayb 1](../maps/waterwayb1.md) | Loneford | 2 | – |
| [Waytobrimhaven 1](../maps/waytobrimhaven1.md) | Loneford | 5 | – |
| [Waytobrimhaven 3](../maps/waytobrimhaven3.md) | Brimhaven | 3 | – |
| [Waytobrimhaven 5](../maps/waytobrimhaven5.md) | Brimhaven | 3 | – |
| [Waytobrimhaven 6](../maps/waytobrimhaven6.md) | Brimhaven | 5 | – |
| [Wild 17](../maps/wild17.md) | Stoutford | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

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
    | Entry ID | `rabid_hound` |
    | Type (wiki) | Enemy |
    | Spawn group | `forestwolf2` |
    | Loot table | `canine` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:108` |
    | Defined in | `res/raw/monsterlist_v069_monsters.json` |

    Raw data:

    ```json
    {
     "id": "rabid_hound",
     "name": "Rabid hound",
     "iconID": "monsters_rltiles2:108",
     "maxHP": 40,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 3,
      "max": 9
     },
     "spawnGroup": "forestwolf2",
     "droplistID": "canine",
     "attackCost": 5,
     "attackChance": 110,
     "blockChance": 30
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rabid_hound.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rabid_hound.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rabid_hound.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rabid_hound.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
