---
description: "Saki is an NPC you can also fight in Andor's Trail, found in Mt. Galmore."
---

# ![](../assets/icons/monsters/monsters_newb_1_122.png){ .sprite } Saki

**Where to find Saki:** Mt. Galmore: [Undertell exit](../maps/undertell_exit.md#pin-npc-saki), [Undertell 1 1](../maps/undertell_1_1.md#pin-npc-saki)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_newb_1_122.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Mt. Galmore |
| **Class** | Ghost |
| **HP** | 498 |
| **XP when defeated** | 1,386 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

!!! warning "You can fight Saki"
    Answering “You followers of Kazaul - you want everything for yourself! Give…” while talking to [Ysrine](../monsters/ysrine.md) starts a fight with Saki.

    Answering “You followers of Kazaul - you want everything for yourself! Give…” starts a fight with Saki.

## Combat

| | |
|---|---|
| Class | Ghost |
| HP | 498 |
| XP when defeated | 1,386 |
| Damage | 5 to 7 |
| AC | 230 |
| BC | 233 |
| DR | 14 |
| Attacks per turn | 3 (4 AP each, 12 AP) |
| Crit chance | none |

**Immune to critical hits.**

**Its hits:** On target: [Deathtouch](../conditions/deathtouch.md) (magnitude 1, 3 rounds, 50% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Soul pearl](../items/soul_pearl.md) | 100% | 5 |
| [Kazaul bonemeal](../items/pot_bm_kazaul.md) | 100% | 2 to 4 |
| [Gold coins](../items/gold.md) | 100% | 650 to 699 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Undertell 1 1](../maps/undertell_1_1.md) | – | 1 | Appears later, during a quest |
| [Undertell exit](../maps/undertell_exit.md) | Mt. Galmore | 1 | Appears later, during a quest |

## Quests that count defeats

- A conversation with [Ysrine](../monsters/ysrine.md) ([Undertell 1 1](../maps/undertell_1_1.md)) checks that this enemy has been defeated.

## Quests

- [Dominion](../quests/dominion.md): stages 20, 30, 70

## Dialogue simulator

