---
description: "Sleepy giant ogre is an NPC you can also fight in Andor's Trail, found in Galmore 18."
---

# ![](../assets/icons/monsters/monsters_cyclops_0.png){ .sprite } Sleepy giant ogre

**Where to find Sleepy giant ogre:** [Galmore 18](../maps/galmore_18.md#pin-npc-mg2_troll)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_cyclops_0.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Galmore 18 |
| **Class** | Giant |
| **HP** | 590 |
| **XP when defeated** | 1,005 |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

!!! warning "You can fight Sleepy giant ogre"
    Answering “Oops” starts a fight with Sleepy giant ogre.

    Sleepy giant ogre turns hostile if you fall out with their faction.

## Combat

| | |
|---|---|
| Class | Giant |
| HP | 590 |
| XP when defeated | 1,005 |
| Damage | 20 to 60 |
| AC | 90 |
| BC | 90 |
| DR | 15 |
| Attacks per turn | 1 (9 AP each, 10 AP) |
| Crit chance | none |

**Its hits:** On target: [Stunned](../conditions/stunned.md) (magnitude 1, 5 rounds, 5% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 30 to 130 |
| [Bone](../items/bone.md) | 100% | 1 |
| [Small rock](../items/rock.md) | 100% | 1 to 3 |

## Dialogue simulator

Talk to Sleepy giant ogre as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/mg2_troll.json" data-npc="Sleepy giant ogre" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (7 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-mg2_troll"></span>**`mg2_troll`** Sleepy giant ogre: “[Snoring]”

    - “Hey, ugly brute - wake up!” *(if random chance (50%))* → [mg2_troll](#d-mg2_troll)
    - “MOVE!!” *(if random chance (50%))* → [mg2_troll](#d-mg2_troll)
    - “Maybe I should just wait a bit?” → [mg2_troll](#d-mg2_troll)
    - “[singing]Troll sat alone on his seat of stone” *(if random chance (10%))* → [mg2_troll_10](#d-mg2_troll_10)
    - “I think I'm going to poke you in your big fat nose.” *(if reached stage 12 of [Galmore story flags (hidden flag)](../quests/galmore_nondisplayed.md#stage-12))* → [mg2_troll_20](#d-mg2_troll_20)
    - “Throw a rock at the troll.” *(if hand over 1× [Small rock](../items/rock.md))* → [mg2_troll_30](#d-mg2_troll_30)

    <span id="d-mg2_troll_10"></span>**`mg2_troll_10`** Sleepy giant ogre: “[Snoring]”

    - “[Singing] And munched and mumbled a bare old bone” → [mg2_troll_12](#d-mg2_troll_12)

    <span id="d-mg2_troll_20"></span>**`mg2_troll_20`** Sleepy giant ogre: “Ouch! OUCH! Oooh - just you wait!!” — **effects:** faction “mg2_troll” set to -100

    - “Oops” → *fight starts*

    <span id="d-mg2_troll_30"></span>**`mg2_troll_30`** Sleepy giant ogre: “Awww ... hmm, moooore ...”

    - Next → [mg2_troll](#d-mg2_troll)

    <span id="d-mg2_troll_12"></span>**`mg2_troll_12`** Sleepy giant ogre: “Hmm? [Snoring]”

    - “[Singing.] For many a year he had gnawed it near For meat was hard to come by.” → [mg2_troll_14](#d-mg2_troll_14)

    <span id="d-mg2_troll_14"></span>**`mg2_troll_14`** Sleepy giant ogre: “[Muttering] Fooood?”

    - Next → [mg2_troll_16](#d-mg2_troll_16)

    <span id="d-mg2_troll_16"></span>**`mg2_troll_16`** Sleepy giant ogre: “[Muttering] No. Can't be. Must be dreaming.”

    - “Hey!” → [mg2_troll](#d-mg2_troll)



## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

- `mg2_troll` belongs to the faction `mg2_troll`. The game treats any character as hostile once your standing with its faction is below zero.

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `mg2_troll` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `mg2_troll` |
    | Loot table | `mg2_troll` |
    | Conversation | `mg2_troll` |
    | Faction | `mg2_troll` |
    | Movement | – |
    | Icon | `monsters_cyclops:0` |
    | Defined in | `res/raw/monsterlist_mt_galmore2.json` |

    Raw data:

    ```json
    {
     "id": "mg2_troll",
     "name": "Sleepy giant ogre",
     "iconID": "monsters_cyclops:0",
     "maxHP": 590,
     "maxAP": 10,
     "moveCost": 8,
     "unique": 1,
     "monsterClass": "giant",
     "attackDamage": {
      "min": 20,
      "max": 60
     },
     "spawnGroup": "mg2_troll",
     "faction": "mg2_troll",
     "phraseID": "mg2_troll",
     "droplistID": "mg2_troll",
     "attackCost": 9,
     "attackChance": 90,
     "blockChance": 90,
     "damageResistance": 15,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "stunned",
        "magnitude": 1,
        "duration": 5,
        "chance": "5"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_troll.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_troll.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_troll.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mg2_troll.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
