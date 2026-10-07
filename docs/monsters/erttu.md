# ![](../assets/icons/monsters/monsters_mage2_0.png){ .sprite } Erttu

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_mage2_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `erttu` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Vilegard |
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
| [vilegard_erttu](../maps/vilegard_erttu.md) | Vilegard | 1 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Erttu. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/erttu_1.json" data-npc="Erttu" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-erttu_1"></span>**`erttu_1`** Erttu: “Hello there outsider. In general, we dislike outsiders here in Vilegard, but there is something about you that I find familiar.”

    - Next → [erttu_default](#d-erttu_default)

    <span id="d-erttu_default"></span>**`erttu_default`** Erttu: “What do you want to talk about?”

    - “Why is everyone in Vilegard so suspicious of outsiders?” *(if reached stage 10 of [Trusting an outsider](../quests/vilegard.md#stage-10))* → [erttu_distrust_1](#d-erttu_distrust_1)
    - “What can you tell me about Vilegard?” → [erttu_vilegard_1](#d-erttu_vilegard_1)

    <span id="d-erttu_distrust_1"></span>**`erttu_distrust_1`** Erttu: “Most of us that live here in Vilegard have a history of trusting people too much. People that have hurt us in the end.”

    - Next → [erttu_distrust_2](#d-erttu_distrust_2)

    <span id="d-erttu_vilegard_1"></span>**`erttu_vilegard_1`** Erttu: “We have almost everything we need here in Vilegard. Our center of the village is the chapel.”

    - Next → [erttu_vilegard_2](#d-erttu_vilegard_2)

    <span id="d-erttu_distrust_2"></span>**`erttu_distrust_2`** Erttu: “Now we start by being suspicious, and ask that outsiders coming here gain our trust by helping us first.”

    - Next → [erttu_distrust_3](#d-erttu_distrust_3)

    <span id="d-erttu_vilegard_2"></span>**`erttu_vilegard_2`** Erttu: “The chapel serves as our place of worship for the Shadow, and also as our place to gather when discussing larger issues in our village.”

    - Next → [erttu_vilegard_3](#d-erttu_vilegard_3)

    <span id="d-erttu_distrust_3"></span>**`erttu_distrust_3`** Erttu: “Also, other people generally look down upon us here in Vilegard for some reason. Especially those snobs from Feygard and the northern cities.”

    - “What else can you tell me about Vilegard?” → [erttu_vilegard_1](#d-erttu_vilegard_1)

    <span id="d-erttu_vilegard_3"></span>**`erttu_vilegard_3`** Erttu: “Apart from the chapel, we have a tavern, a smith and an armorer.”

    - “Thanks for the information. There was something else I wanted to talk about.” → [erttu_default](#d-erttu_default)
    - “Thanks for the information. Goodbye.” → *conversation ends*
    - “Wow, nothing more? I wonder what I am doing in a puny village such as this one.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erttu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erttu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erttu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erttu.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `erttu` |
    | Spawn group | `erttu` |
    | Loot table | – |
    | Conversation | `erttu_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_mage2:0` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "erttu",
     "name": "Erttu",
     "iconID": "monsters_mage2:0",
     "monsterClass": "humanoid",
     "spawnGroup": "erttu",
     "phraseID": "erttu_1"
    }
    ```


<small>Data from v0.8.18</small>
