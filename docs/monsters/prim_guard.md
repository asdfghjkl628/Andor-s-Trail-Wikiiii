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
    The game's data files define 2 separate characters named Prim guard. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, combat statistics, faction, appearance, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`prim_guard`](#v-prim_guard) | NPC/Enemy | Prim: [blackwater_mountain29](../maps/blackwater_mountain29.md#pin-npc-prim_guard) | – | 60 |
| [`prim_guard6`](#v-prim_guard6) | NPC | Prim: [blackwater_mountain29](../maps/blackwater_mountain29.md#pin-npc-prim_guard6) | – | – |

## Prim, Blackwater mountain29 (prim_guard) { #v-prim_guard }

**Entry ID:** `prim_guard` · **Type:** NPC/Enemy

**Location:** Prim: [blackwater_mountain29](../maps/blackwater_mountain29.md#pin-npc-prim_guard)

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
| [blackwater_mountain29](../maps/blackwater_mountain29.md) | Prim | 1 | – |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Prim guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_guard4.json" data-npc="Prim guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-prim_guard-prim_guard4"></span>**`prim_guard4`** Prim guard: “Can't talk now. I'm on guard duty. If you need help, talk to someone else over there instead.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | attackChance added (60); attackCost added (5); attackDamage added ({"max": 6, "min": 3}); blockChance added (70); damageResistance added (3); faction added (fct_prim) (+3 more) |

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


## Prim, Blackwater mountain29 (prim_guard6) { #v-prim_guard6 }

**Entry ID:** `prim_guard6` · **Type:** NPC

**Location:** Prim: [blackwater_mountain29](../maps/blackwater_mountain29.md#pin-npc-prim_guard6)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Prim guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_guard6_1.json" data-npc="Prim guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

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
