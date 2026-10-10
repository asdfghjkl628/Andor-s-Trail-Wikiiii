---
description: "Bridge guard is an NPC you can also fight in Andor's Trail, found in Guynmart Castle."
---

# ![](../assets/icons/monsters/monsters_tometik6_1.png){ .sprite } Bridge guard

**Where to find Bridge guard:** Guynmart Castle: [Fields 5](../maps/fields5.md#pin-npc-guynmart_robber1)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik6_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Guynmart Castle |
| **Class** | Humanoid |
| **HP** | 120 |
| **XP when defeated** | 246 |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! warning "You can fight Bridge guard"
    Answering “Come and try to get it.” starts a fight with Bridge guard.

    Answering “Enough!” starts a fight with Bridge guard.

## Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 120 |
| XP when defeated | 246 |
| Damage | 1 to 4 |
| AC | 40 |
| BC | 150 |
| DR | 5 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 7 to 77 |

## Dialogue simulator

Set your quest stages and items, then talk to Bridge guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/guynmart_robber1_10.json" data-npc="Bridge guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-guynmart_robber1_10"></span>**`guynmart_robber1_10`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if have 2,000 gold)* → [guynmart_robber1_20](#d-guynmart_robber1_20)
    - branch 2 → [guynmart_robber1_12](#d-guynmart_robber1_12)

    <span id="d-guynmart_robber1_20"></span>**`guynmart_robber1_20`** Bridge guard: “I am the new Feygard bridge guard. Har har. Give me your gold.”

    - “OK. Here, you can have 50 pieces of gold. Let me pass now.” *(if pay 50 gold)* → [guynmart_robber1_30](#d-guynmart_robber1_30)
    - “Come and try to get it.” → *fight starts*
    - “Hmm, I will think about your offer.” → *conversation ends*

    <span id="d-guynmart_robber1_12"></span>**`guynmart_robber1_12`** Bridge guard: “I am the new Feygard bridge guard. Har har. We do not let beggars through. Understand? Come back, but only if you have more gold with you.”


    <span id="d-guynmart_robber1_30"></span>**`guynmart_robber1_30`** Bridge guard: “[Gold taken] Very good. But I need more.”

    - “Of course. Here, you can have another 50 pieces of gold.” *(if pay 50 gold)* → [guynmart_robber1_30](#d-guynmart_robber1_30)
    - “Enough!” → *fight starts*
    - “Hmm, I will think about your offer.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 4 lines added |

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
    | Entry ID | `guynmart_robber1` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `guynmart_robber1` |
    | Loot table | `guynmart_drp_robber` |
    | Conversation | `guynmart_robber1_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik6:1` |
    | Defined in | `res/raw/monsterlist_guynmart.json` |

    Raw data:

    ```json
    {
     "id": "guynmart_robber1",
     "name": "Bridge guard",
     "iconID": "monsters_tometik6:1",
     "maxHP": 120,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 1,
      "max": 4
     },
     "phraseID": "guynmart_robber1_10",
     "droplistID": "guynmart_drp_robber",
     "attackCost": 4,
     "attackChance": 40,
     "blockChance": 150,
     "damageResistance": 5
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_robber1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_robber1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_robber1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=guynmart_robber1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
