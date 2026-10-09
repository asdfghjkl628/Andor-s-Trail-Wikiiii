---
description: "Green marble is a non-player character (NPC) in Andor's Trail, found in Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_guynmart_8.png){ .sprite } Green marble

**Where to find Green marble:** Guynmart Castle: [Guynmart wood 10](../maps/guynmart_wood_10.md#pin-npc-guynmart_marble1)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_guynmart_8.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Guynmart Castle |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Quests

- [Marble hunting](../quests/guynmart_marbles.md): stages 21, 30

## Dialogue simulator

Set your quest stages and items, then talk to Green marble. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_marble1_10.json" data-npc="Green marble" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_marble1_10"></span>**`guynmart_marble1_10`** Green marble: “I found a green marble!” — **effects:** sets stage 21 of [Marble hunting](../quests/guynmart_marbles.md#stage-21), gives 1× [Stuephant's marble](../items/guynmart_marble.md), removes monsters from guynmart_wood_10

    - Next → [guynmart_marbles_10](#d-guynmart_marbles_10)

    <span id="d-guynmart_marbles_10"></span>**`guynmart_marbles_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 21 of [Marble hunting](../quests/guynmart_marbles.md#stage-21); reached stage 22 of [Marble hunting](../quests/guynmart_marbles.md#stage-22); reached stage 23 of [Marble hunting](../quests/guynmart_marbles.md#stage-23); reached stage 24 of [Marble hunting](../quests/guynmart_marbles.md#stage-24); reached stage 25 of [Marble hunting](../quests/guynmart_marbles.md#stage-25))* → [guynmart_marbles_20](#d-guynmart_marbles_20)
    - branch 2 → *NPC leaves*

    <span id="d-guynmart_marbles_20"></span>**`guynmart_marbles_20`** Green marble: “That was the last one. I have found them all. Stuephant will be happy.” — **effects:** sets stage 30 of [Marble hunting](../quests/guynmart_marbles.md#stage-30)

    - “I will go back to him now.” → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `guynmart_marble1` |
    | Type (wiki) | NPC |
    | Spawn group | `guynmart_marble1` |
    | Loot table | – |
    | Conversation | `guynmart_marble1_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_guynmart:8` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_marble1",
     "name": "Green marble",
     "iconID": "monsters_guynmart:8",
     "moveCost": 500,
     "unique": 1,
     "phraseID": "guynmart_marble1_10"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_marble1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_marble1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_marble1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_marble1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
