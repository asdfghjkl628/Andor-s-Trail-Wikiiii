---
description: "Galmore wolf is an NPC you can also fight in Andor's Trail, found in Mt. Galmore."
---

# ![](../assets/icons/monsters/monsters_dogs_4.png){ .sprite } Galmore wolf

**Where to find Galmore wolf:** Mt. Galmore: [Galmore 54](../maps/galmore_54.md#pin-npc-mg2_wolves), Mt. Galmore: [Galmore 55](../maps/galmore_55.md#pin-npc-mg2_wolves), Mt. Galmore: [Galmore 64](../maps/galmore_64.md#pin-npc-mg2_wolves)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_dogs_4.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Mt. Galmore |
| **Class** | Animal |
| **HP** | 251 |
| **XP when defeated** | 679 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

!!! warning "You can fight Galmore wolf"
    Answering “Attack!” starts a fight with Galmore wolf.

    Galmore wolf turns hostile if you fall out with their faction.

## Combat

| | |
|---|---|
| Class | Animal |
| HP | 251 |
| XP when defeated | 679 |
| Damage | 15 to 20 |
| AC | 177 |
| BC | 153 |
| DR | 0 |
| Attacks per turn | 3 (3 AP each, 10 AP) |
| Crit chance | 9% (×2.0) |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 20% | 1 to 3 |
| [Gold coins](../items/gold.md) | 10% | 1 to 21 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Galmore 54](../maps/galmore_54.md) | Mt. Galmore | 12 | – |
| [Galmore 55](../maps/galmore_55.md) | Mt. Galmore | 1 | – |
| [Galmore 64](../maps/galmore_64.md) | Mt. Galmore | 1 | – |

## Quests

- [Unusual experiences and achievements](../quests/achievements.md): stage 200
- [General story flags (hidden flag)](../quests/nondisplay.md): stage 70

## Dialogue simulator

Talk to Galmore wolf as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/mg2_wolves.json" data-npc="Galmore wolf" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (9 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-mg2_wolves"></span>**`mg2_wolves`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if wearing [Wolfpack's animal hide](../items/packhide.md))* → [mg2_wolves_1](#d-mg2_wolves_1)
    - branch 2 → [mg2_wolves_2](#d-mg2_wolves_2)

    <span id="d-mg2_wolves_1"></span>**`mg2_wolves_1`** Galmore wolf: “Grrr. You look like a grrreat wolf, but smell two-leggish.”

    - “Grrr, grrr” → [mg2_wolves_10](#d-mg2_wolves_10)
    - “I am the big bad wolf from the stories. Fear me!” → [mg2_wolves_10](#d-mg2_wolves_10)
    - “Move out of my way!” → *NPC leaves*

    <span id="d-mg2_wolves_2"></span>**`mg2_wolves_2`** Galmore wolf: “Grrroarrrr! It's a two-leg!” — **effects:** faction “mg2_wolves_faction” set to -666

    - “Attack!” → *fight starts*

    <span id="d-mg2_wolves_10"></span>**`mg2_wolves_10`** Galmore wolf: “You may go thrrrough herrre. No tarrrrying.” — **effects:** sets stage 200 of [Unusual experiences and achievements](../quests/achievements.md#stage-200)

    - “Agrrreed.” → *conversation ends*
    - “I am hungrrry.” *(if NOT reached stage 70 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-70))* → [mg2_wolves_20](#d-mg2_wolves_20)
    - “I am hungrrry.” *(if reached stage 70 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-70))* → [mg2_wolves_30](#d-mg2_wolves_30)

    <span id="d-mg2_wolves_20"></span>**`mg2_wolves_20`** Galmore wolf: “We can prrrovide you with good rrraw meat.”

    - “Do.” → [mg2_wolves_22](#d-mg2_wolves_22)
    - “No, thank you.” → *conversation ends*

    <span id="d-mg2_wolves_30"></span>**`mg2_wolves_30`** Galmore wolf: “We've alrrready given you. Now go.”

    - “Grrr.” → *conversation ends*
    - “That was looong ago. Long forrrgotten.” *(if 100 rounds passed since timer “mg2_wolves”)* → [mg2_wolves_40](#d-mg2_wolves_40)

    <span id="d-mg2_wolves_22"></span>**`mg2_wolves_22`** Galmore wolf: “Much grrreat meat. Twenty fourrr bites.” — **effects:** sets stage 70 of [General story flags (hidden flag)](../quests/nondisplay.md#stage-70), gives 24× [Meat](../items/meat.md), starts timer “mg2_wolves”

    - “Tha... I mean grrr.” → *conversation ends*

    <span id="d-mg2_wolves_40"></span>**`mg2_wolves_40`** Galmore wolf: “Parrrasite.”

    - “What?” → [mg2_wolves_42](#d-mg2_wolves_42)

    <span id="d-mg2_wolves_42"></span>**`mg2_wolves_42`** Galmore wolf: “Nothing. OK, look herrre.”

    - Next → [mg2_wolves_22](#d-mg2_wolves_22)



## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

- `mg2_wolves` belongs to the faction `mg2_wolves_faction`. The game treats any character as hostile once your standing with its faction is below zero.

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `mg2_wolves` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `mg2_wolves` |
    | Loot table | `canine_dl` |
    | Conversation | `mg2_wolves` |
    | Faction | `mg2_wolves_faction` |
    | Movement | – |
    | Icon | `monsters_dogs:4` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "mg2_wolves",
     "name": "Galmore wolf",
     "iconID": "monsters_dogs:4",
     "maxHP": 251,
     "moveCost": 3,
     "unique": 1,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 15,
      "max": 20
     },
     "faction": "mg2_wolves_faction",
     "phraseID": "mg2_wolves",
     "droplistID": "canine_dl",
     "attackCost": 3,
     "attackChance": 177,
     "criticalSkill": 10,
     "criticalMultiplier": 2.0,
     "blockChance": 153
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_wolves.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
