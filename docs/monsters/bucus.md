---
description: "Bucus is a non-player character (NPC) in Andor's Trail. Starts Key of Luthor."
---

# ![](../assets/icons/monsters/monsters_rogue1_0.png){ .sprite } Bucus

**Where to find Bucus:** appears during a quest or scripted event.

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rogue1_0.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Starts [Key of Luthor](../quests/bucus.md) |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Key of Luthor](../quests/bucus.md): stages 10, 100
- [Search for Andor](../quests/andor.md): stage 50

## Dialogue simulator

Talk to Bucus as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/bucus_welcome.json" data-npc="Bucus" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (18 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-bucus_welcome"></span>**`bucus_welcome`** Bucus: “Hi again, welcome back to the ... Oh wait, I thought you were someone else.”

    - “Have you seen my brother Andor?” → [bucus_andor_select](#d-bucus_andor_select)
    - “What do you know about the Thieves' Guild?” → [bucus_thieves_select](#d-bucus_thieves_select)

    <span id="d-bucus_andor_select"></span>**`bucus_andor_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Key of Luthor](../quests/bucus.md#stage-100))* → [bucus_umar_1](#d-bucus_umar_1)
    - branch 2 → [bucus_andor_no_1](#d-bucus_andor_no_1)

    <span id="d-bucus_thieves_select"></span>**`bucus_thieves_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Key of Luthor](../quests/bucus.md#stage-100))* → [bucus_thieves_complete_3](#d-bucus_thieves_complete_3)
    - branch 2 *(if reached stage 10 of [Key of Luthor](../quests/bucus.md#stage-10))* → [bucus_thieves_continue](#d-bucus_thieves_continue)
    - branch 3 → [bucus_thieves_select2](#d-bucus_thieves_select2)

    <span id="d-bucus_umar_1"></span>**`bucus_umar_1`** Bucus: “OK kid. You've proven yourself to me. Yes, I saw some other kid by that description running around here a few days ago.”

    - Next → [bucus_umar_2](#d-bucus_umar_2)

    <span id="d-bucus_andor_no_1"></span>**`bucus_andor_no_1`** Bucus: “How interesting that you should ask. What if I had seen him? Why would I tell you?”

    - Next → [bucus_andor_no_2](#d-bucus_andor_no_2)

    <span id="d-bucus_thieves_complete_3"></span>**`bucus_thieves_complete_3`** Bucus: “So, let's talk. What do you want to know?”

    - “What do you know about my brother Andor?” → [bucus_umar_1](#d-bucus_umar_1)

    <span id="d-bucus_thieves_continue"></span>**`bucus_thieves_continue`** Bucus: “How is the search for the key of Luthor going?”

    - “What was I supposed to do again?” → [bucus_thieves_4](#d-bucus_thieves_4)
    - “Here, I have it. The key of Luthor.” *(if hand over 1× [Key of Luthor](../items/key_luthor.md))* → [bucus_thieves_complete_1](#d-bucus_thieves_complete_1)
    - “I'm still looking for it. Bye.” → *conversation ends*

    <span id="d-bucus_thieves_select2"></span>**`bucus_thieves_select2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 40 of [Search for Andor](../quests/andor.md#stage-40))* → [bucus_thieves_1](#d-bucus_thieves_1)
    - branch 2 → [bucus_thieves_no](#d-bucus_thieves_no)

    <span id="d-bucus_umar_2"></span>**`bucus_umar_2`** Bucus: “I don't know what he was up to though. He kept asking a lot of questions. Kind of like you do. *snicker*”

    - Next → [bucus_umar_3](#d-bucus_umar_3)

    <span id="d-bucus_andor_no_2"></span>**`bucus_andor_no_2`** Bucus: “No, I can't tell you. Now please leave.”


    <span id="d-bucus_thieves_4"></span>**`bucus_thieves_4`** Bucus: “Bring me the key of Luthor and we can talk more. I don't know anything about the key itself, but rumor has it that it is located somewhere in the catacombs beneath Fallhaven Church.” — **effects:** sets stage 10 of [Key of Luthor](../quests/bucus.md#stage-10)

    - “OK, sounds easy enough.” → *conversation ends*

    <span id="d-bucus_thieves_complete_1"></span>**`bucus_thieves_complete_1`** Bucus: “Wow, you actually got the key of Luthor? I didn't think you would make it out of there.” — **effects:** sets stage 100 of [Key of Luthor](../quests/bucus.md#stage-100)

    - Next → [bucus_thieves_complete_2](#d-bucus_thieves_complete_2)

    <span id="d-bucus_thieves_1"></span>**`bucus_thieves_1`** Bucus: “Who told you that? Argh. OK so you found us. Now what?”

    - “Can I join the Thieves' Guild?” → [bucus_thieves_2](#d-bucus_thieves_2)

    <span id="d-bucus_thieves_no"></span>**`bucus_thieves_no`** Bucus: “Wh, what? No, I don't know anything about that.”


    <span id="d-bucus_umar_3"></span>**`bucus_umar_3`** Bucus: “Anyway, that's all I know. You should go talk to Umar, he probably knows more. Down that hatch over there.” — **effects:** sets stage 50 of [Search for Andor](../quests/andor.md#stage-50)

    - “OK, bye.” → *conversation ends*

    <span id="d-bucus_thieves_complete_2"></span>**`bucus_thieves_complete_2`** Bucus: “Well done kid.”

    - Next → [bucus_thieves_complete_3](#d-bucus_thieves_complete_3)

    <span id="d-bucus_thieves_2"></span>**`bucus_thieves_2`** Bucus: “Hah! Join the Thieves' Guild?! You?! You're one funny kid.”

    - “I'm serious.” → [bucus_thieves_3](#d-bucus_thieves_3)
    - “Yeah, pretty funny eh?” → [bucus_thieves_3](#d-bucus_thieves_3)

    <span id="d-bucus_thieves_3"></span>**`bucus_thieves_3`** Bucus: “OK, tell you what kid. Do a task for me and maybe I'll consider giving you more info.”

    - “What kind of task are we talking about?” → [bucus_thieves_4](#d-bucus_thieves_4)
    - “As long as this leads to some treasure, I'm in!” → [bucus_thieves_4](#d-bucus_thieves_4)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 9 lines changed<br>· text: “Ok, tell you what kid. Do a task for me and maybe I'll consider givin…” → “OK, tell you what kid. Do a task for me and maybe I'll consider givin…”<br>· text: “Hi again, welcome back to the .. Oh wait, I thought you were someone …” → “Hi again, welcome back to the ... Oh wait, I thought you were someone…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `bucus` |
    | Type (wiki) | NPC |
    | Spawn group | `bucus` |
    | Loot table | – |
    | Conversation | `bucus_welcome` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rogue1:0` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "bucus",
     "name": "Bucus",
     "iconID": "monsters_rogue1:0",
     "monsterClass": "humanoid",
     "spawnGroup": "bucus",
     "phraseID": "bucus_welcome"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bucus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bucus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bucus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bucus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
