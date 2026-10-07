# ![](../assets/icons/monsters/monsters_men_4.png){ .sprite } Agent

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_4.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `agent5` |
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
| [blackwater_mountain30](../maps/blackwater_mountain30.md) | Blackwater Mountain | 1 | – |


## Quests

- [The agent and the beast](../quests/bwm_agent.md): stages 50

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Agent. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/bwm_agent_5_start.json" data-npc="Agent" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-bwm_agent_5_start"></span>**`bwm_agent_5_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [The agent and the beast](../quests/bwm_agent.md#stage-50))* → [bwm_agent_5_6](#d-bwm_agent_5_6)
    - branch 2 → [bwm_agent_5_1](#d-bwm_agent_5_1)

    <span id="d-bwm_agent_5_6"></span>**`bwm_agent_5_6`** Agent: “Now hurry. We are almost there. Follow the snowy path to the north, and you should reach the settlement in no time.” — **effects:** sets stage 50 of [The agent and the beast](../quests/bwm_agent.md#stage-50)

    - “OK, I will follow the path to the north, further up the mountain.” → *NPC leaves*

    <span id="d-bwm_agent_5_1"></span>**`bwm_agent_5_1`** Agent: “Hello again. Well done getting through those monsters.”

    - Next → [bwm_agent_5_2](#d-bwm_agent_5_2)

    <span id="d-bwm_agent_5_2"></span>**`bwm_agent_5_2`** Agent: “We are almost there now. Just a little bit more.”

    - Next → [bwm_agent_5_3](#d-bwm_agent_5_3)

    <span id="d-bwm_agent_5_3"></span>**`bwm_agent_5_3`** Agent: “We should hurry this last bit, my settlement is close now.”

    - Next → [bwm_agent_5_4](#d-bwm_agent_5_4)

    <span id="d-bwm_agent_5_4"></span>**`bwm_agent_5_4`** Agent: “I hope you can manage the cold out here.”

    - Next → [bwm_agent_5_5](#d-bwm_agent_5_5)

    <span id="d-bwm_agent_5_5"></span>**`bwm_agent_5_5`** Agent: “Also, stay away from the wyrms. They have a really nasty bite.”

    - Next → [bwm_agent_5_6](#d-bwm_agent_5_6)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=agent5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `agent5` |
    | Spawn group | `bwm_agent_5` |
    | Loot table | – |
    | Conversation | `bwm_agent_5_start` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:4` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "agent5",
     "name": "Agent",
     "iconID": "monsters_men:4",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "bwm_agent_5",
     "phraseID": "bwm_agent_5_start"
    }
    ```


<small>Data from v0.8.18</small>
