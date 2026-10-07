# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Dying patrol

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `g03_deadpatrol_1` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | crackshot_hideout2 |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

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
| [crackshot_hideout2](../maps/crackshot_hideout2.md) | – | 1 | – |


## Quests

- [The ruthless Crackshot](../quests/Thieves03.md): stages 25, 28
- [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md): stages 40

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Dying patrol. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/guild03_deadpatrol1_select.json" data-npc="Dying patrol" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guild03_deadpatrol1_select"></span>**`guild03_deadpatrol1_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 50 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-50))* → [guild03_deadpatrol1_was_first](#d-guild03_deadpatrol1_was_first)
    - branch 2 → [guild03_deadpatrol1_was_second](#d-guild03_deadpatrol1_was_second)

    <span id="d-guild03_deadpatrol1_was_first"></span>**`guild03_deadpatrol1_was_first`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 25 of [The ruthless Crackshot](../quests/Thieves03.md#stage-25)

    - branch 1 → [guild03_deadpatrol_1_1](#d-guild03_deadpatrol_1_1)

    <span id="d-guild03_deadpatrol1_was_second"></span>**`guild03_deadpatrol1_was_second`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 28 of [The ruthless Crackshot](../quests/Thieves03.md#stage-28)

    - branch 1 → [guild03_deadpatrol_1_1](#d-guild03_deadpatrol_1_1)

    <span id="d-guild03_deadpatrol_1_1"></span>**`guild03_deadpatrol_1_1`** Dying patrol: “(You see, horrified, how this man is bleeding out rapidly. He has countless cuts and his face is mutilated. You can almost hear his gasps.)” — **effects:** removes monsters from crackshot_hideout2, sets stage 40 of [Thieves Hidden (hidden flag)](../quests/thieves_hidden.md#stage-40)

    - “Shadow, embrace him.” → *NPC leaves*
    - “For the glory of Feygard, you will be avenged!” → *NPC leaves*



## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_deadpatrol_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_deadpatrol_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_deadpatrol_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_deadpatrol_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `g03_deadpatrol_1` |
    | Spawn group | `g03_deadpatrol_1` |
    | Loot table | – |
    | Conversation | `guild03_deadpatrol1_select` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_omicronrg9.json` |

    Raw data:

    ```json
    {
     "id": "g03_deadpatrol_1",
     "name": "Dying patrol",
     "iconID": "monsters_rltiles3:14",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "g03_deadpatrol_1",
     "phraseID": "guild03_deadpatrol1_select"
    }
    ```


<small>Data from v0.8.18</small>
