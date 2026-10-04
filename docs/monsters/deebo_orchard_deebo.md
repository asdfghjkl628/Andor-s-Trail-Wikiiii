# ![](../assets/icons/monsters/monsters_tometik2_39.png){ .sprite } Deebo

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 10 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Orchard apple](../items/deebo_apples.md) | 100% | 2 to 5 |
| [Deebo's apple juice](../items/apple_orchard_juice.md) | 100% | 3 to 7 |
| [Deebo's apple cider](../items/apple_orchard_cider.md) | 100% | 2 to 4 |
| [Deebo's apple pie](../items/apple_orchard_pie.md) | 100% | 3 to 6 |

## Found on

- [sullengard_apple_farm_east](../maps/sullengard_apple_farm_east.md)

## Quests

- [Bread and circus](../quests/brightport_bakery.md): stages 30, 45
- [Hunting the hunter](../quests/deebo_orchard_hth.md): stages 0, 10, 50
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 205
- [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md): stages 4

??? quote "Dialogue (34 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-deebo_orchard_deebo_0"></span>**`deebo_orchard_deebo_0`** Deebo: “What a lovely day for some good quality hard work outside.”

    - “It sounds like you love being outside.” *(if NOT reached stage 50 of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-50))* → [deebo_orchard_deebo_10](#d-deebo_orchard_deebo_10)
    - “Your horses are magnificent.” → [deebo_orchard_deebo_horse_talk_10](#d-deebo_orchard_deebo_horse_talk_10)
    - “Can I get a new batch of apples for the bakery?” *(if reached stage 205 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-205); NOT reached stage 50 of [Bread and circus](../quests/brightport_bakery.md#stage-50); NOT reached stage 40 of [Bread and circus](../quests/brightport_bakery.md#stage-40))* → [brightport_deebo_selector](#d-brightport_deebo_selector)
    - “Hello. Eatloni from Brightport sent me to ask about the apples.” *(if reached stage 25 of [Bread and circus](../quests/brightport_bakery.md#stage-25); NOT reached stage 205 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-205))* → [brightport_deebo](#d-brightport_deebo)
    - “I will let you get back to your business. Have a great time enjoying the nice weather.” → *conversation ends*
    - “Can I see what you have to trade?” *(if reached stage 50 of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-50))* → *shop opens*

    <span id="d-deebo_orchard_deebo_10"></span>**`deebo_orchard_deebo_10`** Deebo: “I do indeed. But I'll tell you what I really don't enjoy: fixing the property damage done to my farm and losing livestock because of some wild predator!”

    - “A "predator"? What kind of a predator?” → [deebo_orchard_deebo_20](#d-deebo_orchard_deebo_20)
    - “I have killed the Golden jackal and I have the requested proof.” *(if hand over 1× [Golden jackal fur](../items/golden_jackal_fur.md); latest stage of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-40) is 40)* → [deebo_orchard_deebo_90](#d-deebo_orchard_deebo_90)
    - “I have killed the Golden jackal, but I can not prove it.” *(if latest stage of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-40) is 40; carry 0× [Golden jackal fur](../items/golden_jackal_fur.md))* → [deebo_orchard_deebo_85](#d-deebo_orchard_deebo_85)

    <span id="d-deebo_orchard_deebo_horse_talk_10"></span>**`deebo_orchard_deebo_horse_talk_10`** Deebo: “Oh, thank you so much. I am so proud of them.”

    - “You should be. Can I ride one?” → [deebo_orchard_deebo_horse_talk_20](#d-deebo_orchard_deebo_horse_talk_20)

    <span id="d-brightport_deebo_selector"></span>**`brightport_deebo_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 30 of [Bread and circus](../quests/brightport_bakery.md#stage-30); NOT reached stage 45 of [Bread and circus](../quests/brightport_bakery.md#stage-45))* → [brightport_deebo0](#d-brightport_deebo0)
    - Next *(if reached stage 45 of [Bread and circus](../quests/brightport_bakery.md#stage-45))* → [brightport_deebo5](#d-brightport_deebo5)

    <span id="d-brightport_deebo"></span>**`brightport_deebo`** Deebo: “You came for naught. The apples were picked up recently. Should be on their way, if not already delivered.” — **effects:** sets stage 30 of [Bread and circus](../quests/brightport_bakery.md#stage-30)

    - “Well, they were supposed to arrive, but didn't.” → [brightport_deebo1](#d-brightport_deebo1)

    <span id="d-deebo_orchard_deebo_20"></span>**`deebo_orchard_deebo_20`** Deebo: “Have you seen that Golden jackal around here?”

    - “What is a Golden jackal?” → [deebo_orchard_deebo_30](#d-deebo_orchard_deebo_30)
    - “No, sir, I have not. Well, at least I don't think I have.” → [deebo_orchard_deebo_30](#d-deebo_orchard_deebo_30)
    - “I want to hunt down and kill that Golden jackal for you.” *(if latest stage of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-0) is 0)* → [deebo_orchard_deebo_50](#d-deebo_orchard_deebo_50)

    <span id="d-deebo_orchard_deebo_90"></span>**`deebo_orchard_deebo_90`** Deebo: “Wonderful. Let me have it. [You hand over the Golden jackal's fur] Ah yes, this is indeed proof it is dead.” — **effects:** gives 1× [Golden jackal fur](../items/golden_jackal_fur.md), sets stage 50 of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-50)

    - Next → [deebo_orchard_deebo_100](#d-deebo_orchard_deebo_100)

    <span id="d-deebo_orchard_deebo_85"></span>**`deebo_orchard_deebo_85`** Deebo: “Return to me once you have the proof that it is dead.”


    <span id="d-deebo_orchard_deebo_horse_talk_20"></span>**`deebo_orchard_deebo_horse_talk_20`** Deebo: “WHAT?! No way that's going to happen.”

    - “Please.” → [deebo_orchard_deebo_horse_talk_30](#d-deebo_orchard_deebo_horse_talk_30)
    - “Fine. But can we talk about your barn instead?” → [deebo_orchard_deebo_barn_talk_10](#d-deebo_orchard_deebo_barn_talk_10)

    <span id="d-brightport_deebo0"></span>**`brightport_deebo0`** Deebo: “I don't sell my harvest to just anyone, but because I have a contract with the bakery I can give you a batch.”

    - “Sounds good.” → [brightport_deebo2](#d-brightport_deebo2)

    <span id="d-brightport_deebo5"></span>**`brightport_deebo5`** Deebo: “I already told you they'll be picked soon, just go speak with Alduan in the orchard.”


    <span id="d-brightport_deebo1"></span>**`brightport_deebo1`** Deebo: “Oh no! I just hope nothing happened to my precious apples.” — **effects:** sets stage 205 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-205)

    - “Can I get a new batch of apples?” *(if NOT reached stage 40 of [Bread and circus](../quests/brightport_bakery.md#stage-40))* → [brightport_deebo_selector](#d-brightport_deebo_selector)
    - “A little too late now...” *(if reached stage 40 of [Bread and circus](../quests/brightport_bakery.md#stage-40))* → *conversation ends*

    <span id="d-deebo_orchard_deebo_30"></span>**`deebo_orchard_deebo_30`** Deebo: “Well, it is a four-legged nightmare of a canine that has destroyed my property and killed my pig. I fear that one of my horses will be next.”

    - “That's terrible news. What are you going to do about it. Besides complaining, that is?” → [deebo_orchard_deebo_40](#d-deebo_orchard_deebo_40)

    <span id="d-deebo_orchard_deebo_50"></span>**`deebo_orchard_deebo_50`** Deebo: “That's great to hear! When can you start?” — **effects:** sets stage 0 of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-0)

    - “Not right now. Can I pick some apples first?” → [deebo_orchard_deebo_pc_asks_to_pick_apples](#d-deebo_orchard_deebo_pc_asks_to_pick_apples)
    - “Right now. Let's get it!” → [deebo_orchard_deebo_60](#d-deebo_orchard_deebo_60)

    <span id="d-deebo_orchard_deebo_100"></span>**`deebo_orchard_deebo_100`** Deebo: “As far your reward is concerned, I am now willing to sell and trade with you. Please take a look.”

    - “Sounds good.” → *shop opens*

    <span id="d-deebo_orchard_deebo_horse_talk_30"></span>**`deebo_orchard_deebo_horse_talk_30`** Deebo: “No way. Is there anything else that you want to talk about?”

    - “Well, I was also wondering about your barn.” → [deebo_orchard_deebo_barn_talk_10](#d-deebo_orchard_deebo_barn_talk_10)

    <span id="d-deebo_orchard_deebo_barn_talk_10"></span>**`deebo_orchard_deebo_barn_talk_10`** Deebo: “What about it?”

    - “Well, it is one of the biggest buildings that I've ever seen. What's in there?” → [deebo_orchard_deebo_barn_talk_20](#d-deebo_orchard_deebo_barn_talk_20)

    <span id="d-brightport_deebo2"></span>**`brightport_deebo2`** Deebo: “That would be 1,600 gold.”

    - “Ok, here you go. [Give him the gold.]” *(if pay 1,600 gold)* → [brightport_deebo3](#d-brightport_deebo3)
    - “Whaat, I don't have that gold!” → [brightport_deebo4](#d-brightport_deebo4)

    <span id="d-deebo_orchard_deebo_40"></span>**`deebo_orchard_deebo_40`** Deebo: “Funny kid you are. I am looking for someone to hunt it down and kill it.”

    - “Really! I am more than willing and able to do this job for you.” → [deebo_orchard_deebo_50](#d-deebo_orchard_deebo_50)

    <span id="d-deebo_orchard_deebo_pc_asks_to_pick_apples"></span>**`deebo_orchard_deebo_pc_asks_to_pick_apples`** Deebo: “Absolutely not.”

    - “Sorry for asking.” → *conversation ends*

    <span id="d-deebo_orchard_deebo_60"></span>**`deebo_orchard_deebo_60`** Deebo: “First, I have to warn you, this is no ordinary forest animal. This thing is capable of dragging away full-sized adult pigs. Be warned now.”

    - “I am ready! No more talking.” → [deebo_orchard_deebo_70](#d-deebo_orchard_deebo_70)
    - “I am not so sure I am capable, but I will give it a try.” → [deebo_orchard_deebo_70](#d-deebo_orchard_deebo_70)
    - “I need time to think about the risks.” → *conversation ends*

    <span id="d-deebo_orchard_deebo_barn_talk_20"></span>**`deebo_orchard_deebo_barn_talk_20`** Deebo: “Supplies for my orchard and for my horses.”

    - “Can I see for myself? I would like to climb up into the loft for some much needed fun.” → [deebo_orchard_deebo_barn_talk_30](#d-deebo_orchard_deebo_barn_talk_30)

    <span id="d-brightport_deebo3"></span>**`brightport_deebo3`** Deebo: “My workers will have them picked in no time. Go speak with my farmhand, Alduan. He'll give them to you.” — **effects:** sets stage 45 of [Bread and circus](../quests/brightport_bakery.md#stage-45), starts timer “brightport_apple”


    <span id="d-brightport_deebo4"></span>**`brightport_deebo4`** Deebo: “Then no apples for you, because I don't lend!”


    <span id="d-deebo_orchard_deebo_70"></span>**`deebo_orchard_deebo_70`** Deebo: “OK, I have faith in you.”

    - Next → [deebo_orchard_deebo_71](#d-deebo_orchard_deebo_71)

    <span id="d-deebo_orchard_deebo_barn_talk_30"></span>**`deebo_orchard_deebo_barn_talk_30`** Deebo: “No way! You are annoying me. Go away kid.”

    - “OK. I will leave you be.” → *conversation ends*

    <span id="d-deebo_orchard_deebo_71"></span>**`deebo_orchard_deebo_71`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 4 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-4))* → [deebo_orchard_deebo_spawn_gj](#d-deebo_orchard_deebo_spawn_gj)
    - Next *(if latest stage of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-10) is 10)* → [deebo_orchard_deebo_81](#d-deebo_orchard_deebo_81)

    <span id="d-deebo_orchard_deebo_spawn_gj"></span>**`deebo_orchard_deebo_spawn_gj`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 10 of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-10)

    - Next *(if random chance (30%))* → [deebo_orchard_deebo_spawn_gj_30](#d-deebo_orchard_deebo_spawn_gj_30)
    - Next *(if random chance (43%))* → [sullengard_woods12_gj_spawn_43](#d-sullengard_woods12_gj_spawn_43)
    - Next *(if random chance (50%))* → [sullengard_woods4_gj_spawn_50](#d-sullengard_woods4_gj_spawn_50)
    - Next *(if random chance (100%))* → [sullengard_woods_gj_spawn_100](#d-sullengard_woods_gj_spawn_100)

    <span id="d-deebo_orchard_deebo_81"></span>**`deebo_orchard_deebo_81`** Deebo: “The Golden jackal was last seen heading back into the "Sullengard forest" just to the west of my orchard. Return to me with proof of its death.”


    <span id="d-deebo_orchard_deebo_spawn_gj_30"></span>**`deebo_orchard_deebo_spawn_gj_30`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on sullengard_woods4

    - Next → [deebo_orchard_deebo_80](#d-deebo_orchard_deebo_80)

    <span id="d-sullengard_woods12_gj_spawn_43"></span>**`sullengard_woods12_gj_spawn_43`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on sullengard_woods12

    - Next → [deebo_orchard_deebo_80](#d-deebo_orchard_deebo_80)

    <span id="d-sullengard_woods4_gj_spawn_50"></span>**`sullengard_woods4_gj_spawn_50`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on sullengard_west_ravine

    - Next → [deebo_orchard_deebo_80](#d-deebo_orchard_deebo_80)

    <span id="d-sullengard_woods_gj_spawn_100"></span>**`sullengard_woods_gj_spawn_100`** *(silent check: the first matching branch below is taken)* — **effects:** spawns monsters on sullengard_woods_gj1

    - Next → [deebo_orchard_deebo_80](#d-deebo_orchard_deebo_80)

    <span id="d-deebo_orchard_deebo_80"></span>**`deebo_orchard_deebo_80`** Deebo: “The Golden jackal was last seen heading back into the "Sullengard forest" just to the west of my orchard. Return to me with proof of it's death.” — **effects:** sets stage 4 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-4), sets stage 10 of [Hunting the hunter](../quests/deebo_orchard_hth.md#stage-10)




## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=deebo_orchard_deebo.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=deebo_orchard_deebo.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=deebo_orchard_deebo.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=deebo_orchard_deebo.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `deebo_orchard_deebo` · Data from v0.8.18</small>