Talk to Saki as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/saki_selector.json" data-npc="Saki" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (25 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-saki_selector"></span>**`saki_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if latest stage of [Dominion](../quests/dominion.md#stage-10) is 10)* → [saki_meet_10](#d-saki_meet_10)
    - branch 2 *(if reached stage 20 of [Dominion](../quests/dominion.md#stage-20); NOT reached stage 30 of [Dominion](../quests/dominion.md#stage-30))* → [saki_pearls_10](#d-saki_pearls_10)
    - branch 3 *(if reached stage 60 of [Dominion](../quests/dominion.md#stage-60))* → [saki_trapped_10](#d-saki_trapped_10)

    <span id="d-saki_meet_10"></span>**`saki_meet_10`** Saki: “Hello, $playername.”

    - “[freaking out] Who are you? Where did you come from?” → [saki_meet_20](#d-saki_meet_20)

    <span id="d-saki_pearls_10"></span>**`saki_pearls_10`** Saki: “Are you returning because you were successful in retrieving the pearls?”

    - “Yeah, here they are.” *(if hand over 5× [Soul pearl](../items/soul_pearl.md))* → [saki_pearls_20](#d-saki_pearls_20)
    - “[lie] Yes. Here you go, all five of them.” *(if NOT carry 5× [Soul pearl](../items/soul_pearl.md))* → [saki_not_5_pearls](#d-saki_not_5_pearls)

    <span id="d-saki_trapped_10"></span>**`saki_trapped_10`** Saki: “I'm not able to get out!”

    - Next → [saki_trapped_20](#d-saki_trapped_20)

    <span id="d-saki_meet_20"></span>**`saki_meet_20`** Saki: “Saki, my name is. Haunt this area is all I do.”

    - “Pleased to meet you...I think.” → [saki_devotion_selector](#d-saki_devotion_selector)

    <span id="d-saki_pearls_20"></span>**`saki_pearls_20`** Saki: “Thank you for these powerful artifacts!” — **effects:** sets stage 30 of [Dominion](../quests/dominion.md#stage-30), removes monsters from undertell_1_1


    <span id="d-saki_not_5_pearls"></span>**`saki_not_5_pearls`** Saki: “You still have to find all of them. Now go.”

    - “Right, I need to find five of them.” → *conversation ends*

    <span id="d-saki_trapped_20"></span>**`saki_trapped_20`** [Voice of Shannal](../monsters/voice_shannal.md): “My barriers are not just physical, but magical. No one can enter or leave Undertell without my say so. $playername, get this guy!” — **effects:** sets stage 70 of [Dominion](../quests/dominion.md#stage-70)

    - Next → [saki_fight](#d-saki_fight)

    <span id="d-saki_devotion_selector"></span>**`saki_devotion_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 450 of [Devotion](../quests/devotion.md#stage-450))* → [saki_devotion_450_10](#d-saki_devotion_450_10)
    - branch 2 *(if reached stage 480 of [Devotion](../quests/devotion.md#stage-480))* → [saki_devotion_480_10](#d-saki_devotion_480_10)

    <span id="d-saki_fight"></span>**`saki_fight`** [Saki](../monsters/saki.md): “The kid can try!”

    - “It'll be my pleasure!” → [saki_fight_20](#d-saki_fight_20)

    <span id="d-saki_devotion_450_10"></span>**`saki_devotion_450_10`** Saki: “Kha'zaan are no more, thanks to you. Their spirits lingered, making us hide.”

    - Next → [saki_dominion_10](#d-saki_dominion_10)

    <span id="d-saki_devotion_480_10"></span>**`saki_devotion_480_10`** Saki: “Kha'zaan are no more. However, in the future, be wary, and learn not to get bamboozled. Hope you have learned your lesson.”

    - Next → [saki_devotion_480_ysrine_10](#d-saki_devotion_480_ysrine_10)

    <span id="d-saki_fight_20"></span>**`saki_fight_20`** Saki: “You can't have what is mine! I shall use this power to cleanse a corner of Dhayavar and make it my Dominion!”

    - “You followers of Kazaul - you want everything for yourself! Give them up!” → *fight starts*

    <span id="d-saki_dominion_10"></span>**`saki_dominion_10`** Saki: “Well, now you need to find more spirits in this place. Ours.”

    - “And you want me to liberate them. Why?” → [saki_dominion_20](#d-saki_dominion_20)

    <span id="d-saki_devotion_480_ysrine_10"></span>**`saki_devotion_480_ysrine_10`** [Ysrine](../monsters/ysrine.md): “Aye, little one. What were you thinking?”

    - Next → [saki_devotion_480_20](#d-saki_devotion_480_20)

    <span id="d-saki_dominion_20"></span>**`saki_dominion_20`** Saki: “Because while the light of Elythara may not be extinguished, it has dimmed here in Dhayavar.”

    - “Why would your colleagues be spirits? You won the war.” → [saki_dominion_30](#d-saki_dominion_30)

    <span id="d-saki_devotion_480_20"></span>**`saki_devotion_480_20`** [Saki](../monsters/saki.md): “Anyways, it was their spirits that lingered, making us hide.”

    - Next → [saki_dominion_10](#d-saki_dominion_10)

    <span id="d-saki_dominion_30"></span>**`saki_dominion_30`** Saki: “Did we win? Perhaps. Narrowly. And not decisively. The Shadow remains, and monsters from the other realm still roam freely.”

    - “They lost their bodies during the war?” → [saki_dominion_40](#d-saki_dominion_40)

    <span id="d-saki_dominion_40"></span>**`saki_dominion_40`** Saki: “Yes. Five of my closest colleagues lost their corporeal forms here. The magic was heavy, and Elythara's blessing caused their spirits to linger.”

    - “Like the Kha'zaan shades.” → [saki_dominion_50](#d-saki_dominion_50)

    <span id="d-saki_dominion_50"></span>**`saki_dominion_50`** Saki: “Er...yes. Similar. And now that the Kha'zaan are gone, they remain. Will you help them?”

    - “They will not attack me?” → [saki_dominion_60](#d-saki_dominion_60)

    <span id="d-saki_dominion_60"></span>**`saki_dominion_60`** [Lethgar miner ghost](../monsters/lethgar_miner_ghost.md): “They helped defend Dhayavar. They are not likely to harm any of us now.”

    - “Very well. What needs to be done?” → [saki_dominion_70](#d-saki_dominion_70)

    <span id="d-saki_dominion_70"></span>**`saki_dominion_70`** [Saki](../monsters/saki.md): “You are right to be wary. But I swear on Elythara, no harm will come from us.”

    - “Tell me what I must do.” → [saki_dominion_80](#d-saki_dominion_80)

    <span id="d-saki_dominion_80"></span>**`saki_dominion_80`** Saki: “When they fell, their souls condensed into pearls. Five in total.”

    - “Pearls?” → [saki_dominion_90](#d-saki_dominion_90)

    <span id="d-saki_dominion_90"></span>**`saki_dominion_90`** Saki: “Yes. Shimmering soul pearls. Liches gathered them, unaware of what they carried.”

    - “So I must destroy the liches and recover the pearls.” → [saki_dominion_100](#d-saki_dominion_100)

    <span id="d-saki_dominion_100"></span>**`saki_dominion_100`** Saki: “They will return again and again unless stopped. Kill them, reclaim the pearls, and bring them here.” — **effects:** sets stage 20 of [Dominion](../quests/dominion.md#stage-20), spawns monsters on undertell_21, spawns monsters on undertell_3_lava_01, spawns monsters on undertell_4_01, spawns monsters on undertell_7_10, spawns monsters on undertell_5

    - “I will return with the soul pearls.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 25 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `saki` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `saki` |
    | Loot table | `saki_dl` |
    | Conversation | `saki_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_newb_1:122` |
    | Defined in | `res/raw/monsterlist_undertell.json` |

    Raw data:

    ```json
    {
     "id": "saki",
     "name": "Saki",
     "iconID": "monsters_newb_1:122",
     "maxHP": 498,
     "maxAP": 12,
     "unique": 1,
     "monsterClass": "ghost",
     "attackDamage": {
      "min": 5,
      "max": 7
     },
     "phraseID": "saki_selector",
     "droplistID": "saki_dl",
     "attackCost": 4,
     "attackChance": 230,
     "blockChance": 233,
     "damageResistance": 14,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "deathtouch",
        "magnitude": 1,
        "duration": 3,
        "chance": "50"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=saki.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=saki.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=saki.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=saki.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
