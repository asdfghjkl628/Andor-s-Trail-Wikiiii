---
description: "Arcir is a non-player character (NPC) in Andor's Trail."
---

# ![](../assets/icons/monsters/monsters_mage2_0.png){ .sprite } Arcir

**Where to find Arcir:** not placed on any map; appears through a quest or scripted event.

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_mage2_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Entry ID** | `arcir` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Undertell: What was not written](../quests/undertell_book.md): stages 40, 90
- [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md): stage 10

## Dialogue simulator

Set your quest stages and items, then talk to Arcir. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/arcir_start.json" data-npc="Arcir" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (29 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-arcir_start"></span>**`arcir_start`** Arcir: “Hello. I'm Arcir.”

    - “I noticed your statue of Elythara downstairs.” *(if reached stage 10 of [Elythara (Arcir) flags (hidden flag)](../quests/arcir.md#stage-10))* → [arcir_elythara_1](#d-arcir_elythara_1)
    - “You really seem to like your books.” → [arcir_books_1](#d-arcir_books_1)
    - “And I'm your delivery kid. Did you order a 'Dusty old book'?” *(if hand over 1× [Dusty old book](../items/brv_wh_item_09.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 20 of [Delivery](../quests/brv_wh_delivery.md#stage-20))* → [brv_wh_delivery_arcir](#d-brv_wh_delivery_arcir)
    - “What am I supposed to do again?” *(if reached stage 40 of [Undertell: What was not written](../quests/undertell_book.md#stage-40); NOT reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50); NOT reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60); NOT reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70))* → [arcir_remind_40](#d-arcir_remind_40)
    - “The Elytharan ghost still remembers who he was.” *(if reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50); NOT reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60); NOT reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70))* → [arcir_partial_50](#d-arcir_partial_50)
    - “The ghost spoke only of work, of tasks repeated.” *(if reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60); NOT reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50); NOT reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70))* → [arcir_partial_60](#d-arcir_partial_60)
    - “I tried to speak to a ghost, but it would not speak at all.” *(if reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70); NOT reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50); NOT reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60))* → [arcir_partial_70](#d-arcir_partial_70)
    - “I spoke to more than one Elytharan ghost.” *(if reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50); reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60); NOT reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70))* → [arcir_partial_two](#d-arcir_partial_two)
    - “I spoke to more than one Elytharan ghost.” *(if reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70); reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60); NOT reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50))* → [arcir_partial_two](#d-arcir_partial_two)
    - “I spoke to more than one Elytharan ghost.” *(if reached stage 50 of [Undertell: What was not written](../quests/undertell_book.md#stage-50); reached stage 70 of [Undertell: What was not written](../quests/undertell_book.md#stage-70); NOT reached stage 60 of [Undertell: What was not written](../quests/undertell_book.md#stage-60))* → [arcir_partial_two](#d-arcir_partial_two)
    - “The Elytharan ghosts remember different things.” *(if reached stage 80 of [Undertell: What was not written](../quests/undertell_book.md#stage-80); NOT reached stage 90 of [Undertell: What was not written](../quests/undertell_book.md#stage-90))* → [arcir_undertell_complete_npc](#d-arcir_undertell_complete_npc)

    <span id="d-arcir_elythara_1"></span>**`arcir_elythara_1`** Arcir: “Oh, you found my statue in the basement? Yes, Elythara is my protector.”

    - “OK.” → [arcir_anythingelse](#d-arcir_anythingelse)

    <span id="d-arcir_books_1"></span>**`arcir_books_1`** Arcir: “I find great pleasure in my books. They contain the accumulated knowledge of past generations.”

    - “Do you have a book called 'Calomyran Secrets'?” *(if reached stage 10 of [Calomyran secrets](../quests/calomyran.md#stage-10))* → [arcir_calomyran_select](#d-arcir_calomyran_select)
    - “OK.” → [arcir_anythingelse](#d-arcir_anythingelse)
    - “I have found some valuable-looking map. Want to have a look?” *(if carry 1× [Ewmondold's map](../items/inspiring_snake_master_map.md); killed 1× [Ewmondold](../monsters/ewmondold_snake_master.md))* → [arcir_books_rares_map](#d-arcir_books_rares_map)
    - “I have found a strange book about slavery. Interested?” *(if carry 1× [Nasty looking book](../items/ratdom_book.md))* → [arcir_books_rares_book1](#d-arcir_books_rares_book1)
    - “I have a book about world history. Interested?” *(if carry 1× [World History](../items/book_world_history.md))* → [arcir_books_rares_book2](#d-arcir_books_rares_book2)
    - “I found a book about Undertell. I thought you might know something about it.” *(if NOT reached stage 40 of [Undertell: What was not written](../quests/undertell_book.md#stage-40); carry 1× [Undertell: Its Ghosts and History](../items/undertell_book.md))* → [arcir_undertell_10](#d-arcir_undertell_10)

    <span id="d-brv_wh_delivery_arcir"></span>**`brv_wh_delivery_arcir`** Arcir: “Yes, an old but useful book, but you should have wiped it off first. Anyway, here's my delivery fee.” — **effects:** clears stage 20 of [Delivery](../quests/brv_wh_delivery.md#stage-20), sets stage 10 of [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-10), gives 20× [Gold coins](../items/gold.md)

    - “Thank you.” → *conversation ends*

    <span id="d-arcir_remind_40"></span>**`arcir_remind_40`** Arcir: “I asked you to listen, not for stories, but for failure. If Undertell erased the Elytharan deliberately, it would not do so in only one way. Return. Listen for difference.”

    - “I will return to Undertell.” → *conversation ends*

    <span id="d-arcir_partial_50"></span>**`arcir_partial_50`** Arcir: “Memory of the self endures first. Pain follows identity. Systems are not remembered, they are endured. You must listen again.”

    - “I understand.” → *conversation ends*

    <span id="d-arcir_partial_60"></span>**`arcir_partial_60`** Arcir: “Then you heard structure without belief. A system reveals itself through repetition. You must listen more.”

    - “I understand” → *conversation ends*

    <span id="d-arcir_partial_70"></span>**`arcir_partial_70`** Arcir: “Silence is not absence. It is what remains when speech was never permitted.”

    - “I understand.” → *conversation ends*

    <span id="d-arcir_partial_two"></span>**`arcir_partial_two`** Arcir: “Then you have more than one account. That allows comparison, but only if you listen for what does not repeat. Systems reveal themselves at their edges. Return. Do not seek another voice. Seek the limit of speech itself”

    - “I will return once more.” → *conversation ends*

    <span id="d-arcir_undertell_complete_npc"></span>**`arcir_undertell_complete_npc`** Arcir: “Of course they do. History records stone and steel, but memory lives in people even after death. You have given voice to what was buried. That is worth more than any written account.” — **effects:** sets stage 90 of [Undertell: What was not written](../quests/undertell_book.md#stage-90)

    - “I'm glad I could help.” → [arcir_anythingelse](#d-arcir_anythingelse)

    <span id="d-arcir_anythingelse"></span>**`arcir_anythingelse`** Arcir: “Anything else you wanted to ask?”

    - “I noticed your statue of Elythara downstairs.” *(if reached stage 10 of [Elythara (Arcir) flags (hidden flag)](../quests/arcir.md#stage-10))* → [arcir_elythara_1](#d-arcir_elythara_1)
    - “You really seem to like your books.” → [arcir_books_1](#d-arcir_books_1)

    <span id="d-arcir_calomyran_select"></span>**`arcir_calomyran_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Calomyran secrets](../quests/calomyran.md#stage-100))* → [arcir_calomyran_complete](#d-arcir_calomyran_complete)
    - branch 2 *(if reached stage 20 of [Calomyran secrets](../quests/calomyran.md#stage-20))* → [arcir_calomyran_5](#d-arcir_calomyran_5)
    - branch 3 → [arcir_calomyran_1](#d-arcir_calomyran_1)

    <span id="d-arcir_books_rares_map"></span>**`arcir_books_rares_map`** Arcir: “Oh, an ancient map of the area! This would fit well into my collection of old maps. I offer you 500 gold pieces for it.”

    - “Thanks, I'd rather keep it.” → [arcir_books_1](#d-arcir_books_1)
    - “OK. Here is Ewmondold's map.” *(if hand over 1× [Ewmondold's map](../items/inspiring_snake_master_map.md))* → [arcir_books_rares_map_1](#d-arcir_books_rares_map_1)

    <span id="d-arcir_books_rares_book1"></span>**`arcir_books_rares_book1`** Arcir: “Let's have a look. Oh, what the ... Well, this is no book for little ones as you. Give it to me, you get 200 pieces of gold for it.”

    - “Thanks, I'd rather keep it.” → [arcir_books_1](#d-arcir_books_1)
    - “OK. Here is the book about slavery.” *(if hand over 1× [Nasty looking book](../items/ratdom_book.md))* → [arcir_books_rares_book1_1](#d-arcir_books_rares_book1_1)

    <span id="d-arcir_books_rares_book2"></span>**`arcir_books_rares_book2`** Arcir: “Ah, a history textbook.”

    - Next → [arcir_books_rares_book2_1](#d-arcir_books_rares_book2_1)

    <span id="d-arcir_undertell_10"></span>**`arcir_undertell_10`** Arcir: “Undertell! That book was written carefully. Not to preserve truth, but to survive being questioned. The Aewatha Kingdom was meticulous in year four hundred and thirty-two. Stone was counted. Labor was measured. Voices were not.”

    - “What is it leaving out?” → [arcir_undertell_20](#d-arcir_undertell_20)

    <span id="d-arcir_calomyran_complete"></span>**`arcir_calomyran_complete`** Arcir: “I heard you found it and gave it back to old man Benradas. Thank you. He tends to forget things.”

    - Next → [arcir_anythingelse](#d-arcir_anythingelse)

    <span id="d-arcir_calomyran_5"></span>**`arcir_calomyran_5`** Arcir: “You looked downstairs but didn't find it? And a note you say? I guess there must have been someone in my house.”

    - Next → [arcir_calomyran_6](#d-arcir_calomyran_6)

    <span id="d-arcir_calomyran_1"></span>**`arcir_calomyran_1`** Arcir: “'Calomyran Secrets'? Hmm, yes I think I have one of those in my basement.”

    - Next → [arcir_calomyran_2](#d-arcir_calomyran_2)

    <span id="d-arcir_books_rares_map_1"></span>**`arcir_books_rares_map_1`** Arcir: “And here are 500 shining gold pieces. Use them wisely.” — **effects:** gives 500× [Gold coins](../items/gold.md)

    - “Thanks, I have to go now.” → *conversation ends*
    - “Let's talk about other things.” → [arcir_books_1](#d-arcir_books_1)

    <span id="d-arcir_books_rares_book1_1"></span>**`arcir_books_rares_book1_1`** Arcir: “And here are 200 shining gold pieces. Be happy that I'm freeing you from this terrible work.” — **effects:** gives 200× [Gold coins](../items/gold.md)

    - “Thanks, I have to go now.” → *conversation ends*
    - “Let's talk about other things.” → [arcir_books_1](#d-arcir_books_1)

    <span id="d-arcir_books_rares_book2_1"></span>**`arcir_books_rares_book2_1`** Arcir: “But there are a lot of pages missing. Did you rip them out? You should be ashamed of yourself!”

    - “No, that wasn't me!” → [arcir_books_rares_book2_2](#d-arcir_books_rares_book2_2)

    <span id="d-arcir_undertell_20"></span>**`arcir_undertell_20`** Arcir: “The Elytharan followers sent into those mines did not vanish. They were made unrecordable. If even one of them still remembers themselves, then this book is incomplete. You have already walked Undertell. Return and listen for what the…” — **effects:** sets stage 40 of [Undertell: What was not written](../quests/undertell_book.md#stage-40), spawns monsters on undertell_1_1

    - “I will return to Undertell and listen.” → *conversation ends*

    <span id="d-arcir_calomyran_6"></span>**`arcir_calomyran_6`** Arcir: “What did the note say? Larcal ... I know of him. Always causing trouble. He is usually in the barn to the east of here.”

    - “Thanks, bye.” → *conversation ends*

    <span id="d-arcir_calomyran_2"></span>**`arcir_calomyran_2`** Arcir: “Old man Benradas came by last week, wanting to sell me that book. Since it's not really my kind of book, I declined.”

    - Next → [arcir_calomyran_3](#d-arcir_calomyran_3)

    <span id="d-arcir_books_rares_book2_2"></span>**`arcir_books_rares_book2_2`** Arcir: “Such a beautiful book, completely broken! You dare to offer this to me and think I won't notice?!”

    - “[Run]” → [arcir_books_rares_book2_3](#d-arcir_books_rares_book2_3)
    - “Let's talk about other things.” → [arcir_books_1](#d-arcir_books_1)

    <span id="d-arcir_calomyran_3"></span>**`arcir_calomyran_3`** Arcir: “He seemed upset that I didn't like his book, and threw it at me while storming out of the house.”

    - Next → [arcir_calomyran_4](#d-arcir_calomyran_4)

    <span id="d-arcir_books_rares_book2_3"></span>**`arcir_books_rares_book2_3`** Arcir: “Yes, just run away, you book murderer!”


    <span id="d-arcir_calomyran_4"></span>**`arcir_calomyran_4`** Arcir: “Poor old man Benradas, he probably forgot that he left it here. He tends to forget things.”

    - Next → [arcir_anythingelse](#d-arcir_anythingelse)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 7 lines changed<br>· text: “'Calomyran Secrets'? Hm, yes I think I have one of those in my baseme…” → “'Calomyran Secrets'? Hmm, yes I think I have one of those in my basem…”<br>· text: “What did the note say? Larcal.. I know of him. Always causing trouble…” → “What did the note say? Larcal ... I know of him. Always causing troub…” |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 1 line added, 1 line changed |
| [v0.8.11](../versions/0.8.11.md) | Dialogue: 8 lines added, 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 8 lines added, 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `arcir` |
    | Spawn group | `arcir` |
    | Loot table | – |
    | Conversation | `arcir_start` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage2:0` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "arcir",
     "name": "Arcir",
     "iconID": "monsters_mage2:0",
     "monsterClass": "humanoid",
     "spawnGroup": "arcir",
     "phraseID": "arcir_start"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arcir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arcir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arcir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arcir.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
