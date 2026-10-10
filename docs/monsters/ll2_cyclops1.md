---
description: "Polyasem is an NPC you can also fight in Andor's Trail, found in Ll 2 cyclops cave, Mountainlake 27."
---

# ![](../assets/icons/monsters/monsters_ld1_37.png){ .sprite } Polyasem

**Where to find Polyasem:** [Ll 2 cyclops cave](../maps/ll2_cyclops_cave.md#pin-npc-ll2_cyclops1), [Mountainlake 27](../maps/mountainlake27.md#pin-npc-ll2_cyclops1)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_37.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Ll 2 cyclops cave, Mountainlake 27 |
| **Class** | Humanoid |
| **HP** | 100 |
| **XP when defeated** | 194 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

!!! warning "You can fight Polyasem"
    The conversation can lead straight into a fight with Polyasem.

    Polyasem turns hostile if you fall out with their faction.

## Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 100 |
| XP when defeated | 194 |
| Damage | 8 to 16 |
| AC | 100 |
| BC | 50 |
| DR | 10 |
| Attacks per turn | 1 (10 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Ll 2 cyclops cave](../maps/ll2_cyclops_cave.md) | – | 1 | – |
| [Mountainlake 27](../maps/mountainlake27.md) | – | 1 | Appears later, during a quest |

## Dialogue simulator

Talk to Polyasem as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/ll2_cyclops.json" data-npc="Polyasem" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ll2_cyclops"></span>**`ll2_cyclops`** Polyasem: “Ah, there is Nobody. You think you're particularly clever, don't you?”

    - “Well, it has worked with your brother.” → [ll2_cyclops_10](#d-ll2_cyclops_10)

    <span id="d-ll2_cyclops_10"></span>**`ll2_cyclops_10`** Polyasem: “Now let go of the ram and act like a man, kid.”

    - “Well, you'll see what you get for it. Attack!” → [ll2_cyclops_20](#d-ll2_cyclops_20)

    <span id="d-ll2_cyclops_20"></span>**`ll2_cyclops_20`** Polyasem: “Our brother has made us a magnificant gift: We get to hunt our own holiday roast...” — **effects:** spawns monsters on mountainlake27, faction “ll2_cyclops” set to -1

    - Next → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

- `ll2_cyclops1` belongs to the faction `ll2_cyclops`. The game treats any character as hostile once your standing with its faction is below zero.

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ll2_cyclops1` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `ll2_cyclops1` |
    | Loot table | – |
    | Conversation | `ll2_cyclops` |
    | Faction | `ll2_cyclops` |
    | Movement | – |
    | Icon | `monsters_ld1:37` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_cyclops1",
     "name": "Polyasem",
     "iconID": "monsters_ld1:37",
     "maxHP": 100,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 8,
      "max": 16
     },
     "spawnGroup": "ll2_cyclops1",
     "faction": "ll2_cyclops",
     "phraseID": "ll2_cyclops",
     "attackCost": 10,
     "attackChance": 100,
     "blockChance": 50,
     "damageResistance": 10
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_cyclops1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_cyclops1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_cyclops1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_cyclops1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
