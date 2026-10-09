---
description: "Prim guard is an NPC who can also be fought in Andor's Trail, found in Prim."
---

# ![](../assets/icons/monsters/monsters_rltiles1_65.png){ .sprite } Prim guard

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_65.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Prim |
| **Class** | Humanoid |
| **HP** | 60 |
| **XP when defeated** | 102 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game data defines 2 separate characters named Prim guard. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, combat statistics, faction, appearance, movement. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`prim_guard`](#v-prim_guard) | NPC/Enemy | Prim: [Blackwater mountain 29](../maps/blackwater_mountain29.md#pin-npc-prim_guard) | – | 60 |
| [`prim_guard6`](#v-prim_guard6) | NPC | Prim: [Blackwater mountain 29](../maps/blackwater_mountain29.md#pin-npc-prim_guard6) | – | – |

## Prim, Blackwater mountain 29 (prim_guard) { #v-prim_guard }

**Entry ID:** `prim_guard` · **Type:** NPC/Enemy

**Location:** Prim: [Blackwater mountain 29](../maps/blackwater_mountain29.md#pin-npc-prim_guard)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: this character belongs to the faction `fct_prim`, and the game treats members of a faction as hostile once your standing with that faction drops below zero.

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 60 |
| XP when defeated | 102 |
| Damage | 3 to 6 |
| Attack chance | 60 |
| Block chance | 70 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 29](../maps/blackwater_mountain29.md) | Prim | 1 | – |

### Dialogue simulator

Set your quest stages and items, then talk to Prim guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_guard4.json" data-npc="Prim guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-prim_guard-prim_guard4"></span>**`prim_guard4`** Prim guard: “Can't talk now. I'm on guard duty. If you need help, talk to someone else over there instead.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Attack chance: added (60)<br>Attack cost: added (5)<br>Attack damage: added (3–6)<br>Block chance: added (70)<br>Damage resistance: added (3)<br>Faction: added (fct_prim)<br>Max AP: added (10)<br>Max HP: added (60)<br>Move cost: added (5) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (prim_guard)"

    | | |
    |---|---|
    | Entry ID | `prim_guard` |
    | Spawn group | `prim_guard4` |
    | Loot table | – |
    | Conversation | `prim_guard4` |
    | Faction | `fct_prim` |
    | Movement | – |
    | Icon | `monsters_rltiles1:65` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "prim_guard",
     "name": "Prim guard",
     "iconID": "monsters_rltiles1:65",
     "maxHP": 60,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "prim_guard4",
     "faction": "fct_prim",
     "phraseID": "prim_guard4",
     "attackCost": 5,
     "attackChance": 60,
     "blockChance": 70,
     "damageResistance": 3
    }
    ```


## Prim, Blackwater mountain 29 (prim_guard6) { #v-prim_guard6 }

**Entry ID:** `prim_guard6` · **Type:** NPC

**Location:** Prim: [Blackwater mountain 29](../maps/blackwater_mountain29.md#pin-npc-prim_guard6)

### Dialogue simulator

Set your quest stages and items, then talk to Prim guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_guard6_1.json" data-npc="Prim guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-prim_guard6-prim_guard6_1"></span>**`prim_guard6_1`** [General Ortholion](../monsters/ortholion.md): “The guard is mumbling something to himself and seems to be ignoring you completely.”




### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (prim_guard6)"

    | | |
    |---|---|
    | Entry ID | `prim_guard6` |
    | Spawn group | `prim_guard6` |
    | Loot table | – |
    | Conversation | `prim_guard6_1` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles1:76` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "prim_guard6",
     "name": "Prim guard",
     "iconID": "monsters_rltiles1:76",
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "prim_guard6",
     "phraseID": "prim_guard6_1"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
