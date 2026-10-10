---
description: "Maelveon is an NPC you can also fight in Andor's Trail, found in Gargoylecave 3."
---

# ![](../assets/icons/monsters/monsters_liches_2.png){ .sprite } Maelveon

**Where to find Maelveon:** [Gargoylecave 3](../maps/gargoylecave3.md#pin-npc-maelveon)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_liches_2.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Gargoylecave 3 |
| **Class** | Undead |
| **HP** | 55 |
| **XP when defeated** | 149 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "You can fight Maelveon"
    Any of your answers (“Shadow, what?”, “Die, evil creature!” or “Please don't hurt me!”) starts a fight with Maelveon.

## Combat

| | |
|---|---|
| Class | Undead |
| HP | 55 |
| XP when defeated | 149 |
| Damage | 0 to 12 |
| AC | 80 |
| BC | 90 |
| DR | 5 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 12% (×3.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 52 |
| [Polished gem](../items/gem3.md) | 100% | 1 |
| [Regular potion of health](../items/health.md) | 100% | 2 |
| [Stone Cuirass](../items/armor_stone.md) | 100% | 1 |

## Dialogue simulator

Talk to Maelveon as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/maelveon.json" data-npc="Maelveon" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (6 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

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
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect)<br>Dialogue: 4 lines changed<br>· text: “A.. llow the Sssshadow in you.” → “A ... llow the Sssshadow in you.”<br>· text: “[you feel a tingling sensation in your body as the frightening figure…” → “[You feel a tingling sensation in your body as the frightening figure…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `maelveon` |
    | Type (wiki) | NPC/Enemy |
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
