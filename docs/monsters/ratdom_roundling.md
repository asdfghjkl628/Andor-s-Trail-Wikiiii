---
description: "Roundling is an NPC who can also be fought in Andor's Trail, found in Roundlings, Entry."
---

# ![](../assets/icons/monsters/monsters_rltiles1_134.png){ .sprite } Roundling

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_134.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Roundlings, Entry |
| **Class** | Humanoid |
| **HP** | 200 |
| **XP when defeated** | 216–241 |
| **Entries in game data** | 3 |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

!!! info "3 entries in the game data"
    The game's data files define 3 separate characters named Roundling. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, combat statistics, faction, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`ratdom_roundling`](#v-ratdom_roundling) | NPC/Enemy | Roundlings: [ratdom_maze_627](../maps/ratdom_maze_627.md#pin-npc-ratdom_roundling) | – | 200 |
| [`ratdom_roundling2`](#v-ratdom_roundling2) | NPC/Enemy | Entry: [ratdom_maze_448](../maps/ratdom_maze_448.md#pin-npc-ratdom_roundling2) | – | 200 |
| [`ratdom_roundling3`](#v-ratdom_roundling3) | Enemy | Roundlings: [ratdom_maze_627](../maps/ratdom_maze_627.md) | – | 200 |

## Roundlings, Ratdom maze 627 (ratdom_roundling) { #v-ratdom_roundling }

**Entry ID:** `ratdom_roundling` · **Type:** NPC/Enemy

**Location:** Roundlings: [ratdom_maze_627](../maps/ratdom_maze_627.md#pin-npc-ratdom_roundling)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 200 |
| XP when defeated | 216 |
| Damage | 10 to 20 |
| Attack chance | 120 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_627](../maps/ratdom_maze_627.md) | Roundlings | 2 | – |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Roundling. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_roundling.json" data-npc="Roundling" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

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


??? info "Technical information (ratdom_roundling)"

    | | |
    |---|---|
    | Entry ID | `ratdom_roundling` |
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


## Entry, Ratdom maze 448 (ratdom_roundling2) { #v-ratdom_roundling2 }

**Entry ID:** `ratdom_roundling2` · **Type:** NPC/Enemy

**Location:** Entry: [ratdom_maze_448](../maps/ratdom_maze_448.md#pin-npc-ratdom_roundling2)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 200 |
| XP when defeated | 241 |
| Damage | 10 to 30 |
| Attack chance | 120 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_448](../maps/ratdom_maze_448.md) | Entry | 5 | Appears later, during a quest |

### Quests

- [Yellow is it](../quests/ratdom_quest.md): stage 960
- [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md): stage 13

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Roundling. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_roundling2.json" data-npc="Roundling" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

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

    <span id="d-ratdom_roundling2-ratdom_roundling2_20"></span>**`ratdom_roundling2_20`** Roundling: “I see. I thought you were braver. Go then, I don't want to see you again!” — **effects:** sets stage 960 of [Yellow is it](../quests/ratdom_quest.md#stage-960), clears stage 10 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-10), clears stage 11 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-11), sets stage 13 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-13), removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_627, removes monsters from ratdom_maze_448, removes monsters from home, removes monsters from ratdom_bwm1




### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_roundling2)"

    | | |
    |---|---|
    | Entry ID | `ratdom_roundling2` |
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


## Roundlings, Ratdom maze 627 (ratdom_roundling3) { #v-ratdom_roundling3 }

**Entry ID:** `ratdom_roundling3` · **Type:** Enemy

**Location:** Roundlings: [ratdom_maze_627](../maps/ratdom_maze_627.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 200 |
| XP when defeated | 241 |
| Damage | 10 to 30 |
| Attack chance | 120 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_627](../maps/ratdom_maze_627.md) | Roundlings | 2 | Appears later, during a quest |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_roundling3)"

    | | |
    |---|---|
    | Entry ID | `ratdom_roundling3` |
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



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


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
