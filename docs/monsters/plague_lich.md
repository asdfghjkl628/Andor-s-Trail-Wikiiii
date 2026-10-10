---
description: "Plague-Lich is an enemy in Andor's Trail (undead) with 263 HP, worth 729 XP, found in Undertell 10, Undertell 11, Undertell 21. Drops: Gold coins, Lich dust, Major potion of health."
---

# ![](../assets/icons/monsters/monsters_tometik8_58.png){ .sprite } Plague-Lich

**Found in:** [Undertell 10](../maps/undertell_10.md), [Undertell 11](../maps/undertell_11.md), [Undertell 21](../maps/undertell_21.md), [Undertell 3 lava 10](../maps/undertell_3_lava_10.md) (+7 more)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik8_58.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Undertell 10, Undertell 11, Undertell 21 |
| **Class** | Undead |
| **HP** | 263 |
| **XP when defeated** | 729 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 263 |
| XP when defeated | 729 |
| Damage | 9 to 11 |
| AC | 202 |
| BC | 176 |
| DR | 10 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | 11% (×2.0) |

**Its hits:** On target: [Death Plague](../conditions/death_plague.md) (magnitude 3, 4 rounds, 20% chance)

**When it dies:** On self: [Death Plague](../conditions/death_plague.md) (magnitude 2, 3 rounds); [Reclaimed resilience](../conditions/reclaimed_resilience.md) (magnitude 5, 3 rounds)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 40% | 10 to 14 |
| [Lich dust](../items/lich_dust.md) | 9% | 1 |
| [Major potion of health](../items/health_major2.md) | 25% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Undertell 10](../maps/undertell_10.md) | – | 1 | – |
| [Undertell 11](../maps/undertell_11.md) | – | 1 | – |
| [Undertell 21](../maps/undertell_21.md) | – | 1 | – |
| [Undertell 3 lava 10](../maps/undertell_3_lava_10.md) | – | 2 | – |
| [Undertell 4 00](../maps/undertell_4_00.md) | – | 1 | – |
| [Undertell 4 10](../maps/undertell_4_10.md) | – | 2 | – |
| [Undertell 4 11](../maps/undertell_4_11.md) | – | 1 | – |
| [Undertell 7 00](../maps/undertell_7_00.md) | – | 4 | – |
| [Undertell 7 01](../maps/undertell_7_01.md) | – | 2 | – |
| [Undertell 7 10](../maps/undertell_7_10.md) | – | 2 | – |
| [Undertell 7 11](../maps/undertell_7_11.md) | – | 1 | – |


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
    | Entry ID | `plague_lich` |
    | Type (wiki) | Enemy |
    | Spawn group | `helpPlagueLich` |
    | Loot table | `plague_lich_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik8:58` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "plague_lich",
     "name": "Plague-Lich",
     "iconID": "monsters_tometik8:58",
     "maxHP": 263,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 9,
      "max": 11
     },
     "spawnGroup": "helpPlagueLich",
     "droplistID": "plague_lich_dl",
     "attackCost": 4,
     "attackChance": 202,
     "criticalSkill": 13,
     "criticalMultiplier": 2.0,
     "blockChance": 176,
     "damageResistance": 10,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "death_plague",
        "magnitude": 3,
        "duration": 4,
        "chance": "20"
       }
      ]
     },
     "deathEffect": {
      "conditionsSource": [
       {
        "condition": "death_plague",
        "magnitude": 2,
        "duration": 3,
        "chance": "100"
       },
       {
        "condition": "reclaimed_resilience",
        "magnitude": 5,
        "duration": 3,
        "chance": "100"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plague_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plague_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plague_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=plague_lich.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
