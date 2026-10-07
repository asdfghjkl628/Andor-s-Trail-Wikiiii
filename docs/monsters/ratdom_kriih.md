---
description: "Kriih is an NPC who can also be fought in Andor's Trail, found in Pub."
---

# ![](../assets/icons/monsters/monsters_rats_2.png){ .sprite } Kriih

**Where to find Kriih:** Pub: [ratdom_maze_412](../maps/ratdom_maze_412.md#pin-npc-ratdom_kriih)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rats_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Pub |
| **Class** | Animal |
| **HP** | 160 |
| **XP when defeated** | 198 |
| **Entry ID** | `ratdom_kriih` |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 160 |
| XP when defeated | 198 |
| Damage | 20 to 30 |
| Attack chance | 40 |
| Block chance | 20 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 3 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 200 to 500 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_412](../maps/ratdom_maze_412.md) | Pub | 1 | – |

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Kriih. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_kriih.json" data-npc="Kriih" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (18 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ratdom_kriih"></span>**`ratdom_kriih`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 398 of [Yellow is it](../quests/ratdom_quest.md#stage-398))* → [ratdom_kriih_202](#d-ratdom_kriih_202)
    - branch 2 *(if reached stage 399 of [Yellow is it](../quests/ratdom_quest.md#stage-399))* → [ratdom_kriih_200](#d-ratdom_kriih_200)
    - branch 3 → [ratdom_kriih_10](#d-ratdom_kriih_10)

    <span id="d-ratdom_kriih_202"></span>**`ratdom_kriih_202`** Kriih: “Hi $playername. I am not amused with what you have done.”

    - “What do you mean?” → [ratdom_kriih_204](#d-ratdom_kriih_204)

    <span id="d-ratdom_kriih_200"></span>**`ratdom_kriih_200`** Kriih: “Hi $playername. Well done.”

    - “What do you mean?” → [ratdom_kriih_210](#d-ratdom_kriih_210)

    <span id="d-ratdom_kriih_10"></span>**`ratdom_kriih_10`** Kriih: “Hi $playername. I am watching you.”


    <span id="d-ratdom_kriih_204"></span>**`ratdom_kriih_204`** Kriih: “You released Fraedro. You should have killed him or left him in custody.”

    - “I think Fraedro is absolutely innocent.” → [ratdom_kriih_206](#d-ratdom_kriih_206)

    <span id="d-ratdom_kriih_210"></span>**`ratdom_kriih_210`** Kriih: “Killing Fraedro. I loved to see that.”

    - “He earned it.” → [ratdom_kriih_220](#d-ratdom_kriih_220)

    <span id="d-ratdom_kriih_206"></span>**`ratdom_kriih_206`** Kriih: “My plan was that Fraedro should be sentenced to death.”

    - “Really - why?” → [ratdom_kriih_220](#d-ratdom_kriih_220)

    <span id="d-ratdom_kriih_220"></span>**`ratdom_kriih_220`** Kriih: “He deserved death, yes. But not because of the stupid skeleton of Rah.”

    - “Not? Now I'm confused.” → [ratdom_kriih_230](#d-ratdom_kriih_230)

    <span id="d-ratdom_kriih_230"></span>**`ratdom_kriih_230`** Kriih: “Of course not. As if Fraedro could. He's far too good a rat to do such a thing.”

    - Next → [ratdom_kriih_240](#d-ratdom_kriih_240)

    <span id="d-ratdom_kriih_240"></span>**`ratdom_kriih_240`** Kriih: “I took the skeleton myself and scattered the pieces so that no one would find them.”

    - Next → [ratdom_kriih_250](#d-ratdom_kriih_250)

    <span id="d-ratdom_kriih_250"></span>**`ratdom_kriih_250`** Kriih: “And then I blamed it on my cousin Fraedro.”

    - “How mean!” → [ratdom_kriih_260](#d-ratdom_kriih_260)

    <span id="d-ratdom_kriih_260"></span>**`ratdom_kriih_260`** Kriih: “Hahaha! You are funny!”

    - “Why did you do that? He's your cousin.” → [ratdom_kriih_270](#d-ratdom_kriih_270)

    <span id="d-ratdom_kriih_270"></span>**`ratdom_kriih_270`** Kriih: “Yes, yes. But he got in my way.”

    - Next → [ratdom_kriih_280](#d-ratdom_kriih_280)

    <span id="d-ratdom_kriih_280"></span>**`ratdom_kriih_280`** Kriih: “I caught him and presented him to Wart. He believed my story and put him under arrest.”

    - “And then I killed him.” *(if reached stage 399 of [Yellow is it](../quests/ratdom_quest.md#stage-399))* → [ratdom_kriih_290](#d-ratdom_kriih_290)
    - “And then I have set him free.” *(if reached stage 398 of [Yellow is it](../quests/ratdom_quest.md#stage-398))* → [ratdom_kriih_300](#d-ratdom_kriih_300)

    <span id="d-ratdom_kriih_290"></span>**`ratdom_kriih_290`** Kriih: “That was even better than I had planned. I have to thank you. Here, take some coins for the dirty work.”

    - “I don't want your bloody gold.” → [ratdom_kriih_292](#d-ratdom_kriih_292)
    - “It had better be many coins.” → [ratdom_kriih_294](#d-ratdom_kriih_294)

    <span id="d-ratdom_kriih_300"></span>**`ratdom_kriih_300`** Kriih: “Yes, you have destroyed my beautiful plan. You have to pay for that.”

    - “We'll see who pays here.” → *fight starts*
    - “I have to run.” → *conversation ends*

    <span id="d-ratdom_kriih_292"></span>**`ratdom_kriih_292`** Kriih: “Oh how cute. This two-leg has a guilty conscience. It just keeps getting better!”

    - “I should leave before I forget myself.” → *conversation ends*
    - “Now you pay for it - attack!” → *fight starts*

    <span id="d-ratdom_kriih_294"></span>**`ratdom_kriih_294`** Kriih: “10 pieces of gold is not enough? Oh, you draw your weapon? I think I'd better be gone ...” — **effects:** removes monsters from ratdom_maze_412, gives 10× [Gold coins](../items/gold.md)

    - “Wait, you coward!” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 18 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ratdom_kriih` |
    | Spawn group | `ratdom_kriih` |
    | Loot table | `ratdom_kriih` |
    | Conversation | `ratdom_kriih` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rats:2` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_kriih",
     "name": "Kriih",
     "iconID": "monsters_rats:2",
     "maxHP": 160,
     "maxAP": 10,
     "moveCost": 3,
     "unique": 1,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 20,
      "max": 30
     },
     "spawnGroup": "ratdom_kriih",
     "phraseID": "ratdom_kriih",
     "droplistID": "ratdom_kriih",
     "attackCost": 3,
     "attackChance": 40,
     "blockChance": 20
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_kriih.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_kriih.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_kriih.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_kriih.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
