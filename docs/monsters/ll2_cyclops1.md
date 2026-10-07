# ![](../assets/icons/monsters/monsters_ld1_37.png){ .sprite } Polyasem

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_37.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `ll2_cyclops1` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 100 |
| **XP when killed** | 194 |
| **Found in** | ll2_cyclops_cave, mountainlake27 |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 100 |
| Damage | 8 to 16 |
| Attack chance | 100 |
| Block chance | 50 |
| Damage resistance | 10 |
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
| [ll2_cyclops_cave](../maps/ll2_cyclops_cave.md) | – | 1 | – |
| [mountainlake27](../maps/mountainlake27.md) | – | 1 | appears later in a quest |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Polyasem. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/ll2_cyclops.json" data-npc="Polyasem" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ll2_cyclops"></span>**`ll2_cyclops`** Polyasem: “Ah, there is Nobody. You think you're particularly clever, don't you?”

    - “Well, it has worked with your brother.” → [ll2_cyclops_10](#d-ll2_cyclops_10)

    <span id="d-ll2_cyclops_10"></span>**`ll2_cyclops_10`** Polyasem: “Now let go of the ram and act like a man, kid.”

    - “Well, you'll see what you get for it. Attack!” → [ll2_cyclops_20](#d-ll2_cyclops_20)

    <span id="d-ll2_cyclops_20"></span>**`ll2_cyclops_20`** Polyasem: “Our brother has made us a magnificant gift: We get to hunt our own holiday roast...” — **effects:** spawns monsters on mountainlake27, faction “ll2_cyclops” set to -1

    - Next → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_cyclops1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_cyclops1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_cyclops1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ll2_cyclops1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `ll2_cyclops1` |
    | Spawn group | `ll2_cyclops1` |
    | Loot table | – |
    | Conversation | `ll2_cyclops` |
    | Faction | `ll2_cyclops` |
    | Movement | – |
    | Icon | `monsters_ld1:37` |
    | Defined in | `res/raw/monsterlist_lake_laeroth_2.json` |

    Raw data:

    ```json
    {
     "id": "ll2_cyclops1",
     "name": "Polyasem",
     "iconID": "monsters_ld1:37",
     "maxHP": 100,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 8,
      "max": 16
     },
     "spawnGroup": "ll2_cyclops1",
     "faction": "ll2_cyclops",
     "phraseID": "ll2_cyclops",
     "attackCost": 10,
     "attackChance": 100,
     "blockChance": 50,
     "damageResistance": 10
    }
    ```


<small>Data from v0.8.18</small>
