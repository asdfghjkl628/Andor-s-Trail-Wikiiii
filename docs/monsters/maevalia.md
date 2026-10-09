---
description: "Maevalia is a non-player character (NPC) in Andor's Trail, found in Prim."
---

# ![](../assets/icons/monsters/monsters_rltiles3_18.png){ .sprite } Maevalia

**Where to find Maevalia:** Prim: [Tradehouse 0](../maps/tradehouse0.md#pin-npc-maevalia)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_18.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Prim |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Destined for great things](../quests/charwood1.md): stages 19, 20, 21, 30, 50, 60, 115
- [Trial by fire](../quests/charwood2.md): stages 15, 40, 50

## Dialogue simulator

Set your quest stages and items, then talk to Maevalia. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/maevalia.json" data-npc="Maevalia" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (69 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-maevalia"></span>**`maevalia`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 19 of [Destined for great things](../quests/charwood1.md#stage-19)

    - branch 1 *(if reached stage 50 of [Trial by fire](../quests/charwood2.md#stage-50))* → [maevalia_q1](#d-maevalia_q1)
    - branch 2 *(if reached stage 40 of [Trial by fire](../quests/charwood2.md#stage-40))* → [maevalia_h5](#d-maevalia_h5)
    - branch 3 *(if reached stage 15 of [Trial by fire](../quests/charwood2.md#stage-15))* → [maevalia_h2](#d-maevalia_h2)
    - branch 4 *(if reached stage 115 of [Destined for great things](../quests/charwood1.md#stage-115))* → [maevalia_d1](#d-maevalia_d1)
    - branch 5 *(if reached stage 60 of [Destined for great things](../quests/charwood1.md#stage-60))* → [maevalia_s1](#d-maevalia_s1)
    - branch 6 *(if reached stage 50 of [Destined for great things](../quests/charwood1.md#stage-50))* → [maevalia_r5](#d-maevalia_r5)
    - branch 7 *(if reached stage 30 of [Destined for great things](../quests/charwood1.md#stage-30))* → [maevalia_r1](#d-maevalia_r1)
    - branch 8 *(if reached stage 20 of [Destined for great things](../quests/charwood1.md#stage-20))* → [maevalia_r0](#d-maevalia_r0)
    - branch 9 → [maevalia0](#d-maevalia0)

    <span id="d-maevalia_q1"></span>**`maevalia_q1`** Maevalia: “Thank you for all your help!”

    - “Can I rest here?” → [maevalia_d2](#d-maevalia_d2)

    <span id="d-maevalia_h5"></span>**`maevalia_h5`** Maevalia: “You actually killed it?” — **effects:** sets stage 40 of [Trial by fire](../quests/charwood2.md#stage-40)

    - Next → [maevalia_h6](#d-maevalia_h6)

    <span id="d-maevalia_h2"></span>**`maevalia_h2`** Maevalia: “Hello again. Did you reach the lower parts of the Charwood mine?”

    - “Can I rest here?” → [maevalia_d2](#d-maevalia_d2)
    - “No, not yet.” → [maevalia_d9](#d-maevalia_d9)
    - “Yes. I encountered a dragon-like creature in the fiery depths of the mine.” *(if reached stage 30 of [Trial by fire](../quests/charwood2.md#stage-30))* → [maevalia_h3](#d-maevalia_h3)

    <span id="d-maevalia_d1"></span>**`maevalia_d1`** Maevalia: “It's good to see that Falothen and Fayvara are well. Anything else that I can help you with?”

    - “Can I rest here?” → [maevalia_d2](#d-maevalia_d2)
    - “Where do you think the monsters came from?” → [maevalia_d3](#d-maevalia_d3)
    - “I talked to Kantya about what happened in the mine.” *(if reached stage 10 of [Trial by fire](../quests/charwood2.md#stage-10))* → [maevalia_d4](#d-maevalia_d4)

    <span id="d-maevalia_s1"></span>**`maevalia_s1`** Maevalia: “Hello again.”

    - Next → [maevalia_r7](#d-maevalia_r7)

    <span id="d-maevalia_r5"></span>**`maevalia_r5`** Maevalia: “While I am very happy to hear that Falothen and Fayvara are alive and well, it saddens me to hear that we've lost not only Ayell, but also Morenavia.”

    - Next → [maevalia_r6](#d-maevalia_r6)

    <span id="d-maevalia_r1"></span>**`maevalia_r1`** Maevalia: “Hello again. Did you find our missing people?”

    - “Can you tell me the story about what happened here, again?” → [maevalia3](#d-maevalia3)
    - “What was I supposed to do again?” → [maevalia25](#d-maevalia25)
    - “Who were the people that I was supposed to look for, again?” → [maevalia17](#d-maevalia17)
    - “Yeah, about those people.” → [maevalia_r2a](#d-maevalia_r2a)

    <span id="d-maevalia_r0"></span>**`maevalia_r0`** Maevalia: “You again.”

    - “Can you tell me the story about what happened here, again?” → [maevalia3](#d-maevalia3)
    - “What now?” → [maevalia16](#d-maevalia16)

    <span id="d-maevalia0"></span>**`maevalia0`** Maevalia: “You there! This is no place for children!”

    - Next → [maevalia1](#d-maevalia1)

    <span id="d-maevalia_d2"></span>**`maevalia_d2`** Maevalia: “Absolutely. Pick any bed you want over there.”


    <span id="d-maevalia_h6"></span>**`maevalia_h6`** Maevalia: “You are truly a hero to us.”

    - Next → [maevalia_h7](#d-maevalia_h7)

    <span id="d-maevalia_d9"></span>**`maevalia_d9`** Maevalia: “Whatever lurks down there, I'm sure it's not happy to get any visitors.”

    - “I'll go down into the Charwood mine and investigate.” → [maevalia_d10](#d-maevalia_d10)

    <span id="d-maevalia_h3"></span>**`maevalia_h3`** Maevalia: “None of us ever dared to venture that deep.”

    - “I haven't killed the creature yet though.” → [maevalia_d9](#d-maevalia_d9)
    - “Whatever that thing was, it won't bother you any more now that I've killed it. Here is one of the bones from its corpse.” *(if hand over 1× [Thukuzun bone](../items/thukuzun.md))* → [maevalia_h5](#d-maevalia_h5)

    <span id="d-maevalia_d3"></span>**`maevalia_d3`** Maevalia: “I have my guesses. Go talk to Kantya about it. I hear she has the full story, and some interesting theories.”


    <span id="d-maevalia_d4"></span>**`maevalia_d4`** Maevalia: “Good. Did she tell you about that marking on the ground? I saw it myself. Nothing like I've ever seen before.”

    - Next → [maevalia_d5](#d-maevalia_d5)

    <span id="d-maevalia_r7"></span>**`maevalia_r7`** Maevalia: “Things will never be the same again for us.”

    - Next → [maevalia_r8](#d-maevalia_r8)

    <span id="d-maevalia_r6"></span>**`maevalia_r6`** Maevalia: “Morenavia was truly a great leader for us. Now, how will we ever be able to find the right paths?”

    - Next → [maevalia_r7](#d-maevalia_r7)

    <span id="d-maevalia3"></span>**`maevalia3`** Maevalia: “We were attacked. We didn't stand a chance, they were too many and we are no fighters.”

    - Next → [maevalia4](#d-maevalia4)

    <span id="d-maevalia25"></span>**`maevalia25`** Maevalia: “I would be very grateful for knowing what happened to the people we are missing.”

    - Next → [maevalia26](#d-maevalia26)

    <span id="d-maevalia17"></span>**`maevalia17`** Maevalia: “In particular, I'm worried about what happened to Morenavia - our leader. None of us that made it back to this cabin saw what happened to her.”

    - Next → [maevalia18](#d-maevalia18)

    <span id="d-maevalia_r2a"></span>**`maevalia_r2a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 41 of [Destined for great things](../quests/charwood1.md#stage-41))* → [maevalia_r2b](#d-maevalia_r2b)
    - branch 2 → [maevalia_r3](#d-maevalia_r3)

    <span id="d-maevalia16"></span>**`maevalia16`** Maevalia: “I sure hope that the people that we are missing are all alive at least.”

    - Next → [maevalia17](#d-maevalia17)

    <span id="d-maevalia1"></span>**`maevalia1`** Maevalia: “The Charwood area has become a dangerous place as of late. You should leave at once unless you want to get killed ... or worse.”

    - “I can handle myself.” → [maevalia2](#d-maevalia2)
    - “What has happened here?” → [maevalia3](#d-maevalia3)

    <span id="d-maevalia_h7"></span>**`maevalia_h7`** Maevalia: “Not only did you manage to find our missing people, but you also freed us from the creature that caused all this trouble.”

    - Next → [maevalia_h8](#d-maevalia_h8)

    <span id="d-maevalia_d10"></span>**`maevalia_d10`** Maevalia: “Thank you.” — **effects:** sets stage 15 of [Trial by fire](../quests/charwood2.md#stage-15)


    <span id="d-maevalia_d5"></span>**`maevalia_d5`** Maevalia: “I wonder what is down there, in the deeper parts of the mine. I bet that whatever is controlling those monsters is still down there.”

    - “I can go look down there if you want.” → [maevalia_d7](#d-maevalia_d7)
    - “This all sounds too dangerous for me. I better not get involved.” → [maevalia_d6](#d-maevalia_d6)

    <span id="d-maevalia_r8"></span>**`maevalia_r8`** Maevalia: “It is at least some comfort to know that we still have Falothen and Fayvara with us.” — **effects:** sets stage 50 of [Destined for great things](../quests/charwood1.md#stage-50)

    - Next → [maevalia_r9](#d-maevalia_r9)

    <span id="d-maevalia4"></span>**`maevalia4`** Maevalia: “They started pouring out of the mine and the surrounding hills.”

    - “Who were?” → [maevalia5](#d-maevalia5)

    <span id="d-maevalia26"></span>**`maevalia26`** Maevalia: “Head up to our mining town of Charwood heights, and look for the missing people.”

    - Next → [maevalia27](#d-maevalia27)

    <span id="d-maevalia18"></span>**`maevalia18`** Maevalia: “I sure hope she's still alive. We could use some of her wisdom and leadership right now to guide us.”

    - Next → [maevalia19](#d-maevalia19)

    <span id="d-maevalia_r2b"></span>**`maevalia_r2b`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 42 of [Destined for great things](../quests/charwood1.md#stage-42))* → [maevalia_r2c](#d-maevalia_r2c)
    - branch 2 → [maevalia_r3](#d-maevalia_r3)

    <span id="d-maevalia_r3"></span>**`maevalia_r3`** Maevalia: “Yes, what about them?”

    - “I'm still trying to find out what happened to all four of them.” → [maevalia_r3b](#d-maevalia_r3b)

    <span id="d-maevalia2"></span>**`maevalia2`** Maevalia: “For your sake, I urge you to leave. While we need all the help we can get, we can't take responsibility for the dangers that has befell our mining town of Charwood.”

    - “What has happened here?” → [maevalia3](#d-maevalia3)

    <span id="d-maevalia_h8"></span>**`maevalia_h8`** Maevalia: “We are forever in your debt. What can we do to ever repay you?”

    - “I'm just happy to help.” → [maevalia_h9](#d-maevalia_h9)
    - “How about some gold for all my troubles?” → [maevalia_h10](#d-maevalia_h10)
    - “I think that one of your most precious items will suffice as payment.” → [maevalia_h11](#d-maevalia_h11)

    <span id="d-maevalia_d7"></span>**`maevalia_d7`** Maevalia: “You would do that for us? Thank you. I don't know what we would do without your help.”

    - Next → [maevalia_d8](#d-maevalia_d8)

    <span id="d-maevalia_d6"></span>**`maevalia_d6`** Maevalia: “Can't say I blame you. Thank you for the help you've provided so far.”


    <span id="d-maevalia_r9"></span>**`maevalia_r9`** Maevalia: “I hear they are both anxious to talk to you now that they're safe. You should go meet them downstairs in the basement.” — **effects:** sets stage 60 of [Destined for great things](../quests/charwood1.md#stage-60)

    - “OK, I'll go see them in the basement.” → *conversation ends*
    - “I've spoken to them both.” *(if reached stage 65 of [Destined for great things](../quests/charwood1.md#stage-65); reached stage 90 of [Destined for great things](../quests/charwood1.md#stage-90))* → [maevalia_r10](#d-maevalia_r10)

    <span id="d-maevalia5"></span>**`maevalia5`** Maevalia: “The monsters. Disgusting, foul smelling monsters. Nothing like we've ever seen before.”

    - Next → [maevalia6](#d-maevalia6)

    <span id="d-maevalia27"></span>**`maevalia27`** Maevalia: “Please, try to be safe! If you spot any danger, or if those foul monsters are too much for you, don't hesitate to retreat back here.”

    - “OK, I'll try to find your missing people.” → [maevalia28](#d-maevalia28)

    <span id="d-maevalia19"></span>**`maevalia19`** Maevalia: “I'm also worried about Falothen, our weapons trainer. As I ran down the hills myself, I thought I heard him call for help.”

    - Next → [maevalia20](#d-maevalia20)

    <span id="d-maevalia_r2c"></span>**`maevalia_r2c`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 43 of [Destined for great things](../quests/charwood1.md#stage-43))* → [maevalia_r2d](#d-maevalia_r2d)
    - branch 2 → [maevalia_r3](#d-maevalia_r3)

    <span id="d-maevalia_r3b"></span>**`maevalia_r3b`** Maevalia: “Thank you for helping us.”


    <span id="d-maevalia_h9"></span>**`maevalia_h9`** Maevalia: “You are truly our hero. Thank you yet again.” — **effects:** sets stage 50 of [Trial by fire](../quests/charwood2.md#stage-50)


    <span id="d-maevalia_h10"></span>**`maevalia_h10`** Maevalia: “Certainly. Here is what we can spare. Thank you yet again.” — **effects:** sets stage 50 of [Trial by fire](../quests/charwood2.md#stage-50), gives [Gold coins](../items/gold.md)


    <span id="d-maevalia_h11"></span>**`maevalia_h11`** Maevalia: “After helping us, you still want to deprive us of more things that we cherish?”

    - Next → [maevalia_h12](#d-maevalia_h12)

    <span id="d-maevalia_d8"></span>**`maevalia_d8`** Maevalia: “Please try to be safe, and be on the lookout for the dangerous monsters that inhabit the mine.”

    - Next → [maevalia_d9](#d-maevalia_d9)

    <span id="d-maevalia_r10"></span>**`maevalia_r10`** Maevalia: “Good. We are truly grateful for the help that you have provided to us from the Charwood heights.” — **effects:** sets stage 115 of [Destined for great things](../quests/charwood1.md#stage-115)

    - Next → [maevalia_d1](#d-maevalia_d1)

    <span id="d-maevalia6"></span>**`maevalia6`** Maevalia: “They ransacked our whole mining camp. Even burnt down the wooden carving that Morenavia had created last year.”

    - “What did you do?” → [maevalia7](#d-maevalia7)

    <span id="d-maevalia28"></span>**`maevalia28`** Maevalia: “Thank you. The path up to Charwood heights is just east of here.” — **effects:** sets stage 30 of [Destined for great things](../quests/charwood1.md#stage-30)


    <span id="d-maevalia20"></span>**`maevalia20`** Maevalia: “There's also Ayell, our healer, and Fayvara, our armorer. They always stayed together, those two. We don't know what happened to them or where they are.” — **effects:** sets stage 21 of [Destined for great things](../quests/charwood1.md#stage-21)

    - “What are you going to do?” → [maevalia21s](#d-maevalia21s)
    - “As I said, I'll try to find out what happened to them.” *(if reached stage 30 of [Destined for great things](../quests/charwood1.md#stage-30))* → [maevalia28](#d-maevalia28)

    <span id="d-maevalia_r2d"></span>**`maevalia_r2d`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 44 of [Destined for great things](../quests/charwood1.md#stage-44))* → [maevalia_r4](#d-maevalia_r4)
    - branch 2 → [maevalia_r3](#d-maevalia_r3)

    <span id="d-maevalia_h12"></span>**`maevalia_h12`** Maevalia: “I guess we have no choice but to agree. Here, take these. They used to belong to my mother.” — **effects:** sets stage 50 of [Trial by fire](../quests/charwood2.md#stage-50), gives [Worn iron boots](../items/hboot_wirn.md), [Ring of surehit](../items/ring_atkch1.md)


    <span id="d-maevalia7"></span>**`maevalia7`** Maevalia: “We did the only thing we can, seeing as none of us were equipped to fight. We ran.”

    - Next → [maevalia8](#d-maevalia8)

    <span id="d-maevalia21s"></span>**`maevalia21s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Destined for great things](../quests/charwood1.md#stage-30))* → [maevalia21a](#d-maevalia21a)
    - branch 2 → [maevalia21](#d-maevalia21)

    <span id="d-maevalia_r4"></span>**`maevalia_r4`** Maevalia: “Yes, what about them? I saw that Falothen and Fayvara have returned.”

    - “Yes, Falothen and Fayvara were alive. Morenavia and Ayell had been killed by the monsters.” → [maevalia_r5](#d-maevalia_r5)

    <span id="d-maevalia8"></span>**`maevalia8`** Maevalia: “We ran down the mountain, leaving behind our mining settlement of Charwood. Some of us made it here to our former cabin.”

    - Next → [maevalia9](#d-maevalia9)

    <span id="d-maevalia21a"></span>**`maevalia21a`** Maevalia: “With your help, we might at least get somewhere.”

    - Next → [maevalia25](#d-maevalia25)

    <span id="d-maevalia21"></span>**`maevalia21`** Maevalia: “I honestly don't know. We've sent out runners to try to find help. So far, none have returned with help.”

    - “Maybe I can help?” → [maevalia23](#d-maevalia23)
    - “Tough luck. They're probably dead. You should move on with your lives.” → [maevalia22](#d-maevalia22)

    <span id="d-maevalia9"></span>**`maevalia9`** Maevalia: “The few of us that's left have been able to hold them off from here, at least for now.”

    - Next → [maevalia10](#d-maevalia10)

    <span id="d-maevalia23"></span>**`maevalia23`** Maevalia: “Well, I wouldn't want to be responsible for putting you into any trouble.”

    - “I can handle myself.” → [maevalia24](#d-maevalia24)
    - “I might be able to sneak by the monsters undetected.” → [maevalia24](#d-maevalia24)
    - “A few puny monsters won't stop me!” → [maevalia24](#d-maevalia24)

    <span id="d-maevalia22"></span>**`maevalia22`** Maevalia: “Yes, I guess so. Thank you for listening to our story.”


    <span id="d-maevalia10"></span>**`maevalia10`** Maevalia: “Our mining town up in the Charwood hills is completely overrun, however. All our belongings are back there.”

    - Next → [maevalia11](#d-maevalia11)

    <span id="d-maevalia24"></span>**`maevalia24`** Maevalia: “OK. Frankly, I don't know what else we can do. We really need the help.”

    - Next → [maevalia25](#d-maevalia25)

    <span id="d-maevalia11"></span>**`maevalia11`** Maevalia: “There are also several of us that haven't made it down the hill. Many of our friends and relatives from the mining town have not been accounted for yet.”

    - “What do you think has happened to them?” → [maevalia12](#d-maevalia12)

    <span id="d-maevalia12"></span>**`maevalia12`** Maevalia: “I don't want to think about that. Either they've been killed by the foul monsters, or worse.”

    - Next → [maevalia13](#d-maevalia13)

    <span id="d-maevalia13"></span>**`maevalia13`** Maevalia: “You know, we saw one monster carrying around what looked like a net of some sort, instead of weapons like the other ones.”

    - Next → [maevalia14](#d-maevalia14)

    <span id="d-maevalia14"></span>**`maevalia14`** Maevalia: “He shoved the other monsters around, and they all seemed to look up to him, like he was some sort of leader.”

    - Next → [maevalia15](#d-maevalia15)

    <span id="d-maevalia15"></span>**`maevalia15`** Maevalia: “I don't know what that net was for though. I wonder if he was supposed to capture some of us.” — **effects:** sets stage 20 of [Destined for great things](../quests/charwood1.md#stage-20)

    - “What now?” → [maevalia16](#d-maevalia16)
    - “As I said, I'll try to find out what happened to them.” *(if reached stage 30 of [Destined for great things](../quests/charwood1.md#stage-30))* → [maevalia28](#d-maevalia28)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 14 lines changed<br>· text: “Ok. Frankly, I don't know what else we can do. We really need the hel…” → “OK. Frankly, I don't know what else we can do. We really need the hel…”<br>· text: “The Charwood area has become a dangerous place as of late. You should…” → “The Charwood area has become a dangerous place as of late. You should…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `maevalia` |
    | Type (wiki) | NPC |
    | Spawn group | `maevalia` |
    | Loot table | – |
    | Conversation | `maevalia` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:18` |
    | Defined in | `res/raw/monsterlist_v070_npcs.json` |

    Raw data:

    ```json
    {
     "id": "maevalia",
     "name": "Maevalia",
     "iconID": "monsters_rltiles3:18",
     "phraseID": "maevalia"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maevalia.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maevalia.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maevalia.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maevalia.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
