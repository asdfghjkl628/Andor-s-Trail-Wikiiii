---
description: "Thukuzun is an NPC who can also be fought in Andor's Trail, found in lostmine11."
---

# ![](../assets/icons/monsters/monsters_rltiles1_123.png){ .sprite } Thukuzun

**Where to find Thukuzun:** [lostmine11](../maps/lostmine11.md#pin-npc-thukuzun)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_123.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | lostmine11 |
| **Class** | Undead |
| **HP** | 193 |
| **XP when defeated** | 564 |
| **Entry ID** | `thukuzun` |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 193 |
| XP when defeated | 564 |
| Damage | 6 to 25 |
| Attack chance | 136 |
| Block chance | 140 |
| Damage resistance | 9 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |

**On hit:** On target: Ablaze (magnitude 3, 7 rounds, 30% chance)


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Blade of the defiler](../items/blade_defiler.md) | 100% | 1 |
| [Thukuzun bone](../items/thukuzun.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 200 to 500 |
| [Glass gem](../items/gem1.md) | 100% | 1 to 3 |
| [Bone](../items/bone.md) | 100% | 2 to 8 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [lostmine11](../maps/lostmine11.md) | – | 1 | – |

## Quests

- [Trial by fire](../quests/charwood2.md): stage 30

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Thukuzun. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/thukuzun.json" data-npc="Thukuzun" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-thukuzun"></span>**`thukuzun`** Thukuzun: “Ah, another mortal that has come to bow before the might of Thukuzun.” — **effects:** sets stage 30 of [Trial by fire](../quests/charwood2.md#stage-30)

    - Next → [thukuzun_1](#d-thukuzun_1)

    <span id="d-thukuzun_1"></span>**`thukuzun_1`** Thukuzun: “You will be a fine specimen in my army of bones.”

    - “I'll defeat you, foul beast!” → *fight starts*
    - “Fight!” → *fight starts*
    - “Your bones will be a fine specimen in my collection.” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 30, "c… → {"conditionsTarget": [{"chance": "30", … |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `thukuzun` |
    | Spawn group | `thukuzun` |
    | Loot table | `thukuzun` |
    | Conversation | `thukuzun` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:123` |
    | Defined in | `res/raw/monsterlist_v070_charwood2.json` |

    Raw data:

    ```json
    {
     "id": "thukuzun",
     "name": "Thukuzun",
     "iconID": "monsters_rltiles1:123",
     "maxHP": 193,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 6,
      "max": 25
     },
     "phraseID": "thukuzun",
     "droplistID": "thukuzun",
     "attackCost": 3,
     "attackChance": 136,
     "blockChance": 140,
     "damageResistance": 9,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "fire",
        "magnitude": 3,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thukuzun.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thukuzun.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thukuzun.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=thukuzun.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
