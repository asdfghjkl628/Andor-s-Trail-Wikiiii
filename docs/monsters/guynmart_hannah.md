---
description: "Hannah is a non-player character (NPC) in Andor's Trail, found in Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_ld1_225.png){ .sprite } Hannah

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_225.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Guynmart Castle |
| **Entries in game data** | 3 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! info "3 entries in the game data"
    The game data defines 3 separate characters named Hannah. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`guynmart_hannah`](#v-guynmart_hannah) | NPC | Guynmart Castle: [Guynmart](../maps/guynmart.md#pin-npc-guynmart_hannah) | – |
| [`guynmart_hannah2`](#v-guynmart_hannah2) | NPC | Guynmart Castle: [Guynmart main 1](../maps/guynmart_main_1.md#pin-npc-guynmart_hannah2), Guynmart Castle: [Guynmart main 2](../maps/guynmart_main_2.md#pin-npc-guynmart_hannah2) | – |
| [`guynmart_hannah3`](#v-guynmart_hannah3) | NPC | Guynmart Castle: [Guynmart main 1](../maps/guynmart_main_1.md#pin-npc-guynmart_hannah3) | – |

## Guynmart Castle, Guynmart (guynmart_hannah) { #v-guynmart_hannah }

**Entry ID:** `guynmart_hannah` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart](../maps/guynmart.md#pin-npc-guynmart_hannah)

### Quests

- [Roses](../quests/guynmart.md): stages 70, 90, 100
- [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md): stage 7
- [Guynmart Castle shutters (hidden flag)](../quests/guynmart_qRpl_shutters.md): stage 1
- [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md): stage 34

### Dialogue simulator

Set your quest stages and items, then talk to Hannah. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_hannah_10.json" data-npc="Hannah" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (11 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_hannah-guynmart_hannah_10"></span>**`guynmart_hannah_10`** *(silent check: the first matching branch below is taken)* — **effects:** removes monsters from guynmart_main_1, removes monsters from guynmart_main_2, sets stage 34 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-34)

    - branch 1 *(if carry 1× [Rose](../items/guynmart_rose.md))* → [guynmart_hannah_110](#d-guynmart_hannah-guynmart_hannah_110)
    - branch 2 *(if reached stage 70 of [Roses](../quests/guynmart.md#stage-70))* → [guynmart_hannah_12](#d-guynmart_hannah-guynmart_hannah_12)
    - branch 3 → [guynmart_hannah_20](#d-guynmart_hannah-guynmart_hannah_20)

    <span id="d-guynmart_hannah-guynmart_hannah_110"></span>**`guynmart_hannah_110`** Hannah: “Oh, what a lovely rose you found for me!”

    - Next → [guynmart_hannah_112](#d-guynmart_hannah-guynmart_hannah_112)

    <span id="d-guynmart_hannah-guynmart_hannah_12"></span>**`guynmart_hannah_12`** Hannah: “Go away, kid. I want to be alone. I cannot think clearly without the smell of another fresh, fragrant rose.”

    - “I will bring your rose now.” → *conversation ends*
    - “You and your stupid rose.” *(if reached stage 70 of [Roses](../quests/guynmart.md#stage-70))* → *conversation ends*

    <span id="d-guynmart_hannah-guynmart_hannah_20"></span>**`guynmart_hannah_20`** Hannah: “I cannot think clearly ... I need a rose! A fresh, fragrant rose! Please bring me a rose from my garden...” — **effects:** sets stage 70 of [Roses](../quests/guynmart.md#stage-70), spawns monsters on guynmart, clears stage 1 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-1), sets stage 7 of [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md#stage-7)

    - “I have some delicious lunch for you.” *(if carry 1× [Hannah's lunch](../items/guynmart_lunch.md))* → [guynmart_hannah_30](#d-guynmart_hannah-guynmart_hannah_30)
    - “I will go and ask Nuik.” → *conversation ends*

    <span id="d-guynmart_hannah-guynmart_hannah_112"></span>**`guynmart_hannah_112`** Hannah: “Ah - beautiful. Just look!”

    - Next *(if hand over 1× [Rose](../items/guynmart_rose.md))* → [guynmart_hannah_114](#d-guynmart_hannah-guynmart_hannah_114)

    <span id="d-guynmart_hannah-guynmart_hannah_30"></span>**`guynmart_hannah_30`** Hannah: “How can you think of eating and drinking! My love has gone - I will never eat again! Take it for yourself or throw it away. And leave me alone now. A rose ... I need my rose...”

    - “I will bring your rose now.” → *conversation ends*

    <span id="d-guynmart_hannah-guynmart_hannah_114"></span>**`guynmart_hannah_114`** Hannah: “[Hannah takes the rose] Now. I feel better again. Thank you.” — **effects:** sets stage 90 of [Roses](../quests/guynmart.md#stage-90)

    - Next → [guynmart_hannah_120](#d-guynmart_hannah-guynmart_hannah_120)

    <span id="d-guynmart_hannah-guynmart_hannah_120"></span>**`guynmart_hannah_120`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Roses](../quests/guynmart.md#stage-100))* → [guynmart_hannah_122](#d-guynmart_hannah-guynmart_hannah_122)
    - branch 2 → [guynmart_hannah_140](#d-guynmart_hannah-guynmart_hannah_140)

    <span id="d-guynmart_hannah-guynmart_hannah_122"></span>**`guynmart_hannah_122`** Hannah: “Have you found Lovis yet?”

    - “No, sorry. Not yet.” → *conversation ends*

    <span id="d-guynmart_hannah-guynmart_hannah_140"></span>**`guynmart_hannah_140`** Hannah: “I would like to give you Lovis' flute. He used to play on it every day for me. When you find Lovis, show the flute as a token that I sent you.”

    - “I will not disappoint you.” → [guynmart_hannah_150](#d-guynmart_hannah-guynmart_hannah_150)
    - “No, I do not feel like running back and forth.” → *conversation ends*

    <span id="d-guynmart_hannah-guynmart_hannah_150"></span>**`guynmart_hannah_150`** Hannah: “So take this flute and take good care of it.” — **effects:** sets stage 100 of [Roses](../quests/guynmart.md#stage-100), gives 1× [Lovis' Flute](../items/guynmart_flute.md), sets stage 1 of [Guynmart Castle shutters (hidden flag)](../quests/guynmart_qRpl_shutters.md#stage-1), removes monsters from guynmart_main_3, spawns monsters on guynmart_tower_3

    - “I will.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 11 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_hannah)"

    | | |
    |---|---|
    | Entry ID | `guynmart_hannah` |
    | Spawn group | `guynmart_hannah` |
    | Loot table | – |
    | Conversation | `guynmart_hannah_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:225` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_hannah",
     "name": "Hannah",
     "iconID": "monsters_ld1:225",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_hannah_10"
    }
    ```


## Guynmart Castle, Guynmart main 1 and 1 more (guynmart_hannah2) { #v-guynmart_hannah2 }

**Entry ID:** `guynmart_hannah2` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart main 1](../maps/guynmart_main_1.md#pin-npc-guynmart_hannah2), Guynmart Castle: [Guynmart main 2](../maps/guynmart_main_2.md#pin-npc-guynmart_hannah2)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Guynmart main 1](../maps/guynmart_main_1.md) | Guynmart Castle | 1 | Appears later, during a quest |
| [Guynmart main 2](../maps/guynmart_main_2.md) | Guynmart Castle | 1 | Appears later, during a quest |

### Quests

- [Roses](../quests/guynmart.md): stages 190, 200, 210, 211
- [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md): stages 33, 36

### Dialogue simulator

Set your quest stages and items, then talk to Hannah. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_hannah2_10.json" data-npc="Hannah" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (46 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_hannah2-guynmart_hannah2_10"></span>**`guynmart_hannah2_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 200 of [Roses](../quests/guynmart.md#stage-200))* → [guynmart_hannah2_14](#d-guynmart_hannah2-guynmart_hannah2_14)
    - branch 2 *(if reached stage 210 of [Roses](../quests/guynmart.md#stage-210))* → [guynmart_hannah2_12](#d-guynmart_hannah2-guynmart_hannah2_12)
    - branch 3 *(if reached stage 190 of [Roses](../quests/guynmart.md#stage-190))* → [guynmart_hannah2_20](#d-guynmart_hannah2-guynmart_hannah2_20)
    - branch 4 → [guynmart_hannah2_30](#d-guynmart_hannah2-guynmart_hannah2_30)

    <span id="d-guynmart_hannah2-guynmart_hannah2_14"></span>**`guynmart_hannah2_14`** Hannah: “$playername - what a joy to see you again.”


    <span id="d-guynmart_hannah2-guynmart_hannah2_12"></span>**`guynmart_hannah2_12`** Hannah: “Hello $playername.”


    <span id="d-guynmart_hannah2-guynmart_hannah2_20"></span>**`guynmart_hannah2_20`** Hannah: “Now let us hear Lovis.”

    - Next → [guynmart_lovis2_30](#d-guynmart_hannah2-guynmart_lovis2_30)

    <span id="d-guynmart_hannah2-guynmart_hannah2_30"></span>**`guynmart_hannah2_30`** [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2): “Many things have happened. Norgothla came back and Unkorh flew, his men dead or scattered.”

    - Next → [guynmart_hannah2_32](#d-guynmart_hannah2-guynmart_hannah2_32)

    <span id="d-guynmart_hannah2-guynmart_lovis2_30"></span>**`guynmart_lovis2_30`** [Lovis](../monsters/guynmart_lovis.md#v-guynmart_lovis2): “We are deeply in your debt, indeed.”

    - Next → [guynmart_lovis2_40](#d-guynmart_hannah2-guynmart_lovis2_40)

    <span id="d-guynmart_hannah2-guynmart_hannah2_32"></span>**`guynmart_hannah2_32`** [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2): “We found Guynmart down in a cell, but it was too late - My beloved father died in my arms.”

    - Next → [guynmart_hannah2_34](#d-guynmart_hannah2-guynmart_hannah2_34)

    <span id="d-guynmart_hannah2-guynmart_lovis2_40"></span>**`guynmart_lovis2_40`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 1 of [Guynmart quest wizard (hidden flag)](../quests/guynmart_quest_wizard.md#stage-1))* → [guynmart_lovis2_50](#d-guynmart_hannah2-guynmart_lovis2_50)
    - branch 2 → [guynmart_lovis2_70](#d-guynmart_hannah2-guynmart_lovis2_70)

    <span id="d-guynmart_hannah2-guynmart_hannah2_34"></span>**`guynmart_hannah2_34`** [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2): “And Lovis and I are finally married. In spite of the cruel events, or just to forget them a little, we celebrated a joyous feast.”

    - Next → [guynmart_hannah2_40](#d-guynmart_hannah2-guynmart_hannah2_40)

    <span id="d-guynmart_hannah2-guynmart_lovis2_50"></span>**`guynmart_lovis2_50`** Hannah: “We also have good news for you.”

    - Next → [guynmart_lovis2_52](#d-guynmart_hannah2-guynmart_lovis2_52)

    <span id="d-guynmart_hannah2-guynmart_lovis2_70"></span>**`guynmart_lovis2_70`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep); NOT reached stage 33 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-33))* → [guynmart_lovis2_200](#d-guynmart_hannah2-guynmart_lovis2_200)
    - branch 2 → [guynmart_lovis2_100](#d-guynmart_hannah2-guynmart_lovis2_100)

    <span id="d-guynmart_hannah2-guynmart_hannah2_40"></span>**`guynmart_hannah2_40`** [Hannah](../monsters/guynmart_hannah.md#v-guynmart_hannah2): “If it wasn't for you, Guynmart castle would look different today: dark and gloomy and no place you would want to live.”

    - Next → [guynmart_hannah2_50](#d-guynmart_hannah2-guynmart_hannah2_50)

    <span id="d-guynmart_hannah2-guynmart_lovis2_52"></span>**`guynmart_lovis2_52`** Hannah: “Rorthron, the ringmaker, was behaving rather strangely, and so we questioned him. It came to light that he seems to have damaged one of your rings.”

    - Next → [guynmart_lovis2_54](#d-guynmart_hannah2-guynmart_lovis2_54)

    <span id="d-guynmart_hannah2-guynmart_lovis2_200"></span>**`guynmart_lovis2_200`** Hannah: “Regrettably, we still have to sort out an unpleasant thing. Let our shepherd speak.” — **effects:** spawns monsters on guynmart_main_1

    - Next → [guynmart_lovis2_210](#d-guynmart_hannah2-guynmart_lovis2_210)

    <span id="d-guynmart_hannah2-guynmart_lovis2_100"></span>**`guynmart_lovis2_100`** Hannah: “You have earned your reward. Go now into our treasury.” — **effects:** sets stage 200 of [Roses](../quests/guynmart.md#stage-200), spawns monsters on guynmart_main_1, removes monsters from guynmart_main_1


    <span id="d-guynmart_hannah2-guynmart_hannah2_50"></span>**`guynmart_hannah2_50`** Hannah: “Take this rose as a token of my deepest thanks. May its lovely fragrance last forever.” — **effects:** sets stage 190 of [Roses](../quests/guynmart.md#stage-190), gives 1× [Rose](../items/guynmart_rose.md)

    - “Thank you, Lady.” → [guynmart_hannah2_20](#d-guynmart_hannah2-guynmart_hannah2_20)

    <span id="d-guynmart_hannah2-guynmart_lovis2_54"></span>**`guynmart_lovis2_54`** Hannah: “He eventually admitted that he secretly exchanged your ring for a worthless ring.”

    - Next → [guynmart_lovis2_56](#d-guynmart_hannah2-guynmart_lovis2_56)

    <span id="d-guynmart_hannah2-guynmart_lovis2_210"></span>**`guynmart_lovis2_210`** [Shepherd](../monsters/guynmart_shephard.md#v-guynmart_shephard2): “Grumble ... grumble...”

    - Next → [guynmart_lovis2_220](#d-guynmart_hannah2-guynmart_lovis2_220)

    <span id="d-guynmart_hannah2-guynmart_lovis2_56"></span>**`guynmart_lovis2_56`** Hannah: “He promised never to do such things again and handed the real ring over to us. We want to leave it at that.”

    - Next → [guynmart_lovis2_60](#d-guynmart_hannah2-guynmart_lovis2_60)

    <span id="d-guynmart_hannah2-guynmart_lovis2_220"></span>**`guynmart_lovis2_220`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 181 of [Roses](../quests/guynmart.md#stage-181))* → [guynmart_lovis2_220b](#d-guynmart_hannah2-guynmart_lovis2_220b)
    - branch 2 → [guynmart_lovis2_220a](#d-guynmart_hannah2-guynmart_lovis2_220a)

    <span id="d-guynmart_hannah2-guynmart_lovis2_60"></span>**`guynmart_lovis2_60`** Hannah: “So here, take your precious ring back.” — **effects:** gives 1× [Ring of lesser Shadow](../items/ring_shadow0.md), clears stage 1 of [Guynmart quest wizard (hidden flag)](../quests/guynmart_quest_wizard.md#stage-1)

    - “Oh! I can't believe it! Is it really true?” → [guynmart_lovis2_70](#d-guynmart_hannah2-guynmart_lovis2_70)

    <span id="d-guynmart_hannah2-guynmart_lovis2_220b"></span>**`guynmart_lovis2_220b`** *(silent check: the first matching branch below is taken)*

    - branch 1 → [guynmart_lovis2_220c](#d-guynmart_hannah2-guynmart_lovis2_220c)

    <span id="d-guynmart_hannah2-guynmart_lovis2_220a"></span>**`guynmart_lovis2_220a`** *(silent check: the first matching branch below is taken)*

    - branch 1 → [guynmart_lovis2_220c](#d-guynmart_hannah2-guynmart_lovis2_220c)

    <span id="d-guynmart_hannah2-guynmart_lovis2_220c"></span>**`guynmart_lovis2_220c`** Hannah: “It seems sheep were killed by your hand. Our sheep, to be precise.”

    - Next → [guynmart_lovis2_221](#d-guynmart_hannah2-guynmart_lovis2_221)

    <span id="d-guynmart_hannah2-guynmart_lovis2_221"></span>**`guynmart_lovis2_221`** Hannah: “You will be fined 100 gold for each sheep you killed. Do you accept this judgment?”

    - “Yes, what I did was stupid.” → [guynmart_lovis2_300](#d-guynmart_hannah2-guynmart_lovis2_300)
    - “Lies! All lies!” → [guynmart_lovis2_222](#d-guynmart_hannah2-guynmart_lovis2_222)
    - “I can explain - it was an accident...” → [guynmart_lovis2_222](#d-guynmart_hannah2-guynmart_lovis2_222)

    <span id="d-guynmart_hannah2-guynmart_lovis2_300"></span>**`guynmart_lovis2_300`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 25× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_lovis2_325](#d-guynmart_hannah2-guynmart_lovis2_325)
    - branch 2 *(if killed 20× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_lovis2_320](#d-guynmart_hannah2-guynmart_lovis2_320)
    - branch 3 *(if killed 15× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_lovis2_315](#d-guynmart_hannah2-guynmart_lovis2_315)
    - branch 4 *(if killed 10× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_lovis2_310](#d-guynmart_hannah2-guynmart_lovis2_310)
    - branch 5 *(if killed 9× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_lovis2_309](#d-guynmart_hannah2-guynmart_lovis2_309)
    - branch 6 *(if killed 8× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_lovis2_308](#d-guynmart_hannah2-guynmart_lovis2_308)
    - branch 7 *(if killed 7× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_lovis2_307](#d-guynmart_hannah2-guynmart_lovis2_307)
    - branch 8 *(if killed 6× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_lovis2_306](#d-guynmart_hannah2-guynmart_lovis2_306)
    - branch 9 *(if killed 5× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_lovis2_305](#d-guynmart_hannah2-guynmart_lovis2_305)
    - branch 10 *(if killed 4× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_lovis2_304](#d-guynmart_hannah2-guynmart_lovis2_304)
    - branch 11 *(if killed 3× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_lovis2_303](#d-guynmart_hannah2-guynmart_lovis2_303)
    - branch 12 *(if killed 2× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_lovis2_302](#d-guynmart_hannah2-guynmart_lovis2_302)
    - branch 13 *(if killed 1× [Sheep](../monsters/sheep1.md#v-guynmart_sheep))* → [guynmart_lovis2_301](#d-guynmart_hannah2-guynmart_lovis2_301)

    <span id="d-guynmart_hannah2-guynmart_lovis2_222"></span>**`guynmart_lovis2_222`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 181 of [Roses](../quests/guynmart.md#stage-181))* → [guynmart_lovis2_231](#d-guynmart_hannah2-guynmart_lovis2_231)
    - branch 2 → [guynmart_lovis2_230](#d-guynmart_hannah2-guynmart_lovis2_230)

    <span id="d-guynmart_hannah2-guynmart_lovis2_325"></span>**`guynmart_lovis2_325`** Hannah: “2,500 gold for 25 or perhaps even more killed sheep.”

    - “Here is the gold.” *(if pay 2,500 gold)* → [guynmart_lovis2_360](#d-guynmart_hannah2-guynmart_lovis2_360)
    - “I don't have enough gold.” → [guynmart_lovis2_350](#d-guynmart_hannah2-guynmart_lovis2_350)

    <span id="d-guynmart_hannah2-guynmart_lovis2_320"></span>**`guynmart_lovis2_320`** Hannah: “2,000 gold for 20 or perhaps even more killed sheep.”

    - “Here is the gold.” *(if pay 2,000 gold)* → [guynmart_lovis2_360](#d-guynmart_hannah2-guynmart_lovis2_360)
    - “I don't have enough gold.” → [guynmart_lovis2_350](#d-guynmart_hannah2-guynmart_lovis2_350)

    <span id="d-guynmart_hannah2-guynmart_lovis2_315"></span>**`guynmart_lovis2_315`** Hannah: “1,500 gold for 15 or perhaps even more killed sheep.”

    - “Here is the gold.” *(if pay 1,500 gold)* → [guynmart_lovis2_360](#d-guynmart_hannah2-guynmart_lovis2_360)
    - “I don't have enough gold.” → [guynmart_lovis2_350](#d-guynmart_hannah2-guynmart_lovis2_350)

    <span id="d-guynmart_hannah2-guynmart_lovis2_310"></span>**`guynmart_lovis2_310`** Hannah: “1,000 gold for 10 or perhaps even more killed sheep.”

    - “Here is the gold.” *(if pay 1,000 gold)* → [guynmart_lovis2_360](#d-guynmart_hannah2-guynmart_lovis2_360)
    - “I don't have enough gold.” → [guynmart_lovis2_350](#d-guynmart_hannah2-guynmart_lovis2_350)

    <span id="d-guynmart_hannah2-guynmart_lovis2_309"></span>**`guynmart_lovis2_309`** Hannah: “900 gold for 9 killed sheep.”

    - “Here is the gold.” *(if pay 900 gold)* → [guynmart_lovis2_360](#d-guynmart_hannah2-guynmart_lovis2_360)
    - “I don't have enough gold.” → [guynmart_lovis2_350](#d-guynmart_hannah2-guynmart_lovis2_350)

    <span id="d-guynmart_hannah2-guynmart_lovis2_308"></span>**`guynmart_lovis2_308`** Hannah: “800 gold for 8 killed sheep.”

    - “Here is the gold.” *(if pay 800 gold)* → [guynmart_lovis2_360](#d-guynmart_hannah2-guynmart_lovis2_360)
    - “I don't have enough gold.” → [guynmart_lovis2_350](#d-guynmart_hannah2-guynmart_lovis2_350)

    <span id="d-guynmart_hannah2-guynmart_lovis2_307"></span>**`guynmart_lovis2_307`** Hannah: “700 gold for 7 killed sheep.”

    - “Here is the gold.” *(if pay 700 gold)* → [guynmart_lovis2_360](#d-guynmart_hannah2-guynmart_lovis2_360)
    - “I don't have enough gold.” → [guynmart_lovis2_350](#d-guynmart_hannah2-guynmart_lovis2_350)

    <span id="d-guynmart_hannah2-guynmart_lovis2_306"></span>**`guynmart_lovis2_306`** Hannah: “600 gold for 6 killed sheep.”

    - “Here is the gold.” *(if pay 600 gold)* → [guynmart_lovis2_360](#d-guynmart_hannah2-guynmart_lovis2_360)
    - “I don't have enough gold.” → [guynmart_lovis2_350](#d-guynmart_hannah2-guynmart_lovis2_350)

    <span id="d-guynmart_hannah2-guynmart_lovis2_305"></span>**`guynmart_lovis2_305`** Hannah: “500 gold for 5 killed sheep.”

    - “Here is the gold.” *(if pay 500 gold)* → [guynmart_lovis2_360](#d-guynmart_hannah2-guynmart_lovis2_360)
    - “I don't have enough gold.” → [guynmart_lovis2_350](#d-guynmart_hannah2-guynmart_lovis2_350)

    <span id="d-guynmart_hannah2-guynmart_lovis2_304"></span>**`guynmart_lovis2_304`** Hannah: “400 gold for 4 killed sheep.”

    - “Here is the gold.” *(if pay 400 gold)* → [guynmart_lovis2_360](#d-guynmart_hannah2-guynmart_lovis2_360)
    - “I don't have enough gold.” → [guynmart_lovis2_350](#d-guynmart_hannah2-guynmart_lovis2_350)

    <span id="d-guynmart_hannah2-guynmart_lovis2_303"></span>**`guynmart_lovis2_303`** Hannah: “300 gold for 3 killed sheep.”

    - “Here is the gold.” *(if pay 300 gold)* → [guynmart_lovis2_360](#d-guynmart_hannah2-guynmart_lovis2_360)
    - “I don't have enough gold.” → [guynmart_lovis2_350](#d-guynmart_hannah2-guynmart_lovis2_350)

    <span id="d-guynmart_hannah2-guynmart_lovis2_302"></span>**`guynmart_lovis2_302`** Hannah: “200 gold for 2 killed sheep.”

    - “Here is the gold.” *(if pay 200 gold)* → [guynmart_lovis2_360](#d-guynmart_hannah2-guynmart_lovis2_360)
    - “I don't have enough gold.” → [guynmart_lovis2_350](#d-guynmart_hannah2-guynmart_lovis2_350)

    <span id="d-guynmart_hannah2-guynmart_lovis2_301"></span>**`guynmart_lovis2_301`** Hannah: “100 gold for the killed sheep.”

    - “Here is the gold.” *(if pay 100 gold)* → [guynmart_lovis2_360](#d-guynmart_hannah2-guynmart_lovis2_360)
    - “I don't have enough gold.” → [guynmart_lovis2_350](#d-guynmart_hannah2-guynmart_lovis2_350)

    <span id="d-guynmart_hannah2-guynmart_lovis2_231"></span>**`guynmart_lovis2_231`** Hannah: “As you wish. I am very disappointed with you - go now.”

    - “No, sorry, I didn't mean it.” → [guynmart_lovis2_220](#d-guynmart_hannah2-guynmart_lovis2_220)
    - “I will go. Bye.” → [guynmart_lovis2_241](#d-guynmart_hannah2-guynmart_lovis2_241)

    <span id="d-guynmart_hannah2-guynmart_lovis2_230"></span>**`guynmart_lovis2_230`** Hannah: “As you wish. I already regret that we prepared a surprise for you next to the sheep pastures. I am very disappointed in you. Go now.”

    - “No, sorry, I didn't mean it.” → [guynmart_lovis2_220](#d-guynmart_hannah2-guynmart_lovis2_220)
    - “I will go. Bye.” → [guynmart_lovis2_240](#d-guynmart_hannah2-guynmart_lovis2_240)

    <span id="d-guynmart_hannah2-guynmart_lovis2_360"></span>**`guynmart_lovis2_360`** Hannah: “[Gold taken] All the sheep you killed are paid for, so now we will forget the whole thing.” — **effects:** sets stage 33 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-33), removes monsters from guynmart_main_1

    - “I am relieved.” → [guynmart_lovis2_100](#d-guynmart_hannah2-guynmart_lovis2_100)

    <span id="d-guynmart_hannah2-guynmart_lovis2_350"></span>**`guynmart_lovis2_350`** Hannah: “You will find a way to get the missing gold. Then come back and pay the rest.”

    - “OK.” → *conversation ends*

    <span id="d-guynmart_hannah2-guynmart_lovis2_241"></span>**`guynmart_lovis2_241`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 211 of [Roses](../quests/guynmart.md#stage-211), sets stage 36 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-36), removes monsters from guynmart_main_1


    <span id="d-guynmart_hannah2-guynmart_lovis2_240"></span>**`guynmart_lovis2_240`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 210 of [Roses](../quests/guynmart.md#stage-210), sets stage 36 of [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md#stage-36), removes monsters from guynmart_main_1, spawns monsters on guynmart_wood_9




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 46 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 4 lines changed<br>· text: “1000 gold for 10 or perhaps even more killed sheep.” → “{1000} gold for 10 or perhaps even more killed sheep.”<br>· text: “2500 gold for 25 or perhaps even more killed sheep.” → “{2500} gold for 25 or perhaps even more killed sheep.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_hannah2)"

    | | |
    |---|---|
    | Entry ID | `guynmart_hannah2` |
    | Spawn group | `guynmart_hannah2` |
    | Loot table | – |
    | Conversation | `guynmart_hannah2_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:225` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_hannah2",
     "name": "Hannah",
     "iconID": "monsters_ld1:225",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_hannah2_10"
    }
    ```


## Guynmart Castle, Guynmart main 1 (guynmart_hannah3) { #v-guynmart_hannah3 }

**Entry ID:** `guynmart_hannah3` · **Type:** NPC

**Location:** Guynmart Castle: [Guynmart main 1](../maps/guynmart_main_1.md#pin-npc-guynmart_hannah3)

### Quests

- [Roses](../quests/guynmart.md): stages 70, 90, 100
- [Guest tour (hidden flag)](../quests/guynmart_quest_olav.md): stage 7
- [Guynmart Castle shutters (hidden flag)](../quests/guynmart_qRpl_shutters.md): stage 1
- [Guynmart story flags (hidden flag)](../quests/guynmart_nondisplay.md): stage 34

### Dialogue simulator

Set your quest stages and items, then talk to Hannah. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_hannah_10.json" data-npc="Hannah" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [guynmart_hannah_10](#d-guynmart_hannah-guynmart_hannah_10).


### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 11 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (guynmart_hannah3)"

    | | |
    |---|---|
    | Entry ID | `guynmart_hannah3` |
    | Spawn group | `guynmart_hannah3` |
    | Loot table | – |
    | Conversation | `guynmart_hannah_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:225` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_hannah3",
     "name": "Hannah",
     "iconID": "monsters_ld1:225",
     "unique": 1,
     "monsterClass": "humanoid",
     "phraseID": "guynmart_hannah_10"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_hannah.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_hannah.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_hannah.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_hannah.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
