---
description: "Guardian of the bridge is an NPC who can also be fought in Andor's Trail, found in lodar8."
---

# ![](../assets/icons/monsters/monsters_tometik5_23.png){ .sprite } Guardian of the bridge

**Where to find Guardian of the bridge:** [lodar8](../maps/lodar8.md#pin-npc-lbridge)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik5_23.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | lodar8 |
| **Class** | Giant |
| **HP** | 213 |
| **XP when defeated** | 575 |
| **Entry ID** | `lbridge` |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Giant |
| HP | 213 |
| XP when defeated | 575 |
| Damage | 5 to 15 |
| Attack chance | 127 |
| Block chance | 153 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 35 |
| Critical multiplier | 2.0 |
| Critical hit chance | 21% |

**On hit:** Heal HP: 1; On target: Minor fatigue (magnitude 1, 7 rounds, 30% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 20 to 40 |
| [Liquid courage](../items/pot_courage.md) | 5% | 1 |
| [Greataxe of shattered hope](../items/graxe_shatter.md) | 100% | 1 |
| [Regular potion of health](../items/health.md) | 100% | 3 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [lodar8](../maps/lodar8.md) | – | 1 | – |

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Guardian of the bridge. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/lbridge.json" data-npc="Guardian of the bridge" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lbridge"></span>**`lbridge`** Guardian of the bridge: “You will not pass me.”

    - “Fight!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 30, "c… → {"conditionsTarget": [{"chance": "30", …; name: Guardian of the Bridge → Guardian of the bridge |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `lbridge` |
    | Spawn group | `lbridge` |
    | Loot table | `lbridge` |
    | Conversation | `lbridge` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik5:23` |
    | Defined in | `res/raw/monsterlist_v070_lodarmaze.json` |

    Raw data:

    ```json
    {
     "id": "lbridge",
     "name": "Guardian of the bridge",
     "iconID": "monsters_tometik5:23",
     "maxHP": 213,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 5,
      "max": 15
     },
     "phraseID": "lbridge",
     "droplistID": "lbridge",
     "attackCost": 5,
     "attackChance": 127,
     "criticalSkill": 35,
     "criticalMultiplier": 2.0,
     "blockChance": 153,
     "damageResistance": 9,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      },
      "conditionsTarget": [
       {
        "condition": "fatigue_minor",
        "magnitude": 1,
        "duration": 7,
        "chance": "30"
       }
      ]
     }
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lbridge.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lbridge.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lbridge.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lbridge.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
