---
description: "Dying patrol is a non-player character (NPC) in Andor's Trail, found in Crackshot hideout 2."
---

# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Dying patrol

**Where to find Dying patrol:** [Crackshot hideout 2](../maps/crackshot_hideout2.md#pin-npc-g03_deadpatrol_1)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Crackshot hideout 2 |
| **Entry ID** | `g03_deadpatrol_1` |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

## Quests

- [The ruthless Crackshot](../quests/Thieves03.md): stages 25, 28
- [Thieves story flags (hidden flag)](../quests/thieves_hidden.md): stage 40

## Dialogue simulator

Set your quest stages and items, then talk to Dying patrol. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guild03_deadpatrol1_select.json" data-npc="Dying patrol" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guild03_deadpatrol1_select"></span>**`guild03_deadpatrol1_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 50 of [Thieves story flags (hidden flag)](../quests/thieves_hidden.md#stage-50))* → [guild03_deadpatrol1_was_first](#d-guild03_deadpatrol1_was_first)
    - branch 2 → [guild03_deadpatrol1_was_second](#d-guild03_deadpatrol1_was_second)

    <span id="d-guild03_deadpatrol1_was_first"></span>**`guild03_deadpatrol1_was_first`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 25 of [The ruthless Crackshot](../quests/Thieves03.md#stage-25)

    - branch 1 → [guild03_deadpatrol_1_1](#d-guild03_deadpatrol_1_1)

    <span id="d-guild03_deadpatrol1_was_second"></span>**`guild03_deadpatrol1_was_second`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 28 of [The ruthless Crackshot](../quests/Thieves03.md#stage-28)

    - branch 1 → [guild03_deadpatrol_1_1](#d-guild03_deadpatrol_1_1)

    <span id="d-guild03_deadpatrol_1_1"></span>**`guild03_deadpatrol_1_1`** Dying patrol: “(You see, horrified, how this man is bleeding out rapidly. He has countless cuts and his face is mutilated. You can almost hear his gasps.)” — **effects:** removes monsters from crackshot_hideout2, sets stage 40 of [Thieves story flags (hidden flag)](../quests/thieves_hidden.md#stage-40)

    - “Shadow, embrace him.” → *NPC leaves*
    - “For the glory of Feygard, you will be avenged!” → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `g03_deadpatrol_1` |
    | Spawn group | `g03_deadpatrol_1` |
    | Loot table | – |
    | Conversation | `guild03_deadpatrol1_select` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_omicronrg9.json` |

    Raw data:

    ```json
    {
     "id": "g03_deadpatrol_1",
     "name": "Dying patrol",
     "iconID": "monsters_rltiles3:14",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "g03_deadpatrol_1",
     "phraseID": "guild03_deadpatrol1_select"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_deadpatrol_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_deadpatrol_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_deadpatrol_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_deadpatrol_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
