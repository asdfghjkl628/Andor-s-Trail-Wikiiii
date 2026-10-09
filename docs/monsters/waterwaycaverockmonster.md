---
description: "Rock fiend is an enemy in Andor's Trail (construct) with 80 HP, worth 202 XP, found in Waterwayacave 1, Waterwayacave 2, Waterwayacave 3. Drops: Gold coins, Azure gem, Stone club, Small rock."
---

# ![](../assets/icons/monsters/monsters_tometik1_46.png){ .sprite } Rock fiend

**Found in:** [Waterwayacave 1](../maps/waterwayacave1.md), [Waterwayacave 2](../maps/waterwayacave2.md), [Waterwayacave 3](../maps/waterwayacave3.md), [Waterwayacave 4](../maps/waterwayacave4.md)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik1_46.png){ .sprite }</p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Waterwayacave 1, Waterwayacave 2, Waterwayacave 3 |
| **Class** | Construct |
| **HP** | 80 |
| **XP when defeated** | 202 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Combat

| | |
|---|---|
| Class | Construct |
| HP | 80 |
| XP when defeated | 202 |
| Damage | 6 to 8 |
| AC | 60 |
| BC | 80 |
| DR | 3 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 9% (×2.0) |

**Immune to critical hits.**

**Its hits:** On target: [Petrification](../conditions/petrification.md) (magnitude 1, 4 rounds, 25% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 25% | 10 to 15 |
| [Azure gem](../items/gem6.md) | 5% | 1 |
| [Stone club](../items/club_stone.md) | 2% | 1 |
| [Small rock](../items/rock.md) | 5% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waterwayacave 1](../maps/waterwayacave1.md) | – | 10 | – |
| [Waterwayacave 2](../maps/waterwayacave2.md) | – | 12 | – |
| [Waterwayacave 3](../maps/waterwayacave3.md) | – | 24 | – |
| [Waterwayacave 4](../maps/waterwayacave4.md) | – | 11 | – |


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

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
    | Entry ID | `waterwaycaverockmonster` |
    | Type (wiki) | Enemy |
    | Spawn group | `waterwaycaverockmonster` |
    | Loot table | `waterwaycaverockmonster` |
    | Conversation | – |
    | Faction | – |
    | Movement | helpOthers |
    | Icon | `monsters_tometik1:46` |
    | Defined in | `res/raw/monsterlist_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "waterwaycaverockmonster",
     "name": "Rock fiend",
     "iconID": "monsters_tometik1:46",
     "maxHP": 80,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "construct",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 6,
      "max": 8
     },
     "droplistID": "waterwaycaverockmonster",
     "attackCost": 3,
     "attackChance": 60,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 80,
     "damageResistance": 3,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "petrification",
        "magnitude": 1,
        "duration": 4,
        "chance": "25"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waterwaycaverockmonster.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waterwaycaverockmonster.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waterwaycaverockmonster.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=waterwaycaverockmonster.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
