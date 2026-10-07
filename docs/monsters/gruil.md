---
description: "Gruil is an NPC who can also be fought in Andor's Trail. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_rogue1_0.png){ .sprite } Gruil

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rogue1_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Role** | Shopkeeper |
| **Class** | Humanoid |
| **HP** | 160 |
| **XP when defeated** | 112 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Gruil. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, combat statistics, loot or shop stock. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`gruil`](#v-gruil) | NPC | Not on a map | shopkeeper | – |
| [`ratdom_gruil`](#v-ratdom_gruil) | Enemy | Not on a map | – | 160 |

## Not placed on a map (gruil) { #v-gruil }

**Entry ID:** `gruil` · **Type:** NPC · **Role:** Shopkeeper

**Location:** not placed on any map; this entry is added to the world by a quest or scripted event.

### Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Iron dagger](../items/dagger0.md) | 100% | 1 |
| [Weathered shirt](../items/shirt_weathered.md) | 100% | 1 |
| [Crude combat ring](../items/ring_crude_combat.md) | 100% | 1 |
| [Bar brawler's ring](../items/ring_barbrawler.md) | 100% | 1 |
| [Glass gem](../items/gem1.md) | 100% | 5 |
| [Ruby gem](../items/gem2.md) | 100% | 5 |
| [Polished gem](../items/gem3.md) | 100% | 5 |

### Quests

- [Search for Andor](../quests/andor.md): stages 20, 30

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Gruil. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/gruil1.json" data-npc="Gruil" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (8 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-gruil-gruil1"></span>**`gruil1`** Gruil: “Psst, hey. Wanna trade?”

    - “Sure, let's trade.” → *shop opens*
    - “I heard that you talked to my brother a while ago.” *(if reached stage 10 of [Search for Andor](../quests/andor.md#stage-10))* → [gruil_select](#d-gruil-gruil_select)

    <span id="d-gruil-gruil_select"></span>**`gruil_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Search for Andor](../quests/andor.md#stage-30))* → [gruil_return](#d-gruil-gruil_return)
    - branch 2 → [gruil2](#d-gruil-gruil2)

    <span id="d-gruil-gruil_return"></span>**`gruil_return`** Gruil: “Look kid, I already told you.”

    - Next → [gruil_andor1](#d-gruil-gruil_andor1)

    <span id="d-gruil-gruil2"></span>**`gruil2`** Gruil: “Your brother? Oh you mean Andor? I might know something, but that information will cost you. Bring me a poison gland from one of those poisonous snakes and maybe I'll tell you.” — **effects:** sets stage 20 of [Search for Andor](../quests/andor.md#stage-20)

    - “Here, I have a poison gland for you.” *(if hand over 1× [Poison gland](../items/gland.md))* → [gruil_complete](#d-gruil-gruil_complete)
    - “OK, I'll bring one.” → *conversation ends*

    <span id="d-gruil-gruil_andor1"></span>**`gruil_andor1`** Gruil: “I talked to him yesterday. He asked if I knew someone called Umar or something like that. I have no idea who he was talking about.”

    - Next → [gruil_andor2](#d-gruil-gruil_andor2)

    <span id="d-gruil-gruil_complete"></span>**`gruil_complete`** Gruil: “Thanks a lot kid. This will do just fine.” — **effects:** sets stage 30 of [Search for Andor](../quests/andor.md#stage-30)

    - Next → [gruil_andor1](#d-gruil-gruil_andor1)

    <span id="d-gruil-gruil_andor2"></span>**`gruil_andor2`** Gruil: “He seemed really upset about something and left in a hurry. Something about the Thieves' Guild in Fallhaven.”

    - Next → [gruil_andor3](#d-gruil-gruil_andor3)

    <span id="d-gruil-gruil_andor3"></span>**`gruil_andor3`** Gruil: “That's all I know. Maybe you should ask around in Fallhaven. Look for my friend Gaela, he probably knows more.”

    - “Thanks, bye.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (gruil)"

    | | |
    |---|---|
    | Entry ID | `gruil` |
    | Spawn group | `gruil` |
    | Loot table | `shop_gruil` |
    | Conversation | `gruil1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rogue1:0` |
    | Defined in | `res/raw/monsterlist_crossglen_npcs.json` |

    Raw data:

    ```json
    {
     "id": "gruil",
     "name": "Gruil",
     "iconID": "monsters_rogue1:0",
     "monsterClass": "humanoid",
     "spawnGroup": "gruil",
     "phraseID": "gruil1",
     "droplistID": "shop_gruil"
    }
    ```


## Not placed on a map (ratdom_gruil) { #v-ratdom_gruil }

**Entry ID:** `ratdom_gruil` · **Type:** Enemy

**Location:** not placed on any map; this entry is added to the world by a quest or scripted event.

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 160 |
| XP when defeated | 112 |
| Damage | 2 to 5 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Glass gem](../items/gem1.md) | 50% | 1 |


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_gruil)"

    | | |
    |---|---|
    | Entry ID | `ratdom_gruil` |
    | Spawn group | `ratdom_gruil` |
    | Loot table | `drop_ratdom_gruil` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rogue1:0` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_gruil",
     "name": "Gruil",
     "iconID": "monsters_rogue1:0",
     "maxHP": 160,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 5
     },
     "spawnGroup": "ratdom_gruil",
     "droplistID": "drop_ratdom_gruil"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gruil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gruil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gruil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gruil.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
