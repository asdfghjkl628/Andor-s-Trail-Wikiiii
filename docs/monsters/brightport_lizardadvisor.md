---
description: "Tail-swing-tyliad is an NPC you can also fight in Andor's Trail, found in Greenscale tribe."
---

# ![](../assets/icons/monsters/monsters_johny_1.png){ .sprite } Tail-swing-tyliad

**Where to find Tail-swing-tyliad:** Greenscale tribe: [Brightport lizard 1](../maps/brightport_lizard1.md#pin-npc-brightport_lizardadvisor)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_johny_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Greenscale tribe |
| **Class** | Reptile |
| **HP** | 160 |
| **XP when defeated** | 437 |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

!!! warning "You can fight Tail-swing-tyliad"
    Tail-swing-tyliad turns hostile if you fall out with their faction (this can happen in [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md)).

## Combat

| | |
|---|---|
| Class | Reptile |
| HP | 160 |
| XP when defeated | 437 |
| Damage | 8 to 15 |
| AC | 180 |
| BC | 190 |
| DR | 4 |
| Attacks per turn | 2 (6 AP each, 12 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Lizardman bone](../items/brightport_bone.md) | 35% | 1 to 2 |
| [Gold coins](../items/gold.md) | 100% | 30 to 45 |
| [Lizard skin](../items/lizard_skin.md) | 100% | 1 |

## Quests that count defeats

- [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-120) with stepping on a trigger on [Brightport cave 17](../maps/brightport_cave17.md) checks that this enemy has been defeated.

## Dialogue simulator

Set your quest stages and items, then talk to Tail-swing-tyliad. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_tyliad.json" data-npc="Tail-swing-tyliad" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_tyliad"></span>**`brightport_tyliad`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 95 of [The balance of scales](../quests/brightport_lizard.md#stage-95))* → [brightport_tyliad1](#d-brightport_tyliad1)
    - Next *(if NOT reached stage 95 of [The balance of scales](../quests/brightport_lizard.md#stage-95))* → [brightport_tyliad2](#d-brightport_tyliad2)

    <span id="d-brightport_tyliad1"></span>**`brightport_tyliad1`** Tail-swing-tyliad: “You are worthy of our trust now, but don't overstep, outsider.”

    - “Can you tell more about the lizard people?” → [brightport_tyliad3](#d-brightport_tyliad3)

    <span id="d-brightport_tyliad2"></span>**`brightport_tyliad2`** Tail-swing-tyliad: “Carry out your purpose, outsider. Don't dissapoint.”


    <span id="d-brightport_tyliad3"></span>**`brightport_tyliad3`** Tail-swing-tyliad: “Our ancestors, been inhabiting the bright lake for many generations, until you, men without scales, drove us away to the mountains.”

    - Next → [brightport_tyliad4](#d-brightport_tyliad4)

    <span id="d-brightport_tyliad4"></span>**`brightport_tyliad4`** Tail-swing-tyliad: “Us men with scales acknowledge strength, and accept defeat. But mountain have little food, so we fought each other and separate. We came here, others swam north. And we created many tribes.”

    - “Tribes?” → [brightport_tyliad5](#d-brightport_tyliad5)

    <span id="d-brightport_tyliad5"></span>**`brightport_tyliad5`** Tail-swing-tyliad: “Many, but what remains are three great tribes. Us green-fang, honorable brave warriors, the lineage of heroes.”

    - Next → [brightport_tyliad6](#d-brightport_tyliad6)

    <span id="d-brightport_tyliad6"></span>**`brightport_tyliad6`** Tail-swing-tyliad: “Yellow-tail, greedy and cunning. Love to eat gold and steal.”

    - Next → [brightport_tyliad7](#d-brightport_tyliad7)

    <span id="d-brightport_tyliad7"></span>**`brightport_tyliad7`** Tail-swing-tyliad: “And the barbaric red-scale, violent and slowminded, never listen to reason.”

    - “You're not friends with them? Phew!” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 8 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

- `brightport_lizardadvisor` belongs to the faction `lizardman`. The game treats any character as hostile once your standing with its faction is below zero.

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `brightport_lizardadvisor` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `brightport_lizardadvisor` |
    | Loot table | `brightport_greenlizard` |
    | Conversation | `brightport_tyliad` |
    | Faction | `lizardman` |
    | Movement | helpOthers |
    | Icon | `monsters_johny:1` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_lizardadvisor",
     "name": "Tail-swing-tyliad",
     "iconID": "monsters_johny:1",
     "maxHP": 160,
     "maxAP": 12,
     "moveCost": 4,
     "unique": 1,
     "monsterClass": "reptile",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 8,
      "max": 15
     },
     "faction": "lizardman",
     "phraseID": "brightport_tyliad",
     "droplistID": "brightport_greenlizard",
     "attackCost": 6,
     "attackChance": 180,
     "blockChance": 190,
     "damageResistance": 4
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizardadvisor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizardadvisor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizardadvisor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_lizardadvisor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
