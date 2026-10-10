---
description: "Rebelled thief is an NPC you can also fight in Andor's Trail, found in Crackshot hideout 2, Crackshot hideout 3."
---

# ![](../assets/icons/monsters/monsters_ld1_65.png){ .sprite } Rebelled thief

**Where to find Rebelled thief:** [Crackshot hideout 2](../maps/crackshot_hideout2.md#pin-npc-guild03_rebthief_1), [Crackshot hideout 3](../maps/crackshot_hideout3.md#pin-npc-guild03_rebthief_1)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_65.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Crackshot hideout 2, Crackshot hideout 3 |
| **Class** | Humanoid |
| **HP** | 60 |
| **XP when defeated** | 114 |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

!!! warning "You can fight Rebelled thief"
    Answering “The people you've killed will be avenged.” starts a fight with Rebelled thief.

    Rebelled thief turns hostile if you fall out with their faction.

## Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 60 |
| XP when defeated | 114 |
| Damage | 3 to 8 |
| AC | 105 |
| BC | 85 |
| DR | 1 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 9% (×2.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Wooden buckler](../items/shield1.md) | 20% | 1 |
| [Ruby gem](../items/gem2.md) | 50% | 1 to 2 |
| [Leather boots](../items/boots1.md) | 20% | 1 |
| [Gold coins](../items/gold.md) | 75% | 25 to 50 |
| [Iron dagger](../items/dagger0.md) | 25% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Crackshot hideout 2](../maps/crackshot_hideout2.md) | – | 2 | – |
| [Crackshot hideout 3](../maps/crackshot_hideout3.md) | – | 4 | – |

## Dialogue simulator

Talk to Rebelled thief as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/rebthief_guild03_1.json" data-npc="Rebelled thief" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-rebthief_guild03_1"></span>**`rebthief_guild03_1`** Rebelled thief: “Another idiot trying to pass through here, eh? Your life ends here!” — **effects:** faction “rebthief_guild03_1” set to -10

    - “The people you've killed will be avenged.” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

- `guild03_rebthief_1` belongs to the faction `rebthief_guild03_1`. The game treats any character as hostile once your standing with its faction is below zero.

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `guild03_rebthief_1` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `g03_thief_1` |
    | Loot table | `drop_g03_rebthief_1` |
    | Conversation | `rebthief_guild03_1` |
    | Faction | `rebthief_guild03_1` |
    | Movement | helpOthers |
    | Icon | `monsters_ld1:65` |
    | Defined in | `res/raw/monsterlist_omicronrg9.json` |

    Raw data:

    ```json
    {
     "id": "guild03_rebthief_1",
     "name": "Rebelled thief",
     "iconID": "monsters_ld1:65",
     "maxHP": 60,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 3,
      "max": 8
     },
     "spawnGroup": "g03_thief_1",
     "faction": "rebthief_guild03_1",
     "phraseID": "rebthief_guild03_1",
     "droplistID": "drop_g03_rebthief_1",
     "attackCost": 5,
     "attackChance": 105,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 85,
     "damageResistance": 1
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guild03_rebthief_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guild03_rebthief_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guild03_rebthief_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guild03_rebthief_1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
