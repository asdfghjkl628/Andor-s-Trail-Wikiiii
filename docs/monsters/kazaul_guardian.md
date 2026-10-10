---
description: "Kazaul guardian is an NPC you can also fight in Andor's Trail, found in Blackwater mountain 42."
---

# ![](../assets/icons/monsters/monsters_rltiles1_42.png){ .sprite } Kazaul guardian

**Where to find Kazaul guardian:** [Blackwater mountain 42](../maps/blackwater_mountain42.md#pin-npc-kazaul_guardian)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles1_42.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Blackwater mountain 42 |
| **Class** | Demon |
| **HP** | 95 |
| **XP when defeated** | 175 |
| **Immune to crits** | Yes |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "You can fight Kazaul guardian"
    Any of your answers (“A fight, I have been waiting for this!”, “Please don't kill me!” or “For the Shadow!”) during [Lights in the dark](../quests/kazaul.md#stage-50) starts a fight with Kazaul guardian.

## Combat

| | |
|---|---|
| Class | Demon |
| HP | 95 |
| XP when defeated | 175 |
| Damage | 3 to 8 |
| AC | 70 |
| BC | 90 |
| DR | 3 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 23% (×2.0) |

**Immune to critical hits.**


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 52 |
| [Polished gem](../items/gem3.md) | 100% | 1 |
| [Regular potion of health](../items/health.md) | 100% | 2 |
| [Shadow of the slayer](../items/shadow_slayer.md) | 100% | 1 |

## Quests

- [Lights in the dark](../quests/kazaul.md): stage 50

## Dialogue simulator

Talk to Kazaul guardian as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/kazaul_guardian.json" data-npc="Kazaul guardian" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-kazaul_guardian"></span>**`kazaul_guardian`** Kazaul guardian: “Kazaul...”

    - “What?” → [kazaul_guardian_1](#d-kazaul_guardian_1)
    - “Kazaul, destroyer of bright dreams.” *(if reached stage 40 of [Lights in the dark](../quests/kazaul.md#stage-40))* → [kazaul_guardian_2](#d-kazaul_guardian_2)

    <span id="d-kazaul_guardian_1"></span>**`kazaul_guardian_1`** Kazaul guardian: “[The guardian looks completely unaware of your presence]”


    <span id="d-kazaul_guardian_2"></span>**`kazaul_guardian_2`** Kazaul guardian: “[The guardian looks down upon you with its burning eyes]”

    - “Kazaul, defiler of the Elytharan Temple.” → [kazaul_guardian_3](#d-kazaul_guardian_3)

    <span id="d-kazaul_guardian_3"></span>**`kazaul_guardian_3`** Kazaul guardian: “[You see the burning eyes of the guardian instantly turn into a dark red haze]” — **effects:** sets stage 50 of [Lights in the dark](../quests/kazaul.md#stage-50)

    - “A fight, I have been waiting for this!” → *fight starts*
    - “Please don't kill me!” → *fight starts*
    - “For the Shadow!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect)<br>Dialogue: 4 lines changed<br>· text: “Kazaul..” → “Kazaul...”<br>· text: “(You see the burning eyes of the guardian instantly turn into a dark …” → “[You see the burning eyes of the guardian instantly turn into a dark …” |

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
    | Entry ID | `kazaul_guardian` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `kazaul_guardian` |
    | Loot table | `kazaul_guardian` |
    | Conversation | `kazaul_guardian` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:42` |
    | Defined in | `res/raw/monsterlist_v069_monsters.json` |

    Raw data:

    ```json
    {
     "id": "kazaul_guardian",
     "name": "Kazaul guardian",
     "iconID": "monsters_rltiles1:42",
     "maxHP": 95,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "demon",
     "attackDamage": {
      "min": 3,
      "max": 8
     },
     "spawnGroup": "kazaul_guardian",
     "phraseID": "kazaul_guardian",
     "droplistID": "kazaul_guardian",
     "attackCost": 5,
     "attackChance": 70,
     "criticalSkill": 40,
     "criticalMultiplier": 2.0,
     "blockChance": 90,
     "damageResistance": 3
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=kazaul_guardian.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
