---
description: "Crescenzio is a non-player character (NPC) in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_ld1_22.png){ .sprite } Crescenzio

**Where to find Crescenzio:** Brightport: [brightport_bakery1](../maps/brightport_bakery1.md#pin-npc-brightport_chef2)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_22.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Brightport |
| **Entry ID** | `brightport_chef2` |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Quests

- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 187, 189

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Crescenzio. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_crescenzio_0.json" data-npc="Crescenzio" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (25 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_crescenzio_0"></span>**`brightport_crescenzio_0`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 189 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-189))* → [brightport_crescenzio15](#d-brightport_crescenzio15)
    - Next → [brightport_crescenzio](#d-brightport_crescenzio)

    <span id="d-brightport_crescenzio15"></span>**`brightport_crescenzio15`** Crescenzio: “Hello child from Crossglen. Back for my cooking?”

    - “Yes, I want you to cook me some stuffed peppers.” → [brightport_crescenzio6](#d-brightport_crescenzio6)
    - “Do you have butter and dough?” *(if reached stage 5 of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-5))* → [brightport_crescnezio16](#d-brightport_crescnezio16)

    <span id="d-brightport_crescenzio"></span>**`brightport_crescenzio`** Crescenzio: “I am very busy, I hope you haven't intruded into the kitchen for some silly game.”

    - “Can you cook me something?” → [brightport_crescenzio_selector](#d-brightport_crescenzio_selector)
    - “Do you have butter or dough?” *(if reached stage 5 of [A Feygard delicacy](../quests/feygard_delicacy.md#stage-5))* → [brightport_crescenzio1](#d-brightport_crescenzio1)

    <span id="d-brightport_crescenzio6"></span>**`brightport_crescenzio6`** Crescenzio: “To prepare some for you, I'll need peppers and rice. And an appropriate fee of 20 gold. The peppers come in different colors, and each affects the flavor, so I prefer to cook them separately.”

    - “I would like you to cook me some.” → [brightport_crescenzio7](#d-brightport_crescenzio7)

    <span id="d-brightport_crescnezio16"></span>**`brightport_crescnezio16`** Crescenzio: “Ask my colleague Androni, he is working with the ingredients right now.”


    <span id="d-brightport_crescenzio_selector"></span>**`brightport_crescenzio_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 70 of [Bread and circus](../quests/brightport_bakery.md#stage-70))* → [brightport_crescenzio4](#d-brightport_crescenzio4)
    - Next *(if reached stage 187 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-187))* → [brightport_crescenzio3](#d-brightport_crescenzio3)
    - Next *(if NOT reached stage 187 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-187))* → [brightport_crescenzio0](#d-brightport_crescenzio0)

    <span id="d-brightport_crescenzio1"></span>**`brightport_crescenzio1`** Crescenzio: “Do I have? No. Do we have? Yes, quite a lot of both. But no, I will not give you any, if that's what you were about to ask. I have a great deal of work, and you'd do well not to intrude on it.”


    <span id="d-brightport_crescenzio7"></span>**`brightport_crescenzio7`** Crescenzio: “...”

    - “Here's 1 green pepper and rice.” *(if hand over 1× [Green Pepper](../items/green_pepper.md); pay 20 gold; hand over 1× [Rice](../items/brightport_rice.md))* → [brightport_crescenzio8](#d-brightport_crescenzio8)
    - “Here are 5 green peppers and rice.” *(if hand over 5× [Green Pepper](../items/green_pepper.md); hand over 5× [Rice](../items/brightport_rice.md); pay 100 gold)* → [brightport_crescenzio_1](#d-brightport_crescenzio_1)
    - “Here's 1 yellow pepper and rice.” *(if pay 20 gold; hand over 1× [Rice](../items/brightport_rice.md); hand over 1× [Yellow Pepper](../items/yellow_pepper.md))* → [brightport_crescenzio_2](#d-brightport_crescenzio_2)
    - “Here are 5 yellow peppers and rice.” *(if hand over 5× [Yellow Pepper](../items/yellow_pepper.md); pay 100 gold; hand over 5× [Rice](../items/brightport_rice.md))* → [brightport_crescenzio_3](#d-brightport_crescenzio_3)
    - “Here's 1 red pepper and rice.” *(if hand over 1× [Red Pepper](../items/red_pepper.md); hand over 1× [Rice](../items/brightport_rice.md); pay 20 gold)* → [brightport_crescenzio_4](#d-brightport_crescenzio_4)
    - “Here are 5 red peppers and rice.” *(if pay 100 gold; hand over 5× [Red Pepper](../items/red_pepper.md); hand over 5× [Rice](../items/brightport_rice.md))* → [brightport_crescnezio_5](#d-brightport_crescnezio_5)
    - “I don't have the ingredients now, I'll be back again.” → *conversation ends*

    <span id="d-brightport_crescenzio4"></span>**`brightport_crescenzio4`** Crescenzio: “Thanks to the delivery you made, we started baking the first batch of apple tarts for the festival. I can cook you a Crossglen recipe while I keep an eye on the oven.”

    - “What do you want to cook me?” → [brightport_crescenzio5](#d-brightport_crescenzio5)

    <span id="d-brightport_crescenzio3"></span>**`brightport_crescenzio3`** Crescenzio: “We're still swamped with work, but I haven't forgotten, child from Crossglen.”

    - “Got it, bye.” → *conversation ends*

    <span id="d-brightport_crescenzio0"></span>**`brightport_crescenzio0`** Crescenzio: “Do you not like the menu? Ah, I understand. You wish for a taste of your hometown. Wherever you're from, I'm quite busy now, but if you could come back later, I could do it. Where are you from, child?”

    - “Crossglen.” → [brightport_crescenzio2](#d-brightport_crescenzio2)

    <span id="d-brightport_crescenzio8"></span>**`brightport_crescenzio8`** Crescenzio: “Just a moment...” — **effects:** sets stage 189 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-189)

    - Next → [brightport_crescenzio9](#d-brightport_crescenzio9)

    <span id="d-brightport_crescenzio_1"></span>**`brightport_crescenzio_1`** Crescenzio: “Just a moment...” — **effects:** sets stage 189 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-189)

    - Next → [brightport_crescenzio10](#d-brightport_crescenzio10)

    <span id="d-brightport_crescenzio_2"></span>**`brightport_crescenzio_2`** Crescenzio: “Just a moment...” — **effects:** sets stage 189 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-189)

    - Next → [brightport_crescenzio11](#d-brightport_crescenzio11)

    <span id="d-brightport_crescenzio_3"></span>**`brightport_crescenzio_3`** Crescenzio: “Just a moment...” — **effects:** sets stage 189 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-189)

    - Next → [brightport_crescenzio12](#d-brightport_crescenzio12)

    <span id="d-brightport_crescenzio_4"></span>**`brightport_crescenzio_4`** Crescenzio: “Just a moment...” — **effects:** sets stage 189 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-189)

    - Next → [brightport_crescenzio13](#d-brightport_crescenzio13)

    <span id="d-brightport_crescnezio_5"></span>**`brightport_crescnezio_5`** Crescenzio: “Just a moment...” — **effects:** sets stage 189 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-189)

    - Next → [brightport_crescenzio14](#d-brightport_crescenzio14)

    <span id="d-brightport_crescenzio5"></span>**`brightport_crescenzio5`** Crescenzio: “Delicious rice stuffed peppers. In Crossglen they'd make it with millet, but here we get rice from Nor City.”

    - Next → [brightport_crescenzio6](#d-brightport_crescenzio6)

    <span id="d-brightport_crescenzio2"></span>**`brightport_crescenzio2`** Crescenzio: “Understood. Now, I wouldn't mind your presence here if we weren't so busy, so please leave.” — **effects:** sets stage 187 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-187)

    - “Got it, bye.” → *conversation ends*

    <span id="d-brightport_crescenzio9"></span>**`brightport_crescenzio9`** Crescenzio: “Here it is.” — **effects:** gives 1× [Stuffed pepper](../items/brightport_green.md)

    - “I would like you to cook me more.” → [brightport_crescenzio7](#d-brightport_crescenzio7)

    <span id="d-brightport_crescenzio10"></span>**`brightport_crescenzio10`** Crescenzio: “Here it is.” — **effects:** gives 5× [Stuffed pepper](../items/brightport_green.md)

    - “I would like you to cook me more.” → [brightport_crescenzio7](#d-brightport_crescenzio7)

    <span id="d-brightport_crescenzio11"></span>**`brightport_crescenzio11`** Crescenzio: “Here it is.” — **effects:** gives 1× [Stuffed pepper](../items/brightport_yellow.md)

    - “I would like you to cook me more.” → [brightport_crescenzio7](#d-brightport_crescenzio7)

    <span id="d-brightport_crescenzio12"></span>**`brightport_crescenzio12`** Crescenzio: “Here it is.” — **effects:** gives 5× [Yellow Pepper](../items/yellow_pepper.md)

    - “I would like you to cook me more.” → [brightport_crescenzio7](#d-brightport_crescenzio7)

    <span id="d-brightport_crescenzio13"></span>**`brightport_crescenzio13`** Crescenzio: “Here it is.” — **effects:** gives 1× [Stuffed pepper](../items/brightport_red.md)

    - “I would like you to cook me more.” → [brightport_crescenzio7](#d-brightport_crescenzio7)

    <span id="d-brightport_crescenzio14"></span>**`brightport_crescenzio14`** Crescenzio: “Here it is.” — **effects:** gives 5× [Stuffed pepper](../items/brightport_red.md)

    - “I would like you to cook me more.” → [brightport_crescenzio7](#d-brightport_crescenzio7)



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 25 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightport_chef2` |
    | Spawn group | `brightport_chef2` |
    | Loot table | – |
    | Conversation | `brightport_crescenzio_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:22` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_chef2",
     "name": "Crescenzio",
     "iconID": "monsters_ld1:22",
     "phraseID": "brightport_crescenzio_0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_chef2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_chef2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_chef2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_chef2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
