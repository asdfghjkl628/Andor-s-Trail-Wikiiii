---
description: "Rigmor is a non-player character (NPC) in Andor's Trail."
---

# ![](../assets/icons/monsters/monsters_men_1.png){ .sprite } Rigmor

**Where to find Rigmor:** not placed on any map; appears through a quest or scripted event.

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Entry ID** | `rigmor` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [It's knot funny](../quests/fallhaven_lytwings.md): stage 10

## Dialogue simulator

Set your quest stages and items, then talk to Rigmor. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/rigmor.json" data-npc="Rigmor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (10 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-rigmor"></span>**`rigmor`** Rigmor: “Well hello there! Aren't you a cute little fellow.”

    - “Have you seen my brother Andor?” → [rigmor_1](#d-rigmor_1)
    - “Can you tell me about the lytwings?” *(if latest stage of [It's knot funny](../quests/fallhaven_lytwings.md#stage-1) is 1)* → [rigmor_lytwing_1](#d-rigmor_lytwing_1)
    - “I really need to go.” → [rigmor_leave_select](#d-rigmor_leave_select)

    <span id="d-rigmor_1"></span>**`rigmor_1`** Rigmor: “Your brother, you say? His name is Andor? No. I don't recall meeting anyone like that.”

    - “I really need to go.” → [rigmor_leave_select](#d-rigmor_leave_select)

    <span id="d-rigmor_lytwing_1"></span>**`rigmor_lytwing_1`** Rigmor: “I take it you spoke to Arensia?”

    - Next → [rigmor_lytwing_6](#d-rigmor_lytwing_6)

    <span id="d-rigmor_leave_select"></span>**`rigmor_leave_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Calomyran secrets](../quests/calomyran.md#stage-100))* → [rigmor_thanks](#d-rigmor_thanks)
    - branch 2 → *conversation ends*

    <span id="d-rigmor_lytwing_6"></span>**`rigmor_lytwing_6`** Rigmor: “The poor girl. She looks exhausted, and her hair is absolutely tousled. Will those lytwings never leave her alone?”

    - Next → [rigmor_lytwing_2](#d-rigmor_lytwing_2)

    <span id="d-rigmor_thanks"></span>**`rigmor_thanks`** Rigmor: “I heard you helped my old man find his book, thank you. He had been talking about that book for weeks. Poor thing, he tends to forget things.”

    - “It was my pleasure. Goodbye.” → *conversation ends*
    - “You should keep an eye on him, or bad things might happen to him.” → *conversation ends*
    - “Whatever, I just did it for the gold.” → *conversation ends*

    <span id="d-rigmor_lytwing_2"></span>**`rigmor_lytwing_2`** Rigmor: “What do you want to know?”

    - “What do you know about lytwings?” → [rigmor_lytwing_3](#d-rigmor_lytwing_3)
    - “Where can I find lytwings?” → [rigmor_lytwing_5](#d-rigmor_lytwing_5)
    - “Thank you. I really need to go now.” → [rigmor_leave_select](#d-rigmor_leave_select)

    <span id="d-rigmor_lytwing_3"></span>**`rigmor_lytwing_3`** Rigmor: “Lytwings are small magical beings that are also known as the guardians of the forest, and they are known to take revenge on us when we intrude on them, or on nature.”

    - Next → [rigmor_lytwing_4](#d-rigmor_lytwing_4)

    <span id="d-rigmor_lytwing_5"></span>**`rigmor_lytwing_5`** Rigmor: “Lytwings gather near fairy rings. I suggest that you look for large mushroom patches in the woodland surrounding Fallhaven.” — **effects:** sets stage 10 of [It's knot funny](../quests/fallhaven_lytwings.md#stage-10)

    - Next → [rigmor_lytwing_2](#d-rigmor_lytwing_2)

    <span id="d-rigmor_lytwing_4"></span>**`rigmor_lytwing_4`** Rigmor: “They are also very mischievous, and love causing trouble. They probably eat too many fermented berries, if you ask me.”

    - Next → [rigmor_lytwing_2](#d-rigmor_lytwing_2)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 6 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `rigmor` |
    | Spawn group | `rigmor` |
    | Loot table | – |
    | Conversation | `rigmor` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:1` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "rigmor",
     "name": "Rigmor",
     "iconID": "monsters_men:1",
     "monsterClass": "humanoid",
     "spawnGroup": "rigmor",
     "phraseID": "rigmor"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rigmor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rigmor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rigmor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rigmor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
