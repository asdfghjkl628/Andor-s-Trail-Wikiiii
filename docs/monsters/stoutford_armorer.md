---
description: "Odirath is a non-player character (NPC) in Andor's Trail, found in Stoutford. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_ld1_10.png){ .sprite } Odirath

**Where to find Odirath:** Stoutford: [Stoutford armorer](../maps/stoutford_armorer.md#pin-npc-stoutford_armorer)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_10.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper |
| **Found in** | Stoutford |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Reinforced leather buckler](../items/shield_leather.md) | 100% | 1 |
| [Chainmail tunic](../items/tunic_chainmail.md) | 100% | 1 |
| [Superior leather armor](../items/armor2.md) | 100% | 1 |
| [Crude wooden shield](../items/shield4.md) | 100% | 1 |
| [Steel helm](../items/helm_steel.md) | 100% | 1 |
| [Hardened leather cap](../items/hat_hard_leather.md) | 100% | 1 |
| [Crude iron shield](../items/shield_iron1.md) | 100% | 1 |
| [Iron shield](../items/shield_iron2.md) | 100% | 1 |
| [Superior iron shield](../items/shield_iron3.md) | 100% | 1 |
| [Chainmail mittens](../items/hglv_chml.md) | 100% | 1 |
| [Steel cuirass](../items/cuirass_steel.md) | 100% | 1 |
| [Hardened leather gloves](../items/gloves_leather1.md) | 100% | 1 |
| [Armored gloves](../items/armored_gloves.md) | 100% | 1 |

## Quests

- [Lost girl looking for lost things](../quests/stn_quest_gyra.md): stages 10, 70, 170
- [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md): stage 30
- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stage 9

## Dialogue simulator

