---
description: "Blackened olm is an enemy in Andor's Trail (animal) with 75 HP, worth 261 XP, found in Blackwater mountain 75, Elm 4f 5, Elm mine 2. Drops: Thin amphibian skin, Gold coins, Wizened amphibian boots, Battered amphibian gloves."
---

# ![](../assets/icons/monsters/monsters_rltiles2_20.png){ .sprite } Blackened olm

**Found in:** [Blackwater mountain 75](../maps/blackwater_mountain75.md), [Elm 4f 5](../maps/elm_4f_5.md), [Elm mine 2](../maps/elm_mine2.md), [Elm mine 3](../maps/elm_mine3.md) (+2 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_20.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Blackwater mountain 75, Elm 4f 5, Elm mine 2 |
| **Class** | Animal |
| **HP** | 75 |
| **XP when defeated** | 261 |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 75 |
| XP when defeated | 261 |
| Damage | 8 to 11 |
| AC | 120 |
| BC | 135 |
| DR | 7 |
| Attacks per turn | 3 (4 AP each, 12 AP) |
| Crit chance | 15% (×1.5) |

**When you hit it:** On self: [Panic](../conditions/panic.md) (magnitude 1, 3 rounds, 30% chance)


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
| [Blackwater mountain 75](../maps/blackwater_mountain75.md) | – | 11 | – |
| [Elm 4f 5](../maps/elm_4f_5.md) | – | 5 | – |
| [Elm mine 2](../maps/elm_mine2.md) | – | 5 | – |
| [Elm mine 3](../maps/elm_mine3.md) | – | 8 | – |
| [Elm mine 4](../maps/elm_mine4.md) | – | 4 | – |
| [Elm mine 5](../maps/elm_mine5.md) | – | 3 | – |


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
    | Entry ID | `bwm_olm4` |
    | Type (wiki) | Enemy |
    | Spawn group | `bwm_olm2` |
    | Loot table | `bwm_olm` |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles2:20` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "bwm_olm4",
     "name": "Blackened olm",
     "iconID": "monsters_rltiles2:20",
     "maxHP": 75,
     "maxAP": 12,
     "moveCost": 4,
     "monsterClass": "animal",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 8,
      "max": 11
     },
     "spawnGroup": "bwm_olm2",
     "droplistID": "bwm_olm",
     "attackCost": 4,
     "attackChance": 120,
     "criticalSkill": 20,
     "criticalMultiplier": 1.5,
     "blockChance": 135,
     "damageResistance": 7,
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "panic",
        "magnitude": 1,
        "duration": 3,
        "chance": "30"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
