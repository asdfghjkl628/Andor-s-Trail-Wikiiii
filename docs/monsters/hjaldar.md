---
description: "Hjaldar is a non-player character (NPC) in Andor's Trail, found in Remgard. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_rltiles1_70.png){ .sprite } Hjaldar

**Where to find Hjaldar:** Remgard: [remgard_villager1](../maps/remgard_villager1.md#pin-npc-hjaldar)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_70.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper |
| **Found in** | Remgard |
| **Entry ID** | `hjaldar` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Potion of damage focus](../items/pot_focus_dmg.md) | 100% | 8 |
| [Potion of accuracy focus](../items/pot_focus_ac.md) | 100% | 8 |
| [Strong potion of damage focus](../items/pot_focus_dmg2.md) | 100% | 5 |
| [Strong potion of accuracy focus](../items/pot_focus_ac2.md) | 100% | 5 |

## Quests

- [A difference of opinion](../quests/sisterfight.md): stages 40, 41, 45, 60, 61

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Hjaldar. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/hjaldar.json" data-npc="Hjaldar" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (32 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-hjaldar"></span>**`hjaldar`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 61 of [A difference of opinion](../quests/sisterfight.md#stage-61))* → [hjaldar_pots_1](#d-hjaldar_pots_1)
    - branch 2 *(if reached stage 60 of [A difference of opinion](../quests/sisterfight.md#stage-60))* → [hjaldar_r3](#d-hjaldar_r3)
    - branch 3 *(if reached stage 45 of [A difference of opinion](../quests/sisterfight.md#stage-45))* → [hjaldar_r1](#d-hjaldar_r1)
    - branch 4 *(if reached stage 40 of [A difference of opinion](../quests/sisterfight.md#stage-40))* → [hjaldar_7r](#d-hjaldar_7r)
    - branch 5 → [hjaldar_1](#d-hjaldar_1)

    <span id="d-hjaldar_pots_1"></span>**`hjaldar_pots_1`** Hjaldar: “Thanks for contacting Mazeg for me earlier. With this Lyson marrow extract that you brought me, I can now make other potions for you if you want.”

    - “Let me see what potions you have.” → *shop opens*
    - “You are welcome, goodbye.” → *conversation ends*

    <span id="d-hjaldar_r3"></span>**`hjaldar_r3`** Hjaldar: “Thanks for bringing me some of that marrow extract. Nice work finding it!”

    - Next → [hjaldar_r4](#d-hjaldar_r4)

    <span id="d-hjaldar_r1"></span>**`hjaldar_r1`** Hjaldar: “Hello again. Did you find my old friend Mazeg?”

    - “Yes, I brought you some Lyson marrow extract.” *(if hand over 1× [Vial of Lyson marrow extract](../items/lyson_marrow.md))* → [hjaldar_r2](#d-hjaldar_r2)
    - “What was that you were saying about those potions of accuracy focus?” → [hjaldar_6](#d-hjaldar_6)
    - “What made you stop making potions?” → [hjaldar_4](#d-hjaldar_4)
    - “Any ideas on where I might find Mazeg?” → [hjaldar_12](#d-hjaldar_12)

    <span id="d-hjaldar_7r"></span>**`hjaldar_7r`** Hjaldar: “Hello again. Sorry about not being able to help you with those potions of accuracy focus that you asked for.”

    - Next → [hjaldar_7](#d-hjaldar_7)

    <span id="d-hjaldar_1"></span>**`hjaldar_1`** Hjaldar: “Hello there. I am Hjaldar.”

    - “What do you do here?” → [hjaldar_2](#d-hjaldar_2)

    <span id="d-hjaldar_r4"></span>**`hjaldar_r4`** Hjaldar: “Tell me, did you find Mazeg or did you get it from somewhere else?”

    - “I visited Mazeg up in the Blackwater mountain settlement.” → [hjaldar_r5](#d-hjaldar_r5)
    - “You made me run all the way to Blackwater mountain, I sure hope those potions are worth it!” → [hjaldar_r5](#d-hjaldar_r5)

    <span id="d-hjaldar_r2"></span>**`hjaldar_r2`** Hjaldar: “Oh wow. Yes, this is indeed some of that marrow extract. Nice work finding it!” — **effects:** sets stage 60 of [A difference of opinion](../quests/sisterfight.md#stage-60)

    - Next → [hjaldar_r4](#d-hjaldar_r4)

    <span id="d-hjaldar_6"></span>**`hjaldar_6`** Hjaldar: “Oh, potions of accuracy focus. Yes, those were popular. Unfortunately, I can't help you with that now.”

    - Next → [hjaldar_7](#d-hjaldar_7)

    <span id="d-hjaldar_4"></span>**`hjaldar_4`** Hjaldar: “Well, two things. Firstly, I am getting older and don't have the desire to be working full days, making potions for gold.”

    - Next → [hjaldar_5](#d-hjaldar_5)

    <span id="d-hjaldar_12"></span>**`hjaldar_12`** Hjaldar: “No, I don't know. Last time I saw him, he was headed west. From the looks of his backpack, it looked like he was getting ready for quite a long trip to the west.”

    - Next → [hjaldar_13](#d-hjaldar_13)

    <span id="d-hjaldar_7"></span>**`hjaldar_7`** Hjaldar: “My supply of Lyson marrow extract has gone dry. Without some of that, I can't make potions that are useful for anything really.” — **effects:** sets stage 40 of [A difference of opinion](../quests/sisterfight.md#stage-40)

    - “Too bad. Thanks anyway. Goodbye.” → *conversation ends*
    - “Is there somewhere I can get some, and bring it to you?” → [hjaldar_8](#d-hjaldar_8)

    <span id="d-hjaldar_2"></span>**`hjaldar_2`** Hjaldar: “I used to be a potion-maker. In fact, I used to be the only potion-maker here in Remgard.”

    - Next → [hjaldar_3](#d-hjaldar_3)

    <span id="d-hjaldar_r5"></span>**`hjaldar_r5`** Hjaldar: “Blackwater mountain? I'm afraid I don't know where that is. Never mind, I hope that all is well with my old friend.”

    - “He told me to send you his warmest greetings.” → [hjaldar_r6](#d-hjaldar_r6)
    - “He seemed like a pitiful old man that has seen the best of his days.” → [hjaldar_r7](#d-hjaldar_r7)

    <span id="d-hjaldar_5"></span>**`hjaldar_5`** Hjaldar: “Secondly, I ran out of most of the ingredients. Some of them are really hard to get.”

    - “Too bad. Nice talking to you, goodbye.” → *conversation ends*
    - “I am looking for a potion of accuracy focus for the Elwille sisters, can you help with that?” *(if reached stage 31 of [A difference of opinion](../quests/sisterfight.md#stage-31))* → [hjaldar_6](#d-hjaldar_6)

    <span id="d-hjaldar_13"></span>**`hjaldar_13`** Hjaldar: “He even had gear for travelling through colder climates - snow and ice and that sort of thing.” — **effects:** sets stage 41 of [A difference of opinion](../quests/sisterfight.md#stage-41)

    - “Thanks for the info. I will try to find him.” → [hjaldar_14](#d-hjaldar_14)
    - “This sounds like too much trouble. Never mind that potion.” → [hjaldar_11](#d-hjaldar_11)

    <span id="d-hjaldar_8"></span>**`hjaldar_8`** Hjaldar: “I doubt that. It is really hard to find. Only the most well-stocked potion-makers have it.”

    - Next → [hjaldar_9](#d-hjaldar_9)

    <span id="d-hjaldar_3"></span>**`hjaldar_3`** Hjaldar: “That was good business. People even travelled here from other cities down the mountain.”

    - “What made you stop?” → [hjaldar_4](#d-hjaldar_4)

    <span id="d-hjaldar_r6"></span>**`hjaldar_r6`** Hjaldar: “Good. Good. I am glad to hear he is well.”

    - Next → [hjaldar_r8](#d-hjaldar_r8)

    <span id="d-hjaldar_r7"></span>**`hjaldar_r7`** Hjaldar: “Time has not been on his side, I see.”

    - Next → [hjaldar_r8](#d-hjaldar_r8)

    <span id="d-hjaldar_14"></span>**`hjaldar_14`** Hjaldar: “Good luck finding him. If you do find him, which I doubt you do, please say hello to him from me, and tell him that I am well.” — **effects:** sets stage 45 of [A difference of opinion](../quests/sisterfight.md#stage-45)


    <span id="d-hjaldar_11"></span>**`hjaldar_11`** Hjaldar: “OK then. Sorry I couldn't help you. Goodbye.”


    <span id="d-hjaldar_9"></span>**`hjaldar_9`** Hjaldar: “I used to get my supply from my old friend Mazeg. I have no idea where he might be these days though.”

    - Next → [hjaldar_10](#d-hjaldar_10)

    <span id="d-hjaldar_r8"></span>**`hjaldar_r8`** Hjaldar: “Anyway. Let's make that potion that you asked for earlier. I even prepared the other ingredients for another potion beforehand.”

    - Next → [hjaldar_r9](#d-hjaldar_r9)

    <span id="d-hjaldar_10"></span>**`hjaldar_10`** Hjaldar: “I guess, if you can find him, he might be able to provide you with some Lyson marrow extract.”

    - “Any ideas on where I might find him?” → [hjaldar_12](#d-hjaldar_12)
    - “This sounds like too much trouble. Never mind that potion.” → [hjaldar_11](#d-hjaldar_11)

    <span id="d-hjaldar_r9"></span>**`hjaldar_r9`** Hjaldar: “Now, let's see. Some of these... [Hjaldar pulls out some dried up berries and puts them in his mortar]”

    - Next → [hjaldar_r10](#d-hjaldar_r10)

    <span id="d-hjaldar_r10"></span>**`hjaldar_r10`** Hjaldar: “Add some of this into some clean vials...”

    - Next → [hjaldar_r11](#d-hjaldar_r11)

    <span id="d-hjaldar_r11"></span>**`hjaldar_r11`** Hjaldar: “Just a pinch of these into one of these vials...”

    - Next → [hjaldar_r12](#d-hjaldar_r12)

    <span id="d-hjaldar_r12"></span>**`hjaldar_r12`** Hjaldar: “Finally, the Lyson marrow extract...”

    - Next → [hjaldar_r13](#d-hjaldar_r13)

    <span id="d-hjaldar_r13"></span>**`hjaldar_r13`** Hjaldar: “There. Now we just need to give them a good shake.”

    - Next → [hjaldar_r14](#d-hjaldar_r14)

    <span id="d-hjaldar_r14"></span>**`hjaldar_r14`** Hjaldar: “[Hjaldar shakes the vials vigorously, one in each of his hands]”

    - Next → [hjaldar_r15](#d-hjaldar_r15)

    <span id="d-hjaldar_r15"></span>**`hjaldar_r15`** Hjaldar: “Ah, that should do it. Here you go. One potion of accuracy focus and one potion of damage focus. I hope they will be useful to you.” — **effects:** sets stage 61 of [A difference of opinion](../quests/sisterfight.md#stage-61), gives [Potion of damage focus](../items/pot_focus_dmg.md), [Potion of accuracy focus](../items/pot_focus_ac.md)

    - “Thank you.” → *conversation ends*
    - “Whatever. I sure hope all this work is worth it!” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 10 lines changed<br>· text: “Ok then. Sorry I couldn't help you. Goodbye.” → “OK then. Sorry I couldn't help you. Goodbye.”<br>· text: “Blackwater Mountain? I'm afraid I don't know where that is. Never min…” → “Blackwater mountain? I'm afraid I don't know where that is. Never min…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `hjaldar` |
    | Spawn group | `hjaldar` |
    | Loot table | `shop_hjaldar` |
    | Conversation | `hjaldar` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:70` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "hjaldar",
     "name": "Hjaldar",
     "iconID": "monsters_rltiles1:70",
     "monsterClass": "humanoid",
     "spawnGroup": "hjaldar",
     "phraseID": "hjaldar",
     "droplistID": "shop_hjaldar"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hjaldar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hjaldar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hjaldar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hjaldar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
