# ![](../assets/icons/monsters/monsters_men2_9.png){ .sprite } Shady bandit

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men2_9.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `shady_bandit` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 45 |
| **XP when killed** | 94 |
| **Found in** | Fallhaven |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 45 |
| Damage | 3 to 9 |
| Attack chance | 70 |
| Block chance | 50 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 30 |
| Critical multiplier | 3.0 |
| Crit chance | 19% |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 4 to 41 |
| [Piece of Vacor's spell](../items/vacor_spell.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [fallhaven_se](../maps/fallhaven_se.md) | Fallhaven | 1 | – |
| [wild10](../maps/wild10.md) | Fallhaven | 1 | – |
| [wild12](../maps/wild12.md) | Fallhaven | 1 | – |
| [wild9](../maps/wild9.md) | Fallhaven | 1 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Shady bandit. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/fallhaven_bandit.json" data-npc="Shady bandit" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-fallhaven_bandit"></span>**`fallhaven_bandit`** Shady bandit: “Get lost kid. I don't have time for you.”

    - “I'm looking for a piece of the Rift spell.” *(if reached stage 20 of [Missing pieces](../quests/vacor.md#stage-20))* → [fallhaven_bandit_2](#d-fallhaven_bandit_2)

    <span id="d-fallhaven_bandit_2"></span>**`fallhaven_bandit_2`** Shady bandit: “No! Vacor will not gain the power of the rift spell!”

    - “Let's fight!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | name: Shady Bandit → Shady bandit<br>Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shady_bandit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shady_bandit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shady_bandit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shady_bandit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `shady_bandit` |
    | Spawn group | `fallhaven_bandit` |
    | Loot table | `fallhaven_bandit` |
    | Conversation | `fallhaven_bandit` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:9` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "shady_bandit",
     "name": "Shady bandit",
     "iconID": "monsters_men2:9",
     "maxHP": 45,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 9
     },
     "spawnGroup": "fallhaven_bandit",
     "phraseID": "fallhaven_bandit",
     "droplistID": "fallhaven_bandit",
     "attackCost": 5,
     "attackChance": 70,
     "criticalSkill": 30,
     "criticalMultiplier": 3.0,
     "blockChance": 50,
     "damageResistance": 2
    }
    ```


<small>Data from v0.8.18</small>
