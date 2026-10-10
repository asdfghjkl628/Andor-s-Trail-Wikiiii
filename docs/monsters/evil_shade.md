---
description: "Evil shade is an enemy in Andor's Trail (ghost) with 431 HP, worth 1215 XP, found in Undertell 3 02."
---

# ![](../assets/icons/monsters/monsters_newb_1_663.png){ .sprite } Evil shade

**Found in:** [Undertell 3 02](../maps/undertell_3_02.md)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_newb_1_663.png" alt=""></p>

| | |
|---|---|
| **Type** | Enemy (hostile on sight) |
| **Found in** | Undertell 3 02 |
| **Class** | Ghost |
| **HP** | 431 |
| **XP when defeated** | 1,215 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Combat

| | |
|---|---|
| Class | Ghost |
| HP | 431 |
| XP when defeated | 1,215 |
| Damage | 5 to 7 |
| AC | 205 |
| BC | 250 |
| DR | 9 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Deathtouch](../conditions/deathtouch.md) (magnitude 1, 2 rounds, 25% chance)

**When you hit it:** On target: [Revealed](../conditions/revealed.md) (magnitude 4, 2 rounds, 40% chance)

**When it dies:** On self: [Curse of Vainglory](../conditions/vainglory.md) (magnitude 5, until rest)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Undertell 3 02](../maps/undertell_3_02.md) | – | 66 | Appears later, during a quest |

## Quests that count defeats

- A conversation with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that at least 11 of these enemies have been defeated.
- A conversation with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that at least 10 of these enemies have been defeated.
- A conversation with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that at least 9 of these enemies have been defeated.
- A conversation with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that at least 8 of these enemies have been defeated.
- A conversation with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that at least 7 of these enemies have been defeated.
- A conversation with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that at least 6 of these enemies have been defeated.
- A conversation with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that at least 5 of these enemies have been defeated.
- A conversation with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that at least 4 of these enemies have been defeated.
- A conversation with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that at least 3 of these enemies have been defeated.
- A conversation with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that at least 2 of these enemies have been defeated.
- A conversation with stepping on a trigger on [Undertell 3 02](../maps/undertell_3_02.md) checks that this enemy has been defeated.


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
    | Entry ID | `evil_shade` |
    | Type (wiki) | Enemy |
    | Spawn group | `help_anoa` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_newb_1:663` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "evil_shade",
     "name": "Evil shade",
     "iconID": "monsters_newb_1:663",
     "maxHP": 431,
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "ghost",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 5,
      "max": 7
     },
     "spawnGroup": "help_anoa",
     "horizontalFlipChance": 50,
     "attackCost": 5,
     "attackChance": 205,
     "blockChance": 250,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "deathtouch",
        "magnitude": 1,
        "duration": 2,
        "chance": "25"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "revealed",
        "magnitude": 4,
        "duration": 2,
        "chance": "40"
       }
      ]
     },
     "deathEffect": {
      "conditionsSource": [
       {
        "condition": "vainglory",
        "magnitude": 5,
        "duration": 998,
        "chance": "100"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=evil_shade.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=evil_shade.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=evil_shade.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=evil_shade.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
