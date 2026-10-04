# ![](../assets/icons/monsters/monsters_men_4.png){ .sprite } Agent

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_4.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `agent6` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Blackwater Mountain |
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
| [blackwater_mountain38](../maps/blackwater_mountain38.md) | Blackwater Mountain | 1 | – |


## Quests

- [The agent and the beast](../quests/bwm_agent.md): stages 60

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Agent. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/bwm_agent_6_start.json" data-npc="Agent" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

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


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `agent6` |
    | Spawn group | `bwm_agent_6` |
    | Loot table | – |
    | Conversation | `bwm_agent_6_start` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:4` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "agent6",
     "name": "Agent",
     "iconID": "monsters_men:4",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "bwm_agent_6",
     "phraseID": "bwm_agent_6_start"
    }
    ```


<small>Data from v0.8.18</small>
