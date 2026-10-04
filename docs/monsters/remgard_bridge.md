# ![](../assets/icons/monsters/monsters_men2_4.png){ .sprite } Bridge lookout

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

- [mountainlake13a](../maps/mountainlake13a.md)

## Quests

- [Everything in order](../quests/remgard.md): stages 10, 15, 20, 30, 31, 35

??? quote "Dialogue (28 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-remgard_bridge"></span>**`remgard_bridge`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 35 of [Everything in order](../quests/remgard.md#stage-35))* → [remgardb_helped_1](#d-remgardb_helped_1)
    - branch 2 *(if reached stage 31 of [Everything in order](../quests/remgard.md#stage-31))* → [remgardb_helped_n](#d-remgardb_helped_n)
    - branch 3 *(if reached stage 30 of [Everything in order](../quests/remgard.md#stage-30))* → [remgardb_helped_y](#d-remgardb_helped_y)
    - branch 4 *(if reached stage 20 of [Everything in order](../quests/remgard.md#stage-20))* → [remgardb_help_return](#d-remgardb_help_return)
    - branch 5 → [remgardb_1](#d-remgardb_1)

    <span id="d-remgardb_helped_1"></span>**`remgardb_helped_1`** Bridge lookout: “You should go visit our village elder, Jhaeld, and talk to him about what we should do next. I will let you enter Remgard to speak to him.” — **effects:** sets stage 35 of [Everything in order](../quests/remgard.md#stage-35)

    - Next → [remgardb_helped_2](#d-remgardb_helped_2)

    <span id="d-remgardb_helped_n"></span>**`remgardb_helped_n`** Bridge lookout: “Thank you for scouting that cabin. It's a relief to hear that it is empty. Our fears might not be true then after all.” — **effects:** sets stage 31 of [Everything in order](../quests/remgard.md#stage-31)

    - “You are welcome. Anything else I can help you with?” → [remgardb_helped_n_2](#d-remgardb_helped_n_2)
    - “You are welcome. Now, about that reward?” → [remgardb_helped_n_3](#d-remgardb_helped_n_3)

    <span id="d-remgardb_helped_y"></span>**`remgardb_helped_y`** Bridge lookout: “Algangror, sigh. Then it is as we feared. This is terrible news.” — **effects:** sets stage 30 of [Everything in order](../quests/remgard.md#stage-30)

    - Next → [remgardb_helped_1](#d-remgardb_helped_1)

    <span id="d-remgardb_help_return"></span>**`remgardb_help_return`** Bridge lookout: “Did you find anything in that abandoned house?”

    - “Not yet. What was I supposed to do again?” → [remgardb_help_2b](#d-remgardb_help_2b)
    - “Not yet, I am still working on it.” → [remgardb_help_10](#d-remgardb_help_10)
    - “There is a woman called Algangror in the cabin.” *(if reached stage 10 of [Of mice and men](../quests/algangror.md#stage-10))* → [remgardb_helped_y](#d-remgardb_helped_y)
    - “Yes, I have been there, but the cabin was empty.” *(if reached stage 10 of [Of mice and men](../quests/algangror.md#stage-10))* → [remgardb_helped_n](#d-remgardb_helped_n)

    <span id="d-remgardb_1"></span>**`remgardb_1`** Bridge lookout: “Halt! No one is allowed to enter or exit Remgard.”

    - “Why? Is there something wrong?” → [remgardb_2](#d-remgardb_2)

    <span id="d-remgardb_helped_2"></span>**`remgardb_helped_2`** Bridge lookout: “You can probably find him in the tavern to the southeast, since that's where he spends most of his time.”

    - “I will go see him.” → *NPC leaves*

    <span id="d-remgardb_helped_n_2"></span>**`remgardb_helped_n_2`** Bridge lookout: “I guess you have proven yourself to be useful. We might have more work for you if you are interested.”

    - Next → [remgardb_helped_1](#d-remgardb_helped_1)

    <span id="d-remgardb_helped_n_3"></span>**`remgardb_helped_n_3`** Bridge lookout: “No no, we did not discuss any reward. But there might be one for you if you are willing to help us further.”

    - Next → [remgardb_helped_1](#d-remgardb_helped_1)

    <span id="d-remgardb_help_2b"></span>**`remgardb_help_2b`** Bridge lookout: “There is an abandoned house some way to the east of here, on a peninsula on the northern shore of lake Laeroth.”

    - Next → [remgardb_help_3](#d-remgardb_help_3)

    <span id="d-remgardb_help_10"></span>**`remgardb_help_10`** Bridge lookout: “Excellent. Report back as soon as possible.” — **effects:** sets stage 20 of [Everything in order](../quests/remgard.md#stage-20)


    <span id="d-remgardb_2"></span>**`remgardb_2`** Bridge lookout: “Wrong? You bet there is. Several of the townspeople have disappeared, and we are still conducting the investigation.”

    - Next → [remgardb_3](#d-remgardb_3)

    <span id="d-remgardb_help_3"></span>**`remgardb_help_3`** Bridge lookout: “We have reason to believe that this cabin is inhabited by someone, since we have seen candlelight coming from there during the night across the lake. We are not certain though, it could just be the moonlight on the water.”

    - Next → [remgardb_help_4](#d-remgardb_help_4)

    <span id="d-remgardb_3"></span>**`remgardb_3`** Bridge lookout: “We are searching for them in the town, and questioning everyone for clues on where they might be.” — **effects:** sets stage 10 of [Everything in order](../quests/remgard.md#stage-10)

    - “Please continue.” → [remgardb_5](#d-remgardb_5)
    - “Maybe they just left?” → [remgardb_4](#d-remgardb_4)

    <span id="d-remgardb_help_4"></span>**`remgardb_help_4`** Bridge lookout: “That's where you come in, and might be able to help us.”

    - Next → [remgardb_help_5](#d-remgardb_help_5)

    <span id="d-remgardb_5"></span>**`remgardb_5`** Bridge lookout: “Considering our town is surrounded by lake Laeroth, we guards are able to keep a watchful eye on everything going on here. We are able to keep a log of who comes and goes, since this bridge is our only connection to the mainland.”

    - Next → [remgardb_6](#d-remgardb_6)

    <span id="d-remgardb_4"></span>**`remgardb_4`** Bridge lookout: “No, I highly doubt that.”

    - Next → [remgardb_5](#d-remgardb_5)

    <span id="d-remgardb_help_5"></span>**`remgardb_help_5`** Bridge lookout: “I must stay here and guard the bridge, but you could go over there and peek inside.”

    - Next → [remgardb_help_6](#d-remgardb_help_6)

    <span id="d-remgardb_6"></span>**`remgardb_6`** Bridge lookout: “For your sake, it is probably safer for you to remain out of town until our investigation is complete.”

    - “I am willing to help you with the investigation if you want.” → [remgardb_help_1](#d-remgardb_help_1)
    - “OK, I will leave you to your investigation.” → *conversation ends*
    - “How about you allow me to enter town anyway, so that I can trade. I promise to be quick.” → [remgardb_7](#d-remgardb_7)

    <span id="d-remgardb_help_6"></span>**`remgardb_help_6`** Bridge lookout: “Now, I must warn you - this could be dangerous. If it is as we suspected, then the person in the cabin could be a ... shall we say ... persuasive talker.”

    - Next → [remgardb_help_7](#d-remgardb_help_7)

    <span id="d-remgardb_help_1"></span>**`remgardb_help_1`** Bridge lookout: “Hmm, yes, that might be a good idea actually. Considering you made it up here, you must have some knowledge of the surroundings.” — **effects:** sets stage 15 of [Everything in order](../quests/remgard.md#stage-15)

    - Next → [remgardb_help_2](#d-remgardb_help_2)

    <span id="d-remgardb_7"></span>**`remgardb_7`** Bridge lookout: “No. As I said, no one except us guards are allowed to enter or exit town until our investigation is completed. I suggest you leave now.”


    <span id="d-remgardb_help_7"></span>**`remgardb_help_7`** Bridge lookout: “So, if you really want to help us, the task I ask of you is that you only peek inside that cabin and identify if there's anyone there, and if so who that might be.”

    - Next → [remgardb_help_8](#d-remgardb_help_8)

    <span id="d-remgardb_help_2"></span>**`remgardb_help_2`** Bridge lookout: “Tell you what. You might be able to help us.”

    - Next → [remgardb_help_2b](#d-remgardb_help_2b)

    <span id="d-remgardb_help_8"></span>**`remgardb_help_8`** Bridge lookout: “Report back to me as soon as possible, and do not speak for too long with anyone that might be there.”

    - Next → [remgardb_help_9s](#d-remgardb_help_9s)

    <span id="d-remgardb_help_9s"></span>**`remgardb_help_9s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Everything in order](../quests/remgard.md#stage-20))* → *conversation ends*
    - branch 2 → [remgardb_help_9](#d-remgardb_help_9)

    <span id="d-remgardb_help_9"></span>**`remgardb_help_9`** Bridge lookout: “Would you be willing to do this task for us?”

    - “Sure, I would be happy to help.” → [remgardb_help_10](#d-remgardb_help_10)
    - “I'll do it. I sure hope there will be some reward for this though.” → [remgardb_help_10](#d-remgardb_help_10)
    - “No way, this sounds way too dangerous for me.” → [remgardb_help_9d](#d-remgardb_help_9d)
    - “Actually, I have already been there. There is a woman called Algangror in the cabin.” *(if reached stage 10 of [Of mice and men](../quests/algangror.md#stage-10))* → [remgardb_helped_y](#d-remgardb_helped_y)
    - “Actually, I have already been there, but the cabin was empty.” *(if reached stage 10 of [Of mice and men](../quests/algangror.md#stage-10))* → [remgardb_helped_n](#d-remgardb_helped_n)

    <span id="d-remgardb_help_9d"></span>**`remgardb_help_9d`** Bridge lookout: “I don't blame you for declining. After all, it could be a dangerous task. Didn't hurt to ask though.”




## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=remgard_bridge.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=remgard_bridge.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=remgard_bridge.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=remgard_bridge.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `remgard_bridge` · Data from v0.8.18</small>
