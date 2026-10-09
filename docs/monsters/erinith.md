---
description: "Erinith is a non-player character (NPC) in Andor's Trail, found in Crossroads Guardhouse. Starts Deep wound."
---

# ![](../assets/icons/monsters/monsters_rltiles1_82.png){ .sprite } Erinith

**Where to find Erinith:** Crossroads Guardhouse: [Wild 0](../maps/wild0.md#pin-npc-erinith)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_82.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [Deep wound](../quests/erinith.md) |
| **Found in** | Crossroads Guardhouse |
| **Entry ID** | `erinith` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Deep wound](../quests/erinith.md): stages 10, 20, 21, 30, 31, 40, 41, 42, 50

## Dialogue simulator

Set your quest stages and items, then talk to Erinith. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/erinith.json" data-npc="Erinith" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (30 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-erinith"></span>**`erinith`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [Deep wound](../quests/erinith.md#stage-50))* → [erinith_complete_1](#d-erinith_complete_1)
    - branch 2 *(if reached stage 40 of [Deep wound](../quests/erinith.md#stage-40))* → [erinith_givenpotion_1](#d-erinith_givenpotion_1)
    - branch 3 *(if reached stage 41 of [Deep wound](../quests/erinith.md#stage-41))* → [erinith_givenpotion_1](#d-erinith_givenpotion_1)
    - branch 4 *(if reached stage 42 of [Deep wound](../quests/erinith.md#stage-42))* → [erinith_givenpotion_1](#d-erinith_givenpotion_1)
    - branch 5 *(if reached stage 30 of [Deep wound](../quests/erinith.md#stage-30))* → [erinith_needspotions_1](#d-erinith_needspotions_1)
    - branch 6 *(if reached stage 20 of [Deep wound](../quests/erinith.md#stage-20))* → [erinith_needsbook_1](#d-erinith_needsbook_1)
    - branch 7 *(if reached stage 21 of [Deep wound](../quests/erinith.md#stage-21))* → [erinith_needsbook_1](#d-erinith_needsbook_1)
    - branch 8 → [erinith_1](#d-erinith_1)

    <span id="d-erinith_complete_1"></span>**`erinith_complete_1`** Erinith: “Thank you for all your help earlier.”


    <span id="d-erinith_givenpotion_1"></span>**`erinith_givenpotion_1`** Erinith: “Thank you my friend for your help. My book is safe and my wound is healing. I hope our paths will cross again.” — **effects:** sets stage 50 of [Deep wound](../quests/erinith.md#stage-50)


    <span id="d-erinith_needspotions_1"></span>**`erinith_needspotions_1`** Erinith: “Thank you for helping me find my book earlier.”

    - Next → [erinith_needspotions_2](#d-erinith_needspotions_2)

    <span id="d-erinith_needsbook_1"></span>**`erinith_needsbook_1`** Erinith: “Have you found that book yet?”

    - “Not yet, I am still looking.” → [erinith_story_8](#d-erinith_story_8)
    - “Yes, here is your book.” *(if hand over 1× [Erinith's book](../items/erinith_book.md))* → [erinith_needsbook_2](#d-erinith_needsbook_2)

    <span id="d-erinith_1"></span>**`erinith_1`** Erinith: “Please, you have to help me!”

    - “What's wrong?” → [erinith_story_1](#d-erinith_story_1)

    <span id="d-erinith_needspotions_2"></span>**`erinith_needspotions_2`** Erinith: “I am still hurt by this wound that I got from the attack during the night.”

    - Next → [erinith_needspotions_3](#d-erinith_needspotions_3)

    <span id="d-erinith_story_8"></span>**`erinith_story_8`** Erinith: “Please go look for it among those trees to the northeast.”


    <span id="d-erinith_needsbook_2"></span>**`erinith_needsbook_2`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 30 of [Deep wound](../quests/erinith.md#stage-30)

    - branch 1 *(if reached stage 21 of [Deep wound](../quests/erinith.md#stage-21))* → [erinith_needsbook_3_2](#d-erinith_needsbook_3_2)
    - branch 2 → [erinith_needsbook_3_1](#d-erinith_needsbook_3_1)

    <span id="d-erinith_story_1"></span>**`erinith_story_1`** Erinith: “I was setting up camp here during the night, and was attacked by some bandits while asleep.” — **effects:** sets stage 10 of [Deep wound](../quests/erinith.md#stage-10)

    - Next → [erinith_story_2](#d-erinith_story_2)

    <span id="d-erinith_needspotions_3"></span>**`erinith_needspotions_3`** Erinith: “Ack, it hurts so bad and it doesn't seem to be healing itself.”

    - Next → [erinith_needspotions_4](#d-erinith_needspotions_4)

    <span id="d-erinith_needsbook_3_2"></span>**`erinith_needsbook_3_2`** Erinith: “You found it! Oh thank you so much. In return, here is the gold I promised you.” — **effects:** gives [Gold coins](../items/gold.md)

    - Next → [erinith_needspotions_2](#d-erinith_needspotions_2)

    <span id="d-erinith_needsbook_3_1"></span>**`erinith_needsbook_3_1`** Erinith: “You found it! Oh thank you so much. I was so worried that I had lost it.”

    - Next → [erinith_needspotions_2](#d-erinith_needspotions_2)

    <span id="d-erinith_story_2"></span>**`erinith_story_2`** Erinith: “Ack, this wound doesn't seem to be healing itself.”

    - Next → [erinith_story_3](#d-erinith_story_3)

    <span id="d-erinith_needspotions_4"></span>**`erinith_needspotions_4`** Erinith: “I am really in need of some stronger healing here. Maybe some potions would do.”

    - Next → [erinith_needspotions_5](#d-erinith_needspotions_5)

    <span id="d-erinith_story_3"></span>**`erinith_story_3`** Erinith: “At least I managed to keep them from getting my book. I'm sure they were after the book.”

    - “Seems like a valuable book then. This sounds interesting, please go on.” → [erinith_story_4](#d-erinith_story_4)
    - “What happened?” → [erinith_story_4](#d-erinith_story_4)

    <span id="d-erinith_needspotions_5"></span>**`erinith_needspotions_5`** Erinith: “I have heard that the potion makers these days have major potions of health, and not just the regular potions of health.”

    - Next → [erinith_needspotions_6](#d-erinith_needspotions_6)

    <span id="d-erinith_story_4"></span>**`erinith_story_4`** Erinith: “I managed to throw the book in among the trees over there during the attack. [Points to the trees directly to the north]”

    - Next → [erinith_story_5](#d-erinith_story_5)

    <span id="d-erinith_needspotions_6"></span>**`erinith_needspotions_6`** Erinith: “One of those would surely do. Otherwise, I think four regular potions of health would be enough.” — **effects:** sets stage 31 of [Deep wound](../quests/erinith.md#stage-31)

    - “I'll go get those potions for you.” → [erinith_needspotions_7](#d-erinith_needspotions_7)
    - “Here, take this bonemeal potion instead. It's very potent in healing deep wounds.” *(if hand over 1× [Bonemeal potion](../items/bonemeal_potion.md))* → [erinith_gavepotion_bm_1](#d-erinith_gavepotion_bm_1)
    - “Here, take this major potion of health.” *(if hand over 1× [Major potion of health](../items/health_major2.md))* → [erinith_gavepotion_major_1](#d-erinith_gavepotion_major_1)
    - “Here, take this major flask of health.” *(if hand over 1× [Major flask of health](../items/health_major.md))* → [erinith_gavepotion_major_1](#d-erinith_gavepotion_major_1)
    - “Here, take these four regular potions of health.” *(if hand over 4× [Regular potion of health](../items/health.md))* → [erinith_gavepotion_reg_1](#d-erinith_gavepotion_reg_1)

    <span id="d-erinith_story_5"></span>**`erinith_story_5`** Erinith: “I don't think they managed to get the book. It's probably still somewhere among those trees.”

    - “What is in the book?” → [erinith_story_6](#d-erinith_story_6)

    <span id="d-erinith_needspotions_7"></span>**`erinith_needspotions_7`** Erinith: “Thank you my friend. Please hurry back.”


    <span id="d-erinith_gavepotion_bm_1"></span>**`erinith_gavepotion_bm_1`** Erinith: “Bonemeal potion? But ... but ... we are not allowed to use them since they are prohibited by Lord Geomyr.” — **effects:** sets stage 40 of [Deep wound](../quests/erinith.md#stage-40)

    - “Who will find out?” → [erinith_gavepotion_bm_2](#d-erinith_gavepotion_bm_2)
    - “I have tried them myself, it's perfectly safe to use them.” → [erinith_gavepotion_bm_2](#d-erinith_gavepotion_bm_2)

    <span id="d-erinith_gavepotion_major_1"></span>**`erinith_gavepotion_major_1`** Erinith: “Thank you for bringing me one. [Drinks potion]” — **effects:** sets stage 41 of [Deep wound](../quests/erinith.md#stage-41)

    - Next → [erinith_gavepotion_1](#d-erinith_gavepotion_1)

    <span id="d-erinith_gavepotion_reg_1"></span>**`erinith_gavepotion_reg_1`** Erinith: “Thank you for bringing them to me. [Drinks all four potions]” — **effects:** sets stage 42 of [Deep wound](../quests/erinith.md#stage-42)

    - Next → [erinith_gavepotion_1](#d-erinith_gavepotion_1)

    <span id="d-erinith_story_6"></span>**`erinith_story_6`** Erinith: “Oh, I can't say really.”

    - “I could help you find that book if you want.” → [erinith_story_7](#d-erinith_story_7)
    - “What would it be worth for you to get that book back?” → [erinith_story_gold_1](#d-erinith_story_gold_1)

    <span id="d-erinith_gavepotion_bm_2"></span>**`erinith_gavepotion_bm_2`** Erinith: “Hmm, yes. I guess you have a point. Oh well, here goes. [Drinks potion]”

    - Next → [erinith_gavepotion_1](#d-erinith_gavepotion_1)

    <span id="d-erinith_gavepotion_1"></span>**`erinith_gavepotion_1`** Erinith: “Wow, I feel slightly better already. I guess this healing really works.”

    - Next → [erinith_givenpotion_1](#d-erinith_givenpotion_1)

    <span id="d-erinith_story_7"></span>**`erinith_story_7`** Erinith: “You would? Oh thank you.” — **effects:** sets stage 20 of [Deep wound](../quests/erinith.md#stage-20)

    - Next → [erinith_story_8](#d-erinith_story_8)

    <span id="d-erinith_story_gold_1"></span>**`erinith_story_gold_1`** Erinith: “Worth? Well, I was hoping you would help me anyway, but I guess 200 gold could do.”

    - “200 gold it is then. I'll go look for your book.” → [erinith_story_gold_2](#d-erinith_story_gold_2)
    - “A lousy 200 gold, is that all you can do? Fine, I'll go look for your stupid book.” → [erinith_story_gold_2](#d-erinith_story_gold_2)
    - “Keep your gold, I'll return your book for you anyway.” → [erinith_story_7](#d-erinith_story_7)
    - “No, I am not getting involved in this. Goodbye.” → *conversation ends*

    <span id="d-erinith_story_gold_2"></span>**`erinith_story_gold_2`** Erinith: “Make it quick.” — **effects:** sets stage 21 of [Deep wound](../quests/erinith.md#stage-21)

    - Next → [erinith_story_8](#d-erinith_story_8)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 7 lines changed<br>· text: “Thank you for bringing them to me. *drinks all four potions*” → “Thank you for bringing them to me. [Drinks all four potions]”<br>· text: “Thank you for bringing me one. *drinks potion*” → “Thank you for bringing me one. [Drinks potion]” |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed |
| [v0.8.7](../versions/0.8.7.md) | Dialogue: 1 line changed<br>· text: “I have heard that the potion makers these days have potions of major …” → “I have heard that the potion makers these days have major potions of …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `erinith` |
    | Spawn group | `erinith` |
    | Loot table | – |
    | Conversation | `erinith` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:82` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "erinith",
     "name": "Erinith",
     "iconID": "monsters_rltiles1:82",
     "monsterClass": "humanoid",
     "spawnGroup": "erinith",
     "phraseID": "erinith"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erinith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erinith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erinith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erinith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
