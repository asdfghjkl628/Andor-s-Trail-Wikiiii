# ![](../assets/icons/monsters/monsters_omi2_7.png){ .sprite } Shadowfang

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_omi2_7.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `shadowfang1` |
| **Type** | NPC |
| **Class** | Demon |
| **HP** | 98 |
| **XP when killed** | 330 |
| **Found in** | blackwater_mountain76, elm_2f_1, elm_2f_3 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 98 |
| Damage | 3 to 21 |
| Attack chance | 130 |
| Block chance | 110 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 2 AP |
| Critical skill | 10 |
| Critical multiplier | 2.0 |
| Crit chance | 9% |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.

**On hit:** Heal HP: 0 to 3; On target: Venom (magnitude 2, 4 rounds, 10% chance); Vulnerability (magnitude 3, 3 rounds, 10% chance); Bleeding wound (magnitude 3, 2 rounds, 5% chance)

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 1 to 72 |
| [Azure gem](../items/gem6.md) | 100% | 1 to 3 |
| [Ruby gem](../items/gem2.md) | 50% | 1 to 5 |
| [Contaminated poison gland](../items/gland2.md) | 25% | 1 to 2 |
| [Empty potion bottle](../items/vial_empty4.md) | 33.3333% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain76](../maps/blackwater_mountain76.md) | – | 2 | appears later in a quest |
| [elm_2f_1](../maps/elm_2f_1.md) | – | 1 | – |
| [elm_2f_3](../maps/elm_2f_3.md) | – | 1 | – |
| [elm_4f_1](../maps/elm_4f_1.md) | – | 1 | – |
| [elm_4f_5](../maps/elm_4f_5.md) | – | 1 | – |
| [elm_mine3](../maps/elm_mine3.md) | – | 2 | appears later in a quest |
| [elm_mine5](../maps/elm_mine5.md) | – | 3 | – |


## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Shadowfang. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/shadowfang_1.json" data-npc="Shadowfang" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-shadowfang_1"></span>**`shadowfang_1`** Shadowfang: “Sssssh...”

    - “What the...?” → *fight starts*
    - “Hey, have you seen my brother Andor?” → *fight starts*
    - “For the shadow!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shadowfang1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shadowfang1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shadowfang1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shadowfang1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `shadowfang1` |
    | Spawn group | `shadowfang` |
    | Loot table | `shadowfang1` |
    | Conversation | `shadowfang_1` |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_omi2:7` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "shadowfang1",
     "name": "Shadowfang",
     "iconID": "monsters_omi2:7",
     "maxHP": 98,
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "demon",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 3,
      "max": 21
     },
     "spawnGroup": "shadowfang",
     "faction": "",
     "phraseID": "shadowfang_1",
     "droplistID": "shadowfang1",
     "attackCost": 5,
     "attackChance": 130,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 110,
     "damageResistance": 9,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 0,
       "max": 3
      },
      "conditionsTarget": [
       {
        "condition": "venom",
        "magnitude": 2,
        "duration": 4,
        "chance": "10"
       },
       {
        "condition": "vulnerability",
        "magnitude": 3,
        "duration": 3,
        "chance": "10"
       },
       {
        "condition": "bleeding_wound",
        "magnitude": 3,
        "duration": 2,
        "chance": "5"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
