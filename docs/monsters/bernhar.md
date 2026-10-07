---
description: "Bernhar is a non-player character (NPC) in Andor's Trail, found in Arulirmountain 1. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_ld1_18.png){ .sprite } Bernhar

**Where to find Bernhar:** [Arulirmountain 1](../maps/arulirmountain1.md#pin-npc-bernhar)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_18.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Found in** | Arulirmountain 1 |
| **Entry ID** | `bernhar` |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Rockfall deflecting cap](../items/arulir_cap.md) | 100% | 1 |
| [Sure step boots](../items/arulir_boots.md) | 100% | 1 |

## Quests

- [Arulir cave story flags (hidden flag)](../quests/arulircave_non_display.md): stage 10

## Dialogue simulator

Set your quest stages and items, then talk to Bernhar. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/bernhar.json" data-npc="Bernhar" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (12 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-bernhar"></span>**`bernhar`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [Arulir cave story flags (hidden flag)](../quests/arulircave_non_display.md#stage-10))* → [bernhar_16](#d-bernhar_16)
    - branch 2 → [bernhar_10](#d-bernhar_10)

    <span id="d-bernhar_16"></span>**`bernhar_16`** Bernhar: “Oh - the wandering kid! You are still alive? How surprising!”

    - “Hi Bernhar. I want to talk with you again.” → [bernhar_20](#d-bernhar_20)

    <span id="d-bernhar_10"></span>**`bernhar_10`** Bernhar: “Oh - a wandering kid! How surprising!”

    - “Who are you?” → [bernhar_12](#d-bernhar_12)
    - “What are you doing here?” → [bernhar_12](#d-bernhar_12)

    <span id="d-bernhar_20"></span>**`bernhar_20`** Bernhar: “Sure! I could tell you things...”

    - Next → [bernhar_30](#d-bernhar_30)

    <span id="d-bernhar_12"></span>**`bernhar_12`** Bernhar: “My name is Bernhar. I am an explorer, and I'm trying to find out something about the cave system here.”

    - “Have you already found something?” → [bernhar_20](#d-bernhar_20)
    - “Ah. Interesting. Keep having fun with it. Bye.” → *conversation ends*

    <span id="d-bernhar_30"></span>**`bernhar_30`** Bernhar: “Steep mountain flanks and wide, branching, cave passages! But beware - it is dangerous ground! You must not go unprotected!”

    - “What do you mean by "unprotected"?” → [bernhar_40](#d-bernhar_40)
    - “I have heard this before.” *(if reached stage 10 of [Arulir cave story flags (hidden flag)](../quests/arulircave_non_display.md#stage-10))* → [bernhar_32](#d-bernhar_32)

    <span id="d-bernhar_40"></span>**`bernhar_40`** Bernhar: “You are risking your life here. It is not only those Arulir brutes. They are just annoying.” — **effects:** sets stage 10 of [Arulir cave story flags (hidden flag)](../quests/arulircave_non_display.md#stage-10)

    - Next → [bernhar_50](#d-bernhar_50)

    <span id="d-bernhar_32"></span>**`bernhar_32`** Bernhar: “You are not taking me seriously. Let me tell you...”

    - Next → [bernhar_40](#d-bernhar_40)

    <span id="d-bernhar_50"></span>**`bernhar_50`** Bernhar: “The ground is really dangerous. It's deceptive and life-threatening. And there is always the danger of falling rocks from above.”

    - “How did you manage?” → [bernhar_60](#d-bernhar_60)

    <span id="d-bernhar_60"></span>**`bernhar_60`** Bernhar: “I was only able to survive this far because I was wearing the proper protective gear.”

    - Next → [bernhar_70](#d-bernhar_70)

    <span id="d-bernhar_70"></span>**`bernhar_70`** Bernhar: “I have completed my work here though, so I don't need it any more. I could sell it to you for a good price.”

    - “Great, show me please.” → *shop opens*
    - “Maybe another time.” → [bernhar_80](#d-bernhar_80)

    <span id="d-bernhar_80"></span>**`bernhar_80`** Bernhar: “If you go in there unprotected, I fear there will be no other time.”

    - “OK. Let's have a look.” → *shop opens*
    - “I can handle myself.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 12 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `bernhar` |
    | Spawn group | `bernhar` |
    | Loot table | `bernhar_shop` |
    | Conversation | `bernhar` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:18` |
    | Defined in | `res/raw/monsterlist_arulir_mountain.json` |

    Raw data:

    ```json
    {
     "id": "bernhar",
     "name": "Bernhar",
     "iconID": "monsters_ld1:18",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "bernhar",
     "droplistID": "bernhar_shop"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bernhar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bernhar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bernhar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bernhar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
