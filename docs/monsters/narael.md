---
description: "Narael is a non-player character (NPC) in Andor's Trail, found in Flagstone 4."
---

# ![](../assets/icons/monsters/monsters_man1_0.png){ .sprite } Narael

**Where to find Narael:** [Flagstone 4](../maps/flagstone4.md#pin-npc-narael)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_man1_0.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Flagstone 4 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Ancient secrets](../quests/flagstone.md): stage 60

## Dialogue simulator

Talk to Narael as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/narael.json" data-npc="Narael" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (11 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-narael"></span>**`narael`** Narael: “Thank you, thank you for freeing me from that monster.”

    - Next → [narael_select](#d-narael_select)

    <span id="d-narael_select"></span>**`narael_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [Ancient secrets](../quests/flagstone.md#stage-60))* → [narael_9](#d-narael_9)
    - branch 2 → [narael_1](#d-narael_1)

    <span id="d-narael_9"></span>**`narael_9`** Narael: “If you find my wife Taurum in Nor City, please tell her I'm alive and that I haven't forgotten about her.”

    - “I will. Goodbye.” → *conversation ends*
    - “I will. Shadow be with you.” → *conversation ends*

    <span id="d-narael_1"></span>**`narael_1`** Narael: “I have been a captive here for what seems to be an eternity.”

    - Next → [narael_2](#d-narael_2)

    <span id="d-narael_2"></span>**`narael_2`** Narael: “Oh, the things they did to me. Thank you so much for freeing me.”

    - Next → [narael_3](#d-narael_3)

    <span id="d-narael_3"></span>**`narael_3`** Narael: “I was once a citizen in Nor City, during which time some men wanted to open the mines under Mt Galmore again, and like the fool that I am I signed up for the promise of riches.”

    - Next → [narael_4](#d-narael_4)

    <span id="d-narael_4"></span>**`narael_4`** Narael: “After a while, the day came when I wanted to quit the assignment and return to my wife.”

    - Next → [narael_5](#d-narael_5)

    <span id="d-narael_5"></span>**`narael_5`** Narael: “The officer in charge would not let me, and out of malice he threw me in a cell here in the old prison of Flagstone for disobeying his orders.”

    - Next → [narael_6](#d-narael_6)

    <span id="d-narael_6"></span>**`narael_6`** Narael: “If only I could see my wife once more. I have hardly any life left in me, and I don't even have enough strength to leave this place.”

    - Next → [narael_7](#d-narael_7)

    <span id="d-narael_7"></span>**`narael_7`** Narael: “I guess my fate is to perish here, but now as a free man at least.”

    - Next → [narael_8](#d-narael_8)

    <span id="d-narael_8"></span>**`narael_8`** Narael: “Now leave me to my fate. I do not have the strength to leave this place.” — **effects:** sets stage 60 of [Ancient secrets](../quests/flagstone.md#stage-60)

    - Next → [narael_9](#d-narael_9)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 2 lines changed<br>· text: “The officer in charge would not let me, and I was sent to Flagstone a…” → “The officer in charge would not let me, and out of malice he threw me…”<br>· text: “I was once a citizen in Nor City, and worked on the excavation of Mou…” → “I was once a citizen in Nor City, during which time some men wanted t…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `narael` |
    | Type (wiki) | NPC |
    | Spawn group | `narael` |
    | Loot table | – |
    | Conversation | `narael` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_wilderness.json` |

    Raw data:

    ```json
    {
     "id": "narael",
     "name": "Narael",
     "iconID": "monsters_man1:0",
     "monsterClass": "humanoid",
     "spawnGroup": "narael",
     "phraseID": "narael"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=narael.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=narael.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=narael.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=narael.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
