---
description: "Cave mole is an NPC who can also be fought in Andor's Trail, found in Bloskelt + Roskelt."
---

# ![](../assets/icons/monsters/monsters_rltiles1_50.png){ .sprite } Cave mole

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_50.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Bloskelt + Roskelt |
| **Class** | Animal |
| **HP** | 70 |
| **XP when defeated** | 157 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Cave mole. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, combat statistics, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`ratdom_maze_mole`](#v-ratdom_maze_mole) | NPC | Bloskelt + Roskelt: [ratdom_maze_516](../maps/ratdom_maze_516.md#pin-npc-ratdom_maze_mole) | – | – |
| [`ratdom_maze_mole2`](#v-ratdom_maze_mole2) | Enemy | Bloskelt + Roskelt: [ratdom_maze_516](../maps/ratdom_maze_516.md) | – | 70 |

## Bloskelt + Roskelt, Ratdom maze 516 (ratdom_maze_mole) { #v-ratdom_maze_mole }

**Entry ID:** `ratdom_maze_mole` · **Type:** NPC

**Location:** Bloskelt + Roskelt: [ratdom_maze_516](../maps/ratdom_maze_516.md#pin-npc-ratdom_maze_mole)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Cave mole. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_maze_mole.json" data-npc="Cave mole" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ratdom_maze_mole-ratdom_maze_mole"></span>**`ratdom_maze_mole`** Cave mole: “Who's there?”




### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_maze_mole)"

    | | |
    |---|---|
    | Entry ID | `ratdom_maze_mole` |
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


## Bloskelt + Roskelt, Ratdom maze 516 (ratdom_maze_mole2) { #v-ratdom_maze_mole2 }

**Entry ID:** `ratdom_maze_mole2` · **Type:** Enemy

**Location:** Bloskelt + Roskelt: [ratdom_maze_516](../maps/ratdom_maze_516.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 70 |
| XP when defeated | 157 |
| Damage | 8 to 15 |
| Attack chance | 120 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 1, 2 rounds, 75% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_516](../maps/ratdom_maze_516.md) | Bloskelt + Roskelt | 2 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_maze_mole2)"

    | | |
    |---|---|
    | Entry ID | `ratdom_maze_mole2` |
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



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


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
