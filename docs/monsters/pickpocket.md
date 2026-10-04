# ![](../assets/icons/monsters/monsters_men_7.png){ .sprite } Pickpocket

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_7.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `pickpocket` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Fallhaven |
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
| [fallhaven_derelict2](../maps/fallhaven_derelict2.md) | Fallhaven | 1 | – |
| [fallhaven_derelict2_t](../maps/fallhaven_derelict2_t.md) | Fallhaven | 1 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Pickpocket. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/thievesguild_pickpocket_1.json" data-npc="Pickpocket" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-thievesguild_pickpocket_1"></span>**`thievesguild_pickpocket_1`** Pickpocket: “Hello there.”

    - “Who are you?” → [thievesguild_pickpocket_2](#d-thievesguild_pickpocket_2)
    - “What is this place?” → [thievesguild_thief_2](#d-thievesguild_thief_2)

    <span id="d-thievesguild_pickpocket_2"></span>**`thievesguild_pickpocket_2`** Pickpocket: “My real name is unimportant. People mostly call me Quickfingers.”

    - “Why is that?” → [thievesguild_pickpocket_3](#d-thievesguild_pickpocket_3)

    <span id="d-thievesguild_thief_2"></span>**`thievesguild_thief_2`** Pickpocket: “This is our guild hall. We are safe from the guards of Fallhaven in here.”

    - Next → [thievesguild_thief_3](#d-thievesguild_thief_3)

    <span id="d-thievesguild_pickpocket_3"></span>**`thievesguild_pickpocket_3`** Pickpocket: “Well, I have a tendency to ... how shall I put this ... acquire certain things easily.”

    - Next → [thievesguild_pickpocket_4](#d-thievesguild_pickpocket_4)

    <span id="d-thievesguild_thief_3"></span>**`thievesguild_thief_3`** Pickpocket: “We can do pretty much as we like here. As long as Umar allows it, that is.”

    - “Do you know where I can find Umar?” → [thievesguild_thief_4](#d-thievesguild_thief_4)
    - “Who is Umar?” → [thievesguild_thief_5](#d-thievesguild_thief_5)

    <span id="d-thievesguild_pickpocket_4"></span>**`thievesguild_pickpocket_4`** Pickpocket: “Things previously in the possession of other people.”

    - “Do you mean like stealing?” *(if pay 1 gold)* → [thievesguild_pickpocket_5](#d-thievesguild_pickpocket_5)
    - “Isn't that stealing?” *(if NOT have 1 gold)* → [thievesguild_pickpocket_5](#d-thievesguild_pickpocket_5)

    <span id="d-thievesguild_thief_4"></span>**`thievesguild_thief_4`** Pickpocket: “He is probably in his room over there [points].”

    - “Thanks.” → *conversation ends*

    <span id="d-thievesguild_thief_5"></span>**`thievesguild_thief_5`** Pickpocket: “Umar is our guild leader. He decides our rules and guides us in moral decisions.”

    - “Where can I find him?” → [thievesguild_thief_4](#d-thievesguild_thief_4)

    <span id="d-thievesguild_pickpocket_5"></span>**`thievesguild_pickpocket_5`** Pickpocket: “No no. I wouldn't call it stealing. It's more of a transfer of ownership. To me, that is.”

    - “That sounds a lot like stealing to me.” → [thievesguild_pickpocket_6](#d-thievesguild_pickpocket_6)
    - “That sounds like a good justification.” → [thievesguild_pickpocket_6](#d-thievesguild_pickpocket_6)

    <span id="d-thievesguild_pickpocket_6"></span>**`thievesguild_pickpocket_6`** Pickpocket: “After all, we are the Thieves' Guild. What did you expect?”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed<br>· text: “He is probably in his room over there. *points*” → “He is probably in his room over there [points].”<br>· text: “Well, I have a tendency to .. how shall I put this .. acquire certain…” → “Well, I have a tendency to ... how shall I put this ... acquire certa…” |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=pickpocket.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=pickpocket.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=pickpocket.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=pickpocket.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `pickpocket` |
    | Spawn group | `pickpocket` |
    | Loot table | – |
    | Conversation | `thievesguild_pickpocket_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:7` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "pickpocket",
     "name": "Pickpocket",
     "iconID": "monsters_men:7",
     "monsterClass": "humanoid",
     "spawnGroup": "pickpocket",
     "phraseID": "thievesguild_pickpocket_1"
    }
    ```


<small>Data from v0.8.18</small>
