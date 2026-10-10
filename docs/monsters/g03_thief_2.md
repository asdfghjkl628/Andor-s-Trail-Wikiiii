---
description: "Thief warden is an NPC you can also fight in Andor's Trail, found in Crackshot hideout 3."
---

# ![](../assets/icons/monsters/monsters_ld1_10.png){ .sprite } Thief warden

**Where to find Thief warden:** [Crackshot hideout 3](../maps/crackshot_hideout3.md#pin-npc-g03_thief_2)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_10.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Crackshot hideout 3 |
| **Class** | Humanoid |
| **HP** | 68 |
| **XP when defeated** | 141 |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

!!! warning "You can fight Thief warden"
    Any of your answers (“I'm not playing that!!”, “Now your mates will play that with your corpse!” or “For the shadow!”) starts a fight with Thief warden.

    Thief warden turns hostile if you fall out with their faction.

## Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 68 |
| XP when defeated | 141 |
| Damage | 4 to 9 |
| AC | 100 |
| BC | 95 |
| DR | 2 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 12% (×2.0) |

**When you hit it:** On self: [Concentration](../conditions/g03_concentration.md) (magnitude 1, 2 rounds, 25% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Reinforced wooden buckler](../items/shield3.md) | 40% | 1 |
| [Iron sword](../items/ironsword1.md) | 60% | 1 |

## Dialogue simulator

Talk to Thief warden as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/rebthief2_g03_1.json" data-npc="Thief warden" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-rebthief2_g03_1"></span>**`rebthief2_g03_1`** [Thief warden](../monsters/g03_thief_2.md): “You couldn't be in a worse place to play hide and seek, kid. Die!” — **effects:** faction “rebthief2_g03_1” set to -10

    - “I'm not playing that!!” → *fight starts*
    - “Now your mates will play that with your corpse!” → *fight starts*
    - “For the shadow!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

- `g03_thief_2` belongs to the faction `rebthief2_g03_1`. The game treats any character as hostile once your standing with its faction is below zero.

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `g03_thief_2` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `guild03_rebthief_2` |
    | Loot table | `drop_g03_rebthief_2` |
    | Conversation | `rebthief2_g03_1` |
    | Faction | `rebthief2_g03_1` |
    | Movement | none |
    | Icon | `monsters_ld1:10` |
    | Defined in | `res/raw/monsterlist_omicronrg9.json` |

    Raw data:

    ```json
    {
     "id": "g03_thief_2",
     "name": "Thief warden",
     "iconID": "monsters_ld1:10",
     "maxHP": 68,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 4,
      "max": 9
     },
     "spawnGroup": "guild03_rebthief_2",
     "faction": "rebthief2_g03_1",
     "phraseID": "rebthief2_g03_1",
     "droplistID": "drop_g03_rebthief_2",
     "attackCost": 5,
     "attackChance": 100,
     "criticalSkill": 15,
     "criticalMultiplier": 2.0,
     "blockChance": 95,
     "damageResistance": 2,
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "g03_concentration",
        "magnitude": 1,
        "duration": 2,
        "chance": "25"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_thief_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_thief_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_thief_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=g03_thief_2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
