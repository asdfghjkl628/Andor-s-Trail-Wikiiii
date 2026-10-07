---
description: "Ruetmaple is an NPC who can also be fought in Andor's Trail, found in Stoutford."
---

# ![](../assets/icons/monsters/monsters_ld1_65.png){ .sprite } Ruetmaple

**Where to find Ruetmaple:** Stoutford: [Galmore 12](../maps/galmore_12.md#pin-npc-ruetmaple), Stoutford: [Galmore 12a](../maps/galmore_12a.md#pin-npc-ruetmaple), [Galmore 11](../maps/galmore_11.md#pin-npc-ruetmaple)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_65.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Stoutford |
| **Class** | Humanoid |
| **HP** | 50 |
| **XP when defeated** | 163 |
| **Entry ID** | `ruetmaple` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 50 |
| XP when defeated | 163 |
| Damage | 10 to 15 |
| Attack chance | 150 |
| Block chance | 50 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 8 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 3 to 13 |
| [Small rock](../items/rock.md) | 100% | 5 to 9 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 11](../maps/galmore_11.md) | – | 1 | – |
| [Galmore 12](../maps/galmore_12.md) | Stoutford | 1 | – |
| [Galmore 12a](../maps/galmore_12a.md) | Stoutford | 1 | – |

## Quests that count defeats

- A conversation with stepping on a trigger on [Galmore 11](../maps/galmore_11.md) checks that this enemy has been defeated.
- A conversation with stepping on a trigger on [Galmore 12](../maps/galmore_12.md) checks that this enemy has been defeated.
- A conversation with stepping on a trigger on [Galmore 12a](../maps/galmore_12a.md) checks that this enemy has been defeated.

## Dialogue simulator

Set your quest stages and items, then talk to Ruetmaple. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/ruetmaple.json" data-npc="Ruetmaple" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ruetmaple"></span>**`ruetmaple`** Ruetmaple: “Oops - you scared me!”

    - “Are you the one who is throwing rocks down there?” → [ruetmaple_10](#d-ruetmaple_10)

    <span id="d-ruetmaple_10"></span>**`ruetmaple_10`** Ruetmaple: “Yes, no ... go away!”

    - “Stop hurting innocent passers-by.” → [ruetmaple_20](#d-ruetmaple_20)

    <span id="d-ruetmaple_20"></span>**`ruetmaple_20`** Ruetmaple: “I want to be left alone.”

    - “I am leaving now.” → *conversation ends*
    - “Promise me to stop throwing stones, and I will let you go.” → [ruetmaple_22](#d-ruetmaple_22)
    - “You will have peace forever now. Attack!” → [ruetmaple_30](#d-ruetmaple_30)

    <span id="d-ruetmaple_22"></span>**`ruetmaple_22`** Ruetmaple: “Yes, I promise, I promise. Just go, quickly.”

    - “Hey, don't push.” → *conversation ends*
    - “I'll take your word for it.” → *conversation ends*

    <span id="d-ruetmaple_30"></span>**`ruetmaple_30`** Ruetmaple: “No! Please don't do anything to me! I'll promise anything you want. I just want to be left in peace.”

    - “I am leaving now.” → *conversation ends*
    - “Promise me to stop throwing stones, and I let you go.” → [ruetmaple_22](#d-ruetmaple_22)
    - “I don't care about your promises. Attack!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ruetmaple` |
    | Spawn group | `ruetmaple` |
    | Loot table | `ruetmaple` |
    | Conversation | `ruetmaple` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "ruetmaple",
     "name": "Ruetmaple",
     "iconID": "monsters_ld1:65",
     "maxHP": 50,
     "maxAP": 10,
     "moveCost": 8,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 10,
      "max": 15
     },
     "spawnGroup": "ruetmaple",
     "phraseID": "ruetmaple",
     "droplistID": "ruetmaple",
     "attackCost": 5,
     "attackChance": 150,
     "blockChance": 50,
     "damageResistance": 5
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ruetmaple.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ruetmaple.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ruetmaple.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ruetmaple.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
