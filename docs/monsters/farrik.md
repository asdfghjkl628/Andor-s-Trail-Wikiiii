# ![](../assets/icons/monsters/monsters_rogue1_0.png){ .sprite } Farrik

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

## Found on

- [fallhaven_derelict2](../maps/fallhaven_derelict2.md)
- [fallhaven_derelict2_t](../maps/fallhaven_derelict2_t.md)

## Quests

- [Beer Bootlegging](../quests/beer_bootlegging.md): stages 50
- [Night visit](../quests/farrik.md): stages 10, 20, 30, 70, 80

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Farrik. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/farrik_select_1.json" data-npc="Farrik" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (39 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-farrik_select_1"></span>**`farrik_select_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 70 of [Night visit](../quests/farrik.md#stage-70))* → [farrik_return_2](#d-farrik_return_2)
    - branch 2 *(if reached stage 80 of [Night visit](../quests/farrik.md#stage-80))* → [farrik_return_2](#d-farrik_return_2)
    - branch 3 → [farrik_select_2](#d-farrik_select_2)

    <span id="d-farrik_return_2"></span>**`farrik_return_2`** Farrik: “Thank you for your help with the guard captain earlier.”

    - “Sure.” → *conversation ends*
    - “I asked Dunla about the beer distribution operation and the 'business agreement'. He sent me to you.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-40) is 40)* → [farrik_beer](#d-farrik_beer)

    <span id="d-farrik_select_2"></span>**`farrik_select_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Night visit](../quests/farrik.md#stage-20); NOT reached stage 30 of [Night visit](../quests/farrik.md#stage-30))* → [farrik_return_1](#d-farrik_return_1)
    - branch 2 *(if reached stage 30 of [Night visit](../quests/farrik.md#stage-30); NOT reached stage 20 of [Night visit](../quests/farrik.md#stage-20))* → [farrik_return_3](#d-farrik_return_3)
    - branch 3 → [farrik_1](#d-farrik_1)

    <span id="d-farrik_beer"></span>**`farrik_beer`** Farrik: “Well, kid, all you really need to know is that there is a beer-making town that has been selling their beer to other towns and they are getting unfairly taxed on those sales.”

    - “By Feygard?” → [farrik_beer_10](#d-farrik_beer_10)
    - “What is the name of this town?” → [farrik_beer_town](#d-farrik_beer_town)

    <span id="d-farrik_return_1"></span>**`farrik_return_1`** Farrik: “Hello again my friend. How goes your mission to get the guard captain drunk?”

    - “I am not done yet, but I am working on it.” → [farrik_23](#d-farrik_23)
    - “It is done. He should be no problem during the night.” *(if reached stage 60 of [Night visit](../quests/farrik.md#stage-60))* → [farrik_24](#d-farrik_24)

    <span id="d-farrik_return_3"></span>**`farrik_return_3`** Farrik: “So did you tell the guard captain about our plan then?”

    - “No, I haven't talked to him.” → *conversation ends*
    - “[Lie]. No. I went there, but I overheard the guard captain saying there was no real threat, so they will lower…” *(if reached stage 50 of [Night visit](../quests/farrik.md#stage-50))* → [farrik_26](#d-farrik_26)

    <span id="d-farrik_1"></span>**`farrik_1`** Farrik: “Hello. I heard that you helped us find the key of Luthor. Good work, it will really come in handy.”

    - “Who are you?” → [farrik_2](#d-farrik_2)
    - “What can you tell me about the Thieves' Guild?” → [farrik_4](#d-farrik_4)

    <span id="d-farrik_beer_10"></span>**`farrik_beer_10`** Farrik: “Yes.”

    - “Why is the Thieves guild helping this town?” → [farrik_beer_20](#d-farrik_beer_20)

    <span id="d-farrik_beer_town"></span>**`farrik_beer_town`** Farrik: “Oh, how silly of me to leave out that detail.”

    - “Yes, it was 'silly' of you to do that.” → [farrik_beer_town_10](#d-farrik_beer_town_10)

    <span id="d-farrik_23"></span>**`farrik_23`** Farrik: “Good. Report back to me when you have gotten the guard captain to drink that special mead.” — **effects:** sets stage 20 of [Night visit](../quests/farrik.md#stage-20)

    - “Will do.” → [farrik_14](#d-farrik_14)

    <span id="d-farrik_24"></span>**`farrik_24`** Farrik: “That is good news! Now we should be able to get our friend out from jail tonight.” — **effects:** sets stage 70 of [Night visit](../quests/farrik.md#stage-70), removes monsters from fallhaven_prison

    - Next → [farrik_25](#d-farrik_25)

    <span id="d-farrik_26"></span>**`farrik_26`** Farrik: “That's very useful information. Well done. You have my thanks, friend.” — **effects:** sets stage 80 of [Night visit](../quests/farrik.md#stage-80)


    <span id="d-farrik_2"></span>**`farrik_2`** Farrik: “I'm Farrik, Umar's brother.”

    - “What do you do around here?” → [farrik_3](#d-farrik_3)
    - “What can you tell me about the Thieves' Guild?” → [farrik_4](#d-farrik_4)

    <span id="d-farrik_4"></span>**`farrik_4`** Farrik: “We try to keep to ourselves as much as possible, and help our fellow thieves as much as possible.”

    - “Any recent events happening?” → [farrik_5](#d-farrik_5)
    - “I asked Dunla about the beer distribution operation and the 'business agreement'. He sent me to you.” *(if latest stage of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-40) is 40)* → [farrik_beer](#d-farrik_beer)

    <span id="d-farrik_beer_20"></span>**`farrik_beer_20`** Farrik: “Well, the gold of course.”

    - “Anything else?” → [farrik_beer_30](#d-farrik_beer_30)

    <span id="d-farrik_beer_town_10"></span>**`farrik_beer_town_10`** Farrik: “It is Sullengard, of course.” — **effects:** sets stage 50 of [Beer Bootlegging](../quests/beer_bootlegging.md#stage-50)

    - “Sullengard? I've never been there. Where is it located?” *(if NOT reached stage 19 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-19))* → [farrik_beer_sull_unknown](#d-farrik_beer_sull_unknown)
    - “Oh Sullengard? I know where that is...[I think]” → *conversation ends*
    - “Thank you.” → *conversation ends*

    <span id="d-farrik_14"></span>**`farrik_14`** Farrik: “Thank you. Now please leave me.”


    <span id="d-farrik_25"></span>**`farrik_25`** Farrik: “Thank you for your help my friend. Take these coins as a token of our appreciation.” — **effects:** gives [Gold coins](../items/gold.md)

    - “Thank you. Goodbye.” → *conversation ends*
    - “Finally, some gold.” → *conversation ends*

    <span id="d-farrik_3"></span>**`farrik_3`** Farrik: “I mostly manage our trading with other guilds and keep an eye on what the thieves need to be as effective as they can be.”

    - “What can you tell me about the Thieves' Guild?” → [farrik_4](#d-farrik_4)

    <span id="d-farrik_5"></span>**`farrik_5`** Farrik: “Well, there was one thing a few weeks ago. One of our guild members got arrested for trespassing.”

    - Next → [farrik_6](#d-farrik_6)

    <span id="d-farrik_beer_30"></span>**`farrik_beer_30`** Farrik: “Nope. You do not need to know any other details”

    - “Well, could you at least tell what town it is that is making the beer?” → [farrik_beer_town](#d-farrik_beer_town)

    <span id="d-farrik_beer_sull_unknown"></span>**`farrik_beer_sull_unknown`** Farrik: “South of Vilegard, but beware, the travel to it is not for the faint of heart.”

    - “I guess it's on to Sullengard for me. Bye.” → *conversation ends*

    <span id="d-farrik_6"></span>**`farrik_6`** Farrik: “The Fallhaven guard has started to get really annoyed with us lately. Probably because we have been very successful in our recent missions.”

    - Next → [farrik_7](#d-farrik_7)

    <span id="d-farrik_7"></span>**`farrik_7`** Farrik: “The guards have increased their security lately, leading to them arresting one of our members.”

    - Next → [farrik_8](#d-farrik_8)

    <span id="d-farrik_8"></span>**`farrik_8`** Farrik: “He is currently held in the jail here in Fallhaven, pending transfer to Feygard.”

    - “What did he do?” → [farrik_9](#d-farrik_9)

    <span id="d-farrik_9"></span>**`farrik_9`** Farrik: “Oh, nothing serious. He was trying to get into the catacombs of Fallhaven church.”

    - Next → [farrik_10](#d-farrik_10)

    <span id="d-farrik_10"></span>**`farrik_10`** Farrik: “But now that you have helped us with that mission, I guess we don't need to go there anymore.”

    - Next → [farrik_11](#d-farrik_11)

    <span id="d-farrik_11"></span>**`farrik_11`** Farrik: “I guess I can trust you with this secret. We are planning a mission tonight to help him out of jail.” — **effects:** sets stage 10 of [Night visit](../quests/farrik.md#stage-10)

    - “Those guards really seem annoying.” → [farrik_13](#d-farrik_13)
    - “After all, if he wasn't allowed down there, then the guards are right to arrest him.” → [farrik_12](#d-farrik_12)

    <span id="d-farrik_13"></span>**`farrik_13`** Farrik: “Oh yes, they are. The people also dislike them in general, it's not just us in the Thieves' Guild.”

    - “Is there anything I can do to help you with those annoying guards?” → [farrik_16](#d-farrik_16)

    <span id="d-farrik_12"></span>**`farrik_12`** Farrik: “Yeah, I guess so. But for the guild's sake, we would rather have our friend freed than imprisoned.”

    - “Don't worry, your secret plan to free him is safe with me.” → [farrik_14](#d-farrik_14)
    - “[Lie] Don't worry, your secret plan to free him is safe with me.” → [farrik_14](#d-farrik_14)
    - “Maybe I should tell the guards that you are planning to get him out?” *(if NOT reached stage 20 of [Night visit](../quests/farrik.md#stage-20))* → [farrik_15](#d-farrik_15)

    <span id="d-farrik_16"></span>**`farrik_16`** Farrik: “Are you sure you want to annoy the guards? If they catch word of you being involved, you could get into a lot of trouble.”

    - “No problem, I can handle myself!” → [farrik_18](#d-farrik_18)
    - “There might be a reward for this later on. I'm in.” → [farrik_18](#d-farrik_18)
    - “On second thought, maybe I should keep out of this.” → [farrik_17](#d-farrik_17)

    <span id="d-farrik_15"></span>**`farrik_15`** Farrik: “Whatever, they wouldn't believe you anyway.” — **effects:** sets stage 30 of [Night visit](../quests/farrik.md#stage-30)


    <span id="d-farrik_18"></span>**`farrik_18`** Farrik: “Good.”

    - Next → [farrik_19](#d-farrik_19)

    <span id="d-farrik_17"></span>**`farrik_17`** Farrik: “Sure, it's up to you.”

    - “Good luck on your mission.” → [farrik_14](#d-farrik_14)
    - “Maybe I should tell the guards that you are planning to get him out?” *(if NOT reached stage 20 of [Night visit](../quests/farrik.md#stage-20))* → [farrik_15](#d-farrik_15)

    <span id="d-farrik_19"></span>**`farrik_19`** Farrik: “OK, here is the plan. The guard captain has a bit of a drinking problem.”

    - Next → [farrik_20](#d-farrik_20)

    <span id="d-farrik_20"></span>**`farrik_20`** Farrik: “If we were able to supply him with some mead that we have prepared, we might just be able to sneak our friend out during the night, when the captain is sleeping off the drunkenness.”

    - Next → [farrik_20a](#d-farrik_20a)

    <span id="d-farrik_20a"></span>**`farrik_20a`** Farrik: “Our cook can prepare a special brew of mead for you that will knock him out.”

    - Next → [farrik_21](#d-farrik_21)

    <span id="d-farrik_21"></span>**`farrik_21`** Farrik: “He would probably need to be persuaded to drink on duty too. If that should fail, he could probably be bribed instead.”

    - Next → [farrik_22](#d-farrik_22)

    <span id="d-farrik_22"></span>**`farrik_22`** Farrik: “How does that sound to you? Do you think you are up to it?”

    - “No, this is really starting to sound like a bad idea.” → [farrik_17](#d-farrik_17)
    - “Sure, sounds easy!” *(if NOT reached stage 30 of [Night visit](../quests/farrik.md#stage-30))* → [farrik_23](#d-farrik_23)
    - “Sounds a bit dangerous, but I guess I'll try.” *(if NOT reached stage 30 of [Night visit](../quests/farrik.md#stage-30))* → [farrik_23](#d-farrik_23)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.1](../versions/0.7.1.md) | Dialogue: 1 line changed |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 5 lines changed<br>· text: “Ok, here is the plan. The guard captain has a bit of a drinking probl…” → “OK, here is the plan. The guard captain has a bit of a drinking probl…” |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line added, 7 lines changed<br>· text: “The Fallhaven guard has started to get really annoyed at us lately. P…” → “The Fallhaven guard has started to get really annoyed with us lately.…”<br>· text: “Oh you did? Well done. You have my thanks, friend.” → “That's very useful information. Well done. You have my thanks, friend.” |
| [v0.7.15](../versions/0.7.15.md) | Dialogue: 1 line changed<br>· text: “So did you tell the Warden about our plan then?” → “So did you tell the guard captain about our plan then?” |
| [v0.8.2](../versions/0.8.2.md) | Dialogue: 7 lines added, 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=farrik.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=farrik.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=farrik.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=farrik.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `farrik` · Data from v0.8.18</small>
