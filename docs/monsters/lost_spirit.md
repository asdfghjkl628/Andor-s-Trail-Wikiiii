---
description: "Lost spirit is an NPC you can also fight in Andor's Trail, found in Crossglen."
---

# ![](../assets/icons/monsters/monsters_rltiles2_45.png){ .sprite } Lost spirit

**Where to find Lost spirit:** Crossglen: [Hauntedhouse 1](../maps/hauntedhouse1.md#pin-npc-lost_spirit), Crossglen: [Wild 4](../maps/wild4.md#pin-npc-lost_spirit), [Hauntedhouse 2](../maps/hauntedhouse2.md#pin-npc-lost_spirit)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_45.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Crossglen |
| **Class** | Ghost |
| **HP** | 15 |
| **XP when defeated** | 33 |
| **Immune to crits** | Yes |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "You can fight Lost spirit"
    Answering “Oh, I'll free you from it alright.” starts a fight with Lost spirit.

## Combat

| | |
|---|---|
| Class | Ghost |
| HP | 15 |
| XP when defeated | 33 |
| Damage | 1 to 2 |
| AC | 50 |
| BC | 10 |
| DR | 3 |
| Attacks per turn | 1 (9 AP each, 10 AP) |
| Crit chance | none |

**Immune to critical hits.**


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Small empty vial](../items/vial_empty1.md) | 25% | 1 |
| [Glass gem](../items/gem1.md) | 25% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Hauntedhouse 1](../maps/hauntedhouse1.md) | Crossglen | 2 | – |
| [Hauntedhouse 2](../maps/hauntedhouse2.md) | – | 2 | – |
| [Wild 4](../maps/wild4.md) | Crossglen | 1 | – |

## Dialogue simulator

Set your quest stages and items, then talk to Lost spirit. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/haunt.json" data-npc="Lost spirit" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-haunt"></span>**`haunt`** Lost spirit: “Oh mortal, free me from this cursed world!”

    - “Oh, I'll free you from it alright.” → *fight starts*
    - “You mean, by killing you?” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.4](../versions/0.7.4.md) | Attack cost: 10 → 9 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `lost_spirit` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `minorhaunt1` |
    | Loot table | `haunt` |
    | Conversation | `haunt` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:45` |
    | Defined in | `res/raw/monsterlist_fallhaven_animals.json` |

    Raw data:

    ```json
    {
     "id": "lost_spirit",
     "name": "Lost spirit",
     "iconID": "monsters_rltiles2:45",
     "maxHP": 15,
     "monsterClass": "ghost",
     "attackDamage": {
      "min": 1,
      "max": 2
     },
     "spawnGroup": "minorhaunt1",
     "phraseID": "haunt",
     "droplistID": "haunt",
     "attackCost": 9,
     "attackChance": 50,
     "blockChance": 10,
     "damageResistance": 3
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lost_spirit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lost_spirit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lost_spirit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lost_spirit.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
