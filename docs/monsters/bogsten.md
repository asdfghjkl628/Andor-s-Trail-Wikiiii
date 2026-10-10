---
description: "Bogsten is an NPC you can also fight in Andor's Trail, found in Bogsten 1. Starts Fungi panic."
---

# ![](../assets/icons/monsters/monsters_rltiles1_77.png){ .sprite } Bogsten

**Where to find Bogsten:** [Bogsten 1](../maps/bogsten1.md#pin-npc-bogsten)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles1_77.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Role** | Starts [Fungi panic](../quests/fungi_panic.md) |
| **Found in** | Bogsten 1 |
| **Class** | Humanoid |
| **HP** | 35 |
| **XP when defeated** | 53 |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

!!! warning "You can fight Bogsten"
    Answering “Enough talk, time to die.” starts a fight with Bogsten.

## Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 35 |
| XP when defeated | 53 |
| Damage | 3 to 6 |
| AC | 110 |
| BC | 30 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Bogsten's staff](../items/bogsten_staff.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 1 to 10 |
| [Small empty vial](../items/vial_empty1.md) | 25% | 100 to 200 |
| [Bag with mushrooms](../items/fungi_panic_bag.md) | 100% | 1 |

## Quests that count defeats

- [Fungi panic](../quests/fungi_panic.md#stage-90) with stepping on a trigger on [Bogsten 4](../maps/bogsten4.md) checks that this enemy has been defeated.
- A conversation with [Zuul'khan](../monsters/zuul_khan.md) ([Bogsten 4](../maps/bogsten4.md)) checks that this enemy has been defeated.
- A conversation with [Undina Bogsten](../monsters/bogsten_granny.md) ([Mushroom m 2 4](../maps/mushroom_m2_4.md)), [Undina Bogsten](../monsters/bogsten_granny.md#v-bogsten_granny1) ([Mushroom m 2 4](../maps/mushroom_m2_4.md)) checks that this enemy has been defeated.

## Quests

- [Fungi panic](../quests/fungi_panic.md): stages 10, 30, 40, 52, 60, 100, 102

## Dialogue simulator

Talk to Bogsten as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/bogsten_start_select.json" data-npc="Bogsten" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (54 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-bogsten_start_select"></span>**`bogsten_start_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 115 of [Fungi panic](../quests/fungi_panic.md#stage-115))* → [bogsten_115_10](#d-bogsten_115_10)
    - branch 2 *(if reached stage 100 of [Fungi panic](../quests/fungi_panic.md#stage-100))* → [bogsten_100_10](#d-bogsten_100_10)
    - branch 3 *(if reached stage 70 of [Fungi panic](../quests/fungi_panic.md#stage-70))* → [bogsten_70_10](#d-bogsten_70_10)
    - branch 4 *(if reached stage 60 of [Fungi panic](../quests/fungi_panic.md#stage-60))* → [bogsten_60_20](#d-bogsten_60_20)
    - branch 5 *(if reached stage 52 of [Fungi panic](../quests/fungi_panic.md#stage-52))* → [bogsten_52_10](#d-bogsten_52_10)
    - branch 6 *(if reached stage 50 of [Fungi panic](../quests/fungi_panic.md#stage-50))* → [bogsten_50_10](#d-bogsten_50_10)
    - branch 7 *(if reached stage 40 of [Fungi panic](../quests/fungi_panic.md#stage-40))* → [bogsten_40_10](#d-bogsten_40_10)
    - branch 8 *(if reached stage 30 of [Fungi panic](../quests/fungi_panic.md#stage-30))* → [bogsten_30_10](#d-bogsten_30_10)
    - branch 9 *(if reached stage 10 of [Fungi panic](../quests/fungi_panic.md#stage-10))* → [bogsten_10_10](#d-bogsten_10_10)
    - branch 10 *(if NOT reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50); NOT reached stage 100 of [Delicious soup](../quests/gison_soup.md#stage-100); NOT reached stage 110 of [Delicious soup](../quests/gison_soup.md#stage-110))* → [bogsten_waitforsoup](#d-bogsten_waitforsoup)
    - branch 11 → [bogsten_start_0](#d-bogsten_start_0)

    <span id="d-bogsten_115_10"></span>**`bogsten_115_10`** Bogsten: “Now what has happened down there?”

    - “I met a sorcerer called Zuul'khan. He offered me something of value, so now I'll kill you.” → [bogsten_115_20](#d-bogsten_115_20)

    <span id="d-bogsten_100_10"></span>**`bogsten_100_10`** Bogsten: “Hi kid. Nice to meet you again.”

    - “I've finally defeated Zuul'khan and his giant mushroom. You won't have to worry about them anymore.” *(if reached stage 200 of [Fungi panic](../quests/fungi_panic.md#stage-200))* → [bogsten_200_10](#d-bogsten_200_10)

    <span id="d-bogsten_70_10"></span>**`bogsten_70_10`** Bogsten: “It took you a long time to get back here. What has happened down there?”

    - “I met an old sorcerer named Zuul'khan in the cave.” → [bogsten_70_20](#d-bogsten_70_20)

    <span id="d-bogsten_60_20"></span>**`bogsten_60_20`** Bogsten: “Now that I am restored again, I should go back to work.”

    - Next → [bogsten_60_22](#d-bogsten_60_22)

    <span id="d-bogsten_52_10"></span>**`bogsten_52_10`** Bogsten: “Aaah. I feel much better. That was neat. You have my everlasting thanks, kid.”

    - “I am glad I could help.” → [bogsten_60_20](#d-bogsten_60_20)
    - “I'd prefer to have my 150 gold back.” → [bogsten_52_12](#d-bogsten_52_12)

    <span id="d-bogsten_50_10"></span>**`bogsten_50_10`** Bogsten: “I hope you have good news for me.”

    - “Yes, I have got a potion for you.” *(if hand over 1× [Curative potion against mushroom wounding](../items/fungi_panic_cure.md))* → [bogsten_50_20](#d-bogsten_50_20)
    - “No, not yet.” → *conversation ends*

    <span id="d-bogsten_40_10"></span>**`bogsten_40_10`** Bogsten: “Quick, I am dying! The potion maker is the only one who could help me!”

    - “I'll hurry.” → *conversation ends*

    <span id="d-bogsten_30_10"></span>**`bogsten_30_10`** Bogsten: “Have you collected the spores already?”

    - “Yes. I have them with me.” *(if carry 1× [Spores of the giant mushroom](../items/fungi_panic_spores.md))* → [bogsten_30_20](#d-bogsten_30_20)
    - “No, not yet.” → [bogsten_30_12](#d-bogsten_30_12)

    <span id="d-bogsten_10_10"></span>**`bogsten_10_10`** Bogsten: “Have you got the cure?”

    - “Not yet. The potion merchant needs some spore sample to prepare it.” *(if reached stage 20 of [Fungi panic](../quests/fungi_panic.md#stage-20))* → [bogsten_20_10](#d-bogsten_20_10)
    - “No, not yet.” → *conversation ends*

    <span id="d-bogsten_waitforsoup"></span>**`bogsten_waitforsoup`** Bogsten: “Hmm ... hmm ...”

    - “Hello, I am ...” → [bogsten_waitforsoup_1](#d-bogsten_waitforsoup_1)

    <span id="d-bogsten_start_0"></span>**`bogsten_start_0`** Bogsten: “Oh young kid, you look like someone nice. I don't want you to be injured because of me. I urge you to leave!”

    - “What's going on?” → [bogsten_start_1](#d-bogsten_start_1)

    <span id="d-bogsten_115_20"></span>**`bogsten_115_20`** Bogsten: “You...what? After saving me, you would turn against me?”

    - “Enough talk, time to die.” → *fight starts*

    <span id="d-bogsten_200_10"></span>**`bogsten_200_10`** Bogsten: “Oh, that's great news! I suppose I can get back to work with the mushrooms, then. Maybe tomorrow, after I've had time to rest.”

    - “Goodbye.” → *conversation ends*
    - “How can you be so lazy?” → [bogsten_200_20](#d-bogsten_200_20)

    <span id="d-bogsten_70_20"></span>**`bogsten_70_20`** Bogsten: “Zuul'khan? Hmm, I think I have heard this name already.”

    - “He told me that your family imprisoned him using an ancient petrifying spell.” → [bogsten_70_30](#d-bogsten_70_30)

    <span id="d-bogsten_60_22"></span>**`bogsten_60_22`** Bogsten: “I really should.”

    - Next → [bogsten_60_24](#d-bogsten_60_24)

    <span id="d-bogsten_52_12"></span>**`bogsten_52_12`** Bogsten: “No, no, no. The uplifting feeling of saving a life cannot be balanced with gold.”

    - “No?” → [bogsten_52_14](#d-bogsten_52_14)
    - “You are right.” → [bogsten_60_20](#d-bogsten_60_20)

    <span id="d-bogsten_50_20"></span>**`bogsten_50_20`** Bogsten: “Finally! [He pours down the liquid greedily]” — **effects:** sets stage 52 of [Fungi panic](../quests/fungi_panic.md#stage-52)

    - “And there goes 150 gold again...” → [bogsten_52_10](#d-bogsten_52_10)

    <span id="d-bogsten_30_20"></span>**`bogsten_30_20`** Bogsten: “These spores would do. Please go and give them to Fallhaven's potion merchant.” — **effects:** sets stage 40 of [Fungi panic](../quests/fungi_panic.md#stage-40)

    - “I'll hurry.” → *conversation ends*

    <span id="d-bogsten_30_12"></span>**`bogsten_30_12`** Bogsten: “Please get them for me.”

    - Next → *conversation ends*

    <span id="d-bogsten_20_10"></span>**`bogsten_20_10`** Bogsten: “I'm sorry to have dragged you into this, kid. Take this key. It will open the way to my mushroom cave. You will certainly find what you need.” — **effects:** sets stage 30 of [Fungi panic](../quests/fungi_panic.md#stage-30), gives 1× [Bogsten's key](../items/bogsten_key.md)

    - “I will have a look.” → *conversation ends*

    <span id="d-bogsten_waitforsoup_1"></span>**`bogsten_waitforsoup_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (20%))* → [bogsten_waitforsoup_50](#d-bogsten_waitforsoup_50)
    - branch 2 *(if random chance (25%))* → [bogsten_waitforsoup_40](#d-bogsten_waitforsoup_40)
    - branch 3 *(if random chance (33%))* → [bogsten_waitforsoup_30](#d-bogsten_waitforsoup_30)
    - branch 4 *(if random chance (50%))* → [bogsten_waitforsoup_20](#d-bogsten_waitforsoup_20)
    - branch 5 → [bogsten_waitforsoup_10](#d-bogsten_waitforsoup_10)

    <span id="d-bogsten_start_1"></span>**`bogsten_start_1`** Bogsten: “No. I shouldn't be telling you. It's too dangerous.”

    - “I'm sure I can help.” → [bogsten_start_2](#d-bogsten_start_2)
    - “I'm way stronger than I look.” → [bogsten_start_2](#d-bogsten_start_2)
    - “OK. Nevermind.” → *conversation ends*

    <span id="d-bogsten_200_20"></span>**`bogsten_200_20`** Bogsten: “When you get to my age, maybe you'll understand that you don't need to rush through life. Now leave me to my rest.”


    <span id="d-bogsten_70_30"></span>**`bogsten_70_30`** Bogsten: “A petrifying spell? But this has to be renewed every week.”

    - “Exactly. Thanks to your laxity, Zuul'khan got free.” → [bogsten_70_40](#d-bogsten_70_40)

    <span id="d-bogsten_60_24"></span>**`bogsten_60_24`** Bogsten: “I should...”

    - Next → [bogsten_60_26](#d-bogsten_60_26)

    <span id="d-bogsten_52_14"></span>**`bogsten_52_14`** Bogsten: “No.”

    - Next → [bogsten_60_20](#d-bogsten_60_20)

    <span id="d-bogsten_waitforsoup_50"></span>**`bogsten_waitforsoup_50`** Bogsten: “All is flux, nothing stays still.”

    - “What?” → [bogsten_waitforsoup_90](#d-bogsten_waitforsoup_90)

    <span id="d-bogsten_waitforsoup_40"></span>**`bogsten_waitforsoup_40`** Bogsten: “How could they see anything but the shadows if they were never allowed to move their heads?”

    - “What?” → [bogsten_waitforsoup_90](#d-bogsten_waitforsoup_90)

    <span id="d-bogsten_waitforsoup_30"></span>**`bogsten_waitforsoup_30`** Bogsten: “There are two things a person should never be angry at: What they can help, and what they cannot.”

    - “What?” → [bogsten_waitforsoup_90](#d-bogsten_waitforsoup_90)

    <span id="d-bogsten_waitforsoup_20"></span>**`bogsten_waitforsoup_20`** Bogsten: “An empty vessel makes the loudest sound. So they that have the least wit are the greatest babblers.”

    - “What?” → [bogsten_waitforsoup_90](#d-bogsten_waitforsoup_90)

    <span id="d-bogsten_waitforsoup_10"></span>**`bogsten_waitforsoup_10`** Bogsten: “Wise men speak because they have something to say; fools because they have to say something.”

    - “What?” → [bogsten_waitforsoup_90](#d-bogsten_waitforsoup_90)

    <span id="d-bogsten_start_2"></span>**`bogsten_start_2`** Bogsten: “My family has used this place to grow mushrooms for five generations. Our mushrooms are famous from Feygard to Nor City, loved by gourmets and potion makers alike.”

    - Next → [bogsten_start_3](#d-bogsten_start_3)

    <span id="d-bogsten_70_40"></span>**`bogsten_70_40`** Bogsten: “And why is this Zuul'khan still running around? What did you do the whole time down there? Go and finish your work!”

    - “What? Do it yourself!” → *conversation ends*
    - “Do you actually do anything with your own hands?” → *conversation ends*
    - “I already defeated Zuul'khan.” *(if killed 1× [Zuul'khan](../monsters/zuul_khan.md))* → [bogsten_90_20](#d-bogsten_90_20)

    <span id="d-bogsten_60_26"></span>**`bogsten_60_26`** Bogsten: “What? ... Ah, yes - work.”

    - “You seem a bit distracted.” → [bogsten_60_30](#d-bogsten_60_30)

    <span id="d-bogsten_waitforsoup_90"></span>**`bogsten_waitforsoup_90`** Bogsten: “Leave me now, kid. I'm trying to think, don't confuse me with your presence.”

    - “OK. I will come back when you have more time.” → *conversation ends*

    <span id="d-bogsten_start_3"></span>**`bogsten_start_3`** Bogsten: “Last month, I went to Nor City to sell an excellent batch and decided to stay a little longer.”

    - Next → [bogsten_start_4](#d-bogsten_start_4)

    <span id="d-bogsten_90_20"></span>**`bogsten_90_20`** Bogsten: “So Zuul'khan is dead?”

    - “I don't think so. He just disappeared into the ground.” → [bogsten_90_30](#d-bogsten_90_30)

    <span id="d-bogsten_60_30"></span>**`bogsten_60_30`** Bogsten: “Indeed. I can't concentrate.”

    - Next → [bogsten_60_32](#d-bogsten_60_32)

    <span id="d-bogsten_start_4"></span>**`bogsten_start_4`** Bogsten: “You see, my son is studying across the country to become a Shadow priest, and he is currently in the Valanyr temple of the Shadow. I had not seen him for so long, so I decided to visit him.”

    - Next → [bogsten_start_5](#d-bogsten_start_5)

    <span id="d-bogsten_90_30"></span>**`bogsten_90_30`** Bogsten: “Disappeared! I hope he doesn't appear here next. Well, as a reward for your efforts, please take this bag of mushrooms to the potion merchant in Fallhaven. I'm sure he'll prepare something good for you.” — **effects:** sets stage 100 of [Fungi panic](../quests/fungi_panic.md#stage-100), gives 1× [Bag with mushrooms](../items/fungi_panic_bag.md)

    - Next → [bogsten_90_40](#d-bogsten_90_40)

    <span id="d-bogsten_60_32"></span>**`bogsten_60_32`** Bogsten: “There seems to be an evil force near us. Yes, that must be it.”

    - Next → [bogsten_60_34](#d-bogsten_60_34)

    <span id="d-bogsten_start_5"></span>**`bogsten_start_5`** Bogsten: “Anyway, when I came back here, I felt something strange had happened. I couldn't tell what, but I knew evil was around as soon as I touched the door knob.”

    - “Dealing with evil is my favorite hobby.” → [bogsten_start_6](#d-bogsten_start_6)
    - “Get to the point.” → [bogsten_start_6](#d-bogsten_start_6)
    - “I will never help a worshipper of the Shadow!” → *conversation ends*

    <span id="d-bogsten_90_40"></span>**`bogsten_90_40`** Bogsten: “Anyway. The evil force is not gone, so you'll have to go down there again.”

    - “What??” → [bogsten_90_50](#d-bogsten_90_50)

    <span id="d-bogsten_60_34"></span>**`bogsten_60_34`** Bogsten: “I remember my father warned me about this kind of thing before passing away. But I was just a kid and I forgot his advice on how to deal with it.”

    - “Don't worry. I deal with evil every day. Whatever lurks down there, I can handle it.” → [bogsten_60_40](#d-bogsten_60_40)
    - “How can you forget something that important! I guess I have no choice but to go.” → [bogsten_60_40](#d-bogsten_60_40)
    - “Stupid old man. You really think I'm here to clean up your own mess!” → *conversation ends*

    <span id="d-bogsten_start_6"></span>**`bogsten_start_6`** Bogsten: “When I got to my mushroom cave, I was attacked by some sort of giant living mushroom. I've been sick since then, to the point where I'm afraid I won't live long. I've locked all access to my cave to prevent anyone from being hurt.”

    - “You really look bad. How can I help?” → [bogsten_start_7](#d-bogsten_start_7)

    <span id="d-bogsten_90_50"></span>**`bogsten_90_50`** Bogsten: “It has moved probably to another place. But that is someone else's problem.” — **effects:** sets stage 102 of [Fungi panic](../quests/fungi_panic.md#stage-102)

    - “Honestly now?” → [bogsten_90_54](#d-bogsten_90_54)

    <span id="d-bogsten_60_40"></span>**`bogsten_60_40`** Bogsten: “Very good. Please go into my caves and check if everything is right.”

    - “You're getting on my nerves now.” → [bogsten_60_40](#d-bogsten_60_40)
    - “OK. Down again.” → [bogsten_60_50](#d-bogsten_60_50)
    - “No way! You've bored me more than enough!” → *conversation ends*

    <span id="d-bogsten_start_7"></span>**`bogsten_start_7`** Bogsten: “I know this potion maker in Fallhaven. Could you go ask him for a cure?”

    - “Sure. I'll go there right now.” → [bogsten_start_8](#d-bogsten_start_8)
    - “You fool! I'm not here to run your errands!” → *conversation ends*

    <span id="d-bogsten_90_54"></span>**`bogsten_90_54`** Bogsten: “Leave now. I need to rest.”


    <span id="d-bogsten_60_50"></span>**`bogsten_60_50`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [Fungi panic](../quests/fungi_panic.md#stage-60))* → [bogsten_60_52](#d-bogsten_60_52)
    - branch 2 → [bogsten_60_54](#d-bogsten_60_54)

    <span id="d-bogsten_start_8"></span>**`bogsten_start_8`** Bogsten: “Thank you! I'll be waiting for you. Be quick!” — **effects:** sets stage 10 of [Fungi panic](../quests/fungi_panic.md#stage-10)

    - Next → *conversation ends*

    <span id="d-bogsten_60_52"></span>**`bogsten_60_52`** Bogsten: “Don't forget that there are hidden rooms. I gave you my necklace so that you can find them. Wear it down in the caves. Never take it off.”

    - “I'm curious what I will find there.” → *conversation ends*

    <span id="d-bogsten_60_54"></span>**`bogsten_60_54`** Bogsten: “There are hidden rooms. I'll give you my necklace so that you can find them. Wear it down in the caves. Never take it off.” — **effects:** sets stage 60 of [Fungi panic](../quests/fungi_panic.md#stage-60), gives 1× [Bogsten's necklace](../items/bogsten_necklace.md)

    - “I'm curious what I will find there.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 54 lines added |

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
    | Entry ID | `bogsten` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `bogsten` |
    | Loot table | `bogsten` |
    | Conversation | `bogsten_start_select` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:77` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "bogsten",
     "name": "Bogsten",
     "iconID": "monsters_rltiles1:77",
     "maxHP": 35,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "bogsten",
     "phraseID": "bogsten_start_select",
     "droplistID": "bogsten",
     "attackCost": 5,
     "attackChance": 110,
     "blockChance": 30
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bogsten.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bogsten.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bogsten.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bogsten.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
