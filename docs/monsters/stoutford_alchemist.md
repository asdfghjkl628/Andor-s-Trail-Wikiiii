---
description: "Blornvale is a non-player character (NPC) in Andor's Trail, found in Stoutford. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_rltiles1_70.png){ .sprite } Blornvale

**Where to find Blornvale:** [Stoutford, Stoutford potion](#v-stoutford_alchemist), [Stoutford, Stoutford potion](#v-stoutford_alchemist2)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_70.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Shopkeeper |
| **Found in** | Stoutford |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Stoutford, Stoutford potion { #v-stoutford_alchemist }

**Where:** Stoutford: [Stoutford potion](../maps/stoutford_potion.md#pin-npc-stoutford_alchemist) · **Role:** Shopkeeper

### Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Soap](../items/soap.md) | 100% | 5 |
| [Regular potion of health](../items/health.md) | 100% | 5 |

### Quests

- [The thorns of vengeance](../quests/thorns_vengeance.md): stages 70, 71, 72, 74, 75, 80
- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stages 201, 202

### Dialogue simulator

Set your quest stages and items, then talk to Blornvale. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/blornvale_select_0.json" data-npc="Blornvale" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (39 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stoutford_alchemist-blornvale_select_0"></span>**`blornvale_select_0`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 75 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-75))* → [blornvale_thorns72_90](#d-stoutford_alchemist-blornvale_thorns72_90)
    - branch 2 *(if reached stage 74 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-74))* → [blornvale_thorns74](#d-stoutford_alchemist-blornvale_thorns74)
    - branch 3 *(if reached stage 72 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-72))* → [blornvale_thorns72](#d-stoutford_alchemist-blornvale_thorns72)
    - branch 4 *(if reached stage 71 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-71))* → [blornvale_thorns70_20](#d-stoutford_alchemist-blornvale_thorns70_20)
    - branch 5 *(if reached stage 70 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-70))* → [blornvale_thorns70](#d-stoutford_alchemist-blornvale_thorns70)
    - branch 6 *(if carry 1× [Potion of truth](../items/potion_truth.md))* → [blornvale_thorns50](#d-stoutford_alchemist-blornvale_thorns50)
    - branch 7 *(if reached stage 202 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-202))* → [blornvale_select_1](#d-stoutford_alchemist-blornvale_select_1)
    - branch 8 → [blornvale_select_2](#d-stoutford_alchemist-blornvale_select_2)

    <span id="d-stoutford_alchemist-blornvale_thorns72_90"></span>**`blornvale_thorns72_90`** Blornvale: “And you child, go away now and tell no more fairy tales.” — **effects:** sets stage 75 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-75)

    - “But...” → [blornvale_thorns72_92](#d-stoutford_alchemist-blornvale_thorns72_92)

    <span id="d-stoutford_alchemist-blornvale_thorns74"></span>**`blornvale_thorns74`** Blornvale: “You dare to come here again?”

    - “Yes. I need some potions.” → [blornvale_thorns74_1](#d-stoutford_alchemist-blornvale_thorns74_1)

    <span id="d-stoutford_alchemist-blornvale_thorns72"></span>**`blornvale_thorns72`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 65 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-65))* → [blornvale_thorns72_20](#d-stoutford_alchemist-blornvale_thorns72_20)
    - branch 2 → [blornvale_thorns72_10](#d-stoutford_alchemist-blornvale_thorns72_10)

    <span id="d-stoutford_alchemist-blornvale_thorns70_20"></span>**`blornvale_thorns70_20`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on stoutford_potion, sets stage 71 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-71)

    - branch 1 → [blornvale_thorns70_22](#d-stoutford_alchemist-blornvale_thorns70_22)

    <span id="d-stoutford_alchemist-blornvale_thorns70"></span>**`blornvale_thorns70`** Blornvale: “What ... what is this? I feel strange...”

    - “[Loud voice] Tahalendor! Come in, we can start!” *(if reached stage 65 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-65))* → [blornvale_thorns70_20](#d-stoutford_alchemist-blornvale_thorns70_20)
    - “Well, it looks like the potion is already working. Blornvale - that is your name. Right?” *(if NOT reached stage 65 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-65))* → [blornvale_thorns70_10](#d-stoutford_alchemist-blornvale_thorns70_10)

    <span id="d-stoutford_alchemist-blornvale_thorns50"></span>**`blornvale_thorns50`** Blornvale: “Ah, my best customer! Do you want to buy more potions?”

    - “Your potions are unhealthy. Two of our men drank them, and now they are complaining of bad stomachache.” *(if NOT reached stage 200 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-200))* → [blornvale_thorns50_10](#d-stoutford_alchemist-blornvale_thorns50_10)
    - “Your potions are unhealthy. A friend of mine drank it, and now he is complaining of bad stomachache.” *(if reached stage 200 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-200))* → [blornvale_thorns50_10](#d-stoutford_alchemist-blornvale_thorns50_10)

    <span id="d-stoutford_alchemist-blornvale_select_1"></span>**`blornvale_select_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 → [blornvale_select_2](#d-stoutford_alchemist-blornvale_select_2)

    <span id="d-stoutford_alchemist-blornvale_select_2"></span>**`blornvale_select_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 202 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-202))* → [blornvale_shop2](#d-stoutford_alchemist-blornvale_shop2)
    - branch 2 → [blornvale_shop1](#d-stoutford_alchemist-blornvale_shop1)

    <span id="d-stoutford_alchemist-blornvale_thorns72_92"></span>**`blornvale_thorns72_92`** Blornvale: “No more talk. Go now!”


    <span id="d-stoutford_alchemist-blornvale_thorns74_1"></span>**`blornvale_thorns74_1`** Blornvale: “As you wish.”

    - “Yes.” → *shop opens*

    <span id="d-stoutford_alchemist-blornvale_thorns72_20"></span>**`blornvale_thorns72_20`** Blornvale: “You gave me a potion of truth! How dare you! Did you think I wouldn't recognize it?” — **effects:** spawns monsters on stoutford_potion

    - “That will not help you. You are forced to tell the truth.” → [blornvale_thorns72_30](#d-stoutford_alchemist-blornvale_thorns72_30)

    <span id="d-stoutford_alchemist-blornvale_thorns72_10"></span>**`blornvale_thorns72_10`** Blornvale: “That was - a potion of truth! How dare you! Did you think I wouldn't recognize it?” — **effects:** sets stage 74 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-74)

    - “it was worth a try.” → *conversation ends*

    <span id="d-stoutford_alchemist-blornvale_thorns70_22"></span>**`blornvale_thorns70_22`** [Tahalendor](../monsters/tahalendor.md#v-tahalendor2): “Well, it looks like the potion is already working. Blornvale, how did you kill Aryfora's father, your own brother?”

    - Next → [blornvale_thorns70_24](#d-stoutford_alchemist-blornvale_thorns70_24)

    <span id="d-stoutford_alchemist-blornvale_thorns70_10"></span>**`blornvale_thorns70_10`** Blornvale: “Yes.”

    - “How did you kill Aryfora's father, your own brother?” → [blornvale_thorns70_12](#d-stoutford_alchemist-blornvale_thorns70_12)

    <span id="d-stoutford_alchemist-blornvale_thorns50_10"></span>**`blornvale_thorns50_10`** Blornvale: “That cannot be! My potions are not bad, and never have any side effects!”

    - “Well, who believes that? Prove it!” → [blornvale_thorns50_20](#d-stoutford_alchemist-blornvale_thorns50_20)

    <span id="d-stoutford_alchemist-blornvale_shop2"></span>**`blornvale_shop2`** [Blornvale](../monsters/stoutford_alchemist.md#v-stoutford_alchemist2): “Come, I will show you my special selection.” — **effects:** clears stage 201 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-201)

    - “OK, let's see if it's more interesting than soap.” *(if reached stage 201 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-201); NOT reached stage 202 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-202))* → *shop opens*
    - “Yes, let's have a look.” *(if reached stage 202 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-202))* → *shop opens*
    - “No, thank you.” → *conversation ends*
    - “Do you happen to sell empty bottles?” *(if reached stage 23 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-23); NOT reached stage 25 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-25))* → [stoutford_widow2_10_b](#d-stoutford_alchemist-stoutford_widow2_10_b)

    <span id="d-stoutford_alchemist-blornvale_shop1"></span>**`blornvale_shop1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 200 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-200))* → [blornvale_shop1_8](#d-stoutford_alchemist-blornvale_shop1_8)
    - branch 2 *(if NOT killed 1× [Great dark wolf](../monsters/blornvale_wolf.md))* → [blornvale_shop1_2](#d-stoutford_alchemist-blornvale_shop1_2)
    - branch 3 → [blornvale_shop1_6](#d-stoutford_alchemist-blornvale_shop1_6)

    <span id="d-stoutford_alchemist-blornvale_thorns72_30"></span>**`blornvale_thorns72_30`** Blornvale: “I don't think so. After all, I'm a potion maker and I have an antidote for it.”

    - Next → [blornvale_thorns72_40](#d-stoutford_alchemist-blornvale_thorns72_40)

    <span id="d-stoutford_alchemist-blornvale_thorns70_24"></span>**`blornvale_thorns70_24`** [Blornvale](../monsters/stoutford_alchemist.md): “He was naive enough to take a potion from me. I poisoned him with the potion of Quick Death.”

    - Next → [blornvale_thorns70_26](#d-stoutford_alchemist-blornvale_thorns70_26)

    <span id="d-stoutford_alchemist-blornvale_thorns70_12"></span>**`blornvale_thorns70_12`** Blornvale: “He was naive enough to take a potion from me. I poisoned him with the potion of Quick Death.” — **effects:** sets stage 72 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-72)

    - “I thought so. Didn't you worry that someone would suspect you?” → [blornvale_thorns70_14](#d-stoutford_alchemist-blornvale_thorns70_14)

    <span id="d-stoutford_alchemist-blornvale_thorns50_20"></span>**`blornvale_thorns50_20`** Blornvale: “Is there any left over from the potions?”

    - “Yes, here. I still have one bottle of your potion of the brave.” *(if hand over 1× [Potion of truth](../items/potion_truth.md))* → [blornvale_thorns50_30](#d-stoutford_alchemist-blornvale_thorns50_30)
    - “No, I poured all the rest away.” → [blornvale_thorns50_22](#d-stoutford_alchemist-blornvale_thorns50_22)

    <span id="d-stoutford_alchemist-stoutford_widow2_10_b"></span>**`stoutford_widow2_10_b`** Blornvale: “No, unfortunately not. Maybe try my colleague in Fallhaven?”

    - “Sigh - well, thanks.” → *conversation ends*

    <span id="d-stoutford_alchemist-blornvale_shop1_8"></span>**`blornvale_shop1_8`** Blornvale: “Welcome to my shop kid. My potions are not for the faint of heart. Do you want to take a look?”

    - “Sure.” → [blornvale_shop1_10](#d-stoutford_alchemist-blornvale_shop1_10)
    - “Not interested.” → *conversation ends*
    - “Maybe later.” → *conversation ends*
    - “Do you happen to sell empty bottles?” *(if reached stage 23 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-23); NOT reached stage 25 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-25))* → [stoutford_widow2_10_b](#d-stoutford_alchemist-stoutford_widow2_10_b)

    <span id="d-stoutford_alchemist-blornvale_shop1_2"></span>**`blornvale_shop1_2`** Blornvale: “Did you kill this brute behind my house?”

    - “Yes.” → [blornvale_shop1_4](#d-stoutford_alchemist-blornvale_shop1_4)
    - “No, not yet.” → *conversation ends*

    <span id="d-stoutford_alchemist-blornvale_shop1_6"></span>**`blornvale_shop1_6`** Blornvale: “You have indeed killed this brute behind my house!” — **effects:** sets stage 202 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-202)

    - “Yes. Are you content now?” → [blornvale_select_1](#d-stoutford_alchemist-blornvale_select_1)

    <span id="d-stoutford_alchemist-blornvale_thorns72_40"></span>**`blornvale_thorns72_40`** Blornvale: “Ah, I see, Tahalendor is here too, fine. Tahalendor, here is a stupid little kid with too much imagination. Please take it with you.”

    - Next → [blornvale_thorns72_50](#d-stoutford_alchemist-blornvale_thorns72_50)

    <span id="d-stoutford_alchemist-blornvale_thorns70_26"></span>**`blornvale_thorns70_26`** [Tahalendor](../monsters/tahalendor.md#v-tahalendor2): “I thought so. Didn't you worry that someone would suspect you?”

    - Next → [blornvale_thorns70_28](#d-stoutford_alchemist-blornvale_thorns70_28)

    <span id="d-stoutford_alchemist-blornvale_thorns70_14"></span>**`blornvale_thorns70_14`** Blornvale: “Only an alchemist could have found out, so I had only Aryfora herself to fear. But no one believed her accusations.”

    - “That's enough evidence, thank you. I am going to bring Tahalendor here.” → *conversation ends*

    <span id="d-stoutford_alchemist-blornvale_thorns50_30"></span>**`blornvale_thorns50_30`** Blornvale: “Do you see me drinking? Yes? Anything wrong? No - this potion is just perfect!” — **effects:** sets stage 70 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-70)

    - “Yes. I'm just curious if you will still think so in a minute.” → [blornvale_thorns70](#d-stoutford_alchemist-blornvale_thorns70)

    <span id="d-stoutford_alchemist-blornvale_thorns50_22"></span>**`blornvale_thorns50_22`** Blornvale: “Then you can never prove it. That's good. Out now, leave my shop, you scum!” — **effects:** sets stage 74 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-74)


    <span id="d-stoutford_alchemist-blornvale_shop1_10"></span>**`blornvale_shop1_10`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 201 of [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md#stage-201)

    - branch 1 → *shop opens*

    <span id="d-stoutford_alchemist-blornvale_shop1_4"></span>**`blornvale_shop1_4`** Blornvale: “You lie. You shouldn't try that on a potion maker.”

    - “Oh.” → *conversation ends*

    <span id="d-stoutford_alchemist-blornvale_thorns72_50"></span>**`blornvale_thorns72_50`** [Tahalendor](../monsters/tahalendor.md#v-tahalendor2): “Sorry Blornvale, first I have to ask you if you killed Aryfora's father, your own brother?”

    - Next → [blornvale_thorns72_60](#d-stoutford_alchemist-blornvale_thorns72_60)

    <span id="d-stoutford_alchemist-blornvale_thorns70_28"></span>**`blornvale_thorns70_28`** [Blornvale](../monsters/stoutford_alchemist.md): “Only an alchemist could have found out, so I had only Aryfora herself to fear. But no one believed her accusations, not even you, Tahalendor.”

    - Next → [blornvale_thorns70_30](#d-stoutford_alchemist-blornvale_thorns70_30)

    <span id="d-stoutford_alchemist-blornvale_thorns72_60"></span>**`blornvale_thorns72_60`** [Blornvale](../monsters/stoutford_alchemist.md): “Of course not. Nobody is sadder about the loss than me.”

    - “He lies. Can't you see?” → [blornvale_thorns72_70](#d-stoutford_alchemist-blornvale_thorns72_70)

    <span id="d-stoutford_alchemist-blornvale_thorns70_30"></span>**`blornvale_thorns70_30`** [Tahalendor](../monsters/tahalendor.md#v-tahalendor2): “I have heard enough. Thank you, kid. I will ensure that Blornvale never makes trouble again.” — **effects:** sets stage 80 of [The thorns of vengeance](../quests/thorns_vengeance.md#stage-80), removes monsters from stoutford_potion, removes monsters from stoutford_potion

    - Next → *conversation ends*

    <span id="d-stoutford_alchemist-blornvale_thorns72_70"></span>**`blornvale_thorns72_70`** Blornvale: “Here, Tahalendor, I'll give you a bottle of your favorite potion. And please take this child with you when you go.”

    - Next → [blornvale_thorns72_80](#d-stoutford_alchemist-blornvale_thorns72_80)

    <span id="d-stoutford_alchemist-blornvale_thorns72_80"></span>**`blornvale_thorns72_80`** [Tahalendor](../monsters/tahalendor.md#v-tahalendor2): “I will, sorry for disturbing you.”

    - Next → [blornvale_thorns72_90](#d-stoutford_alchemist-blornvale_thorns72_90)



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 38 lines added |
| [v0.8.9](../versions/0.8.9.md) | Dialogue: 1 line added, 2 lines changed |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Stoutford, Stoutford potion (2) { #v-stoutford_alchemist2 }

**Where:** Stoutford: [Stoutford potion](../maps/stoutford_potion.md#pin-npc-stoutford_alchemist2) · **Role:** Shopkeeper

### Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Potion of deftness](../items/potion_deftness_bad.md) | 100% | 10 |
| [Potion of the brave](../items/potion_brave.md) | 100% | 10 |
| [Restore dazed](../items/pot_dazed_restore.md) | 100% | 4 to 5 |
| [Restore fear](../items/pot_fear_restore.md) | 100% | 3 to 6 |
| [Restore stunned](../items/pot_stunned_restore.md) | 100% | 5 |
| [Restore weapon feebleness](../items/pot_feebleness_restore.md) | 100% | 4 to 6 |
| [Potion of quick death](../items/pot_quickdeath.md) | 100% | 2 |
| [Regular potion of health](../items/health.md) | 100% | 10 |

### Quests

- [The thorns of vengeance](../quests/thorns_vengeance.md): stages 70, 71, 72, 74, 75, 80
- [Stoutford story flags (hidden flag)](../quests/stn_nondisplay.md): stages 201, 202

### Dialogue simulator

Set your quest stages and items, then talk to Blornvale. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/blornvale_select_0.json" data-npc="Blornvale" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [blornvale_select_0](#d-stoutford_alchemist-blornvale_select_0).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 38 lines added |
| [v0.8.9](../versions/0.8.9.md) | Dialogue: 1 line added, 2 lines changed |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Blornvale. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: loot or shop stock.

| Entry | Type | Section |
|---|---|---|
| `stoutford_alchemist` | NPC | [Stoutford, Stoutford potion](#v-stoutford_alchemist) |
| `stoutford_alchemist2` | NPC | [Stoutford, Stoutford potion](#v-stoutford_alchemist2) |

??? info "Technical information: stoutford_alchemist"

    | | |
    |---|---|
    | Entry ID | `stoutford_alchemist` |
    | Type (wiki) | NPC |
    | Spawn group | `stoutford_alchemist` |
    | Loot table | `stoutford_alchemist` |
    | Conversation | `blornvale_select_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:70` |
    | Defined in | `res/raw/monsterlist_stoutford.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_alchemist",
     "name": "Blornvale",
     "iconID": "monsters_rltiles1:70",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "stoutford_alchemist",
     "phraseID": "blornvale_select_0",
     "droplistID": "stoutford_alchemist"
    }
    ```

??? info "Technical information: stoutford_alchemist2"

    | | |
    |---|---|
    | Entry ID | `stoutford_alchemist2` |
    | Type (wiki) | NPC |
    | Spawn group | `stoutford_alchemist2` |
    | Loot table | `stoutford_alchemist2` |
    | Conversation | `blornvale_select_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:70` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_alchemist2",
     "name": "Blornvale",
     "iconID": "monsters_rltiles1:70",
     "monsterClass": "humanoid",
     "spawnGroup": "stoutford_alchemist2",
     "phraseID": "blornvale_select_0",
     "droplistID": "stoutford_alchemist2"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_alchemist.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_alchemist.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_alchemist.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stoutford_alchemist.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
