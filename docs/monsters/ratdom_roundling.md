---
description: "Roundling is an NPC you can also fight in Andor's Trail, found in Roundlings, Entry."
---

# ![](../assets/icons/monsters/monsters_rltiles1_134.png){ .sprite } Roundling

**Where to find Roundling:** [Roundlings, Ratdom maze 627](#v-ratdom_roundling), [Entry, Ratdom maze 448](#v-ratdom_roundling2), [Roundlings, Ratdom maze 627](#v-ratdom_roundling3)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_134.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Roundlings, Entry |
| **Class** | Humanoid |
| **HP** | 200 |
| **XP when defeated** | 216–241 |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

## Roundlings, Ratdom maze 627 { #v-ratdom_roundling }

**Where:** Roundlings: [Ratdom maze 627](../maps/ratdom_maze_627.md#pin-npc-ratdom_roundling)

!!! warning "You can fight Roundling"
    The conversation can lead straight into a fight with Roundling.

    Roundling turns hostile if you fall out with their faction.

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 200 |
| XP when defeated | 216 |
| Damage | 10 to 20 |
| AC | 120 |
| BC | 0 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Dialogue simulator

Set your quest stages and items, then talk to Roundling. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_roundling.json" data-npc="Roundling" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ratdom_roundling-ratdom_roundling"></span>**`ratdom_roundling`** Roundling: “If strangers come hither to gain our treasure, their hope is in vain. In the darkest deep ground, with our Yellow Round, their bones will forever remain.”

    - “What a nice poem. They are good, aren't they, Clevred?” → [ratdom_roundling_10](#d-ratdom_roundling-ratdom_roundling_10)

    <span id="d-ratdom_roundling-ratdom_roundling_10"></span>**`ratdom_roundling_10`** [Clevred](../monsters/ratdom_rat.md): “Really, they're good at poetry. But we'll take the artifact with us anyway.”

    - “Of course. So now to work ...” → [ratdom_roundling_90](#d-ratdom_roundling-ratdom_roundling_90)

    <span id="d-ratdom_roundling-ratdom_roundling_90"></span>**`ratdom_roundling_90`** *(silent check: the first matching branch below is taken)* — **effects:** faction “fct_ratdom_roundling” set to -10

    - branch 1 → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Entry, Ratdom maze 448 { #v-ratdom_roundling2 }

**Where:** Entry: [Ratdom maze 448](../maps/ratdom_maze_448.md#pin-npc-ratdom_roundling2)

!!! warning "You can fight Roundling"
    The conversation can lead straight into a fight with Roundling.

    Roundling turns hostile if you fall out with their faction.

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 200 |
| XP when defeated | 241 |
| Damage | 10 to 30 |
| AC | 120 |
| BC | 0 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Quests

- [Yellow is it](../quests/ratdom_quest.md): stage 960
- [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md): stage 13

### Dialogue simulator

Set your quest stages and items, then talk to Roundling. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_roundling2.json" data-npc="Roundling" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ratdom_roundling2-ratdom_roundling2"></span>**`ratdom_roundling2`** Roundling: “A thief who thinks to get through with our treasure, is due to give his life upon a strife, and all his stolen goods too.”

    - “Eh, let us think a minute.” → *conversation ends*
    - “Well, OK. We have no chance against so many roundlings.” → [ratdom_roundling2_10](#d-ratdom_roundling2-ratdom_roundling2_10)
    - “Never - attack!” → [ratdom_roundling2_90](#d-ratdom_roundling2-ratdom_roundling2_90)

    <span id="d-ratdom_roundling2-ratdom_roundling2_10"></span>**`ratdom_roundling2_10`** [Clevred](../monsters/ratdom_rat.md): “Coward! You didn't even try.”

    - “Never call me coward! Attack!” → [ratdom_roundling2_90](#d-ratdom_roundling2-ratdom_roundling2_90)
    - “They are too many for us, we would be killed. Let's give up the artifact.” → [ratdom_roundling2_12](#d-ratdom_roundling2-ratdom_roundling2_12)

    <span id="d-ratdom_roundling2-ratdom_roundling2_90"></span>**`ratdom_roundling2_90`** *(silent check: the first matching branch below is taken)* — **effects:** faction “fct_ratdom_roundling2” set to -10

    - branch 1 → *fight starts*

    <span id="d-ratdom_roundling2-ratdom_roundling2_12"></span>**`ratdom_roundling2_12`** Roundling: “Never! I'd rather die!”

    - “If you think so, then let's attack!” → [ratdom_roundling2_90](#d-ratdom_roundling2-ratdom_roundling2_90)
    - “Die you will, if you can't let go of it. I will leave it behind.” → [ratdom_roundling2_20](#d-ratdom_roundling2-ratdom_roundling2_20)

    <span id="d-ratdom_roundling2-ratdom_roundling2_20"></span>**`ratdom_roundling2_20`** Roundling: “I see. I thought you were braver. Go then, I don't want to see you again!” — **effects:** sets stage 960 of [Yellow is it](../quests/ratdom_quest.md#stage-960), clears stage 10 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-10), clears stage 11 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-11), sets stage 13 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-13), removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_448, removes monsters from home, removes monsters from ratdom_bwm1




### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Roundlings, Ratdom maze 627 (2) { #v-ratdom_roundling3 }

**Where:** Roundlings: [Ratdom maze 627](../maps/ratdom_maze_627.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 200 |
| XP when defeated | 241 |
| Damage | 10 to 30 |
| AC | 120 |
| BC | 0 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Ratdom maze 627](../maps/ratdom_maze_627.md) | Roundlings | 2 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**3 entries.** The game data defines 3 separate characters named Roundling. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, combat statistics, faction, movement.

| Entry | Type | Section |
|---|---|---|
| `ratdom_roundling` | NPC/Enemy | [Roundlings, Ratdom maze 627](#v-ratdom_roundling) |
| `ratdom_roundling2` | NPC/Enemy | [Entry, Ratdom maze 448](#v-ratdom_roundling2) |
| `ratdom_roundling3` | Enemy | [Roundlings, Ratdom maze 627](#v-ratdom_roundling3) |

- `ratdom_roundling` belongs to the faction `fct_ratdom_roundling`. The game treats any character as hostile once your standing with its faction is below zero.
- `ratdom_roundling2` belongs to the faction `fct_ratdom_roundling2`. The game treats any character as hostile once your standing with its faction is below zero.

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: ratdom_roundling"

    | | |
    |---|---|
    | Entry ID | `ratdom_roundling` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `ratdom_roundling` |
    | Loot table | – |
    | Conversation | `ratdom_roundling` |
    | Faction | `fct_ratdom_roundling` |
    | Movement | helpOthers |
    | Icon | `monsters_rltiles1:134` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_roundling",
     "name": "Roundling",
     "iconID": "monsters_rltiles1:134",
     "maxHP": 200,
     "monsterClass": "humanoid",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 10,
      "max": 20
     },
     "spawnGroup": "ratdom_roundling",
     "faction": "fct_ratdom_roundling",
     "phraseID": "ratdom_roundling",
     "attackCost": 5,
     "attackChance": 120
    }
    ```

??? info "Technical information: ratdom_roundling2"

    | | |
    |---|---|
    | Entry ID | `ratdom_roundling2` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `ratdom_roundling2` |
    | Loot table | – |
    | Conversation | `ratdom_roundling2` |
    | Faction | `fct_ratdom_roundling2` |
    | Movement | helpOthers |
    | Icon | `monsters_rltiles1:134` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_roundling2",
     "name": "Roundling",
     "iconID": "monsters_rltiles1:134",
     "maxHP": 200,
     "monsterClass": "humanoid",
     "movementAggressionType": "helpOthers",
     "attackDamage": {
      "min": 10,
      "max": 30
     },
     "spawnGroup": "ratdom_roundling2",
     "faction": "fct_ratdom_roundling2",
     "phraseID": "ratdom_roundling2",
     "attackCost": 5,
     "attackChance": 120
    }
    ```

??? info "Technical information: ratdom_roundling3"

    | | |
    |---|---|
    | Entry ID | `ratdom_roundling3` |
    | Type (wiki) | Enemy |
    | Spawn group | `ratdom_roundling3` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_rltiles1:134` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_roundling3",
     "name": "Roundling",
     "iconID": "monsters_rltiles1:134",
     "maxHP": 200,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 10,
      "max": 30
     },
     "spawnGroup": "ratdom_roundling3",
     "attackCost": 5,
     "attackChance": 120
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_roundling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_roundling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_roundling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_roundling.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
