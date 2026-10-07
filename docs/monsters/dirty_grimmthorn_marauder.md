# ![](../assets/icons/monsters/monsters_newb_1_20.png){ .sprite } Dirty grimmthorn marauder

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_newb_1_20.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `dirty_grimmthorn_marauder` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 370 |
| **XP when killed** | 606 |
| **Found in** | way_to_sullengard_west_0, way_to_sullengard_west_1, way_to_sullengard_west_2 |
| **Introduced** | [v0.8.8](../versions/0.8.8.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 370 |
| Damage | 9 |
| Attack chance | 189 |
| Block chance | 77 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 12 |
| Critical multiplier | 2.25 |
| Crit chance | 10% |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 75% | 4 to 10 |
| [Maul](../items/maul.md) | 3% | 1 |
| [Titanforge stompers](../items/titanforge_stompers.md) | 0.1% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [way_to_sullengard_west_0](../maps/way_to_sullengard_west_0.md) | – | 1 | – |
| [way_to_sullengard_west_1](../maps/way_to_sullengard_west_1.md) | – | 1 | – |
| [way_to_sullengard_west_2](../maps/way_to_sullengard_west_2.md) | – | 1 | – |
| [way_to_sullengard_west_3](../maps/way_to_sullengard_west_3.md) | – | 2 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Dirty grimmthorn marauder. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/dirty_grimmthorn_marauder_1.json" data-npc="Dirty grimmthorn marauder" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-dirty_grimmthorn_marauder_1"></span>**`dirty_grimmthorn_marauder_1`** Dirty grimmthorn marauder: “We are in a rush to get through here, kid. Get out of our way or die.”

    - “Where is the Shadow to help me now?” → *fight starts*
    - “Please don't hurt me.” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dirty_grimmthorn_marauder.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dirty_grimmthorn_marauder.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dirty_grimmthorn_marauder.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=dirty_grimmthorn_marauder.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `dirty_grimmthorn_marauder` |
    | Spawn group | `dirty_grimmthorn_marauder` |
    | Loot table | `dirty_grimmthorn_marauder_dl` |
    | Conversation | `dirty_grimmthorn_marauder_1` |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_newb_1:20` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "dirty_grimmthorn_marauder",
     "name": "Dirty grimmthorn marauder",
     "iconID": "monsters_newb_1:20",
     "maxHP": 370,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 9,
      "max": 9
     },
     "phraseID": "dirty_grimmthorn_marauder_1",
     "droplistID": "dirty_grimmthorn_marauder_dl",
     "attackCost": 5,
     "attackChance": 189,
     "criticalSkill": 12,
     "criticalMultiplier": 2.25,
     "blockChance": 77,
     "damageResistance": 9
    }
    ```


<small>Data from v0.8.18</small>
