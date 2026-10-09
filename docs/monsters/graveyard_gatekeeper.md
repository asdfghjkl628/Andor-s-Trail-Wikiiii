---
description: "Graveyard gatekeeper is an enemy in Andor's Trail (undead) with 169 HP, worth 492 XP, found in Haunted cemetery 1, Haunted cemetery 2, Haunted forest 12. Drops: Skeletal remains, Gold coins, Human skull, Tonic of blood."
---

# ![](../assets/icons/monsters/monsters_tometik1_70.png){ .sprite } Graveyard gatekeeper

**Found in:** [Haunted cemetery 1](../maps/haunted_cemetery1.md), [Haunted cemetery 2](../maps/haunted_cemetery2.md), [Haunted forest 12](../maps/haunted_forest12.md), [Haunted forest 15](../maps/haunted_forest15.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik1_70.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Haunted cemetery 1, Haunted cemetery 2, Haunted forest 12 |
| **Class** | Undead |
| **HP** | 169 |
| **XP when defeated** | 492 |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 169 |
| XP when defeated | 492 |
| Damage | 15 to 21 |
| AC | 183 |
| BC | 107 |
| DR | 15 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | 5% (×2.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Skeletal remains](../items/skeletal_remains.md) | 25% | 1 to 2 |
| [Gold coins](../items/gold.md) | 30% | 6 to 12 |
| [Human skull](../items/human_skull.md) | 5% | 1 |
| [Tonic of blood](../items/tonic_of_blood.md) | 8% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Haunted cemetery 1](../maps/haunted_cemetery1.md) | – | 6 | – |
| [Haunted cemetery 2](../maps/haunted_cemetery2.md) | – | 5 | – |
| [Haunted forest 12](../maps/haunted_forest12.md) | – | 3 | – |
| [Haunted forest 15](../maps/haunted_forest15.md) | – | 3 | – |
| [Haunted forest 20](../maps/haunted_forest20.md) | – | 1 | – |
| [Haunted forest way to house 1](../maps/haunted_forest_way_to_house1.md) | – | 2 | – |
| [Haunted forest way to house 2](../maps/haunted_forest_way_to_house2.md) | – | 2 | – |
| [Haunted forest way to house 4](../maps/haunted_forest_way_to_house4.md) | – | 1 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.3](../versions/0.8.3.md) | Added |

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
    | Entry ID | `graveyard_gatekeeper` |
    | Type (wiki) | Enemy |
    | Spawn group | `graveyard_gatekeeper` |
    | Loot table | `graveyard_keeper_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik1:70` |
    | Defined in | `res/raw/monsterlist_haunted_forest.json` |

    Raw data:

    ```json
    {
     "id": "graveyard_gatekeeper",
     "name": "Graveyard gatekeeper",
     "iconID": "monsters_tometik1:70",
     "maxHP": 169,
     "moveCost": 6,
     "monsterClass": "undead",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 15,
      "max": 21
     },
     "droplistID": "graveyard_keeper_dl",
     "attackCost": 4,
     "attackChance": 183,
     "criticalSkill": 5,
     "criticalMultiplier": 2.0,
     "blockChance": 107,
     "damageResistance": 15
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_gatekeeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_gatekeeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_gatekeeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_gatekeeper.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
