---
description: "Durnan the Hollow is a non-player character (NPC) in Andor's Trail, found in Undertell 1 0."
---

# ![](../assets/icons/monsters/monsters_gisons_10.png){ .sprite } Durnan the Hollow

**Where to find Durnan the Hollow:** [Undertell 1 0](../maps/undertell_1_0.md#pin-npc-durnan)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_gisons_10.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Undertell 1 0 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Quests

- [The fifth master](../quests/fifth_master.md): stage 30

## Dialogue simulator

Set your quest stages and items, then talk to Durnan the Hollow. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/undertell_ghost_durnan_10.json" data-npc="Durnan the Hollow" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-undertell_ghost_durnan_10"></span>**`undertell_ghost_durnan_10`** [Dummy NPC](../monsters/none.md): “A ghostly miner leans heavily on a spectral pickaxe, using it as a cane. His faded eyes glimmer faintly in the warm air of the tunnels.”

    - “Who are you?” → [undertell_ghost_durnan_20](#d-undertell_ghost_durnan_20)

    <span id="d-undertell_ghost_durnan_20"></span>**`undertell_ghost_durnan_20`** [Durnan the Hollow](../monsters/durnan.md): “Durnan...once of the Lethgar. This pick carried me through life, now it props up what's left of me.”

    - “Do you remember anyone named Varnel?” *(if reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20); NOT reached stage 40 of [The fifth master](../quests/fifth_master.md#stage-40))* → [undertell_ghost_durnan_30](#d-undertell_ghost_durnan_30)
    - “I have to go now, but it was nice talking to you.” → *conversation ends*

    <span id="d-undertell_ghost_durnan_30"></span>**`undertell_ghost_durnan_30`** Durnan the Hollow: “Varnel...the scribe. He was no miner, yet they made him dig beside us. Always scribbling between swings. Said he wrote words to keep them from the Masters.”

    - “Do you know where he went?” → [undertell_ghost_durnan_40](#d-undertell_ghost_durnan_40)

    <span id="d-undertell_ghost_durnan_40"></span>**`undertell_ghost_durnan_40`** Durnan the Hollow: “East, through the lower caverns. He spoke of a town where the sun still touched the Sutdover River. Said he would hide among its people until the voices of the Masters faded from his dreams.”

    - “Thank you, Durnan.” → [undertell_ghost_durnan_50](#d-undertell_ghost_durnan_50)

    <span id="d-undertell_ghost_durnan_50"></span>**`undertell_ghost_durnan_50`** Durnan the Hollow: “If you find what he carried...bury it deep, far from here. The chains broke too late for us. Now...let me rest.” — **effects:** sets stage 30 of [The fifth master](../quests/fifth_master.md#stage-30)




## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `durnan` |
    | Type (wiki) | NPC |
    | Spawn group | `durnan` |
    | Loot table | – |
    | Conversation | `undertell_ghost_durnan_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:10` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "durnan",
     "name": "Durnan the Hollow",
     "iconID": "monsters_gisons:10",
     "monsterClass": "humanoid",
     "phraseID": "undertell_ghost_durnan_10"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=durnan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=durnan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=durnan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=durnan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
