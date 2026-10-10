---
description: "Fraedro is an NPC you can also fight in Andor's Trail, found in Pub."
---

# ![](../assets/icons/monsters/monsters_rats_0.png){ .sprite } Fraedro

**Where to find Fraedro:** Pub: [Ratdom maze 626](../maps/ratdom_maze_626.md#pin-npc-ratdom_fraedro)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_rats_0.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Pub |
| **Introduced** | [v0.8.5](../versions/0.8.5.md) |

</div>

!!! warning "You can fight Fraedro"
    The conversation during [Yellow is it](../quests/ratdom_quest.md#stage-399) can lead straight into a fight with Fraedro.

No combat stats are defined for Fraedro, so the fight is over in one hit.

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 200 to 500 |
| [Fraedro's key](../items/ratdom_fraedro_key.md) | 100% | 1 |

## Quests

- [Yellow is it](../quests/ratdom_quest.md): stages 398, 399
- [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md): stage 180

## Dialogue simulator

Talk to Fraedro as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_fraedro.json" data-npc="Fraedro" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (15 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ratdom_fraedro"></span>**`ratdom_fraedro`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 180 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-180))* → [ratdom_fraedro_1](#d-ratdom_fraedro_1)
    - Next → [ratdom_fraedro_1s](#d-ratdom_fraedro_1s)

    <span id="d-ratdom_fraedro_1"></span>**`ratdom_fraedro_1`** [Fraedro](../monsters/ratdom_fraedro.md): “Please don't hurt me.”

    - “Who are you?” → [ratdom_fraedro_2](#d-ratdom_fraedro_2)
    - “Why did you steal King Rah's skeleton?” → [ratdom_fraedro_10](#d-ratdom_fraedro_10)
    - “OK, bye.” → *conversation ends*

    <span id="d-ratdom_fraedro_1s"></span>**`ratdom_fraedro_1s`** [Fraedro](../monsters/ratdom_fraedro.md): “Please don't hurt me. I am starving.”

    - “Who are you?” → [ratdom_fraedro_2](#d-ratdom_fraedro_2)
    - “Why did you steal King Rah's skeleton?” → [ratdom_fraedro_10](#d-ratdom_fraedro_10)
    - “Starving? I have some cheese for you here.” *(if NOT reached stage 180 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-180); hand over 1× [Cheese](../items/cheese.md))* → [ratdom_fraedro_cheese_1](#d-ratdom_fraedro_cheese_1)
    - “Starving? I have some good cheddar from Charwood for you here.” *(if NOT reached stage 180 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-180); NOT carry 1× [Cheese](../items/cheese.md); hand over 1× [Charwood cheddar](../items/charwood_cheddar.md))* → [ratdom_fraedro_cheese_1](#d-ratdom_fraedro_cheese_1)
    - “Starving? I have some moldy blue cheese for you here.” *(if NOT reached stage 180 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-180); NOT carry 1× [Cheese](../items/cheese.md); NOT carry 1× [Charwood cheddar](../items/charwood_cheddar.md); hand over 1× [Blue cheese](../items/cheese_blue.md))* → [ratdom_fraedro_cheese_1](#d-ratdom_fraedro_cheese_1)
    - “Starving? I have some goat cheese for you here. It smells only slightly.” *(if NOT reached stage 180 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-180); NOT carry 1× [Cheese](../items/cheese.md); NOT carry 1× [Charwood cheddar](../items/charwood_cheddar.md); NOT carry 1× [Blue cheese](../items/cheese_blue.md); hand over 1× [Goat cheese](../items/cheese_goat.md))* → [ratdom_fraedro_cheese_1](#d-ratdom_fraedro_cheese_1)
    - “Starving? Sorry, I have no cheese for you.” *(if NOT reached stage 180 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-180); NOT carry 1× [Cheese](../items/cheese.md); NOT carry 1× [Charwood cheddar](../items/charwood_cheddar.md); NOT carry 1× [Blue cheese](../items/cheese_blue.md); NOT carry 1× [Goat cheese](../items/cheese_goat.md))* → [ratdom_fraedro](#d-ratdom_fraedro)
    - “OK, bye.” → *conversation ends*

    <span id="d-ratdom_fraedro_2"></span>**`ratdom_fraedro_2`** Fraedro: “Fraedro, good traveler. Please don't hurt me.”

    - “Ah, that's why you're so heavily guarded.” → [ratdom_fraedro_4](#d-ratdom_fraedro_4)

    <span id="d-ratdom_fraedro_10"></span>**`ratdom_fraedro_10`** Fraedro: “It was not me! It was not me!”

    - “Finally confess!” → [ratdom_fraedro_10](#d-ratdom_fraedro_10)
    - “I believe you. Go now, while you can.” → [ratdom_fraedro_20](#d-ratdom_fraedro_20)
    - “I am going to kill you for your deeds now.” → [ratdom_fraedro_12](#d-ratdom_fraedro_12)
    - “I give up.” → *conversation ends*

    <span id="d-ratdom_fraedro_cheese_1"></span>**`ratdom_fraedro_cheese_1`** Fraedro: “Oh, my pleading has been heard. Thanks!”

    - Next → [ratdom_fraedro_cheese_10](#d-ratdom_fraedro_cheese_10)

    <span id="d-ratdom_fraedro_4"></span>**`ratdom_fraedro_4`** Fraedro: “I don't know why I'm being held here. I haven't done anything wrong.”

    - “Yeah, everyone says that.” → [ratdom_fraedro](#d-ratdom_fraedro)
    - “I believe you. Go now, while you can.” → [ratdom_fraedro_20](#d-ratdom_fraedro_20)

    <span id="d-ratdom_fraedro_20"></span>**`ratdom_fraedro_20`** Fraedro: “What? Thank you, thank you! [Fraedro turns to flee, losing a small golden key in the process]” — **effects:** sets stage 398 of [Yellow is it](../quests/ratdom_quest.md#stage-398), gives 1× [Fraedro's key](../items/ratdom_fraedro_key.md), removes monsters from ratdom_maze_626

    - “You better get out of the area quick.” → *NPC leaves*

    <span id="d-ratdom_fraedro_12"></span>**`ratdom_fraedro_12`** Fraedro: “Please don't! It was not me!”

    - “Die now!” → [ratdom_fraedro_14](#d-ratdom_fraedro_14)
    - “Run and live with your guilty conscience.” → [ratdom_fraedro_20](#d-ratdom_fraedro_20)
    - “I give up.” → *conversation ends*

    <span id="d-ratdom_fraedro_cheese_10"></span>**`ratdom_fraedro_cheese_10`** Fraedro: “You must be the rightful heir of King Rah.”

    - “Who, me?” *(if reached stage 10 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-10))* → [ratdom_fraedro_cheese_12](#d-ratdom_fraedro_cheese_12)
    - “Sure.” → [ratdom_fraedro_cheese_20](#d-ratdom_fraedro_cheese_20)

    <span id="d-ratdom_fraedro_14"></span>**`ratdom_fraedro_14`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 399 of [Yellow is it](../quests/ratdom_quest.md#stage-399)

    - branch 1 → *fight starts*

    <span id="d-ratdom_fraedro_cheese_12"></span>**`ratdom_fraedro_cheese_12`** [Clevred](../monsters/ratdom_rat.md): “Of course I am.”

    - Next → [ratdom_fraedro_cheese_20](#d-ratdom_fraedro_cheese_20)

    <span id="d-ratdom_fraedro_cheese_20"></span>**`ratdom_fraedro_cheese_20`** [Fraedro](../monsters/ratdom_fraedro.md): “Then you shall get your sword back. I had only borrowed it and taken good care of it.”

    - “King Rah's sword?” → [ratdom_fraedro_cheese_30](#d-ratdom_fraedro_cheese_30)

    <span id="d-ratdom_fraedro_cheese_30"></span>**`ratdom_fraedro_cheese_30`** Fraedro: “You'll find it further down in the caves. Say the words 'Veni gladio fidelis'.” — **effects:** sets stage 180 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-180)

    - “I'll try to remember.” *(if reached stage 10 of [Ratdom story flags (hidden flag)](../quests/ratdom_nondisplay.md#stage-10))* → [ratdom_fraedro_cheese_32](#d-ratdom_fraedro_cheese_32)

    <span id="d-ratdom_fraedro_cheese_32"></span>**`ratdom_fraedro_cheese_32`** [Clevred](../monsters/ratdom_rat.md): “[Clevred rolls his eyes] He. will. try. to remember. That can only go wrong.”

    - Next → [ratdom_fraedro](#d-ratdom_fraedro)



## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 15 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “Fraedro, good sir. Please don't hurt me.” → “Fraedro, good traveler. Please don't hurt me.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

- `ratdom_fraedro`: no combat statistics are defined, so the game uses its defaults (1 HP, no attack) if a fight with this entry starts.

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ratdom_fraedro` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `ratdom_fraedro` |
    | Loot table | `ratdom_fraedro` |
    | Conversation | `ratdom_fraedro` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rats:0` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_fraedro",
     "name": "Fraedro",
     "iconID": "monsters_rats:0",
     "moveCost": 1,
     "unique": 1,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 20,
      "max": 30
     },
     "spawnGroup": "ratdom_fraedro",
     "phraseID": "ratdom_fraedro",
     "droplistID": "ratdom_fraedro"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_fraedro.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_fraedro.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_fraedro.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_fraedro.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
