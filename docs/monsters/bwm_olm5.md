---
description: "Contaminated olm is an enemy in Andor's Trail (animal) with 90 HP, worth 294 XP, found in elm_2f_1, elm_3f, elm_4f_1. Drops: Thin amphibian skin, Gold coins, Wizened amphibian boots, Battered amphibian gloves."
---

# ![](../assets/icons/monsters/monsters_rltiles2_23.png){ .sprite } Contaminated olm

**Found in:** [elm_2f_1](../maps/elm_2f_1.md), [elm_3f](../maps/elm_3f.md), [elm_4f_1](../maps/elm_4f_1.md), [elm_4f_2](../maps/elm_4f_2.md) (+4 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_23.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | elm_2f_1, elm_3f, elm_4f_1 |
| **Class** | Animal |
| **HP** | 90 |
| **XP when defeated** | 294 |
| **Entry ID** | `bwm_olm5` |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 90 |
| XP when defeated | 294 |
| Damage | 6 to 14 |
| Attack chance | 133 |
| Block chance | 146 |
| Damage resistance | 8 |
| Max AP | 12 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 4 AP |
| Critical skill | 25 |
| Critical multiplier | 1.5 |
| Critical hit chance | 17% |

**On hit:** On target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 2, 2 rounds, 10% chance)

**When hit:** On self: [Panic](../conditions/panic.md) (magnitude 1, 3 rounds, 30% chance); On target: [Nausea](../conditions/nausea.md) (magnitude 2, 2 rounds, 15% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

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
| [elm_2f_1](../maps/elm_2f_1.md) | – | 19 | – |
| [elm_3f](../maps/elm_3f.md) | – | 9 | – |
| [elm_4f_1](../maps/elm_4f_1.md) | – | 6 | – |
| [elm_4f_2](../maps/elm_4f_2.md) | – | 7 | – |
| [elm_4f_3](../maps/elm_4f_3.md) | – | 2 | – |
| [elm_4f_4](../maps/elm_4f_4.md) | – | 3 | – |
| [elm_4f_5](../maps/elm_4f_5.md) | – | 3 | – |
| [elm_mine5](../maps/elm_mine5.md) | – | 7 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `bwm_olm5` |
    | Spawn group | `elm_mine1` |
    | Loot table | `bwm_olm` |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles2:23` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "bwm_olm5",
     "name": "Contaminated olm",
     "iconID": "monsters_rltiles2:23",
     "maxHP": 90,
     "maxAP": 12,
     "moveCost": 4,
     "monsterClass": "animal",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 6,
      "max": 14
     },
     "spawnGroup": "elm_mine1",
     "droplistID": "bwm_olm",
     "attackChance": 133,
     "criticalSkill": 25,
     "criticalMultiplier": 1.5,
     "blockChance": 146,
     "damageResistance": 8,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 2,
        "duration": 2,
        "chance": "10"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "panic",
        "magnitude": 1,
        "duration": 3,
        "chance": "30"
       }
      ],
      "conditionsTarget": [
       {
        "condition": "nausea",
        "magnitude": 2,
        "duration": 2,
        "chance": "15"
       }
      ]
     }
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_olm5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
