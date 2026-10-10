---
description: "Falothen is a non-player character (NPC) in Andor's Trail, found in Charwood, Tradehouse 0a. Teaches One-handed sword proficiency, Two-handed sword proficiency, Axe proficiency, Blunt weapon proficiency, Dagger proficiency, Pole weapon proficiency, Unarmed fighting."
---

# ![](../assets/icons/monsters/monsters_tometik5_0.png){ .sprite } Falothen

**Where to find Falothen:** [Charwood, Minerhouse 0](#v-falothen0), [Tradehouse 0a](#v-falothen1)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik5_0.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Role** | Teaches [One-handed sword proficiency](../skills/weaponProficiency1hsword.md), [Two-handed sword proficiency](../skills/weaponProficiency2hsword.md), [Axe proficiency](../skills/weaponProficiencyAxe.md), [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md), [Dagger proficiency](../skills/weaponProficiencyDagger.md), [Pole weapon proficiency](../skills/weaponProficiencyPole.md), [Unarmed fighting](../skills/weaponProficiencyUnarmed.md) |
| **Found in** | Charwood, Tradehouse 0a |
| **Introduced** | v0.7.0 or earlier |

</div>

## Charwood, Minerhouse 0 { #v-falothen0 }

**Where:** Charwood: [Minerhouse 0](../maps/minerhouse0.md#pin-npc-falothen0)

### Quests

- [Destined for great things](../quests/charwood1.md): stage 41

### Dialogue simulator

Talk to Falothen as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/falothen0.json" data-npc="Falothen" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-falothen0-falothen0"></span>**`falothen0`** Falothen: “You there, thank the Shadow you're here! Quickly, untie these ropes!”

    - “[Untie the ropes]” → [falothen0_1](#d-falothen0-falothen0_1)
    - “I think I'll leave you right there.” → *conversation ends*

    <span id="d-falothen0-falothen0_1"></span>**`falothen0_1`** Falothen: “I'm free, thank you! I'll make my way down the hill to the Charwood cabin. Meet me back there.”

    - Next → [falothen0_2](#d-falothen0-falothen0_2)

    <span id="d-falothen0-falothen0_2"></span>**`falothen0_2`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 41 of [Destined for great things](../quests/charwood1.md#stage-41)

    - branch 1 → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Tradehouse 0a { #v-falothen1 }

**Where:** [Tradehouse 0a](../maps/tradehouse0a.md#pin-npc-falothen1) · **Role:** Teaches [One-handed sword proficiency](../skills/weaponProficiency1hsword.md), [Two-handed sword proficiency](../skills/weaponProficiency2hsword.md), [Axe proficiency](../skills/weaponProficiencyAxe.md), [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md), [Dagger proficiency](../skills/weaponProficiencyDagger.md), [Pole weapon proficiency](../skills/weaponProficiencyPole.md), [Unarmed fighting](../skills/weaponProficiencyUnarmed.md)

### Quests

- [Destined for great things](../quests/charwood1.md): stages 65, 70, 71, 72, 73, 74, 75, 76, 80, 110

### Dialogue simulator

Talk to Falothen as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/falothen1.json" data-npc="Falothen" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (72 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-falothen1-falothen1"></span>**`falothen1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70))* → [falothen1_0](#d-falothen1-falothen1_0)
    - branch 2 *(if reached stage 71 of [Destined for great things](../quests/charwood1.md#stage-71))* → [falothen1_0](#d-falothen1-falothen1_0)
    - branch 3 *(if reached stage 72 of [Destined for great things](../quests/charwood1.md#stage-72))* → [falothen1_0](#d-falothen1-falothen1_0)
    - branch 4 *(if reached stage 73 of [Destined for great things](../quests/charwood1.md#stage-73))* → [falothen1_0](#d-falothen1-falothen1_0)
    - branch 5 *(if reached stage 74 of [Destined for great things](../quests/charwood1.md#stage-74))* → [falothen1_0](#d-falothen1-falothen1_0)
    - branch 6 *(if reached stage 75 of [Destined for great things](../quests/charwood1.md#stage-75))* → [falothen1_0](#d-falothen1-falothen1_0)
    - branch 7 *(if reached stage 76 of [Destined for great things](../quests/charwood1.md#stage-76))* → [falothen1_0](#d-falothen1-falothen1_0)
    - branch 8 → [falothen1_1](#d-falothen1-falothen1_1)

    <span id="d-falothen1-falothen1_0"></span>**`falothen1_0`** Falothen: “Hello again, my friend. I hope you've been using what I taught you.”

    - Next → [falothen1_s](#d-falothen1-falothen1_s)

    <span id="d-falothen1-falothen1_1"></span>**`falothen1_1`** Falothen: “Hello again. Thank you for saving me from captivity up in the Charwood heights!”

    - Next → [falothen1_2](#d-falothen1-falothen1_2)

    <span id="d-falothen1-falothen1_s"></span>**`falothen1_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 91 of [Destined for great things](../quests/charwood1.md#stage-91))* → [falothen1_s0](#d-falothen1-falothen1_s0)
    - branch 2 → [falothen1_s1](#d-falothen1-falothen1_s1)

    <span id="d-falothen1-falothen1_2"></span>**`falothen1_2`** Falothen: “I won't dare to think about what those monsters would have done to me, had you not freed me!”

    - Next → [falothen1_3](#d-falothen1-falothen1_3)

    <span id="d-falothen1-falothen1_s0"></span>**`falothen1_s0`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 110 of [Destined for great things](../quests/charwood1.md#stage-110)

    - branch 1 → [falothen1_9](#d-falothen1-falothen1_9)

    <span id="d-falothen1-falothen1_s1"></span>**`falothen1_s1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 92 of [Destined for great things](../quests/charwood1.md#stage-92))* → [falothen1_s0](#d-falothen1-falothen1_s0)
    - branch 2 → [falothen1_s2](#d-falothen1-falothen1_s2)

    <span id="d-falothen1-falothen1_3"></span>**`falothen1_3`** Falothen: “In return, I am willing to teach you the things I know. I used to be a weapons trainer for the Charwood heights, before all of this started.”

    - “What can you teach me?” → [falothen1_4](#d-falothen1-falothen1_4)

    <span id="d-falothen1-falothen1_9"></span>**`falothen1_9`** Falothen: “I can help you get better in the other types of weapons as well, of course, if you want. But for that, I will have to require some form of payment.”

    - “What sort of payment?” → [falothen1_10](#d-falothen1-falothen1_10)

    <span id="d-falothen1-falothen1_s2"></span>**`falothen1_s2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 93 of [Destined for great things](../quests/charwood1.md#stage-93))* → [falothen1_s0](#d-falothen1-falothen1_s0)
    - branch 2 → [falothen1_s3](#d-falothen1-falothen1_s3)

    <span id="d-falothen1-falothen1_4"></span>**`falothen1_4`** Falothen: “I can teach you how to better handle most types of weapons, so that you can get even more proficient in them.”

    - “What weapon types can you teach me?” → [falothen1_5](#d-falothen1-falothen1_5)

    <span id="d-falothen1-falothen1_10"></span>**`falothen1_10`** Falothen: “We usually don't teach anyone outside our settlement. Last time I did, I was given five Oegyth crystals and 5,000 gold in return for my services.”

    - Next → [falothen1_11](#d-falothen1-falothen1_11)

    <span id="d-falothen1-falothen1_s3"></span>**`falothen1_s3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 94 of [Destined for great things](../quests/charwood1.md#stage-94))* → [falothen1_s0](#d-falothen1-falothen1_s0)
    - branch 2 → [falothen1_9](#d-falothen1-falothen1_9)

    <span id="d-falothen1-falothen1_5"></span>**`falothen1_5`** Falothen: “I can teach you about swords, either one-handed or two-handed ones. I know a bit about daggers, axes, polearms, and blunt weapons. I also know a fair deal about fighting with your bare fists.”

    - Next → [falothen1_6](#d-falothen1-falothen1_6)

    <span id="d-falothen1-falothen1_11"></span>**`falothen1_11`** Falothen: “Seeing as you saved me, I think it's reasonable to only require two of those crystals from you. I still have expenses to pay, mind you, so I will require that gold.” — **effects:** sets stage 80 of [Destined for great things](../quests/charwood1.md#stage-80)

    - “I don't have that on me right now. I'll be back.” → *conversation ends*
    - “I'm not interested right now.” → *conversation ends*
    - “I think I should hold on to those crystals some more.” *(if carry 2× [Oegyth crystal](../items/oegyth.md))* → [falothen1_12](#d-falothen1-falothen1_12)
    - “I might be interested.” *(if carry 2× [Oegyth crystal](../items/oegyth.md))* → [falothen1_13](#d-falothen1-falothen1_13)

    <span id="d-falothen1-falothen1_6"></span>**`falothen1_6`** Falothen: “I only have time to teach you about one type of weapon, so make sure you pick the one that suits you best.” — **effects:** sets stage 65 of [Destined for great things](../quests/charwood1.md#stage-65)

    - “Tell me more about fighting with your bare fists.” → [falothen1_7_f](#d-falothen1-falothen1_7_f)
    - “Tell me more about two-handed swords.” → [falothen1_7_2hs](#d-falothen1-falothen1_7_2hs)
    - “Tell me more about one-handed swords.” → [falothen1_7_1hs](#d-falothen1-falothen1_7_1hs)
    - “Tell me more about daggers.” → [falothen1_7_d](#d-falothen1-falothen1_7_d)
    - “Tell me more about axes.” → [falothen1_7_a](#d-falothen1-falothen1_7_a)
    - “Tell me more about blunt weapons.” → [falothen1_7_b](#d-falothen1-falothen1_7_b)
    - “Tell me more about polearms.” → [falothen1_7_pa](#d-falothen1-falothen1_7_pa)
    - “I'll be right back.” → *conversation ends*

    <span id="d-falothen1-falothen1_12"></span>**`falothen1_12`** Falothen: “Yes, those things sure are valuable.”


    <span id="d-falothen1-falothen1_13"></span>**`falothen1_13`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if have 5,000 gold)* → [falothen1_14](#d-falothen1-falothen1_14)
    - branch 2 → [falothen1_13q](#d-falothen1-falothen1_13q)

    <span id="d-falothen1-falothen1_7_f"></span>**`falothen1_7_f`** Falothen: “Unarmed, now that's my kind of style! When not being hampered by either a weapon or shield, you can be a lot more flexible in your moves.”

    - Next → [falothen1_7_f1](#d-falothen1-falothen1_7_f1)

    <span id="d-falothen1-falothen1_7_2hs"></span>**`falothen1_7_2hs`** Falothen: “Two handed swords are usually much heavier than their one-handed counterparts, which means that they are much harder to swing correctly.”

    - Next → [falothen1_7_2hs1](#d-falothen1-falothen1_7_2hs1)

    <span id="d-falothen1-falothen1_7_1hs"></span>**`falothen1_7_1hs`** Falothen: “One handed swords, now that's an art form. They have a wide range of uses, from slashing to piercing types.”

    - Next → [falothen1_7_1hs1](#d-falothen1-falothen1_7_1hs1)

    <span id="d-falothen1-falothen1_7_d"></span>**`falothen1_7_d`** Falothen: “Daggers, the choice of the fast fighter. Their light weight usually makes you much faster when attacking. Some of them also have nasty side effects. Nasty for your opponent, that is.”

    - Next → [falothen1_7_d1](#d-falothen1-falothen1_7_d1)

    <span id="d-falothen1-falothen1_7_a"></span>**`falothen1_7_a`** Falothen: “Oh yes. The mighty axes. You can do a lot of damage with them, if you know how to handle them correctly.”

    - Next → [falothen1_7_a1](#d-falothen1-falothen1_7_a1)

    <span id="d-falothen1-falothen1_7_b"></span>**`falothen1_7_b`** Falothen: “Now, blunt weapons is my way of categorizing everything from the simple club, to maces up to quarterstaves, and even whips. The technique for using them well is mostly the same, although whips are obviously somewhat different.”

    - Next → [falothen1_7_b1](#d-falothen1-falothen1_7_b1)

    <span id="d-falothen1-falothen1_7_pa"></span>**`falothen1_7_pa`** Falothen: “Polearms are a spike or a blade, or both, on the end of a long pole. Wielding one with one hand is not practical, but they make up for that with their defensive capabilities.”

    - Next → [falothan1_7_pa1](#d-falothen1-falothan1_7_pa1)

    <span id="d-falothen1-falothen1_14"></span>**`falothen1_14`** Falothen: “Which weapon type would you be interested in?”

    - “Tell me more about fighting with your bare fists.” → [falothen1_2nd_f](#d-falothen1-falothen1_2nd_f)
    - “Tell me more about two-handed swords.” → [falothen1_2nd_2hs](#d-falothen1-falothen1_2nd_2hs)
    - “Tell me more about one-handed swords.” → [falothen1_2nd_1hs](#d-falothen1-falothen1_2nd_1hs)
    - “Tell me more about daggers.” → [falothen1_2nd_d](#d-falothen1-falothen1_2nd_d)
    - “Tell me more about axes.” → [falothen1_2nd_a](#d-falothen1-falothen1_2nd_a)
    - “Tell me more about blunt weapons.” → [falothen1_2nd_b](#d-falothen1-falothen1_2nd_b)
    - “Tell me more about polearms.” → [falothen1_2nd_pa](#d-falothen1-falothen1_2nd_pa)
    - “I'll be right back.” → *conversation ends*

    <span id="d-falothen1-falothen1_13q"></span>**`falothen1_13q`** Falothen: “It seems you do not have the gold required for it.”


    <span id="d-falothen1-falothen1_7_f1"></span>**`falothen1_7_f1`** Falothen: “Fighting unarmed can make you land more successful punches, and will also make you quicker when dodging blows.”

    - “Sounds good. Teach me how to be better at unarmed fighting.” → [falothen1_7_f2](#d-falothen1-falothen1_7_f2)
    - “Let's go back to the other types of weapons.” → [falothen1_6](#d-falothen1-falothen1_6)

    <span id="d-falothen1-falothen1_7_2hs1"></span>**`falothen1_7_2hs1`** Falothen: “In return, they provide much deeper cuts that hurt your opponent more. I can teach you how to better handle swinging your two-handed swords.”

    - “Sounds good. Teach me two-handed sword fighting.” → [falothen1_7_2hs2](#d-falothen1-falothen1_7_2hs2)
    - “Let's go back to the other types of weapons.” → [falothen1_6](#d-falothen1-falothen1_6)

    <span id="d-falothen1-falothen1_7_1hs1"></span>**`falothen1_7_1hs1`** Falothen: “I can teach you how to handle them better, so that you land your attacks more often.”

    - “Sounds good. Teach me how to fight with one-handed swords.” → [falothen1_7_1hs2](#d-falothen1-falothen1_7_1hs2)
    - “Let's go back to the other types of weapons.” → [falothen1_6](#d-falothen1-falothen1_6)

    <span id="d-falothen1-falothen1_7_d1"></span>**`falothen1_7_d1`** Falothen: “I can teach you how to handle them better, so that you land your attacks more often.”

    - “Sounds good. Teach me how to fight with daggers.” → [falothen1_7_d2](#d-falothen1-falothen1_7_d2)
    - “Let's go back to the other types of weapons.” → [falothen1_6](#d-falothen1-falothen1_6)

    <span id="d-falothen1-falothen1_7_a1"></span>**`falothen1_7_a1`** Falothen: “I can teach you how to get better at fighting with all types of axes, from the small hatchet up to the larger two-handed greataxes. Even a scythe, although not designed for combat, can do a lot of damage if you know how to use it. That…”

    - “Sounds good. Teach me how to fight with axes.” → [falothen1_7_a2](#d-falothen1-falothen1_7_a2)
    - “Let's go back to the other types of weapons.” → [falothen1_6](#d-falothen1-falothen1_6)

    <span id="d-falothen1-falothen1_7_b1"></span>**`falothen1_7_b1`** Falothen: “I can teach you how to better land your blows with all blunt weapons.”

    - “Sounds good. Teach me how to fight with blunt weapons.” → [falothen1_7_b2](#d-falothen1-falothen1_7_b2)
    - “Let's go back to the other types of weapons.” → [falothen1_6](#d-falothen1-falothen1_6)

    <span id="d-falothen1-falothan1_7_pa1"></span>**`falothan1_7_pa1`** Falothen: “You can attack your foe from a great distance with a polearm, making it difficult for your foe to attack you.”

    - “Let's go back to the other types of weapons.” → [falothen1_6](#d-falothen1-falothen1_6)
    - “Sounds good. Teach me how to fight with polearms.” → [falothen_1_pa2](#d-falothen1-falothen_1_pa2)

    <span id="d-falothen1-falothen1_2nd_f"></span>**`falothen1_2nd_f`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 75 of [Destined for great things](../quests/charwood1.md#stage-75))* → [falothen1_2nd_no](#d-falothen1-falothen1_2nd_no)
    - branch 2 → [falothen1_2nd_f0](#d-falothen1-falothen1_2nd_f0)

    <span id="d-falothen1-falothen1_2nd_2hs"></span>**`falothen1_2nd_2hs`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 71 of [Destined for great things](../quests/charwood1.md#stage-71))* → [falothen1_2nd_no](#d-falothen1-falothen1_2nd_no)
    - branch 2 → [falothen1_2nd_2hs0](#d-falothen1-falothen1_2nd_2hs0)

    <span id="d-falothen1-falothen1_2nd_1hs"></span>**`falothen1_2nd_1hs`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 70 of [Destined for great things](../quests/charwood1.md#stage-70))* → [falothen1_2nd_no](#d-falothen1-falothen1_2nd_no)
    - branch 2 → [falothen1_2nd_1hs0](#d-falothen1-falothen1_2nd_1hs0)

    <span id="d-falothen1-falothen1_2nd_d"></span>**`falothen1_2nd_d`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 72 of [Destined for great things](../quests/charwood1.md#stage-72))* → [falothen1_2nd_no](#d-falothen1-falothen1_2nd_no)
    - branch 2 → [falothen1_2nd_d0](#d-falothen1-falothen1_2nd_d0)

    <span id="d-falothen1-falothen1_2nd_a"></span>**`falothen1_2nd_a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 74 of [Destined for great things](../quests/charwood1.md#stage-74))* → [falothen1_2nd_no](#d-falothen1-falothen1_2nd_no)
    - branch 2 → [falothen1_2nd_a0](#d-falothen1-falothen1_2nd_a0)

    <span id="d-falothen1-falothen1_2nd_b"></span>**`falothen1_2nd_b`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 73 of [Destined for great things](../quests/charwood1.md#stage-73))* → [falothen1_2nd_no](#d-falothen1-falothen1_2nd_no)
    - branch 2 → [falothen1_2nd_b0](#d-falothen1-falothen1_2nd_b0)

    <span id="d-falothen1-falothen1_2nd_pa"></span>**`falothen1_2nd_pa`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 76 of [Destined for great things](../quests/charwood1.md#stage-76))* → [falothen1_2nd_no](#d-falothen1-falothen1_2nd_no)
    - branch 2 → [falothen1_2nd_pa0](#d-falothen1-falothen1_2nd_pa0)

    <span id="d-falothen1-falothen1_7_f2"></span>**`falothen1_7_f2`** Falothen: “[Falothen teaches you the unarmed fighting skill]” — **effects:** sets stage 75 of [Destined for great things](../quests/charwood1.md#stage-75), +1 [Unarmed fighting](../skills/weaponProficiencyUnarmed.md)

    - Next → [falothen1_8](#d-falothen1-falothen1_8)

    <span id="d-falothen1-falothen1_7_2hs2"></span>**`falothen1_7_2hs2`** Falothen: “[Falothen teaches you the two-handed sword skill]” — **effects:** sets stage 71 of [Destined for great things](../quests/charwood1.md#stage-71), +1 [Two-handed sword proficiency](../skills/weaponProficiency2hsword.md)

    - Next → [falothen1_8](#d-falothen1-falothen1_8)

    <span id="d-falothen1-falothen1_7_1hs2"></span>**`falothen1_7_1hs2`** Falothen: “[Falothen teaches you the one-handed sword skill]” — **effects:** sets stage 70 of [Destined for great things](../quests/charwood1.md#stage-70), +1 [One-handed sword proficiency](../skills/weaponProficiency1hsword.md)

    - Next → [falothen1_8](#d-falothen1-falothen1_8)

    <span id="d-falothen1-falothen1_7_d2"></span>**`falothen1_7_d2`** Falothen: “[Falothen teaches you the dagger skill]” — **effects:** sets stage 72 of [Destined for great things](../quests/charwood1.md#stage-72), +1 [Dagger proficiency](../skills/weaponProficiencyDagger.md)

    - Next → [falothen1_8](#d-falothen1-falothen1_8)

    <span id="d-falothen1-falothen1_7_a2"></span>**`falothen1_7_a2`** Falothen: “[Falothen teaches you the axe skill]” — **effects:** sets stage 74 of [Destined for great things](../quests/charwood1.md#stage-74), +1 [Axe proficiency](../skills/weaponProficiencyAxe.md)

    - Next → [falothen1_8](#d-falothen1-falothen1_8)

    <span id="d-falothen1-falothen1_7_b2"></span>**`falothen1_7_b2`** Falothen: “[Falothen teaches you the blunt weapons skill]” — **effects:** sets stage 73 of [Destined for great things](../quests/charwood1.md#stage-73), +1 [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md)

    - Next → [falothen1_8](#d-falothen1-falothen1_8)

    <span id="d-falothen1-falothen_1_pa2"></span>**`falothen_1_pa2`** Falothen: “[Falothen teaches you the polearm skill]” — **effects:** sets stage 76 of [Destined for great things](../quests/charwood1.md#stage-76), +1 [Pole weapon proficiency](../skills/weaponProficiencyPole.md)

    - Next → [falothen1_8](#d-falothen1-falothen1_8)

    <span id="d-falothen1-falothen1_2nd_no"></span>**`falothen1_2nd_no`** Falothen: “I've already taught you that skill.”

    - “Let's go back to the other types of weapons.” → [falothen1_14](#d-falothen1-falothen1_14)

    <span id="d-falothen1-falothen1_2nd_f0"></span>**`falothen1_2nd_f0`** Falothen: “Unarmed, now that's my kind of style! When not being hampered by either a weapon or shield, you can be a lot more flexible in your moves.”

    - Next → [falothen1_2nd_f1](#d-falothen1-falothen1_2nd_f1)

    <span id="d-falothen1-falothen1_2nd_2hs0"></span>**`falothen1_2nd_2hs0`** Falothen: “Two handed swords are usually much heavier than their one-handed counterparts, which means that they are much harder to swing correctly.”

    - Next → [falothen1_2nd_2hs1](#d-falothen1-falothen1_2nd_2hs1)

    <span id="d-falothen1-falothen1_2nd_1hs0"></span>**`falothen1_2nd_1hs0`** Falothen: “One handed swords, now that's an art form. They have a wide range of uses, from slashing to piercing types.”

    - Next → [falothen1_2nd_1hs1](#d-falothen1-falothen1_2nd_1hs1)

    <span id="d-falothen1-falothen1_2nd_d0"></span>**`falothen1_2nd_d0`** Falothen: “Daggers, the choice of the fast fighter. Their light weight usually makes you much faster when attacking. Some of them also have nasty side effects. Nasty for your opponent, that is.”

    - Next → [falothen1_2nd_d1](#d-falothen1-falothen1_2nd_d1)

    <span id="d-falothen1-falothen1_2nd_a0"></span>**`falothen1_2nd_a0`** Falothen: “Oh yes. The mighty axes. You can do a lot of damage with them, if you know how to handle them correctly.”

    - Next → [falothen1_2nd_a1](#d-falothen1-falothen1_2nd_a1)

    <span id="d-falothen1-falothen1_2nd_b0"></span>**`falothen1_2nd_b0`** Falothen: “Now, blunt weapons is my way of categorizing everything from the simple club, to maces up to quarterstaves. The technique for using them well is mostly the same.”

    - Next → [falothen1_2nd_b1](#d-falothen1-falothen1_2nd_b1)

    <span id="d-falothen1-falothen1_2nd_pa0"></span>**`falothen1_2nd_pa0`** Falothen: “Polearms are a spike or a blade, or both, on the end of a long pole. Wielding one with one hand is not practical, but they make up for that with their defensive capabilities.”

    - Next → [falothen1_2nd_pa1](#d-falothen1-falothen1_2nd_pa1)

    <span id="d-falothen1-falothen1_8"></span>**`falothen1_8`** Falothen: “There. That wasn't so hard once you get the hang of it, now was it?”

    - Next → [falothen1_s](#d-falothen1-falothen1_s)

    <span id="d-falothen1-falothen1_2nd_f1"></span>**`falothen1_2nd_f1`** Falothen: “Fighting unarmed can make you land more successful punches, and will also make you quicker when dodging blows.”

    - “Sounds good. Teach me how to be better at unarmed fighting. Here are two Oegyth crystals and 5,000 gold as payment.” *(if hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold)* → [falothen1_2nd_f3](#d-falothen1-falothen1_2nd_f3)
    - “Let's go back to the other types of weapons.” → [falothen1_14](#d-falothen1-falothen1_14)

    <span id="d-falothen1-falothen1_2nd_2hs1"></span>**`falothen1_2nd_2hs1`** Falothen: “In return, they provide much deeper cuts that hurt your opponent more. I can teach you how to better handle swinging your two-handed swords.”

    - “Sounds good. Teach me two-handed sword fighting. Here are two Oegyth crystals and 5,000 gold as payment.” *(if hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold)* → [falothen1_2nd_2hs3](#d-falothen1-falothen1_2nd_2hs3)
    - “Let's go back to the other types of weapons.” → [falothen1_14](#d-falothen1-falothen1_14)

    <span id="d-falothen1-falothen1_2nd_1hs1"></span>**`falothen1_2nd_1hs1`** Falothen: “I can teach you how to handle them better, so that you land your attacks more often.”

    - “Sounds good. Teach me how to fight with one-handed swords. Here are two Oegyth crystals and 5,000 gold as payment.” *(if hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold)* → [falothen1_2nd_1hs3](#d-falothen1-falothen1_2nd_1hs3)
    - “Let's go back to the other types of weapons.” → [falothen1_14](#d-falothen1-falothen1_14)

    <span id="d-falothen1-falothen1_2nd_d1"></span>**`falothen1_2nd_d1`** Falothen: “I can teach you how to handle them better, so that you land your attacks more often.”

    - “Sounds good. Teach me how to fight with daggers. Here are two Oegyth crystals and 5,000 gold as payment.” *(if hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold)* → [falothen1_2nd_d3](#d-falothen1-falothen1_2nd_d3)
    - “Let's go back to the other types of weapons.” → [falothen1_14](#d-falothen1-falothen1_14)

    <span id="d-falothen1-falothen1_2nd_a1"></span>**`falothen1_2nd_a1`** Falothen: “I can teach you how to get better at fighting with all types of axes, from the small hatchet up to the larger two-handed greataxes. That way, you can be very versatile in your choice of weapons.”

    - “Sounds good. Teach me how to fight with axes. Here are two Oegyth crystals and 5,000 gold as payment.” *(if hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold)* → [falothen1_2nd_a3](#d-falothen1-falothen1_2nd_a3)
    - “Let's go back to the other types of weapons.” → [falothen1_14](#d-falothen1-falothen1_14)

    <span id="d-falothen1-falothen1_2nd_b1"></span>**`falothen1_2nd_b1`** Falothen: “I can teach you how to better land your blows with all blunt weapons.”

    - “Sounds good. Teach me how to fight with blunt weapons. Here are two Oegyth crystals and 5,000 gold as payment.” *(if hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold)* → [falothen1_2nd_b3](#d-falothen1-falothen1_2nd_b3)
    - “Let's go back to the other types of weapons.” → [falothen1_14](#d-falothen1-falothen1_14)

    <span id="d-falothen1-falothen1_2nd_pa1"></span>**`falothen1_2nd_pa1`** Falothen: “You can attack your foe from a great distance with a polearm, making it difficult for your foe to attack you.”

    - “Sounds good. Teach me how to better fight with polearms. Here are two Oegyth crystals and 5,000 gold as payment.” *(if hand over 2× [Oegyth crystal](../items/oegyth.md); pay 5,000 gold)* → [falothen1_2nd_pa3](#d-falothen1-falothen1_2nd_pa3)
    - “Let's go back to the other types of weapons.” → [falothen1_14](#d-falothen1-falothen1_14)

    <span id="d-falothen1-falothen1_2nd_f3"></span>**`falothen1_2nd_f3`** Falothen: “[Falothen teaches you the unarmed fighting skill]” — **effects:** sets stage 75 of [Destined for great things](../quests/charwood1.md#stage-75), +1 [Unarmed fighting](../skills/weaponProficiencyUnarmed.md)

    - Next → [falothen1_15](#d-falothen1-falothen1_15)

    <span id="d-falothen1-falothen1_2nd_2hs3"></span>**`falothen1_2nd_2hs3`** Falothen: “[Falothen teaches you the two-handed sword skill]” — **effects:** sets stage 71 of [Destined for great things](../quests/charwood1.md#stage-71), +1 [Two-handed sword proficiency](../skills/weaponProficiency2hsword.md)

    - Next → [falothen1_15](#d-falothen1-falothen1_15)

    <span id="d-falothen1-falothen1_2nd_1hs3"></span>**`falothen1_2nd_1hs3`** Falothen: “[Falothen teaches you the one-handed sword skill]” — **effects:** sets stage 70 of [Destined for great things](../quests/charwood1.md#stage-70), +1 [One-handed sword proficiency](../skills/weaponProficiency1hsword.md)

    - Next → [falothen1_15](#d-falothen1-falothen1_15)

    <span id="d-falothen1-falothen1_2nd_d3"></span>**`falothen1_2nd_d3`** Falothen: “[Falothen teaches you the dagger skill]” — **effects:** sets stage 72 of [Destined for great things](../quests/charwood1.md#stage-72), +1 [Dagger proficiency](../skills/weaponProficiencyDagger.md)

    - Next → [falothen1_15](#d-falothen1-falothen1_15)

    <span id="d-falothen1-falothen1_2nd_a3"></span>**`falothen1_2nd_a3`** Falothen: “[Falothen teaches you the axe skill]” — **effects:** sets stage 74 of [Destined for great things](../quests/charwood1.md#stage-74), +1 [Axe proficiency](../skills/weaponProficiencyAxe.md)

    - Next → [falothen1_15](#d-falothen1-falothen1_15)

    <span id="d-falothen1-falothen1_2nd_b3"></span>**`falothen1_2nd_b3`** Falothen: “[Falothen teaches you the blunt weapons skill]” — **effects:** sets stage 73 of [Destined for great things](../quests/charwood1.md#stage-73), +1 [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md)

    - Next → [falothen1_15](#d-falothen1-falothen1_15)

    <span id="d-falothen1-falothen1_2nd_pa3"></span>**`falothen1_2nd_pa3`** Falothen: “[Falothen teaches you the polearm skill]” — **effects:** sets stage 76 of [Destined for great things](../quests/charwood1.md#stage-76), +1 [Pole weapon proficiency](../skills/weaponProficiencyPole.md)

    - Next → [falothen1_15](#d-falothen1-falothen1_15)

    <span id="d-falothen1-falothen1_15"></span>**`falothen1_15`** Falothen: “Well done! You learn quickly.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 11 lines changed |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 2 lines changed<br>· text: “I can teach you how to get better at fighting with all types of axes,…” → “I can teach you how to get better at fighting with all types of axes,…”<br>· text: “Now, blunt weapons is my way of categorizing everything from the simp…” → “Now, blunt weapons is my way of categorizing everything from the simp…” |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 7 lines added, 4 lines changed<br>· text: “I can teach you about swords, either one-handed or two-handed ones. I…” → “I can teach you about swords, either one-handed or two-handed ones. I…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 8 lines changed<br>· text: “We usually don't teach anyone outside our settlement. Last time I did…” → “We usually don't teach anyone outside our settlement. Last time I did…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Falothen. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location.

| Entry | Type | Section |
|---|---|---|
| `falothen0` | NPC | [Charwood, Minerhouse 0](#v-falothen0) |
| `falothen1` | NPC | [Tradehouse 0a](#v-falothen1) |

??? info "Technical information: falothen0"

    | | |
    |---|---|
    | Entry ID | `falothen0` |
    | Type (wiki) | NPC |
    | Spawn group | `falothen0` |
    | Loot table | – |
    | Conversation | `falothen0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik5:0` |
    | Defined in | `res/raw/monsterlist_v070_npcs.json` |

    Raw data:

    ```json
    {
     "id": "falothen0",
     "name": "Falothen",
     "iconID": "monsters_tometik5:0",
     "unique": 1,
     "phraseID": "falothen0"
    }
    ```

??? info "Technical information: falothen1"

    | | |
    |---|---|
    | Entry ID | `falothen1` |
    | Type (wiki) | NPC |
    | Spawn group | `falothen1` |
    | Loot table | – |
    | Conversation | `falothen1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik5:0` |
    | Defined in | `res/raw/monsterlist_v070_npcs.json` |

    Raw data:

    ```json
    {
     "id": "falothen1",
     "name": "Falothen",
     "iconID": "monsters_tometik5:0",
     "phraseID": "falothen1"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=falothen0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=falothen0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=falothen0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=falothen0.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
