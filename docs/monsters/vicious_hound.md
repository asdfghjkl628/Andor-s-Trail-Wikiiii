---
description: "Vicious hound is an enemy in Andor's Trail (animal) with 31 HP, worth 92 XP, found in Foaming Flask Tavern, Stoutford, Prim. Drops: Gold coins, Animal hair, Meat, Leather boots."
---

# ![](../assets/icons/monsters/monsters_rltiles2_110.png){ .sprite } Vicious hound

**Found in:** Blackwater Mountain: [Blackwater mountain 14](../maps/blackwater_mountain14.md), Blackwater Mountain: [Blackwater mountain 70](../maps/blackwater_mountain70.md), Blackwater Mountain: [Bwmfill 1](../maps/bwmfill1.md), Flagstone Prison: [Lake shore road 2](../maps/lake_shore_road_2.md) (+19 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_110.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Foaming Flask Tavern, Stoutford, Prim |
| **Class** | Animal |
| **HP** | 31 |
| **XP when defeated** | 92 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 31 |
| XP when defeated | 92 |
| Damage | 3 to 9 |
| AC | 150 |
| BC | 60 |
| DR | 3 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 |
| [Animal hair](../items/hair.md) | 30% | 1 |
| [Meat](../items/meat.md) | 30% | 1 |
| [Leather boots](../items/boots1.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Beekeeper 2](../maps/beekeeper2.md) | Foaming Flask Tavern | 3 | – |
| [Blackwater mountain 1](../maps/blackwater_mountain1.md) | Stoutford | 3 | – |
| [Blackwater mountain 10](../maps/blackwater_mountain10.md) | Prim | 2 | – |
| [Blackwater mountain 12](../maps/blackwater_mountain12.md) | Prim | 2 | – |
| [Blackwater mountain 14](../maps/blackwater_mountain14.md) | Blackwater Mountain | 2 | – |
| [Blackwater mountain 70](../maps/blackwater_mountain70.md) | Blackwater Mountain | 3 | – |
| [Bwmfill 1](../maps/bwmfill1.md) | Blackwater Mountain | 2 | – |
| [Guynmart](../maps/guynmart.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 1](../maps/guynmart_wood_1.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 10](../maps/guynmart_wood_10.md) | Guynmart Castle | 1 | – |
| [Guynmart wood 11](../maps/guynmart_wood_11.md) | Guynmart Castle | 3 | – |
| [Guynmart wood 12](../maps/guynmart_wood_12.md) | Guynmart Castle | 1 | – |
| [Guynmart wood 13](../maps/guynmart_wood_13.md) | Guynmart Castle | 4 | – |
| [Guynmart wood 15](../maps/guynmart_wood_15.md) | – | 3 | – |
| [Guynmart wood 17](../maps/guynmart_wood_17.md) | – | 3 | – |
| [Guynmart wood 17b](../maps/guynmart_wood_17b.md) | – | 3 | – |
| [Guynmart wood 2](../maps/guynmart_wood_2.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 3](../maps/guynmart_wood_3.md) | Guynmart Castle | 2 | – |
| [Guynmart wood 4](../maps/guynmart_wood_4.md) | Guynmart Castle | 1 | – |
| [Guynmart wood 6](../maps/guynmart_wood_6.md) | Guynmart Castle | 3 | – |
| [Guynmart wood 8](../maps/guynmart_wood_8.md) | Guynmart Castle | 5 | – |
| [Lake shore road 2](../maps/lake_shore_road_2.md) | Flagstone Prison | 2 | – |
| [Wild 17](../maps/wild17.md) | Stoutford | 2 | – |


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
    | Entry ID | `vicious_hound` |
    | Type (wiki) | Enemy |
    | Spawn group | `forestboar4` |
    | Loot table | `canineboss` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:110` |
    | Defined in | `res/raw/monsterlist_v069_monsters.json` |

    Raw data:

    ```json
    {
     "id": "vicious_hound",
     "name": "Vicious hound",
     "iconID": "monsters_rltiles2:110",
     "maxHP": 31,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 3,
      "max": 9
     },
     "spawnGroup": "forestboar4",
     "droplistID": "canineboss",
     "attackCost": 5,
     "attackChance": 150,
     "blockChance": 60,
     "damageResistance": 3
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vicious_hound.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vicious_hound.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vicious_hound.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vicious_hound.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
