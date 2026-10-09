---
description: "Vilegard smith is a non-player character (NPC) in Andor's Trail, found in Vilegard. Shopkeeper; starts Trusting an outsider."
---

# ![](../assets/icons/monsters/monsters_mage2_0.png){ .sprite } Vilegard smith

**Where to find Vilegard smith:** Vilegard: [Vilegard smith](../maps/vilegard_smith.md#pin-npc-vilegard_smith)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_mage2_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Role** | Shopkeeper; starts [Trusting an outsider](../quests/vilegard.md) |
| **Found in** | Vilegard |
| **Entry ID** | `vilegard_smith` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Giant hammer](../items/hammer1.md) | 100% | 1 |
| [Fine wooden club](../items/club_fine_wooden.md) | 100% | 1 |
| [Hardened iron longsword](../items/longsword_hard_iron.md) | 100% | 1 |
| [Fine iron axe](../items/axe_fine_iron.md) | 100% | 1 |
| [Hardened iron sword](../items/sword_hard_iron.md) | 100% | 1 |
| [Claymore of the berserker](../items/clmr_bers.md) | 100% | 1 |
| [Massive two-handed sword](../items/clmr_msv.md) | 100% | 1 |
| [Fine iron broadsword](../items/broadsword_fine_iron.md) | 100% | 1 |
| [Steel broadsword](../items/broadsword2.md) | 100% | 1 |
| [Fencing blade](../items/sword_fencing.md) | 100% | 1 |
| [Steel spear](../items/spear_steel.md) | 100% | 1 |

## Quests

- [A creeping fear](../quests/xulviir.md): stages 20, 30
- [Feygard errands](../quests/feygard_shipment.md): stages 55, 56
- [Trusting an outsider](../quests/vilegard.md): stage 10

## Dialogue simulator

