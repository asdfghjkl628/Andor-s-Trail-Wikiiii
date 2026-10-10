---
description: "Blackwater border patrol is an NPC you can also fight in Andor's Trail, found in Blackwater Mountain."
---

# ![](../assets/icons/monsters/monsters_rltiles1_76.png){ .sprite } Blackwater border patrol

**Where to find Blackwater border patrol:** Blackwater Mountain: [Blackwater mountain 52](../maps/blackwater_mountain52.md#pin-npc-blackwater_border_patrol)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_76.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Blackwater Mountain |
| **Class** | Humanoid |
| **HP** | 60 |
| **XP when defeated** | 102 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "You can fight Blackwater border patrol"
    Blackwater border patrol turns hostile if you fall out with their faction (this can happen in [Clouded intent](../quests/prim_hunt.md)).

## Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 60 |
| XP when defeated | 102 |
| Damage | 3 to 6 |
| AC | 60 |
| BC | 70 |
| DR | 3 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Dialogue simulator

Set your quest stages and items, then talk to Blackwater border patrol. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/blackwater_guard2.json" data-npc="Blackwater border patrol" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-blackwater_guard2"></span>**`blackwater_guard2`** Blackwater border patrol: “Halt! You should not step any further.”

    - Next → [blackwater_guard2_1](#d-blackwater_guard2_1)

    <span id="d-blackwater_guard2_1"></span>**`blackwater_guard2_1`** Blackwater border patrol: “There is something over there. Do you see it?”

    - Next → [blackwater_guard2_2](#d-blackwater_guard2_2)

    <span id="d-blackwater_guard2_2"></span>**`blackwater_guard2_2`** Blackwater border patrol: “A mist? A Shadow? I'm sure I saw something moving.”

    - Next → [blackwater_guard2_3](#d-blackwater_guard2_3)

    <span id="d-blackwater_guard2_3"></span>**`blackwater_guard2_3`** Blackwater border patrol: “Screw this guard duty stuff. I am staying back here.”

    - Next → [blackwater_guard2_4](#d-blackwater_guard2_4)

    <span id="d-blackwater_guard2_4"></span>**`blackwater_guard2_4`** Blackwater border patrol: “Good thing we blocked that entrance from that old cabin.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Attack chance: added (60)<br>Attack cost: added (5)<br>Attack damage: added (3–6)<br>Block chance: added (70)<br>Damage resistance: added (3)<br>Faction: added (fct_bwm)<br>Max AP: added (10)<br>Max HP: added (60)<br>Move cost: added (5) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

- `blackwater_border_patrol` belongs to the faction `fct_bwm`. The game treats any character as hostile once your standing with its faction is below zero.

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `blackwater_border_patrol` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `blackwater_guard2` |
    | Loot table | – |
    | Conversation | `blackwater_guard2` |
    | Faction | `fct_bwm` |
    | Movement | – |
    | Icon | `monsters_rltiles1:76` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "blackwater_border_patrol",
     "name": "Blackwater border patrol",
     "iconID": "monsters_rltiles1:76",
     "maxHP": 60,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "blackwater_guard2",
     "faction": "fct_bwm",
     "phraseID": "blackwater_guard2",
     "attackCost": 5,
     "attackChance": 60,
     "blockChance": 70,
     "damageResistance": 3
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=blackwater_border_patrol.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=blackwater_border_patrol.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=blackwater_border_patrol.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=blackwater_border_patrol.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
