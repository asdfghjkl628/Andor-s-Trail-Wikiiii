---
description: "Cave mole is an NPC you can also fight in Andor's Trail, found in Bloskelt + Roskelt."
---

# ![](../assets/icons/monsters/monsters_rltiles1_50.png){ .sprite } Cave mole

**Where to find Cave mole:** [Bloskelt + Roskelt, Ratdom maze 516](#v-ratdom_maze_mole), [Bloskelt + Roskelt, Ratdom maze 516](#v-ratdom_maze_mole2)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles1_50.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Bloskelt + Roskelt |
| **Class** | Animal |
| **HP** | 70 |
| **XP when defeated** | 157 |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

## Bloskelt + Roskelt, Ratdom maze 516 { #v-ratdom_maze_mole }

**Where:** Bloskelt + Roskelt: [Ratdom maze 516](../maps/ratdom_maze_516.md#pin-npc-ratdom_maze_mole)

### Dialogue simulator

Talk to Cave mole as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_maze_mole.json" data-npc="Cave mole" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ratdom_maze_mole-ratdom_maze_mole"></span>**`ratdom_maze_mole`** Cave mole: “Who's there?”




### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Bloskelt + Roskelt, Ratdom maze 516 (2) { #v-ratdom_maze_mole2 }

**Where:** Bloskelt + Roskelt: [Ratdom maze 516](../maps/ratdom_maze_516.md)

### Combat

| | |
|---|---|
| Class | Animal |
| HP | 70 |
| XP when defeated | 157 |
| Damage | 8 to 15 |
| AC | 120 |
| BC | 0 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 1, 2 rounds, 75% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Ratdom maze 516](../maps/ratdom_maze_516.md) | Bloskelt + Roskelt | 2 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Cave mole. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, combat statistics, movement.

| Entry | Type | Section |
|---|---|---|
| `ratdom_maze_mole` | NPC | [Bloskelt + Roskelt, Ratdom maze 516](#v-ratdom_maze_mole) |
| `ratdom_maze_mole2` | Enemy | [Bloskelt + Roskelt, Ratdom maze 516](#v-ratdom_maze_mole2) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: ratdom_maze_mole"

    | | |
    |---|---|
    | Entry ID | `ratdom_maze_mole` |
    | Type (wiki) | NPC |
    | Spawn group | `ratdom_maze_mole` |
    | Loot table | – |
    | Conversation | `ratdom_maze_mole` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:50` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_maze_mole",
     "name": "Cave mole",
     "iconID": "monsters_rltiles1:50",
     "moveCost": 5,
     "spawnGroup": "ratdom_maze_mole",
     "phraseID": "ratdom_maze_mole"
    }
    ```

??? info "Technical information: ratdom_maze_mole2"

    | | |
    |---|---|
    | Entry ID | `ratdom_maze_mole2` |
    | Type (wiki) | Enemy |
    | Spawn group | `ratdom_maze_mole2` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_rltiles1:50` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_maze_mole2",
     "name": "Cave mole",
     "iconID": "monsters_rltiles1:50",
     "maxHP": 70,
     "unique": 1,
     "monsterClass": "animal",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 8,
      "max": 15
     },
     "spawnGroup": "ratdom_maze_mole2",
     "attackCost": 5,
     "attackChance": 120,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 1,
        "duration": 2,
        "chance": "75"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_maze_mole.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_maze_mole.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_maze_mole.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_maze_mole.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
