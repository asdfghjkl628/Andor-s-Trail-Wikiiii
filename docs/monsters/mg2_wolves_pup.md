---
description: "Galmore wolf's pup is an NPC who can also be fought in Andor's Trail, found in Mt. Galmore."
---

# ![](../assets/icons/monsters/monsters_tometik10_75.png){ .sprite } Galmore wolf's pup

**Where to find Galmore wolf's pup:** Mt. Galmore: [galmore_54](../maps/galmore_54.md#pin-npc-mg2_wolves_pup)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik10_75.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Mt. Galmore |
| **Class** | Animal |
| **HP** | 187 |
| **XP when defeated** | 459 |
| **Entry ID** | `mg2_wolves_pup` |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 187 |
| XP when defeated | 459 |
| Damage | 10 to 13 |
| Attack chance | 156 |
| Block chance | 187 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 3 AP |
| Critical skill | 5 |
| Critical multiplier | 2.0 |
| Critical hit chance | 5% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Warg veal](../items/warg_veal.md) | 8% | 1 |
| [Red apple](../items/apple_red.md) | 15% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [galmore_54](../maps/galmore_54.md) | Mt. Galmore | 16 | – |

## Quests

- [Unusual experiences and achievements](../quests/achievements.md): stage 200

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Galmore wolf's pup. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/mg2_wolves_pup.json" data-npc="Galmore wolf&#x27;s pup" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

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


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `mg2_wolves_pup` |
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


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


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
