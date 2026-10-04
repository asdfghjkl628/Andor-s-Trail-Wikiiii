# ![](../assets/icons/monsters/monsters_tometik1_70.png){ .sprite } Graveyard king

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik1_70.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `graveyardking` |
| **Type** | NPC |
| **Class** | Undead |
| **HP** | 300 |
| **XP when killed** | 984 |
| **Found in** | graveyard1 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 300 |
| Damage | 8 to 25 |
| Attack chance | 175 |
| Block chance | 170 |
| Damage resistance | 12 |
| Max AP | 12 |
| Attack cost | 3 AP |
| Attacks per turn | 4 |
| Move cost | 5 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Crit chance | 9% |

**On hit:** Heal HP: 1 to 4; On target: Putrefaction (magnitude 3, 3 rounds, 50% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Graveyard key](../items/graveyardkey.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 80% | 3000 to 6000 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [graveyard1](../maps/graveyard1.md) | – | 1 | – |


## Quests that count kills

- [Mine for the taking](../quests/graveyard_quest.md#stage-70) with stepping on a trigger on [graveyard1](../maps/graveyard1.md) checks that you've killed at least 1
- [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-240) with stepping on a trigger on [graveyard1](../maps/graveyard1.md) checks that you've killed at least 1


## Quests

- [Mine for the taking](../quests/graveyard_quest.md): stages 60

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Graveyard king. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/graveyardking_1.json" data-npc="Graveyard king" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-graveyardking_1"></span>**`graveyardking_1`** Graveyard king: “[You notice this undead is wearing a key around its neck]” — **effects:** sets stage 60 of [Mine for the taking](../quests/graveyard_quest.md#stage-60)

    - “I've come for the key.” → [graveyardking_2](#d-graveyardking_2)

    <span id="d-graveyardking_2"></span>**`graveyardking_2`** Graveyard king: “You no brain.”

    - “Very well.” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyardking.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyardking.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyardking.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=graveyardking.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `graveyardking` |
    | Spawn group | `graveyardking` |
    | Loot table | `graveyardkingdrop` |
    | Conversation | `graveyardking_1` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_tometik1:70` |
    | Defined in | `res/raw/monsterlist_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "graveyardking",
     "name": "Graveyard king",
     "iconID": "monsters_tometik1:70",
     "maxHP": 300,
     "maxAP": 12,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 8,
      "max": 25
     },
     "spawnGroup": "graveyardking",
     "phraseID": "graveyardking_1",
     "droplistID": "graveyardkingdrop",
     "attackCost": 3,
     "attackChance": 175,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 170,
     "damageResistance": 12,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 4
      },
      "conditionsTarget": [
       {
        "condition": "putrefaction",
        "magnitude": 3,
        "duration": 3,
        "chance": "50"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
