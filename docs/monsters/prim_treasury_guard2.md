---
description: "Strong Prim treasury guard is an NPC you can also fight in Andor's Trail, found in Prim."
---

# ![](../assets/icons/monsters/monsters_rltiles1_69.png){ .sprite } Strong Prim treasury guard

**Where to find Strong Prim treasury guard:** Prim: [Blackwater mountain 25](../maps/blackwater_mountain25.md#pin-npc-prim_treasury_guard2)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rltiles1_69.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Prim |
| **Class** | Humanoid |
| **HP** | 160 |
| **XP when defeated** | 603 |
| **Introduced** | [v0.8.15](../versions/0.8.15.md) |

</div>

!!! warning "You can fight Strong Prim treasury guard"
    Answering “Forget it. Prepare to die!” starts a fight with Strong Prim treasury guard.

## Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 160 |
| XP when defeated | 603 |
| Damage | 25 to 40 |
| AC | 160 |
| BC | 170 |
| DR | 13 |
| Attacks per turn | 2 (5 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Dialogue simulator

Talk to Strong Prim treasury guard as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/prim_treasury_guard2.json" data-npc="Strong Prim treasury guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (3 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-prim_treasury_guard2"></span>**`prim_treasury_guard2`** Strong Prim treasury guard: “Well, well, well.”

    - “Eh, you look bigger than before. And stronger.” → [prim_treasury_guard2_10](#d-prim_treasury_guard2_10)

    <span id="d-prim_treasury_guard2_10"></span>**`prim_treasury_guard2_10`** Strong Prim treasury guard: “It's a good thing I noticed my colleague has left his post. He was pretty weak anyway.”

    - “Listen, we could avoid some trouble. I'll give you 200 gold pieces if you let me pass.” → [prim_treasury_guard2_20](#d-prim_treasury_guard2_20)

    <span id="d-prim_treasury_guard2_20"></span>**`prim_treasury_guard2_20`** Strong Prim treasury guard: “Make it 2,000, then we have a deal.”

    - “OK, here.” *(if pay 2,000 gold)* → *NPC leaves*
    - “Forget it. Prepare to die!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.8.15](../versions/0.8.15.md) | Added<br>Dialogue: 3 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “Make it 2000, then we have a deal.” → “Make it {2000}, then we have a deal.” |

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
    | Entry ID | `prim_treasury_guard2` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `prim_treasury_guard2` |
    | Loot table | – |
    | Conversation | `prim_treasury_guard2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:69` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "prim_treasury_guard2",
     "name": "Strong Prim treasury guard",
     "iconID": "monsters_rltiles1:69",
     "maxHP": 160,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 25,
      "max": 40
     },
     "spawnGroup": "prim_treasury_guard2",
     "phraseID": "prim_treasury_guard2",
     "attackCost": 5,
     "attackChance": 160,
     "blockChance": 170,
     "damageResistance": 13
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_treasury_guard2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_treasury_guard2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_treasury_guard2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=prim_treasury_guard2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
