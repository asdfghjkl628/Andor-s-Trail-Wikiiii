# ![](../assets/icons/monsters/monsters_men_3.png){ .sprite } Guard captain

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

- [fallhaven_prison](../maps/fallhaven_prison.md)

## Quests

- [A path to the Duleian Road](../quests/pathway_fallhaven.md): stages 20
- [Night visit](../quests/farrik.md): stages 32, 40, 50, 60, 90

??? quote "Dialogue (31 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-fallhaven_warden_select_1"></span>**`fallhaven_warden_select_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [Night visit](../quests/farrik.md#stage-60))* → [fallhaven_warden_11](#d-fallhaven_warden_11)
    - branch 2 *(if reached stage 90 of [Night visit](../quests/farrik.md#stage-90))* → [fallhaven_warden_35](#d-fallhaven_warden_35)
    - branch 3 → [fallhaven_warden_select_2](#d-fallhaven_warden_select_2)

    <span id="d-fallhaven_warden_11"></span>**`fallhaven_warden_11`** Guard captain: “Hello again, kid. Thanks for the drink earlier. I had it all in one go. It sure tasted a bit different than before, but I guess that is just because I'm not used to it anymore.”

    - “That's great! Cheers!” → *conversation ends*
    - “I recently talked to the watchman who blocks the old pathway to the Duleian Road. Why don't you just pay the woodcutter?” *(if latest stage of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-10) is 10)* → [fallhaven_warden_pathway_1](#d-fallhaven_warden_pathway_1)

    <span id="d-fallhaven_warden_35"></span>**`fallhaven_warden_35`** Guard captain: “Hello again, my friend. Thank you for your help in dealing with the thieves earlier.”

    - Next → [fallhaven_warden_36](#d-fallhaven_warden_36)

    <span id="d-fallhaven_warden_select_2"></span>**`fallhaven_warden_select_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [Night visit](../quests/farrik.md#stage-50))* → [fallhaven_warden_30](#d-fallhaven_warden_30)
    - branch 2 *(if reached stage 32 of [Night visit](../quests/farrik.md#stage-32))* → [fallhaven_warden_12](#d-fallhaven_warden_12)
    - branch 3 → [fallhaven_warden](#d-fallhaven_warden)

    <span id="d-fallhaven_warden_pathway_1"></span>**`fallhaven_warden_pathway_1`** Guard captain: “Hah! Jakrar? I should pay Jakrar before he has done his work? No way! Either he does his woodcutting job before I pay him or the passage stays blocked! That's how I always do it. It's the only way to get the job done well.”

    - “Would anything change your mind?” → [fallhaven_warden_pathway_2](#d-fallhaven_warden_pathway_2)

    <span id="d-fallhaven_warden_36"></span>**`fallhaven_warden_36`** Guard captain: “I will make sure to tell other guards how you helped us here in Fallhaven.”

    - “Thank you. Goodbye.” → *conversation ends*
    - “I recently talked to the watchman who blocks the old pathway to the Duleian Road. Why don't you just pay the woodcutter?” *(if latest stage of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-10) is 10)* → [fallhaven_warden_pathway_1](#d-fallhaven_warden_pathway_1)

    <span id="d-fallhaven_warden_30"></span>**`fallhaven_warden_30`** Guard captain: “Hello again, my friend. Did you tell those thieves that we will lower our security tonight?”

    - “Yes, they won't expect a thing.” *(if reached stage 80 of [Night visit](../quests/farrik.md#stage-80))* → [fallhaven_warden_31](#d-fallhaven_warden_31)
    - “No, not yet. I'm working on it.” → [fallhaven_warden_25](#d-fallhaven_warden_25)

    <span id="d-fallhaven_warden_12"></span>**`fallhaven_warden_12`** Guard captain: “Hello again, kid. Thanks for the drink earlier. I still haven't had it.”

    - Next → [fallhaven_warden_5](#d-fallhaven_warden_5)

    <span id="d-fallhaven_warden"></span>**`fallhaven_warden`** Guard captain: “State your business.”

    - “Who is that prisoner?” → [warden_prisoner_1](#d-warden_prisoner_1)
    - “I heard that you are fond of mead.” *(if reached stage 20 of [Night visit](../quests/farrik.md#stage-20))* → [fallhaven_warden_1](#d-fallhaven_warden_1)
    - “The thieves are planning an escape for their friend.” *(if reached stage 30 of [Night visit](../quests/farrik.md#stage-30))* → [fallhaven_warden_20](#d-fallhaven_warden_20)
    - “I recently talked to the watchman who blocks the old pathway to the Duleian Road. Why don't you just pay the woodcutter?” *(if latest stage of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-10) is 10)* → [fallhaven_warden_pathway_1](#d-fallhaven_warden_pathway_1)

    <span id="d-fallhaven_warden_pathway_2"></span>**`fallhaven_warden_pathway_2`** Guard captain: “No way! Get lost or I'll throw you in jail! Talk to that filthy woodcutter if you want to reopen the path, but nothing will change my mind!”

    - “So where can I find him?” → [fallhaven_warden_pathway_3](#d-fallhaven_warden_pathway_3)

    <span id="d-fallhaven_warden_31"></span>**`fallhaven_warden_31`** Guard captain: “Great. Thank you for your help. Here, take these coins as a token of our appreciation.” — **effects:** sets stage 90 of [Night visit](../quests/farrik.md#stage-90), gives [Gold coins](../items/gold.md)

    - Next → [fallhaven_warden_36](#d-fallhaven_warden_36)

    <span id="d-fallhaven_warden_25"></span>**`fallhaven_warden_25`** Guard captain: “Good. Report back to me when you have told them.” — **effects:** sets stage 50 of [Night visit](../quests/farrik.md#stage-50)

    - “Will do.” → *conversation ends*

    <span id="d-fallhaven_warden_5"></span>**`fallhaven_warden_5`** Guard captain: “I could get fined for drinking on duty. I don't think I would dare try it right now.”

    - Next → [fallhaven_warden_6](#d-fallhaven_warden_6)

    <span id="d-warden_prisoner_1"></span>**`warden_prisoner_1`** Guard captain: “That thief? He was caught in the act. Trespassing he was. Trying to get down into the catacombs of Fallhaven church.”

    - Next → [warden_prisoner_2](#d-warden_prisoner_2)

    <span id="d-fallhaven_warden_1"></span>**`fallhaven_warden_1`** Guard captain: “Mead? Oh ... no, I don't do that anymore. Who told you that?”

    - Next → [fallhaven_warden_2](#d-fallhaven_warden_2)

    <span id="d-fallhaven_warden_20"></span>**`fallhaven_warden_20`** Guard captain: “Really, they would dare go up against the guard in Fallhaven? Do you have any details on their plan?”

    - “I heard they are planning his escape tonight.” → [fallhaven_warden_21](#d-fallhaven_warden_21)
    - “No, I was just kidding with you. Never mind.” → *conversation ends*
    - “On second thought, I better not upset the Thieves' Guild. Never mind I said anything.” → *conversation ends*

    <span id="d-fallhaven_warden_pathway_3"></span>**`fallhaven_warden_pathway_3`** Guard captain: “He lives in his hut, immediately south of my prison. Don't you bother me again!” — **effects:** sets stage 20 of [A path to the Duleian Road](../quests/pathway_fallhaven.md#stage-20)

    - “Easy. Easy. I'm already leaving.” → *conversation ends*
    - “I wanted to leave your shabby prison anyway.” → *conversation ends*

    <span id="d-fallhaven_warden_6"></span>**`fallhaven_warden_6`** Guard captain: “Thank you for the drink though, I will enjoy it when I get home later tomorrow.”

    - “You are welcome. Goodbye.” → *conversation ends*
    - “What if someone would pay you the amount of the fine?” → [fallhaven_warden_7](#d-fallhaven_warden_7)

    <span id="d-warden_prisoner_2"></span>**`warden_prisoner_2`** Guard captain: “Luckily, we caught him before he could get down there. Now he'll serve as an example to all other thieves.”

    - Next → [warden_prisoner_3](#d-warden_prisoner_3)

    <span id="d-fallhaven_warden_2"></span>**`fallhaven_warden_2`** Guard captain: “I've stopped doing that years ago.”

    - “Sounds like a good approach. Good luck with keeping away from it.” → *conversation ends*
    - “Not just even a little bit?” → [fallhaven_warden_3](#d-fallhaven_warden_3)

    <span id="d-fallhaven_warden_21"></span>**`fallhaven_warden_21`** Guard captain: “Tonight? Thank you for this information. We will make sure to increase the security tonight then, but in such a way that they won't notice.” — **effects:** sets stage 40 of [Night visit](../quests/farrik.md#stage-40)

    - Next → [fallhaven_warden_22](#d-fallhaven_warden_22)

    <span id="d-fallhaven_warden_7"></span>**`fallhaven_warden_7`** Guard captain: “Oh, that sounds a bit shady. I doubt anyone could afford the 450 gold around here. Anyway, I would need a bit more than that just to risk it.”

    - “I have 500 gold right here that you could have.” *(if pay 500 gold)* → [fallhaven_warden_9](#d-fallhaven_warden_9)
    - “You know you want the mead right?” → [fallhaven_warden_8](#d-fallhaven_warden_8)
    - “Yes, I agree. This is starting to sound too shady. Goodbye.” → *conversation ends*

    <span id="d-warden_prisoner_3"></span>**`warden_prisoner_3`** Guard captain: “Damn thieves. There must be a nest of them around here somewhere. If only I could find where they hide.”


    <span id="d-fallhaven_warden_3"></span>**`fallhaven_warden_3`** Guard captain: “Um. *clears throat* I really shouldn't.”

    - “I brought some with me if you would like to have a sip.” *(if reached stage 25 of [Night visit](../quests/farrik.md#stage-25); hand over 1× [Prepared sleepy mead](../items/sleepingmead.md))* → [fallhaven_warden_4](#d-fallhaven_warden_4)
    - “OK, goodbye.” → *conversation ends*

    <span id="d-fallhaven_warden_22"></span>**`fallhaven_warden_22`** Guard captain: “When they do decide to break him free, we will be prepared. Maybe we can arrest more of those filthy thieves.”

    - Next → [fallhaven_warden_23](#d-fallhaven_warden_23)

    <span id="d-fallhaven_warden_9"></span>**`fallhaven_warden_9`** Guard captain: “Wow, that much gold? I'm sure I could even get away with this without being fined. Then I could have the gold AND a nice drink of mead at the same time.” — **effects:** sets stage 60 of [Night visit](../quests/farrik.md#stage-60)

    - Next → [fallhaven_warden_10](#d-fallhaven_warden_10)

    <span id="d-fallhaven_warden_8"></span>**`fallhaven_warden_8`** Guard captain: “Oh sure. Now that you mention it. It sure would be good.”

    - “So what if I pay you, say, 400 gold. Would that cover enough of your anxiety to enjoy the drink now?” *(if pay 400 gold)* → [fallhaven_warden_9](#d-fallhaven_warden_9)
    - “This is starting to sound too shady for me. I'll leave you to your duty, goodbye.” → *conversation ends*
    - “I'll go get that gold for you. Goodbye.” → *conversation ends*

    <span id="d-fallhaven_warden_4"></span>**`fallhaven_warden_4`** Guard captain: “Oh sweet drinks of joy. I really shouldn't have this while on duty though.” — **effects:** sets stage 32 of [Night visit](../quests/farrik.md#stage-32)

    - Next → [fallhaven_warden_5](#d-fallhaven_warden_5)

    <span id="d-fallhaven_warden_23"></span>**`fallhaven_warden_23`** Guard captain: “Thank you again for the information. I'm not sure how you may know this, but I really appreciate you telling me.”

    - Next → [fallhaven_warden_24](#d-fallhaven_warden_24)

    <span id="d-fallhaven_warden_10"></span>**`fallhaven_warden_10`** Guard captain: “Thank you kid, you really are nice. Now leave me to enjoy my drink.”


    <span id="d-fallhaven_warden_24"></span>**`fallhaven_warden_24`** Guard captain: “I want you to go one step further and tell them that we will have less security for tonight. But instead we will increase the security. That way we can really be ready for them.”

    - “Sure, I can do that.” → [fallhaven_warden_25](#d-fallhaven_warden_25)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines added, 10 lines changed<br>· text: “I want you to go one step further and tell them that we will have les…” → “I want you to go one step further and tell them that we will have les…”<br>· text: “Mead? Oh.. no, I don't do that anymore. Who told you that?” → “Mead? Oh ... no, I don't do that anymore. Who told you that?” |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed<br>· text: “Thank you again for the information. While I'm not sure how you may k…” → “Thank you again for the information. I'm not sure how you may know th…” |
| [v0.7.15](../versions/0.7.15.md) | name: Warden → Guard captain |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=warden.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=warden.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=warden.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=warden.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `warden` · Data from v0.8.18</small>
