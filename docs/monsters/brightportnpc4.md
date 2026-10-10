---
description: "Franz is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_ld1_34.png){ .sprite } Franz

**Where to find Franz:** Brightport: [Brightport school 12](../maps/brightport_school12.md#pin-npc-brightportnpc4)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_34.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Brightport |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Quests

- [No rest for the wicked](../quests/Stanwickquest.md): stage 45
- [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md): stages 42, 45

## Dialogue simulator

Set your quest stages and items, then talk to Franz. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_franz_selector.json" data-npc="Franz" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_franz_selector"></span>**`brightport_franz_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT 6 rounds passed since timer “franz_note_read_timer”; NOT latest stage of [No rest for the wicked](../quests/Stanwickquest.md#stage-45) is 45; reached stage 45 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-45))* → [brightport_franz3](#d-brightport_franz3)
    - Next *(if reached stage 45 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-45); 6 rounds passed since timer “franz_note_read_timer”; NOT reached stage 45 of [No rest for the wicked](../quests/Stanwickquest.md#stage-45))* → [brightport_franz](#d-brightport_franz)
    - Next → [brightport_franz1](#d-brightport_franz1)

    <span id="d-brightport_franz3"></span>**`brightport_franz3`** Franz: “I haven't read your question yet. Come back later.”


    <span id="d-brightport_franz"></span>**`brightport_franz`** Franz: “I've read your question, but I must say, your handwriting could use some improvement.”

    - “Hey, if you'd slain dragons like me, you wouldn't have time to practice either.” → [brightport_franz4](#d-brightport_franz4)
    - “Tsk, skip to the answer please.” → [brightport_franz4](#d-brightport_franz4)

    <span id="d-brightport_franz1"></span>**`brightport_franz1`** [Franz](../monsters/brightportnpc4.md): “I am currently busy grading today's assignment papers. If you have any questions, please write them down and bring them to me.”

    - “[Give written note]” *(if hand over 1× [Written note](../items/brightport_note.md))* → [brightport_franz2](#d-brightport_franz2)
    - “Could you tell me what you know about the library theft?” *(if NOT reached stage 45 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-45); reached stage 25 of [No rest for the wicked](../quests/Stanwickquest.md#stage-25))* → [brightport_franz6](#d-brightport_franz6)
    - “Never mind, that's too much hassle.” → *conversation ends*

    <span id="d-brightport_franz4"></span>**`brightport_franz4`** Franz: “There is not much I can tell you about the incident. None of us teachers knew anything about the scroll or where it was kept. In such a case, one might presume that the most logical step would be to investigate the room where it was stored.” — **effects:** sets stage 45 of [No rest for the wicked](../quests/Stanwickquest.md#stage-45)

    - Next → [brightport_franz5](#d-brightport_franz5)

    <span id="d-brightport_franz2"></span>**`brightport_franz2`** Franz: “I'll read it next after I'm done with this other paper. Please come back later.” — **effects:** sets stage 45 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-45), starts timer “franz_note_read_timer”


    <span id="d-brightport_franz6"></span>**`brightport_franz6`** Franz: “As I've said, I'm busy. Write your question down and I'll answer you later.” — **effects:** sets stage 42 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-42)

    - “[Guess I'll find some paper and ink.]” → *conversation ends*

    <span id="d-brightport_franz5"></span>**`brightport_franz5`** Franz: “However, the library was locked, so one would need to ask the Headmaster for permission.”

    - “Thanks, I will do that.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 8 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightportnpc4` |
    | Type (wiki) | NPC |
    | Spawn group | `brightportnpc4` |
    | Loot table | – |
    | Conversation | `brightport_franz_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:34` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportnpc4",
     "name": "Franz",
     "iconID": "monsters_ld1:34",
     "phraseID": "brightport_franz_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
