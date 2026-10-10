---
description: "Moriath is a non-player character (NPC) in Andor's Trail, found in Lake Laeroth. Starts Take care of the caretaker."
---

# ![](../assets/icons/monsters/monsters_rltiles1_74.png){ .sprite } Moriath

**Where to find Moriath:** Lake Laeroth: [Laerothmanor 1](../maps/laerothmanor1.md#pin-npc-moriath)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles1_74.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Starts [Take care of the caretaker](../quests/laeroth_caretaker.md) |
| **Found in** | Lake Laeroth |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

## Quests

- [Take care of the caretaker](../quests/laeroth_caretaker.md): stages 10, 15, 17, 35, 50, 180
- [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md): stage 120

## Dialogue simulator

Talk to Moriath as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/moriath_selector.json" data-npc="Moriath" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (29 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-moriath_selector"></span>**`moriath_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-10))* → [moriath_1_0](#d-moriath_1_0)
    - branch 2 → [moriath_0](#d-moriath_0)

    <span id="d-moriath_1_0"></span>**`moriath_1_0`** Moriath: “Hello again.”

    - “Finally, success. I had to raise the spirits of many family members, but Jerelin said he would release you from the…” *(if reached stage 170 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-170))* → [moriath_9_1](#d-moriath_9_1)
    - “Audela told me to talk again to her husband Jerelin. I think I don't need another of Jerelin's items again. His seal…” *(if reached stage 160 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-160); NOT reached stage 170 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-170))* → [moriath_7_1](#d-moriath_7_1)
    - “Cuned now sent me to his mother Audela. Where are Audela's item?” *(if reached stage 120 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-120); NOT reached stage 130 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-130))* → [moriath_6_1](#d-moriath_6_1)
    - “Jerelin was not helpful. In fact, he just ignored me.” *(if reached stage 110 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-110); NOT reached stage 120 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-120))* → [moriath_5_1](#d-moriath_5_1)
    - “Cuned has sent me to talk to his father Jerelin. Now I need a personal item of him” *(if reached stage 90 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-90); NOT reached stage 110 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-110))* → [moriath_4_1](#d-moriath_4_1)
    - “I spoke to the spirit of Eyvipa. Even now he was extremely displeased at being passed over in favor of Cuned in the…” *(if reached stage 70 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-70); NOT reached stage 90 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-90))* → [moriath_3_1](#d-moriath_3_1)
    - “I spoke to the spirit of Verigil, but he told me he cannot help. I must speak to his uncle, Eyvipa. So I need a…” *(if reached stage 40 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-40); NOT reached stage 70 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-70))* → [moriath_2_1](#d-moriath_2_1)
    - “I have found how to raise a spirit and talk to it. However, I need a personal item from the deceased.” *(if reached stage 30 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-30); NOT reached stage 40 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-40))* → [moriath_1_1](#d-moriath_1_1)
    - “Can you tell me about this place?” → [moriath_history_2](#d-moriath_history_2)
    - “Can you tell me again why you are still here?” *(if NOT reached stage 30 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-30))* → [moriath_caretaker_2](#d-moriath_caretaker_2)
    - “I have to leave to look for my brother.” *(if NOT reached stage 20 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-20))* → *conversation ends*

    <span id="d-moriath_0"></span>**`moriath_0`** Moriath: “Hello. It's so very long since I have seen another person. Who are you, and why are you here?”

    - “I'm $playername. I'm looking for my brother, Andor. Have you seen him?” → [moriath_1](#d-moriath_1)

    <span id="d-moriath_9_1"></span>**`moriath_9_1`** Moriath: “Thank you. I will do that if it releases me from the oath. I will do it immediately. Farewell, and thanks again.” — **effects:** removes monsters from laerothmanor1, sets stage 180 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-180), sets stage 120 of [Laeroth story flags (hidden flag)](../quests/laeroth_nondisplay.md#stage-120)

    - Next → *NPC leaves*

    <span id="d-moriath_7_1"></span>**`moriath_7_1`** Moriath: “Yes, probably you are right.”


    <span id="d-moriath_6_1"></span>**`moriath_6_1`** Moriath: “Audela has always an "A" as intials on her personal items. They should be easy to find.”


    <span id="d-moriath_5_1"></span>**`moriath_5_1`** Moriath: “Maybe it helps if you talk to Cuned again?”

    - “Hmm, I could try that.” → *conversation ends*

    <span id="d-moriath_4_1"></span>**`moriath_4_1`** Moriath: “Jerelin has put a "J" as intials on his personal items. Please look for it yourself.”


    <span id="d-moriath_3_1"></span>**`moriath_3_1`** Moriath: “Cuned has put a "C" as intials on his personal items. Please look for it yourself.”

    - “Thanks. Will do!” → *conversation ends*

    <span id="d-moriath_2_1"></span>**`moriath_2_1`** Moriath: “There are items from all the generations scattered around. They were fond of putting their intials on them. A mixture of vanity and possessiveness I think. So see if you can find something with "E" marked on it.” — **effects:** sets stage 50 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-50)

    - “Thanks. Will do!” → *conversation ends*

    <span id="d-moriath_1_1"></span>**`moriath_1_1`** Moriath: “Well, the previous lord was Verigil. His son, Adakin, did not take any of his fathers possesions when he left. You might find something in the master bedroom.” — **effects:** sets stage 35 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-35)

    - “Thanks!” → *conversation ends*

    <span id="d-moriath_history_2"></span>**`moriath_history_2`** Moriath: “Laeroth manor? Yes, of course.”

    - Next → [moriath_history_3](#d-moriath_history_3)

    <span id="d-moriath_caretaker_2"></span>**`moriath_caretaker_2`** Moriath: “I am bound by an oath to take care of the manor. It is not an oath I ever gave though. I cannot care for everything of course. I take care of the main house, the bridges, and tend to the graves as best I can. Everything else has gradually…” — **effects:** sets stage 10 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-10)

    - “How can you be bound by an oath you never gave?” → [moriath_caretaker_3](#d-moriath_caretaker_3)

    <span id="d-moriath_1"></span>**`moriath_1`** Moriath: “No. I just told you that you are the first person I have seen here in a very long time. Getting to the old manor is difficult and dangerous, and there is nothing here. So why would anyone come here?”

    - “So why are you here?” → [moriath_caretaker_1](#d-moriath_caretaker_1)
    - “What is this place?” → [moriath_history_1](#d-moriath_history_1)
    - “I guess I'll be going then.” → *conversation ends*

    <span id="d-moriath_history_3"></span>**`moriath_history_3`** Moriath: “Many years ago, this island was used as a refuge in times of danger by communities that lived on the lakeshore. There was little here other than a small fortification, but being an island, that was enough for protection.”

    - Next → [moriath_history_4](#d-moriath_history_4)

    <span id="d-moriath_caretaker_3"></span>**`moriath_caretaker_3`** Moriath: “It is a matter of honor. The Lord of the manor saved my great-great grandfather from certain death many years ago. In return my great-great grandfather vowed that his family would always look after the manor.” — **effects:** sets stage 15 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-15)

    - “He should not have made a vow that bound his family for generations!” → [moriath_caretaker_4](#d-moriath_caretaker_4)
    - “Well, that's too bad for you. I need to get going. I have to find my brother.” → *conversation ends*

    <span id="d-moriath_caretaker_1"></span>**`moriath_caretaker_1`** Moriath: “I am Moriath, the caretaker for this manor.”

    - “What is this place?” → [moriath_history_1](#d-moriath_history_1)
    - “Can you tell me more about this place?” → [moriath_history_2](#d-moriath_history_2)
    - “If there is nobody else here, why do you stay?” → [moriath_caretaker_2](#d-moriath_caretaker_2)

    <span id="d-moriath_history_1"></span>**`moriath_history_1`** Moriath: “This is Laeroth manor. Or what is left of it, anyway.”

    - “What are you doing here?” → [moriath_caretaker_1](#d-moriath_caretaker_1)
    - “Can you tell me more about this place?” → [moriath_history_2](#d-moriath_history_2)

    <span id="d-moriath_history_4"></span>**`moriath_history_4`** Moriath: “Then a man by the name of Laeroth, along with a group of followers, declared himself the Lord of Laeroth, and took the fortifications and the island as his own.”

    - Next → [moriath_history_5](#d-moriath_history_5)

    <span id="d-moriath_caretaker_4"></span>**`moriath_caretaker_4`** Moriath: “I do not disagree, but he did.”

    - “Is there something I can do to help?” → [moriath_caretaker_5](#d-moriath_caretaker_5)
    - “Too bad. Look on the bright side though. You have an entire manor to yourself. Bye.” → *conversation ends*

    <span id="d-moriath_history_5"></span>**`moriath_history_5`** Moriath: “For many years his family continued to provide refuge to those that lived on the shore, and they even built a watchtower on the mountain to the south, as a lookout for approaching enemies. In return, the manor was provided with supplies.”

    - “Interesting. Please continue.” → [moriath_history_6](#d-moriath_history_6)
    - “Maybe I shouldn't have asked. This is getting boring. I need to leave, and look for my brother.” → *conversation ends*

    <span id="d-moriath_caretaker_5"></span>**`moriath_caretaker_5`** Moriath: “The only thing that would help is for me to be released from the oath.”

    - “Who can do that?” → [moriath_caretaker_6](#d-moriath_caretaker_6)

    <span id="d-moriath_history_6"></span>**`moriath_history_6`** Moriath: “The fall of the manor began when the shore folk, led by a man called Korhald, built a bridge to an island, and founded the city of Remgard.”

    - Next → [moriath_history_6a](#d-moriath_history_6a)

    <span id="d-moriath_caretaker_6"></span>**`moriath_caretaker_6`** Moriath: “The current lord, of course. But he has gone. I do not know his whereabouts, or even if he is still alive. If I knew he was deceased I would consider the oath void, but I do not know that.”

    - “There is nobody else?” → [moriath_caretaker_7](#d-moriath_caretaker_7)

    <span id="d-moriath_history_6a"></span>**`moriath_history_6a`** Moriath: “They admired Korhald because without him the city of Remgard would not exist, but he was not well liked. He ruled the city like an oppressive king. When he died the cityfolk built a tomb in his honor, but well away from Remgard. Somewhere…”

    - Next → [moriath_history_7](#d-moriath_history_7)

    <span id="d-moriath_caretaker_7"></span>**`moriath_caretaker_7`** Moriath: “Any of the past lords Laeroth could release me from the oath. But, like my great-great grandfather, they are long dead. Their graves are in the tomb on the far island. So unless you can talk to the dead, they will be of no help.”

    - “How can I talk to the dead?” → [moriath_caretaker_8](#d-moriath_caretaker_8)

    <span id="d-moriath_history_7"></span>**`moriath_history_7`** Moriath: “Anyway, Remgard was far from any enemies, and easily defended, so the islands in the lake were no longer important, and the supplies stopped coming.”

    - Next → [moriath_history_8](#d-moriath_history_8)

    <span id="d-moriath_caretaker_8"></span>**`moriath_caretaker_8`** Moriath: “I have no idea. I am a caretaker, not a priest. The manor has an extensive library. Maybe you should look there.” — **effects:** sets stage 17 of [Take care of the caretaker](../quests/laeroth_caretaker.md#stage-17)

    - “I'll take a look.” → *conversation ends*
    - “That sounds like a lot of work, and I need to go and find my brother.” → *conversation ends*

    <span id="d-moriath_history_8"></span>**`moriath_history_8`** Moriath: “With no place to grow food on the islands most of the staff left. The last lord that resided here had only one son, and when the lord died his son abandoned the manor and left to look for other opportunities.”

    - “So if the son has left, why do you stay here?” → [moriath_caretaker_2](#d-moriath_caretaker_2)
    - “Thanks for the history lesson. I need to leave, and look for my brother.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added<br>Dialogue: 29 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `moriath` |
    | Type (wiki) | NPC |
    | Spawn group | `moriath` |
    | Loot table | – |
    | Conversation | `moriath_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles1:74` |
    | Defined in | `res/raw/monsterlist_laeroth.json` |

    Raw data:

    ```json
    {
     "id": "moriath",
     "name": "Moriath",
     "iconID": "monsters_rltiles1:74",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "moriath_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=moriath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=moriath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=moriath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=moriath.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
