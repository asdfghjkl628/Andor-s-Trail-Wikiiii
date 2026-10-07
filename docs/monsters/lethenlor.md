# ![](../assets/icons/monsters/monsters_tometik6_16.png){ .sprite } Lethenlor

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik6_16.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `lethenlor` |
| **Type** | NPC |
| **Class** | ? |
| **HP** | 1 |
| **Found in** | Foaming Flask Tavern |
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
| [tradehouse1](../maps/tradehouse1.md) | Foaming Flask Tavern | 1 | – |


## Quests

- [Destined for great things](../quests/charwood1.md): stages 10

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Lethenlor. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/lethenlor0.json" data-npc="Lethenlor" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lethenlor0"></span>**`lethenlor0`** Lethenlor: “Can I help you?”

    - “Who are you?” → [lethenlor4](#d-lethenlor4)
    - “What is this place?” → [lethenlor1](#d-lethenlor1)
    - “Anything interesting happening around here?” → [lethenlor5](#d-lethenlor5)

    <span id="d-lethenlor4"></span>**`lethenlor4`** Lethenlor: “Does it matter? I don't know you, and you don't know me.”

    - “Wow, you're not very friendly, are you?” → [lethenlor2](#d-lethenlor2)
    - “What is this place?” → [lethenlor1](#d-lethenlor1)
    - “Anything interesting happening around here?” → [lethenlor5](#d-lethenlor5)

    <span id="d-lethenlor1"></span>**`lethenlor1`** Lethenlor: “Well, it's our cabin. What are you doing here, anyway?”

    - “I'm looking for my brother, Andor.” → [lethenlor3](#d-lethenlor3)
    - “Not much, maybe there is some loot in here that I can grab.” → [lethenlor2](#d-lethenlor2)
    - “Anything interesting happening around here?” → [lethenlor5](#d-lethenlor5)

    <span id="d-lethenlor5"></span>**`lethenlor5`** Lethenlor: “He he. Interesting. Let's just say our line of work is ... interesting.”

    - Next → [lethenlor6](#d-lethenlor6)

    <span id="d-lethenlor2"></span>**`lethenlor2`** Lethenlor: “Hrmpf. I think you had better leave.”


    <span id="d-lethenlor3"></span>**`lethenlor3`** Lethenlor: “OK. Good luck with that.”

    - “Who are you?” → [lethenlor4](#d-lethenlor4)
    - “Anything interesting happening around here?” → [lethenlor5](#d-lethenlor5)

    <span id="d-lethenlor6"></span>**`lethenlor6`** Lethenlor: “But never mind that. I heard there were some troubles up by the Charwood mining town recently.”

    - “Charwood, where's that?” → [lethenlor7](#d-lethenlor7)

    <span id="d-lethenlor7"></span>**`lethenlor7`** Lethenlor: “It's just northeast of here. Look for the Charwood cabin north of here.” — **effects:** sets stage 10 of [Destined for great things](../quests/charwood1.md#stage-10)




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed<br>· text: “He he. Interesting. Let's just say our line of work is .. interesting.” → “He he. Interesting. Let's just say our line of work is ... interestin…”<br>· text: “Ok. Good luck with that.” → “OK. Good luck with that.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lethenlor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lethenlor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lethenlor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lethenlor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `lethenlor` |
    | Spawn group | `lethenlor` |
    | Loot table | – |
    | Conversation | `lethenlor0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik6:16` |
    | Defined in | `res/raw/monsterlist_v070_npcs.json` |

    Raw data:

    ```json
    {
     "id": "lethenlor",
     "name": "Lethenlor",
     "iconID": "monsters_tometik6:16",
     "phraseID": "lethenlor0"
    }
    ```


<small>Data from v0.8.18</small>
