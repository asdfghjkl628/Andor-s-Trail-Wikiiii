---
description: "Keknazar is an NPC you can also fight in Andor's Trail, found in Crossroads Guardhouse."
---

# ![](../assets/icons/monsters/monsters_misc_9.png){ .sprite } Keknazar

**Where to find Keknazar:** Crossroads Guardhouse: [Houseatcrossroads 5](../maps/houseatcrossroads5.md#pin-npc-keknazar)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_misc_9.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Crossroads Guardhouse |
| **Class** | Reptile |
| **HP** | 90 |
| **XP when defeated** | 178 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "You can fight Keknazar"
    Any of your answers (“For the Shadow!”, “You will not survive this, you pathetic creature.” or “A fight! I have been looking forward to this!”) starts a fight with Keknazar.

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 90 |
| XP when defeated | 178 |
| Damage | 3 to 9 |
| AC | 50 |
| BC | 70 |
| DR | 8 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 15% (×3.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 0 to 45 |
| [Bone](../items/bone.md) | 100% | 1 to 3 |
| [Minor vial of health](../items/health_minor.md) | 100% | 1 to 2 |
| [Lesser shielding necklace](../items/necklace_shield_0.md) | 100% | 1 |

## Dialogue simulator

Talk to Keknazar as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/keknazar.json" data-npc="Keknazar" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-keknazar"></span>**`keknazar`** Keknazar: “*Hssss* [You hear squishing sounds as the creature starts moving towards you]”

    - “For the Shadow!” → *fight starts*
    - “You will not survive this, you pathetic creature.” → *fight starts*
    - “A fight! I have been looking forward to this!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect)<br>Dialogue: 1 line changed<br>· text: “*hssss* (You hear squishing sounds as the creature starts moving towa…” → “*Hssss* [You hear squishing sounds as the creature starts moving towa…” |

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
    | Entry ID | `keknazar` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `keknazar` |
    | Loot table | `keknazar` |
    | Conversation | `keknazar` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_misc:9` |
    | Defined in | `res/raw/monsterlist_v0610_monsters1.json` |

    Raw data:

    ```json
    {
     "id": "keknazar",
     "name": "Keknazar",
     "iconID": "monsters_misc:9",
     "maxHP": 90,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "reptile",
     "attackDamage": {
      "min": 3,
      "max": 9
     },
     "spawnGroup": "keknazar",
     "phraseID": "keknazar",
     "droplistID": "keknazar",
     "attackCost": 5,
     "attackChance": 50,
     "criticalSkill": 20,
     "criticalMultiplier": 3.0,
     "blockChance": 70,
     "damageResistance": 8
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=keknazar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=keknazar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=keknazar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=keknazar.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
