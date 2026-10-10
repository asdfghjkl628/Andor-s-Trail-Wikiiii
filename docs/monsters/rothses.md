---
description: "Rothses is a non-player character (NPC) in Andor's Trail, found in Remgard. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_ld1_14.png){ .sprite } Rothses

**Where to find Rothses:** Remgard: [Remgard armour](../maps/remgard_armour.md#pin-npc-rothses)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_14.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper |
| **Found in** | Remgard |
| **Introduced** | v0.7.0 or earlier |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Remgard shield](../items/remgard_shield_1.md) | 100% | 1 |
| [Combat helm](../items/helm_combat1.md) | 100% | 1 |
| [Enhanced combat helmet](../items/helm_combat2.md) | 100% | 1 |
| [Remgard combat helmet](../items/helm_combat3.md) | 100% | 1 |
| [Defender's helmet](../items/helm_defend1.md) | 100% | 1 |
| [Gloves of the guardian](../items/gloves_guard1.md) | 100% | 1 |
| [Combat boots](../items/boots_combat1.md) | 100% | 1 |
| [Enhanced combat boots](../items/boots_combat2.md) | 100% | 1 |
| [Remgard boots](../items/boots_remgard1.md) | 100% | 1 |
| [Boots of the guardian](../items/boots_guard1.md) | 100% | 1 |
| [Lightweight splint mail](../items/ltbdy_spmail.md) | 100% | 1 |
| [Worn splint mail](../items/spmail2.md) | 100% | 1 |
| [Heavy plated boots](../items/hboot_plat.md) | 100% | 1 |

## Quests

- [Everything in order](../quests/remgard.md): stages 64, 70

## Dialogue simulator

Talk to Rothses as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/rothses.json" data-npc="Rothses" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (35 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-rothses"></span>**`rothses`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 45 of [What is that stench?](../quests/remgard2.md#stage-45))* → [rothses_c1](#d-rothses_c1)
    - branch 2 → [rothses_1](#d-rothses_1)

    <span id="d-rothses_c1"></span>**`rothses_c1`** Rothses: “Our hero enters my shop. I am honored. How may I help you? A new set of boots perhaps, or some new gloves?”

    - “Let me see what you have for sale.” → *shop opens*
    - “Jhaeld told me you could help me improve my equipment.” *(if reached stage 45 of [What is that stench?](../quests/remgard2.md#stage-45))* → [rothses_c2](#d-rothses_c2)

    <span id="d-rothses_1"></span>**`rothses_1`** Rothses: “Hi. How may I help you? A new set of boots perhaps, or some new gloves?”

    - “Let me see what you have for sale.” → *shop opens*
    - “Jhaeld sent me to ask you about the people that have gone missing.” *(if reached stage 52 of [Everything in order](../quests/remgard.md#stage-52))* → [rothses_3s](#d-rothses_3s)
    - “How is business?” → [rothses_2](#d-rothses_2)

    <span id="d-rothses_c2"></span>**`rothses_c2`** Rothses: “Oh yes, I can make modifications to most of our defensive equipment that I sell. Want me to look through your things to see if there's anything I can improve for you?”

    - “Sure, go ahead.” → [rothses_imp_s0](#d-rothses_imp_s0)
    - “No, I would not want you going through my stuff.” → [rothses_c3](#d-rothses_c3)
    - “Maybe some other time.” → [rothses_c3](#d-rothses_c3)

    <span id="d-rothses_3s"></span>**`rothses_3s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 64 of [Everything in order](../quests/remgard.md#stage-64))* → [rothses_19](#d-rothses_19)
    - branch 2 → [rothses_3](#d-rothses_3)

    <span id="d-rothses_2"></span>**`rothses_2`** Rothses: “It's OK, I guess. Not as good as I would like it to be, now that the gates to the town are closed. But people here still seem to need new pieces of leather every now and then.”

    - “Let me see what you have for sale.” → *shop opens*
    - “Jhaeld sent me to ask you about the people that have gone missing.” *(if reached stage 52 of [Everything in order](../quests/remgard.md#stage-52))* → [rothses_3s](#d-rothses_3s)

    <span id="d-rothses_imp_s0"></span>**`rothses_imp_s0`** Rothses: “Hmm, let me see.”

    - Next → [rothses_imp_s](#d-rothses_imp_s)

    <span id="d-rothses_c3"></span>**`rothses_c3`** Rothses: “Sure. I would be honored to have you back if you change your mind.”


    <span id="d-rothses_19"></span>**`rothses_19`** Rothses: “Look, I told you before.”

    - Next → [rothses_20](#d-rothses_20)

    <span id="d-rothses_3"></span>**`rothses_3`** Rothses: “Oh, I don't know much about that. Funny you should ask. [Rothses gives you a suspicious look]”

    - “Are you sure? Anything you know or might have seen may be of interest.” → [rothses_4](#d-rothses_4)

    <span id="d-rothses_imp_s"></span>**`rothses_imp_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if carry 1× [Remgard shield](../items/remgard_shield_1.md))* → [rothses_imp_shield](#d-rothses_imp_shield)
    - branch 2 *(if wearing [Remgard shield](../items/remgard_shield_1.md))* → [rothses_imp_shield_w](#d-rothses_imp_shield_w)
    - branch 3 → [rothses_imp_s3](#d-rothses_imp_s3)

    <span id="d-rothses_20"></span>**`rothses_20`** Rothses: “Now, if you'll excuse me, I have things to do.”


    <span id="d-rothses_4"></span>**`rothses_4`** Rothses: “Well, you would think that I see most of what is going on here, considering my shop is this close to Remgard's connecting entrance bridge.”

    - Next → [rothses_5](#d-rothses_5)

    <span id="d-rothses_imp_shield"></span>**`rothses_imp_shield`** Rothses: “That's a nice looking Remgard shield you have there. For 700 gold, I am able to improve it so that it blocks blows a bit better.”

    - “Sure, here is the gold.” *(if pay 700 gold; hand over 1× [Remgard shield](../items/remgard_shield_1.md))* → [rothses_imp_shield_2](#d-rothses_imp_shield_2)
    - “Maybe later. Do I have anything else that you can improve?” → [rothses_imp_s3](#d-rothses_imp_s3)

    <span id="d-rothses_imp_shield_w"></span>**`rothses_imp_shield_w`** Rothses: “That's a nice looking Remgard shield you are wearing. Remove it from your hands and I might be able to help you improve it, if you want.”

    - “Anything else?” → [rothses_imp_s3](#d-rothses_imp_s3)

    <span id="d-rothses_imp_s3"></span>**`rothses_imp_s3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if carry 1× [Combat gloves](../items/gloves_combat1.md))* → [rothses_imp_gloves](#d-rothses_imp_gloves)
    - branch 2 *(if wearing [Combat gloves](../items/gloves_combat1.md))* → [rothses_imp_gloves_w](#d-rothses_imp_gloves_w)
    - branch 3 → [rothses_imp_s4](#d-rothses_imp_s4)

    <span id="d-rothses_5"></span>**`rothses_5`** Rothses: “However, I don't know anything about it. *cough*”

    - “Is there something you are not telling me?” → [rothses_7](#d-rothses_7)
    - “Did the guards ask you about what you know?” → [rothses_6](#d-rothses_6)

    <span id="d-rothses_imp_shield_2"></span>**`rothses_imp_shield_2`** Rothses: “Here you go. One improved Remgard shield.” — **effects:** gives [Remgard combat shield](../items/remgard_shield_2.md)

    - “Do I have anything else that you can improve?” → [rothses_imp_s3](#d-rothses_imp_s3)

    <span id="d-rothses_imp_gloves"></span>**`rothses_imp_gloves`** Rothses: “Those are some nice looking combat gloves you have there. For 300 gold, I am able to improve them so that they block blows a bit better.”

    - “Sure, here is the gold.” *(if pay 300 gold; hand over 1× [Combat gloves](../items/gloves_combat1.md))* → [rothses_imp_gloves_2](#d-rothses_imp_gloves_2)
    - “Maybe later. Do I have anything else that you can improve?” → [rothses_imp_s4](#d-rothses_imp_s4)

    <span id="d-rothses_imp_gloves_w"></span>**`rothses_imp_gloves_w`** Rothses: “Those are some nice looking combat gloves you are wearing. Remove them from your hands and I might be able to help you improve them, if you want.”

    - “Anything else?” → [rothses_imp_s4](#d-rothses_imp_s4)

    <span id="d-rothses_imp_s4"></span>**`rothses_imp_s4`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if carry 1× [Superior chain mail](../items/armour_superior_chain.md))* → [rothses_imp_armour](#d-rothses_imp_armour)
    - branch 2 *(if wearing [Superior chain mail](../items/armour_superior_chain.md))* → [rothses_imp_armour_w](#d-rothses_imp_armour_w)
    - branch 3 → [rothses_imp_s5](#d-rothses_imp_s5)

    <span id="d-rothses_7"></span>**`rothses_7`** Rothses: “I did see Bethir the night before she disappeared. She had some equipment to sell. Nothing out of the ordinary though.”

    - Next → [rothses_8](#d-rothses_8)

    <span id="d-rothses_6"></span>**`rothses_6`** Rothses: “Oh yes, they've been around asking everyone. I told them everything I know, already.”

    - Next → [rothses_7](#d-rothses_7)

    <span id="d-rothses_imp_gloves_2"></span>**`rothses_imp_gloves_2`** Rothses: “Here you go. One pair of improved combat gloves.” — **effects:** gives [Enhanced combat gloves](../items/gloves_combat2.md)

    - “Do I have anything else that you can improve?” → [rothses_imp_s4](#d-rothses_imp_s4)

    <span id="d-rothses_imp_armour"></span>**`rothses_imp_armour`** Rothses: “Now that is one fine looking chain mail you have there! For 3,000 gold, I am able to improve it so that it not only blocks blows better, but also hinders your attacks less.”

    - “Sure, here is the gold.” *(if pay 3,000 gold; hand over 1× [Superior chain mail](../items/armour_superior_chain.md))* → [rothses_imp_armour_2](#d-rothses_imp_armour_2)
    - “Maybe later. Do I have anything else that you can improve?” → [rothses_imp_s5](#d-rothses_imp_s5)

    <span id="d-rothses_imp_armour_w"></span>**`rothses_imp_armour_w`** Rothses: “Now that is one fine looking chain mail you are wearing. Remove it from your chest and I might be able to help you improve it, if you want.”

    - “Anything else?” → [rothses_imp_s5](#d-rothses_imp_s5)

    <span id="d-rothses_imp_s5"></span>**`rothses_imp_s5`** *(silent check: the first matching branch below is taken)*

    - branch 1 → [rothses_imp_n](#d-rothses_imp_n)

    <span id="d-rothses_8"></span>**`rothses_8`** Rothses: “I did not see where she went after that.”

    - Next → [rothses_9](#d-rothses_9)

    <span id="d-rothses_imp_armour_2"></span>**`rothses_imp_armour_2`** Rothses: “Here you go. One improved chain mail.” — **effects:** gives [Remgard chain mail](../items/armour_chain_remg.md)

    - “Do I have anything else that you can improve?” → [rothses_imp_s5](#d-rothses_imp_s5)

    <span id="d-rothses_imp_n"></span>**`rothses_imp_n`** Rothses: “No, you don't seem to have anything that I can improve. Come back later and I might be able to help you.”


    <span id="d-rothses_9"></span>**`rothses_9`** Rothses: “Look, I told all this to the guards before. Are you implying anything?”

    - “I'll keep my eye on you.” → [rothses_jhaeld_s_1](#d-rothses_jhaeld_s_1)
    - “Thank you for your cooperation.” → [rothses_jhaeld_s_1](#d-rothses_jhaeld_s_1)

    <span id="d-rothses_jhaeld_s_1"></span>**`rothses_jhaeld_s_1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 64 of [Everything in order](../quests/remgard.md#stage-64)

    - branch 1 *(if reached stage 61 of [Everything in order](../quests/remgard.md#stage-61))* → [rothses_jhaeld_s_2](#d-rothses_jhaeld_s_2)
    - branch 2 → [rothses_20](#d-rothses_20)

    <span id="d-rothses_jhaeld_s_2"></span>**`rothses_jhaeld_s_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 62 of [Everything in order](../quests/remgard.md#stage-62))* → [rothses_jhaeld_s_3](#d-rothses_jhaeld_s_3)
    - branch 2 → [rothses_20](#d-rothses_20)

    <span id="d-rothses_jhaeld_s_3"></span>**`rothses_jhaeld_s_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 63 of [Everything in order](../quests/remgard.md#stage-63))* → [rothses_jhaeld_s_4](#d-rothses_jhaeld_s_4)
    - branch 2 → [rothses_20](#d-rothses_20)

    <span id="d-rothses_jhaeld_s_4"></span>**`rothses_jhaeld_s_4`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 70 of [Everything in order](../quests/remgard.md#stage-70)

    - branch 1 → [rothses_20](#d-rothses_20)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 10 lines changed<br>· text: “It's ok, I guess. Not as good as I would like it to be, now that the …” → “It's OK, I guess. Not as good as I would like it to be, now that the …”<br>· text: “Oh, I don't know much about that. Funny you should ask. (Rothses give…” → “Oh, I don't know much about that. Funny you should ask. [Rothses give…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “Now that is one fine looking chain mail you have there! For 3000 gold…” → “Now that is one fine looking chain mail you have there! For {3000} go…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `rothses` |
    | Type (wiki) | NPC |
    | Spawn group | `rothses` |
    | Loot table | `shop_rothses` |
    | Conversation | `rothses` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:14` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "rothses",
     "name": "Rothses",
     "iconID": "monsters_ld1:14",
     "monsterClass": "humanoid",
     "spawnGroup": "rothses",
     "phraseID": "rothses",
     "droplistID": "shop_rothses"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rothses.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rothses.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rothses.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rothses.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
