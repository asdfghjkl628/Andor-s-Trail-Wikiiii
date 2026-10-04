# ![](../assets/icons/monsters/monsters_men_4.png){ .sprite } Agent

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

- [blackwater_mountain14](../maps/blackwater_mountain14.md)

## Quests

- [The agent and the beast](../quests/bwm_agent.md): stages 30

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Agent. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/bwm_agent_3_start.json" data-npc="Agent" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-bwm_agent_3_start"></span>**`bwm_agent_3_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [The agent and the beast](../quests/bwm_agent.md#stage-30))* → [bwm_agent_3_4](#d-bwm_agent_3_4)
    - branch 2 → [bwm_agent_3_1](#d-bwm_agent_3_1)

    <span id="d-bwm_agent_3_4"></span>**`bwm_agent_3_4`** Agent: “Beware of the nasty monsters, they can really cause some harm!” — **effects:** sets stage 30 of [The agent and the beast](../quests/bwm_agent.md#stage-30)

    - “OK, I will follow this path up the mountain.” → *NPC leaves*
    - “Great, more monsters. Just what I needed.” → *NPC leaves*

    <span id="d-bwm_agent_3_1"></span>**`bwm_agent_3_1`** Agent: “Hello. You made it here, good.”

    - “I talked to some people in the village Prim. They had some interesting things to say about Blackwater mountain.” *(if reached stage 25 of [The agent and the beast](../quests/bwm_agent.md#stage-25))* → [bwm_agent_3_5](#d-bwm_agent_3_5)
    - “I went east, as you said.” → [bwm_agent_3_2](#d-bwm_agent_3_2)

    <span id="d-bwm_agent_3_5"></span>**`bwm_agent_3_5`** Agent: “Do not listen to their lies. They poison your thoughts and would not hesitate to stab you in the back once they get the chance.”

    - “What have they done?” → [bwm_agent_3_6](#d-bwm_agent_3_6)
    - “Yes, they do seem a bit shady.” → [bwm_agent_3_7](#d-bwm_agent_3_7)

    <span id="d-bwm_agent_3_2"></span>**`bwm_agent_3_2`** Agent: “Good. Now let's get up this mountain. I will meet you halfway up there.”

    - Next → [bwm_agent_3_3](#d-bwm_agent_3_3)

    <span id="d-bwm_agent_3_6"></span>**`bwm_agent_3_6`** Agent: “I will not talk of them now. Follow me up to the Blackwater mountain settlement and we will talk more there.”

    - “Sure.” → [bwm_agent_3_2](#d-bwm_agent_3_2)
    - “I'm keeping my eye on you. But I'll agree to your terms for now.” → [bwm_agent_3_2](#d-bwm_agent_3_2)

    <span id="d-bwm_agent_3_7"></span>**`bwm_agent_3_7`** Agent: “Indeed they do.”

    - Next → [bwm_agent_3_6](#d-bwm_agent_3_6)

    <span id="d-bwm_agent_3_3"></span>**`bwm_agent_3_3`** Agent: “This path leads up to the Blackwater mountain settlement. Follow this path and we will talk later.”

    - Next → [bwm_agent_3_4](#d-bwm_agent_3_4)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `agent3` · Data from v0.8.18</small>
