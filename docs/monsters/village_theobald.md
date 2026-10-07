# ![](../assets/icons/monsters/monsters_ld1_121.png){ .sprite } Theobald

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_121.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `village_theobald` |
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
| [wexlow_village](../maps/wexlow_village.md) | Wexlow Village | 1 | appears later in a quest |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Theobald. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/village_theobald_start.json" data-npc="Theobald" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-village_theobald_start"></span>**`village_theobald_start`** Theobald: “We are indebted to you now. Your heroism will never be forgotten by the members of this tiny village.”

    - “Why do you live in this "tiny village" anyway?” → [village_theobald_1](#d-village_theobald_1)

    <span id="d-village_theobald_1"></span>**`village_theobald_1`** Theobald: “That is indeed an excellent question.”

    - Next → [village_theobald_2](#d-village_theobald_2)

    <span id="d-village_theobald_2"></span>**`village_theobald_2`** Theobald: “Let me explain.”

    - “Please, go ahead.” → [village_theobald_3](#d-village_theobald_3)

    <span id="d-village_theobald_3"></span>**`village_theobald_3`** Theobald: “You see, all eight of us were born and raised in the glorious city of Feygard. In fact, we grew up together. Best friends too! But for various reasons, things started to change for us.”

    - “Really? I am intrigued to hear more.” → [village_theobald_4](#d-village_theobald_4)

    <span id="d-village_theobald_4"></span>**`village_theobald_4`** Theobald: “Well, I don't want to speak for everyone else, but for Theodora and I, we began to desire a quieter, more laid back lifestyle.”

    - “That makes sense. But what about the others?” → [village_theobald_5](#d-village_theobald_5)
    - “But do you ever miss it? I mean, if Feygard is so glorious, then you must miss it?” → [village_theobald_miss_feygard](#d-village_theobald_miss_feygard)

    <span id="d-village_theobald_5"></span>**`village_theobald_5`** Theobald: “Well, like I said before, I don't want to talk for them, but Osric is my best friend, so I know he longed for the days he could raise a garden and live off the land.”


    <span id="d-village_theobald_miss_feygard"></span>**`village_theobald_miss_feygard`** Theobald: “Oh, I do miss it a lot. Well, I miss most of it a lot. I miss my family. I miss my old customers coming into my market.”

    - “"Most of it"?” → [village_theobald_miss_feygard_2](#d-village_theobald_miss_feygard_2)

    <span id="d-village_theobald_miss_feygard_2"></span>**`village_theobald_miss_feygard_2`** Theobald: “Yeah. I don't miss the noise and the hustle and bustle of the city at all hours of the day. It gets tiresome.”

    - “Thank you for that. It really helped to hear about Feygard from one of its citizens.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 8 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_theobald.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_theobald.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_theobald.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_theobald.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `village_theobald` |
    | Spawn group | `village_theobald` |
    | Loot table | – |
    | Conversation | `village_theobald_start` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:121` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "village_theobald",
     "name": "Theobald",
     "iconID": "monsters_ld1:121",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "village_theobald_start"
    }
    ```


<small>Data from v0.8.18</small>
