---
description: "Unnmir is a non-player character (NPC) in Andor's Trail. Starts Lost treasures."
---

# ![](../assets/icons/monsters/monsters_mage2_0.png){ .sprite } Unnmir

**Where to find Unnmir:** not placed on any map; appears through a quest or scripted event.

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_mage2_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [Lost treasures](../quests/nocmar.md) |
| **Entry ID** | `unnmir` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Lost treasures](../quests/nocmar.md): stages 10, 50

## Dialogue simulator

Set your quest stages and items, then talk to Unnmir. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/unnmir.json" data-npc="Unnmir" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (24 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-unnmir"></span>**`unnmir`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if latest stage of [Lost treasures](../quests/nocmar.md#stage-10) is 10)* → [unnmir_r](#d-unnmir_r)
    - branch 2 *(if reached stage 40 of [Lost treasures](../quests/nocmar.md#stage-40))* → [unnmir_hs_10](#d-unnmir_hs_10)
    - branch 3 → [unnmir_0](#d-unnmir_0)

    <span id="d-unnmir_r"></span>**`unnmir_r`** Unnmir: “Hello again. You should go talk to Nocmar.”

    - Next → [unnmir_13](#d-unnmir_13)

    <span id="d-unnmir_hs_10"></span>**`unnmir_hs_10`** Unnmir: “You've come back to visit me?”

    - “Yes and I am really hoping that you can help me! I found the heartstone, but it burns to the touch. I cannot carry it.” *(if NOT reached stage 50 of [Lost treasures](../quests/nocmar.md#stage-50))* → [unnmir_hs_20](#d-unnmir_hs_20)
    - “I don't want to hold you from your busy day. I will leave now.” → *conversation ends*

    <span id="d-unnmir_0"></span>**`unnmir_0`** Unnmir: “Hi there.”

    - “There was a drunk outside the tavern that told me a story about you two.” *(if reached stage 100 of [Drunken tale](../quests/fallhavendrunk.md#stage-100))* → [unnmir_1](#d-unnmir_1)
    - “Inside Undertell, I stumbled across the remains of an adventurer. Among his possessions, he had a 'Jewel of Fallhaven'.” *(if reached stage 10 of [Undertell: What was not written](../quests/undertell_book.md#stage-10); NOT reached stage 40 of [Undertell: What was not written](../quests/undertell_book.md#stage-40); carry 1× [Undertell: Its Ghosts and History](../items/undertell_book.md))* → [unnmir_undertell_book_10](#d-unnmir_undertell_book_10)

    <span id="d-unnmir_13"></span>**`unnmir_13`** Unnmir: “His house is just southwest of the tavern.”

    - “Thanks, I'll go see him.” → *conversation ends*

    <span id="d-unnmir_hs_20"></span>**`unnmir_hs_20`** Unnmir: “Too hot, you say? Hah, that makes sense. The heartstone has been sitting near that cursed rift for centuries, soaking up its heat. No man alive could carry it as it is. But there is a way. Back when I still walked the high trails of…”

    - Next → [unnmir_hs_25](#d-unnmir_hs_25)

    <span id="d-unnmir_1"></span>**`unnmir_1`** Unnmir: “That old drunk over at the tavern told you his story did he?”

    - Next → [unnmir_2](#d-unnmir_2)

    <span id="d-unnmir_undertell_book_10"></span>**`unnmir_undertell_book_10`** Unnmir: “And?”

    - “And he had this book. [show the Undertell history book] I was hoping for your insight.” → [unnmir_undertell_book_20](#d-unnmir_undertell_book_20)

    <span id="d-unnmir_hs_25"></span>**`unnmir_hs_25`** Unnmir: “They called it "Galmore Ice". Unlike any common frost, it does not melt in your hand or in the lowlands. Only the hottest fire, or something born of the Rift itself, can turn it to water. If you can get your hands on a block of it, place…”

    - Next → [unnmir_hs_narrator_10](#d-unnmir_hs_narrator_10)

    <span id="d-unnmir_2"></span>**`unnmir_2`** Unnmir: “Same old story. We used to travel together a few years back.”

    - Next → [unnmir_3](#d-unnmir_3)

    <span id="d-unnmir_undertell_book_20"></span>**`unnmir_undertell_book_20`** Unnmir: “If that book matters, someone in Fallhaven should know why.”

    - “But who?” → [unnmir_undertell_book_30](#d-unnmir_undertell_book_30)

    <span id="d-unnmir_hs_narrator_10"></span>**`unnmir_hs_narrator_10`** [Dummy NPC](../monsters/none.md): “Unnmir leans back, shaking his head.”

    - Next → [unnmir_hs_30](#d-unnmir_hs_30)

    <span id="d-unnmir_3"></span>**`unnmir_3`** Unnmir: “Real adventuring you know, swords and spells.”

    - Next → [unnmir_4](#d-unnmir_4)

    <span id="d-unnmir_undertell_book_30"></span>**`unnmir_undertell_book_30`** Unnmir: “Someone with a lot of books, I presume.”

    - “OK, you don't know then. Thanks anyway.” → *conversation ends*

    <span id="d-unnmir_hs_30"></span>**`unnmir_hs_30`** [Unnmir](../monsters/unnmir.md): “Climbing to that height is no small task, and the beasts there guard it jealously. But if you truly want to see heartsteel reforged, you'll need to brave the peak. No one else can do this but you.” — **effects:** sets stage 50 of [Lost treasures](../quests/nocmar.md#stage-50)

    - “Great. Thanks. That helps a lot.” → *conversation ends*

    <span id="d-unnmir_4"></span>**`unnmir_4`** Unnmir: “Then, after a while, we stopped. I can't really say why, I guess we got tired of life on the road. We settled down here in Fallhaven.”

    - Next → [unnmir_5](#d-unnmir_5)

    <span id="d-unnmir_5"></span>**`unnmir_5`** Unnmir: “Nice little town here. A lot of thieves around, but they don't bother me.”

    - Next → [unnmir_6](#d-unnmir_6)

    <span id="d-unnmir_6"></span>**`unnmir_6`** Unnmir: “So what's your story, kid? How did you end up here in Fallhaven?”

    - “I'm looking for my brother.” → [unnmir_7](#d-unnmir_7)

    <span id="d-unnmir_7"></span>**`unnmir_7`** Unnmir: “Yeah yeah, I get it. Your brother has probably run off to some dungeon, trying to go adventuring. [Rolls eyes]”

    - Next → [unnmir_8](#d-unnmir_8)

    <span id="d-unnmir_8"></span>**`unnmir_8`** Unnmir: “Or maybe he has gone to one of the bigger cities to the north.”

    - Next → [unnmir_9](#d-unnmir_9)

    <span id="d-unnmir_9"></span>**`unnmir_9`** Unnmir: “Can't say I blame him for wanting to see the world.”

    - Next → [unnmir_10](#d-unnmir_10)

    <span id="d-unnmir_10"></span>**`unnmir_10`** Unnmir: “Hey, by the way, are you looking to be an adventurer?”

    - “Yes” → [unnmir_11](#d-unnmir_11)
    - “No, not really.” → [unnmir_12](#d-unnmir_12)

    <span id="d-unnmir_11"></span>**`unnmir_11`** Unnmir: “Nice. I'll give you a hint, kid. *snickering* Go see Nocmar over by the west side of town. Tell him I sent you.” — **effects:** sets stage 10 of [Lost treasures](../quests/nocmar.md#stage-10)

    - Next → [unnmir_13](#d-unnmir_13)

    <span id="d-unnmir_12"></span>**`unnmir_12`** Unnmir: “Smart move. Adventuring leads to a lot of scars. If you know what I mean.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 4 lines changed<br>· text: “Nice. I'll give you a hint, kid. *snickering*. Go see Nocmar over by …” → “Nice. I'll give you a hint, kid. *snickering* Go see Nocmar over by t…”<br>· text: “Yeah yeah, I get it. Your brother has probably run off to some dungeo…” → “Yeah yeah, I get it. Your brother has probably run off to some dungeo…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 8 lines added, 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `unnmir` |
    | Spawn group | `unnmir` |
    | Loot table | – |
    | Conversation | `unnmir` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage2:0` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "unnmir",
     "name": "Unnmir",
     "iconID": "monsters_mage2:0",
     "monsterClass": "humanoid",
     "spawnGroup": "unnmir",
     "phraseID": "unnmir"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=unnmir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=unnmir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=unnmir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=unnmir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
