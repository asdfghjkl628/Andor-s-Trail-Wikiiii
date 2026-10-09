---
description: "Mara is an NPC you can also fight in Andor's Trail, found in Crossglen. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_men_7.png){ .sprite } Mara

**Where to find Mara:** [Appears during a quest or event](#v-mara), [Crossglen, Crossglen](#v-ratdom_mara)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_7.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Role** | Shopkeeper |
| **Found in** | Crossglen |
| **Class** | Humanoid |
| **HP** | 90 |
| **XP when defeated** | 95 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Appears during a quest or event { #v-mara }

**Where:** appears during a quest or scripted event. · **Role:** Shopkeeper

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

Set your quest stages and items, then talk to Mara. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/mara1.json" data-npc="Mara" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

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


## Crossglen, Crossglen { #v-ratdom_mara }

**Where:** Crossglen: [Crossglen](../maps/crossglen.md)

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 90 |
| XP when defeated | 95 |
| Damage | 1 to 4 |
| AC | 60 |
| BC | 40 |
| DR | 0 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Bread](../items/bread.md) | 100% | 1 to 2 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Crossglen](../maps/crossglen.md) | Crossglen | 1 | Appears later, during a quest |

### Quests that count defeats

- [More rats!](../quests/ratdom_mikhail.md#stage-30) with stepping on a trigger on [Crossglen](../maps/crossglen.md) checks that this enemy has been defeated.
- [More rats!](../quests/ratdom_mikhail.md#stage-52) with [Mikhail](../monsters/mikhail.md) ([Home](../maps/home.md)), [Gruiik](../monsters/ratdom_mikhail.md) ([Home](../maps/home.md)) checks that this enemy has been defeated.
- [More rats!](../quests/ratdom_mikhail.md#stage-54) with [Mikhail](../monsters/mikhail.md) ([Home](../maps/home.md)), [Gruiik](../monsters/ratdom_mikhail.md) ([Home](../maps/home.md)) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Mara. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, combat statistics, loot or shop stock.

| Entry | Type | Section |
|---|---|---|
| `mara` | NPC | [Appears during a quest or event](#v-mara) |
| `ratdom_mara` | Enemy | [Crossglen, Crossglen](#v-ratdom_mara) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: mara"

    | | |
    |---|---|
    | Entry ID | `mara` |
    | Type (wiki) | NPC |
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

??? info "Technical information: ratdom_mara"

    | | |
    |---|---|
    | Entry ID | `ratdom_mara` |
    | Type (wiki) | Enemy |
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
