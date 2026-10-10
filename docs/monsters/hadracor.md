---
description: "Hadracor is a non-player character (NPC) in Andor's Trail, found in Crossroads Guardhouse. Shopkeeper; starts Devastated land."
---

# ![](../assets/icons/monsters/monsters_men2_2.png){ .sprite } Hadracor

**Where to find Hadracor:** Crossroads Guardhouse: [Roadtocarntower 1](../maps/roadtocarntower1.md#pin-npc-hadracor)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_men2_2.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper; starts [Devastated land](../quests/hadracor.md) |
| **Found in** | Crossroads Guardhouse |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Woodcutter's axe](../items/axe1.md) | 100% | 1 |
| [Woodcutter's hatchet](../items/woodcutter_hatchet.md) | 100% | 1 |
| [Gutsplitter](../items/axe_gutsplitter.md) | 100% | 1 |
| [Skullcrusher](../items/hammer_skullcrusher.md) | 100% | 1 |
| [Reinforced black axe](../items/axe_black2.md) | 100% | 1 |
| [Black greataxe](../items/graxe_black.md) | 100% | 1 |
| [Crude leather armor](../items/armour_crude_leather.md) | 100% | 1 |
| [Rigid leather armor](../items/armour_rigid_leather.md) | 100% | 1 |
| [Leather gloves](../items/gloves1.md) | 100% | 1 |
| [Woodcutter's gloves](../items/gloves_woodcutter.md) | 100% | 1 |
| [Woodcutter's boots](../items/woodcutter_boots.md) | 100% | 1 |

## Quests

- [Devastated land](../quests/hadracor.md): stages 10, 20, 21, 30
- [It makes no fence](../quests/tunlon_fence.md): stages 30, 32

## Dialogue simulator

Talk to Hadracor as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/hadracor.json" data-npc="Hadracor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (37 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-hadracor"></span>**`hadracor`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Devastated land](../quests/hadracor.md#stage-30))* → [hadracor_complete_1](#d-hadracor_complete_1)
    - branch 2 *(if reached stage 21 of [Devastated land](../quests/hadracor.md#stage-21))* → [hadracor_gaveitems_1](#d-hadracor_gaveitems_1)
    - branch 3 *(if reached stage 20 of [Devastated land](../quests/hadracor.md#stage-20))* → [hadracor_gaveitems_1](#d-hadracor_gaveitems_1)
    - branch 4 *(if reached stage 10 of [Devastated land](../quests/hadracor.md#stage-10))* → [hadracor_wantsitems_1](#d-hadracor_wantsitems_1)
    - branch 5 → [hadracor_1](#d-hadracor_1)

    <span id="d-hadracor_complete_1"></span>**`hadracor_complete_1`** Hadracor: “Hello again. Thank you for your help with those wasps earlier.”

    - Next → [hadracor_complete_2](#d-hadracor_complete_2)

    <span id="d-hadracor_gaveitems_1"></span>**`hadracor_gaveitems_1`** Hadracor: “Well done my friend. Thank you for getting revenge on those things.”

    - Next → [hadracor_complete_2](#d-hadracor_complete_2)

    <span id="d-hadracor_wantsitems_1"></span>**`hadracor_wantsitems_1`** Hadracor: “Hello again. Did you kill those wasps for us?”

    - “Could you tell me your story again?” → [hadracor_story_2](#d-hadracor_story_2)
    - “What was I supposed to do again?” → [hadracor_story_6](#d-hadracor_story_6)
    - “Not yet, but I am working on it.” → [hadracor_accept_3](#d-hadracor_accept_3)
    - “Yes, I killed six of them.” *(if hand over 6× [Giant wasp wing](../items/hadracor_waspwing.md))* → [hadracor_wantsitems_3](#d-hadracor_wantsitems_3)
    - “Yes, I killed five of them.” *(if hand over 5× [Giant wasp wing](../items/hadracor_waspwing.md))* → [hadracor_wantsitems_2](#d-hadracor_wantsitems_2)
    - “No, but I wanted to ask if you have some spare wood to make fences out of.” *(if reached stage 20 of [It makes no fence](../quests/tunlon_fence.md#stage-20); NOT reached stage 30 of [It makes no fence](../quests/tunlon_fence.md#stage-30))* → [hadracor_fence_1](#d-hadracor_fence_1)
    - “No, I'm too busy running up and down Blackwater mountain.” *(if reached stage 30 of [It makes no fence](../quests/tunlon_fence.md#stage-30); NOT reached stage 32 of [It makes no fence](../quests/tunlon_fence.md#stage-32))* → [hadracor_fence_2](#d-hadracor_fence_2)

    <span id="d-hadracor_1"></span>**`hadracor_1`** Hadracor: “Hello there, I am Hadracor.”

    - “What is this place?” → [hadracor_story_1](#d-hadracor_story_1)
    - “Have you seen my brother Andor around here? Looks somewhat like me.” → [hadracor_andor_1](#d-hadracor_andor_1)
    - “Do you by any chance have some spare wood to make fences out of?” *(if reached stage 20 of [It makes no fence](../quests/tunlon_fence.md#stage-20); NOT reached stage 30 of [It makes no fence](../quests/tunlon_fence.md#stage-30))* → [hadracor_fence_1](#d-hadracor_fence_1)
    - “I'm $playername, running up and down Blackwater mountain for errands.” *(if reached stage 30 of [It makes no fence](../quests/tunlon_fence.md#stage-30); NOT reached stage 32 of [It makes no fence](../quests/tunlon_fence.md#stage-32))* → [hadracor_fence_2](#d-hadracor_fence_2)

    <span id="d-hadracor_complete_2"></span>**`hadracor_complete_2`** Hadracor: “As a token of our appreciation, we are willing to trade some of our equipment with you if you want.” — **effects:** sets stage 30 of [Devastated land](../quests/hadracor.md#stage-30)

    - Next → [hadracor_complete_3](#d-hadracor_complete_3)

    <span id="d-hadracor_story_2"></span>**`hadracor_story_2`** Hadracor: “Our orders were to cut down all trees south of the Feygard bridge and north of this here road to Carn Tower.”

    - Next → [hadracor_story_3](#d-hadracor_story_3)

    <span id="d-hadracor_story_6"></span>**`hadracor_story_6`** Hadracor: “You see, there were these really nasty wasps in that forest we cut down.”

    - Next → [hadracor_story_7](#d-hadracor_story_7)

    <span id="d-hadracor_accept_3"></span>**`hadracor_accept_3`** Hadracor: “Good, hurry back once you are done.” — **effects:** sets stage 10 of [Devastated land](../quests/hadracor.md#stage-10)


    <span id="d-hadracor_wantsitems_3"></span>**`hadracor_wantsitems_3`** Hadracor: “Wow, you actually killed six of those things? I thought there were only five, so I guess I should be even more grateful. Here, take these gloves as thanks.” — **effects:** sets stage 21 of [Devastated land](../quests/hadracor.md#stage-21), gives [Woodcutter's gloves](../items/gloves_woodcutter.md)

    - Next → [hadracor_gaveitems_1](#d-hadracor_gaveitems_1)

    <span id="d-hadracor_wantsitems_2"></span>**`hadracor_wantsitems_2`** Hadracor: “Wow, you actually killed those things?” — **effects:** sets stage 20 of [Devastated land](../quests/hadracor.md#stage-20)

    - Next → [hadracor_gaveitems_1](#d-hadracor_gaveitems_1)

    <span id="d-hadracor_fence_1"></span>**`hadracor_fence_1`** Hadracor: “Oh we do have a lot of wood indeed. However, all of this is very brittle and can only be used as firewood.” — **effects:** sets stage 30 of [It makes no fence](../quests/tunlon_fence.md#stage-30)

    - “Then, willy-nilly, I will explain to Tunlon that I was unsuccessful. He may even want his 200 gold pieces back.” → [hadracor_fence_1b](#d-hadracor_fence_1b)

    <span id="d-hadracor_fence_2"></span>**`hadracor_fence_2`** Hadracor: “I saw you a few times in the forest over there coming from the mountains. Do you go there often?”

    - “Well, I try to avoid it. The route past Stoutford and Prim is long and arduous.” → [hadracor_fence_3](#d-hadracor_fence_3)

    <span id="d-hadracor_story_1"></span>**`hadracor_story_1`** Hadracor: “This is the encampment that we woodcutters set up while working on the trees here for the past few days.”

    - “What have you been working on?” → [hadracor_story_2](#d-hadracor_story_2)
    - “I noticed a lot of tree stumps around here.” → [hadracor_story_2](#d-hadracor_story_2)

    <span id="d-hadracor_andor_1"></span>**`hadracor_andor_1`** Hadracor: “Looks like you eh? No, I would have remembered.”

    - “OK, goodbye.” → *conversation ends*
    - “What is this place?” → [hadracor_story_1](#d-hadracor_story_1)

    <span id="d-hadracor_complete_3"></span>**`hadracor_complete_3`** Hadracor: “It's not much, but we do have some really sharp axes that you might be interested in.”

    - “No thanks. Goodbye.” → *conversation ends*
    - “OK, let me see what you have.” → *shop opens*
    - “Do you by any chance have some spare wood to make fences out of?” *(if reached stage 20 of [It makes no fence](../quests/tunlon_fence.md#stage-20); NOT reached stage 30 of [It makes no fence](../quests/tunlon_fence.md#stage-30))* → [hadracor_fence_1](#d-hadracor_fence_1)
    - “No, thanks. I'm too busy running up and down Blackwater mountain.” *(if reached stage 30 of [It makes no fence](../quests/tunlon_fence.md#stage-30); NOT reached stage 32 of [It makes no fence](../quests/tunlon_fence.md#stage-32))* → [hadracor_fence_2](#d-hadracor_fence_2)

    <span id="d-hadracor_story_3"></span>**`hadracor_story_3`** Hadracor: “I guess the nobles of Feygard have some plans for these lands.”

    - Next → [hadracor_story_4](#d-hadracor_story_4)

    <span id="d-hadracor_story_7"></span>**`hadracor_story_7`** Hadracor: “Nothing like we've seen before, and I'll tell you, we have seen a lot of wildlife in our days.”

    - Next → [hadracor_story_8](#d-hadracor_story_8)

    <span id="d-hadracor_fence_1b"></span>**`hadracor_fence_1b`** Hadracor: “Wait!”

    - Next → [hadracor_fence_1c](#d-hadracor_fence_1c)

    <span id="d-hadracor_fence_3"></span>**`hadracor_fence_3`** Hadracor: “I like to believe that. Look, I told my men to cut down some trees for you. You can now take a shortcut.” — **effects:** sets stage 32 of [It makes no fence](../quests/tunlon_fence.md#stage-32)

    - “Really? Thanks alot!” → [hadracor_fence_4](#d-hadracor_fence_4)

    <span id="d-hadracor_story_4"></span>**`hadracor_story_4`** Hadracor: “We, we just cut down them trees. No questions asked.”

    - Next → [hadracor_story_5](#d-hadracor_story_5)

    <span id="d-hadracor_story_8"></span>**`hadracor_story_8`** Hadracor: “They almost got the best of us, and we were almost ready to quit it. But a job is a job and we need to get paid by Feygard for this job.”

    - Next → [hadracor_story_9](#d-hadracor_story_9)

    <span id="d-hadracor_fence_1c"></span>**`hadracor_fence_1c`** Hadracor: “I like to sit here and look at the mountains and what's moving there. It's very relaxing after our hard work.”

    - “Yes, the mountains are very beautiful - from a distance.” → [hadracor_fence_2](#d-hadracor_fence_2)

    <span id="d-hadracor_fence_4"></span>**`hadracor_fence_4`** Hadracor: “The passage is over there, a bit to the east from here.”

    - Next → [hadracor_fence_5](#d-hadracor_fence_5)

    <span id="d-hadracor_story_5"></span>**`hadracor_story_5`** Hadracor: “However, this time we encountered some trouble.”

    - Next → [hadracor_story_6](#d-hadracor_story_6)

    <span id="d-hadracor_story_9"></span>**`hadracor_story_9`** Hadracor: “So we went ahead and finished all of them trees, trying to evade the wasps as much as we could.”

    - Next → [hadracor_story_10](#d-hadracor_story_10)

    <span id="d-hadracor_fence_5"></span>**`hadracor_fence_5`** Hadracor: “We were happy to do this for you. Now calm down.”

    - Next → [hadracor_fence_6](#d-hadracor_fence_6)

    <span id="d-hadracor_story_10"></span>**`hadracor_story_10`** Hadracor: “However, I bet that whatever plans the nobles of Feygard have for these lands, they surely don't include these nasty wasps still being around.”

    - Next → [hadracor_story_11](#d-hadracor_story_11)

    <span id="d-hadracor_fence_6"></span>**`hadracor_fence_6`** Hadracor: “And stop kissing my feet.”


    <span id="d-hadracor_story_11"></span>**`hadracor_story_11`** Hadracor: “See this scratch here? And this abscess? Yep, those wasps.”

    - Next → [hadracor_story_11_1](#d-hadracor_story_11_1)

    <span id="d-hadracor_story_11_1"></span>**`hadracor_story_11_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 10 of [Devastated land](../quests/hadracor.md#stage-10))* → [hadracor_accept_1_1](#d-hadracor_accept_1_1)
    - branch 2 → [hadracor_story_12](#d-hadracor_story_12)

    <span id="d-hadracor_accept_1_1"></span>**`hadracor_accept_1_1`** Hadracor: “I noticed that some of the wasps are larger than the other ones, and the other wasps tend to follow the larger ones around.”

    - Next → [hadracor_accept_2](#d-hadracor_accept_2)

    <span id="d-hadracor_story_12"></span>**`hadracor_story_12`** Hadracor: “I would love to get revenge on those wasps. We, we aren't good enough fighters to take on those wasps, they are really too quick for us.”

    - “Tough luck, you seem like a bunch of weaklings anyway.” → [hadracor_decline_1](#d-hadracor_decline_1)
    - “I could try to take on those wasps for you if you want.” → [hadracor_accept_1](#d-hadracor_accept_1)
    - “Just a couple of wasps? That's no problem for me. I'll kill them for you.” → [hadracor_accept_1](#d-hadracor_accept_1)

    <span id="d-hadracor_accept_2"></span>**`hadracor_accept_2`** Hadracor: “If you could kill at least five of those giant ones and bring me back their wings as proof, I would be very grateful.”

    - “Sure, I will be back with those giant wasp wings for you.” → [hadracor_accept_3](#d-hadracor_accept_3)
    - “No problem.” → [hadracor_accept_3](#d-hadracor_accept_3)
    - “On second thought, I better stay out of this.” → [hadracor_decline_2](#d-hadracor_decline_2)

    <span id="d-hadracor_decline_1"></span>**`hadracor_decline_1`** Hadracor: “I will pretend I didn't hear that.”


    <span id="d-hadracor_accept_1"></span>**`hadracor_accept_1`** Hadracor: “You would? Sure, you have a try.”

    - Next → [hadracor_accept_1_1](#d-hadracor_accept_1_1)

    <span id="d-hadracor_decline_2"></span>**`hadracor_decline_2`** Hadracor: “Fine, I guess we can find someone else to help us get revenge on them.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 5 lines changed |
| [v0.8.10](../versions/0.8.10.md) | Dialogue: 8 lines added, 3 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `hadracor` |
    | Type (wiki) | NPC |
    | Spawn group | `hadracor` |
    | Loot table | `shop_hadracor` |
    | Conversation | `hadracor` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:2` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "hadracor",
     "name": "Hadracor",
     "iconID": "monsters_men2:2",
     "monsterClass": "humanoid",
     "spawnGroup": "hadracor",
     "phraseID": "hadracor",
     "droplistID": "shop_hadracor"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hadracor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hadracor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hadracor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hadracor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
