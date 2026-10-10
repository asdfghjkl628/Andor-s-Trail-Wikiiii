---
description: "Gylew's henchman is an NPC you can also fight in Andor's Trail, found in Waterway 5."
---

# ![](../assets/icons/monsters/monsters_men_8.png){ .sprite } Gylew's henchman

**Where to find Gylew's henchman:** [Waterway 5](#v-gylew_henchman), [Waterway 5](#v-gylew_henchman_aggresive)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_men_8.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Waterway 5 |
| **Class** | Humanoid |
| **HP** | 219 |
| **XP when defeated** | 394 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Waterway 5 { #v-gylew_henchman }

**Where:** [Waterway 5](../maps/waterway5.md#pin-npc-gylew_henchman)

### Dialogue simulator

Talk to Gylew's henchman as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/gylew_henchman.json" data-npc="Gylew&#x27;s henchman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-gylew_henchman-gylew_henchman"></span>**`gylew_henchman`** Gylew's henchman: “Hey, I'm trying to admire the view here. Get out of my way.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.8.11](../versions/0.8.11.md) | Attack chance: added (70)<br>Attack cost: added (3)<br>Attack damage: added (11–22)<br>Block chance: added (60)<br>Loot table added<br>Max HP: added (200)<br>Move cost: added (5) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Waterway 5 (2) { #v-gylew_henchman_aggresive }

**Where:** [Waterway 5](../maps/waterway5.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 219 |
| XP when defeated | 394 |
| Damage | 14 to 19 |
| AC | 85 |
| BC | 55 |
| DR | 2 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 17% (×2.5) |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Feline hat](../items/feline_hat.md) | 100% | 1 |
| [Brimhaven brew](../items/brv_brew.md) | 100% | 1 to 3 |
| [Smoked sausage](../items/smoked-sausage.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Waterway 5](../maps/waterway5.md) | – | 1 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Gylew's henchman. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, combat statistics, loot or shop stock, movement.

| Entry | Type | Section |
|---|---|---|
| `gylew_henchman` | NPC | [Waterway 5](#v-gylew_henchman) |
| `gylew_henchman_aggresive` | Enemy | [Waterway 5](#v-gylew_henchman_aggresive) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: gylew_henchman"

    | | |
    |---|---|
    | Entry ID | `gylew_henchman` |
    | Type (wiki) | NPC |
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

??? info "Technical information: gylew_henchman_aggresive"

    | | |
    |---|---|
    | Entry ID | `gylew_henchman_aggresive` |
    | Type (wiki) | Enemy |
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
