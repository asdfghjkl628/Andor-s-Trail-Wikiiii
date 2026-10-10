---
description: "Prim guard is an NPC you can also fight in Andor's Trail, found in Prim."
---

# ![](../assets/icons/monsters/monsters_rltiles1_65.png){ .sprite } Prim guard

**Where to find Prim guard:** [Prim, Blackwater mountain 29](#v-prim_guard), [Prim, Blackwater mountain 29](#v-prim_guard6)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles1_65.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Prim |
| **Class** | Humanoid |
| **HP** | 60 |
| **XP when defeated** | 102 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Prim, Blackwater mountain 29 { #v-prim_guard }

**Where:** Prim: [Blackwater mountain 29](../maps/blackwater_mountain29.md#pin-npc-prim_guard)

!!! warning "You can fight Prim guard"
    Prim guard turns hostile if you fall out with their faction (this can happen in [The agent and the beast](../quests/bwm_agent.md)).

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 60 |
| XP when defeated | 102 |
| Damage | 3 to 6 |
| AC | 60 |
| BC | 70 |
| DR | 3 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Dialogue simulator

Talk to Prim guard as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_guard4.json" data-npc="Prim guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-prim_guard-prim_guard4"></span>**`prim_guard4`** Prim guard: “Can't talk now. I'm on guard duty. If you need help, talk to someone else over there instead.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Attack chance: added (60)<br>Attack cost: added (5)<br>Attack damage: added (3–6)<br>Block chance: added (70)<br>Damage resistance: added (3)<br>Faction: added (fct_prim)<br>Max AP: added (10)<br>Max HP: added (60)<br>Move cost: added (5) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Prim, Blackwater mountain 29 (2) { #v-prim_guard6 }

**Where:** Prim: [Blackwater mountain 29](../maps/blackwater_mountain29.md#pin-npc-prim_guard6)

### Dialogue simulator

Talk to Prim guard as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_guard6_1.json" data-npc="Prim guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-prim_guard6-prim_guard6_1"></span>**`prim_guard6_1`** [General Ortholion](../monsters/ortholion.md): “The guard is mumbling something to himself and seems to be ignoring you completely.”




### Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Prim guard. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, combat statistics, faction, appearance, movement.

| Entry | Type | Section |
|---|---|---|
| `prim_guard` | NPC/Enemy | [Prim, Blackwater mountain 29](#v-prim_guard) |
| `prim_guard6` | NPC | [Prim, Blackwater mountain 29](#v-prim_guard6) |

- `prim_guard` belongs to the faction `fct_prim`. The game treats any character as hostile once your standing with its faction is below zero.

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: prim_guard"

    | | |
    |---|---|
    | Entry ID | `prim_guard` |
    | Type (wiki) | NPC/Enemy |
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

??? info "Technical information: prim_guard6"

    | | |
    |---|---|
    | Entry ID | `prim_guard6` |
    | Type (wiki) | NPC |
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
