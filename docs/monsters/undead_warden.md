# ![](../assets/icons/monsters/monsters_liches_0.png){ .sprite } Undead warden

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_liches_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `undead_warden` |
| **Type** | NPC |
| **Class** | Undead |
| **HP** | 57 |
| **XP when killed** | 113 |
| **Found in** | Flagstone Prison |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 57 |
| Damage | 4 to 8 |
| Attack chance | 120 |
| Block chance | 60 |
| Damage resistance | 1 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 20 |
| Critical multiplier | 2.0 |
| Crit chance | 15% |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 20 to 29 |
| [Sharpened gem](../items/gem4.md) | 100% | 1 |
| [Regular potion of health](../items/health.md) | 100% | 1 |
| [Flagstone Warden's necklace](../items/necklace_flagstone.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [flagstone_upper](../maps/flagstone_upper.md) | Flagstone Prison | 1 | – |


## Quests

- [Ancient secrets](../quests/flagstone.md): stages 31

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Undead warden. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/flagstone_guard0.json" data-npc="Undead warden" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-flagstone_guard0"></span>**`flagstone_guard0`** Undead warden: “Ah, another mortal. Prepare to become part of my undead army!” — **effects:** sets stage 31 of [Ancient secrets](../quests/flagstone.md#stage-31)

    - “Shadow take you.” → *fight starts*
    - “Prepare to die once more.” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | minor data change |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=undead_warden.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=undead_warden.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=undead_warden.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=undead_warden.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `undead_warden` |
    | Spawn group | `flagstone_guard0` |
    | Loot table | `flagstone_guard0` |
    | Conversation | `flagstone_guard0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_liches:0` |
    | Defined in | `res/raw/monsterlist_wilderness.json` |

    Raw data:

    ```json
    {
     "id": "undead_warden",
     "name": "Undead warden",
     "iconID": "monsters_liches:0",
     "maxHP": 57,
     "unique": 1,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 4,
      "max": 8
     },
     "spawnGroup": "flagstone_guard0",
     "phraseID": "flagstone_guard0",
     "droplistID": "flagstone_guard0",
     "attackCost": 5,
     "attackChance": 120,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 60,
     "damageResistance": 1
    }
    ```


<small>Data from v0.8.18</small>
