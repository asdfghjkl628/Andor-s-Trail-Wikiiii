---
description: "Drunkard is a non-player character (NPC) in Andor's Trail, found in Fallhaven. Starts Drunken tale."
---

# ![](../assets/icons/monsters/monsters_men_0.png){ .sprite } Drunkard

**Where to find Drunkard:** Fallhaven: [Fallhaven north-west](../maps/fallhaven_nw.md#pin-npc-drunkard)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [Drunken tale](../quests/fallhavendrunk.md) |
| **Found in** | Fallhaven |
| **Entry ID** | `drunkard` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Drunken tale](../quests/fallhavendrunk.md): stages 10, 100
- [You shall pass](../quests/undertell_barricades.md): stages 130, 140
- [Undertell story flags (hidden flag)](../quests/undertell_hidden.md): stage 55

## Dialogue simulator

Set your quest stages and items, then talk to Drunkard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/fallhaven_drunk_selector.json" data-npc="Drunkard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (25 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-fallhaven_drunk_selector"></span>**`fallhaven_drunk_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if latest stage of [You shall pass](../quests/undertell_barricades.md#stage-140) is 140)* → [fallhaven_rain_qs_140](#d-fallhaven_rain_qs_140)
    - branch 2 → [fallhaven_drunk](#d-fallhaven_drunk)

    <span id="d-fallhaven_rain_qs_140"></span>**`fallhaven_rain_qs_140`** Drunkard: “Let me meet the merchant and then return. Please go meet Bela.”


    <span id="d-fallhaven_drunk"></span>**`fallhaven_drunk`** Drunkard: “No problem. No sireee! Not causing any more trouble now. I sits here outside now.”

    - Next → [fallhaven_drunk_2](#d-fallhaven_drunk_2)

    <span id="d-fallhaven_drunk_2"></span>**`fallhaven_drunk_2`** Drunkard: “Wait, who are you again? Are you that guard?”

    - “Yes.” → [fallhaven_drunk_3_1](#d-fallhaven_drunk_3_1)
    - “No.” → [fallhaven_drunk_3_2](#d-fallhaven_drunk_3_2)
    - “No, I am here to give you something.” *(if reached stage 120 of [You shall pass](../quests/undertell_barricades.md#stage-120); carry 1× [Potion of heightened senses](../items/pot_senses.md); NOT reached stage 55 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-55); have 5,000 gold)* → [fallhaven_drunk_potion_10](#d-fallhaven_drunk_potion_10)
    - “Shannal sent me.” *(if reached stage 55 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-55); NOT reached stage 130 of [You shall pass](../quests/undertell_barricades.md#stage-130); have 5,000 gold)* → [fallhaven_drunk_potion_30](#d-fallhaven_drunk_potion_30)
    - “Are you okay now?” *(if latest stage of [You shall pass](../quests/undertell_barricades.md#stage-130) is 130)* → [fallhaven_drunk_remember_30](#d-fallhaven_drunk_remember_30)

    <span id="d-fallhaven_drunk_3_1"></span>**`fallhaven_drunk_3_1`** Drunkard: “Oh, guard. I'm not causing any trouble anymore, see? I sits outside now as you says, OK?”

    - Next → [fallhaven_drunk_4](#d-fallhaven_drunk_4)

    <span id="d-fallhaven_drunk_3_2"></span>**`fallhaven_drunk_3_2`** Drunkard: “Oh good. That guard threw me out of the tavern. If I see him again I'll show him one thing or another.”

    - Next → [fallhaven_drunk_4](#d-fallhaven_drunk_4)

    <span id="d-fallhaven_drunk_potion_10"></span>**`fallhaven_drunk_potion_10`** Drunkard: “Is it that mead I ordered from the tavern?”

    - “No, it's not mead. That's the last thing that you need.” → [fallhaven_drunk_potion_20](#d-fallhaven_drunk_potion_20)

    <span id="d-fallhaven_drunk_potion_30"></span>**`fallhaven_drunk_potion_30`** Drunkard: “Shannal? That name sounds familiar to me, yet distant to me.” — **effects:** sets stage 55 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-55)

    - “Just drink the potion.” → [fallhaven_drunk_potion_drink_nar](#d-fallhaven_drunk_potion_drink_nar)

    <span id="d-fallhaven_drunk_remember_30"></span>**`fallhaven_drunk_remember_30`** Drunkard: “Well, let me get on with life...I seem to have made a mess of myself.”

    - “Worry not, as restitution, Shannal made the kidnapper's descendant, Benbyr pay up. Here's 5,000 gold. Keep it and…” *(if pay 5,000 gold)* → [fallhaven_drunk_remember_40](#d-fallhaven_drunk_remember_40)

    <span id="d-fallhaven_drunk_4"></span>**`fallhaven_drunk_4`** Drunkard: “Drink drink drink, drink some more. Drink, drink ... Uh how did it go again?”

    - Next → [fallhaven_drunk_5](#d-fallhaven_drunk_5)

    <span id="d-fallhaven_drunk_potion_20"></span>**`fallhaven_drunk_potion_20`** Drunkard: “Well, then I don't want it. Go get me some more mead from the lovely barkeeper, Bela.”

    - “No. I have a potion that will make you recover. Shannal's ghost has asked that you drink it. Now, here, drink it.” *(if hand over 1× [Potion of heightened senses](../items/pot_senses.md))* → [fallhaven_drunk_potion_30](#d-fallhaven_drunk_potion_30)

    <span id="d-fallhaven_drunk_potion_drink_nar"></span>**`fallhaven_drunk_potion_drink_nar`** [Dummy NPC](../monsters/none.md): “While leaning his head back, he downs the potion in one gulp...amazing.”

    - Next → [fallhaven_drunk_remember_10](#d-fallhaven_drunk_remember_10)

    <span id="d-fallhaven_drunk_remember_40"></span>**`fallhaven_drunk_remember_40`** Drunkard: “Thank you! Please ask Bela to keep them safe till Rain, oh by the way, that's my name, gets over this hangover. I need new clothes. So I will take 150 gold and visit the merchant. Please give Bela the remaining 4,850 gold.” — **effects:** sets stage 140 of [You shall pass](../quests/undertell_barricades.md#stage-140), gives 4850× [Gold coins](../items/gold.md)


    <span id="d-fallhaven_drunk_5"></span>**`fallhaven_drunk_5`** Drunkard: “Were you saying something? Where was I? Yes, so we were in this dungeon.”

    - Next → [fallhaven_drunk_6](#d-fallhaven_drunk_6)

    <span id="d-fallhaven_drunk_remember_10"></span>**`fallhaven_drunk_remember_10`** [Drunkard](../monsters/drunkard.md): “Now I remember; it was horrible. [weeping]” — **effects:** sets stage 130 of [You shall pass](../quests/undertell_barricades.md#stage-130)

    - “There...there...Shannal's ghost told me to tell you she's at peace.” → [fallhaven_drunk_remember_20](#d-fallhaven_drunk_remember_20)

    <span id="d-fallhaven_drunk_6"></span>**`fallhaven_drunk_6`** Drunkard: “Or was it a house? I can't remember.”

    - Next → [fallhaven_drunk_7](#d-fallhaven_drunk_7)

    <span id="d-fallhaven_drunk_remember_20"></span>**`fallhaven_drunk_remember_20`** Drunkard: “Thank you! To have passed her life at that place, kidnapped against her will, away from her husband and kids...”

    - Next → [fallhaven_drunk_remember_30](#d-fallhaven_drunk_remember_30)

    <span id="d-fallhaven_drunk_7"></span>**`fallhaven_drunk_7`** Drunkard: “No no, it was outside! Now I remember.”

    - Next → [fallhaven_drunk_7_select](#d-fallhaven_drunk_7_select)

    <span id="d-fallhaven_drunk_7_select"></span>**`fallhaven_drunk_7_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Drunken tale](../quests/fallhavendrunk.md#stage-100))* → [fallhaven_drunk_11](#d-fallhaven_drunk_11)
    - branch 2 → [fallhaven_drunk_8](#d-fallhaven_drunk_8)

    <span id="d-fallhaven_drunk_11"></span>**`fallhaven_drunk_11`** Drunkard: “[Takes a gulp of the mead] That's good stuff!”

    - Next → [fallhaven_drunk_12](#d-fallhaven_drunk_12)

    <span id="d-fallhaven_drunk_8"></span>**`fallhaven_drunk_8`** Drunkard: “That's where we... Hey, where did my mead go? Did you take it from me?”

    - “Yes” → [fallhaven_drunk_9_1](#d-fallhaven_drunk_9_1)
    - “No” → [fallhaven_drunk_9_2](#d-fallhaven_drunk_9_2)

    <span id="d-fallhaven_drunk_12"></span>**`fallhaven_drunk_12`** Drunkard: “Yeah, me and Unnmir had good times. Go ask him yourself, he is usually in the barn to the east of here. I wonder *burps* where that treasure went.” — **effects:** sets stage 100 of [Drunken tale](../quests/fallhavendrunk.md#stage-100)

    - “Treasure? I'm in! I'll go look for Unnmir right away.” → *conversation ends*
    - “Thank you for the story. Goodbye.” → *conversation ends*

    <span id="d-fallhaven_drunk_9_1"></span>**`fallhaven_drunk_9_1`** Drunkard: “Well then give it back! Or go buy me another mead.” — **effects:** sets stage 10 of [Drunken tale](../quests/fallhavendrunk.md#stage-10)

    - “Here, have some mead.” *(if hand over 1× [Mead](../items/mead.md))* → [fallhaven_drunk_10](#d-fallhaven_drunk_10)
    - “OK, I'll go buy some mead for you.” → *conversation ends*
    - “No. I don't think I should help you. Goodbye.” → *conversation ends*

    <span id="d-fallhaven_drunk_9_2"></span>**`fallhaven_drunk_9_2`** Drunkard: “I must have drunk it then. Could you get me a new mead do you think?” — **effects:** sets stage 10 of [Drunken tale](../quests/fallhavendrunk.md#stage-10)

    - “Here, have some mead.” *(if hand over 1× [Mead](../items/mead.md))* → [fallhaven_drunk_10](#d-fallhaven_drunk_10)
    - “OK, I'll go buy some mead for you.” → *conversation ends*
    - “No. I don't think I should help you. Goodbye.” → *conversation ends*

    <span id="d-fallhaven_drunk_10"></span>**`fallhaven_drunk_10`** Drunkard: “Oh sweet drinks of joy. May the sssshadow be with you kid. [Makes big eyes]”

    - Next → [fallhaven_drunk_11](#d-fallhaven_drunk_11)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 8 lines changed<br>· text: “That's where we.. Hey, where did my mead go? Did you take it from me?” → “That's where we... Hey, where did my mead go? Did you take it from me?”<br>· text: “Oh, sir. I'm not causing any trouble anymore, see? I sits outside now…” → “Oh, sir. I'm not causing any trouble anymore, see? I sits outside now…” |
| [v0.8.18](../versions/0.8.18.md) | Conversation changed<br>Dialogue: 10 lines added, 2 lines changed<br>· text: “Oh, sir. I'm not causing any trouble anymore, see? I sits outside now…” → “Oh, guard. I'm not causing any trouble anymore, see? I sits outside n…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `drunkard` |
    | Spawn group | `fallhaven_drunk` |
    | Loot table | – |
    | Conversation | `fallhaven_drunk_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:0` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "drunkard",
     "name": "Drunkard",
     "iconID": "monsters_men:0",
     "monsterClass": "humanoid",
     "spawnGroup": "fallhaven_drunk",
     "phraseID": "fallhaven_drunk_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drunkard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drunkard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drunkard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=drunkard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
