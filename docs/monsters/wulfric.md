# ![](../assets/icons/monsters/monsters_tometik3_10.png){ .sprite } Wulfric

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik3_10.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `wulfric` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Wexlow Village |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

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
| [way_to_wexlow1](../maps/way_to_wexlow1.md) | Wexlow Village | 1 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Wulfric. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/wulfric_ip.json" data-npc="Wulfric" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-wulfric_ip"></span>**`wulfric_ip`** Wulfric: “Hey there. I am "Wulfric the Wonderful".”

    - “I am wondering...” → [wulfric_wonder](#d-wulfric_wonder)

    <span id="d-wulfric_wonder"></span>**`wulfric_wonder`** Wulfric: “Why I'm so wonderful?”

    - “Well, yeah, but no, not really.” → [wulfric_ask_about_andor](#d-wulfric_ask_about_andor)
    - “Do you know where the residents of Wexlow Village are?” *(if reached stage 11 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-11); NOT reached stage 10 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-10))* → [wulfric_wexlow](#d-wulfric_wexlow)
    - “Yes, why are you so wonderful?” → [wulfric_wonder_answer](#d-wulfric_wonder_answer)

    <span id="d-wulfric_ask_about_andor"></span>**`wulfric_ask_about_andor`** Wulfric: “What then?”

    - “Whether you've seen my brother, Andor or not. You see, he looks like me, but not as good looking.” → [wulfric_andor](#d-wulfric_andor)

    <span id="d-wulfric_wexlow"></span>**`wulfric_wexlow`** Wulfric: “Wexlow Village? Where is that?”

    - “Oh, nevermind.” → *conversation ends*

    <span id="d-wulfric_wonder_answer"></span>**`wulfric_wonder_answer`** Wulfric: “Because all the ladies say that I am.”


    <span id="d-wulfric_andor"></span>**`wulfric_andor`** Wulfric: “Nope. Sorry. Is there anything else?”

    - “I am wondering...” → [wulfric_wonder](#d-wulfric_wonder)
    - “Nope.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wulfric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wulfric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wulfric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=wulfric.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `wulfric` |
    | Spawn group | `wulfric` |
    | Loot table | – |
    | Conversation | `wulfric_ip` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik3:10` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "wulfric",
     "name": "Wulfric",
     "iconID": "monsters_tometik3:10",
     "monsterClass": "humanoid",
     "phraseID": "wulfric_ip"
    }
    ```


<small>Data from v0.8.18</small>
