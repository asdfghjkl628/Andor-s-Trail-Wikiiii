---
description: "Jakrar is a non-player character (NPC) in Andor's Trail, found in Fallhaven. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_men2_2.png){ .sprite } Jakrar

**Where to find Jakrar:** Fallhaven: [Fallhaven south-west](../maps/fallhaven_sw.md#pin-npc-jakrar)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men2_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper |
| **Found in** | Fallhaven |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Wooden club](../items/club1.md) | 100% | 2 |
| [Woodcutter's axe](../items/axe1.md) | 100% | 1 |
| [Iron axe](../items/axe2.md) | 100% | 1 |
| [Broken wooden buckler](../items/broken_buckler.md) | 100% | 1 |
| [Crude wooden buckler](../items/shield_crude_wooden.md) | 100% | 2 |

## Quests

- [A path to the Duleian Road](../quests/pathway_fallhaven.md): stages 30, 40, 50
- [It makes no fence](../quests/tunlon_fence.md): stage 20

## Dialogue simulator

Set your quest stages and items, then talk to Jakrar. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/fallhaven_lumberjack.json" data-npc="Jakrar" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (18 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-fallhaven_lumberjack"></span>**`fallhaven_lumberjack`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 50 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-50))* → [fallhaven_lumberjack_15](#d-fallhaven_lumberjack_15)
    - Next *(if reached stage 40 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-40); NOT reached stage 50 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-50))* → [fallhaven_lumberjack_16](#d-fallhaven_lumberjack_16)
    - Next *(if reached stage 30 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-30))* → [fallhaven_lumberjack_14](#d-fallhaven_lumberjack_14)
    - Next → [fallhaven_lumberjack_1](#d-fallhaven_lumberjack_1)

    <span id="d-fallhaven_lumberjack_15"></span>**`fallhaven_lumberjack_15`** Jakrar: “Hello again my friend.”

    - “I cannot thank you enough for cutting away those trees! Finally I've got a shortcut!” *(if reached stage 60 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-60))* → [fallhaven_lumberjack_13](#d-fallhaven_lumberjack_13)
    - “What have you got for sale?” → *shop opens*
    - “Never mind. I don't need your services for now.” → *conversation ends*
    - “Tunlon has sent me to ask for some wood for fences.” *(if reached stage 10 of [It makes no fence](../quests/tunlon_fence.md#stage-10); NOT reached stage 20 of [It makes no fence](../quests/tunlon_fence.md#stage-20))* → [fallhaven_lumberjack_17](#d-fallhaven_lumberjack_17)

    <span id="d-fallhaven_lumberjack_16"></span>**`fallhaven_lumberjack_16`** Jakrar: “Thank you for bringing me back my axe!”

    - “So will you cut away those trees that block the old pathway?” → [fallhaven_lumberjack_11](#d-fallhaven_lumberjack_11)

    <span id="d-fallhaven_lumberjack_14"></span>**`fallhaven_lumberjack_14`** Jakrar: “Have you made any progress in finding my precious axe?”

    - “Hello again! I've finally found your axe!” *(if hand over 1× [Jakrar's woodcutting axe](../items/jakrar_axe.md))* → [fallhaven_lumberjack_10](#d-fallhaven_lumberjack_10)
    - “No I haven't. But I'm working on it.” → *conversation ends*
    - “Nope, But I am wondering if you have anything for sale that would help me find your axe?” → *shop opens*

    <span id="d-fallhaven_lumberjack_1"></span>**`fallhaven_lumberjack_1`** Jakrar: “Hi, I'm Jakrar.”

    - “Are you a woodcutter?” → [fallhaven_lumberjack_2](#d-fallhaven_lumberjack_2)
    - “Tunlon has sent me to ask for some wood for fences.” *(if reached stage 10 of [It makes no fence](../quests/tunlon_fence.md#stage-10); NOT reached stage 20 of [It makes no fence](../quests/tunlon_fence.md#stage-20))* → [fallhaven_lumberjack_17](#d-fallhaven_lumberjack_17)

    <span id="d-fallhaven_lumberjack_13"></span>**`fallhaven_lumberjack_13`** Jakrar: “You're welcome. But you're not the only one who is happy. There are more people resting for a night in Fallhaven, which helps our economy. Some even bought items at my store! By the way, I was surprised, but I even got paid well by the…”

    - “Great. Now everything is much better than it was before!” → *conversation ends*
    - “I wanted to ask about something else.” → [fallhaven_lumberjack_15](#d-fallhaven_lumberjack_15)

    <span id="d-fallhaven_lumberjack_17"></span>**`fallhaven_lumberjack_17`** Jakrar: “See, I have done a lot of tree cutting lately, and I need a break. Sorry, kid.”

    - “Oh, alright. But where should I ask then?” → [fallhaven_lumberjack_18](#d-fallhaven_lumberjack_18)

    <span id="d-fallhaven_lumberjack_11"></span>**`fallhaven_lumberjack_11`** Jakrar: “Sure! Already on my way! The work will be finished soon.” — **effects:** sets stage 50 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-50)

    - “That sounds great! Remember to ask the stupid guard captain for a decent payment.” → [fallhaven_lumberjack_12](#d-fallhaven_lumberjack_12)

    <span id="d-fallhaven_lumberjack_10"></span>**`fallhaven_lumberjack_10`** Jakrar: “Let me see... Oh yes! This is my axe! I cannot thank you enough!” — **effects:** sets stage 40 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-40)

    - “So will you cut away those trees that block the old pathway?” → [fallhaven_lumberjack_11](#d-fallhaven_lumberjack_11)

    <span id="d-fallhaven_lumberjack_2"></span>**`fallhaven_lumberjack_2`** Jakrar: “Yes, I'm Fallhaven's woodcutter. Need anything done in the finest of woods? I have probably got it.”

    - “I'd like to talk with you about Fallhaven's passage to the Duleian Road.” *(if latest stage of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-20) is 20)* → [fallhaven_lumberjack_3](#d-fallhaven_lumberjack_3)
    - “Never mind. I don't need your services for now.” → *conversation ends*
    - “What have you got for sale?” → *shop opens*

    <span id="d-fallhaven_lumberjack_18"></span>**`fallhaven_lumberjack_18`** Jakrar: “I have heard that a forest to the north was cleared out recently. Sure enough they got some wood laying around there.” — **effects:** sets stage 20 of [It makes no fence](../quests/tunlon_fence.md#stage-20)

    - “Thank you very much, I will go there now.” → *conversation ends*

    <span id="d-fallhaven_lumberjack_12"></span>**`fallhaven_lumberjack_12`** Jakrar: “Sure. Will do that. He he.”

    - “Shadow be with you.” → *conversation ends*
    - “Goodbye.” → *conversation ends*

    <span id="d-fallhaven_lumberjack_3"></span>**`fallhaven_lumberjack_3`** Jakrar: “Oh no. Not again. I won't start cutting the trees unless I have received a payment beforehand. Go away!”

    - “Is there anything that would change your mind?” → [fallhaven_lumberjack_4](#d-fallhaven_lumberjack_4)
    - “Seems like nobody wants to open the road again. Great.” → *conversation ends*

    <span id="d-fallhaven_lumberjack_4"></span>**`fallhaven_lumberjack_4`** Jakrar: “Hmm. Well if you would do me a great favor I would start to cut the trees away.”

    - “Sure! What is it?” → [fallhaven_lumberjack_5](#d-fallhaven_lumberjack_5)

    <span id="d-fallhaven_lumberjack_5"></span>**`fallhaven_lumberjack_5`** Jakrar: “Let me tell you a story. Long ago, I was cutting in the woods to the north of Fallhaven. I used to cut the trees with great speed with my favorite axe. It was made of fine steel and probably worth more than my hut.”

    - Next → [fallhaven_lumberjack_6](#d-fallhaven_lumberjack_6)

    <span id="d-fallhaven_lumberjack_6"></span>**`fallhaven_lumberjack_6`** Jakrar: “But then, I got attacked by a pack of wolves and I had to flee immediately. I barely saved my life, but during the escape I lost my precious axe.”

    - Next → [fallhaven_lumberjack_7](#d-fallhaven_lumberjack_7)

    <span id="d-fallhaven_lumberjack_7"></span>**`fallhaven_lumberjack_7`** Jakrar: “I'm afraid of travelling to that place again because I'm not a trained fighter and the wolves, especially their leader, were really powerful.”

    - “So I guess you want me to retrieve your axe?” → [fallhaven_lumberjack_8](#d-fallhaven_lumberjack_8)

    <span id="d-fallhaven_lumberjack_8"></span>**`fallhaven_lumberjack_8`** Jakrar: “Yes exactly. If you would do me that favor I will gladly cut away the trees and receive payment afterwards. Just head north to the Crossroads guardhouse and then head eastwards down the Duleian Road. That's where I lost my axe. And look…” — **effects:** sets stage 30 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-30)

    - “Sounds simple enough. On my way.” → *conversation ends*
    - “No way! That is far too dangerous!” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Loot table added<br>Dialogue: 14 lines added, 2 lines changed<br>· text: “Hi, I'm Jakrar.” → “null” |
| [v0.7.15](../versions/0.7.15.md) | Dialogue: 2 lines changed<br>· text: “You're welcome. But you're not the only one who is happy. There are m…” → “You're welcome. But you're not the only one who is happy. There are m…” |
| [v0.8.10](../versions/0.8.10.md) | Dialogue: 2 lines added, 2 lines changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `jakrar` |
    | Type (wiki) | NPC |
    | Spawn group | `fallhaven_lumberjack` |
    | Loot table | `shop_fallhaven_lumberjack` |
    | Conversation | `fallhaven_lumberjack` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:2` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "jakrar",
     "name": "Jakrar",
     "iconID": "monsters_men2:2",
     "monsterClass": "humanoid",
     "spawnGroup": "fallhaven_lumberjack",
     "phraseID": "fallhaven_lumberjack",
     "droplistID": "shop_fallhaven_lumberjack"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jakrar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jakrar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jakrar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jakrar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
