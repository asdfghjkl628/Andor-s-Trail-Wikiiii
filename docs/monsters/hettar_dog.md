---
description: "Wolfhound is an NPC you can also fight in Andor's Trail, found in Blackwater Mountain."
---

# ![](../assets/icons/monsters/monsters_dogs_3.png){ .sprite } Wolfhound

**Where to find Wolfhound:** [Blackwater Mountain, Blackwater mountain 55](#v-hettar_dog), [Blackwater Mountain, Blackwater mountain 55](#v-hettar_dog2), [Blackwater Mountain, Blackwater mountain 55](#v-hettar_dog3)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_dogs_3.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Blackwater Mountain |
| **Class** | Animal |
| **HP** | 40 |
| **XP when defeated** | 117 |
| **Introduced** | [v0.7.12](../versions/0.7.12.md) |

</div>

## Blackwater Mountain, Blackwater mountain 55 { #v-hettar_dog }

**Where:** Blackwater Mountain: [Blackwater mountain 55](../maps/blackwater_mountain55.md#pin-npc-hettar_dog)

### Quests

- [Where is Norry?](../quests/hettar_dog.md): stages 40, 50
- [Hettar dog story flags (hidden flag)](../quests/hettar_dog_nd.md): stages 1, 2

### Dialogue simulator

Talk to Wolfhound as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/hettar_dog.json" data-npc="Wolfhound" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-hettar_dog-hettar_dog"></span>**`hettar_dog`** Wolfhound: “Growl!” — **effects:** sets stage 1 of [Hettar dog story flags (hidden flag)](../quests/hettar_dog_nd.md#stage-1)

    - “Hey Norry, look here! I have some much better food for you from Hettar.” *(if hand over 1× [Wyrm meat](../items/hettar_bone.md); reached stage 2 of [Hettar dog story flags (hidden flag)](../quests/hettar_dog_nd.md#stage-2))* → [hettar_dog_10](#d-hettar_dog-hettar_dog_10)
    - “Hey Norry, look here! I have a Wyrm steak for you from Hettar.” *(if carry 1× [Wyrm meat](../items/hettar_bone.md); NOT reached stage 2 of [Hettar dog story flags (hidden flag)](../quests/hettar_dog_nd.md#stage-2))* → [hettar_dog_50](#d-hettar_dog-hettar_dog_50)
    - “Now run to Hettar! He is waiting for you.” *(if reached stage 40 of [Where is Norry?](../quests/hettar_dog.md#stage-40))* → [hettar_dog_20](#d-hettar_dog-hettar_dog_20)
    - “OK, I go. Stupid dog.” → *conversation ends*

    <span id="d-hettar_dog-hettar_dog_10"></span>**`hettar_dog_10`** [Dummy NPC](../monsters/none.md): “The wolfhound fetched the meat from your hand and devoured it greedily in a few seconds.” — **effects:** sets stage 2 of [Hettar dog story flags (hidden flag)](../quests/hettar_dog_nd.md#stage-2), sets stage 40 of [Where is Norry?](../quests/hettar_dog.md#stage-40)

    - “There, there. And now run to Hettar! He is waiting for you.” → [hettar_dog_20](#d-hettar_dog-hettar_dog_20)

    <span id="d-hettar_dog-hettar_dog_50"></span>**`hettar_dog_50`** Wolfhound: “Grrrowl.”

    - “Ah, I see. These monstrous bones here on the ground are delicious too.” → *conversation ends*

    <span id="d-hettar_dog-hettar_dog_20"></span>**`hettar_dog_20`** [Dummy NPC](../monsters/none.md): “A moment later the huge wolfhound was gone.” — **effects:** removes monsters from blackwater_mountain55, spawns monsters on blackwater_mountain55, sets stage 50 of [Where is Norry?](../quests/hettar_dog.md#stage-50)




### Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Blackwater Mountain, Blackwater mountain 55 (2) { #v-hettar_dog2 }

**Where:** Blackwater Mountain: [Blackwater mountain 55](../maps/blackwater_mountain55.md#pin-npc-hettar_dog2)

### Dialogue simulator

Talk to Wolfhound as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/hettar_dog2.json" data-npc="Wolfhound" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-hettar_dog2-hettar_dog2"></span>**`hettar_dog2`** Wolfhound: “Growl!”




### Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Blackwater Mountain, Blackwater mountain 55 (3) { #v-hettar_dog3 }

**Where:** Blackwater Mountain: [Blackwater mountain 55](../maps/blackwater_mountain55.md)

### Combat

| | |
|---|---|
| Class | Animal |
| HP | 40 |
| XP when defeated | 117 |
| Damage | 1 to 8 |
| AC | 80 |
| BC | 150 |
| DR | 5 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 55](../maps/blackwater_mountain55.md) | Blackwater Mountain | 1 | Appears later, during a quest |

### Quests that count defeats

- [Where is Norry?](../quests/hettar_dog.md#stage-90) with [Little Hettar](../monsters/hettar.md) ([Blackwater mountain 55](../maps/blackwater_mountain55.md)) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**3 entries.** The game data defines 3 separate characters named Wolfhound. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, combat statistics, loot or shop stock.

| Entry | Type | Section |
|---|---|---|
| `hettar_dog` | NPC | [Blackwater Mountain, Blackwater mountain 55](#v-hettar_dog) |
| `hettar_dog2` | NPC | [Blackwater Mountain, Blackwater mountain 55](#v-hettar_dog2) |
| `hettar_dog3` | Enemy | [Blackwater Mountain, Blackwater mountain 55](#v-hettar_dog3) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: hettar_dog"

    | | |
    |---|---|
    | Entry ID | `hettar_dog` |
    | Type (wiki) | NPC |
    | Spawn group | `hettar_dog` |
    | Loot table | – |
    | Conversation | `hettar_dog` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_dogs:3` |
    | Defined in | `res/raw/monsterlist_brimhaven_2b.json` |

    Raw data:

    ```json
    {
     "id": "hettar_dog",
     "name": "Wolfhound",
     "iconID": "monsters_dogs:3",
     "monsterClass": "animal",
     "spawnGroup": "hettar_dog",
     "phraseID": "hettar_dog"
    }
    ```

??? info "Technical information: hettar_dog2"

    | | |
    |---|---|
    | Entry ID | `hettar_dog2` |
    | Type (wiki) | NPC |
    | Spawn group | `hettar_dog2` |
    | Loot table | – |
    | Conversation | `hettar_dog2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_dogs:3` |
    | Defined in | `res/raw/monsterlist_brimhaven_2b.json` |

    Raw data:

    ```json
    {
     "id": "hettar_dog2",
     "name": "Wolfhound",
     "iconID": "monsters_dogs:3",
     "monsterClass": "animal",
     "spawnGroup": "hettar_dog2",
     "phraseID": "hettar_dog2"
    }
    ```

??? info "Technical information: hettar_dog3"

    | | |
    |---|---|
    | Entry ID | `hettar_dog3` |
    | Type (wiki) | Enemy |
    | Spawn group | `hettar_dog3` |
    | Loot table | `hettar_dog3` |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_dogs:3` |
    | Defined in | `res/raw/monsterlist_brimhaven_2b.json` |

    Raw data:

    ```json
    {
     "id": "hettar_dog3",
     "name": "Wolfhound",
     "iconID": "monsters_dogs:3",
     "maxHP": 40,
     "unique": 1,
     "monsterClass": "animal",
     "attackDamage": {
      "min": 1,
      "max": 8
     },
     "spawnGroup": "hettar_dog3",
     "droplistID": "hettar_dog3",
     "attackCost": 4,
     "attackChance": 80,
     "blockChance": 150,
     "damageResistance": 5
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hettar_dog.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hettar_dog.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hettar_dog.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=hettar_dog.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
