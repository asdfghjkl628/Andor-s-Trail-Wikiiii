---
description: "Librarian is an NPC you can also fight in Andor's Trail, found in Library."
---

# ![](../assets/icons/monsters/monsters_rltiles1_94.png){ .sprite } Librarian

**Where to find Librarian:** Library: [Ratdom maze 611](../maps/ratdom_maze_611.md#pin-npc-ratdom_librarian)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_94.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Library |
| **Class** | Humanoid |
| **HP** | 60 |
| **XP when defeated** | 42 |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

!!! warning "You can fight Librarian"
    Answering “Andor is my brother. I'm going to look for a clue to his whereabouts now. You…” starts a fight with Librarian.

    Answering “You'll soon stop laughing.” starts a fight with Librarian.

## Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 60 |
| XP when defeated | 42 |
| Damage | 10 to 30 |
| AC | 0 |
| BC | 0 |
| DR | 0 |
| Attacks per turn | 1 (10 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Ratcave Torch](../items/ratdom_torch.md) | 50% | 1 |
| [Gold coins](../items/gold.md) | 50% | 30 to 80 |
| [Nasty looking book](../items/ratdom_book.md) | 100% | 1 |

## Quests

- [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md): stages 93, 95

## Dialogue simulator

Set your quest stages and items, then talk to Librarian. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_librarian.json" data-npc="Librarian" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (13 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ratdom_librarian"></span>**`ratdom_librarian`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 95 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-95))* → [ratdom_librarian_42](#d-ratdom_librarian_42)
    - Next → [ratdom_librarian_2](#d-ratdom_librarian_2)

    <span id="d-ratdom_librarian_42"></span>**`ratdom_librarian_42`** [Dummy NPC](../monsters/none.md): “The librarian is completely absorbed in his new book.”


    <span id="d-ratdom_librarian_2"></span>**`ratdom_librarian_2`** Librarian: “Andor! Good that you are back at last!”

    - “I am $playername. You have confused me with my brother.” → [ratdom_librarian_10](#d-ratdom_librarian_10)
    - “Indeed. Any news?” → [ratdom_librarian_20](#d-ratdom_librarian_20)
    - “Here I have a new book for your library.” *(if hand over 1× [World History](../items/book_world_history.md))* → [ratdom_librarian_40](#d-ratdom_librarian_40)

    <span id="d-ratdom_librarian_10"></span>**`ratdom_librarian_10`** Librarian: “Yes. I see it now. Please leave. My master is not present today.”

    - “Andor - master? What ... Where is my brother?” → [ratdom_librarian_12](#d-ratdom_librarian_12)

    <span id="d-ratdom_librarian_20"></span>**`ratdom_librarian_20`** Librarian: “I am not sure. Today I hear footsteps of strangers in the corridors.”

    - “[muttering] Probably mine.” → [ratdom_librarian_22](#d-ratdom_librarian_22)
    - “Then what are you waiting for? Go and look who is wandering through our passages!” → [ratdom_librarian_30](#d-ratdom_librarian_30)
    - “Nonsense. Strangers would never find this secret library.” → [ratdom_librarian_24](#d-ratdom_librarian_24)

    <span id="d-ratdom_librarian_40"></span>**`ratdom_librarian_40`** Librarian: “Oh! What a wonder! I always wanted to have a copy of that wonderful book! Here, take this special bone as a token of my everlasting thanks. [gives leg bone of a rat]” — **effects:** gives 1× [Back bones of a rat](../items/ratdom_rat_skelett_back.md), sets stage 95 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-95)

    - “A lousy bone for this valuable book?!” → [ratdom_librarian_42](#d-ratdom_librarian_42)

    <span id="d-ratdom_librarian_12"></span>**`ratdom_librarian_12`** Librarian: “That does not concern you. Mind your own business and leave now!”

    - “Bye.” → *conversation ends*
    - “Tell me about Andor, or ...” → [ratdom_librarian_14](#d-ratdom_librarian_14)

    <span id="d-ratdom_librarian_22"></span>**`ratdom_librarian_22`** Librarian: “What? You are the stranger! You are not allowed to be here!”

    - “It's fine, I'm going already.” → *conversation ends*
    - “Andor is my brother. I'm going to look for a clue to his whereabouts now. You won't stop me from doing that.” → *fight starts*

    <span id="d-ratdom_librarian_30"></span>**`ratdom_librarian_30`** Librarian: “As you command me - I'll be right back.”

    - “Take your time, better to be be thorough!” → [ratdom_librarian_32](#d-ratdom_librarian_32)

    <span id="d-ratdom_librarian_24"></span>**`ratdom_librarian_24`** Librarian: “You're right, I'm sure I only see pipe dreams.”

    - Next *(if carry 1× [World History](../items/book_world_history.md))* → [ratdom_librarian_26](#d-ratdom_librarian_26)

    <span id="d-ratdom_librarian_14"></span>**`ratdom_librarian_14`** Librarian: “Or what? Attack? Hahaha!”

    - “You'll soon stop laughing.” → *fight starts*
    - “Just you wait when I come back.” → *conversation ends*

    <span id="d-ratdom_librarian_32"></span>**`ratdom_librarian_32`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 93 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-93)

    - Next → *NPC leaves*

    <span id="d-ratdom_librarian_26"></span>**`ratdom_librarian_26`** Librarian: “If only I had something to read. Something new, that I haven't read twenty times already.”

    - “Here I have a new book for your library.” *(if hand over 1× [World History](../items/book_world_history.md))* → [ratdom_librarian_40](#d-ratdom_librarian_40)



## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 13 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ratdom_librarian` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `ratdom_librarian` |
    | Loot table | `ratdom_librarian` |
    | Conversation | `ratdom_librarian` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:94` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_librarian",
     "name": "Librarian",
     "iconID": "monsters_rltiles1:94",
     "maxHP": 60,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 10,
      "max": 30
     },
     "spawnGroup": "ratdom_librarian",
     "phraseID": "ratdom_librarian",
     "droplistID": "ratdom_librarian"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_librarian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_librarian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_librarian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_librarian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