Talk to Odirath as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/odirath_0.json" data-npc="Odirath" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (20 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-odirath_0"></span>**`odirath_0`** Odirath: “Welcome to my shop. Are you looking for anything in particular?”

    - “Please show me everything you have available.” → *shop opens*
    - “I am looking for my brother, Andor. Have you seen anyone recently that looks a bit like me?” → [odirath_1](#d-odirath_1)
    - “Can you tell me anything about Stoutford?” → [odirath_1_1](#d-odirath_1_1)
    - “You look a bit worried.” *(if NOT reached stage 10 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-10); NOT reached stage 60 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-60))* → [odirath_2](#d-odirath_2)
    - “You look happy again.” *(if reached stage 60 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-60))* → [odirath_3](#d-odirath_3)
    - “Did you really order such an ugly porcelain figure? Oops, sorry I didn't mean to offend you.” *(if hand over 1× [Pretty porcelain figure](../items/brv_wh_item_07.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 40 of [Delivery](../quests/brv_wh_delivery.md#stage-40))* → [brv_wh_delivery_odirath](#d-brv_wh_delivery_odirath)
    - “I have tried to open the southern castle gate, but the mechanism seems broken. Can you repair it?” *(if reached stage 5 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-5); NOT reached stage 9 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-9))* → [odirath_8](#d-odirath_8)

    <span id="d-odirath_1"></span>**`odirath_1`** Odirath: “I did see someone that might have been your brother. He was with a rather dubious looking person. They didn't stay around here very long though. Sorry, but that's all I can tell you. You should ask around town. Other townsfolk may know…”

    - “Thanks. I'll go and do that now.” → *conversation ends*
    - “Please show me what you have to trade.” → *shop opens*
    - “OK. Can you tell me anything about Stoutford?” → [odirath_1_1](#d-odirath_1_1)

    <span id="d-odirath_1_1"></span>**`odirath_1_1`** Odirath: “Stoutford is a small town, and life used to be easy here. A lot of traders stayed in Stoutford on their way to and from Blackwater mountain, and spent money that boosted the economy of the whole town. Those days are gone though.”

    - “What happened?” → [odirath_1_2](#d-odirath_1_2)

    <span id="d-odirath_2"></span>**`odirath_2`** Odirath: “Yes, indeed. My daughter has not come home for some days. I don't know what's happened to her.”

    - “And you have no idea where she might be?” → [odirath_2_1](#d-odirath_2_1)

    <span id="d-odirath_3"></span>**`odirath_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 99 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-99))* → [odirath_3_2](#d-odirath_3_2)
    - branch 2 → [odirath_3_1](#d-odirath_3_1)

    <span id="d-brv_wh_delivery_odirath"></span>**`brv_wh_delivery_odirath`** Odirath: “Yes, indeed. A gift for my beautiful daughter... but why did it take so long? Sigh, here's my delivery fee.” — **effects:** clears stage 40 of [Delivery](../quests/brv_wh_delivery.md#stage-40), sets stage 30 of [Brimhaven warehouse delivery (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-30), gives 30× [Gold coins](../items/gold.md)

    - “Thank you.” → *conversation ends*

    <span id="d-odirath_8"></span>**`odirath_8`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 10 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-10))* → [odirath_8a](#d-odirath_8a)
    - branch 2 *(if NOT reached stage 20 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-20))* → [odirath_8a](#d-odirath_8a)
    - branch 3 *(if NOT reached stage 30 of [Stoutford's old castle](../quests/stoutford_castle.md#stage-30))* → [odirath_8a](#d-odirath_8a)
    - branch 4 *(if NOT reached stage 60 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-60))* → [odirath_8b](#d-odirath_8b)
    - branch 5 → [odirath_8c](#d-odirath_8c)

    <span id="d-odirath_1_2"></span>**`odirath_1_2`** Odirath: “The path to Blackwater mountain was cut off by a rock fall. That stopped most of the traders from coming here. The attacks by the monsters stopped the rest.”

    - “How do I get to Blackwater mountain?” → [odirath_1_3](#d-odirath_1_3)
    - “Monsters?” → [odirath_1_4](#d-odirath_1_4)

    <span id="d-odirath_2_1"></span>**`odirath_2_1`** Odirath: “I've been looking for her all over Stoutford. She does not leave the city. So she can only be in the castle, or kidnapped, or worse.”

    - “Did you already look for her in the castle?” → [odirath_2_2](#d-odirath_2_2)

    <span id="d-odirath_3_2"></span>**`odirath_3_2`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 170 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-170)

    - branch 1 → [odirath_3_3](#d-odirath_3_3)

    <span id="d-odirath_3_1"></span>**`odirath_3_1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 70 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-70)

    - branch 1 → [odirath_3_3](#d-odirath_3_3)

    <span id="d-odirath_8a"></span>**`odirath_8a`** Odirath: “No, sorry. As long as there are still skeletons running around the castle, I can't work there.”

    - “I understand.” → [odirath_0](#d-odirath_0)

    <span id="d-odirath_8b"></span>**`odirath_8b`** Odirath: “I can do that as soon as my daughter is back here.”

    - “I understand.” → [odirath_0](#d-odirath_0)

    <span id="d-odirath_8c"></span>**`odirath_8c`** Odirath: “The gate mechanism is broken? No problem. Now that the skeletons are gone, I can fix it for you.” — **effects:** sets stage 9 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-9)

    - “Great!” → [odirath_0](#d-odirath_0)

    <span id="d-odirath_1_3"></span>**`odirath_1_3`** Odirath: “Just follow the path west, but you will have to find a way past the rockfall.”

    - “Thanks for the directions. I'm headed there right now.” → *conversation ends*
    - “Thanks. What about the monsters?” → [odirath_1_4](#d-odirath_1_4)
    - “Thanks for the information. Please show me what you have to trade.” → *shop opens*

    <span id="d-odirath_1_4"></span>**`odirath_1_4`** Odirath: “They started attacking the town recently. Nobody is sure why. Their attacks have been unsuccessful, so we are all hoping that they will give up soon and go back to wherever they came from.”

    - “Thanks for the information, but I have to leave.” → *conversation ends*
    - “Thanks for the information. Do you have anything to trade?” → *shop opens*
    - “Thanks. I'm looking for my brother, Andor. Has anyone new been through here recently?” → [odirath_1](#d-odirath_1)
    - “How do I get to Blackwater mountain?” → [odirath_1_3](#d-odirath_1_3)

    <span id="d-odirath_2_2"></span>**`odirath_2_2`** Odirath: “You cannot go to the castle anymore, do not you know that? At least not if you want to continue living.”

    - “I see. She will certainly reappear soon. In the meantime you could show me everything you have for sale.” → *shop opens*
    - “I am also looking for someone: my brother, Andor. Have you seen anyone recently that looks a bit like me?” → [odirath_1](#d-odirath_1)
    - “OK. Can you tell me anything about Stoutford?” → [odirath_1_1](#d-odirath_1_1)
    - “I'm not afraid. I could have a look in the castle.” → [odirath_2_3](#d-odirath_2_3)

    <span id="d-odirath_3_3"></span>**`odirath_3_3`** Odirath: “Gyra is back and has told me everything. Many thanks again for your help.”

    - “I was happy to do it.” → [odirath_3_5](#d-odirath_3_5)

    <span id="d-odirath_2_3"></span>**`odirath_2_3`** Odirath: “You would do that for me? I can hardly accept your offer.” — **effects:** sets stage 10 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-10)

    - “I'm on my way.” → *conversation ends*
    - “No problem, but first I have something else I wish to discuss.” → [odirath_0](#d-odirath_0)

    <span id="d-odirath_3_5"></span>**`odirath_3_5`** Odirath: “Please give the helmet to its owner Lord Bourbon - eh, Lord Berbane I mean. He will be in the tavern.”

    - “OK.” → *conversation ends*
    - “I did that already. But he didn't seem to be happy about it.” *(if reached stage 90 of [Lost girl looking for lost things](../quests/stn_quest_gyra.md#stage-90))* → *conversation ends*
    - “I did that already. Although he won't need it, because the castle is already clear of the undead.” *(if reached stage 149 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-149))* → *conversation ends*
    - “Maybe.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 15 lines added |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 1 line added, 1 line changed |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 1 line changed |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 4 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `stoutford_armorer` |
    | Type (wiki) | NPC |
    | Spawn group | `stoutford_armorer` |
    | Loot table | `shop_odirath` |
    | Conversation | `odirath_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:10` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_armorer",
     "name": "Odirath",
     "iconID": "monsters_ld1:10",
     "monsterClass": "humanoid",
     "spawnGroup": "stoutford_armorer",
     "phraseID": "odirath_0",
     "droplistID": "shop_odirath"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_armorer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_armorer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_armorer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_armorer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
