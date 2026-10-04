# ![](../assets/icons/monsters/monsters_ld1_141.png){ .sprite } Tamarukh

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_141.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `tamarukh` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | Loneford |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

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
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [waytobrimhaven2](../maps/waytobrimhaven2.md) | Loneford | 1 | appears later in a quest |


## Quests

- [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md): stages 88

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Tamarukh. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/tamarukh.json" data-npc="Tamarukh" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tamarukh"></span>**`tamarukh`** Tamarukh: “Isn't it a pity to see all that fertile land wasted?”

    - “Do you mean the lake?” → [tamarukh_10](#d-tamarukh_10)

    <span id="d-tamarukh_10"></span>**`tamarukh_10`** Tamarukh: “Sure. We had built this dam in Brimhaven to get more space for arable land, but someone must have sabotaged it.”

    - “Would you like to repair the dam again?” → [tamarukh_20](#d-tamarukh_20)

    <span id="d-tamarukh_20"></span>**`tamarukh_20`** Tamarukh: “Yes, I would see to it, if I had enough money.”

    - “Everyone wants my money. I better go.” → *conversation ends*
    - “It should not fail because of a lack of money. Here you have 2,500 gold.” *(if pay 2,500 gold)* → [tamarukh_30](#d-tamarukh_30)

    <span id="d-tamarukh_30"></span>**`tamarukh_30`** Tamarukh: “That is very noble of you. I will take care of it.” — **effects:** sets stage 88 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-88)




## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 4 lines added |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed<br>· text: “Sure. We had built this dam in Brimhaven to get more space for arable…” → “Sure. We had built this dam in Brimhaven to get more space for arable…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tamarukh.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tamarukh.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tamarukh.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tamarukh.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `tamarukh` |
    | Spawn group | `tamarukh` |
    | Loot table | – |
    | Conversation | `tamarukh` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:141` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "tamarukh",
     "name": "Tamarukh",
     "iconID": "monsters_ld1:141",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "spawnGroup": "tamarukh",
     "phraseID": "tamarukh"
    }
    ```


<small>Data from v0.8.18</small>
