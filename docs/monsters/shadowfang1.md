---
description: "Shadowfang is an NPC you can also fight in Andor's Trail, found in Blackwater mountain 76, Elm 2f 1, Elm 2f 3."
---

# ![](../assets/icons/monsters/monsters_omi2_7.png){ .sprite } Shadowfang

**Where to find Shadowfang:** [Blackwater mountain 76](../maps/blackwater_mountain76.md#pin-npc-shadowfang1), [Elm 2f 1](../maps/elm_2f_1.md#pin-npc-shadowfang1), [Elm 2f 3](../maps/elm_2f_3.md#pin-npc-shadowfang1), [Elm 4f 1](../maps/elm_4f_1.md#pin-npc-shadowfang1) (+3 more)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_omi2_7.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Blackwater mountain 76, Elm 2f 1, Elm 2f 3 |
| **Class** | Demon |
| **HP** | 98 |
| **XP when defeated** | 330 |
| **Immune to crits** | Yes |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

!!! warning "You can fight Shadowfang"
    Any of your answers (“What the...?”, “Hey, have you seen my brother Andor?” or “For the shadow!”) starts a fight with Shadowfang.

## Combat

| | |
|---|---|
| Class | Demon |
| HP | 98 |
| XP when defeated | 330 |
| Damage | 3 to 21 |
| AC | 130 |
| BC | 110 |
| DR | 9 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 9% (×2.0) |

**Immune to critical hits.**

**Its hits:** Heal HP: 0 to 3; On target: [Venom](../conditions/venom.md) (magnitude 2, 4 rounds, 10% chance); [Vulnerability](../conditions/vulnerability.md) (magnitude 3, 3 rounds, 10% chance); [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 3, 2 rounds, 5% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 1 to 72 |
| [Azure gem](../items/gem6.md) | 100% | 1 to 3 |
| [Ruby gem](../items/gem2.md) | 50% | 1 to 5 |
| [Contaminated poison gland](../items/gland2.md) | 25% | 1 to 2 |
| [Empty potion bottle](../items/vial_empty4.md) | 33.3333% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 76](../maps/blackwater_mountain76.md) | – | 2 | Appears later, during a quest |
| [Elm 2f 1](../maps/elm_2f_1.md) | – | 1 | – |
| [Elm 2f 3](../maps/elm_2f_3.md) | – | 1 | – |
| [Elm 4f 1](../maps/elm_4f_1.md) | – | 1 | – |
| [Elm 4f 5](../maps/elm_4f_5.md) | – | 1 | – |
| [Elm mine 3](../maps/elm_mine3.md) | – | 2 | Appears later, during a quest |
| [Elm mine 5](../maps/elm_mine5.md) | – | 3 | – |

## Dialogue simulator

Talk to Shadowfang as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/shadowfang_1.json" data-npc="Shadowfang" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-shadowfang_1"></span>**`shadowfang_1`** Shadowfang: “Sssssh...”

    - “What the...?” → *fight starts*
    - “Hey, have you seen my brother Andor?” → *fight starts*
    - “For the shadow!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 1 line added |

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
    | Entry ID | `shadowfang1` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `shadowfang` |
    | Loot table | `shadowfang1` |
    | Conversation | `shadowfang_1` |
    | Faction | – |
    | Movement | protectSpawn |
    | Icon | `monsters_omi2:7` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "shadowfang1",
     "name": "Shadowfang",
     "iconID": "monsters_omi2:7",
     "maxHP": 98,
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "demon",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 3,
      "max": 21
     },
     "spawnGroup": "shadowfang",
     "faction": "",
     "phraseID": "shadowfang_1",
     "droplistID": "shadowfang1",
     "attackCost": 5,
     "attackChance": 130,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 110,
     "damageResistance": 9,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 0,
       "max": 3
      },
      "conditionsTarget": [
       {
        "condition": "venom",
        "magnitude": 2,
        "duration": 4,
        "chance": "10"
       },
       {
        "condition": "vulnerability",
        "magnitude": 3,
        "duration": 3,
        "chance": "10"
       },
       {
        "condition": "bleeding_wound",
        "magnitude": 3,
        "duration": 2,
        "chance": "5"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shadowfang1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shadowfang1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shadowfang1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=shadowfang1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
