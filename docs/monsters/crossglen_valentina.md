# ![](../assets/icons/monsters/monsters_ld1_167.png){ .sprite } Valentina

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

- [home](../maps/home.md)

## Quests

- [Search for Andor](../quests/andor.md): stages 110

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Valentina. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/crossglen_valentina_selector.json" data-npc="Valentina" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (12 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-crossglen_valentina_selector"></span>**`crossglen_valentina_selector`** *(silent check: the first matching branch below is taken)*

    - “Can we talk about Andor?” *(if reached stage 26 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-26))* → [crossglen_valentina_andor_10](#d-crossglen_valentina_andor_10)
    - “I would like to learn more about Aunt Valeria.” *(if reached stage 26 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-26))* → [crossglen_valentina_valeria_10](#d-crossglen_valentina_valeria_10)
    - “What's wrong?” → [crossglen_valentina_10](#d-crossglen_valentina_10)

    <span id="d-crossglen_valentina_andor_10"></span>**`crossglen_valentina_andor_10`** Valentina: “I should be able to help you, but first you have to tell me where have you been?”

    - “I've traveled great distances from home and have seen my fair share of Dhayavar during my search for Andor.” *(if reached stage 72 of [Search for Andor](../quests/andor.md#stage-72); reached stage 85 of [Search for Andor](../quests/andor.md#stage-85); reached stage 170 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-170); reached stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60))* → [crossglen_valentina_andor_20](#d-crossglen_valentina_andor_20)
    - “I've been around a lot of Dhayavar and have spoken to a lot of people about Andor.” *(if reached stage 72 of [Search for Andor](../quests/andor.md#stage-72); reached stage 85 of [Search for Andor](../quests/andor.md#stage-85); reached stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60))* → [crossglen_valentina_andor_20](#d-crossglen_valentina_andor_20)
    - “I've talked with a potion maker.” *(if reached stage 72 of [Search for Andor](../quests/andor.md#stage-72); NOT reached stage 85 of [Search for Andor](../quests/andor.md#stage-85); NOT reached stage 170 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-170); NOT reached stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60))* → [crossglen_valentina_andor_21](#d-crossglen_valentina_andor_21)
    - “I've been to Remgard looking for Andor” *(if NOT reached stage 72 of [Search for Andor](../quests/andor.md#stage-72); NOT reached stage 85 of [Search for Andor](../quests/andor.md#stage-85); reached stage 170 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-170); NOT reached stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60))* → [crossglen_valentina_andor_21](#d-crossglen_valentina_andor_21)
    - “I've been to this really cool place called Blackwater settlement.” *(if NOT reached stage 72 of [Search for Andor](../quests/andor.md#stage-72); NOT reached stage 85 of [Search for Andor](../quests/andor.md#stage-85); NOT reached stage 170 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-170); reached stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60))* → [crossglen_valentina_andor_21](#d-crossglen_valentina_andor_21)
    - “I've not gone much past Sullengard.” *(if NOT reached stage 85 of [Search for Andor](../quests/andor.md#stage-85); NOT reached stage 72 of [Search for Andor](../quests/andor.md#stage-72); NOT reached stage 170 of [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-170); NOT reached stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60))* → [crossglen_valentina_andor_21](#d-crossglen_valentina_andor_21)
    - “I've been running around a lot, but I've not learned much.” → [crossglen_valentina_andor_21](#d-crossglen_valentina_andor_21)

    <span id="d-crossglen_valentina_valeria_10"></span>**`crossglen_valentina_valeria_10`** Valentina: “Right now? No. I am not ready to discuss this with you.”

    - “Well, I look forward to a time where you will be ready.” → *conversation ends*

    <span id="d-crossglen_valentina_10"></span>**`crossglen_valentina_10`** Valentina: “Do you really need to ask me that? Please leave my house and come back when I have calmed down.”

    - “OK mother.” → *conversation ends*

    <span id="d-crossglen_valentina_andor_20"></span>**`crossglen_valentina_andor_20`** Valentina: “I see my child. I can also see that your confidence and skills have grown tremendously, but tell me, with all this adventuring, have you been to Brightport yet?”

    - “[While holding back a smirk, you lie] Yes, why?” → [crossglen_valentina_andor_25](#d-crossglen_valentina_andor_25)
    - “No. Should I have?” → [crossglen_valentina_andor_30](#d-crossglen_valentina_andor_30)

    <span id="d-crossglen_valentina_andor_21"></span>**`crossglen_valentina_andor_21`** Valentina: “I see my child. Tell me, with your limited adventuring, have you made it to Brightport yet?”

    - “No. Should I have?” → [crossglen_valentina_andor_30](#d-crossglen_valentina_andor_30)
    - “[While holding back a smirk, you lie] Yes, why?” → [crossglen_valentina_andor_25](#d-crossglen_valentina_andor_25)

    <span id="d-crossglen_valentina_andor_25"></span>**`crossglen_valentina_andor_25`** Valentina: “Don't you remember who lives there?”

    - “Umm...no, no I don't.” → [crossglen_valentina_andor_40](#d-crossglen_valentina_andor_40)

    <span id="d-crossglen_valentina_andor_30"></span>**`crossglen_valentina_andor_30`** Valentina: “What? Why not? Don't you remember who lives there?”

    - “Umm...no, no I don't.” → [crossglen_valentina_andor_40](#d-crossglen_valentina_andor_40)

    <span id="d-crossglen_valentina_andor_40"></span>**`crossglen_valentina_andor_40`** Valentina: “Andor's best friend from school, Stanwick. If you remember, they are very close friends. Maybe Stanwick has seen Andor?”

    - “Oh, Stanwick, of course.” → [crossglen_valentina_andor_50](#d-crossglen_valentina_andor_50)
    - “Stanwick? I never liked that kid. He's really annoying and always picked on me. I really don't want to talk to him.” → [crossglen_valentina_andor_50](#d-crossglen_valentina_andor_50)
    - “Are you sure that this is worth it? All the information that I have is pointing me to Nor City.” *(if reached stage 80 of [Search for Andor](../quests/andor.md#stage-80))* → [crossglen_valentina_andor_55](#d-crossglen_valentina_andor_55)

    <span id="d-crossglen_valentina_andor_50"></span>**`crossglen_valentina_andor_50`** Valentina: “Yes, I think you should go to Brightport and seek him out. Maybe, just maybe, he could be helpful to us for once.” — **effects:** sets stage 110 of [Search for Andor](../quests/andor.md#stage-110)

    - “Thanks, mother. I will go to Brightport next.” → *conversation ends*

    <span id="d-crossglen_valentina_andor_55"></span>**`crossglen_valentina_andor_55`** Valentina: “Nor City?! What do you know about Nor City?”

    - “Well, I know there is a lady named 'Lydalon' there.” → [crossglen_valentina_andor_60](#d-crossglen_valentina_andor_60)

    <span id="d-crossglen_valentina_andor_60"></span>**`crossglen_valentina_andor_60`** Valentina: “Oh, OK. Just be careful there. Anyways...”

    - Next → [crossglen_valentina_andor_50](#d-crossglen_valentina_andor_50)



## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 11 lines added |
| [v0.8.4](../versions/0.8.4.md) | Dialogue: 1 line added, 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossglen_valentina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossglen_valentina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossglen_valentina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossglen_valentina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `crossglen_valentina` · Data from v0.8.18</small>
