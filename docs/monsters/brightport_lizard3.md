---
description: "Green-blade-remio is an NPC you can also fight in Andor's Trail, found in Greenscale tribe."
---

# ![](../assets/icons/monsters/monsters_johny_0.png){ .sprite } Green-blade-remio

**Where to find Green-blade-remio:** Greenscale tribe: [Brightport lizard 1](../maps/brightport_lizard1.md#pin-npc-brightport_lizard3)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_johny_0.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Greenscale tribe |
| **Class** | Reptile |
| **HP** | 250 |
| **XP when defeated** | 702 |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

!!! warning "You can fight Green-blade-remio"
    Green-blade-remio turns hostile if you fall out with their faction (this can happen in [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md)).

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 250 |
| XP when defeated | 702 |
| Damage | 13 to 22 |
| AC | 220 |
| BC | 180 |
| DR | 4 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | 9% (×1.5) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Lizardman bone](../items/brightport_bone.md) | 35% | 1 to 2 |
| [Gold coins](../items/gold.md) | 100% | 30 to 45 |
| [Lizard skin](../items/lizard_skin.md) | 100% | 1 |

## Dialogue simulator

Talk to Green-blade-remio as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_genericlizard_selector.json" data-npc="Green-blade-remio" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_genericlizard_selector"></span>**`brightport_genericlizard_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 95 of [The balance of scales](../quests/brightport_lizard.md#stage-95))* → [brightport_genericlizard_friend](#d-brightport_genericlizard_friend)
    - Next *(if NOT reached stage 40 of [The balance of scales](../quests/brightport_lizard.md#stage-40))* → [brightport_genericlizard_enemy](#d-brightport_genericlizard_enemy)
    - Next → [brightport_genericlizard_neutral](#d-brightport_genericlizard_neutral)

    <span id="d-brightport_genericlizard_friend"></span>**`brightport_genericlizard_friend`** Green-blade-remio: “You are welcome here, but don't overstep boundaries.”


    <span id="d-brightport_genericlizard_enemy"></span>**`brightport_genericlizard_enemy`** Green-blade-remio: “Outsider, speak to leader Elyzard.”


    <span id="d-brightport_genericlizard_neutral"></span>**`brightport_genericlizard_neutral`** Green-blade-remio: “I am watching you, outsider.”




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

- `brightport_lizard3` belongs to the faction `lizardman`. The game treats any character as hostile once your standing with its faction is below zero.

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightport_lizard3` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `brightport_lizard3` |
    | Loot table | `brightport_greenlizard` |
    | Conversation | `brightport_genericlizard_selector` |
    | Faction | `lizardman` |
    | Movement | helpOthers |
    | Icon | `monsters_johny:0` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_lizard3",
     "name": "Green-blade-remio",
     "iconID": "monsters_johny:0",
     "maxHP": 250,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "reptile",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 13,
      "max": 22
     },
     "faction": "lizardman",
     "phraseID": "brightport_genericlizard_selector",
     "droplistID": "brightport_greenlizard",
     "attackCost": 5,
     "attackChance": 220,
     "criticalSkill": 10,
     "criticalMultiplier": 1.5,
     "blockChance": 180,
     "damageResistance": 4
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizard3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizard3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizard3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizard3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
