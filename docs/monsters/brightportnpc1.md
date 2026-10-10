---
description: "Milena is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_karvis2_6.png){ .sprite } Milena

**Where to find Milena:** Brightport: [Brightport school 3](../maps/brightport_school3.md#pin-npc-brightportnpc1)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_karvis2_6.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Brightport |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Quests

- [No rest for the wicked](../quests/Stanwickquest.md): stage 30

## Dialogue simulator

Set your quest stages and items, then talk to Milena. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_milena.json" data-npc="Milena" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_milena"></span>**`brightport_milena`** Milena: “Ah, this deer soup smells just heavenly.”

    - “Could you sell me some traveling supplies?” → [brightport_milena1](#d-brightport_milena1)
    - “Could you tell me what you know about the library theft?” *(if reached stage 25 of [No rest for the wicked](../quests/Stanwickquest.md#stage-25); NOT reached stage 96 of [No rest for the wicked](../quests/Stanwickquest.md#stage-96))* → [brightport_milena2](#d-brightport_milena2)
    - “Soup from those creepy deer? Yuck.” → *conversation ends*

    <span id="d-brightport_milena1"></span>**`brightport_milena1`** Milena: “No sorry, the dining room is for students only.”

    - Next → [brightport_milena](#d-brightport_milena)

    <span id="d-brightport_milena2"></span>**`brightport_milena2`** Milena: “I don't know much about it to be honest. I'm just the cook. But...”

    - Next → [brightport_milena3](#d-brightport_milena3)

    <span id="d-brightport_milena3"></span>**`brightport_milena3`** Milena: “One evening, sometime last year. I was preparing the soup stock for the next day, when I noticed a dark figure heading outside from the direction of the dormitory.” — **effects:** sets stage 30 of [No rest for the wicked](../quests/Stanwickquest.md#stage-30)

    - Next → [brightport_milena4](#d-brightport_milena4)

    <span id="d-brightport_milena4"></span>**`brightport_milena4`** Milena: “I thought it was my sleepy mind playing tricks on me, so I didn't give it much thought. I told the headmaster but it didn't seem to be related to the theft.”

    - “Interesting, thanks.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightportnpc1` |
    | Type (wiki) | NPC |
    | Spawn group | `brightportnpc1` |
    | Loot table | – |
    | Conversation | `brightport_milena` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:6` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportnpc1",
     "name": "Milena",
     "iconID": "monsters_karvis2:6",
     "unique": 1,
     "phraseID": "brightport_milena"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportnpc1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
