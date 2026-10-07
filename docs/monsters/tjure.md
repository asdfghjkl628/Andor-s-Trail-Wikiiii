# ![](../assets/icons/monsters/monsters_ld1_19.png){ .sprite } Tjure

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_19.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `tjure` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Blackwater Mountain |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain54](../maps/blackwater_mountain54.md) | Blackwater Mountain | 1 | – |


## Quests

- [The silver scale](../quests/mermaid_scale.md): stages 10, 20, 30, 90, 100
- [Delivery - nondisplay (hidden flag)](../quests/brv_wh_delivery_nondisplay.md): stages 50

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Tjure. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/tjure.json" data-npc="Tjure" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (25 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tjure"></span>**`tjure`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 200 of [The silver scale](../quests/mermaid_scale.md#stage-200))* → [tjure_200](#d-tjure_200)
    - branch 2 *(if reached stage 100 of [The silver scale](../quests/mermaid_scale.md#stage-100))* → [tjure_100](#d-tjure_100)
    - branch 3 *(if reached stage 90 of [The silver scale](../quests/mermaid_scale.md#stage-90))* → [tjure_90](#d-tjure_90)
    - branch 4 *(if reached stage 90 of [The silver scale](../quests/mermaid_scale.md#stage-90); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 60 of [Delivery](../quests/brv_wh_delivery.md#stage-60))* → [tjure_wh_delivery_90](#d-tjure_wh_delivery_90)
    - branch 5 *(if reached stage 30 of [The silver scale](../quests/mermaid_scale.md#stage-30))* → [tjure_30](#d-tjure_30)
    - branch 6 *(if reached stage 20 of [The silver scale](../quests/mermaid_scale.md#stage-20))* → [tjure_20](#d-tjure_20)
    - branch 7 *(if reached stage 10 of [The silver scale](../quests/mermaid_scale.md#stage-10))* → [tjure_10](#d-tjure_10)
    - branch 8 → [tjure_0](#d-tjure_0)

    <span id="d-tjure_200"></span>**`tjure_200`** Tjure: “Oh, you look better than the last time we met. Thank you for your help.”

    - “It was an interesting experience.” → *conversation ends*
    - “Indeed. By the way, did you order a 'Mysterious green something'?” *(if hand over 1× [Mysterious green something](../items/brv_wh_item_05.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 60 of [Delivery](../quests/brv_wh_delivery.md#stage-60))* → [brv_wh_delivery_tjure](#d-brv_wh_delivery_tjure)

    <span id="d-tjure_100"></span>**`tjure_100`** [Tjure](../monsters/tjure.md): “Thank you for your help.”

    - “It was an interesting experience.” → *conversation ends*
    - “No problem. By the way, did you order a 'Mysterious green something'?” *(if hand over 1× [Mysterious green something](../items/brv_wh_item_05.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 60 of [Delivery](../quests/brv_wh_delivery.md#stage-60))* → [brv_wh_delivery_tjure](#d-brv_wh_delivery_tjure)

    <span id="d-tjure_90"></span>**`tjure_90`** Tjure: “*Sigh* You were my last hope. Leave me now.” — **effects:** sets stage 90 of [The silver scale](../quests/mermaid_scale.md#stage-90)

    - “Hope you learned from it.” → *conversation ends*
    - “OK. One question before I go: did you order a 'Mysterious green something'?” *(if hand over 1× [Mysterious green something](../items/brv_wh_item_05.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 60 of [Delivery](../quests/brv_wh_delivery.md#stage-60))* → [brv_wh_delivery_tjure](#d-brv_wh_delivery_tjure)

    <span id="d-tjure_wh_delivery_90"></span>**`tjure_wh_delivery_90`** Tjure: “*Sigh* You were my last hope. Leave me now.”

    - “Not until I have delivered this to you. Are you the one who ordered a 'Mysterious green something'?” *(if hand over 1× [Mysterious green something](../items/brv_wh_item_05.md))* → [brv_wh_delivery_tjure](#d-brv_wh_delivery_tjure)

    <span id="d-tjure_30"></span>**`tjure_30`** Tjure: “At first I was happy with my shimmering scale. But I soon realized that everything in my life was going wrong.”

    - Next → [tjure_30_10](#d-tjure_30_10)

    <span id="d-tjure_20"></span>**`tjure_20`** Tjure: “Crying and sobbing, the mermaid called after me. Finally, she screamed at me that I would never find peace, and that I would never want to approach water again!” — **effects:** sets stage 20 of [The silver scale](../quests/mermaid_scale.md#stage-20)

    - Next → [tjure_30](#d-tjure_30)

    <span id="d-tjure_10"></span>**`tjure_10`** Tjure: “I pulled out one of her shimmering, dazzling scales, and ran away.” — **effects:** sets stage 10 of [The silver scale](../quests/mermaid_scale.md#stage-10)

    - “No! You really did that?” → [tjure_10_10](#d-tjure_10_10)

    <span id="d-tjure_0"></span>**`tjure_0`** Tjure: “Oh, what a rare surprise!”

    - “Who are you?” → [tjure_0_10](#d-tjure_0_10)
    - “What are you doing in such a lonely place?” → [tjure_0_10](#d-tjure_0_10)
    - “Eh, sorry to disturb you.” → *conversation ends*
    - “I'm surprised to see you here as well. Did you order 'Mysterious green something'?” *(if hand over 1× [Mysterious green something](../items/brv_wh_item_05.md); reached stage 10 of [Delivery](../quests/brv_wh_delivery.md#stage-10); reached stage 60 of [Delivery](../quests/brv_wh_delivery.md#stage-60))* → [brv_wh_delivery_tjure](#d-brv_wh_delivery_tjure)

    <span id="d-brv_wh_delivery_tjure"></span>**`brv_wh_delivery_tjure`** Tjure: “What?! My lucky clover...but why now? Anyway, I'll no longer run out of luck. Here's my delivery fee.” — **effects:** clears stage 60 of [Delivery](../quests/brv_wh_delivery.md#stage-60), sets stage 50 of [Delivery - nondisplay (hidden flag)](../quests/brv_wh_delivery_nondisplay.md#stage-50), gives 50× [Gold coins](../items/gold.md)

    - “Thank you.” → *conversation ends*

    <span id="d-tjure_30_10"></span>**`tjure_30_10`** Tjure: “I couldn't think of anything else but the wrath of the people of the river.”

    - Next → [tjure_30_20](#d-tjure_30_20)

    <span id="d-tjure_10_10"></span>**`tjure_10_10`** Tjure: “The mermaid immediately awoke and was very angry. But on land she had no chance to catch me.”

    - Next → [tjure_20](#d-tjure_20)

    <span id="d-tjure_0_10"></span>**`tjure_0_10`** Tjure: “I am Tjure of Brimhaven. I am ... was ... a successful merchant. But my luck has run out.”

    - Next → [tjure_0_12](#d-tjure_0_12)

    <span id="d-tjure_30_20"></span>**`tjure_30_20`** Tjure: “What could I do? I tried to throw it away or give it to other people - all in vain.”

    - Next → [tjure_30_30](#d-tjure_30_30)

    <span id="d-tjure_0_12"></span>**`tjure_0_12`** Tjure: “All I can do now is hide in this lonely place, far away from any water.”

    - “Aha. I won't bother you then.” → *conversation ends*
    - “Why is that?” → [tjure_0_20](#d-tjure_0_20)

    <span id="d-tjure_30_30"></span>**`tjure_30_30`** Tjure: “I traveled all over Dhayavar to find someone to help me. Finally, a wise woman, far in the northeast, listened to my story. She advised me to return the scale to the mermaid. This would break the curse.”

    - Next → [tjure_30_32](#d-tjure_30_32)

    <span id="d-tjure_0_20"></span>**`tjure_0_20`** Tjure: “I once found a mermaid asleep on the beach of a river, north of here. What a beautiful sight! I could not avert my eyes!”

    - Next → [tjure_0_22](#d-tjure_0_22)

    <span id="d-tjure_30_32"></span>**`tjure_30_32`** Tjure: “But I did not dare to do this.”

    - Next → [tjure_30_34](#d-tjure_30_34)

    <span id="d-tjure_0_22"></span>**`tjure_0_22`** Tjure: “Especially, the colorful tail attracted me so much, that I did something that I have deeply regretted since then.”

    - “What did you do?” → [tjure_10](#d-tjure_10)

    <span id="d-tjure_30_34"></span>**`tjure_30_34`** Tjure: “She told me that my only other option was to find some kind-hearted person to buy it from me, but then they take on the curse.” — **effects:** sets stage 30 of [The silver scale](../quests/mermaid_scale.md#stage-30)

    - “Who would be that stupid?” → [tjure_30_40](#d-tjure_30_40)
    - “Let me be the one to rescue you. Sell me the scale.” → [tjure_30_90](#d-tjure_30_90)

    <span id="d-tjure_30_40"></span>**`tjure_30_40`** Tjure: “I know, I know. When they heard my story, everybody ran away.”

    - “That's too bad. I hope that you will find someone to buy it. Bye.” → [tjure_30_50](#d-tjure_30_50)
    - “Not me. I will buy the scale.” → [tjure_30_90](#d-tjure_30_90)

    <span id="d-tjure_30_90"></span>**`tjure_30_90`** Tjure: “Here, take it! I have to request gold for it, otherwise it won't work. But one piece of gold should be enough.”

    - “No problem, here, take the gold.” *(if pay 1 gold)* → [tjure_30_92](#d-tjure_30_92)
    - “Forget it.” → *conversation ends*

    <span id="d-tjure_30_50"></span>**`tjure_30_50`** Tjure: “So you really won't help me? You will leave me to my misery?”

    - “Sorry, I can't do it. Bye.” → [tjure_90](#d-tjure_90)
    - “I have to think about it.” → *conversation ends*
    - “OK. maybe I am stupid, but sell me the scale.” → [tjure_30_90](#d-tjure_30_90)

    <span id="d-tjure_30_92"></span>**`tjure_30_92`** [Dummy NPC](../monsters/none.md): “(As soon as you take the scale in your hands, a great sluggishness and a feeling of despair come over you.)” — **effects:** sets stage 100 of [The silver scale](../quests/mermaid_scale.md#stage-100), applies condition mermaid_scale

    - “I feel ... strange!” → [tjure_30_94](#d-tjure_30_94)

    <span id="d-tjure_30_94"></span>**`tjure_30_94`** Tjure: “(For a second you feel very dizzy. At least you manage not to faint. As from afar you hear a voice.)”

    - Next → [tjure_100](#d-tjure_100)



## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 23 lines added |
| [v0.7.11](../versions/0.7.11.md) | Dialogue: 1 line changed<br>· text: “I once found a mermaid asleep on the beach of a river. What a beautif…” → “I once found a mermaid asleep on the beach of a river, north of here.…” |
| [v0.7.15](../versions/0.7.15.md) | Dialogue: 1 line changed |
| [v0.7.17](../versions/0.7.17.md) | Dialogue: 2 lines added, 5 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tjure.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tjure.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tjure.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tjure.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `tjure` |
    | Spawn group | `tjure` |
    | Loot table | – |
    | Conversation | `tjure` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:19` |
    | Defined in | `res/raw/monsterlist_arulir_mountain.json` |

    Raw data:

    ```json
    {
     "id": "tjure",
     "name": "Tjure",
     "iconID": "monsters_ld1:19",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "tjure"
    }
    ```


<small>Data from v0.8.18</small>
