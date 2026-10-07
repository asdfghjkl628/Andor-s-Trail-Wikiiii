# ![](../assets/icons/monsters/monsters_karvis2_8.png){ .sprite } Sheep

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_karvis2_8.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `guynmart_sheep` |
| **Type** | NPC |
| **Class** | Animal |
| **HP** | 5 |
| **XP when killed** | 4 |
| **Found in** | Guynmart Castle |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 5 |
| Damage | 0 to 1 |
| Attack chance | 10 |
| Block chance | 5 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 20% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [guynmart_wood_9](../maps/guynmart_wood_9.md) | Guynmart Castle | 25 | – |


## Quests that count kills

- A conversation with [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that you've killed at least 1
- A conversation with [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that you've killed at least 25
- A conversation with [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that you've killed at least 20
- A conversation with [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that you've killed at least 15
- A conversation with [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that you've killed at least 10
- A conversation with [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that you've killed at least 9
- A conversation with [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that you've killed at least 8
- A conversation with [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that you've killed at least 7
- A conversation with [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that you've killed at least 6
- A conversation with [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that you've killed at least 5
- A conversation with [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that you've killed at least 4
- A conversation with [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that you've killed at least 3
- A conversation with [Hannah](../monsters/guynmart_hannah2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)), [Lovis](../monsters/guynmart_lovis2.md) ([guynmart_main_0](../maps/guynmart_main_0.md)) checks that you've killed at least 2
- [Roses](../quests/guynmart.md#stage-170) with stepping on a trigger on [guynmart_farmhouse](../maps/guynmart_farmhouse.md) checks that you've killed at least 1
- A conversation with [Shepherd](../monsters/guynmart_shephard.md) ([guynmart_wood_9](../maps/guynmart_wood_9.md)), [Shepherd](../monsters/guynmart_shephard2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) checks that you've killed at least 1
- A conversation with [Shepherd](../monsters/guynmart_shephard.md) ([guynmart_wood_9](../maps/guynmart_wood_9.md)), [Shepherd](../monsters/guynmart_shephard2.md) ([guynmart_main_1](../maps/guynmart_main_1.md)) checks that you've killed at least 20


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Sheep. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_sheep_10.json" data-npc="Sheep" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-guynmart_sheep_10"></span>**`guynmart_sheep_10`** Sheep: “Baah!”

    - “Baah!” → *conversation ends*
    - “You look tasty...” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_sheep.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_sheep.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_sheep.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_sheep.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `guynmart_sheep` |
    | Spawn group | `guynmart_sheep` |
    | Loot table | `guynmart_sheep` |
    | Conversation | `guynmart_sheep_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:8` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_sheep",
     "name": "Sheep",
     "iconID": "monsters_karvis2:8",
     "maxHP": 5,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 0,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 0,
      "max": 1
     },
     "phraseID": "guynmart_sheep_10",
     "droplistID": "guynmart_sheep",
     "attackCost": 5,
     "attackChance": 10,
     "blockChance": 5
    }
    ```


<small>Data from v0.8.18</small>
