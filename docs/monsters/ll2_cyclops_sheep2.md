# ![](../assets/icons/monsters/monsters_rltiles2_55.png){ .sprite } Sheep

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_55.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `ll2_cyclops_sheep2` |
| **Type** | NPC |
| **Class** | Animal |
| **HP** | 1 |
| **Found in** | ll2_cyclops_cave, mountainlake27, mountainlake28 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

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
| [ll2_cyclops_cave](../maps/ll2_cyclops_cave.md) | – | 1 | appears later in a quest |
| [mountainlake27](../maps/mountainlake27.md) | – | 1 | appears later in a quest |
| [mountainlake28](../maps/mountainlake28.md) | – | 4 | – |


## Quests

- [A map of the Great Lake Laeroth](../quests/lake_map.md): stages 58

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Sheep. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/ll2_cyclops_sheep2.json" data-npc="Sheep" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ll2_cyclops_sheep2"></span>**`ll2_cyclops_sheep2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 57 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-57))* → [ll2_cyclops_sheep2_10](#d-ll2_cyclops_sheep2_10)
    - branch 2 → [ll2_cyclops_sheep](#d-ll2_cyclops_sheep)

    <span id="d-ll2_cyclops_sheep2_10"></span>**`ll2_cyclops_sheep2_10`** Sheep: “Baaah.”

    - “You look strong enough to carry me. I hang down beneath you, and you pull me outwards.” → [ll2_cyclops_sheep2_20](#d-ll2_cyclops_sheep2_20)

    <span id="d-ll2_cyclops_sheep"></span>**`ll2_cyclops_sheep`** Sheep: “Baaah.”


    <span id="d-ll2_cyclops_sheep2_20"></span>**`ll2_cyclops_sheep2_20`** Sheep: “The sheep carries you willingly.” — **effects:** sets stage 58 of [A map of the Great Lake Laeroth](../quests/lake_map.md#stage-58), removes monsters from ll2_cyclops_cave




## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_cyclops_sheep2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_cyclops_sheep2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_cyclops_sheep2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_cyclops_sheep2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `ll2_cyclops_sheep2` |
    | Spawn group | `ll2_cyclops_sheep2` |
    | Loot table | – |
    | Conversation | `ll2_cyclops_sheep2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:55` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_cyclops_sheep2",
     "name": "Sheep",
     "iconID": "monsters_rltiles2:55",
     "monsterClass": "animal",
     "spawnGroup": "ll2_cyclops_sheep2",
     "horizontalFlipChance": 100,
     "phraseID": "ll2_cyclops_sheep2"
    }
    ```


<small>Data from v0.8.18</small>
