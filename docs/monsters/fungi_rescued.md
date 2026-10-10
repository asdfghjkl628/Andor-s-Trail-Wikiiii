---
description: "Lediofa is a non-player character (NPC) in Andor's Trail, found in Mushroom m 3 2, Fallhaven."
---

# ![](../assets/icons/monsters/monsters_ld1_20.png){ .sprite } Lediofa

**Where to find Lediofa:** [Mushroom m 3 2](#v-fungi_rescued), [Fallhaven, Fallhaven potions](#v-fungi_rescued2)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_20.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Mushroom m 3 2, Fallhaven |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

## Mushroom m 3 2 { #v-fungi_rescued }

**Where:** [Mushroom m 3 2](../maps/mushroom_m3_2.md#pin-npc-fungi_rescued)

### Quests

- [Fungi panic](../quests/fungi_panic.md): stage 210

### Dialogue simulator

Talk to Lediofa as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/fungi_rescued.json" data-npc="Lediofa" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (12 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-fungi_rescued-fungi_rescued"></span>**`fungi_rescued`** Lediofa: “Thank you, thank you!”

    - “Who are you?” → [fungi_rescued_10](#d-fungi_rescued-fungi_rescued_10)

    <span id="d-fungi_rescued-fungi_rescued_10"></span>**`fungi_rescued_10`** Lediofa: “My name is Lediofa. I was travelling with my family to Vilegard. We wanted to visit my uncle.”

    - Next → [fungi_rescued_20](#d-fungi_rescued-fungi_rescued_20)

    <span id="d-fungi_rescued-fungi_rescued_20"></span>**`fungi_rescued_20`** Lediofa: “We were attacked by robbers in the forest. I don't know what happened to my family. It was terrible.”

    - “Poor child.” → [fungi_rescued_30](#d-fungi_rescued-fungi_rescued_30)

    <span id="d-fungi_rescued-fungi_rescued_30"></span>**`fungi_rescued_30`** Lediofa: “I was dragged into this cave.”

    - Next → [fungi_rescued_40](#d-fungi_rescued-fungi_rescued_40)

    <span id="d-fungi_rescued-fungi_rescued_40"></span>**`fungi_rescued_40`** Lediofa: “The only thing I saw was a figure clad in black who kept muttering mean sounding words.”

    - “That must have been Zuul'khan.” → [fungi_rescued_50](#d-fungi_rescued-fungi_rescued_50)

    <span id="d-fungi_rescued-fungi_rescued_50"></span>**`fungi_rescued_50`** Lediofa: “Yes, it was him. I hope you're not one of his friends? Please no!”

    - “Don't panic. I am $playername from Crossglen. Zuul'khan received his just punishment. He can't do anything to you…” → [fungi_rescued_60](#d-fungi_rescued-fungi_rescued_60)

    <span id="d-fungi_rescued-fungi_rescued_60"></span>**`fungi_rescued_60`** Lediofa: “Oh, how relieved I am to hear that! Thank you again!”

    - Next → [fungi_rescued_70](#d-fungi_rescued-fungi_rescued_70)

    <span id="d-fungi_rescued-fungi_rescued_70"></span>**`fungi_rescued_70`** Lediofa: “This black-clad man wanted to feed me to this awful big mushroom. He told me the mushroom still needed to grow much larger, and then it could help him invade the land.”

    - Next → [fungi_rescued_80](#d-fungi_rescued-fungi_rescued_80)

    <span id="d-fungi_rescued-fungi_rescued_80"></span>**`fungi_rescued_80`** Lediofa: “I'm glad this nightmare is over now. Thanks to you, $playername.”

    - “Oh, that was nothing.” → [fungi_rescued_90](#d-fungi_rescued-fungi_rescued_90)
    - “I do things like that every other day.” → [fungi_rescued_90](#d-fungi_rescued-fungi_rescued_90)
    - “It was a tough fight indeed.” → [fungi_rescued_90](#d-fungi_rescued-fungi_rescued_90)

    <span id="d-fungi_rescued-fungi_rescued_90"></span>**`fungi_rescued_90`** Lediofa: “I should go look for my parents - I'm sure they are very worried. Although...”

    - “What is it?” → [fungi_rescued_100](#d-fungi_rescued-fungi_rescued_100)

    <span id="d-fungi_rescued-fungi_rescued_100"></span>**`fungi_rescued_100`** Lediofa: “I feel a bit ill. Maybe I should rest a bit before I leave.”

    - “That might be the giant mushroom's poison. The potioner in Fallhaven knows the cure.” → [fungi_rescued_110](#d-fungi_rescued-fungi_rescued_110)

    <span id="d-fungi_rescued-fungi_rescued_110"></span>**`fungi_rescued_110`** Lediofa: “[Lediofa's eyes widen.] I've been poisoned...? Oh no! I'll seek the potioner right away. Thank you for telling me. I hope we meet again, $playername.” — **effects:** sets stage 210 of [Fungi panic](../quests/fungi_panic.md#stage-210), spawns monsters on fallhaven_potions

    - “Good luck!” → *NPC leaves*



### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 12 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Fallhaven, Fallhaven potions { #v-fungi_rescued2 }

**Where:** Fallhaven: [Fallhaven potions](../maps/fallhaven_potions.md#pin-npc-fungi_rescued2)

### Quests

- [Fungi panic](../quests/fungi_panic.md): stage 220

### Dialogue simulator

Talk to Lediofa as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/fungi_rescued2.json" data-npc="Lediofa" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (6 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-fungi_rescued2-fungi_rescued2"></span>**`fungi_rescued2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 220 of [Fungi panic](../quests/fungi_panic.md#stage-220))* → [fungi_rescued2_1](#d-fungi_rescued2-fungi_rescued2_1)
    - branch 2 *(if reached stage 220 of [Fungi panic](../quests/fungi_panic.md#stage-220))* → [fungi_rescued2_30](#d-fungi_rescued2-fungi_rescued2_30)

    <span id="d-fungi_rescued2-fungi_rescued2_1"></span>**`fungi_rescued2_1`** Lediofa: “Outrageous! I told you already, I don't have 150 gold!”

    - Next → [fungi_rescued2_10](#d-fungi_rescued2-fungi_rescued2_10)

    <span id="d-fungi_rescued2-fungi_rescued2_30"></span>**`fungi_rescued2_30`** Lediofa: “You've saved me again, $playername. You truly are a hero. If you ever find yourself in Nor City, I'm sure my family would love to meet you. Thank you!” — **effects:** sets stage 220 of [Fungi panic](../quests/fungi_panic.md#stage-220)

    - “Take care!” → *NPC leaves*

    <span id="d-fungi_rescued2-fungi_rescued2_10"></span>**`fungi_rescued2_10`** [Potion merchant](../monsters/potion_merchant.md): “I'm sorry that you're ill, girl, but I can't work for free. The price is 150 gold, no less.”

    - Next → [fungi_rescued2_20](#d-fungi_rescued2-fungi_rescued2_20)

    <span id="d-fungi_rescued2-fungi_rescued2_20"></span>**`fungi_rescued2_20`** [Lediofa](../monsters/fungi_rescued.md#v-fungi_rescued2): “You greedy swine...Oh! It's $playername! I came here to cure the mushroom poison, but that lousy merchant won't help me until he receives payment. And I have no gold...”

    - “That's no trouble. I can spare 150 gold to help.” *(if pay 150 gold)* → [fungi_rescued2_30](#d-fungi_rescued2-fungi_rescued2_30)
    - “I'm sorry to hear that, but I can't spare the gold to help you right now.” → *conversation ends*
    - “The potioner is right, you know. Nobody works for free.” → [fungi_rescued2_20_2](#d-fungi_rescued2-fungi_rescued2_20_2)

    <span id="d-fungi_rescued2-fungi_rescued2_20_2"></span>**`fungi_rescued2_20_2`** Lediofa: “But what can I do? I don't feel well...”




### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Lediofa. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location, combat statistics, movement.

| Entry | Type | Section |
|---|---|---|
| `fungi_rescued` | NPC | [Mushroom m 3 2](#v-fungi_rescued) |
| `fungi_rescued2` | NPC | [Fallhaven, Fallhaven potions](#v-fungi_rescued2) |

??? info "Technical information: fungi_rescued"

    | | |
    |---|---|
    | Entry ID | `fungi_rescued` |
    | Type (wiki) | NPC |
    | Spawn group | `fungi_rescued` |
    | Loot table | – |
    | Conversation | `fungi_rescued` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:20` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "fungi_rescued",
     "name": "Lediofa",
     "iconID": "monsters_ld1:20",
     "maxAP": 10,
     "moveCost": 2,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "spawnGroup": "fungi_rescued",
     "phraseID": "fungi_rescued"
    }
    ```

??? info "Technical information: fungi_rescued2"

    | | |
    |---|---|
    | Entry ID | `fungi_rescued2` |
    | Type (wiki) | NPC |
    | Spawn group | `fungi_rescued2` |
    | Loot table | – |
    | Conversation | `fungi_rescued2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:20` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "fungi_rescued2",
     "name": "Lediofa",
     "iconID": "monsters_ld1:20",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "fungi_rescued2",
     "phraseID": "fungi_rescued2"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fungi_rescued.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fungi_rescued.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fungi_rescued.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fungi_rescued.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
