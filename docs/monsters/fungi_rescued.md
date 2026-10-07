# ![](../assets/icons/monsters/monsters_ld1_20.png){ .sprite } Lediofa

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_20.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `fungi_rescued` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | mushroom_m3_2 |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

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
| Move cost | 2 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mushroom_m3_2](../maps/mushroom_m3_2.md) | – | 1 | appears later in a quest |


## Quests

- [Fungi panic](../quests/fungi_panic.md): stages 210

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Lediofa. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/fungi_rescued.json" data-npc="Lediofa" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (12 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-fungi_rescued"></span>**`fungi_rescued`** Lediofa: “Thank you, thank you!”

    - “Who are you?” → [fungi_rescued_10](#d-fungi_rescued_10)

    <span id="d-fungi_rescued_10"></span>**`fungi_rescued_10`** Lediofa: “My name is Lediofa. I was travelling with my family to Vilegard. We wanted to visit my uncle.”

    - Next → [fungi_rescued_20](#d-fungi_rescued_20)

    <span id="d-fungi_rescued_20"></span>**`fungi_rescued_20`** Lediofa: “We were attacked by robbers in the forest. I don't know what happened to my family. It was terrible.”

    - “Poor child.” → [fungi_rescued_30](#d-fungi_rescued_30)

    <span id="d-fungi_rescued_30"></span>**`fungi_rescued_30`** Lediofa: “I was dragged into this cave.”

    - Next → [fungi_rescued_40](#d-fungi_rescued_40)

    <span id="d-fungi_rescued_40"></span>**`fungi_rescued_40`** Lediofa: “The only thing I saw was a figure clad in black who kept muttering mean sounding words.”

    - “That must have been Zuul'khan.” → [fungi_rescued_50](#d-fungi_rescued_50)

    <span id="d-fungi_rescued_50"></span>**`fungi_rescued_50`** Lediofa: “Yes, it was him. I hope you're not one of his friends? Please no!”

    - “Don't panic. I am $playername from Crossglen. Zuul'khan received his just punishment. He can't do anything to you…” → [fungi_rescued_60](#d-fungi_rescued_60)

    <span id="d-fungi_rescued_60"></span>**`fungi_rescued_60`** Lediofa: “Oh, how relieved I am to hear that! Thank you again!”

    - Next → [fungi_rescued_70](#d-fungi_rescued_70)

    <span id="d-fungi_rescued_70"></span>**`fungi_rescued_70`** Lediofa: “This black-clad man wanted to feed me to this awful big mushroom. He told me the mushroom still needed to grow much larger, and then it could help him invade the land.”

    - Next → [fungi_rescued_80](#d-fungi_rescued_80)

    <span id="d-fungi_rescued_80"></span>**`fungi_rescued_80`** Lediofa: “I'm glad this nightmare is over now. Thanks to you, $playername.”

    - “Oh, that was nothing.” → [fungi_rescued_90](#d-fungi_rescued_90)
    - “I do things like that every other day.” → [fungi_rescued_90](#d-fungi_rescued_90)
    - “It was a tough fight indeed.” → [fungi_rescued_90](#d-fungi_rescued_90)

    <span id="d-fungi_rescued_90"></span>**`fungi_rescued_90`** Lediofa: “I should go look for my parents - I'm sure they are very worried. Although...”

    - “What is it?” → [fungi_rescued_100](#d-fungi_rescued_100)

    <span id="d-fungi_rescued_100"></span>**`fungi_rescued_100`** Lediofa: “I feel a bit ill. Maybe I should rest a bit before I leave.”

    - “That might be the giant mushroom's poison. The potioner in Fallhaven knows the cure.” → [fungi_rescued_110](#d-fungi_rescued_110)

    <span id="d-fungi_rescued_110"></span>**`fungi_rescued_110`** Lediofa: “[Lediofa's eyes widen.] I've been poisoned...? Oh no! I'll seek the potioner right away. Thank you for telling me. I hope we meet again, $playername.” — **effects:** sets stage 210 of [Fungi panic](../quests/fungi_panic.md#stage-210), spawns monsters on fallhaven_potions

    - “Good luck!” → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 12 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fungi_rescued.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fungi_rescued.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fungi_rescued.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fungi_rescued.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `fungi_rescued` |
    | Spawn group | `fungi_rescued` |
    | Loot table | – |
    | Conversation | `fungi_rescued` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:20` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "fungi_rescued",
     "name": "Lediofa",
     "iconID": "monsters_ld1:20",
     "maxAP": 10,
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "spawnGroup": "fungi_rescued",
     "phraseID": "fungi_rescued"
    }
    ```


<small>Data from v0.8.18</small>
