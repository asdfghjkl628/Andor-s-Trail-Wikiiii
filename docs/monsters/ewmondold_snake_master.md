# ![](../assets/icons/monsters/monsters_tometik1_18.png){ .sprite } Ewmondold

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik1_18.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `ewmondold_snake_master` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 70 |
| **XP when killed** | 150 |
| **Found in** | snakecave3 |
| **Introduced** | [v0.7.12](../versions/0.7.12.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 70 |
| Damage | 2 to 5 |
| Attack chance | 67 |
| Block chance | 13 |
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
| [Gold coins](../items/gold.md) | 100% | 200 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [snakecave3](../maps/snakecave3.md) | – | 1 | appears later in a quest |


## Quests that count kills

- A conversation with [Arcir](../monsters/arcir.md) checks that you've killed at least 1
- A conversation with stepping on a trigger on [snakecave3](../maps/snakecave3.md) checks that you've killed at least 1


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Ewmondold. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/ewmondold_snake_master_10.json" data-npc="Ewmondold" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ewmondold_snake_master_10"></span>**`ewmondold_snake_master_10`** Ewmondold: “My new powers have enhanced my appearance, don't you agree?”

    - “You are too dangerous to be kept alive.” → [ewmondold_snake_master_20](#d-ewmondold_snake_master_20)

    <span id="d-ewmondold_snake_master_20"></span>**`ewmondold_snake_master_20`** Ewmondold: “Oh, you think you can stop me, do you? Come and try!”

    - “I won't try, I'll succeed!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ewmondold_snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ewmondold_snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ewmondold_snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ewmondold_snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `ewmondold_snake_master` |
    | Spawn group | `ewmondold_snake_master` |
    | Loot table | `gold200` |
    | Conversation | `ewmondold_snake_master_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik1:18` |
    | Defined in | `res/raw/monsterlist_brimhaven_2.json` |

    Raw data:

    ```json
    {
     "id": "ewmondold_snake_master",
     "name": "Ewmondold",
     "iconID": "monsters_tometik1:18",
     "maxHP": 70,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 5
     },
     "phraseID": "ewmondold_snake_master_10",
     "droplistID": "gold200",
     "attackCost": 5,
     "attackChance": 67,
     "criticalSkill": 200,
     "criticalMultiplier": 3.0,
     "blockChance": 13,
     "damageResistance": 4
    }
    ```


<small>Data from v0.8.18</small>
