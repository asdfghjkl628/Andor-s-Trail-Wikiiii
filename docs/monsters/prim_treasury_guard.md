---
description: "Prim treasury guard is an NPC who can also be fought in Andor's Trail, found in Prim."
---

# ![](../assets/icons/monsters/monsters_rltiles1_69.png){ .sprite } Prim treasury guard

**Where to find Prim treasury guard:** Prim: [blackwater_mountain25](../maps/blackwater_mountain25.md#pin-npc-prim_treasury_guard)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_69.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Prim |
| **Class** | Humanoid |
| **HP** | 60 |
| **XP when defeated** | 102 |
| **Entry ID** | `prim_treasury_guard` |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 60 |
| XP when defeated | 102 |
| Damage | 3 to 6 |
| Attack chance | 60 |
| Block chance | 70 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain25](../maps/blackwater_mountain25.md) | Prim | 1 | – |

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Prim treasury guard. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_treasury_guard.json" data-npc="Prim treasury guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-prim_treasury_guard"></span>**`prim_treasury_guard`** Prim treasury guard: “See these bars? They will hold against almost anything.”

    - “Guthbered said I could choose anything from the vault. So let me in.” *(if reached stage 240 of [Clouded intent](../quests/prim_hunt.md#stage-240))* → [prim_treasury_guard_10](#d-prim_treasury_guard_10)
    - “Guthbered said I could choose anything from the vault. So let me in.” *(if reached stage 250 of [Clouded intent](../quests/prim_hunt.md#stage-250))* → [prim_treasury_guard_10](#d-prim_treasury_guard_10)

    <span id="d-prim_treasury_guard_10"></span>**`prim_treasury_guard_10`** Prim treasury guard: “He said so? [His piercing gaze unsettles you.]”

    - “Y... yes.” → [prim_treasury_guard_20](#d-prim_treasury_guard_20)

    <span id="d-prim_treasury_guard_20"></span>**`prim_treasury_guard_20`** Prim treasury guard: “Nice try, kid. Now go play again.”

    - “OK, bye.” → *conversation ends*
    - “Play? I'm going to play - with you!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | attackChance added (60); attackCost added (5); attackDamage added ({"max": 6, "min": 3}); blockChance added (70); damageResistance added (3); faction added (fct_prim) (+3 more)<br>Dialogue: 1 line changed<br>· text: “See these bars? They will hold for almost anything.” → “See these bars? They will hold against almost anything.” |
| [v0.8.15](../versions/0.8.15.md) | Dialogue: 2 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `prim_treasury_guard` |
    | Spawn group | `prim_treasury_guard` |
    | Loot table | – |
    | Conversation | `prim_treasury_guard` |
    | Faction | `fct_prim` |
    | Movement | – |
    | Icon | `monsters_rltiles1:69` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "prim_treasury_guard",
     "name": "Prim treasury guard",
     "iconID": "monsters_rltiles1:69",
     "maxHP": 60,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "prim_treasury_guard",
     "faction": "fct_prim",
     "phraseID": "prim_treasury_guard",
     "attackCost": 5,
     "attackChance": 60,
     "blockChance": 70,
     "damageResistance": 3
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_treasury_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_treasury_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_treasury_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_treasury_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
