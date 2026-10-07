# ![](../assets/icons/monsters/monsters_rltiles1_74.png){ .sprite } Moyra

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_74.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `moyra` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Prim |
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
| [blackwater_mountain11](../maps/blackwater_mountain11.md) | Prim | 1 | – |


## Quests

- [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md): stages 9

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Moyra. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/moyra_1.json" data-npc="Moyra" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (13 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-moyra_1"></span>**`moyra_1`** Moyra: “Stay away. This is my hiding spot.”

    - “What are you hiding from?” → [moyra_2](#d-moyra_2)
    - “Do you know anything about the accident with Lorn?” *(if reached stage 20 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-20); NOT reached stage 9 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-9))* → [moyra_8](#d-moyra_8)
    - “Who are you?” → [moyra_3](#d-moyra_3)
    - “Do you know anything about the accident with Lorn?” *(if reached stage 9 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-9))* → [moyra_12](#d-moyra_12)

    <span id="d-moyra_2"></span>**`moyra_2`** Moyra: “Claws, beasts, gornauds. They cannot reach me here.”

    - “'Gornauds', is that what those monsters outside the village are called?” → [moyra_5](#d-moyra_5)
    - “Yeah sure. Stay here and hide you pathetic creature.” → [moyra_4](#d-moyra_4)

    <span id="d-moyra_8"></span>**`moyra_8`** Moyra: “Lorn? N...No. Why I would know about that?”

    - “I promise I won't say anything.” → [moyra_9a](#d-moyra_9a)
    - “I can make you talk one way or another.” → [moyra_9b](#d-moyra_9b)

    <span id="d-moyra_3"></span>**`moyra_3`** Moyra: “Me? I am Moyra.”

    - “Why are you hiding?” → [moyra_2](#d-moyra_2)

    <span id="d-moyra_12"></span>**`moyra_12`** Moyra: “I told you everything I know, sorry.”

    - “Shadow be with you.” → *conversation ends*
    - “OK, bye.” → *conversation ends*
    - “Bah, useless kid.” → *conversation ends*

    <span id="d-moyra_5"></span>**`moyra_5`** Moyra: “Please, not so loud! They could hear you.”

    - Next → [moyra_6](#d-moyra_6)

    <span id="d-moyra_4"></span>**`moyra_4`** Moyra: “You are mean! I don't want to talk to you any more.”


    <span id="d-moyra_9a"></span>**`moyra_9a`** Moyra: “You promise?”

    - “I do.” → [moyra_10](#d-moyra_10)
    - “[Lie] I do.” → [moyra_10](#d-moyra_10)

    <span id="d-moyra_9b"></span>**`moyra_9b`** Moyra: “Alright! I will tell you, but please don't hurt me.”

    - “Good kid.” → [moyra_10](#d-moyra_10)
    - “Don't worry, hah. But tell me.” → [moyra_10](#d-moyra_10)

    <span id="d-moyra_6"></span>**`moyra_6`** Moyra: “I have seen them on the path up the mountain. Sharpening their claws.”

    - Next → [moyra_7](#d-moyra_7)

    <span id="d-moyra_10"></span>**`moyra_10`** Moyra: “I heard about Lorn's accident, but I don't believe he fell off the mountain. He is the most skilled man I know when it comes to climbing the mountain.”

    - “What about his partners?” → [moyra_11](#d-moyra_11)

    <span id="d-moyra_7"></span>**`moyra_7`** Moyra: “I hide here now, so they cannot get to me.”


    <span id="d-moyra_11"></span>**`moyra_11`** Moyra: “They're still missing, but I don't know...” — **effects:** sets stage 9 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-9)

    - “Thank you for your honest words.” → *conversation ends*
    - “Bah, useless kid.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed<br>· text: “Claws, beasts, Gornauds. They cannot reach me here.” → “Claws, beasts, gornauds. They cannot reach me here.” |
| [v0.7.14](../versions/0.7.14.md) | Dialogue: 6 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=moyra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=moyra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=moyra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=moyra.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `moyra` |
    | Spawn group | `moyra` |
    | Loot table | – |
    | Conversation | `moyra_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:74` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "moyra",
     "name": "Moyra",
     "iconID": "monsters_rltiles1:74",
     "monsterClass": "humanoid",
     "spawnGroup": "moyra",
     "phraseID": "moyra_1"
    }
    ```


<small>Data from v0.8.18</small>
