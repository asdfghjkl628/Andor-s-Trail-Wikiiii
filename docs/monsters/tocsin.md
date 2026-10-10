---
description: "Tocsin is a non-player character (NPC) in Andor's Trail, found in Undertell 4 00."
---

# ![](../assets/icons/monsters/monsters_ld2_161.png){ .sprite } Tocsin

**Where to find Tocsin:** [Undertell 4 00](../maps/undertell_4_00.md#pin-npc-tocsin)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld2_161.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Undertell 4 00 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Quests

- [Undertell story flags (hidden flag)](../quests/undertell_hidden.md): stage 95

## Dialogue simulator

Talk to Tocsin as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/tocsin_selector.json" data-npc="Tocsin" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (19 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-tocsin_selector"></span>**`tocsin_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if carry 1× [Rotten meat](../items/meat2.md); NOT reached stage 50 of [About a girl](../quests/about_a_girl.md#stage-50))* → [tocsin_rotten_10](#d-tocsin_rotten_10)
    - branch 2 *(if carry 1× [Rotten fish](../items/rotten_fish.md); NOT reached stage 50 of [About a girl](../quests/about_a_girl.md#stage-50))* → [tocsin_rotten_10](#d-tocsin_rotten_10)
    - branch 3 → [tocsin_switch](#d-tocsin_switch)

    <span id="d-tocsin_rotten_10"></span>**`tocsin_rotten_10`** [Tocsin](../monsters/tocsin.md): “Kek-kek-kek-kek-KRAAAK!”

    - Next → [tocsin_rotten_20](#d-tocsin_rotten_20)

    <span id="d-tocsin_switch"></span>**`tocsin_switch`** [Kha'zaan Porter](../monsters/porter.md): “What is wrong with you?”

    - “Nothing.” → [tocsin_porter_10](#d-tocsin_porter_10)
    - “Nothing. I'm just happy to still have ten fingers!” *(if reached stage 95 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-95))* → [tocsin_porter_10](#d-tocsin_porter_10)

    <span id="d-tocsin_rotten_20"></span>**`tocsin_rotten_20`** [Dummy NPC](../monsters/none.md): “The creature lunges forward...you pull back moments before it clamps onto your hand!” — **effects:** sets stage 95 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-95)

    - Next → [tocsin_switch](#d-tocsin_switch)

    <span id="d-tocsin_porter_10"></span>**`tocsin_porter_10`** Tocsin: “You talk to me. She doesn't talk to mortals such as yourself.”

    - “But what is it?” → [tocsin_porter_20](#d-tocsin_porter_20)

    <span id="d-tocsin_porter_20"></span>**`tocsin_porter_20`** Tocsin: “"She" is a campanite, a pet if you will...yeah, my guard pet and not an "it".”

    - “A pet? I want a pet. Where can I get a campanite for myself?” → [porter_pet_10](#d-porter_pet_10)
    - “Why do you have her?” → [porter_pet_15](#d-porter_pet_15)

    <span id="d-porter_pet_10"></span>**`porter_pet_10`** Tocsin: “You, have a pet? Nah! You are not allowed.”

    - “Why not?” → [porter_pet_20](#d-porter_pet_20)

    <span id="d-porter_pet_15"></span>**`porter_pet_15`** Tocsin: “She helps me do my job of preventing rift rafts such as yourself from passing through this here door.”

    - “But what's through that door?” *(if NOT reached stage 95 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-95))* → [porter_door_10](#d-porter_door_10)
    - “But what's through that door?” *(if reached stage 95 of [Undertell story flags (hidden flag)](../quests/undertell_hidden.md#stage-95))* → [porter_pet_hungry_10](#d-porter_pet_hungry_10)

    <span id="d-porter_pet_20"></span>**`porter_pet_20`** Tocsin: “Well, you are an explorer, so you will find yourself in places unsuitable for pets.”

    - “Blah! Whatever.” → *conversation ends*

    <span id="d-porter_door_10"></span>**`porter_door_10`** Tocsin: “Nothing for mortals to see without permission.”

    - “Permission from whom?” → [porter_door_20](#d-porter_door_20)

    <span id="d-porter_pet_hungry_10"></span>**`porter_pet_hungry_10`** Tocsin: “Tocsin over here is hungry.”

    - “What?” → [porter_pet_hungry_20](#d-porter_pet_hungry_20)

    <span id="d-porter_door_20"></span>**`porter_door_20`** Tocsin: “If you had it, then you would know. Now leave me.”


    <span id="d-porter_pet_hungry_20"></span>**`porter_pet_hungry_20`** Tocsin: “Give me your rotten animal parts so Tocsin can eat and if she enjoys your offerings, then I will allow your entry.”

    - “No problem! I've been looking to get rid of them anyway.” → [porter_pet_hungry_30](#d-porter_pet_hungry_30)

    <span id="d-porter_pet_hungry_30"></span>**`porter_pet_hungry_30`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if hand over 1× [Rotten meat](../items/meat2.md))* → [porter_pet_hungry_30_1](#d-porter_pet_hungry_30_1)
    - branch 2 *(if hand over 1× [Rotten fish](../items/rotten_fish.md))* → [porter_pet_hungry_30_2](#d-porter_pet_hungry_30_2)
    - branch 3 → [porter_pet_hungry_fed_10](#d-porter_pet_hungry_fed_10)

    <span id="d-porter_pet_hungry_30_1"></span>**`porter_pet_hungry_30_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if hand over 1× [Rotten meat](../items/meat2.md))* → [porter_pet_hungry_30_1](#d-porter_pet_hungry_30_1)
    - branch 2 *(if hand over 1× [Rotten fish](../items/rotten_fish.md))* → [porter_pet_hungry_30_2](#d-porter_pet_hungry_30_2)
    - branch 3 → [porter_pet_hungry_fed_10](#d-porter_pet_hungry_fed_10)

    <span id="d-porter_pet_hungry_30_2"></span>**`porter_pet_hungry_30_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if hand over 1× [Rotten fish](../items/rotten_fish.md))* → [porter_pet_hungry_30_2](#d-porter_pet_hungry_30_2)
    - branch 2 → [porter_pet_hungry_fed_10](#d-porter_pet_hungry_fed_10)

    <span id="d-porter_pet_hungry_fed_10"></span>**`porter_pet_hungry_fed_10`** [Dummy NPC](../monsters/none.md): “The porter proceeds to feed what you have given him to Tocsin. You watch with amazement as it looks as if Tocsin simply swallowed it whole.”

    - “Well, do I have permission?” → [porter_pet_hungry_fed_20](#d-porter_pet_hungry_fed_20)

    <span id="d-porter_pet_hungry_fed_20"></span>**`porter_pet_hungry_fed_20`** [Kha'zaan Porter](../monsters/porter.md): “If you had it, then you would know. Now leave me.”

    - “What?!” → [porter_pet_hungry_fed_30](#d-porter_pet_hungry_fed_30)

    <span id="d-porter_pet_hungry_fed_30"></span>**`porter_pet_hungry_fed_30`** Tocsin: “Look at her, she didn't enjoy that meal. Now leave us.”




## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 19 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `tocsin` |
    | Type (wiki) | NPC |
    | Spawn group | `tocsin` |
    | Loot table | – |
    | Conversation | `tocsin_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld2:161` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "tocsin",
     "name": "Tocsin",
     "iconID": "monsters_ld2:161",
     "monsterClass": "animal",
     "phraseID": "tocsin_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tocsin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tocsin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tocsin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tocsin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
