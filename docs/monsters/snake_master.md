# ![](../assets/icons/monsters/monsters_liches_1.png){ .sprite } Snake master

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_liches_1.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `snake_master` |
| **Type** | NPC |
| **Class** | Undead |
| **HP** | 55 |
| **XP when killed** | 112 |
| **Found in** | snakecave3 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 55 |
| Damage | 1 to 4 |
| Attack chance | 60 |
| Block chance | 10 |
| Damage resistance | 4 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 200 |
| Critical multiplier | 3.0 |
| Crit chance | 58% |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 9 |
| [Venomous Dagger](../items/dagger_venom.md) | 100% | 1 |
| [Polished gem](../items/gem3.md) | 100% | 1 |
| [Regular potion of health](../items/health.md) | 100% | 1 |
| [Ewmondold's map](../items/inspiring_snake_master_map.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [snakecave3](../maps/snakecave3.md) | – | 1 | – |


## Quests that count kills

- [Perception is not reality](../quests/new_snake_master.md#stage-10) with [Ewmondold](../monsters/inspiring_snake_master.md) ([wild2](../maps/wild2.md)) checks that you've killed at least 1
- [Perception is not reality](../quests/new_snake_master.md#stage-20) with [Ewmondold](../monsters/inspiring_snake_master.md) ([wild2](../maps/wild2.md)) checks that you've killed at least 1


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Snake master. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/snakemaster.json" data-npc="Snake master" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-snakemaster"></span>**`snakemaster`** Snake master: “Well well, what have we here? A visitor, how nice. I'm impressed you got this far through all my minions. Now prepare to die, puny creature.”

    - “Great, I have been waiting for a fight!” → *fight starts*
    - “Let's see who dies here.” → *fight starts*
    - “Please don't hurt me!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `snake_master` |
    | Spawn group | `cavesnake3_boss` |
    | Loot table | `snakemaster` |
    | Conversation | `snakemaster` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_liches:1` |
    | Defined in | `res/raw/monsterlist_crossglen_animals.json` |

    Raw data:

    ```json
    {
     "id": "snake_master",
     "name": "Snake master",
     "iconID": "monsters_liches:1",
     "maxHP": 55,
     "unique": 1,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 1,
      "max": 4
     },
     "spawnGroup": "cavesnake3_boss",
     "phraseID": "snakemaster",
     "droplistID": "snakemaster",
     "attackCost": 5,
     "attackChance": 60,
     "criticalSkill": 200,
     "criticalMultiplier": 3.0,
     "blockChance": 10,
     "damageResistance": 4
    }
    ```


<small>Data from v0.8.18</small>
