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

- [blackwater_mountain5](../maps/blackwater_mountain5.md)

## Quests

- [The agent and the beast](../quests/bwm_agent.md): stages 1, 5, 10

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Agent. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/bwm_agent_1_start.json" data-npc="Agent" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (14 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-bwm_agent_1_start"></span>**`bwm_agent_1_start`** Agent: “Oh, someone from the outside! Please, adventurer, you have to help us!”

    - “What is the matter?” → [bwm_agent_1_2](#d-bwm_agent_1_2)
    - “'Us'? I only see you here.” → [bwm_agent_1_3](#d-bwm_agent_1_3)

    <span id="d-bwm_agent_1_2"></span>**`bwm_agent_1_2`** Agent: “We urgently need help from someone outside!”

    - Next → [bwm_agent_1_4](#d-bwm_agent_1_4)

    <span id="d-bwm_agent_1_3"></span>**`bwm_agent_1_3`** Agent: “Very funny. I was sent by my settlement to get help from the outside.”

    - Next → [bwm_agent_1_4](#d-bwm_agent_1_4)

    <span id="d-bwm_agent_1_4"></span>**`bwm_agent_1_4`** Agent: “The people of my settlement, the Blackwater mountain, are slowly being reduced in numbers by the monsters and the savage bandits.” — **effects:** sets stage 1 of [The agent and the beast](../quests/bwm_agent.md#stage-1)

    - Next → [bwm_agent_1_5](#d-bwm_agent_1_5)

    <span id="d-bwm_agent_1_5"></span>**`bwm_agent_1_5`** Agent: “The monsters are closing in on us, and we desperately need help by some able fighter.”

    - “I guess I could help, I have killed a few monsters here and there.” → [bwm_agent_1_7](#d-bwm_agent_1_7)
    - “A fight, great. I'm in!” → [bwm_agent_1_7](#d-bwm_agent_1_7)
    - “Will there be a reward for this?” → [bwm_agent_1_6](#d-bwm_agent_1_6)
    - “Hmm, no. I had better not get involved in this.” → *conversation ends*

    <span id="d-bwm_agent_1_7"></span>**`bwm_agent_1_7`** Agent: “Excellent. The Blackwater mountain settlement is some distance away. Frankly, I am amazed that I made it this far alive.” — **effects:** sets stage 5 of [The agent and the beast](../quests/bwm_agent.md#stage-5)

    - Next → [bwm_agent_1_8](#d-bwm_agent_1_8)

    <span id="d-bwm_agent_1_6"></span>**`bwm_agent_1_6`** Agent: “Reward? Hmm, I was hoping you would help us for other reasons than a reward. But I guess my master will reward you sufficiently if you survive.”

    - “Alright, I'll do it.” → [bwm_agent_1_7](#d-bwm_agent_1_7)

    <span id="d-bwm_agent_1_8"></span>**`bwm_agent_1_8`** Agent: “I must warn you though, that there are some nasty monsters on the way.”

    - Next → [bwm_agent_1_9](#d-bwm_agent_1_9)

    <span id="d-bwm_agent_1_9"></span>**`bwm_agent_1_9`** Agent: “But I guess you seem strong enough.”

    - “Yeah, I can handle myself.” → [bwm_agent_1_10](#d-bwm_agent_1_10)
    - “No problem.” → [bwm_agent_1_10](#d-bwm_agent_1_10)

    <span id="d-bwm_agent_1_10"></span>**`bwm_agent_1_10`** Agent: “Good. First though, we must cross this mine to the other side.”

    - Next → [bwm_agent_1_11](#d-bwm_agent_1_11)

    <span id="d-bwm_agent_1_11"></span>**`bwm_agent_1_11`** Agent: “The mine shaft over there [points] has collapsed, so I guess you won't make it through there.”

    - Next → [bwm_agent_1_12](#d-bwm_agent_1_12)

    <span id="d-bwm_agent_1_12"></span>**`bwm_agent_1_12`** Agent: “You will have to go through the abandoned mine below. Beware that the mine is pitch-black, so you will have to navigate in there without any light.”

    - “What about you?” → [bwm_agent_1_13](#d-bwm_agent_1_13)
    - “OK, I'll go through the pitch-black mine.” → [bwm_agent_1_14](#d-bwm_agent_1_14)

    <span id="d-bwm_agent_1_13"></span>**`bwm_agent_1_13`** Agent: “I'll try to crawl back through the mine shaft here. That's how I got here in the first place.”

    - Next → [bwm_agent_1_14](#d-bwm_agent_1_14)

    <span id="d-bwm_agent_1_14"></span>**`bwm_agent_1_14`** Agent: “Let's meet at the other side of this mine shaft.” — **effects:** sets stage 10 of [The agent and the beast](../quests/bwm_agent.md#stage-10), removes monsters from blackwater_mountain5

    - “OK. You crawl through the shaft, and I'll go below. See you on the other side!” → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 6 lines changed<br>· text: “Excellent. The Blackwater settlement is some distance away. Frankly, …” → “Excellent. The Blackwater mountain settlement is some distance away. …”<br>· text: “The mine shaft over there *points* has collapsed, so I guess you won'…” → “The mine shaft over there [points] has collapsed, so I guess you won'…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “Oh, someone from the outside! Please, sir! You have to help us!” → “Oh, someone from the outside! Please, adventurer, you have to help us!” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `agent1` · Data from v0.8.18</small>
