---
description: "Erethori is a non-player character (NPC) in Andor's Trail, found in Foaming Flask Tavern."
---

# ![](../assets/icons/monsters/monsters_ld1_100.png){ .sprite } Erethori

**Where to find Erethori:** Foaming Flask Tavern: [Waytominingtown 1a](../maps/waytominingtown1a.md#pin-npc-erethori)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_100.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Foaming Flask Tavern |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Destined for great things](../quests/charwood1.md): stage 11

## Dialogue simulator

Set your quest stages and items, then talk to Erethori. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/erethori0.json" data-npc="Erethori" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-erethori0"></span>**`erethori0`** Erethori: “I hope you're not here to ask for help, like all those other people that have come by.”

    - “What people?” → [erethori3](#d-erethori3)
    - “Who are you?” → [erethori1](#d-erethori1)

    <span id="d-erethori3"></span>**`erethori3`** Erethori: “It seems something must have happened up in the Charwood mining town recently.”

    - Next → [erethori4](#d-erethori4)

    <span id="d-erethori1"></span>**`erethori1`** Erethori: “I'm no one. You did not see me, or any of my friends here.”

    - “Sure thing.” → *conversation ends*
    - “You guys seem to be up to something.” → [erethori2](#d-erethori2)

    <span id="d-erethori4"></span>**`erethori4`** Erethori: “There have been quite a few people coming by here and asking us for help.”

    - Next → [erethori5](#d-erethori5)

    <span id="d-erethori2"></span>**`erethori2`** Erethori: “Really? I think you had better leave.”


    <span id="d-erethori5"></span>**`erethori5`** Erethori: “Don't know what happened over there though. Maybe you should go ask the people in the Charwood cabin.”

    - “Charwood, where is that?” → [erethori6](#d-erethori6)

    <span id="d-erethori6"></span>**`erethori6`** Erethori: “It's just north of here. Take the path west of our camp here, and head straight north. It's just around the bend there [points].” — **effects:** sets stage 11 of [Destined for great things](../quests/charwood1.md#stage-11)

    - “Thanks, I'll go check it out.” → *conversation ends*
    - “I have better things to do.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “It's just north of here. Take the path west of our camp here, and hea…” → “It's just north of here. Take the path west of our camp here, and hea…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `erethori` |
    | Type (wiki) | NPC |
    | Spawn group | `erethori` |
    | Loot table | – |
    | Conversation | `erethori0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:100` |
    | Defined in | `res/raw/monsterlist_v070_npcs.json` |

    Raw data:

    ```json
    {
     "id": "erethori",
     "name": "Erethori",
     "iconID": "monsters_ld1:100",
     "phraseID": "erethori0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erethori.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erethori.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erethori.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erethori.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
