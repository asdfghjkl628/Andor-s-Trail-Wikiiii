# ![](../assets/icons/monsters/monsters_liches_3.png){ .sprite } Dark priest

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_liches_3.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `dds_dark_priest` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 1 |
| **Found in** | galmore_41 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

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
| [galmore_41](../maps/galmore_41.md) | – | 1 | appears later in a quest |


## Quests

- [Darkness in the Daylight](../quests/darkness_in_daylight.md): stages 250
- [Shadows](../quests/shadows.md): stages 230

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Dark priest. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/dds_dark_priest.json" data-npc="Dark priest" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-dds_dark_priest"></span>**`dds_dark_priest`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 190 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-190))* → [dds_dark_priest_2](#d-dds_dark_priest_2)
    - branch 2 *(if reached stage 165 of [Shadows](../quests/shadows.md#stage-165))* → [dds_dark_priest_4](#d-dds_dark_priest_4)

    <span id="d-dds_dark_priest_2"></span>**`dds_dark_priest_2`** Dark priest: “How dare you stop my spell?” — **effects:** sets stage 250 of [Darkness in the Daylight](../quests/darkness_in_daylight.md#stage-250)

    - “It is best for Dhayavar.” → [dds_dark_priest_10](#d-dds_dark_priest_10)

    <span id="d-dds_dark_priest_4"></span>**`dds_dark_priest_4`** Dark priest: “How dare you stop my spell?” — **effects:** sets stage 230 of [Shadows](../quests/shadows.md#stage-230)

    - “It is best for Dhayavar.” → [dds_dark_priest_10](#d-dds_dark_priest_10)

    <span id="d-dds_dark_priest_10"></span>**`dds_dark_priest_10`** Dark priest: “I have no time for this.” — **effects:** removes monsters from galmore_41, spawns monsters on galmore_41

    - “Oh, you are running away?” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_dark_priest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_dark_priest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_dark_priest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dds_dark_priest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `dds_dark_priest` |
    | Spawn group | `dds_dark_priest` |
    | Loot table | – |
    | Conversation | `dds_dark_priest` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_liches:3` |
    | Defined in | `res/raw/monsterlist_darknessanddaylight.json` |

    Raw data:

    ```json
    {
     "id": "dds_dark_priest",
     "name": "Dark priest",
     "iconID": "monsters_liches:3",
     "moveCost": 5,
     "monsterClass": "humanoid",
     "spawnGroup": "dds_dark_priest",
     "phraseID": "dds_dark_priest"
    }
    ```


<small>Data from v0.8.18</small>
