---
description: "Mushroom guardian is an NPC you can also fight in Andor's Trail, found in Flagstone Prison."
---

# ![](../assets/icons/monsters/monsters_gisons_3.png){ .sprite } Mushroom guardian

**Where to find Mushroom guardian:** Flagstone Prison: [Lake shore road 8](../maps/lake_shore_road_8.md#pin-npc-guardian_mushroom)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_gisons_3.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Flagstone Prison |
| **Class** | Animal |
| **HP** | 160 |
| **XP when defeated** | 286 |
| **Introduced** | [v0.8.8](../versions/0.8.8.md) |

</div>

!!! warning "You can fight Mushroom guardian"
    Any of your answers (“Yes!” or “No, I swear. Please don't hurt me.”) starts a fight with Mushroom guardian.

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 160 |
| XP when defeated | 286 |
| Damage | 3 to 8 |
| AC | 120 |
| BC | 60 |
| DR | 0 |
| Attacks per turn | 3 (4 AP each, 12 AP) |
| Crit chance | 13% (×2.0) |

**Its hits:** On target: [Spore poisoning](../conditions/spore_poison.md) (magnitude 2, 5 rounds, 20% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Mushroom](../items/mushroom.md) | 10% | 1 to 2 |
| [Small rock](../items/rock.md) | 15% | 1 to 3 |
| [Garnet stone](../items/garnet_stone.md) | 1% | 1 |

## Dialogue simulator

Talk to Mushroom guardian as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/guardian_mushroom_1.json" data-npc="Mushroom guardian" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guardian_mushroom_1"></span>**`guardian_mushroom_1`** Mushroom guardian: “You're here to take our magical mushroom!”

    - “Yes!” → *fight starts*
    - “No, I swear. Please don't hurt me.” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added<br>Dialogue: 1 line added |

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
    | Entry ID | `guardian_mushroom` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `guardian_mushroom` |
    | Loot table | `guardian_mushroom_dl` |
    | Conversation | `guardian_mushroom_1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:3` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "guardian_mushroom",
     "name": "Mushroom guardian",
     "iconID": "monsters_gisons:3",
     "maxHP": 160,
     "maxAP": 12,
     "moveCost": 6,
     "unique": 1,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 3,
      "max": 8
     },
     "phraseID": "guardian_mushroom_1",
     "droplistID": "guardian_mushroom_dl",
     "attackCost": 4,
     "attackChance": 120,
     "criticalSkill": 18,
     "criticalMultiplier": 2.0,
     "blockChance": 60,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "spore_poison",
        "magnitude": 2,
        "duration": 5,
        "chance": "20"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guardian_mushroom.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guardian_mushroom.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guardian_mushroom.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guardian_mushroom.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
