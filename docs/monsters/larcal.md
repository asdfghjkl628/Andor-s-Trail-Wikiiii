---
description: "Larcal is an NPC you can also fight in Andor's Trail."
---

# ![](../assets/icons/monsters/monsters_men2_2.png){ .sprite } Larcal

**Where to find Larcal:** appears during a quest or scripted event.

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men2_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Class** | Humanoid |
| **HP** | 51 |
| **XP when defeated** | 55 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "You can fight Larcal"
    Answering “At last, a fight. I have been waiting for this!” starts a fight with Larcal.

## Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 51 |
| XP when defeated | 55 |
| Damage | 1 to 2 |
| AC | 25 |
| BC | 50 |
| DR | 0 |
| Attacks per turn | 1 (9 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 70% | 4 to 12 |
| [Wooden club](../items/club1.md) | 100% | 1 |
| [Calomyran secrets](../items/calomyran_secrets.md) | 100% | 1 |
| [Milk](../items/milk.md) | 100% | 1 |

## Dialogue simulator

Set your quest stages and items, then talk to Larcal. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/larcal.json" data-npc="Larcal" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-larcal"></span>**`larcal`** Larcal: “I don't have time for you, kid. Get lost.”

    - “I found a note with your name on it while looking for the book 'Calomyran Secrets'.” *(if reached stage 20 of [Calomyran secrets](../quests/calomyran.md#stage-20))* → [larcal_1](#d-larcal_1)

    <span id="d-larcal_1"></span>**`larcal_1`** Larcal: “Now now, what have we here? Are you implying that I have been down in Arcir's basement?”

    - Next → [larcal_2](#d-larcal_2)

    <span id="d-larcal_2"></span>**`larcal_2`** Larcal: “So, maybe I was. The book is mine anyway.”

    - Next → [larcal_3](#d-larcal_3)

    <span id="d-larcal_3"></span>**`larcal_3`** Larcal: “Look, let's solve this peacefully. You walk away and forget about that book, and you might still live.”

    - “Very well. Keep your book.” → [larcal_4](#d-larcal_4)
    - “No, you will give me that book.” → [larcal_5](#d-larcal_5)

    <span id="d-larcal_4"></span>**`larcal_4`** Larcal: “Good, now run away.”


    <span id="d-larcal_5"></span>**`larcal_5`** Larcal: “OK, now you're starting to annoy me, kid. Get lost while you still can.”

    - “Very well. I will leave.” → *conversation ends*
    - “No, that book is not yours!” → [larcal_6](#d-larcal_6)

    <span id="d-larcal_6"></span>**`larcal_6`** Larcal: “You are still here? OK then, if you want the book that bad, you will have to take it from me!”

    - “At last, a fight. I have been waiting for this!” → *fight starts*
    - “I had hoped it wouldn't come to this.” → *fight starts*
    - “Very well. I will leave.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed<br>· text: “You are still here? Ok then, if you want the book that bad, you will …” → “You are still here? OK then, if you want the book that bad, you will …”<br>· text: “Ok, now you're starting to annoy me, kid. Get lost while you still ca…” → “OK, now you're starting to annoy me, kid. Get lost while you still ca…” |
| [v0.7.4](../versions/0.7.4.md) | Attack cost: 10 → 9 |
| [v0.8.3](../versions/0.8.3.md) | Dialogue: 1 line changed<br>· text: “Good boy. Now run away.” → “Good, now run away.” |

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
    | Entry ID | `larcal` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `larcal` |
    | Loot table | `larcal` |
    | Conversation | `larcal` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men2:2` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "larcal",
     "name": "Larcal",
     "iconID": "monsters_men2:2",
     "maxHP": 51,
     "maxAP": 10,
     "moveCost": 10,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 1,
      "max": 2
     },
     "spawnGroup": "larcal",
     "phraseID": "larcal",
     "droplistID": "larcal",
     "attackCost": 9,
     "attackChance": 25,
     "blockChance": 50
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=larcal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=larcal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=larcal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=larcal.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
