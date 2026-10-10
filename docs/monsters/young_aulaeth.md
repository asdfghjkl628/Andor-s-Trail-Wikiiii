---
description: "Young aulaeth is an enemy in Andor's Trail (giant) with 105 HP, worth 131 XP, found in Blackwater Mountain. Drops: Gold coins, Bone, Small empty vial, Regular potion of health."
---

# ![](../assets/icons/monsters/monsters_rltiles2_176.png){ .sprite } Young aulaeth

**Found in:** Blackwater Mountain: [Blackwater mountain 20](../maps/blackwater_mountain20.md), Blackwater Mountain: [Blackwater mountain 30](../maps/blackwater_mountain30.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_176.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Blackwater Mountain |
| **Class** | Giant |
| **HP** | 105 |
| **XP when defeated** | 131 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat

| | |
|---|---|
| Class | Giant |
| HP | 105 |
| XP when defeated | 131 |
| Damage | 0 to 4 |
| AC | 40 |
| BC | 30 |
| DR | 5 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** Heal HP: 1


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 1 to 5 |
| [Bone](../items/bone.md) | 10% | 1 to 3 |
| [Small empty vial](../items/vial_empty1.md) | 25% | 1 |
| [Regular potion of health](../items/health.md) | 10% | 1 to 2 |
| [Blackwater dagger](../items/bwm_dagger.md) | 1% | 1 |
| [Blackwater iron sword](../items/bwm_ironsword.md) | 1% | 1 |
| [Minor potion of speed](../items/pot_speed_1.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 20](../maps/blackwater_mountain20.md) | Blackwater Mountain | 4 | – |
| [Blackwater mountain 30](../maps/blackwater_mountain30.md) | Blackwater Mountain | 1 | – |


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
    | Entry ID | `young_aulaeth` |
    | Type (wiki) | Enemy |
    | Spawn group | `wyrm_1` |
    | Loot table | `aulaeth` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:176` |
    | Defined in | `res/raw/monsterlist_v069_monsters.json` |

    Raw data:

    ```json
    {
     "id": "young_aulaeth",
     "name": "Young aulaeth",
     "iconID": "monsters_rltiles2:176",
     "maxHP": 105,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 0,
      "max": 4
     },
     "spawnGroup": "wyrm_1",
     "droplistID": "aulaeth",
     "attackCost": 5,
     "attackChance": 40,
     "blockChance": 30,
     "damageResistance": 5,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      }
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=young_aulaeth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=young_aulaeth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=young_aulaeth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=young_aulaeth.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
