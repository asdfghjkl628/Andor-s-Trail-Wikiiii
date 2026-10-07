---
description: "Taret is a non-player character (NPC) in Andor's Trail, found in Loneford."
---

# ![](../assets/icons/monsters/monsters_ld1_132.png){ .sprite } Taret

**Where to find Taret:** Loneford: [Loneford 17](../maps/loneford17.md#pin-npc-taret)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_132.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Loneford |
| **Entry ID** | `taret` |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Quests

- [General story flags 2 (hidden flag)](../quests/nondisplay_2.md): stages 60, 75

## Dialogue simulator

Set your quest stages and items, then talk to Taret. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/taret_0.json" data-npc="Taret" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-taret_0"></span>**`taret_0`** Taret: “Hello kid. What can I do for you?”

    - “I'm looking for my brother, Andor. He looks a bit like me. Have you seen him?” → [taret_1](#d-taret_1)
    - “Can you tell me anything about the local area?” → [taret_2](#d-taret_2)

    <span id="d-taret_1"></span>**`taret_1`** Taret: “Sorry. I don't recall seeing anyone like that.”

    - “OK. Thanks for your time.” → *conversation ends*
    - “Can you tell me anything about the local area?” → [taret_2](#d-taret_2)

    <span id="d-taret_2"></span>**`taret_2`** Taret: “There's not much to tell. Loneford is mostly a quiet place, although I have heard rumors that there is some criminal organization based here. Personally, I don't believe it.”

    - Next → [taret_3](#d-taret_3)

    <span id="d-taret_3"></span>**`taret_3`** Taret: “The nastiest person in town is probably my neighbor. *laughs*. Be careful about walking in on her!” — **effects:** sets stage 60 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-60)

    - “I appreciate the warning, but unfortunately it's too late. I already met her.” *(if reached stage 50 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-50); NOT reached stage 70 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-70))* → [taret_4](#d-taret_4)
    - “Thanks for the warning.” → [taret_4](#d-taret_4)
    - “You are right. I told her you warned me that she was not always nice to strangers, but I think that just annoyed her.” *(if reached stage 70 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-70); NOT reached stage 75 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-75))* → [taret_5](#d-taret_5)

    <span id="d-taret_4"></span>**`taret_4`** Taret: “Is there anything else I can help you with?”

    - “I'm looking for my brother, Andor. He looks a bit like me. Have you seen him?” → [taret_1](#d-taret_1)

    <span id="d-taret_5"></span>**`taret_5`** Taret: “Thanks kid. *sigh*. I expect she will be around here later to complain about that. You should be more careful what you say to people.” — **effects:** sets stage 75 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-75)

    - “Sorry. You are right.” → [taret_4](#d-taret_4)



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `taret` |
    | Spawn group | `taret` |
    | Loot table | – |
    | Conversation | `taret_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:132` |
    | Defined in | `res/raw/monsterlist_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "taret",
     "name": "Taret",
     "iconID": "monsters_ld1:132",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "taret",
     "phraseID": "taret_0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=taret.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=taret.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=taret.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=taret.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
