---
description: "Mountain Sheep is an NPC you can also fight in Andor's Trail, found in Blackwater Mountain."
---

# ![](../assets/icons/monsters/monsters_rltiles2_55.png){ .sprite } Mountain Sheep

**Where to find Mountain Sheep:** Blackwater Mountain: [Bwmfill 3](../maps/bwmfill3.md#pin-npc-bwm_sheep1), Blackwater Mountain: [Bwmfill tunlon](../maps/bwmfill_tunlon.md#pin-npc-bwm_sheep1)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles2_55.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Blackwater Mountain |
| **Class** | Animal |
| **HP** | 30 |
| **XP when defeated** | 33 |
| **Introduced** | [v0.8.10](../versions/0.8.10.md) |

</div>

!!! warning "You can fight Mountain Sheep"
    Any of your answers (“You look tasty - attack!” or “Attack!”) starts a fight with Mountain Sheep.

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 30 |
| XP when defeated | 33 |
| Damage | 1 to 5 |
| AC | 60 |
| BC | 20 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Raw lamb meat](../items/lamb_meat_raw.md) | 20% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Bwmfill 3](../maps/bwmfill3.md) | Blackwater Mountain | 10 | – |
| [Bwmfill tunlon](../maps/bwmfill_tunlon.md) | Blackwater Mountain | 2 | – |

## Quests that count defeats

- A conversation with [Mountain Sheep](../monsters/bwm_sheep1.md) ([Bwmfill 3](../maps/bwmfill3.md)) checks that this enemy has been defeated.
- A conversation with stepping on a trigger on [Bwmfill 3](../maps/bwmfill3.md), [Tunlon](../monsters/tunlon.md) ([Bwmfill 3](../maps/bwmfill3.md)) checks that this enemy has been defeated.
- A conversation with [Tunlon](../monsters/tunlon.md) ([Bwmfill 3](../maps/bwmfill3.md)) checks that this enemy has been defeated.

## Dialogue simulator

Talk to Mountain Sheep as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/bwm_sheep_dialogue.json" data-npc="Mountain Sheep" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-bwm_sheep_dialogue"></span>**`bwm_sheep_dialogue`** Mountain Sheep: “Baa!”

    - “[Pet]” *(if NOT killed 1× [Mountain Sheep](../monsters/bwm_sheep1.md))* → *conversation ends*
    - “You look tasty - attack!” *(if NOT killed 1× [Mountain Sheep](../monsters/bwm_sheep1.md); random chance (20%))* → *fight starts*
    - “Attack!” *(if killed 1× [Mountain Sheep](../monsters/bwm_sheep1.md))* → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.8.10](../versions/0.8.10.md) | Added<br>Dialogue: 1 line added |

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
    | Entry ID | `bwm_sheep1` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `bwm_sheep` |
    | Loot table | `bwm_sheep` |
    | Conversation | `bwm_sheep_dialogue` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles2:55` |
    | Defined in | `res/raw/monsterlist_bwmfill.json` |

    Raw data:

    ```json
    {
     "id": "bwm_sheep1",
     "name": "Mountain Sheep",
     "iconID": "monsters_rltiles2:55",
     "maxHP": 30,
     "maxAP": 10,
     "moveCost": 3,
     "monsterClass": "animal",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 1,
      "max": 5
     },
     "spawnGroup": "bwm_sheep",
     "phraseID": "bwm_sheep_dialogue",
     "droplistID": "bwm_sheep",
     "attackCost": 5,
     "attackChance": 60,
     "blockChance": 20,
     "damageResistance": 0
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bwm_sheep1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
