---
description: "Gaela is a non-player character (NPC) in Andor's Trail."
---

# ![](../assets/icons/monsters/monsters_men2_9.png){ .sprite } Gaela

**Where to find Gaela:** appears during a quest or scripted event.

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men2_9.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Search for Andor](../quests/andor.md): stage 40

## Dialogue simulator

Set your quest stages and items, then talk to Gaela. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/gaela.json" data-npc="Gaela" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-gaela"></span>**`gaela`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 40 of [Search for Andor](../quests/andor.md#stage-40))* → [gaela_r](#d-gaela_r)
    - branch 2 → [gaela_0](#d-gaela_0)

    <span id="d-gaela_r"></span>**`gaela_r`** Gaela: “Hello again. I hope you will find what you are looking for.”


    <span id="d-gaela_0"></span>**`gaela_0`** Gaela: “Swift is my blade. Poisoned is my tongue. Or was it the other way around?”

    - “There seems to be a lot of thieves here in Fallhaven.” → [gaela_1](#d-gaela_1)

    <span id="d-gaela_1"></span>**`gaela_1`** Gaela: “Yes, we thieves have a strong presence here.”

    - “Anything more?” *(if reached stage 30 of [Search for Andor](../quests/andor.md#stage-30))* → [gaela_2](#d-gaela_2)

    <span id="d-gaela_2"></span>**`gaela_2`** Gaela: “I heard that you helped Gruil, a fellow thief in Crossglen village.”

    - Next → [gaela_3](#d-gaela_3)

    <span id="d-gaela_3"></span>**`gaela_3`** Gaela: “Word has also reached me that you are looking for someone. I might be able to help you.”

    - Next → [gaela_4](#d-gaela_4)

    <span id="d-gaela_4"></span>**`gaela_4`** Gaela: “You should go talk to Bucus in the derelict house a bit southwest of here. Tell him you want to know more about the Thieves' Guild.” — **effects:** sets stage 40 of [Search for Andor](../quests/andor.md#stage-40)

    - “Thanks, I'll go talk to him.” → [gaela_5](#d-gaela_5)

    <span id="d-gaela_5"></span>**`gaela_5`** Gaela: “Consider it a favor done in return for helping Gruil.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `gaela` |
    | Type (wiki) | NPC |
    | Spawn group | `gaela` |
    | Loot table | – |
    | Conversation | `gaela` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:9` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "gaela",
     "name": "Gaela",
     "iconID": "monsters_men2:9",
     "monsterClass": "humanoid",
     "spawnGroup": "gaela",
     "phraseID": "gaela"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gaela.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gaela.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gaela.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gaela.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
