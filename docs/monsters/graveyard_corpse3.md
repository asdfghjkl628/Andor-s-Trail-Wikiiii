# ![](../assets/icons/monsters/monsters_zombie2_0.png){ .sprite } Angry graveyard corpse

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_zombie2_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `graveyard_corpse3` |
| **Type** | NPC |
| **Class** | Undead |
| **HP** | 90 |
| **XP when killed** | 447 |
| **Found in** | graveyard0 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 90 |
| Damage | 6 to 19 |
| Attack chance | 170 |
| Block chance | 165 |
| Damage resistance | 11 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 3 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Crit chance | 9% |

**On hit:** Heal HP: 1 to 3; On target: Putrefaction (magnitude 2, 3 rounds, 30% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 200 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [graveyard0](../maps/graveyard0.md) | – | 1 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Angry graveyard corpse. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/graveyard_corpse1.json" data-npc="Angry graveyard corpse" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-graveyard_corpse1"></span>**`graveyard_corpse1`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 90 of [Mine for the taking](../quests/graveyard_quest.md#stage-90); NOT reached stage 95 of [Mine for the taking](../quests/graveyard_quest.md#stage-95))* → [graveyard_corpse2](#d-graveyard_corpse2)

    <span id="d-graveyard_corpse2"></span>**`graveyard_corpse2`** Angry graveyard corpse: “You have small brain but small brain better than no brain. ARGH!!!”

    - “Small brain??” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 2 lines added |
| [v0.7.12](../versions/0.7.12.md) | droplistID added (gold200); maxAP added (10); movementAggressionType removed; phraseID added (graveyard_corpse1) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_corpse3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_corpse3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_corpse3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyard_corpse3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `graveyard_corpse3` |
    | Spawn group | `graveyard_corpse3` |
    | Loot table | `gold200` |
    | Conversation | `graveyard_corpse1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_zombie2:0` |
    | Defined in | `res/raw/monsterlist_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "graveyard_corpse3",
     "name": "Angry graveyard corpse",
     "iconID": "monsters_zombie2:0",
     "maxHP": 90,
     "maxAP": 10,
     "moveCost": 3,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 6,
      "max": 19
     },
     "spawnGroup": "graveyard_corpse3",
     "phraseID": "graveyard_corpse1",
     "droplistID": "gold200",
     "attackCost": 3,
     "attackChance": 170,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 165,
     "damageResistance": 11,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 3
      },
      "conditionsTarget": [
       {
        "condition": "putrefaction",
        "magnitude": 2,
        "duration": 3,
        "chance": "30"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
