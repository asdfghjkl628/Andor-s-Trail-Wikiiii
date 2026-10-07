---
description: "Teacher is an NPC who can also be fought in Andor's Trail, found in Brimhaven."
---

# ![](../assets/icons/monsters/monsters_ld1_155.png){ .sprite } Teacher

**Where to find Teacher:** Brimhaven: [brimhaven_school](../maps/brimhaven_school.md#pin-npc-brv_teacher)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_155.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Brimhaven |
| **Class** | Humanoid |
| **HP** | 150 |
| **XP when defeated** | 282 |
| **Entry ID** | `brv_teacher` |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 150 |
| XP when defeated | 282 |
| Damage | 3 to 7 |
| Attack chance | 40 |
| Block chance | 130 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brimhaven_school](../maps/brimhaven_school.md) | Brimhaven | 1 | – |

## Quests that count defeats

- [Lessons learned](../quests/brv_school2.md#stage-122) with stepping on a trigger on [brimhaven_school](../maps/brimhaven_school.md) checks that this enemy has been defeated.
- A conversation with [Statue](../monsters/brv_school_statue.md) ([brimhaven_school](../maps/brimhaven_school.md)) checks that this enemy has been defeated.

## Quests

- [Lessons learned](../quests/brv_school2.md): stages 120, 124, 200, 210, 220, 230
- [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md): stages 10, 40

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Teacher. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_teacher.json" data-npc="Teacher" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (37 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_teacher"></span>**`brv_teacher`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 230 of [Lessons learned](../quests/brv_school2.md#stage-230))* → [brv_teacher_230](#d-brv_teacher_230)
    - branch 2 *(if reached stage 220 of [Lessons learned](../quests/brv_school2.md#stage-220))* → [brv_teacher_220](#d-brv_teacher_220)
    - branch 3 *(if reached stage 210 of [Lessons learned](../quests/brv_school2.md#stage-210))* → [brv_teacher_210](#d-brv_teacher_210)
    - branch 4 *(if reached stage 200 of [Lessons learned](../quests/brv_school2.md#stage-200))* → [brv_teacher_200](#d-brv_teacher_200)
    - branch 5 *(if reached stage 152 of [Lessons learned](../quests/brv_school2.md#stage-152))* → [brv_teacher_152](#d-brv_teacher_152)
    - branch 6 *(if reached stage 150 of [Lessons learned](../quests/brv_school2.md#stage-150))* → [brv_teacher_150](#d-brv_teacher_150)
    - branch 7 *(if reached stage 124 of [Lessons learned](../quests/brv_school2.md#stage-124))* → [brv_teacher_124](#d-brv_teacher_124)
    - branch 8 *(if reached stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120))* → [brv_teacher_120](#d-brv_teacher_120)
    - branch 9 *(if reached stage 104 of [Lessons learned](../quests/brv_school2.md#stage-104); reached stage 22 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-22))* → [brv_teacher_104a](#d-brv_teacher_104a)
    - branch 10 *(if reached stage 104 of [Lessons learned](../quests/brv_school2.md#stage-104))* → [brv_teacher_104b](#d-brv_teacher_104b)
    - branch 11 *(if reached stage 102 of [Lessons learned](../quests/brv_school2.md#stage-102))* → [brv_teacher_102](#d-brv_teacher_102)
    - branch 12 *(if reached stage 60 of [Lessons learned](../quests/brv_school2.md#stage-60))* → [brv_teacher_60](#d-brv_teacher_60)
    - branch 13 *(if reached stage 40 of [Lessons learned](../quests/brv_school2.md#stage-40))* → [brv_teacher_40](#d-brv_teacher_40)
    - branch 14 *(if reached stage 30 of [Lessons learned](../quests/brv_school2.md#stage-30))* → [brv_teacher_30](#d-brv_teacher_30)
    - branch 15 *(if reached stage 12 of [Lessons learned](../quests/brv_school2.md#stage-12))* → [brv_teacher_12](#d-brv_teacher_12)
    - branch 16 → [brv_school_enter_20](#d-brv_school_enter_20)

    <span id="d-brv_teacher_230"></span>**`brv_teacher_230`** Teacher: “Murderer! Out of my sight!”


    <span id="d-brv_teacher_220"></span>**`brv_teacher_220`** Teacher: “Ah, my best student! Welcome back to my school.”


    <span id="d-brv_teacher_210"></span>**`brv_teacher_210`** Teacher: “I remember that I banned you from this school! What are you doing here?”


    <span id="d-brv_teacher_200"></span>**`brv_teacher_200`** Teacher: “Thank you again for saving me and my class. You are always welcome here!”


    <span id="d-brv_teacher_152"></span>**`brv_teacher_152`** Teacher: “where... where am I? And you, kid? I have never seen you before. What are you doing in my class?”

    - “Good morning! Do not worry about me, I'll be gone immediately.” → *conversation ends*
    - “I just destroyed the evil statue in the corner.” → [brv_teacher_152_10](#d-brv_teacher_152_10)

    <span id="d-brv_teacher_150"></span>**`brv_teacher_150`** Teacher: “Have you gone mad? Why did you release this monster?”

    - “Instead of scolding me, it would be better if you could think of something helpful.” → *conversation ends*
    - “You are mad yourself! Who brought this monster here?” → *conversation ends*

    <span id="d-brv_teacher_124"></span>**`brv_teacher_124`** [Teacher](../monsters/brv_teacher.md): “Very, very good!”

    - Next → [brv_teacher_124_10](#d-brv_teacher_124_10)

    <span id="d-brv_teacher_120"></span>**`brv_teacher_120`** [Teacher](../monsters/brv_teacher.md): “Enough - stop now! I have seen enough. You have an interesting fighting style.” — **effects:** sets stage 124 of [Lessons learned](../quests/brv_school2.md#stage-124), clears stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120), spawns monsters on brimhaven_school

    - “Thank you.” → [brv_teacher_120_10](#d-brv_teacher_120_10)

    <span id="d-brv_teacher_104a"></span>**`brv_teacher_104a`** Teacher: “Very, very good!”

    - Next → [brv_teacher_104a_10](#d-brv_teacher_104a_10)

    <span id="d-brv_teacher_104b"></span>**`brv_teacher_104b`** Teacher: “I saw that you cheated!”

    - Next → [brv_teacher_104b_10](#d-brv_teacher_104b_10)

    <span id="d-brv_teacher_102"></span>**`brv_teacher_102`** [Teacher](../monsters/brv_teacher.md): “What have you done! You killed Golin! Murdered him!”

    - “It was not intentional.” → [brv_teacher_102_10](#d-brv_teacher_102_10)
    - “He earned it.” → [brv_teacher_102_10](#d-brv_teacher_102_10)

    <span id="d-brv_teacher_60"></span>**`brv_teacher_60`** Teacher: “Do you have a question?”

    - “I'd like to duel with you.” → [brv_teacher_60_10](#d-brv_teacher_60_10)
    - “No, madam.” → *conversation ends*

    <span id="d-brv_teacher_40"></span>**`brv_teacher_40`** Teacher: “Back to your seat, while I explain the rules!”


    <span id="d-brv_teacher_30"></span>**`brv_teacher_30`** Teacher: “I won't have you running around during my history lesson! Back to your seat!”


    <span id="d-brv_teacher_12"></span>**`brv_teacher_12`** Teacher: “You noticed our beautiful mascot? I just love it.”

    - “Eh, really?” → [brv_teacher_12_10](#d-brv_teacher_12_10)

    <span id="d-brv_school_enter_20"></span>**`brv_school_enter_20`** [Teacher](../monsters/brv_teacher.md): “No walking around in my lessons! Please sit down.” — **effects:** sets stage 10 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-10)

    - “OK.” → [brv_school_enter_90](#d-brv_school_enter_90)

    <span id="d-brv_teacher_152_10"></span>**`brv_teacher_152_10`** Teacher: “The statue is gone? What a relief - I don't know how to thank you! I never had a good feeling about it.” — **effects:** sets stage 200 of [Lessons learned](../quests/brv_school2.md#stage-200)

    - “Yes, it seems that it had enchanted you all.” → [brv_teacher_152_20](#d-brv_teacher_152_20)

    <span id="d-brv_teacher_124_10"></span>**`brv_teacher_124_10`** Teacher: “I couldn't have done it better!”

    - “It was no big thing...” → [brv_teacher_124_20](#d-brv_teacher_124_20)

    <span id="d-brv_teacher_120_10"></span>**`brv_teacher_120_10`** [Teacher](../monsters/brv_teacher.md): “I don't think that I could teach you anything new.”

    - Next → [brv_teacher_124_20](#d-brv_teacher_124_20)

    <span id="d-brv_teacher_104a_10"></span>**`brv_teacher_104a_10`** Teacher: “You treated Golin in a great way, I couldn't have done it better!”

    - “It was no big thing...” → [brv_teacher_104a_20](#d-brv_teacher_104a_20)

    <span id="d-brv_teacher_104b_10"></span>**`brv_teacher_104b_10`** Teacher: “You didn't use the harmless school gear. Golin could have been injured!”

    - “Eh, yes...” → [brv_teacher_104b_20](#d-brv_teacher_104b_20)

    <span id="d-brv_teacher_102_10"></span>**`brv_teacher_102_10`** Teacher: “You killed Golin! You actually killed him! I don't believe it!”

    - “Eh...” → [brv_teacher_102_20](#d-brv_teacher_102_20)
    - “It was an accident, tragic.” → [brv_teacher_102_20](#d-brv_teacher_102_20)
    - “Your little favorite provoked me.” → [brv_teacher_102_20](#d-brv_teacher_102_20)

    <span id="d-brv_teacher_60_10"></span>**`brv_teacher_60_10`** Teacher: “What an interesting idea! Nobody ever asked me. Well, I shouldn't do it, I might hurt you. But it is tempting.”

    - “Could we begin?” → [brv_teacher_60_20](#d-brv_teacher_60_20)

    <span id="d-brv_teacher_12_10"></span>**`brv_teacher_12_10`** Teacher: “Now hurry, take a seat!”


    <span id="d-brv_school_enter_90"></span>**`brv_school_enter_90`** Teacher: “No talking, please.”

    - “But...” → [brv_school_enter_90](#d-brv_school_enter_90)

    <span id="d-brv_teacher_152_20"></span>**`brv_teacher_152_20`** Teacher: “I still can't believe it. How could I have let this ghastly mascot into here? Especially me, as a learned teacher. I should have known better.”

    - Next → [brv_teacher_152_90](#d-brv_teacher_152_90)

    <span id="d-brv_teacher_124_20"></span>**`brv_teacher_124_20`** Teacher: “As a reward, you can get yourself a cake from Arlish at the general store. Tell her I sent you.” — **effects:** sets stage 220 of [Lessons learned](../quests/brv_school2.md#stage-220), sets stage 40 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-40)

    - “Thank you!” → *conversation ends*

    <span id="d-brv_teacher_104a_20"></span>**`brv_teacher_104a_20`** Teacher: “As a reward, you can get yourself a cake from Arlish at the general store. Tell her I sent you.” — **effects:** sets stage 40 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-40)

    - “Thank you!” → [brv_teacher_104a_30](#d-brv_teacher_104a_30)

    <span id="d-brv_teacher_104b_20"></span>**`brv_teacher_104b_20`** Teacher: “I cannot accept such a behaviour! You have to leave our school - now!” — **effects:** sets stage 210 of [Lessons learned](../quests/brv_school2.md#stage-210)

    - Next → *conversation ends*

    <span id="d-brv_teacher_102_20"></span>**`brv_teacher_102_20`** Teacher: “I still can't believe it. Leave the school - now!” — **effects:** sets stage 230 of [Lessons learned](../quests/brv_school2.md#stage-230)

    - Next → *conversation ends*

    <span id="d-brv_teacher_60_20"></span>**`brv_teacher_60_20`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if wearing [Wooden sword](../items/brv_school_sword.md); wearing [Paper shield](../items/brv_school_shield.md))* → [brv_teacher_60_24](#d-brv_teacher_60_24)
    - branch 2 → [brv_teacher_60_22](#d-brv_teacher_60_22)

    <span id="d-brv_teacher_152_90"></span>**`brv_teacher_152_90`** Teacher: “We all owe our lives to you! As a reward, you can get yourself a cake from Arlish at the general store. Tell her I sent you.” — **effects:** sets stage 40 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-40)

    - “Thank you!” → *conversation ends*

    <span id="d-brv_teacher_104a_30"></span>**`brv_teacher_104a_30`** Teacher: “I can't teach you things that are new for you. Leave now, you don't need to come to school anymore.” — **effects:** sets stage 220 of [Lessons learned](../quests/brv_school2.md#stage-220)

    - Next → *conversation ends*

    <span id="d-brv_teacher_60_24"></span>**`brv_teacher_60_24`** Teacher: “Let's see what you are able to do!”

    - “Draw your weapon!” → [brv_teacher_60_26](#d-brv_teacher_60_26)
    - “I changed my mind. Let me go for now.” → *conversation ends*

    <span id="d-brv_teacher_60_22"></span>**`brv_teacher_60_22`** Teacher: “But of course you have to use the school weapon set first. Come back when you are properly equipped.”


    <span id="d-brv_teacher_60_26"></span>**`brv_teacher_60_26`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 120 of [Lessons learned](../quests/brv_school2.md#stage-120)

    - branch 1 → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 37 lines added |
| [v0.7.15](../versions/0.7.15.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brv_teacher` |
    | Spawn group | `brv_teacher_save` |
    | Loot table | – |
    | Conversation | `brv_teacher` |
    | Faction | `brv_fct_school_duel` |
    | Movement | – |
    | Icon | `monsters_ld1:155` |
    | Defined in | `res/raw/monsterlist_brimhaven2.json` |

    Raw data:

    ```json
    {
     "id": "brv_teacher",
     "name": "Teacher",
     "iconID": "monsters_ld1:155",
     "maxHP": 150,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 7
     },
     "spawnGroup": "brv_teacher_save",
     "faction": "brv_fct_school_duel",
     "phraseID": "brv_teacher",
     "attackCost": 4,
     "attackChance": 40,
     "blockChance": 130,
     "damageResistance": 5
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_teacher.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_teacher.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_teacher.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_teacher.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
