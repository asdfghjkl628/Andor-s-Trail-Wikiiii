# ![](../assets/icons/monsters/monsters_tometik8_41.png){ .sprite } Erwyn's knight

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik8_41.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `erwyn_knight` |
| **Type** | NPC |
| **Class** | Undead |
| **HP** | 75 |
| **XP when killed** | 121 |
| **Found in** | Flagstone Prison |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 75 |
| Damage | 4 to 6 |
| Attack chance | 100 |
| Block chance | 70 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [stoutford_castle0](../maps/stoutford_castle0.md) | Flagstone Prison | 3 | – |
| [stoutford_castle1](../maps/stoutford_castle1.md) | – | 1 | – |
| [waytogalmore0](../maps/waytogalmore0.md) | Flagstone Prison | 1 | – |
| [waytogalmore1](../maps/waytogalmore1.md) | Flagstone Prison | 2 | – |


## Quests that count kills

- [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-46) with stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md), stepping on a trigger on [wild18](../maps/wild18.md) checks that you've killed at least 7
- A conversation with [Colonel Lutarc](../monsters/stn_colonel.md) ([waytogalmore0](../maps/waytogalmore0.md)), stepping on a trigger on [waytogalmore0](../maps/waytogalmore0.md) checks that you've killed at least 1


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Erwyn's knight. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_castle_0.json" data-npc="Erwyn&#x27;s knight" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-stoutford_castle_0"></span>**`stoutford_castle_0`** Erwyn's knight: “Ah another mortal! You shall be another servant in Lord Erwyn's army! Ha Ha!”

    - “No thank you. Maybe another time.” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_knight.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_knight.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_knight.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn_knight.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `erwyn_knight` |
    | Spawn group | `erwyn_knight` |
    | Loot table | – |
    | Conversation | `stoutford_castle_0` |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik8:41` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "erwyn_knight",
     "name": "Erwyn's knight",
     "iconID": "monsters_tometik8:41",
     "maxHP": 75,
     "unique": 1,
     "monsterClass": "undead",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 4,
      "max": 6
     },
     "spawnGroup": "erwyn_knight",
     "phraseID": "stoutford_castle_0",
     "attackCost": 3,
     "attackChance": 100,
     "blockChance": 70
    }
    ```


<small>Data from v0.8.18</small>
