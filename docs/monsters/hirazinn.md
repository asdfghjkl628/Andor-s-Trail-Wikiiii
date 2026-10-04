# ![](../assets/icons/monsters/monsters_demon2_0.png){ .sprite } Hira'zinn

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_demon2_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `hirazinn` |
| **Type** | NPC |
| **Class** | Demon |
| **HP** | 263 |
| **XP when killed** | 683 |
| **Found in** | lodarcave4a |
| **Immune to crits** | Yes |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 263 |
| Damage | 3 to 6 |
| Attack chance | 129 |
| Block chance | 132 |
| Damage resistance | 21 |
| Max AP | 10 |
| Attack cost | 2 AP |
| Attacks per turn | 5 |
| Move cost | 5 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Crit chance | 9% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.

**On hit:** Heal HP: 1 to 6; On target: Fear (magnitude 4, 3 rounds, 30% chance); Bleeding wound (magnitude 3, 3 rounds, 30% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Heart of the Hira'zinn](../items/hirazinn.md) | 100% | 1 |
| [Shadowstalker](../items/shdstlk.md) | 100% | 1 |
| [Broken sword](../items/xulviir0.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 200 to 500 |
| [Glass gem](../items/gem1.md) | 100% | 1 to 3 |
| [Bone](../items/bone.md) | 100% | 0 to 4 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [lodarcave4a](../maps/lodarcave4a.md) | – | 1 | – |


## Quests

- [Searching for madness](../quests/lodar2.md): stages 40

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Hira'zinn. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/hirazinn.json" data-npc="Hira&#x27;zinn" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-hirazinn"></span>**`hirazinn`** Hira'zinn: “[The foul creature swings its many arms at you, while giving away a high-pitched shrieking sound]”

    - Next → [hirazinn_1](#d-hirazinn_1)

    <span id="d-hirazinn_1"></span>**`hirazinn_1`** Hira'zinn: “[The piercing noise fills your head with a mind-numbing headache]”

    - Next → [hirazinn_2](#d-hirazinn_2)

    <span id="d-hirazinn_2"></span>**`hirazinn_2`** Hira'zinn: “[You also feel a strong urge to leave this place]” — **effects:** sets stage 40 of [Searching for madness](../quests/lodar2.md#stage-40)

    - “[Run away screaming]” → *conversation ends*
    - “[Attack]” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 30, "c… → {"conditionsTarget": [{"chance": "30", …; size removed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirazinn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirazinn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirazinn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hirazinn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `hirazinn` |
    | Spawn group | `hirazinn` |
    | Loot table | `hirazinn` |
    | Conversation | `hirazinn` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_demon2:0` |
    | Defined in | `res/raw/monsterlist_v070_lodarcave.json` |

    Raw data:

    ```json
    {
     "id": "hirazinn",
     "name": "Hira'zinn",
     "iconID": "monsters_demon2:0",
     "maxHP": 263,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "demon",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "phraseID": "hirazinn",
     "droplistID": "hirazinn",
     "attackCost": 2,
     "attackChance": 129,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 132,
     "damageResistance": 21,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 6
      },
      "conditionsTarget": [
       {
        "condition": "fear",
        "magnitude": 4,
        "duration": 3,
        "chance": "30"
       },
       {
        "condition": "bleeding_wound",
        "magnitude": 3,
        "duration": 3,
        "chance": "30"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
