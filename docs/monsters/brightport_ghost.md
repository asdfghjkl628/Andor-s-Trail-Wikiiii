---
description: "Agitated ghost is an NPC you can also fight in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_rltiles2_45.png){ .sprite } Agitated ghost

**Where to find Agitated ghost:** Brightport: [Brightport grave](../maps/brightport_grave.md#pin-npc-brightport_ghost)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles2_45.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Brightport |
| **Class** | Undead |
| **HP** | 159 |
| **XP when defeated** | 252 |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

!!! warning "You can fight Agitated ghost"
    Answering “You make no sense cursed creature, I will put you to rest now.” during [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-239) starts a fight with Agitated ghost.

    The conversation during [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-238) can lead straight into a fight with Agitated ghost.

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 159 |
| XP when defeated | 252 |
| Damage | 10 to 15 |
| AC | 80 |
| BC | 90 |
| DR | 3 |
| Attacks per turn | 1 (10 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Quests

- [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md): stages 238, 239, 241

## Dialogue simulator

Talk to Agitated ghost as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_ghost.json" data-npc="Agitated ghost" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (9 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_ghost"></span>**`brightport_ghost`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 241 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-241)

    - Next *(if reached stage 239 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-239))* → [brightport_ghost8](#d-brightport_ghost8)
    - Next *(if NOT reached stage 238 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-238))* → [brightport_ghost1](#d-brightport_ghost1)
    - Next *(if reached stage 238 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-238))* → [brightport_ghost6](#d-brightport_ghost6)

    <span id="d-brightport_ghost8"></span>**`brightport_ghost8`** Agitated ghost: “Vengeance, vengeance!” — **effects:** sets stage 239 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-239)

    - “I promise I will find a way to put you to rest properly.” → *conversation ends*
    - “You make no sense cursed creature, I will put you to rest now.” → *fight starts*

    <span id="d-brightport_ghost1"></span>**`brightport_ghost1`** [Agitated ghost](../monsters/brightport_ghost.md): “You scoundrel dogs of Feygard, how dare you disturb the rest of a knight of Nor City!”

    - Next → [brightport_ghost2](#d-brightport_ghost2)

    <span id="d-brightport_ghost6"></span>**`brightport_ghost6`** [Agitated ghost](../monsters/brightport_ghost.md): “The blood we shed for the Kingdom was in vain.”

    - Next → [brightport_ghost7](#d-brightport_ghost7)

    <span id="d-brightport_ghost2"></span>**`brightport_ghost2`** [Drendolas](../monsters/brightport_studentghost1.md): “Well actually I'm from Remgard and my friend over there is from...”

    - Next → [brightport_ghost3](#d-brightport_ghost3)

    <span id="d-brightport_ghost7"></span>**`brightport_ghost7`** [Agitated ghost](../monsters/brightport_ghost.md): “It was stolen to birth this curse, and now we cannot rest!”

    - Next → [brightport_ghost8](#d-brightport_ghost8)

    <span id="d-brightport_ghost3"></span>**`brightport_ghost3`** [Agitated ghost](../monsters/brightport_ghost.md): “Silence! No more of your lies... You used me!”

    - “It's time I put you to rest. [Fight.]” → [brightport_ghost4](#d-brightport_ghost4)
    - “What are you talking about?” → [brightport_ghost5](#d-brightport_ghost5)

    <span id="d-brightport_ghost4"></span>**`brightport_ghost4`** *(silent check: the first matching branch below is taken)* — **effects:** removes monsters from brightport_grave, removes monsters from brightport_grave, spawns monsters on brightport_school8, spawns monsters on brightport_school8, sets stage 238 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-238)

    - branch 1 → *fight starts*

    <span id="d-brightport_ghost5"></span>**`brightport_ghost5`** [Dummy NPC](../monsters/none.md): “The two kids sneak past the ghost and leave in a hurry.” — **effects:** sets stage 238 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-238), removes monsters from brightport_grave, removes monsters from brightport_grave, spawns monsters on brightport_school8, spawns monsters on brightport_school8

    - Next → [brightport_ghost6](#d-brightport_ghost6)



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 9 lines added |

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
    | Entry ID | `brightport_ghost` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `brightport_ghost` |
    | Loot table | – |
    | Conversation | `brightport_ghost` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:45` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_ghost",
     "name": "Agitated ghost",
     "iconID": "monsters_rltiles2:45",
     "maxHP": 159,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 10,
      "max": 15
     },
     "phraseID": "brightport_ghost",
     "attackChance": 80,
     "blockChance": 90,
     "damageResistance": 3
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
