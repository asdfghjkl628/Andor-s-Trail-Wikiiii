---
description: "Norath is a non-player character (NPC) in Andor's Trail, found in Remgard."
---

# ![](../assets/icons/monsters/monsters_ld1_8.png){ .sprite } Norath

**Where to find Norath:** Remgard: [Remgard farmer 3](../maps/remgard_farmer3.md#pin-npc-norath)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_8.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Remgard |
| **Entry ID** | `norath` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Everything in order](../quests/remgard.md): stages 61, 70

## Dialogue simulator

Set your quest stages and items, then talk to Norath. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/norath.json" data-npc="Norath" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (16 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-norath"></span>**`norath`** *(silent check: the first matching branch below is taken)*

    - branch 1 → [norath_1](#d-norath_1)

    <span id="d-norath_1"></span>**`norath_1`** Norath: “Hello there. Can I help you?”

    - “I was sent by Jhaeld to ask about your missing wife.” *(if reached stage 51 of [Everything in order](../quests/remgard.md#stage-51))* → [norath_jhaeld1](#d-norath_jhaeld1)
    - “Do you have anything to trade?” → [norath_2](#d-norath_2)
    - “What do you do around here?” → [norath_3](#d-norath_3)

    <span id="d-norath_jhaeld1"></span>**`norath_jhaeld1`** Norath: “What do you want me to say? She is missing.”

    - “Is there anything else you have found out that you didn't tell the guards earlier?” → [norath_jhaeld2](#d-norath_jhaeld2)

    <span id="d-norath_2"></span>**`norath_2`** Norath: “Me? No, I don't have anything to sell you. Does this look like a shop to you?”

    - “I was sent by Jhaeld to ask about your missing wife.” *(if reached stage 51 of [Everything in order](../quests/remgard.md#stage-51))* → [norath_jhaeld1](#d-norath_jhaeld1)
    - “What do you do around here?” → [norath_3](#d-norath_3)

    <span id="d-norath_3"></span>**`norath_3`** Norath: “Well, usually I tend to the crops that we grow here. Now, I can't find the strength to do that though.”

    - “Why, what's wrong?” → [norath_4](#d-norath_4)

    <span id="d-norath_jhaeld2"></span>**`norath_jhaeld2`** Norath: “No. I told those guards the whole story. If I were to find out more, I would immediately tell them of course.”

    - Next → [norath_jhaeld3](#d-norath_jhaeld3)

    <span id="d-norath_4"></span>**`norath_4`** Norath: “My wife, Bethir. She is gone, and no one seems to know where she is.”

    - Next → [norath_5](#d-norath_5)

    <span id="d-norath_jhaeld3"></span>**`norath_jhaeld3`** Norath: “We did have a minor argument just the night before she went missing. But it was just a minor thing, nothing serious.”

    - Next → [norath_jhaeld_s_1](#d-norath_jhaeld_s_1)

    <span id="d-norath_5"></span>**`norath_5`** Norath: “I even went so far as to ask the guards to look for her, but she is nowhere to be found.”

    - “Are you sure she isn't just out of town running some errands?” → [norath_6](#d-norath_6)
    - “Where do you think she has gone?” → [norath_7](#d-norath_7)
    - “I was sent by Jhaeld to ask you about her.” *(if reached stage 51 of [Everything in order](../quests/remgard.md#stage-51))* → [norath_jhaeld1](#d-norath_jhaeld1)

    <span id="d-norath_jhaeld_s_1"></span>**`norath_jhaeld_s_1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 61 of [Everything in order](../quests/remgard.md#stage-61)

    - branch 1 *(if reached stage 62 of [Everything in order](../quests/remgard.md#stage-62))* → [norath_jhaeld_s_2](#d-norath_jhaeld_s_2)
    - branch 2 → [norath_jhaeld4](#d-norath_jhaeld4)

    <span id="d-norath_6"></span>**`norath_6`** Norath: “If that were the case, I would have hoped she would have told me first. No, I can feel it - I am sure something bad has happened to her.”

    - “Where do you think she has gone?” → [norath_7](#d-norath_7)
    - “I was sent by Jhaeld to ask you about her.” *(if reached stage 51 of [Everything in order](../quests/remgard.md#stage-51))* → [norath_jhaeld1](#d-norath_jhaeld1)

    <span id="d-norath_7"></span>**`norath_7`** Norath: “To be quite honest, I have no idea.”

    - “Are you sure she isn't just out of town running some errands?” → [norath_6](#d-norath_6)
    - “I was sent by Jhaeld to ask you about her.” *(if reached stage 51 of [Everything in order](../quests/remgard.md#stage-51))* → [norath_jhaeld1](#d-norath_jhaeld1)

    <span id="d-norath_jhaeld_s_2"></span>**`norath_jhaeld_s_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 63 of [Everything in order](../quests/remgard.md#stage-63))* → [norath_jhaeld_s_3](#d-norath_jhaeld_s_3)
    - branch 2 → [norath_jhaeld4](#d-norath_jhaeld4)

    <span id="d-norath_jhaeld4"></span>**`norath_jhaeld4`** Norath: “Now, if you'll excuse me, I have things to tend to.”


    <span id="d-norath_jhaeld_s_3"></span>**`norath_jhaeld_s_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 64 of [Everything in order](../quests/remgard.md#stage-64))* → [norath_jhaeld_s_4](#d-norath_jhaeld_s_4)
    - branch 2 → [norath_jhaeld4](#d-norath_jhaeld4)

    <span id="d-norath_jhaeld_s_4"></span>**`norath_jhaeld_s_4`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 70 of [Everything in order](../quests/remgard.md#stage-70)

    - branch 1 → [norath_jhaeld4](#d-norath_jhaeld4)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 8 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `norath` |
    | Spawn group | `norath` |
    | Loot table | – |
    | Conversation | `norath` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:8` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "norath",
     "name": "Norath",
     "iconID": "monsters_ld1:8",
     "monsterClass": "humanoid",
     "spawnGroup": "norath",
     "phraseID": "norath"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=norath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=norath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=norath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=norath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
