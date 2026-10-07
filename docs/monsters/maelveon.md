---
description: "Maelveon is an NPC who can also be fought in Andor's Trail, found in gargoylecave3."
---

# ![](../assets/icons/monsters/monsters_liches_2.png){ .sprite } Maelveon

**Where to find Maelveon:** [gargoylecave3](../maps/gargoylecave3.md#pin-npc-maelveon)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_liches_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | gargoylecave3 |
| **Class** | Undead |
| **HP** | 55 |
| **XP when defeated** | 149 |
| **Entry ID** | `maelveon` |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Undead |
| HP | 55 |
| XP when defeated | 149 |
| Damage | 0 to 12 |
| Attack chance | 80 |
| Block chance | 90 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 10 AP |
| Critical skill | 15 |
| Critical multiplier | 3.0 |
| Critical hit chance | 12% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 52 |
| [Polished gem](../items/gem3.md) | 100% | 1 |
| [Regular potion of health](../items/health.md) | 100% | 2 |
| [Stone Cuirass](../items/armor_stone.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [gargoylecave3](../maps/gargoylecave3.md) | – | 1 | – |

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Maelveon. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/maelveon.json" data-npc="Maelveon" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-maelveon"></span>**`maelveon`** Maelveon: “[You feel a tingling sensation in your body as the frightening figure begins to speak]”

    - Next → [maelveon_1](#d-maelveon_1)

    <span id="d-maelveon_1"></span>**`maelveon_1`** Maelveon: “Sssshadow take you.”

    - Next → [maelveon_2](#d-maelveon_2)

    <span id="d-maelveon_2"></span>**`maelveon_2`** Maelveon: “G ... argoyle Shadow.”

    - Next → [maelveon_3](#d-maelveon_3)

    <span id="d-maelveon_3"></span>**`maelveon_3`** Maelveon: “A ... llow the Sssshadow in you.”

    - “The Shadow, what do you mean?” → [maelveon_4](#d-maelveon_4)
    - “Die, evil creature!” → [maelveon_4](#d-maelveon_4)
    - “I will not be affected by your nonsense!” → [maelveon_4](#d-maelveon_4)

    <span id="d-maelveon_4"></span>**`maelveon_4`** Maelveon: “[The figure lifts his hand and points at you]”

    - Next → [maelveon_5](#d-maelveon_5)

    <span id="d-maelveon_5"></span>**`maelveon_5`** Maelveon: “Sssshadow be with you.”

    - “Shadow, what?” → *fight starts*
    - “Die, evil creature!” → *fight starts*
    - “Please don't hurt me!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect)<br>Dialogue: 4 lines changed<br>· text: “G.. argoyle Shadow.” → “G ... argoyle Shadow.”<br>· text: “A.. llow the Sssshadow in you.” → “A ... llow the Sssshadow in you.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `maelveon` |
    | Spawn group | `maelveon` |
    | Loot table | `maelveon` |
    | Conversation | `maelveon` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_liches:2` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "maelveon",
     "name": "Maelveon",
     "iconID": "monsters_liches:2",
     "maxHP": 55,
     "unique": 1,
     "monsterClass": "undead",
     "attackDamage": {
      "min": 0,
      "max": 12
     },
     "spawnGroup": "maelveon",
     "phraseID": "maelveon",
     "droplistID": "maelveon",
     "attackCost": 3,
     "attackChance": 80,
     "criticalSkill": 15,
     "criticalMultiplier": 3.0,
     "blockChance": 90,
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

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maelveon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maelveon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maelveon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=maelveon.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
