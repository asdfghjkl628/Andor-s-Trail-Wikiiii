---
description: "Ewmondold is an NPC who can also be fought in Andor's Trail, found in snakecave3, Blackwater Mountain. Starts Perception is not reality."
---

# ![](../assets/icons/monsters/monsters_tometik1_18.png){ .sprite } Ewmondold

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik1_18.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Role** | Starts [Perception is not reality](../quests/new_snake_master.md) |
| **Found in** | snakecave3, Blackwater Mountain |
| **Class** | Humanoid |
| **HP** | 70 |
| **XP when defeated** | 150 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.7.12](../versions/0.7.12.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Ewmondold. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, combat statistics, loot or shop stock, appearance, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`ewmondold_snake_master`](#v-ewmondold_snake_master) | NPC/Enemy | [snakecave3](../maps/snakecave3.md#pin-npc-ewmondold_snake_master) | – | 70 |
| [`inspiring_snake_master`](#v-inspiring_snake_master) | NPC | Blackwater Mountain: [wild2](../maps/wild2.md#pin-npc-inspiring_snake_master) | starts [Perception is not reality](../quests/new_snake_master.md) | – |

## Snakecave3 (ewmondold_snake_master) { #v-ewmondold_snake_master }

**Entry ID:** `ewmondold_snake_master` · **Type:** NPC/Enemy

**Location:** [snakecave3](../maps/snakecave3.md#pin-npc-ewmondold_snake_master)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 70 |
| XP when defeated | 150 |
| Damage | 2 to 5 |
| Attack chance | 67 |
| Block chance | 13 |
| Damage resistance | 4 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 200 |
| Critical multiplier | 3.0 |
| Critical hit chance | 58% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 200 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [snakecave3](../maps/snakecave3.md) | – | 1 | Appears later, during a quest |

### Quests that count defeats

- A conversation with [Arcir](../monsters/arcir.md) checks that this enemy has been defeated.
- A conversation with stepping on a trigger on [snakecave3](../maps/snakecave3.md) checks that this enemy has been defeated.

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Ewmondold. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ewmondold_snake_master_10.json" data-npc="Ewmondold" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ewmondold_snake_master-ewmondold_snake_master_10"></span>**`ewmondold_snake_master_10`** Ewmondold: “My new powers have enhanced my appearance, don't you agree?”

    - “You are too dangerous to be kept alive.” → [ewmondold_snake_master_20](#d-ewmondold_snake_master-ewmondold_snake_master_20)

    <span id="d-ewmondold_snake_master-ewmondold_snake_master_20"></span>**`ewmondold_snake_master_20`** Ewmondold: “Oh, you think you can stop me, do you? Come and try!”

    - “I won't try, I'll succeed!” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ewmondold_snake_master)"

    | | |
    |---|---|
    | Entry ID | `ewmondold_snake_master` |
    | Spawn group | `ewmondold_snake_master` |
    | Loot table | `gold200` |
    | Conversation | `ewmondold_snake_master_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik1:18` |
    | Defined in | `res/raw/monsterlist_brimhaven_2.json` |

    Raw data:

    ```json
    {
     "id": "ewmondold_snake_master",
     "name": "Ewmondold",
     "iconID": "monsters_tometik1:18",
     "maxHP": 70,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 5
     },
     "phraseID": "ewmondold_snake_master_10",
     "droplistID": "gold200",
     "attackCost": 5,
     "attackChance": 67,
     "criticalSkill": 200,
     "criticalMultiplier": 3.0,
     "blockChance": 13,
     "damageResistance": 4
    }
    ```


## Blackwater Mountain, Wild2 (inspiring_snake_master) { #v-inspiring_snake_master }

**Entry ID:** `inspiring_snake_master` · **Type:** NPC · **Role:** Starts [Perception is not reality](../quests/new_snake_master.md)

**Location:** Blackwater Mountain: [wild2](../maps/wild2.md#pin-npc-inspiring_snake_master)

### Quests

- [Perception is not reality](../quests/new_snake_master.md): stages 5, 10, 20

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Ewmondold. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/inspiring_snake_master_10.json" data-npc="Ewmondold" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-inspiring_snake_master-inspiring_snake_master_10"></span>**`inspiring_snake_master_10`** Ewmondold: “Hello, young adventurer. I am Ewmondold, a world famous traveler.”

    - Next → [inspiring_snake_master_select](#d-inspiring_snake_master-inspiring_snake_master_select)

    <span id="d-inspiring_snake_master-inspiring_snake_master_select"></span>**`inspiring_snake_master_select`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT killed 1× [Snake master](../monsters/snake_master.md); NOT reached stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5))* → [inspiring_snake_master_30](#d-inspiring_snake_master-inspiring_snake_master_30)
    - Next *(if reached stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5); NOT killed 1× [Snake master](../monsters/snake_master.md))* → [inspiring_snake_master_25](#d-inspiring_snake_master-inspiring_snake_master_25)
    - Next *(if killed 1× [Snake master](../monsters/snake_master.md); NOT reached stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5))* → [inspiring_snake_master_20](#d-inspiring_snake_master-inspiring_snake_master_20)
    - Next *(if reached stage 20 of [Perception is not reality](../quests/new_snake_master.md#stage-20); NOT reached stage 25 of [Perception is not reality](../quests/new_snake_master.md#stage-25))* → [inspiring_snake_master_20](#d-inspiring_snake_master-inspiring_snake_master_20)
    - Next *(if reached stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5); NOT carry 1× [Ewmondold's map](../items/inspiring_snake_master_map.md))* → [inspiring_snake_master_25](#d-inspiring_snake_master-inspiring_snake_master_25)
    - Next *(if reached stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5); killed 1× [Snake master](../monsters/snake_master.md); hand over 1× [Ewmondold's map](../items/inspiring_snake_master_map.md))* → [inspiring_snake_master_80](#d-inspiring_snake_master-inspiring_snake_master_80)

    <span id="d-inspiring_snake_master-inspiring_snake_master_30"></span>**`inspiring_snake_master_30`** Ewmondold: “Are you looking to help a man in need?”

    - “Not right now. Bye.” → *conversation ends*
    - “Yes, of course I am. What can I do for you?” → [inspiring_snake_master_40](#d-inspiring_snake_master-inspiring_snake_master_40)

    <span id="d-inspiring_snake_master-inspiring_snake_master_25"></span>**`inspiring_snake_master_25`** Ewmondold: “Have you found my map yet?”

    - “No, not yet.” → *conversation ends*

    <span id="d-inspiring_snake_master-inspiring_snake_master_20"></span>**`inspiring_snake_master_20`** Ewmondold: “Thanks for killing the Snake master, sucker - the way for me to rule is now free...” — **effects:** removes monsters from wild2, sets stage 10 of [Perception is not reality](../quests/new_snake_master.md#stage-10), spawns monsters on snakecave3


    <span id="d-inspiring_snake_master-inspiring_snake_master_80"></span>**`inspiring_snake_master_80`** Ewmondold: “Ah, my 'map'. Good!” — **effects:** sets stage 20 of [Perception is not reality](../quests/new_snake_master.md#stage-20)

    - Next → [inspiring_snake_master_20](#d-inspiring_snake_master-inspiring_snake_master_20)

    <span id="d-inspiring_snake_master-inspiring_snake_master_40"></span>**`inspiring_snake_master_40`** Ewmondold: “I too am an adventurer. I recently attempted to make my way through this here cave.”

    - Next → [inspiring_snake_master_50](#d-inspiring_snake_master-inspiring_snake_master_50)

    <span id="d-inspiring_snake_master-inspiring_snake_master_50"></span>**`inspiring_snake_master_50`** Ewmondold: “In the beginning it was relatively easy. It wasn't until I ran into the Snake master's minions.”

    - Next → [inspiring_snake_master_60](#d-inspiring_snake_master-inspiring_snake_master_60)

    <span id="d-inspiring_snake_master-inspiring_snake_master_60"></span>**`inspiring_snake_master_60`** Ewmondold: “I was quickly ambushed and was forced to flee in order to save my life. But of course, during my attempt to flee, I dropped my map.”

    - “I could retrieve the map for you.” → [inspiring_snake_master_70](#d-inspiring_snake_master-inspiring_snake_master_70)

    <span id="d-inspiring_snake_master-inspiring_snake_master_70"></span>**`inspiring_snake_master_70`** Ewmondold: “Please do and hurry back to me.” — **effects:** sets stage 5 of [Perception is not reality](../quests/new_snake_master.md#stage-5)




### Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 10 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (inspiring_snake_master)"

    | | |
    |---|---|
    | Entry ID | `inspiring_snake_master` |
    | Spawn group | `inspiring_snake_master` |
    | Loot table | – |
    | Conversation | `inspiring_snake_master_10` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles2:82` |
    | Defined in | `res/raw/monsterlist_brimhaven_2.json` |

    Raw data:

    ```json
    {
     "id": "inspiring_snake_master",
     "name": "Ewmondold",
     "iconID": "monsters_rltiles2:82",
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "inspiring_snake_master",
     "phraseID": "inspiring_snake_master_10"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ewmondold_snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ewmondold_snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ewmondold_snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ewmondold_snake_master.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
