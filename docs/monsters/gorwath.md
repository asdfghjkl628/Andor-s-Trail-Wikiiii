---
description: "Gorwath is a non-player character (NPC) in Andor's Trail, found in Crossglen. Starts You're the postman."
---

# ![](../assets/icons/monsters/monsters_ld1_88.png){ .sprite } Gorwath

**Where to find Gorwath:** Crossglen: [Crossglen](../maps/crossglen.md#pin-npc-gorwath)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_88.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Starts [You're the postman](../quests/postman.md) |
| **Found in** | Crossglen |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Quests

- [You're the postman](../quests/postman.md): stages 10, 12, 15, 30

## Dialogue simulator

Set your quest stages and items, then talk to Gorwath. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/gorwath.json" data-npc="Gorwath" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (25 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-gorwath"></span>**`gorwath`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [You're the postman](../quests/postman.md#stage-30))* → [gorwath_done](#d-gorwath_done)
    - branch 2 *(if reached stage 20 of [You're the postman](../quests/postman.md#stage-20))* → [gorwath_love](#d-gorwath_love)
    - branch 3 *(if reached stage 15 of [You're the postman](../quests/postman.md#stage-15))* → [gorwath_tmp](#d-gorwath_tmp)
    - branch 4 *(if reached stage 10 of [You're the postman](../quests/postman.md#stage-10))* → [gorwath_letter_20](#d-gorwath_letter_20)
    - branch 5 → [gorwath_letter](#d-gorwath_letter)

    <span id="d-gorwath_done"></span>**`gorwath_done`** Gorwath: “Thanks again for your great help!”

    - “My pleasure.” → [gorwath_exit](#d-gorwath_exit)

    <span id="d-gorwath_love"></span>**`gorwath_love`** Gorwath: “You are back! Did you find Arensia?”

    - “Yes. I gave her the letter and she asked me to tell you that she loves you too.” → [gorwath_love_1](#d-gorwath_love_1)

    <span id="d-gorwath_tmp"></span>**`gorwath_tmp`** Gorwath: “Did you give her the letter yet?”

    - “Eh ... no. I thought, it wasn't that important.” → [gorwath_tmp2](#d-gorwath_tmp2)

    <span id="d-gorwath_letter_20"></span>**`gorwath_letter_20`** Gorwath: “Would you be so kind to give her my letter?” — **effects:** sets stage 10 of [You're the postman](../quests/postman.md#stage-10)

    - “Yeah sure, why not?” → [gorwath_letter_50](#d-gorwath_letter_50)
    - “No I'm busy. Good bye.” → [gorwath_letter_22](#d-gorwath_letter_22)

    <span id="d-gorwath_letter"></span>**`gorwath_letter`** Gorwath: “Hey, Andor!”

    - “I am not Andor. What do you want from him?” → [gorwath_letter_1](#d-gorwath_letter_1)

    <span id="d-gorwath_exit"></span>**`gorwath_exit`** Gorwath: “I will go now and prepare a present for lovely Arensia. When we get married, you will of course be invited.”

    - “OK. Bye.” → [gorwath_exit_1](#d-gorwath_exit_1)

    <span id="d-gorwath_love_1"></span>**`gorwath_love_1`** Gorwath: “That's great! I'm so excited!”

    - Next → [gorwath_love_2](#d-gorwath_love_2)

    <span id="d-gorwath_tmp2"></span>**`gorwath_tmp2`** Gorwath: “Not that important?? I can barely breathe if I don't get her answer! Hurry now! Please, do.”


    <span id="d-gorwath_letter_50"></span>**`gorwath_letter_50`** Gorwath: “Thanks a lot. Here's the letter. Go to Fallhaven and look for Arensia.” — **effects:** sets stage 15 of [You're the postman](../quests/postman.md#stage-15), gives 1× [Gorwath's letter](../items/gorwath_letter.md)

    - “Fallhaven is a big city. How shall I find her?” → [gorwath_letter_52](#d-gorwath_letter_52)

    <span id="d-gorwath_letter_22"></span>**`gorwath_letter_22`** Gorwath: “You really don't want to help me? Then I have no more hope.”

    - “Now, now. Give me your precious letter, I'll do it.” → [gorwath_letter_50](#d-gorwath_letter_50)
    - “Sorry, but I have no time. I have to find my brother now.” → [gorwath_letter_24](#d-gorwath_letter_24)
    - “Grow up and solve your problems yourself. I'm not a postman!” → [gorwath_letter_24](#d-gorwath_letter_24)

    <span id="d-gorwath_letter_1"></span>**`gorwath_letter_1`** Gorwath: “Oh, Andor promised to meet me here. Who are you?”

    - “My name is $playername. I'm looking for my brother too, he has been away for a while now.” → [gorwath_letter_2](#d-gorwath_letter_2)
    - “My name is none of your business. Get out of our property now!” → *conversation ends*

    <span id="d-gorwath_exit_1"></span>**`gorwath_exit_1`** Gorwath: “Before we go our separate ways, please take this ring that I found behind those haystacks over there.” — **effects:** removes monsters from crossglen, gives [Kid's ring](../items/kids_ring.md)


    <span id="d-gorwath_love_2"></span>**`gorwath_love_2`** Gorwath: “You have truly earned these gold pieces.” — **effects:** sets stage 30 of [You're the postman](../quests/postman.md#stage-30), gives 30× [Gold coins](../items/gold.md)

    - “Thank you.” → [gorwath_exit](#d-gorwath_exit)

    <span id="d-gorwath_letter_52"></span>**`gorwath_letter_52`** Gorwath: “She is the daughter of Jakrar the woodcutter, so she will surely live there.”


    <span id="d-gorwath_letter_24"></span>**`gorwath_letter_24`** Gorwath: “Good by then. I will not disturb you anymore. * Sob *” — **effects:** sets stage 12 of [You're the postman](../quests/postman.md#stage-12), removes monsters from crossglen


    <span id="d-gorwath_letter_2"></span>**`gorwath_letter_2`** Gorwath: “Oh dear, oh dear. This is a very personal matter. I don't want everyone to know about it.”

    - “I want to help you since my brother did not. Please tell me what's on your mind.” → [gorwath_letter_3](#d-gorwath_letter_3)
    - “I promise not to tell anyone.” → [gorwath_letter_3](#d-gorwath_letter_3)

    <span id="d-gorwath_letter_3"></span>**`gorwath_letter_3`** Gorwath: “Really? That's very kind of you.”

    - Next → [gorwath_letter_10](#d-gorwath_letter_10)

    <span id="d-gorwath_letter_10"></span>**`gorwath_letter_10`** Gorwath: “You probably don't know me. I am Gorwath. I only recently moved to Crossglen to live with my aunt.”

    - “With Leta?” → [gorwath_letter_11](#d-gorwath_letter_11)

    <span id="d-gorwath_letter_11"></span>**`gorwath_letter_11`** Gorwath: “Yes. You know her? Then you will also know how strict she can be. Sigh.”

    - “Indeed.” → [gorwath_letter_12](#d-gorwath_letter_12)

    <span id="d-gorwath_letter_12"></span>**`gorwath_letter_12`** Gorwath: “I met someone at the last weekly market and I want to send them something.”

    - “Who is he?” → [gorwath_letter_13](#d-gorwath_letter_13)

    <span id="d-gorwath_letter_13"></span>**`gorwath_letter_13`** Gorwath: “To be precise, I have a letter ... for ... a lovely girl.”

    - “Huh?” → [gorwath_letter_14](#d-gorwath_letter_14)

    <span id="d-gorwath_letter_14"></span>**`gorwath_letter_14`** Gorwath: “Yes, she is the most beautiful girl in the world! Her name is Arensia.”

    - “Hm, I don't know anyone here by that name.” → [gorwath_letter_15](#d-gorwath_letter_15)

    <span id="d-gorwath_letter_15"></span>**`gorwath_letter_15`** Gorwath: “Unfortunately she lives in Fallhaven. My aunt would never allow me to go there.”

    - “And how could I help you?” → [gorwath_letter_16](#d-gorwath_letter_16)

    <span id="d-gorwath_letter_16"></span>**`gorwath_letter_16`** Gorwath: “Andor promised to take the letter to her. Maybe you could ...”

    - “I could what?” → [gorwath_letter_20](#d-gorwath_letter_20)



## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 25 lines added |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 1 line changed |
| [v0.8.5](../versions/0.8.5.md) | Dialogue: 2 lines changed<br>· text: “I will go now and prepare a present for lovely Arensia.” → “I will go now and prepare a present for lovely Arensia. When we get m…”<br>· text: “And when we get married, you will of course be invited.” → “Before we go our separate ways, please take this ring that I found be…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `gorwath` |
    | Type (wiki) | NPC |
    | Spawn group | `gorwath` |
    | Loot table | – |
    | Conversation | `gorwath` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:88` |
    | Defined in | `res/raw/monsterlist_gorwath.json` |

    Raw data:

    ```json
    {
     "id": "gorwath",
     "name": "Gorwath",
     "iconID": "monsters_ld1:88",
     "monsterClass": "humanoid",
     "spawnGroup": "gorwath",
     "phraseID": "gorwath"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gorwath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gorwath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gorwath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gorwath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