Set your quest stages and items, then talk to Vilegard smith. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/vilegard_smith_select.json" data-npc="Vilegard smith" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (29 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-vilegard_smith_select"></span>**`vilegard_smith_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 56 of [Feygard errands](../quests/feygard_shipment.md#stage-56))* → [vilegard_smith_1](#d-vilegard_smith_1)
    - branch 2 *(if reached stage 55 of [Feygard errands](../quests/feygard_shipment.md#stage-55))* → [vilegard_smith_fg_2](#d-vilegard_smith_fg_2)
    - branch 3 *(if reached stage 30 of [Trusting an outsider](../quests/vilegard.md#stage-30))* → [vilegard_smith_1](#d-vilegard_smith_1)
    - branch 4 → [vilegard_shop_notrust_smith](#d-vilegard_shop_notrust_smith)

    <span id="d-vilegard_smith_1"></span>**`vilegard_smith_1`** Vilegard smith: “Hello there. I heard you helped us here in Vilegard. What can I help you with?”

    - “Can I see what items you have for sale?” → *shop opens*
    - “I have a shipment of Feygard items for you.” *(if reached stage 35 of [Feygard errands](../quests/feygard_shipment.md#stage-35); hand over 10× [Feygard iron sword](../items/fg_ironsword.md))* → [vilegard_smith_fg_1](#d-vilegard_smith_fg_1)
    - “On the body of something called the Hira'zinn, I found this peculiar sword. Do you know anything about it?” *(if carry 1× [Broken sword](../items/xulviir0.md))* → [vilegard_smith_xul_1](#d-vilegard_smith_xul_1)

    <span id="d-vilegard_smith_fg_2"></span>**`vilegard_smith_fg_2`** Vilegard smith: “Thank you for bringing me these items, they will be most useful to us here in the southern lands, and Vilegard in particular. We rarely get our hands on Feygard items, so these are really welcome.”

    - “I was sent to deliver these items to a Feygard patrol stationed in the Foaming Flask tavern.” → [vilegard_smith_fg_3](#d-vilegard_smith_fg_3)

    <span id="d-vilegard_shop_notrust_smith"></span>**`vilegard_shop_notrust_smith`** Vilegard smith: “You are an outsider. We don't like outsiders here in Vilegard. Please leave.”

    - “Why is everyone in Vilegard so suspicious of outsiders?” → [vilegard_shop_notrust_2](#d-vilegard_shop_notrust_2)
    - “Can I see what items you have for sale?” → [vilegard_shop_notrust_2](#d-vilegard_shop_notrust_2)
    - “I have a shipment of Feygard items for you.” *(if reached stage 35 of [Feygard errands](../quests/feygard_shipment.md#stage-35); carry 10× [Feygard iron sword](../items/fg_ironsword.md))* → [vilegard_shop_notrust_2](#d-vilegard_shop_notrust_2)
    - “On the body of something called the Hira'zinn, I found this peculiar sword. Do you know anything about it?” *(if carry 1× [Broken sword](../items/xulviir0.md))* → [vilegard_shop_notrust_2](#d-vilegard_shop_notrust_2)

    <span id="d-vilegard_smith_fg_1"></span>**`vilegard_smith_fg_1`** Vilegard smith: “Oh, this is most unexpected but very welcome. I will not question how you acquired these items, but instead express my gratitude for bringing them to me.” — **effects:** sets stage 55 of [Feygard errands](../quests/feygard_shipment.md#stage-55)

    - Next → [vilegard_smith_fg_2](#d-vilegard_smith_fg_2)

    <span id="d-vilegard_smith_xul_1"></span>**`vilegard_smith_xul_1`** Vilegard smith: “[Takes a step back] What ... is ... that? It can't be? No. Let me look at it.”

    - Next → [vilegard_smith_xul_2](#d-vilegard_smith_xul_2)

    <span id="d-vilegard_smith_fg_3"></span>**`vilegard_smith_fg_3`** Vilegard smith: “Instead, you brought them to me. You have my thanks.”

    - Next → [vilegard_smith_fg_4](#d-vilegard_smith_fg_4)

    <span id="d-vilegard_shop_notrust_2"></span>**`vilegard_shop_notrust_2`** Vilegard smith: “I don't trust you. You should go see Jolnor in the chapel if you want some sympathy.” — **effects:** sets stage 10 of [Trusting an outsider](../quests/vilegard.md#stage-10)


    <span id="d-vilegard_smith_xul_2"></span>**`vilegard_smith_xul_2`** Vilegard smith: “It has all the markings. But it can't be? I don't understand.”

    - “What is it?” → [vilegard_smith_xul_3](#d-vilegard_smith_xul_3)

    <span id="d-vilegard_smith_fg_4"></span>**`vilegard_smith_fg_4`** Vilegard smith: “Hah, this means that we have another opportunity here. What if you were to deliver some other items to the Feygard patrol instead? Hah, this will really make my day.”

    - Next → [vilegard_smith_fg_5](#d-vilegard_smith_fg_5)

    <span id="d-vilegard_smith_xul_3"></span>**`vilegard_smith_xul_3`** Vilegard smith: “This thing that you have stumbled upon, my friend. This is the Xul'viir. A most foul item indeed.”

    - Next → [vilegard_smith_xul_4](#d-vilegard_smith_xul_4)

    <span id="d-vilegard_smith_fg_5"></span>**`vilegard_smith_fg_5`** Vilegard smith: “I might have something that will do just fine... Let me just find them.”

    - Next → [vilegard_smith_fg_6](#d-vilegard_smith_fg_6)

    <span id="d-vilegard_smith_xul_4"></span>**`vilegard_smith_xul_4`** Vilegard smith: “It has been said that King Luthor destroyed the sword so that it would not fall into the wrong hands.”

    - Next → [vilegard_smith_xul_5](#d-vilegard_smith_xul_5)

    <span id="d-vilegard_smith_fg_6"></span>**`vilegard_smith_fg_6`** Vilegard smith: “Here they are. Ha ha, these will do just fine for those deceiving Feygard snobs.”

    - Next → [vilegard_smith_fg_7](#d-vilegard_smith_fg_7)

    <span id="d-vilegard_smith_xul_5"></span>**`vilegard_smith_xul_5`** Vilegard smith: “It would seem that either he, or the stories have not been telling the truth.”

    - Next → [vilegard_smith_xul_6](#d-vilegard_smith_xul_6)

    <span id="d-vilegard_smith_fg_7"></span>**`vilegard_smith_fg_7`** Vilegard smith: “Take these items and deliver them to wherever you were supposed to deliver the items you gave me.” — **effects:** sets stage 56 of [Feygard errands](../quests/feygard_shipment.md#stage-56), gives [Degraded Feygard iron sword](../items/fg_ironsword_d.md)


    <span id="d-vilegard_smith_xul_6"></span>**`vilegard_smith_xul_6`** Vilegard smith: “If restored, anyone wielding it would make their enemies tremble from only the sight of it.”

    - Next → [vilegard_smith_xul_7](#d-vilegard_smith_xul_7)

    <span id="d-vilegard_smith_xul_7"></span>**`vilegard_smith_xul_7`** Vilegard smith: “You must destroy it, of course. Here, put it into my smelting pit and we'll be rid of it.”

    - “Here it is. We had better get rid of it.” *(if hand over 1× [Broken sword](../items/xulviir0.md))* → [vilegard_smith_xul_8](#d-vilegard_smith_xul_8)
    - “I'd like to keep it.” → [vilegard_smith_xul_9](#d-vilegard_smith_xul_9)

    <span id="d-vilegard_smith_xul_8"></span>**`vilegard_smith_xul_8`** Vilegard smith: “Into the smelting pit with it. Good. See how it bubbles and flares? That's the lives of countless people thanking you for destroying it.” — **effects:** sets stage 30 of [A creeping fear](../quests/xulviir.md#stage-30)


    <span id="d-vilegard_smith_xul_9"></span>**`vilegard_smith_xul_9`** Vilegard smith: “You can't be serious. It needs to be destroyed!”

    - “Here it is. We had better get rid of it.” *(if hand over 1× [Broken sword](../items/xulviir0.md))* → [vilegard_smith_xul_8](#d-vilegard_smith_xul_8)
    - “You mentioned restoring it before, what would that entail?” → [vilegard_smith_xul_10](#d-vilegard_smith_xul_10)

    <span id="d-vilegard_smith_xul_10"></span>**`vilegard_smith_xul_10`** Vilegard smith: “The original sword had ornaments of rare crystals, and a blade that was as sharp as nothing else.”

    - Next → [vilegard_smith_xul_11](#d-vilegard_smith_xul_11)

    <span id="d-vilegard_smith_xul_11"></span>**`vilegard_smith_xul_11`** Vilegard smith: “I can't believe I'm telling you this. Give. It. Here. Now! It needs to be destroyed!”

    - “Here it is. We had better get rid of it.” *(if hand over 1× [Broken sword](../items/xulviir0.md))* → [vilegard_smith_xul_8](#d-vilegard_smith_xul_8)
    - “How about you get to work on restoring it, and I won't kill you.” → [vilegard_smith_xul_12](#d-vilegard_smith_xul_12)

    <span id="d-vilegard_smith_xul_12"></span>**`vilegard_smith_xul_12`** Vilegard smith: “I ... what? Are you threatening me?”

    - “You won't believe what I had to go through to get it.” → [vilegard_smith_xul_13](#d-vilegard_smith_xul_13)

    <span id="d-vilegard_smith_xul_13"></span>**`vilegard_smith_xul_13`** Vilegard smith: “Sigh. You don't know what you are getting yourself into, kid.”

    - Next → [vilegard_smith_xul_14](#d-vilegard_smith_xul_14)

    <span id="d-vilegard_smith_xul_14"></span>**`vilegard_smith_xul_14`** Vilegard smith: “Regardless, to restore the sword to its former shape, I'd need some of those crystals that it was adorned with, and those crystals are really hard to come by.”

    - Next → [vilegard_smith_xul_15](#d-vilegard_smith_xul_15)

    <span id="d-vilegard_smith_xul_15"></span>**`vilegard_smith_xul_15`** Vilegard smith: “I think they are called Oegyth or something like that. The sword had three of them on its hilt.”

    - “Never mind. Here is the sword. We had better destroy it.” *(if hand over 1× [Broken sword](../items/xulviir0.md))* → [vilegard_smith_xul_8](#d-vilegard_smith_xul_8)
    - “I'll go find some of those crystals.” → [vilegard_smith_xul_16](#d-vilegard_smith_xul_16)
    - “I have three of those crystals right here.” *(if carry 3× [Oegyth crystal](../items/oegyth.md))* → [vilegard_smith_xul_17](#d-vilegard_smith_xul_17)

    <span id="d-vilegard_smith_xul_16"></span>**`vilegard_smith_xul_16`** Vilegard smith: “Pfft. Run along now, and don't threaten anyone else, you hear?”


    <span id="d-vilegard_smith_xul_17"></span>**`vilegard_smith_xul_17`** Vilegard smith: “You continue to amaze me. Now, are you really sure that you want to do this? The lives of the people that it has slain will haunt you.”

    - “I'm sure. Here is the sword and three of those crystals. Restore it to how it once was.” *(if hand over 3× [Oegyth crystal](../items/oegyth.md); hand over 1× [Broken sword](../items/xulviir0.md))* → [vilegard_smith_xul_19](#d-vilegard_smith_xul_19)
    - “Never mind. Here is the sword. We had better destroy it.” *(if hand over 1× [Broken sword](../items/xulviir0.md))* → [vilegard_smith_xul_8](#d-vilegard_smith_xul_8)

    <span id="d-vilegard_smith_xul_19"></span>**`vilegard_smith_xul_19`** Vilegard smith: “Sigh. OK, whatever you say. We just need to fit these into there, and sharpen up this bit here. There. It should be almost like it once was.” — **effects:** sets stage 20 of [A creeping fear](../quests/xulviir.md#stage-20), gives [Xul'viir](../items/xulviir.md)

    - “Thanks.” → [vilegard_smith_xul_16](#d-vilegard_smith_xul_16)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line added, 6 lines changed<br>· text: “[takes a step back] What.. is.. that? It can't be? No. Let me look at…” → “[Takes a step back] What ... is ... that? It can't be? No. Let me loo…”<br>· text: “Sigh. Ok, whatever you say. We just need to fit these into there, and…” → “Sigh. OK, whatever you say. We just need to fit these into there, and…” |
| [v0.7.11](../versions/0.7.11.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `vilegard_smith` |
    | Spawn group | `vg_smith` |
    | Loot table | `shop_vg_smith` |
    | Conversation | `vilegard_smith_select` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage2:0` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "vilegard_smith",
     "name": "Vilegard smith",
     "iconID": "monsters_mage2:0",
     "monsterClass": "humanoid",
     "spawnGroup": "vg_smith",
     "phraseID": "vilegard_smith_select",
     "droplistID": "shop_vg_smith"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vilegard_smith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vilegard_smith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vilegard_smith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=vilegard_smith.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
