---
description: "White wyrm is an enemy in Andor's Trail (reptile) with 55 HP, worth 204 XP, found in Blackwater Mountain. Drops: Gold coins, Bone, Small empty vial, Regular potion of health."
---

# ![](../assets/icons/monsters/monsters_rltiles1_119.png){ .sprite } White wyrm

**Found in:** Blackwater Mountain: [Blackwater mountain 30](../maps/blackwater_mountain30.md), Blackwater Mountain: [Blackwater mountain 32](../maps/blackwater_mountain32.md), Blackwater Mountain: [Blackwater mountain 37](../maps/blackwater_mountain37.md), Blackwater Mountain: [Blackwater mountain 55](../maps/blackwater_mountain55.md) (+2 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_119.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Blackwater Mountain |
| **Class** | Reptile |
| **HP** | 55 |
| **XP when defeated** | 204 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 55 |
| XP when defeated | 204 |
| Damage | 4 to 10 |
| AC | 75 |
| BC | 130 |
| DR | 5 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Minor fatigue](../conditions/fatigue_minor.md) (magnitude 1, 5 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 60 |
| [Bone](../items/bone.md) | 10% | 1 to 2 |
| [Small empty vial](../items/vial_empty1.md) | 25% | 1 |
| [Regular potion of health](../items/health.md) | 10% | 1 to 2 |
| [White wyrm claw](../items/bwm_claws.md) | 10% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 30](../maps/blackwater_mountain30.md) | Blackwater Mountain | 1 | – |
| [Blackwater mountain 32](../maps/blackwater_mountain32.md) | Blackwater Mountain | 16 | – |
| [Blackwater mountain 37](../maps/blackwater_mountain37.md) | Blackwater Mountain | 2 | – |
| [Blackwater mountain 55](../maps/blackwater_mountain55.md) | Blackwater Mountain | 5 | – |
| [Bwmfill 5](../maps/bwmfill5.md) | Blackwater Mountain | 1 | – |
| [Bwmfill 6](../maps/bwmfill6.md) | Blackwater Mountain | 1 | – |

## Quests that count defeats

- A conversation with [Jern](../monsters/prim_bar_regular.md) ([Blackwater mountain 22](../maps/blackwater_mountain22.md)) checks that this enemy has been defeated.


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | On hit, condition on target: [Minor fatigue](../conditions/fatigue_minor.md) (magnitude 1, 5 rounds, 50% chance) → (magnitude 1, 5 rounds, 50% chance) |

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
    | Entry ID | `white_wyrm` |
    | Type (wiki) | Enemy |
    | Spawn group | `wyrm_3` |
    | Loot table | `wyrm_3` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:119` |
    | Defined in | `res/raw/monsterlist_v069_monsters.json` |

    Raw data:

    ```json
    {
     "id": "white_wyrm",
     "name": "White wyrm",
     "iconID": "monsters_rltiles1:119",
     "maxHP": 55,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 4,
      "max": 10
     },
     "spawnGroup": "wyrm_3",
     "droplistID": "wyrm_3",
     "attackCost": 3,
     "attackChance": 75,
     "blockChance": 130,
     "damageResistance": 5,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "fatigue_minor",
        "magnitude": 1,
        "duration": 5,
        "chance": "50"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=white_wyrm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=white_wyrm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=white_wyrm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=white_wyrm.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
