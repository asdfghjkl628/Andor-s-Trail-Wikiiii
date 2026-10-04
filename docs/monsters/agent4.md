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

- [blackwater_mountain17](../maps/blackwater_mountain17.md)

## Quests

- [The agent and the beast](../quests/bwm_agent.md): stages 40

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Agent. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/bwm_agent_4_start.json" data-npc="Agent" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-bwm_agent_4_start"></span>**`bwm_agent_4_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 40 of [The agent and the beast](../quests/bwm_agent.md#stage-40))* → [bwm_agent_4_5](#d-bwm_agent_4_5)
    - branch 2 → [bwm_agent_4_1](#d-bwm_agent_4_1)

    <span id="d-bwm_agent_4_5"></span>**`bwm_agent_4_5`** Agent: “Meet me further up the mountain, and we will talk more.” — **effects:** sets stage 40 of [The agent and the beast](../quests/bwm_agent.md#stage-40)

    - “OK, see you there.” → *NPC leaves*

    <span id="d-bwm_agent_4_1"></span>**`bwm_agent_4_1`** Agent: “Hello again. Well done defeating the gornaud beasts.”

    - “Their attacks really hurt. What are these things?” → [bwm_agent_4_6](#d-bwm_agent_4_6)
    - “How come they do not attack you?” → [bwm_agent_4_3](#d-bwm_agent_4_3)
    - “Yeah, no problem. Just another trail of dead bodies behind me.” → [bwm_agent_4_2](#d-bwm_agent_4_2)

    <span id="d-bwm_agent_4_6"></span>**`bwm_agent_4_6`** Agent: “I do not know where they come from. All I know is that they started to appear one day, blocking the path up the mountain.”

    - Next → [bwm_agent_4_7](#d-bwm_agent_4_7)

    <span id="d-bwm_agent_4_3"></span>**`bwm_agent_4_3`** Agent: “Me? There must be something about me that scares them. I have no idea what it would be, some scent perhaps?”

    - Next → [bwm_agent_4_4](#d-bwm_agent_4_4)

    <span id="d-bwm_agent_4_2"></span>**`bwm_agent_4_2`** Agent: “Careful what you wish for, for it may come true.”

    - Next → [bwm_agent_4_4](#d-bwm_agent_4_4)

    <span id="d-bwm_agent_4_7"></span>**`bwm_agent_4_7`** Agent: “And, their attacks are tough. Once one of them gets a hold of you, the other ones seem really eager to hit you too.”

    - “Nothing I can't handle.” → [bwm_agent_4_4](#d-bwm_agent_4_4)
    - “How come they do not attack you?” → [bwm_agent_4_3](#d-bwm_agent_4_3)

    <span id="d-bwm_agent_4_4"></span>**`bwm_agent_4_4`** Agent: “Anyway, we should get going. I'll run ahead of you up the mountain.”

    - Next → [bwm_agent_4_5](#d-bwm_agent_4_5)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed<br>· text: “Hello again. Well done defeating the Gornaud beasts.” → “Hello again. Well done defeating the gornaud beasts.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent4.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `agent4` · Data from v0.8.18</small>
