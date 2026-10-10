---
description: "Kazaul crimson arbiter lich is an enemy in Andor's Trail (undead) with 305 HP, worth 883 XP, found in Undertell 4 00, Undertell 4 01, Undertell 4 10. Drops: Gold coins, Lich dust, Major potion of health, Kazaul bonemeal."
---

# ![](../assets/icons/monsters/monsters_antison_5.png){ .sprite } Kazaul crimson arbiter lich

**Found in:** [Undertell 4 00](../maps/undertell_4_00.md), [Undertell 4 01](../maps/undertell_4_01.md), [Undertell 4 10](../maps/undertell_4_10.md), [Undertell 4 11](../maps/undertell_4_11.md) (+5 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_antison_5.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Undertell 4 00, Undertell 4 01, Undertell 4 10 |
| **Class** | Undead |
| **HP** | 305 |
| **XP when defeated** | 883 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 305 |
| XP when defeated | 883 |
| Damage | 11 to 13 |
| AC | 210 |
| BC | 190 |
| DR | 12 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | 12% (×2.0) |

**Its hits:** On target: [Divine judgement](../conditions/divine_judgement.md) (magnitude 1, 3 rounds, 14% chance)

**When you hit it:** On target: [Kazaul possession](../conditions/kazarite_misery.md) (magnitude 1, 2 rounds, 5% chance)

**When it dies:** On self: [Divine punishment](../conditions/divine_punishment.md) (magnitude 1, 2 rounds)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 50% | 9 to 10 |
| [Lich dust](../items/lich_dust.md) | 11% | 1 |
| [Major potion of health](../items/health_major2.md) | 40% | 2 to 3 |
| [Kazaul bonemeal](../items/pot_bm_kazaul.md) | 9% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Undertell 4 00](../maps/undertell_4_00.md) | – | 3 | – |
| [Undertell 4 01](../maps/undertell_4_01.md) | – | 5 | – |
| [Undertell 4 10](../maps/undertell_4_10.md) | – | 7 | – |
| [Undertell 4 11](../maps/undertell_4_11.md) | – | 3 | – |
| [Undertell 5](../maps/undertell_5.md) | – | 4 | – |
| [Undertell 7 00](../maps/undertell_7_00.md) | – | 1 | – |
| [Undertell 7 01](../maps/undertell_7_01.md) | – | 4 | – |
| [Undertell 7 10](../maps/undertell_7_10.md) | – | 9 | – |
| [Undertell 7 11](../maps/undertell_7_11.md) | – | 5 | – |


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

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
    | Entry ID | `kazaul_crimson_arbiter_lich` |
    | Type (wiki) | Enemy |
    | Spawn group | `kazaul_crimson_arbiter_lich` |
    | Loot table | `undertell_level4_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_antison:5` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "kazaul_crimson_arbiter_lich",
     "name": "Kazaul crimson arbiter lich",
     "iconID": "monsters_antison:5",
     "maxHP": 305,
     "moveCost": 4,
     "monsterClass": "undead",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 11,
      "max": 13
     },
     "horizontalFlipChance": 50,
     "droplistID": "undertell_level4_lich_dl",
     "attackCost": 4,
     "attackChance": 210,
     "criticalSkill": 15,
     "criticalMultiplier": 2.0,
     "blockChance": 190,
     "damageResistance": 12,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "divine_judgement",
        "magnitude": 1,
        "duration": 3,
        "chance": "14"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "kazarite_misery",
        "magnitude": 1,
        "duration": 2,
        "chance": "5"
       }
      ]
     },
     "deathEffect": {
      "conditionsSource": [
       {
        "condition": "divine_punishment",
        "magnitude": 1,
        "duration": 2,
        "chance": "100"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_crimson_arbiter_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_crimson_arbiter_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_crimson_arbiter_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_crimson_arbiter_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
