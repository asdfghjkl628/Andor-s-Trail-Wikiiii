---
description: "Allares is a non-player character (NPC) in Andor's Trail, found in Brightport. Starts Bread and circus."
---

# ![](../assets/icons/monsters/monsters_ld_edit_0.png){ .sprite } Allares

**Where to find Allares:** Brightport: [Brightport bakery 1](../maps/brightport_bakery1.md#pin-npc-brightportstoragenpc)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld_edit_0.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Starts [Bread and circus](../quests/brightport_bakery.md) |
| **Found in** | Brightport |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Quests

- [Bread and circus](../quests/brightport_bakery.md): stages 1, 22, 23, 70

## Dialogue simulator

Talk to Allares as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_allares.json" data-npc="Allares" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (17 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_allares"></span>**`brightport_allares`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 70 of [Bread and circus](../quests/brightport_bakery.md#stage-70))* → [brightport_allares_end](#d-brightport_allares_end)
    - Next *(if reached stage 22 of [Bread and circus](../quests/brightport_bakery.md#stage-22); NOT reached stage 23 of [Bread and circus](../quests/brightport_bakery.md#stage-23))* → [brightport_allares4](#d-brightport_allares4)
    - Next *(if reached stage 5 of [Bread and circus](../quests/brightport_bakery.md#stage-5))* → [brightport_allares3](#d-brightport_allares3)
    - Next → [brightport_allares0](#d-brightport_allares0)

    <span id="d-brightport_allares_end"></span>**`brightport_allares_end`** Allares: “Hello. You've done good work today. Saved us quite a bit of time.”

    - “It was a nice distraction.” → *conversation ends*

    <span id="d-brightport_allares4"></span>**`brightport_allares4`** Allares: “Have you brought me the deer meat?”

    - “Yes, here you go.” *(if hand over 1× [Raw venison](../items/brightport_rawmeat.md))* → [brightport_allares5](#d-brightport_allares5)
    - “No, not yet.” → *conversation ends*

    <span id="d-brightport_allares3"></span>**`brightport_allares3`** Allares: “Hello, how is the work?”

    - “I brought the apples to Eatloni, he'll have them brought in soon.” *(if reached stage 198 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-198))* → [brightport_allares9](#d-brightport_allares9)
    - “Delon said there was an apple delivery that was supposed to arrive but didn't.” *(if reached stage 20 of [Bread and circus](../quests/brightport_bakery.md#stage-20); NOT reached stage 22 of [Bread and circus](../quests/brightport_bakery.md#stage-22))* → [brightport_allares6](#d-brightport_allares6)
    - “I have the 30 apples here.” *(if reached stage 25 of [Bread and circus](../quests/brightport_bakery.md#stage-25); carry 30× [Orchard apple](../items/deebo_apples.md); NOT reached stage 198 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-198))* → [brightport_allares_apples](#d-brightport_allares_apples)
    - “I'm still doing it.” *(if NOT reached stage 16 of [Bread and circus](../quests/brightport_bakery.md#stage-16))* → *conversation ends*
    - “I'm still looking for those apples.” *(if reached stage 23 of [Bread and circus](../quests/brightport_bakery.md#stage-23); NOT reached stage 70 of [Bread and circus](../quests/brightport_bakery.md#stage-70))* → *conversation ends*

    <span id="d-brightport_allares0"></span>**`brightport_allares0`** Allares: “Please don't bother the cooks. We are very busy today. We've got some big orders for the festival down in Sullengard.”

    - “Perhaps I could help?” *(if NOT reached stage 157 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-157); NOT reached stage 1 of [Bread and circus](../quests/brightport_bakery.md#stage-1))* → [brightport_allares1](#d-brightport_allares1)
    - “Eatloni told me to see you.” *(if reached stage 157 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-157); NOT reached stage 1 of [Bread and circus](../quests/brightport_bakery.md#stage-1))* → [brightport_allares2](#d-brightport_allares2)
    - “That's nice. But I don't care. See you later.” → *conversation ends*

    <span id="d-brightport_allares5"></span>**`brightport_allares5`** Allares: “Very good, you've convinced me of your capabilities. Please talk to Eatloni outside, he was in charge of the apple delivery and should know more.” — **effects:** sets stage 23 of [Bread and circus](../quests/brightport_bakery.md#stage-23)


    <span id="d-brightport_allares9"></span>**`brightport_allares9`** Allares: “Very good $playername, you've been our most useful temporary worker so far.”

    - Next → [brightport_allares10](#d-brightport_allares10)

    <span id="d-brightport_allares6"></span>**`brightport_allares6`** Allares: “Yes it should have arrived quite a while ago, usually they are on time. That is terrible for today of all days as we have a big order to fulfill in the next few days.”

    - “I could go help look for it.” → [brightport_allares7](#d-brightport_allares7)

    <span id="d-brightport_allares_apples"></span>**`brightport_allares_apples`** Allares: “That is good, $playername, but not quite right. It is Eatloni you were supposed to deliver them to, there is a proper procedure for everything.”


    <span id="d-brightport_allares1"></span>**`brightport_allares1`** Allares: “Today we're swamped, so we'll pay you a full day's wage for just a bit of work. Go down to the storage area and see what Delon asks of you.” — **effects:** sets stage 1 of [Bread and circus](../quests/brightport_bakery.md#stage-1)


    <span id="d-brightport_allares2"></span>**`brightport_allares2`** Allares: “Very good, very good! Go down to the storage room and speak with Delon. You two will be working together.” — **effects:** sets stage 1 of [Bread and circus](../quests/brightport_bakery.md#stage-1)


    <span id="d-brightport_allares10"></span>**`brightport_allares10`** Allares: “And now let's discuss your payment. 50 gold for the bakery work.”

    - Next → [brightport_allares11](#d-brightport_allares11)

    <span id="d-brightport_allares7"></span>**`brightport_allares7`** Allares: “Hmm, maybe you could. But I'm a little hesitant. If the merchant went missing, that could mean danger, and I don't want to be responsible for you.”

    - “Don't worry, I'm an experienced adventurer.” → [brightport_allares8](#d-brightport_allares8)

    <span id="d-brightport_allares11"></span>**`brightport_allares11`** Allares: “50 for the venison.”

    - Next → [brightport_allares12](#d-brightport_allares12)

    <span id="d-brightport_allares8"></span>**`brightport_allares8`** Allares: “You do have some shiny equipment on you, which shows me you're a bit experienced, but I'd rather you prove it by bringing me something tough to get. Some venison, or in other words, deer meat. And yes I will pay you, it's just that it's…” — **effects:** sets stage 22 of [Bread and circus](../quests/brightport_bakery.md#stage-22)

    - “Easy enough.” → *conversation ends*

    <span id="d-brightport_allares12"></span>**`brightport_allares12`** Allares: “And 100 for bringing us the apples. Any complaints?”

    - “Just give me the gold already.” → [brightport_allares13](#d-brightport_allares13)

    <span id="d-brightport_allares13"></span>**`brightport_allares13`** Allares: “OK, here you go. Don't spend it all in useless shops. Ideally buy some pastries at our bakery.” — **effects:** gives 200× [Gold coins](../items/gold.md), sets stage 70 of [Bread and circus](../quests/brightport_bakery.md#stage-70)

    - “Back to my journey.” → *conversation ends*
    - “So little...” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 17 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 2 lines changed<br>· text: “Yes it should have arrived quite a while ago, usually they are on tim…” → “Yes it should have arrived quite a while ago, usually they are on tim…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightportstoragenpc` |
    | Type (wiki) | NPC |
    | Spawn group | `brightportstoragenpc` |
    | Loot table | – |
    | Conversation | `brightport_allares` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld_edit:0` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportstoragenpc",
     "name": "Allares",
     "iconID": "monsters_ld_edit:0",
     "monsterClass": "humanoid",
     "phraseID": "brightport_allares"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportstoragenpc.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportstoragenpc.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportstoragenpc.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportstoragenpc.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
