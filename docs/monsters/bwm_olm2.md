---
description: "Albino olm is an enemy in Andor's Trail (animal) with 66 HP, worth 231 XP, found in Blackwater mountain 74, Blackwater mountain 74 h, Blackwater mountain 75. Drops: Thin amphibian skin, Gold coins, Wizened amphibian boots, Battered amphibian gloves."
---

# ![](../assets/icons/monsters/monsters_omi2_9.png){ .sprite } Albino olm

**Found in:** [Blackwater mountain 74](../maps/blackwater_mountain74.md), [Blackwater mountain 74 h](../maps/blackwater_mountain74_h.md), [Blackwater mountain 75](../maps/blackwater_mountain75.md), [Elm 5f 1](../maps/elm5f_1.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_omi2_9.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Blackwater mountain 74, Blackwater mountain 74 h, Blackwater mountain 75 |
| **Class** | Animal |
| **HP** | 66 |
| **XP when defeated** | 231 |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 66 |
| XP when defeated | 231 |
| Damage | 7 to 10 |
| AC | 117 |
| BC | 133 |
| DR | 8 |
| Attacks per turn | 3 (4 AP each, 12 AP) |
| Crit chance | 9% (×1.5) |

**When you hit it:** On self: [Panic](../conditions/panic.md) (magnitude 1, 3 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Thin amphibian skin](../items/bwm_olm_drop.md) | 15% | 1 |
| [Gold coins](../items/gold.md) | 100% | 1 to 20 |
| [Wizened amphibian boots](../items/bwm_olm_drop2.md) | 3.5% | 1 |
| [Battered amphibian gloves](../items/bwm_olm_drop3.md) | 3.5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 74](../maps/blackwater_mountain74.md) | – | 7 | – |
| [Blackwater mountain 74 h](../maps/blackwater_mountain74_h.md) | – | 3 | – |
| [Blackwater mountain 75](../maps/blackwater_mountain75.md) | – | 8 | – |
| [Elm 5f 1](../maps/elm5f_1.md) | – | 1 | – |
| [Elm 2f 1](../maps/elm_2f_1.md) | – | 2 | – |
| [Elm mine 2](../maps/elm_mine2.md) | – | 6 | – |
| [Elm mine 3](../maps/elm_mine3.md) | – | 2 | – |
| [Elm mine 4](../maps/elm_mine4.md) | – | 6 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

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
    | Entry ID | `bwm_olm2` |
    | Type (wiki) | Enemy |
    | Spawn group | `bwm_olm` |
    | Loot table | `bwm_olm` |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_omi2:9` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "bwm_olm2",
     "name": "Albino olm",
     "iconID": "monsters_omi2:9",
     "maxHP": 66,
     "maxAP": 12,
     "moveCost": 4,
     "monsterClass": "animal",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 7,
      "max": 10
     },
     "spawnGroup": "bwm_olm",
     "droplistID": "bwm_olm",
     "attackCost": 4,
     "attackChance": 117,
     "criticalSkill": 10,
     "criticalMultiplier": 1.5,
     "blockChance": 133,
     "damageResistance": 8,
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "panic",
        "magnitude": 1,
        "duration": 3,
        "chance": "20"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
