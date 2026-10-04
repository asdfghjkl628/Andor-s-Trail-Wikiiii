# ![](../assets/icons/monsters/monsters_men_7.png){ .sprite } Fanamor

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

- [crossroads](../maps/crossroads.md)
- [fallhaven_derelict2](../maps/fallhaven_derelict2.md)
- [fallhaven_derelict2_t](../maps/fallhaven_derelict2_t.md)

## Quests

- [Thief apprentice](../quests/Thieves01.md): stages 35, 40, 45, 51, 55

??? quote "Dialogue (39 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-fanamor_selector"></span>**`fanamor_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 55 of [Thief apprentice](../quests/Thieves01.md#stage-55))* → [fanamor_guild_10](#d-fanamor_guild_10)
    - branch 2 *(if reached stage 35 of [Thief apprentice](../quests/Thieves01.md#stage-35); NOT killed 1× [Feygard scout](../monsters/feygard_scout.md))* → [fanamor_guild_5a](#d-fanamor_guild_5a)
    - branch 3 *(if 120 rounds passed since timer “Fanamorbleeding”; reached stage 45 of [Thief apprentice](../quests/Thieves01.md#stage-45))* → [fanamor_guild_0](#d-fanamor_guild_0)
    - branch 4 *(if reached stage 45 of [Thief apprentice](../quests/Thieves01.md#stage-45))* → [fanamor_guild_8](#d-fanamor_guild_8)
    - branch 5 *(if killed 1× [Feygard scout](../monsters/feygard_scout.md); reached stage 40 of [Thief apprentice](../quests/Thieves01.md#stage-40))* → [fanamor_guild_5](#d-fanamor_guild_5)
    - branch 6 *(if reached stage 35 of [Thief apprentice](../quests/Thieves01.md#stage-35); NOT reached stage 40 of [Thief apprentice](../quests/Thieves01.md#stage-40))* → [fanamor_guild_4](#d-fanamor_guild_4)
    - branch 7 → [fanamor](#d-fanamor)

    <span id="d-fanamor_guild_10"></span>**`fanamor_guild_10`** Fanamor: “Hello, friend! Thank you for all you've done for me.”

    - “It was nothing. Bye.” → *conversation ends*
    - “It's my job. Nice to see you survived those anklebiters ...” → *conversation ends*
    - “Hmm, maybe you can help me?” *(if reached stage 150 of [Troubling times](../quests/troubling_times.md#stage-150); NOT reached stage 180 of [Troubling times](../quests/troubling_times.md#stage-180))* → [fanamor_tt](#d-fanamor_tt)

    <span id="d-fanamor_guild_5a"></span>**`fanamor_guild_5a`** Fanamor: “Watch out! Behind you!”

    - “What ...?” → *conversation ends*

    <span id="d-fanamor_guild_0"></span>**`fanamor_guild_0`** Fanamor: “(You look away when you see the corpse of Fanamor. Anklebiters probably had something to do with this horrible event.)” — **effects:** sets stage 51 of [Thief apprentice](../quests/Thieves01.md#stage-51)

    - “[Bury the corpse.]” → [fanamor_guild_0a](#d-fanamor_guild_0a)

    <span id="d-fanamor_guild_8"></span>**`fanamor_guild_8`** Fanamor: “Have you brought me that bandage?”

    - “Yes, I have it!” *(if hand over 1× [Bandage](../items/bandage.md); reached stage 50 of [Thief apprentice](../quests/Thieves01.md#stage-50))* → [fanamor_guild_9a](#d-fanamor_guild_9a)
    - “I'm still searching.” → [fanamor_guild_9b](#d-fanamor_guild_9b)

    <span id="d-fanamor_guild_5"></span>**`fanamor_guild_5`** Fanamor: “Wow, you ... you really got rid of him ....”

    - “Did you doubt me?” → [fanamor_guild_6](#d-fanamor_guild_6)
    - “Yes, even though he was strong, as we can expect of Feygard soldiers ...” → [fanamor_guild_6](#d-fanamor_guild_6)

    <span id="d-fanamor_guild_4"></span>**`fanamor_guild_4`** [Fanamor](../monsters/fanamor.md): “Tsch ... I ... cannot ... You kid, protect the book!”

    - Next → [feygard_scout_3](#d-feygard_scout_3)

    <span id="d-fanamor"></span>**`fanamor`** Fanamor: “Yikes! You scared me there.”

    - Next → [fanamor_1](#d-fanamor_1)

    <span id="d-fanamor_tt"></span>**`fanamor_tt`** Fanamor: “Sure. I heard you're looking for Sly Seraphina.”

    - “Eavesdropping is not nice.” → [fanamor_tt_10](#d-fanamor_tt_10)
    - “Yes. Do you have any idea where she might be hiding?” → [fanamor_tt_20](#d-fanamor_tt_20)

    <span id="d-fanamor_guild_0a"></span>**`fanamor_guild_0a`** *(silent check: the first matching branch below is taken)* — **effects:** removes monsters from crossroads

    - branch 1 → *NPC leaves*

    <span id="d-fanamor_guild_9a"></span>**`fanamor_guild_9a`** Fanamor: “(You help Fanamor put the bandage on the wound) ... I think I will be able ... to move in a few minutes. See you at the Guild. Thank you kid.” — **effects:** sets stage 55 of [Thief apprentice](../quests/Thieves01.md#stage-55), removes monsters from crossroads, spawns monsters on fallhaven_derelict2

    - “I'm glad to hear that. Bye.” → *NPC leaves*
    - “Nothing for me.” → *NPC leaves*

    <span id="d-fanamor_guild_9b"></span>**`fanamor_guild_9b`** Fanamor: “Hurry up! I do not have much time ...”


    <span id="d-fanamor_guild_6"></span>**`fanamor_guild_6`** Fanamor: “Argh ... The Feygard Scout hit me badly. I have not much time ... I am bleeding very heavily.”

    - “I don't think so.” → [fanamor_guild_7a](#d-fanamor_guild_7a)
    - “Can I help?” → [fanamor_guild_7b](#d-fanamor_guild_7b)

    <span id="d-feygard_scout_3"></span>**`feygard_scout_3`** [Feygard scout](../monsters/feygard_scout.md): “(Grabs the book) What have we here? A lost kid trying to do business with this scum, hah? You are under arrest!” — **effects:** sets stage 40 of [Thief apprentice](../quests/Thieves01.md#stage-40)

    - “Not without a fight!” → *fight starts*
    - “How dare you! Prepare to die, useless soldier!” → *fight starts*
    - “For the shadow!” → *fight starts*

    <span id="d-fanamor_1"></span>**`fanamor_1`** Fanamor: “I was just strolling through these woods ... eh ... killing anklebiters.”

    - Next → [fanamor_2](#d-fanamor_2)

    <span id="d-fanamor_tt_10"></span>**`fanamor_tt_10`** Fanamor: “We are thieves - already forgotten?”

    - “So can you help me?” → [fanamor_tt_20](#d-fanamor_tt_20)
    - “Nevertheless, one can still maintain one's good manners.” → [fanamor_tt_12](#d-fanamor_tt_12)

    <span id="d-fanamor_tt_20"></span>**`fanamor_tt_20`** Fanamor: “Of course. In fact, I know exactly where she's hiding right now.”

    - “Great. That will save me a lot of running around.” → [fanamor_tt_22](#d-fanamor_tt_22)

    <span id="d-fanamor_guild_7a"></span>**`fanamor_guild_7a`** Fanamor: “Yes, I am. I have no time for jokes!”

    - Next → [fanamor_guild_7b](#d-fanamor_guild_7b)

    <span id="d-fanamor_guild_7b"></span>**`fanamor_guild_7b`** Fanamor: “I need a bandage quickly, or I will never return to the guild house. A priest might help ...” — **effects:** sets stage 45 of [Thief apprentice](../quests/Thieves01.md#stage-45), starts timer “Fanamorbleeding”

    - “Yeah, OK.” → *conversation ends*
    - “I will find a bandage for you, don't worry.” → *conversation ends*

    <span id="d-fanamor_2"></span>**`fanamor_2`** Fanamor: “Yes. Killing them was what I was doing. Not running away from them. No, killing them.”

    - Next → [fanamor_3](#d-fanamor_3)

    <span id="d-fanamor_tt_12"></span>**`fanamor_tt_12`** Fanamor: “Phh.”


    <span id="d-fanamor_tt_22"></span>**`fanamor_tt_22`** Fanamor: “Here's how we do it: You can guess, and I'll tell you whether it's true or not.”

    - Next → [fanamor_tt_24](#d-fanamor_tt_24)

    <span id="d-fanamor_3"></span>**`fanamor_3`** Fanamor: “*sigh*”

    - Next → [fanamor_4](#d-fanamor_4)

    <span id="d-fanamor_tt_24"></span>**`fanamor_tt_24`** Fanamor: “And each tip only costs you 100 gold pieces.”

    - “I should have known.” → [fanamor_tt_26](#d-fanamor_tt_26)

    <span id="d-fanamor_4"></span>**`fanamor_4`** Fanamor: “Oh, who am I kidding. OK, I was trying to get through the forest here and got ambushed by these anklebiters.”

    - Next → [fanamor_5](#d-fanamor_5)

    <span id="d-fanamor_tt_26"></span>**`fanamor_tt_26`** Fanamor: “You already know that she is near a town.”

    - “But which one?” → [fanamor_tt_30](#d-fanamor_tt_30)

    <span id="d-fanamor_5"></span>**`fanamor_5`** Fanamor: “I won't leave until nightfall, when they can't see me anymore and I might be able to sneak back.”

    - Next → [fanamor_6](#d-fanamor_6)

    <span id="d-fanamor_tt_30"></span>**`fanamor_tt_30`** Fanamor: “Guess!”

    - “Vilegard?” *(if pay 100 gold; faction “tt_hide” = 6)* → [fanamor_tt_40](#d-fanamor_tt_40)
    - “Vilegard?” *(if pay 100 gold; NOT faction “tt_hide” = 6)* → [fanamor_tt_50](#d-fanamor_tt_50)
    - “Brimhaven?” *(if pay 100 gold; faction “tt_hide” = 5)* → [fanamor_tt_40](#d-fanamor_tt_40)
    - “Brimhaven?” *(if pay 100 gold; NOT faction “tt_hide” = 5)* → [fanamor_tt_50](#d-fanamor_tt_50)
    - “Prim?” *(if pay 100 gold; faction “tt_hide” = 4)* → [fanamor_tt_40](#d-fanamor_tt_40)
    - “Prim?” *(if pay 100 gold; NOT faction “tt_hide” = 4)* → [fanamor_tt_50](#d-fanamor_tt_50)
    - “Loneford?” *(if pay 100 gold; faction “tt_hide” = 3)* → [fanamor_tt_40](#d-fanamor_tt_40)
    - “Loneford?” *(if pay 100 gold; NOT faction “tt_hide” = 3)* → [fanamor_tt_50](#d-fanamor_tt_50)
    - “Stoutford?” *(if pay 100 gold; faction “tt_hide” = 2)* → [fanamor_tt_40](#d-fanamor_tt_40)
    - “Stoutford?” *(if pay 100 gold; NOT faction “tt_hide” = 2)* → [fanamor_tt_50](#d-fanamor_tt_50)
    - “Sullengard?” *(if pay 100 gold; faction “tt_hide” = 1)* → [fanamor_tt_40](#d-fanamor_tt_40)
    - “Sullengard?” *(if pay 100 gold; NOT faction “tt_hide” = 1)* → [fanamor_tt_50](#d-fanamor_tt_50)
    - “Oh, I'm running out of gold.” *(if NOT have 100 gold)* → [fanamor_tt_34](#d-fanamor_tt_34)
    - “Enough. I think you don't know yourself.” → [fanamor_tt_32](#d-fanamor_tt_32)

    <span id="d-fanamor_6"></span>**`fanamor_6`** Fanamor: “This is my hiding spot! Now leave me.”

    - “Umar sent me with the words "You are no one.No one knows you.No one has seen you." Now give me the journal please.” *(if reached stage 30 of [Thief apprentice](../quests/Thieves01.md#stage-30))* → [fanamor_guild_1](#d-fanamor_guild_1)

    <span id="d-fanamor_tt_40"></span>**`fanamor_tt_40`** Fanamor: “Hey, that's right!”

    - “Thank you for your help.” → [fanamor_tt_60](#d-fanamor_tt_60)

    <span id="d-fanamor_tt_50"></span>**`fanamor_tt_50`** Fanamor: “Nope - 100 gold. Try again ...”

    - Next → [fanamor_tt_30](#d-fanamor_tt_30)

    <span id="d-fanamor_tt_34"></span>**`fanamor_tt_34`** Fanamor: “No problem. I can wait.”


    <span id="d-fanamor_tt_32"></span>**`fanamor_tt_32`** Fanamor: “You are so smart. I'm sorry I tried.”


    <span id="d-fanamor_guild_1"></span>**`fanamor_guild_1`** Fanamor: “Finally! I was getting tired of waiting here killing these beasts ...”

    - Next → [fanamor_guild_2](#d-fanamor_guild_2)

    <span id="d-fanamor_tt_60"></span>**`fanamor_tt_60`** Fanamor: “Thanks for the gold. But don't tell her that I betrayed her.”


    <span id="d-fanamor_guild_2"></span>**`fanamor_guild_2`** [Fanamor](../monsters/fanamor.md): “Take this. All I've seen is written here ...” — **effects:** sets stage 35 of [Thief apprentice](../quests/Thieves01.md#stage-35), spawns monsters on crossroads

    - Next → [feygard_scout_1](#d-feygard_scout_1)

    <span id="d-feygard_scout_1"></span>**`feygard_scout_1`** [Feygard scout](../monsters/feygard_scout.md): “Halt! You have been caught!”

    - Next → [fanamor_guild_3](#d-fanamor_guild_3)

    <span id="d-fanamor_guild_3"></span>**`fanamor_guild_3`** [Dummy NPC](../monsters/none.md): “In the blink of an eye, Fanamor starts attacking the scout.”

    - Next → [feygard_scout_2](#d-feygard_scout_2)

    <span id="d-feygard_scout_2"></span>**`feygard_scout_2`** [Feygard scout](../monsters/feygard_scout.md): “Argh ... damned trash, take this! (His sword swings quickly, and severely wounds Fanamor)”

    - Next → [fanamor_guild_4](#d-fanamor_guild_4)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed<br>· text: “Oh, who am I kidding. Ok, I was trying to get through the forest here…” → “Oh, who am I kidding. OK, I was trying to get through the forest here…”<br>· text: “.. sigh ..” → “*sigh*” |
| [v0.7.8](../versions/0.7.8.md) | movementAggressionType added (none); phraseID: fanamor → fanamor_selector<br>Dialogue: 19 lines added, 1 line changed |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 2 lines changed<br>· text: “I need a bandage quickly, or I will never return to the guild house.” → “I need a bandage quickly, or I will never return to the guild house. …” |
| [v0.8.13](../versions/0.8.13.md) | Dialogue: 13 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fanamor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fanamor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fanamor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fanamor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `fanamor` · Data from v0.8.18</small>
