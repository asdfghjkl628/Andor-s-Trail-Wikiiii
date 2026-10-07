---
description: "Mara is an NPC who can also be fought in Andor's Trail, found in Crossglen. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_men_7.png){ .sprite } Mara

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_7.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Role** | Shopkeeper |
| **Found in** | Crossglen |
| **Class** | Humanoid |
| **HP** | 90 |
| **XP when defeated** | 95 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Mara. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, combat statistics, loot or shop stock. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`mara`](#v-mara) | NPC | Not on a map | shopkeeper | – |
| [`ratdom_mara`](#v-ratdom_mara) | Enemy | Crossglen: [crossglen](../maps/crossglen.md) | – | 90 |

## Not placed on a map (mara) { #v-mara }

**Entry ID:** `mara` · **Type:** NPC · **Role:** Shopkeeper

**Location:** not placed on any map; this entry is added to the world by a quest or scripted event.

### Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Green apple](../items/apple_green.md) | 100% | 5 |
| [Meat](../items/meat.md) | 100% | 5 |
| [Cooked meat](../items/meat_cooked.md) | 100% | 5 |
| [Carrot](../items/carrot.md) | 100% | 5 |
| [Bread](../items/bread.md) | 100% | 5 |
| [Mead](../items/mead.md) | 100% | 5 |

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Mara. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/mara1.json" data-npc="Mara" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-mara-mara1"></span>**`mara1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Rat infestation](../quests/odair.md#stage-100))* → [mara_thanks](#d-mara-mara_thanks)
    - branch 2 → [mara_default](#d-mara-mara_default)

    <span id="d-mara-mara_thanks"></span>**`mara_thanks`** Mara: “I heard you helped Odair clean out that old supply cave. Thanks a lot, we'll start using it soon.”

    - “It was my pleasure.” → [mara_default](#d-mara-mara_default)

    <span id="d-mara-mara_default"></span>**`mara_default`** Mara: “Never mind those drunken fellas, they're always causing trouble. Want something to eat?”

    - “Do you have anything to trade?” → *shop opens*



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (mara)"

    | | |
    |---|---|
    | Entry ID | `mara` |
    | Spawn group | `mara` |
    | Loot table | `shop_mara` |
    | Conversation | `mara1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:7` |
    | Defined in | `res/raw/monsterlist_crossglen_npcs.json` |

    Raw data:

    ```json
    {
     "id": "mara",
     "name": "Mara",
     "iconID": "monsters_men:7",
     "monsterClass": "humanoid",
     "spawnGroup": "mara",
     "phraseID": "mara1",
     "droplistID": "shop_mara"
    }
    ```


## Crossglen, Crossglen (ratdom_mara) { #v-ratdom_mara }

**Entry ID:** `ratdom_mara` · **Type:** Enemy

**Location:** Crossglen: [crossglen](../maps/crossglen.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 90 |
| XP when defeated | 95 |
| Damage | 1 to 4 |
| Attack chance | 60 |
| Block chance | 40 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Bread](../items/bread.md) | 100% | 1 to 2 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [crossglen](../maps/crossglen.md) | Crossglen | 1 | Appears later, during a quest |

### Quests that count defeats

- [More rats!](../quests/ratdom_mikhail.md#stage-30) with stepping on a trigger on [crossglen](../maps/crossglen.md) checks that this enemy has been defeated.
- [More rats!](../quests/ratdom_mikhail.md#stage-52) with [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)), [Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md)) checks that this enemy has been defeated.
- [More rats!](../quests/ratdom_mikhail.md#stage-54) with [Mikhail](../monsters/mikhail.md) ([home](../maps/home.md)), [Gruiik](../monsters/ratdom_mikhail.md) ([home](../maps/home.md)) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_mara)"

    | | |
    |---|---|
    | Entry ID | `ratdom_mara` |
    | Spawn group | `ratdom_mara` |
    | Loot table | `drop_ratdom_mara` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:7` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_mara",
     "name": "Mara",
     "iconID": "monsters_men:7",
     "maxHP": 90,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 1,
      "max": 4
     },
     "spawnGroup": "ratdom_mara",
     "droplistID": "drop_ratdom_mara",
     "attackCost": 5,
     "attackChance": 60,
     "blockChance": 40
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mara.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mara.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mara.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=mara.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
