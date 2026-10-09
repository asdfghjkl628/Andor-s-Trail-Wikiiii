---
description: "Anavrin is a non-player character (NPC) in Andor's Trail, found in Undertell 5."
---

# ![](../assets/icons/monsters/monsters_liches_3.png){ .sprite } Anavrin

**Where to find Anavrin:** [Undertell 5](../maps/undertell_5.md#pin-npc-anavrin)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_liches_3.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Undertell 5 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Quests

- [The fifth master](../quests/fifth_master.md): stages 85, 90

## Dialogue simulator

Set your quest stages and items, then talk to Anavrin. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/anavrin_initial_selector.json" data-npc="Anavrin" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-anavrin_initial_selector"></span>**`anavrin_initial_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 80 of [The fifth master](../quests/fifth_master.md#stage-80); NOT reached stage 85 of [The fifth master](../quests/fifth_master.md#stage-85))* → [anavrin_resurrection_30](#d-anavrin_resurrection_30)
    - branch 2 *(if NOT reached stage 90 of [The fifth master](../quests/fifth_master.md#stage-90))* → [anavrin_revelation_10](#d-anavrin_revelation_10)
    - branch 3 → [anavrin_after_revival_10](#d-anavrin_after_revival_10)

    <span id="d-anavrin_resurrection_30"></span>**`anavrin_resurrection_30`** [Anavrin](../monsters/anavrin.md): “You have undone silence itself, mortal. The rift shall open again, and through it we will see our dominion restored.” — **effects:** sets stage 85 of [The fifth master](../quests/fifth_master.md#stage-85)

    - “[Try to comprehend the revelation.]” → *conversation ends*

    <span id="d-anavrin_revelation_10"></span>**`anavrin_revelation_10`** Anavrin: “You have done as we asked. The ritual of Five Aspects is complete...and with it, truth returns to the world.”

    - “Truth? What do you mean?” → [anavrin_revelation_20](#d-anavrin_revelation_20)

    <span id="d-anavrin_after_revival_10"></span>**`anavrin_after_revival_10`** Anavrin: “Do you hear it now? The world hums with the memory of its first breath. Silence was never the absence of sound...it was waiting.”


    <span id="d-anavrin_revelation_20"></span>**`anavrin_revelation_20`** Anavrin: “The Shadow that your kind worship is not what you believe. It is no benevolent guardian, no path to balance. It is the echo of our masters...the Kazaul.”

    - “That cannot be true. The Shadow guides and protects.” → [anavrin_revelation_30](#d-anavrin_revelation_30)

    <span id="d-anavrin_revelation_30"></span>**`anavrin_revelation_30`** Anavrin: “Believe what soothes you. Denial is the comfort of the living. But when you walk in its darkness again, listen...and you will hear our voices in its breath.”

    - “You lie. The Shadow is not Kazaul.” → [anavrin_revelation_40](#d-anavrin_revelation_40)

    <span id="d-anavrin_revelation_40"></span>**`anavrin_revelation_40`** Anavrin: “Perhaps. Or perhaps you already know the truth, but your heart fears its shape. Leave now, child of dust. The Fifth is awake, and the world will not remain silent much longer.” — **effects:** sets stage 90 of [The fifth master](../quests/fifth_master.md#stage-90)




## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `anavrin` |
    | Type (wiki) | NPC |
    | Spawn group | `anavrin` |
    | Loot table | – |
    | Conversation | `anavrin_initial_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_liches:3` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "anavrin",
     "name": "Anavrin",
     "iconID": "monsters_liches:3",
     "unique": 1,
     "monsterClass": "undead",
     "phraseID": "anavrin_initial_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anavrin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anavrin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anavrin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=anavrin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
