---
description: "Wolfhound is an NPC who can also be fought in Andor's Trail, found in Blackwater Mountain."
---

# ![](../assets/icons/monsters/monsters_dogs_3.png){ .sprite } Wolfhound

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_dogs_3.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Blackwater Mountain |
| **Class** | Animal |
| **HP** | 40 |
| **XP when defeated** | 117 |
| **Entries in game data** | 3 |
| **Introduced** | [v0.7.12](../versions/0.7.12.md) |

</div>

!!! info "3 entries in the game data"
    The game's data files define 3 separate characters named Wolfhound. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, combat statistics, loot or shop stock. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`hettar_dog`](#v-hettar_dog) | NPC | Blackwater Mountain: [blackwater_mountain55](../maps/blackwater_mountain55.md#pin-npc-hettar_dog) | – | – |
| [`hettar_dog2`](#v-hettar_dog2) | NPC | Blackwater Mountain: [blackwater_mountain55](../maps/blackwater_mountain55.md#pin-npc-hettar_dog2) | – | – |
| [`hettar_dog3`](#v-hettar_dog3) | Enemy | Blackwater Mountain: [blackwater_mountain55](../maps/blackwater_mountain55.md) | – | 40 |

## Blackwater Mountain, Blackwater mountain55 (hettar_dog) { #v-hettar_dog }

**Entry ID:** `hettar_dog` · **Type:** NPC

**Location:** Blackwater Mountain: [blackwater_mountain55](../maps/blackwater_mountain55.md#pin-npc-hettar_dog)

### Quests

- [Where is Norry?](../quests/hettar_dog.md): stages 40, 50
- [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md): stages 1, 2

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Wolfhound. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/hettar_dog.json" data-npc="Wolfhound" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-hettar_dog-hettar_dog"></span>**`hettar_dog`** Wolfhound: “Growl!” — **effects:** sets stage 1 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-1)

    - “Hey Norry, look here! I have some much better food for you from Hettar.” *(if hand over 1× [Wyrm meat](../items/hettar_bone.md); reached stage 2 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-2))* → [hettar_dog_10](#d-hettar_dog-hettar_dog_10)
    - “Hey Norry, look here! I have a Wyrm steak for you from Hettar.” *(if carry 1× [Wyrm meat](../items/hettar_bone.md); NOT reached stage 2 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-2))* → [hettar_dog_50](#d-hettar_dog-hettar_dog_50)
    - “Now run to Hettar! He is waiting for you.” *(if reached stage 40 of [Where is Norry?](../quests/hettar_dog.md#stage-40))* → [hettar_dog_20](#d-hettar_dog-hettar_dog_20)
    - “OK, I go. Stupid dog.” → *conversation ends*

    <span id="d-hettar_dog-hettar_dog_10"></span>**`hettar_dog_10`** [Dummy NPC](../monsters/none.md): “The wolfhound fetched the meat from your hand and devoured it greedily in a few seconds.” — **effects:** sets stage 2 of [hettar_dog_nd (hidden flag)](../quests/hettar_dog_nd.md#stage-2), sets stage 40 of [Where is Norry?](../quests/hettar_dog.md#stage-40)

    - “There, there. And now run to Hettar! He is waiting for you.” → [hettar_dog_20](#d-hettar_dog-hettar_dog_20)

    <span id="d-hettar_dog-hettar_dog_50"></span>**`hettar_dog_50`** Wolfhound: “Grrrowl.”

    - “Ah, I see. These monstrous bones here on the ground are delicious too.” → *conversation ends*

    <span id="d-hettar_dog-hettar_dog_20"></span>**`hettar_dog_20`** [Dummy NPC](../monsters/none.md): “A moment later the huge wolfhound was gone.” — **effects:** removes monsters from blackwater_mountain55, spawns monsters on blackwater_mountain55, sets stage 50 of [Where is Norry?](../quests/hettar_dog.md#stage-50)




### Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (hettar_dog)"

    | | |
    |---|---|
    | Entry ID | `hettar_dog` |
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


## Blackwater Mountain, Blackwater mountain55 (hettar_dog2) { #v-hettar_dog2 }

**Entry ID:** `hettar_dog2` · **Type:** NPC

**Location:** Blackwater Mountain: [blackwater_mountain55](../maps/blackwater_mountain55.md#pin-npc-hettar_dog2)

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Wolfhound. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/hettar_dog2.json" data-npc="Wolfhound" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-hettar_dog2-hettar_dog2"></span>**`hettar_dog2`** Wolfhound: “Growl!”




### Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (hettar_dog2)"

    | | |
    |---|---|
    | Entry ID | `hettar_dog2` |
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


## Blackwater Mountain, Blackwater mountain55 (hettar_dog3) { #v-hettar_dog3 }

**Entry ID:** `hettar_dog3` · **Type:** Enemy

**Location:** Blackwater Mountain: [blackwater_mountain55](../maps/blackwater_mountain55.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Animal |
| HP | 40 |
| XP when defeated | 117 |
| Damage | 1 to 8 |
| Attack chance | 80 |
| Block chance | 150 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 4 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Meat](../items/meat.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [blackwater_mountain55](../maps/blackwater_mountain55.md) | Blackwater Mountain | 1 | Appears later, during a quest |

### Quests that count defeats

- [Where is Norry?](../quests/hettar_dog.md#stage-90) with [Little Hettar](../monsters/hettar.md) ([blackwater_mountain55](../maps/blackwater_mountain55.md)) checks that this enemy has been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (hettar_dog3)"

    | | |
    |---|---|
    | Entry ID | `hettar_dog3` |
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



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


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
