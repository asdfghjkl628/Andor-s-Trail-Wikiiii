---
description: "Richimor is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_ld1_96.png){ .sprite } Richimor

**Where to find Richimor:** Brightport: [brightport1](../maps/brightport1.md#pin-npc-brightportnpc2)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_96.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brightport |
| **Entry ID** | `brightportnpc2` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Quests

- [No rest for the wicked](../quests/Stanwickquest.md): stage 60
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 86, 248

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Richimor. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brightpor_richimor_selector.json" data-npc="Richimor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (11 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightpor_richimor_selector"></span>**`brightpor_richimor_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 86 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-86))* → [brightport_richimor3](#d-brightport_richimor3)
    - Next → [brightport_richimor](#d-brightport_richimor)

    <span id="d-brightport_richimor3"></span>**`brightport_richimor3`** Richimor: “Ho, ho, what resplendent blue waves.”

    - “Can you please tell me that story again?” → [brightport_richimor4](#d-brightport_richimor4)
    - “You must have been living here for a long time, right?” *(if reached stage 55 of [No rest for the wicked](../quests/Stanwickquest.md#stage-55); NOT reached stage 60 of [No rest for the wicked](../quests/Stanwickquest.md#stage-60))* → [brightport_richimor5](#d-brightport_richimor5)

    <span id="d-brightport_richimor"></span>**`brightport_richimor`** Richimor: “Hello, young fellow. Want to hear a story?”

    - “Sure. Old fellow.” → [brightport_richimor0](#d-brightport_richimor0)
    - “You must have been living here for a long time, right?” *(if reached stage 55 of [No rest for the wicked](../quests/Stanwickquest.md#stage-55); NOT reached stage 60 of [No rest for the wicked](../quests/Stanwickquest.md#stage-60))* → [brightport_richimor5](#d-brightport_richimor5)

    <span id="d-brightport_richimor4"></span>**`brightport_richimor4`** Richimor: “It would be my joy, young fellow.”

    - Next → [brightport_richimor0](#d-brightport_richimor0)

    <span id="d-brightport_richimor5"></span>**`brightport_richimor5`** Richimor: “Yes, I have seen Brightport change. I've lived through its tumultuous times. Why do you ask, young fellow?”

    - “I'm looking for a person who lived here a long time ago named Bryma. Have you heard of them?” → [brightport_richimor6](#d-brightport_richimor6)

    <span id="d-brightport_richimor0"></span>**`brightport_richimor0`** Richimor: “Do you know why the houses in Brightport that are closest to the shore of the lake, have foundations made of stone?”

    - “I don't know, why?” → [brightport_richimor1](#d-brightport_richimor1)

    <span id="d-brightport_richimor6"></span>**`brightport_richimor6`** Richimor: “That's a name I haven't heard in more than 20 years!”

    - Next → [brightport_richimor7](#d-brightport_richimor7)

    <span id="d-brightport_richimor1"></span>**`brightport_richimor1`** Richimor: “During the normal time of the year, the water that flows through Brimhaven does so uninterrupted. But when the rainy season starts, the flow becomes a monstrous maelstrom, overflowing onto the plains and into the lake.”

    - Next → [brightport_richimor2](#d-brightport_richimor2)

    <span id="d-brightport_richimor7"></span>**`brightport_richimor7`** Richimor: “She was my student, and like many young bakers, she aspired to make a name for herself and became a researcher. But one day, she decided to leave Brightport, and I have not heard from her since.”

    - “She might be my only clue to solve a problem. Is there really nothing you can tell me about her whereabouts?” → [brightport_richimor8](#d-brightport_richimor8)

    <span id="d-brightport_richimor2"></span>**`brightport_richimor2`** Richimor: “That, and the confluence of other rivers to the east, which drain into the lake, causes the water level to rise and flood the grasslands surrounding the lake. It reaches up until the foundation of the houses but never rises more than the…” — **effects:** sets stage 86 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-86)

    - “Wow, that's fascinating!” → *conversation ends*

    <span id="d-brightport_richimor8"></span>**`brightport_richimor8`** Richimor: “Hmm, it sounds like you've found yourself in some kind of argument. If it helps, she left a lot of her writings and research at my house for safekeeping. You can read through them. I hope it proves helpful.” — **effects:** sets stage 60 of [No rest for the wicked](../quests/Stanwickquest.md#stage-60), sets stage 248 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-248)




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 11 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightportnpc2` |
    | Spawn group | `brightportnpc2` |
    | Loot table | – |
    | Conversation | `brightpor_richimor_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:96` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportnpc2",
     "name": "Richimor",
     "iconID": "monsters_ld1:96",
     "phraseID": "brightpor_richimor_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
