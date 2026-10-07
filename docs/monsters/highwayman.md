---
description: "Highwayman is an NPC who can also be fought in Andor's Trail, found in Fallhaven, way_to_sullengard_east9."
---

# ![](../assets/icons/monsters/monsters_men_8.png){ .sprite } Highwayman

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_8.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Fallhaven, way_to_sullengard_east9 |
| **Class** | Humanoid |
| **HP** | 54–200 |
| **XP when defeated** | 85–621 |
| **Entries in game data** | 3 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "3 entries in the game data"
    The game's data files define 3 separate characters named Highwayman. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, combat statistics, loot or shop stock, faction, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`highwayman`](#v-highwayman) | NPC/Enemy | Fallhaven: [wild9](../maps/wild9.md#pin-npc-highwayman) | – | 54 |
| [`highwayman1`](#v-highwayman1) | NPC/Enemy | Fallhaven: [roadbeforecrossroads3](../maps/roadbeforecrossroads3.md#pin-npc-highwayman1) | – | 154 |
| [`sullengard_highwayman`](#v-sullengard_highwayman) | NPC/Enemy | [way_to_sullengard_east9](../maps/way_to_sullengard_east9.md#pin-npc-sullengard_highwayman) | – | 200 |

## Fallhaven, Wild9 (highwayman) { #v-highwayman }

**Entry ID:** `highwayman` · **Type:** NPC/Enemy

**Location:** Fallhaven: [wild9](../maps/wild9.md#pin-npc-highwayman)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 54 |
| XP when defeated | 85 |
| Damage | 2 to 4 |
| Attack chance | 90 |
| Block chance | 30 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 50 |
| Critical multiplier | 2.0 |
| Critical hit chance | 26% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 4 to 41 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [wild9](../maps/wild9.md) | Fallhaven | 1 | – |

### Quests that count defeats

- [Unusual experiences and achievements](../quests/achievements.md#stage-20) with stepping on a trigger on [wild9](../maps/wild9.md) checks that at least 20 of these enemies have been defeated.
- A conversation with [Highwayman](../monsters/highwayman.md#v-sullengard_highwayman) ([way_to_sullengard_east9](../maps/way_to_sullengard_east9.md)) checks that this enemy has been defeated.

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Highwayman. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/bandit1.json" data-npc="Highwayman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-highwayman-bandit1"></span>**`bandit1`** Highwayman: “What have we here? A lost wanderer?” — **effects:** faction “fct_bandit1” set to -10

    - Next → [bandit1_2](#d-highwayman-bandit1_2)

    <span id="d-highwayman-bandit1_2"></span>**`bandit1_2`** Highwayman: “How much is your life worth to you? Give me 100 gold and I'll let you go.”

    - “OK OK. Here is the gold. Please don't hurt me!” *(if pay 100 gold)* → [bandit1_3](#d-highwayman-bandit1_3)
    - “How about we fight over it?” → [bandit1_4](#d-highwayman-bandit1_4)
    - “How much is your life worth?” → [bandit1_4](#d-highwayman-bandit1_4)

    <span id="d-highwayman-bandit1_3"></span>**`bandit1_3`** Highwayman: “About damn time. You are free to go.” — **effects:** faction “fct_bandit1” set to 11

    - Next → *NPC leaves*

    <span id="d-highwayman-bandit1_4"></span>**`bandit1_4`** Highwayman: “OK then, your life it is. Let's fight. I have been looking forward to a good fight!”

    - “Let's fight!” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Faction: added (fct_bandit1)<br>Movement: added (protectSpawn)<br>Dialogue: 4 lines changed<br>· text: “Ok then, your life it is. Let's fight. I have been looking forward to…” → “OK then, your life it is. Let's fight. I have been looking forward to…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (highwayman)"

    | | |
    |---|---|
    | Entry ID | `highwayman` |
    | Spawn group | `bandit1` |
    | Loot table | `bandit1` |
    | Conversation | `bandit1` |
    | Faction | `fct_bandit1` |
    | Movement | protectSpawn |
    | Icon | `monsters_men:8` |
    | Defined in | `res/raw/monsterlist_wilderness.json` |

    Raw data:

    ```json
    {
     "id": "highwayman",
     "name": "Highwayman",
     "iconID": "monsters_men:8",
     "maxHP": 54,
     "monsterClass": "humanoid",
     "movementAggressionType": "protectSpawn",
     "attackDamage": {
      "min": 2,
      "max": 4
     },
     "spawnGroup": "bandit1",
     "faction": "fct_bandit1",
     "phraseID": "bandit1",
     "droplistID": "bandit1",
     "attackCost": 5,
     "attackChance": 90,
     "criticalSkill": 50,
     "criticalMultiplier": 2.0,
     "blockChance": 30,
     "damageResistance": 2
    }
    ```


## Fallhaven, Roadbeforecrossroads3 (highwayman1) { #v-highwayman1 }

**Entry ID:** `highwayman1` · **Type:** NPC/Enemy

**Location:** Fallhaven: [roadbeforecrossroads3](../maps/roadbeforecrossroads3.md#pin-npc-highwayman1)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 154 |
| XP when defeated | 239 |
| Damage | 2 to 7 |
| Attack chance | 160 |
| Block chance | 70 |
| Damage resistance | 4 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 1 to 20 |
| [Torn shirt](../items/shirt_torn.md) | 100% | 1 |
| [Mead](../items/mead.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [roadbeforecrossroads3](../maps/roadbeforecrossroads3.md) | Fallhaven | 1 | – |

### Quests that count defeats

- A conversation with [Highwayman](../monsters/highwayman.md#v-sullengard_highwayman) ([way_to_sullengard_east9](../maps/way_to_sullengard_east9.md)) checks that this enemy has been defeated.

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Highwayman. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/highwayman1.json" data-npc="Highwayman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-highwayman1-highwayman1"></span>**`highwayman1`** Highwayman: “Hold up. What have we here? A lone traveller on the Duleian road.” — **effects:** faction “fct_highwayman1” set to -10

    - Next → [highwayman1_2](#d-highwayman1-highwayman1_2)

    <span id="d-highwayman1-highwayman1_2"></span>**`highwayman1_2`** Highwayman: “Haven't you heard, travelling this road can be dangerous.”

    - Next → [highwayman1_3](#d-highwayman1-highwayman1_3)

    <span id="d-highwayman1-highwayman1_3"></span>**`highwayman1_3`** Highwayman: “There have been reports of people being robbed of all their possessions whilst travelling down this road.”

    - Next → [highwayman1_4](#d-highwayman1-highwayman1_4)

    <span id="d-highwayman1-highwayman1_4"></span>**`highwayman1_4`** Highwayman: “Tell you what, if you give me ... shall we say ... 500 gold, I can almost guarantee that you won't be robbed on this road.”

    - “Sounds good. Here is 500 gold.” *(if pay 500 gold)* → [highwayman1_5](#d-highwayman1-highwayman1_5)
    - “Hey, that sounds like robbery to me!” → [highwayman1_7](#d-highwayman1-highwayman1_7)
    - “How about I just kill you instead?” → [highwayman1_6](#d-highwayman1-highwayman1_6)

    <span id="d-highwayman1-highwayman1_5"></span>**`highwayman1_5`** Highwayman: “Thank you. Have a pleasant day. Watch out for those robbers!” — **effects:** faction “fct_highwayman1” set to 11

    - Next → *NPC leaves*

    <span id="d-highwayman1-highwayman1_7"></span>**`highwayman1_7`** Highwayman: “Oh no no, are you accusing me of robbing you? That's not the case at all. I'm just asking for 500 gold so that you won't be robbed of all your possessions while travelling down this road.”

    - “OK. Here is 500 gold.” *(if pay 500 gold)* → [highwayman1_5](#d-highwayman1-highwayman1_5)
    - “How about I just kill you instead?” → [highwayman1_6](#d-highwayman1-highwayman1_6)

    <span id="d-highwayman1-highwayman1_6"></span>**`highwayman1_6`** Highwayman: “Oh, I see. You are trying to rob ME instead? Well then, I will not be so easily defeated. Prepare yourself.”

    - “Fight!” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Faction: added (fct_highwayman1)<br>Unique flag: removed (was 1)<br>Dialogue: 4 lines changed<br>· text: “Tell you what, if you give me .. shall we say .. 500 gold, I can almo…” → “Tell you what, if you give me ... shall we say ... 500 gold, I can al…” |
| [v0.8.7](../versions/0.8.7.md) | Class: added (humanoid) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (highwayman1)"

    | | |
    |---|---|
    | Entry ID | `highwayman1` |
    | Spawn group | `highwayman1` |
    | Loot table | `highwayman1` |
    | Conversation | `highwayman1` |
    | Faction | `fct_highwayman1` |
    | Movement | – |
    | Icon | `monsters_men:8` |
    | Defined in | `res/raw/monsterlist_v070_npcs.json` |

    Raw data:

    ```json
    {
     "id": "highwayman1",
     "name": "Highwayman",
     "iconID": "monsters_men:8",
     "maxHP": 154,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 7
     },
     "faction": "fct_highwayman1",
     "phraseID": "highwayman1",
     "droplistID": "highwayman1",
     "attackCost": 5,
     "attackChance": 160,
     "blockChance": 70,
     "damageResistance": 4
    }
    ```


## Way to sullengard east9 (sullengard_highwayman) { #v-sullengard_highwayman }

**Entry ID:** `sullengard_highwayman` · **Type:** NPC/Enemy

**Location:** [way_to_sullengard_east9](../maps/way_to_sullengard_east9.md#pin-npc-sullengard_highwayman)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 200 |
| XP when defeated | 621 |
| Damage | 10 to 20 |
| Attack chance | 200 |
| Block chance | 150 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 50 |
| Critical multiplier | 2.0 |
| Critical hit chance | 26% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Bandit's Brew](../items/sullengrad_bandit_brew.md) | 10% | 1 |
| [Gold coins](../items/gold.md) | 70% | 51 to 106 |
| [Ring of damage +5](../items/ring_dmg5.md) | 5% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [way_to_sullengard_east9](../maps/way_to_sullengard_east9.md) | – | 1 | – |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Highwayman. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_highwayman.json" data-npc="Highwayman" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sullengard_highwayman-sullengard_highwayman"></span>**`sullengard_highwayman`** Highwayman: “I've been looking for someone who fits your description.” — **effects:** faction “fct_highwayman2” set to -10

    - “You have? Why?” → [sullengard_highwayman_2](#d-sullengard_highwayman-sullengard_highwayman_2)

    <span id="d-sullengard_highwayman-sullengard_highwayman_2"></span>**`sullengard_highwayman_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if killed 0× [Highwayman](../monsters/highwayman.md#v-highwayman1))* → [sullengard_highwayman_2a](#d-sullengard_highwayman-sullengard_highwayman_2a)
    - branch 2 *(if killed 0× [Highwayman](../monsters/highwayman.md))* → [sullengard_highwayman_2b](#d-sullengard_highwayman-sullengard_highwayman_2b)
    - branch 3 → [sullengard_highwayman_3](#d-sullengard_highwayman-sullengard_highwayman_3)

    <span id="d-sullengard_highwayman-sullengard_highwayman_2a"></span>**`sullengard_highwayman_2a`** Highwayman: “Yes! You are the one that has killed my fellow "road travellers" and now you must pay!”

    - “Bring it on!” → *fight starts*

    <span id="d-sullengard_highwayman-sullengard_highwayman_2b"></span>**`sullengard_highwayman_2b`** Highwayman: “Yes! You are the one that has killed my fellow "road travellers" and now you must pay!”

    - “Bring it on!” → *fight starts*

    <span id="d-sullengard_highwayman-sullengard_highwayman_3"></span>**`sullengard_highwayman_3`** Highwayman: “Yes, you do look like him. He is the one who helped Sullengard financially on many occasions.”

    - “Hey, it must be my brother Andor! Tell me more about him.” → [sullengard_highwayman_4](#d-sullengard_highwayman-sullengard_highwayman_4)

    <span id="d-sullengard_highwayman-sullengard_highwayman_4"></span>**`sullengard_highwayman_4`** Highwayman: “Pay me 750 gold coins first or I'll rob you and then the Sullengard for my living!”

    - “Fine. Here's 750 gold coins. Now, tell me about him.” *(if pay 750 gold)* → [sullengard_highwayman_5](#d-sullengard_highwayman-sullengard_highwayman_5)
    - “Bring it on!” → *fight starts*

    <span id="d-sullengard_highwayman-sullengard_highwayman_5"></span>**`sullengard_highwayman_5`** Highwayman: “He is taller and stronger than you. Have a good time!” — **effects:** faction “fct_highwayman2” set to 11

    - branch 1 → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (sullengard_highwayman)"

    | | |
    |---|---|
    | Entry ID | `sullengard_highwayman` |
    | Spawn group | `sullengard_highwayman` |
    | Loot table | `sullengard_highwayman_drop` |
    | Conversation | `sullengard_highwayman` |
    | Faction | `fct_highwayman2` |
    | Movement | – |
    | Icon | `monsters_men:8` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_highwayman",
     "name": "Highwayman",
     "iconID": "monsters_men:8",
     "maxHP": 200,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 10,
      "max": 20
     },
     "spawnGroup": "sullengard_highwayman",
     "faction": "fct_highwayman2",
     "phraseID": "sullengard_highwayman",
     "droplistID": "sullengard_highwayman_drop",
     "attackCost": 5,
     "attackChance": 200,
     "criticalSkill": 50,
     "criticalMultiplier": 2.0,
     "blockChance": 150,
     "damageResistance": 3
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=highwayman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=highwayman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=highwayman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=highwayman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
