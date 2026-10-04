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

- [blackwater_mountain38](../maps/blackwater_mountain38.md)

## Quests

- [The agent and the beast](../quests/bwm_agent.md): stages 60

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-bwm_agent_6_start"></span>**`bwm_agent_6_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60))* → [bwm_agent_6_3](#d-bwm_agent_6_3)
    - branch 2 → [bwm_agent_6_0](#d-bwm_agent_6_0)

    <span id="d-bwm_agent_6_3"></span>**`bwm_agent_6_3`** Agent: “Go ahead, I will meet you inside.”

    - “OK, see you inside.” → *NPC leaves*

    <span id="d-bwm_agent_6_0"></span>**`bwm_agent_6_0`** Agent: “We meet again. Well done fighting your way up here.”

    - Next → [bwm_agent_6_1](#d-bwm_agent_6_1)

    <span id="d-bwm_agent_6_1"></span>**`bwm_agent_6_1`** Agent: “I am glad you followed me up the mountain to help us out.”

    - “How did you get up here so fast?” → [bwm_agent_6_6](#d-bwm_agent_6_6)
    - “Those were some tough fights, but I can manage.” → [bwm_agent_6_5](#d-bwm_agent_6_5)
    - “Are we there yet?” → [bwm_agent_6_2](#d-bwm_agent_6_2)

    <span id="d-bwm_agent_6_6"></span>**`bwm_agent_6_6`** Agent: “I learned some shortcuts up and down the mountain a while back. Nothing strange about that right?”

    - Next → [bwm_agent_6_7](#d-bwm_agent_6_7)

    <span id="d-bwm_agent_6_5"></span>**`bwm_agent_6_5`** Agent: “Yes, you seem like an able fighter.”

    - “Are we there yet?” → [bwm_agent_6_2](#d-bwm_agent_6_2)

    <span id="d-bwm_agent_6_2"></span>**`bwm_agent_6_2`** Agent: “Oh yes. In fact, our Blackwater mountain settlement is just down these stairs.”

    - Next → [bwm_agent_6_4](#d-bwm_agent_6_4)

    <span id="d-bwm_agent_6_7"></span>**`bwm_agent_6_7`** Agent: “Anyway, we are right at the settlement now. In fact, our Blackwater mountain settlement is just down these stairs.”

    - Next → [bwm_agent_6_4](#d-bwm_agent_6_4)

    <span id="d-bwm_agent_6_4"></span>**`bwm_agent_6_4`** Agent: “You should go down these stairs and talk to our battle master, Harlenn. He can usually be found at the third level down.” — **effects:** sets stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60)

    - Next → [bwm_agent_6_3](#d-bwm_agent_6_3)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent6.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `agent6` · Data from v0.8.18</small>
