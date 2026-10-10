---
description: "Galmore wolf's pup is an NPC you can also fight in Andor's Trail, found in Mt. Galmore."
---

# ![](../assets/icons/monsters/monsters_tometik10_75.png){ .sprite } Galmore wolf's pup

**Where to find Galmore wolf's pup:** Mt. Galmore: [Galmore 54](../maps/galmore_54.md#pin-npc-mg2_wolves_pup)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik10_75.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Mt. Galmore |
| **Class** | Animal |
| **HP** | 187 |
| **XP when defeated** | 459 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

!!! warning "You can fight Galmore wolf's pup"
    Answering “Kill!” starts a fight with Galmore wolf's pup.

    Galmore wolf's pup turns hostile if you fall out with their faction.

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 187 |
| XP when defeated | 459 |
| Damage | 10 to 13 |
| AC | 156 |
| BC | 187 |
| DR | 0 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | 5% (×2.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Warg veal](../items/warg_veal.md) | 8% | 1 |
| [Red apple](../items/apple_red.md) | 15% | 1 |

## Quests

- [Unusual experiences and achievements](../quests/achievements.md): stage 200

## Dialogue simulator

Talk to Galmore wolf's pup as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/mg2_wolves_pup.json" data-npc="Galmore wolf&#x27;s pup" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-mg2_wolves_pup"></span>**`mg2_wolves_pup`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if wearing [Wolfpack's animal hide](../items/packhide.md))* → [mg2_wolves_pup_1](#d-mg2_wolves_pup_1)
    - branch 2 → [mg2_wolves_pup_2](#d-mg2_wolves_pup_2)

    <span id="d-mg2_wolves_pup_1"></span>**`mg2_wolves_pup_1`** Galmore wolf's pup: “Yelp - don't hurt us, big wolf.” — **effects:** sets stage 200 of [Unusual experiences and achievements](../quests/achievements.md#stage-200)

    - “Grrr, grrr” → *NPC leaves*
    - “Move out of my way!” → *NPC leaves*

    <span id="d-mg2_wolves_pup_2"></span>**`mg2_wolves_pup_2`** Galmore wolf's pup: “Help! It's a two-leg!” — **effects:** faction “mg2_wolves_faction” set to -666

    - “Kill!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

- `mg2_wolves_pup` belongs to the faction `mg2_wolves_faction`. The game treats any character as hostile once your standing with its faction is below zero.

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `mg2_wolves_pup` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `mg2_wolves_pup` |
    | Loot table | `orphaned_warg_pup_dl` |
    | Conversation | `mg2_wolves_pup` |
    | Faction | `mg2_wolves_faction` |
    | Movement | protectSpawn |
    | Icon | `monsters_tometik10:75` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "mg2_wolves_pup",
     "name": "Galmore wolf's pup",
     "iconID": "monsters_tometik10:75",
     "maxHP": 187,
     "moveCost": 3,
     "monsterClass": "animal",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 10,
      "max": 13
     },
     "faction": "mg2_wolves_faction",
     "phraseID": "mg2_wolves_pup",
     "droplistID": "orphaned_warg_pup_dl",
     "attackCost": 4,
     "attackChance": 156,
     "criticalSkill": 5,
     "criticalMultiplier": 2.0,
     "blockChance": 187
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves_pup.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves_pup.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves_pup.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves_pup.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
