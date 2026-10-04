# ![](../assets/icons/monsters/monsters_omi1_0.png){ .sprite } Feygard scout

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_omi1_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `feygard_scout` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 83 |
| **XP when killed** | 209 |
| **Found in** | Crossroads Guardhouse |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 83 |
| Damage | 6 to 11 |
| Attack chance | 110 |
| Block chance | 95 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 25 |
| Critical multiplier | 2.5 |
| Crit chance | 17% |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Fanamor's Journal](../items/Fanamor_journal.md) | 100% | 1 |
| [Feygard iron dagger](../items/feygard_iron_dagger.md) | 100% | 1 |
| [Polished gem](../items/gem3.md) | 100% | 1 to 3 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [crossroads](../maps/crossroads.md) | Crossroads Guardhouse | 1 | appears later in a quest |


## Quests that count kills

- A conversation with [Fanamor](../monsters/fanamor.md) ([crossroads](../maps/crossroads.md)) checks that you've killed at least 1


## Quests

- [Thief apprentice](../quests/Thieves01.md): stages 40

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Feygard scout. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/feygard_scout_3.json" data-npc="Feygard scout" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-feygard_scout_3"></span>**`feygard_scout_3`** [Feygard scout](../monsters/feygard_scout.md): “(Grabs the book) What have we here? A lost kid trying to do business with this scum, hah? You are under arrest!” — **effects:** sets stage 40 of [Thief apprentice](../quests/Thieves01.md#stage-40)

    - “Not without a fight!” → *fight starts*
    - “How dare you! Prepare to die, useless soldier!” → *fight starts*
    - “For the shadow!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_scout.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_scout.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_scout.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_scout.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `feygard_scout` |
    | Spawn group | `feygard_scout` |
    | Loot table | `Feygard_scout` |
    | Conversation | `feygard_scout_3` |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_omi1:0` |
    | Defined in | `res/raw/monsterlist_omicronrg9.json` |

    Raw data:

    ```json
    {
     "id": "feygard_scout",
     "name": "Feygard scout",
     "iconID": "monsters_omi1:0",
     "maxHP": 83,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 6,
      "max": 11
     },
     "spawnGroup": "feygard_scout",
     "phraseID": "feygard_scout_3",
     "droplistID": "Feygard_scout",
     "attackCost": 5,
     "attackChance": 110,
     "criticalSkill": 25,
     "criticalMultiplier": 2.5,
     "blockChance": 95,
     "damageResistance": 5
    }
    ```


<small>Data from v0.8.18</small>
