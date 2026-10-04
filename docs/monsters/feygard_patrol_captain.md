# ![](../assets/icons/monsters/monsters_men_3.png){ .sprite } Feygard patrol captain

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_3.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `feygard_patrol_captain` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Foaming Flask Tavern |
| **Introduced** | v0.7.0 or earlier |

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
| [foaming_flask](../maps/foaming_flask.md) | Foaming Flask Tavern | 1 | – |


## Quests

- [Beer Bootlegging](../quests/beer_bootlegging.md): stages 10, 90, 100, 110, 120
- [Feygard errands](../quests/feygard_shipment.md): stages 50, 60
- [Immaculate kidnapping](../quests/Thieves02.md): stages 15
- [Uncertain cause](../quests/wrye.md): stages 42

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Feygard patrol captain. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/ff_captain_1.json" data-npc="Feygard patrol captain" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (49 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ff_captain_1"></span>**`ff_captain_1`** [Feygard patrol captain](../monsters/feygard_patrol_captain.md): “Are you lost, son? This is no place for a kid like you.”

    - “I have a shipment of iron swords from Gandoren for you.” *(if reached stage 56 of [Feygard errands](../quests/feygard_shipment.md#stage-56); hand over 10× [Degraded Feygard iron sword](../items/fg_ironsword_d.md))* → [ff_captain_vg_items_1](#d-ff_captain_vg_items_1)
    - “I have a shipment of iron swords from Gandoren for you.” *(if reached stage 25 of [Feygard errands](../quests/feygard_shipment.md#stage-25); hand over 10× [Feygard iron sword](../items/fg_ironsword.md))* → [ff_captain_fg_items_1](#d-ff_captain_fg_items_1)
    - “Who are you?” → [ff_captain_2](#d-ff_captain_2)
    - “Have you seen a boy called Rincel around here recently?” *(if reached stage 41 of [Uncertain cause](../quests/wrye.md#stage-41))* → [ff_captain_rincel_1](#d-ff_captain_rincel_1)
    - “Hi! I have been sent by Herg ... Hertzsen Laumwill, patriarch of the Laumwill family, to bring back his daughter!” *(if reached stage 10 of [Immaculate kidnapping](../quests/Thieves02.md#stage-10); NOT reached stage 15 of [Immaculate kidnapping](../quests/Thieves02.md#stage-15))* → [ff_captain_guild02_1](#d-ff_captain_guild02_1)
    - “Let's talk about the beer investigation.” *(if reached stage 10 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-10); NOT reached stage 90 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-90); NOT reached stage 100 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-100); NOT reached stage 110 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-110); NOT reached stage 120 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-120))* → [ff_captain_selector](#d-ff_captain_selector)

    <span id="d-ff_captain_vg_items_1"></span>**`ff_captain_vg_items_1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 60 of [Feygard errands](../quests/feygard_shipment.md#stage-60)

    - branch 1 → [ff_captain_items_1](#d-ff_captain_items_1)

    <span id="d-ff_captain_fg_items_1"></span>**`ff_captain_fg_items_1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 50 of [Feygard errands](../quests/feygard_shipment.md#stage-50)

    - branch 1 → [ff_captain_items_1](#d-ff_captain_items_1)

    <span id="d-ff_captain_2"></span>**`ff_captain_2`** Feygard patrol captain: “I am the guard captain of this patrol. We hail from the great city of Feygard.”

    - “Feygard, where is that?” → [ff_captain_4](#d-ff_captain_4)
    - “What do you do around here?” → [ff_captain_3](#d-ff_captain_3)

    <span id="d-ff_captain_rincel_1"></span>**`ff_captain_rincel_1`** Feygard patrol captain: “There was a kid running around in here a while ago.”

    - Next → [ff_captain_rincel_2](#d-ff_captain_rincel_2)

    <span id="d-ff_captain_guild02_1"></span>**`ff_captain_guild02_1`** Feygard patrol captain: “What? I haven't been informed of that. Since you seem like an inexperienced kid, I don't believe you.”

    - “Ergh ... Mr Laumwill is grateful for your protection. However ... Ah! He has given this reward of 1,000 gold for your…” *(if pay 1,000 gold)* → [ff_captain_guild02_2a](#d-ff_captain_guild02_2a)
    - “Trust me, I'm the one that delivered those swords from Gandoren to you!” *(if reached stage 80 of [Feygard errands](../quests/feygard_shipment.md#stage-80))* → [ff_captain_guild02_2b](#d-ff_captain_guild02_2b)
    - “(I would like to bribe the captain, but I need at least 1,000 Gold) I will come back later.” *(if NOT have 1,000 gold)* → *conversation ends*

    <span id="d-ff_captain_selector"></span>**`ff_captain_selector`** Feygard patrol captain: “Have you learned anything about the beer?”

    - “Not yet.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-10) is 10)* → [ff_captain_hurry_up](#d-ff_captain_hurry_up)
    - “A little bit, but I need to go find out more.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-20) is 20)* → [ff_captain_hurry_up](#d-ff_captain_hurry_up)
    - “I've talked to a couple of tavern owners, learned a few things, but I need to talk to some more people” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-30) is 30)* → [ff_captain_hurry_up](#d-ff_captain_hurry_up)
    - “I've learned a lot, but I am still not ready to give you my report.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-40) is 40)* → [ff_captain_hurry_up](#d-ff_captain_hurry_up)
    - “All the information I have obtained points me to Sullengard.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-50) is 50)* → [ff_captain_beer_120](#d-ff_captain_beer_120)
    - “I still have some investigation to conduct in Sullengard. I will return to you afterwards.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-60) is 60)* → *conversation ends*
    - “I still have some investigation to conduct in Sullengard. I will return to you afterwards.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-70) is 70)* → *conversation ends*
    - “I've learned everything that you will care to know about the beer bootlegging operation.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-80) is 80)* → [ff_captain_beer_tell_everything_10](#d-ff_captain_beer_tell_everything_10)
    - “I know who is distributing the beer, but not the source of the beer.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-80) is 80)* → [ff_captain_beer_tell_sull](#d-ff_captain_beer_tell_sull)
    - “I know where the beer is coming from, but I do not know who is distributing it.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-80) is 80)* → [ff_captain_beer_tell_thieves](#d-ff_captain_beer_tell_thieves)
    - “I am sorry, but I have learned nothing that I am willing to share or feel confident in sharing with you.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-80) is 80)* → [ff_captain_beer_tell](#d-ff_captain_beer_tell)

    <span id="d-ff_captain_items_1"></span>**`ff_captain_items_1`** Feygard patrol captain: “Excellent, I have been waiting for these. Thank you for bringing them to me.”


    <span id="d-ff_captain_4"></span>**`ff_captain_4`** Feygard patrol captain: “The great city of Feygard is the greatest sight you will ever see. Follow the road northwest.”

    - “Thank you. Shadow be with you.” → [ff_captain_shadow_1](#d-ff_captain_shadow_1)
    - “Thank you, Goodbye.” → *conversation ends*

    <span id="d-ff_captain_3"></span>**`ff_captain_3`** Feygard patrol captain: “We are travelling the main road to make sure the merchants and travelers are safe. We keep the peace around here.”

    - “You mentioned Feygard. Where is that?” → [ff_captain_4](#d-ff_captain_4)
    - “So when you say "peace", you really mean "law enforcement"?” *(if NOT reached stage 10 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-10))* → [ff_captain_beer_10](#d-ff_captain_beer_10)

    <span id="d-ff_captain_rincel_2"></span>**`ff_captain_rincel_2`** Feygard patrol captain: “I never talked to him though, so I don't know if he is the one you are looking for.”

    - “OK, that might be something worth checking anyway.” → [ff_captain_rincel_3](#d-ff_captain_rincel_3)

    <span id="d-ff_captain_guild02_2a"></span>**`ff_captain_guild02_2a`** Feygard patrol captain: “Oh! What a considerable reward! OK, OK. Only Feygard people are so generous!”

    - Next → [ff_captain_guild02_3](#d-ff_captain_guild02_3)

    <span id="d-ff_captain_guild02_2b"></span>**`ff_captain_guild02_2b`** Feygard patrol captain: “Oh, I see. Maybe you're right.”

    - Next → [ff_captain_guild02_3](#d-ff_captain_guild02_3)

    <span id="d-ff_captain_hurry_up"></span>**`ff_captain_hurry_up`** Feygard patrol captain: “Then why are you wasting your and my time by coming back here? Get going.”

    - “Yes, sir! I'm on it.” → *conversation ends*

    <span id="d-ff_captain_beer_120"></span>**`ff_captain_beer_120`** Feygard patrol captain: “Sullengard? Of course! Get down there now kid and get me more information.”

    - “Yes, sir. Anything for the glorious Feygard.” → *conversation ends*
    - “I'll go to Sullengard when I feel like it. You don't own me.” → *conversation ends*
    - “Watch it captain! I am not one of your soldiers.” → *conversation ends*

    <span id="d-ff_captain_beer_tell_everything_10"></span>**`ff_captain_beer_tell_everything_10`** Feygard patrol captain: “I knew that I could count on you kid. Please enlighten me and I will reward you handsomely.”

    - “What would you like to know first?” → [ff_captain_beer_tell_everything_20](#d-ff_captain_beer_tell_everything_20)

    <span id="d-ff_captain_beer_tell_sull"></span>**`ff_captain_beer_tell_sull`** Feygard patrol captain: “That is disappointing, but at least you know something. Tell me.”

    - “It is the Theives guild.” → [ff_captain_beer_tell_sull_10](#d-ff_captain_beer_tell_sull_10)

    <span id="d-ff_captain_beer_tell_thieves"></span>**`ff_captain_beer_tell_thieves`** Feygard patrol captain: “That is disappointing, but at least you know something. Please tell me.”

    - “The brewers are the families of Sullengard.” → [ff_captain_beer_tell_thieves_10](#d-ff_captain_beer_tell_thieves_10)

    <span id="d-ff_captain_beer_tell"></span>**`ff_captain_beer_tell`** Feygard patrol captain: “WHAT?! Tell me what you know, now!”

    - “That's the thing, I don't 'know' anything that I could prove.” → [ff_captain_beer_tell_10](#d-ff_captain_beer_tell_10)

    <span id="d-ff_captain_shadow_1"></span>**`ff_captain_shadow_1`** Feygard patrol captain: “The Shadow? Don't tell me you believe in that stuff. In my experience, only troublemakers talk of the Shadow.”


    <span id="d-ff_captain_beer_10"></span>**`ff_captain_beer_10`** Feygard patrol captain: “You got it, kid, we watch out for lawbreakers!”

    - “I knew it! Do you have your eye on anyone right now?” → [ff_captain_beer_20](#d-ff_captain_beer_20)
    - “There's nothing to look at here. [You slowly back up and end the conversation.]” → *conversation ends*

    <span id="d-ff_captain_rincel_3"></span>**`ff_captain_rincel_3`** Feygard patrol captain: “I noticed he left to the west heading out of the Foaming Flask tavern.” — **effects:** sets stage 42 of [Uncertain cause](../quests/wrye.md#stage-42)

    - “West. Got it. Thanks for the information.” → [ff_captain_rincel_4](#d-ff_captain_rincel_4)

    <span id="d-ff_captain_guild02_3"></span>**`ff_captain_guild02_3`** Feygard patrol captain: “I have to stay here to supervise my guards. They sometimes need educating about what to do. I assume you're able to escort her without problems?” — **effects:** sets stage 15 of [Immaculate kidnapping](../quests/Thieves02.md#stage-15)

    - “[Lie]For the glory of Feygard, I will!” → *conversation ends*
    - “[Lie]Don't worry, she's safe with me.” → *conversation ends*

    <span id="d-ff_captain_beer_tell_everything_20"></span>**`ff_captain_beer_tell_everything_20`** Feygard patrol captain: “Where is it coming from?”

    - “It is coming from a town south of here called Sullengard.” → [ff_captain_beer_tell_everything_30](#d-ff_captain_beer_tell_everything_30)

    <span id="d-ff_captain_beer_tell_sull_10"></span>**`ff_captain_beer_tell_sull_10`** Feygard patrol captain: “The Thieves' Guild? Are you sure?”

    - “Oh yeah. I heard it directly from them.” → [ff_captain_beer_tell_sull_20](#d-ff_captain_beer_tell_sull_20)

    <span id="d-ff_captain_beer_tell_thieves_10"></span>**`ff_captain_beer_tell_thieves_10`** Feygard patrol captain: “Sullengard?! Of course it would be coming from Sullengard. I should have known it is coming from them.”

    - Next → [ff_captain_beer_tell_thieves_11](#d-ff_captain_beer_tell_thieves_11)

    <span id="d-ff_captain_beer_tell_10"></span>**`ff_captain_beer_tell_10`** Feygard patrol captain: “I knew that you would be a waste of my time. I'll reward you with nothing.” — **effects:** sets stage 120 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-120), faction “factionCountShadow” set to 4, faction “factionCountThieves” set to 4, faction “factionCountFeygard” set to -4

    - “I should get going. Sorry that I could not be more helpful.” → *conversation ends*

    <span id="d-ff_captain_beer_20"></span>**`ff_captain_beer_20`** Feygard patrol captain: “You bet I have. I suspect we are witnessing one right now.”

    - “Really?! Who is it? Can I help?” → [ff_captain_beer_30](#d-ff_captain_beer_30)

    <span id="d-ff_captain_rincel_4"></span>**`ff_captain_rincel_4`** Feygard patrol captain: “Always happy to help. Anything for the glory of Feygard.”

    - “Shadow be with you.” → [ff_captain_shadow_1](#d-ff_captain_shadow_1)
    - “Goodbye.” → *conversation ends*

    <span id="d-ff_captain_beer_tell_everything_30"></span>**`ff_captain_beer_tell_everything_30`** Feygard patrol captain: “Sullengard?! Of course it would be coming from Sullengard.”

    - Next → [ff_captain_beer_tell_everything_32](#d-ff_captain_beer_tell_everything_32)

    <span id="d-ff_captain_beer_tell_sull_20"></span>**`ff_captain_beer_tell_sull_20`** Feygard patrol captain: “Well done kid. Here, take some gold.” — **effects:** gives [Gold coins](../items/gold.md), faction “factionCountThieves” set to -4, faction “factionCountFeygard” set to 4

    - “Thanks and Shadow be with you.” → [ff_captain_beer_tell_sull_30](#d-ff_captain_beer_tell_sull_30)
    - “Thanks and glory to Feygard.” → [ff_captain_beer_tell_sull_30](#d-ff_captain_beer_tell_sull_30)

    <span id="d-ff_captain_beer_tell_thieves_11"></span>**`ff_captain_beer_tell_thieves_11`** Feygard patrol captain: “Well done kid. Here, take some gold.” — **effects:** gives [Gold coins](../items/gold.md), faction “factionCountShadow” set to -4, faction “factionCountFeygard” set to 4

    - “Thanks!” → [ff_captain_beer_tell_thieves_20](#d-ff_captain_beer_tell_thieves_20)

    <span id="d-ff_captain_beer_30"></span>**`ff_captain_beer_30`** Feygard patrol captain: “Hey, kid, not so loud!”

    - “Oh, sorry, but this sounds exciting.” → [ff_captain_beer_40](#d-ff_captain_beer_40)

    <span id="d-ff_captain_beer_tell_everything_32"></span>**`ff_captain_beer_tell_everything_32`** Feygard patrol captain: “What else can you tell me?”

    - “I know that the Thieves' Guild are the ones helping the people of Sullengard distribute their beer.” → [ff_captain_beer_tell_everything_33](#d-ff_captain_beer_tell_everything_33)

    <span id="d-ff_captain_beer_tell_sull_30"></span>**`ff_captain_beer_tell_sull_30`** Feygard patrol captain: “I'd like you to know that as soon as I can get word back to Feygard, we will be putting an end to their beer bootlegging operation.” — **effects:** sets stage 100 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-100)


    <span id="d-ff_captain_beer_tell_thieves_20"></span>**`ff_captain_beer_tell_thieves_20`** Feygard patrol captain: “I'd like you to know that as soon as I can get word back to Feygard, we will be putting an end to their beer bootlegging operation.” — **effects:** sets stage 110 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-110)

    - “Glory to Feygard.” → *conversation ends*

    <span id="d-ff_captain_beer_40"></span>**`ff_captain_beer_40`** Feygard patrol captain: “Well, if you look around this tavern, both inside and outside, do you notice anything?”

    - “Um...no. Should I?” → [ff_captain_beer_50](#d-ff_captain_beer_50)

    <span id="d-ff_captain_beer_tell_everything_33"></span>**`ff_captain_beer_tell_everything_33`** Feygard patrol captain: “The Thieves' Guild? Are you sure?”

    - “Oh yeah. I heard it directly from them.” → [ff_captain_beer_tell_everything_40](#d-ff_captain_beer_tell_everything_40)

    <span id="d-ff_captain_beer_50"></span>**`ff_captain_beer_50`** Feygard patrol captain: “YES!”

    - “Please enlighten me.” → [ff_captain_beer_60](#d-ff_captain_beer_60)
    - “Now you are the one that needs to lower his voice.” → [ff_captain_beer_60](#d-ff_captain_beer_60)

    <span id="d-ff_captain_beer_tell_everything_40"></span>**`ff_captain_beer_tell_everything_40`** Feygard patrol captain: “Well done kid. Here, take some gold.” — **effects:** gives [Gold coins](../items/gold.md), faction “factionCountShadow” set to -4, faction “factionCountThieves” set to -4, faction “factionCountFeygard” set to 4

    - “All that work, and the reward is just gold?” → [ff_captain_beer_tell_everything_50](#d-ff_captain_beer_tell_everything_50)

    <span id="d-ff_captain_beer_60"></span>**`ff_captain_beer_60`** Feygard patrol captain: “There is a large amount of beer here. There are a number of beer barrels outside. Both full and empty ones. There is a lot inside as well. Too much in fact!”

    - “OK...Why does this equal a law being broken?” → [ff_captain_beer_70](#d-ff_captain_beer_70)

    <span id="d-ff_captain_beer_tell_everything_50"></span>**`ff_captain_beer_tell_everything_50`** Feygard patrol captain: “Hey, what do you want from me? I'm stuck here babysitting a bunch of drunk guards.”

    - Next → [ff_captain_beer_tell_everything_60](#d-ff_captain_beer_tell_everything_60)

    <span id="d-ff_captain_beer_70"></span>**`ff_captain_beer_70`** Feygard patrol captain: “Well, for starters, Feygard taxes all beer sales. It is one of the best sources of gold used by Feygard to provide protection for the cities and towns.”

    - “Understood, but I am still not seeing how this means that a law has been broken.” → [ff_captain_beer_80](#d-ff_captain_beer_80)

    <span id="d-ff_captain_beer_tell_everything_60"></span>**`ff_captain_beer_tell_everything_60`** Feygard patrol captain: “Anyways, I'd like you to know that as soon as I can get word back to Feygard, we will be putting an end to their beer bootlegging operation.” — **effects:** sets stage 90 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-90)

    - “Glory to Feygard.” → *conversation ends*

    <span id="d-ff_captain_beer_80"></span>**`ff_captain_beer_80`** Feygard patrol captain: “Well, you see kid, I used to work in the 'tax collection' division of the Feygard patrol and I don't ever remember seeing the kind of collected taxes that would reflect this kind of volume of beer.”

    - “Um...I think I might be catching up to what you are thinking. Please, continue” → [ff_captain_beer_90](#d-ff_captain_beer_90)

    <span id="d-ff_captain_beer_90"></span>**`ff_captain_beer_90`** Feygard patrol captain: “That's pretty much it kid, but I need your help.”

    - “Anything for the glorious Feygard.” → [ff_captain_beer_100](#d-ff_captain_beer_100)
    - “OK, but only if there is something in it for me.” → [ff_captain_beer_100](#d-ff_captain_beer_100)
    - “No, thanks. I'm out of here.” → *conversation ends*

    <span id="d-ff_captain_beer_100"></span>**`ff_captain_beer_100`** Feygard patrol captain: “Great to hear. I need you to talk with the tavern owner and find out anything you can about the beer.” — **effects:** sets stage 10 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-10)

    - “Why me?” → [ff_captain_beer_110](#d-ff_captain_beer_110)
    - “Sounds easy. I'll do it.” → [ff_captain_beer_111](#d-ff_captain_beer_111)

    <span id="d-ff_captain_beer_110"></span>**`ff_captain_beer_110`** Feygard patrol captain: “Well, because I am a Feygard captain and as such, the tavern keep will never give me information.”


    <span id="d-ff_captain_beer_111"></span>**`ff_captain_beer_111`** Feygard patrol captain: “Great. Report back to me when you have learnt something useful.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 4 lines added, 1 line changed |
| [v0.8.2](../versions/0.8.2.md) | Dialogue: 30 lines added, 2 lines changed |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 1 line changed |
| [v0.8.13](../versions/0.8.13.md) | Dialogue: 3 lines changed<br>· text: “The thieves guild? Are you sure?” → “The Thieves' Guild? Are you sure?”<br>· text: “The thieves guild? Are you sure?” → “The Thieves' Guild? Are you sure?” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 3 lines added, 4 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol_captain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol_captain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol_captain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol_captain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `feygard_patrol_captain` |
    | Spawn group | `ff_captain` |
    | Loot table | – |
    | Conversation | `ff_captain_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:3` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "feygard_patrol_captain",
     "name": "Feygard patrol captain",
     "iconID": "monsters_men:3",
     "monsterClass": "humanoid",
     "spawnGroup": "ff_captain",
     "phraseID": "ff_captain_1"
    }
    ```


<small>Data from v0.8.18</small>
