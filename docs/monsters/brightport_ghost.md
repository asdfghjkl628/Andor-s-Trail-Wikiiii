---
description: "Agitated ghost is an NPC who can also be fought in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_rltiles2_45.png){ .sprite } Agitated ghost

**Where to find Agitated ghost:** Brightport: [brightport_grave](../maps/brightport_grave.md#pin-npc-brightport_ghost)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_45.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Brightport |
| **Class** | Undead |
| **HP** | 159 |
| **XP when defeated** | 252 |
| **Entry ID** | `brightport_ghost` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 159 |
| XP when defeated | 252 |
| Damage | 10 to 15 |
| Attack chance | 80 |
| Block chance | 90 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brightport_grave](../maps/brightport_grave.md) | Brightport | 1 | – |

## Quests

- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 238, 239, 241

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Agitated ghost. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_ghost.json" data-npc="Agitated ghost" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_ghost"></span>**`brightport_ghost`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 241 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-241)

    - Next *(if reached stage 239 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-239))* → [brightport_ghost8](#d-brightport_ghost8)
    - Next *(if NOT reached stage 238 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-238))* → [brightport_ghost1](#d-brightport_ghost1)
    - Next *(if reached stage 238 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-238))* → [brightport_ghost6](#d-brightport_ghost6)

    <span id="d-brightport_ghost8"></span>**`brightport_ghost8`** Agitated ghost: “Vengeance, vengeance!” — **effects:** sets stage 239 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-239)

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

    <span id="d-brightport_ghost4"></span>**`brightport_ghost4`** *(silent check: the first matching branch below is taken)* — **effects:** removes monsters from brightport_grave, removes monsters from brightport_grave, spawns monsters on brightport_school8, spawns monsters on brightport_school8, sets stage 238 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-238)

    - branch 1 → *fight starts*

    <span id="d-brightport_ghost5"></span>**`brightport_ghost5`** [Dummy NPC](../monsters/none.md): “The two kids sneak past the ghost and leave in a hurry.” — **effects:** sets stage 238 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-238), removes monsters from brightport_grave, removes monsters from brightport_grave, spawns monsters on brightport_school8, spawns monsters on brightport_school8

    - Next → [brightport_ghost6](#d-brightport_ghost6)



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightport_ghost` |
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


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


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
