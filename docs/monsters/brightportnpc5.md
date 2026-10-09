---
description: "Frederich is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_ld1_125.png){ .sprite } Frederich

**Where to find Frederich:** Brightport: [Brightport school 10](../maps/brightport_school10.md#pin-npc-brightportnpc5)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_125.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brightport |
| **Entry ID** | `brightportnpc5` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Quests

- [No rest for the wicked](../quests/Stanwickquest.md): stage 40

## Dialogue simulator

Set your quest stages and items, then talk to Frederich. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_frederich_selector.json" data-npc="Frederich" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_frederich_selector"></span>**`brightport_frederich_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 224 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-224))* → [brightport_frederich_afterlecture](#d-brightport_frederich_afterlecture)
    - Next *(if reached stage 225 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-225); NOT reached stage 224 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-224))* → [brightport_frederich_lecture](#d-brightport_frederich_lecture)
    - Next *(if NOT reached stage 225 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-225))* → [brightport_frederich_beforelecture](#d-brightport_frederich_beforelecture)

    <span id="d-brightport_frederich_afterlecture"></span>**`brightport_frederich_afterlecture`** Frederich: “The one student whose name I don't remember. The one that didn't bolt out of the door. What is it?”

    - “Could you tell me what you know about the library theft?” *(if reached stage 25 of [No rest for the wicked](../quests/Stanwickquest.md#stage-25); NOT reached stage 96 of [No rest for the wicked](../quests/Stanwickquest.md#stage-96))* → [brightport_frederich](#d-brightport_frederich)
    - “Nothing, bye.” → *conversation ends*

    <span id="d-brightport_frederich_lecture"></span>**`brightport_frederich_lecture`** Frederich: “Back to your seat, student! I will not have anyone interrupting my history lecture.”


    <span id="d-brightport_frederich_beforelecture"></span>**`brightport_frederich_beforelecture`** Frederich: “Class is about to begin, please sit down. I will accept questions after the lecture is over.”


    <span id="d-brightport_frederich"></span>**`brightport_frederich`** Frederich: “What is there to know, the case is solved!”

    - “Why do you think that?” → [brightport_frederich1](#d-brightport_frederich1)

    <span id="d-brightport_frederich1"></span>**`brightport_frederich1`** Frederich: “I always knew that boy Stanwick was up to no good. They made a poor choice entrusting the library to someone associated with those Nor City savages. It's obvious he was tasked to steal the scroll for them.” — **effects:** sets stage 40 of [No rest for the wicked](../quests/Stanwickquest.md#stage-40)

    - Next → [brightport_frederich2](#d-brightport_frederich2)

    <span id="d-brightport_frederich2"></span>**`brightport_frederich2`** Frederich: “It's only a matter of time before he spits out the names of his accomplices.”




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightportnpc5` |
    | Spawn group | `brightportnpc5` |
    | Loot table | – |
    | Conversation | `brightport_frederich_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:125` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportnpc5",
     "name": "Frederich",
     "iconID": "monsters_ld1:125",
     "maxHP": 120,
     "phraseID": "brightport_frederich_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
