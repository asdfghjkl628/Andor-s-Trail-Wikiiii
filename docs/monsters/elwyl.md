# ![](../assets/icons/monsters/monsters_ld1_187.png){ .sprite } Elwyl

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_187.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `elwyl` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Remgard |
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
| [remgard_villager5](../maps/remgard_villager5.md) | Remgard | 1 | – |


## Quests

- [A difference of opinion](../quests/sisterfight.md): stages 20, 30, 31, 70, 71

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Elwyl. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/elwyl.json" data-npc="Elwyl" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (32 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-elwyl"></span>**`elwyl`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 71 of [A difference of opinion](../quests/sisterfight.md#stage-71))* → [elwyl_cmp_1](#d-elwyl_cmp_1)
    - branch 2 *(if reached stage 70 of [A difference of opinion](../quests/sisterfight.md#stage-70))* → [elwyl_res_2](#d-elwyl_res_2)
    - branch 3 *(if reached stage 31 of [A difference of opinion](../quests/sisterfight.md#stage-31))* → [elwyl_pot_1](#d-elwyl_pot_1)
    - branch 4 *(if reached stage 20 of [A difference of opinion](../quests/sisterfight.md#stage-20))* → [elwyl_12](#d-elwyl_12)
    - branch 5 → [elwyl_1](#d-elwyl_1)

    <span id="d-elwyl_cmp_1"></span>**`elwyl_cmp_1`** Elwyl: “Oh, it's you again. Thanks for bringing me that potion earlier.”

    - Next → [elwyl_res_7](#d-elwyl_res_7)

    <span id="d-elwyl_res_2"></span>**`elwyl_res_2`** Elwyl: “Huh, what's this? It's yellow ... I was sure that it used to be blue. Let me smell it to make sure that it's the right kind of potion.”

    - Next → [elwyl_res_3](#d-elwyl_res_3)

    <span id="d-elwyl_pot_1"></span>**`elwyl_pot_1`** Elwyl: “Oh, it's you again. What do you want?”

    - “I have one of those potions of accuracy focus for you.” *(if hand over 1× [Potion of accuracy focus](../items/pot_focus_ac.md))* → [elwyl_res_1](#d-elwyl_res_1)
    - “I have a strong potion of accuracy focus for you.” *(if hand over 1× [Strong potion of accuracy focus](../items/pot_focus_ac2.md))* → [elwyl_res_1](#d-elwyl_res_1)
    - “You talked about some potion before. Could you repeat that?” → [elwyl_12](#d-elwyl_12)
    - “Some people have been complaining that your squabbling has kept them awake at night.” *(if reached stage 10 of [A difference of opinion](../quests/sisterfight.md#stage-10))* → [elwyl_10](#d-elwyl_10)

    <span id="d-elwyl_12"></span>**`elwyl_12`** Elwyl: “Oh, my sister is just so stubborn! You know, last night, I was talking to her about those potions that Hjaldar used to make. The smell from his brewing used to reach into our house here ... or, I mean ... my house here.”

    - Next → [elwyl_13](#d-elwyl_13)

    <span id="d-elwyl_1"></span>**`elwyl_1`** Elwyl: “Who are you? Did we invite you here? No, I didn't think so. Now get out!”

    - “Are you sisters?” → [elwyl_3](#d-elwyl_3)
    - “I go wherever I wish.” → [elwyl_2](#d-elwyl_2)
    - “OK, I'll leave.” → *conversation ends*

    <span id="d-elwyl_res_7"></span>**`elwyl_res_7`** Elwyl: “Hey Elwel, you were wrong all along! Why won't you ever admit it when you are clearly wrong?” — **effects:** sets stage 71 of [A difference of opinion](../quests/sisterfight.md#stage-71)


    <span id="d-elwyl_res_3"></span>**`elwyl_res_3`** Elwyl: “Hmm, yes, it smells exactly as I remember it. It must be the right potion.”

    - Next → [elwyl_res_4](#d-elwyl_res_4)

    <span id="d-elwyl_res_1"></span>**`elwyl_res_1`** Elwyl: “Oh good. Give me that.” — **effects:** sets stage 70 of [A difference of opinion](../quests/sisterfight.md#stage-70)

    - Next → [elwyl_res_2](#d-elwyl_res_2)

    <span id="d-elwyl_10"></span>**`elwyl_10`** Elwyl: “That's what I always tell her, to keep it down. She is insistent on shouting at me when we argue. I guess all of her shouting must have made her more or less deaf, since I also have to shout to her to make her understand.”

    - Next → [elwyl_11](#d-elwyl_11)

    <span id="d-elwyl_13"></span>**`elwyl_13`** Elwyl: “So, I was talking to her about those potions of accuracy focus and how I always thought their blue liquid seemed so odd, since there were no blue things that he used while making them.”

    - Next → [elwyl_14](#d-elwyl_14)

    <span id="d-elwyl_3"></span>**`elwyl_3`** Elwyl: “Yes. Argh. It's not like I am proud of being a sister to ... her.”

    - Next → [elwyl_4](#d-elwyl_4)

    <span id="d-elwyl_2"></span>**`elwyl_2`** Elwyl: “Bah. Leave, before I call the guards over here!”


    <span id="d-elwyl_res_4"></span>**`elwyl_res_4`** Elwyl: “This means ... that Elwel was wrong anyway!”

    - Next → [elwyl_res_5](#d-elwyl_res_5)

    <span id="d-elwyl_11"></span>**`elwyl_11`** Elwyl: “She doesn't stop either. I can't remember for how long this has been going on, it almost feels like forever.” — **effects:** sets stage 20 of [A difference of opinion](../quests/sisterfight.md#stage-20)

    - Next → [elwyl_12](#d-elwyl_12)

    <span id="d-elwyl_14"></span>**`elwyl_14`** Elwyl: “Then all of a sudden, she started arguing with me about how I have things completely wrong. She insists that the potions were green.”

    - Next → [elwyl_15](#d-elwyl_15)

    <span id="d-elwyl_4"></span>**`elwyl_4`** Elwyl: “She is the black sheep of the family. She never agrees to anything, and always complains. Just look at her.”

    - Next → [elwyl_5](#d-elwyl_5)

    <span id="d-elwyl_res_5"></span>**`elwyl_res_5`** Elwyl: “Elwel, look at this, you were wrong! The potion wasn't green as you said, it's yellow! Why didn't you just listen to me?!”

    - Next → [elwyl_res_6](#d-elwyl_res_6)

    <span id="d-elwyl_15"></span>**`elwyl_15`** Elwyl: “I can't understand why she would make such a big deal out of it, when the potion was clearly blue. I remember it distinctly. Argh, how stubborn she is! She wouldn't even admit that she is wrong!” — **effects:** sets stage 30 of [A difference of opinion](../quests/sisterfight.md#stage-30)

    - “Are you sure it was blue?” → [elwyl_16](#d-elwyl_16)
    - “Why make such a big thing out of what color some potion was?” → [elwyl_17](#d-elwyl_17)
    - “Is there anything I can do to help you two?” → [elwyl_18](#d-elwyl_18)

    <span id="d-elwyl_5"></span>**`elwyl_5`** Elwyl: “She even has the stomach to call ME the black sheep of the family, when it is clearly SHE that is causing all the trouble around here.”

    - Next → [elwyl_6](#d-elwyl_6)

    <span id="d-elwyl_res_6"></span>**`elwyl_res_6`** Elwyl: “Elwel, you are always trying your best to prove me wrong. Well look at this, now you are wrong for once!”

    - “Whatever, you two don't seem to get along very well. I'll leave you to your squabbling.” → [elwyl_res_7](#d-elwyl_res_7)
    - “I hope that you two will get along some day.” → [elwyl_res_7](#d-elwyl_res_7)

    <span id="d-elwyl_16"></span>**`elwyl_16`** Elwyl: “Why ... yes ... of course. I am not wrong! They were clearly blue.”

    - “Why make such a big thing out of what color some potion was?” → [elwyl_17](#d-elwyl_17)
    - “Is there anything I can do to help you two?” → [elwyl_18](#d-elwyl_18)

    <span id="d-elwyl_17"></span>**`elwyl_17`** Elwyl: “Exactly. She is clearly wrong, so why won't she just admit it, and we can move along?”

    - “Are you sure it was blue?” → [elwyl_16](#d-elwyl_16)
    - “Is there anything I can do to help you two?” → [elwyl_18](#d-elwyl_18)

    <span id="d-elwyl_18"></span>**`elwyl_18`** Elwyl: “Maybe you could go visit Hjaldar and get one of those potions of accuracy focus, and we can both show her that she is clearly wrong.”

    - Next → [elwyl_19](#d-elwyl_19)

    <span id="d-elwyl_6"></span>**`elwyl_6`** Elwyl: “She's always nagging me about how I should move out of what she considers to be HER house, when it in fact is MY house and SHE is the one that should move out so that things can settle down.”

    - Next → [elwyl_7](#d-elwyl_7)

    <span id="d-elwyl_19"></span>**`elwyl_19`** Elwyl: “His house is up on the northeast shore of town. [Elwyl points outside]”

    - Next → [elwyl_20](#d-elwyl_20)

    <span id="d-elwyl_7"></span>**`elwyl_7`** [Elwel](../monsters/elwel.md): “Ahem. As I've told you several times, Elwyl, since it's YOU that is causing all the trouble, I think it would be best for both our sake if YOU moved out.”

    - Next → [elwyl_8](#d-elwyl_8)

    <span id="d-elwyl_20"></span>**`elwyl_20`** Elwyl: “I'm not sure why he doesn't make those potions anymore though. Maybe he still has some old ones still in supply that you may have?”

    - “I'll return with one of those potions.” → [elwyl_21](#d-elwyl_21)
    - “I am not getting involved in this. You'll have to solve your own conflict.” → [elwyl_22](#d-elwyl_22)

    <span id="d-elwyl_8"></span>**`elwyl_8`** [Elwyl](../monsters/elwyl.md): “Argh. I am so upset at her!”

    - “Good luck with that. I'll leave you to your fighting.” → *conversation ends*
    - “Is there anything I can do to help?” → [elwyl_9](#d-elwyl_9)
    - “Some people have been complaining that your squabbling has kept them awake at night.” *(if reached stage 10 of [A difference of opinion](../quests/sisterfight.md#stage-10))* → [elwyl_10](#d-elwyl_10)

    <span id="d-elwyl_21"></span>**`elwyl_21`** Elwyl: “Good. Maybe when you bring that potion, she will agree to being wrong for once!” — **effects:** sets stage 31 of [A difference of opinion](../quests/sisterfight.md#stage-31)


    <span id="d-elwyl_22"></span>**`elwyl_22`** Elwyl: “Bah, you kids are never good for anything.”


    <span id="d-elwyl_9"></span>**`elwyl_9`** Elwyl: “Yes, you can leave! I never invited you here. Leave, before I call the guards!”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.1](../versions/0.7.1.md) | Dialogue: 1 line added, 2 lines changed |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 11 lines changed<br>· text: “Oh, my sister is just so stubborn! You know, last night, I was talkin…” → “Oh, my sister is just so stubborn! You know, last night, I was talkin…”<br>· text: “This means .. that Elwel was wrong anyway!” → “This means ... that Elwel was wrong anyway!” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elwyl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elwyl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elwyl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elwyl.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `elwyl` |
    | Spawn group | `elwyl` |
    | Loot table | – |
    | Conversation | `elwyl` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:187` |
    | Defined in | `res/raw/monsterlist_v0611_npcs2.json` |

    Raw data:

    ```json
    {
     "id": "elwyl",
     "name": "Elwyl",
     "iconID": "monsters_ld1:187",
     "monsterClass": "humanoid",
     "spawnGroup": "elwyl",
     "phraseID": "elwyl"
    }
    ```


<small>Data from v0.8.18</small>
