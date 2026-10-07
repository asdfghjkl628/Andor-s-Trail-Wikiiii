---
description: "Rolwynn is a non-player character (NPC) in Andor's Trail, found in Crossroads Guardhouse. Starts Flows through the veins."
---

# ![](../assets/icons/monsters/monsters_rltiles1_77.png){ .sprite } Rolwynn

**Where to find Rolwynn:** Crossroads Guardhouse: [Fields 0](../maps/fields0.md#pin-npc-rolwynn)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_77.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Starts [Flows through the veins](../quests/loneford.md) |
| **Found in** | Crossroads Guardhouse |
| **Entry ID** | `rolwynn` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Flows through the veins](../quests/loneford.md): stages 10, 11, 22, 25

## Dialogue simulator

Set your quest stages and items, then talk to Rolwynn. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/rolwynn.json" data-npc="Rolwynn" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (20 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-rolwynn"></span>**`rolwynn`** Rolwynn: “What have we done to deserve this? Please, will you help us?”

    - “What do you think is the cause of the illness?” *(if reached stage 11 of [Flows through the veins](../quests/loneford.md#stage-11))* → [rolwynn_1](#d-rolwynn_1)
    - “What's wrong?” → [loneford_farmer0_1](#d-loneford_farmer0_1)

    <span id="d-rolwynn_1"></span>**`rolwynn_1`** Rolwynn: “My guess is that this must be something done by those arrogant people from Feygard.”

    - Next → [rolwynn_2](#d-rolwynn_2)

    <span id="d-loneford_farmer0_1"></span>**`loneford_farmer0_1`** Rolwynn: “Didn't you hear about the illness?”

    - “What illness?” → [loneford_farmer_il_1](#d-loneford_farmer_il_1)

    <span id="d-rolwynn_2"></span>**`rolwynn_2`** Rolwynn: “They are always looking for ways to make our lives a little bit harder.”

    - Next → [rolwynn_3](#d-rolwynn_3)

    <span id="d-loneford_farmer_il_1"></span>**`loneford_farmer_il_1`** Rolwynn: “It all started a few days ago. Selgan found Hesor passed out on his old crop field, completely white faced and shivering.”

    - Next → [loneford_farmer_il_2](#d-loneford_farmer_il_2)

    <span id="d-rolwynn_3"></span>**`rolwynn_3`** Rolwynn: “We try to farm our lands to feed ourselves, but they demand that they get a share of whatever we bring in.”

    - Next → [rolwynn_4](#d-rolwynn_4)

    <span id="d-loneford_farmer_il_2"></span>**`loneford_farmer_il_2`** Rolwynn: “A few days later, Selgan started showing the same symptoms as Hesor, with stomach aches. I also started feeling the pains and got the shivers.”

    - Next → [loneford_farmer_il_3](#d-loneford_farmer_il_3)

    <span id="d-rolwynn_4"></span>**`rolwynn_4`** Rolwynn: “Lately, the crops haven't been as good as they used to be, and the guards apparently think we are withholding some part of their share.”

    - Next → [rolwynn_5](#d-rolwynn_5)

    <span id="d-loneford_farmer_il_3"></span>**`loneford_farmer_il_3`** Rolwynn: “Then, all people showed the symptoms in one way or another.”

    - Next → [loneford_farmer_il_4](#d-loneford_farmer_il_4)

    <span id="d-rolwynn_5"></span>**`rolwynn_5`** Rolwynn: “I am sure that they did something to us as punishment for not following their *rules*. They are always talking about how the laws and rules are so precious to them.” — **effects:** sets stage 22 of [Flows through the veins](../quests/loneford.md#stage-22)

    - Next → [loneford_ill_c_1](#d-loneford_ill_c_1)

    <span id="d-loneford_farmer_il_4"></span>**`loneford_farmer_il_4`** Rolwynn: “Poor old Selgan and Hesor apparently got the worst of it, and both died the day before yesterday.”

    - Next → [loneford_farmer_il_5](#d-loneford_farmer_il_5)

    <span id="d-loneford_ill_c_1"></span>**`loneford_ill_c_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 21 of [Flows through the veins](../quests/loneford.md#stage-21))* → [loneford_ill_c_2](#d-loneford_ill_c_2)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-loneford_farmer_il_5"></span>**`loneford_farmer_il_5`** Rolwynn: “Cursed illness, why did it have to be Selgan and Hesor? I wonder who is next.”

    - Next → [loneford_farmer_il_6](#d-loneford_farmer_il_6)

    <span id="d-loneford_ill_c_2"></span>**`loneford_ill_c_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 22 of [Flows through the veins](../quests/loneford.md#stage-22))* → [loneford_ill_c_3](#d-loneford_ill_c_3)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-loneford_ill_c_n"></span>**`loneford_ill_c_n`** Rolwynn: “That's what I think anyway.”


    <span id="d-loneford_farmer_il_6"></span>**`loneford_farmer_il_6`** Rolwynn: “We all started to investigate what could be the cause. We still aren't certain what the cause is, but we have our suspicions.” — **effects:** sets stage 10 of [Flows through the veins](../quests/loneford.md#stage-10)

    - Next → [loneford_farmer_il_7](#d-loneford_farmer_il_7)

    <span id="d-loneford_ill_c_3"></span>**`loneford_ill_c_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 23 of [Flows through the veins](../quests/loneford.md#stage-23))* → [loneford_ill_c_4](#d-loneford_ill_c_4)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-loneford_farmer_il_7"></span>**`loneford_farmer_il_7`** Rolwynn: “Luckily, now Feygard has sent patrols up here to help guard the village at least. We are still suffering though, and we fear who will be taken by the illness next.” — **effects:** sets stage 11 of [Flows through the veins](../quests/loneford.md#stage-11)


    <span id="d-loneford_ill_c_4"></span>**`loneford_ill_c_4`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 24 of [Flows through the veins](../quests/loneford.md#stage-24))* → [loneford_ill_c_5](#d-loneford_ill_c_5)
    - branch 2 → [loneford_ill_c_n](#d-loneford_ill_c_n)

    <span id="d-loneford_ill_c_5"></span>**`loneford_ill_c_5`** Rolwynn: “There's something else also. I talked to that drunk, Landa, in the tavern earlier today. He said he saw something but didn't dare tell me what it was.” — **effects:** sets stage 25 of [Flows through the veins](../quests/loneford.md#stage-25)

    - “Thank you, I will go talk to him.” → *conversation ends*
    - “Great, another drunk that I have to talk to.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 5 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `rolwynn` |
    | Spawn group | `rolwynn` |
    | Loot table | – |
    | Conversation | `rolwynn` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:77` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "rolwynn",
     "name": "Rolwynn",
     "iconID": "monsters_rltiles1:77",
     "monsterClass": "humanoid",
     "spawnGroup": "rolwynn",
     "phraseID": "rolwynn"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rolwynn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rolwynn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rolwynn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rolwynn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
