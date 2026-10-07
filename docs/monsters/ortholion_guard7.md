---
description: "Confused Feygard soldier is an NPC who can also be fought in Andor's Trail, found in Elm mine 2."
---

# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Confused Feygard soldier

**Where to find Confused Feygard soldier:** [Elm mine 2](../maps/elm_mine2.md#pin-npc-ortholion_guard7)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Elm mine 2 |
| **Class** | Humanoid |
| **HP** | 211 |
| **XP when defeated** | 342 |
| **Entry ID** | `ortholion_guard7` |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 211 |
| XP when defeated | 342 |
| Damage | 2 to 18 |
| Attack chance | 91 |
| Block chance | 110 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 7 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 1 to 50 |
| [Worn iron boots](../items/hboot_wirn.md) | 25% | 1 |
| [Hardened iron sword](../items/sword_hard_iron.md) | 25% | 1 |
| [Crude iron helmet](../items/helm_crude_iron.md) | 25% | 1 |
| [Ring of damage +1](../items/ring_dmg1.md) | 25% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Elm mine 2](../maps/elm_mine2.md) | – | 1 | – |

## Dialogue simulator

Set your quest stages and items, then talk to Confused Feygard soldier. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/ortholion_guard7.json" data-npc="Confused Feygard soldier" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ortholion_guard7"></span>**`ortholion_guard7`** Confused Feygard soldier: “HAH! I SPOTTED YOU, EVIL BEING! *raises his sword*”

    - “I'm not a threat, stop!” → [ortholion_guard7_10](#d-ortholion_guard7_10)
    - “This one won't be my fault.” → [ortholion_guard7_10](#d-ortholion_guard7_10)
    - “Hah! I spotted you, useless soldier!” → [ortholion_guard7_10](#d-ortholion_guard7_10)

    <span id="d-ortholion_guard7_10"></span>**`ortholion_guard7_10`** *(silent check: the first matching branch below is taken)* — **effects:** removes monsters from elm_mine2

    - Next → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 1 line added |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 1 line added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ortholion_guard7` |
    | Spawn group | `ortholion_guard7` |
    | Loot table | `ortholion_guard7` |
    | Conversation | `ortholion_guard7` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "ortholion_guard7",
     "name": "Confused Feygard soldier",
     "iconID": "monsters_rltiles3:14",
     "maxHP": 211,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 2,
      "max": 18
     },
     "spawnGroup": "ortholion_guard7",
     "phraseID": "ortholion_guard7",
     "droplistID": "ortholion_guard7",
     "attackCost": 7,
     "attackChance": 91,
     "blockChance": 110,
     "damageResistance": 2
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard7.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
