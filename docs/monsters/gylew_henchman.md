---
description: "Gylew's henchman is an NPC who can also be fought in Andor's Trail, found in waterway5."
---

# ![](../assets/icons/monsters/monsters_men_8.png){ .sprite } Gylew's henchman

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_8.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | waterway5 |
| **Class** | Humanoid |
| **HP** | 219 |
| **XP when defeated** | 394 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Gylew's henchman. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, combat statistics, loot or shop stock, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`gylew_henchman`](#v-gylew_henchman) | NPC | [waterway5](../maps/waterway5.md#pin-npc-gylew_henchman) | – | – |
| [`gylew_henchman_aggresive`](#v-gylew_henchman_aggresive) | Enemy | [waterway5](../maps/waterway5.md) | – | 219 |

## Waterway5 (gylew_henchman) { #v-gylew_henchman }

**Entry ID:** `gylew_henchman` · **Type:** NPC

**Location:** [waterway5](../maps/waterway5.md#pin-npc-gylew_henchman)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Gylew's henchman. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/gylew_henchman.json" data-npc="Gylew&#x27;s henchman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-gylew_henchman-gylew_henchman"></span>**`gylew_henchman`** Gylew's henchman: “Hey, I'm trying to admire the view here. Get out of my way.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.8.11](../versions/0.8.11.md) | Attack chance: added (70)<br>Attack cost: added (3)<br>Attack damage: added (11–22)<br>Block chance: added (60)<br>Loot table added<br>Max HP: added (200)<br>Move cost: added (5) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (gylew_henchman)"

    | | |
    |---|---|
    | Entry ID | `gylew_henchman` |
    | Spawn group | `gylew_henchman` |
    | Loot table | `gold100` |
    | Conversation | `gylew_henchman` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:8` |
    | Defined in | `res/raw/monsterlist_v0611_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "gylew_henchman",
     "name": "Gylew's henchman",
     "iconID": "monsters_men:8",
     "maxHP": 200,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 11,
      "max": 22
     },
     "spawnGroup": "gylew_henchman",
     "phraseID": "gylew_henchman",
     "droplistID": "gold100",
     "attackCost": 3,
     "attackChance": 70,
     "blockChance": 60
    }
    ```


## Waterway5 (gylew_henchman_aggresive) { #v-gylew_henchman_aggresive }

**Entry ID:** `gylew_henchman_aggresive` · **Type:** Enemy

**Location:** [waterway5](../maps/waterway5.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 219 |
| XP when defeated | 394 |
| Damage | 14 to 19 |
| Attack chance | 85 |
| Block chance | 55 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 2 AP |
| Critical skill | 25 |
| Critical multiplier | 2.5 |
| Critical hit chance | 17% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Feline hat](../items/feline_hat.md) | 100% | 1 |
| [Brimhaven brew](../items/brv_brew.md) | 100% | 1 to 3 |
| [Smoked sausage](../items/smoked-sausage.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [waterway5](../maps/waterway5.md) | – | 1 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (gylew_henchman_aggresive)"

    | | |
    |---|---|
    | Entry ID | `gylew_henchman_aggresive` |
    | Spawn group | `help_gylew` |
    | Loot table | `gylew_henchman_dl` |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_men:8` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "gylew_henchman_aggresive",
     "name": "Gylew's henchman",
     "iconID": "monsters_men:8",
     "maxHP": 219,
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 14,
      "max": 19
     },
     "spawnGroup": "help_gylew",
     "droplistID": "gylew_henchman_dl",
     "attackCost": 3,
     "attackChance": 85,
     "criticalSkill": 25,
     "criticalMultiplier": 2.5,
     "blockChance": 55,
     "damageResistance": 2
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gylew_henchman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gylew_henchman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gylew_henchman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gylew_henchman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
