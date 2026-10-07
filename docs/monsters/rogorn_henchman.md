# ![](../assets/icons/monsters/monsters_rogue1_0.png){ .sprite } Rogorn's henchman

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rogue1_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `rogorn_henchman` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 130 |
| **XP when killed** | 259 |
| **Found in** | Crossroads Guardhouse |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 130 |
| Damage | 5 to 8 |
| Attack chance | 80 |
| Block chance | 120 |
| Damage resistance | 4 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 20 |
| [Piece of painting](../items/rogorn_qitem.md) | 100% | 1 |
| [Minor vial of health](../items/health_minor.md) | 100% | 1 to 2 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [roadtocarntower2](../maps/roadtocarntower2.md) | Crossroads Guardhouse | 2 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Rogorn's henchman. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/rogorn_henchman.json" data-npc="Rogorn&#x27;s henchman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-rogorn_henchman"></span>**`rogorn_henchman`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 40 of [The path is clear to me](../quests/rogorn.md#stage-40))* → [rogorn_henchman_atk](#d-rogorn_henchman_atk)
    - branch 2 *(if reached stage 45 of [The path is clear to me](../quests/rogorn.md#stage-45))* → [rogorn_henchman_noatk](#d-rogorn_henchman_noatk)
    - branch 3 → [rogorn_henchman_1](#d-rogorn_henchman_1)

    <span id="d-rogorn_henchman_atk"></span>**`rogorn_henchman_atk`** Rogorn's henchman: “For the Shadow!”

    - “Fight” → *fight starts*

    <span id="d-rogorn_henchman_noatk"></span>**`rogorn_henchman_noatk`** Rogorn's henchman: “Good to hear that there are at least a few people left out there willing to take a stand against Feygard.”


    <span id="d-rogorn_henchman_1"></span>**`rogorn_henchman_1`** Rogorn's henchman: “Should you really be out here all by yourself?”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rogorn_henchman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rogorn_henchman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rogorn_henchman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=rogorn_henchman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `rogorn_henchman` |
    | Spawn group | `rogorn_henchman` |
    | Loot table | `rogorn_henchman` |
    | Conversation | `rogorn_henchman` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rogue1:0` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "rogorn_henchman",
     "name": "Rogorn's henchman",
     "iconID": "monsters_rogue1:0",
     "maxHP": 130,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 5,
      "max": 8
     },
     "spawnGroup": "rogorn_henchman",
     "phraseID": "rogorn_henchman",
     "droplistID": "rogorn_henchman",
     "attackCost": 3,
     "attackChance": 80,
     "blockChance": 120,
     "damageResistance": 4
    }
    ```


<small>Data from v0.8.18</small>
