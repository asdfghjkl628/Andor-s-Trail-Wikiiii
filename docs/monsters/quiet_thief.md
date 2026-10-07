---
description: "Pixtumn is an NPC who can also be fought in Andor's Trail, found in Brimhaven. Shopkeeper."
---

# ![](../assets/icons/monsters/monsters_rogue1_0.png){ .sprite } Pixtumn

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rogue1_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Role** | Shopkeeper |
| **Found in** | Brimhaven |
| **Class** | Humanoid |
| **HP** | 1 |
| **XP when defeated** | 1 |
| **Entries in game data** | 4 |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

!!! info "4 entries in the game data"
    The game data defines 4 separate characters named Pixtumn. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, loot or shop stock. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`quiet_thief`](#v-quiet_thief) | NPC | Brimhaven: [Brimhaven inn east](../maps/brimhaven_inn_east.md#pin-npc-quiet_thief) | shopkeeper | – |
| [`quiet_thief_1`](#v-quiet_thief_1) | Enemy | Brimhaven: [Brimhaven inn east](../maps/brimhaven_inn_east.md) | – | 1 |
| [`quiet_thief_2`](#v-quiet_thief_2) | Enemy | Brimhaven: [Brimhaven inn east](../maps/brimhaven_inn_east.md) | – | 1 |
| [`quiet_thief_3`](#v-quiet_thief_3) | Enemy | Brimhaven: [Brimhaven inn east](../maps/brimhaven_inn_east.md) | – | 1 |

## Brimhaven, Brimhaven inn east (quiet_thief) { #v-quiet_thief }

**Entry ID:** `quiet_thief` · **Type:** NPC · **Role:** Shopkeeper

**Location:** Brimhaven: [Brimhaven inn east](../maps/brimhaven_inn_east.md#pin-npc-quiet_thief)

### Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Necklace of dexterity](../items/necklace_dexterity.md) | 100% | 1 |
| [Defender's ring](../items/ring_defender.md) | 100% | 1 |
| [Leather gloves of attack](../items/gloves_leather_attack.md) | 100% | 1 |
| [Curved dagger](../items/daggr_curv.md) | 100% | 1 |
| [Ring of surehit](../items/ring_atkch1.md) | 100% | 1 |
| [Fine leather cap](../items/hat_fine_leather.md) | 100% | 1 |
| [Fancy green hat](../items/hat_fancy_green.md) | 100% | 1 |

### Quests

- [A strange looking dagger](../quests/brv_dagger.md): stages 30, 40
- [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md): stages 30, 40

### Dialogue simulator

Set your quest stages and items, then talk to Pixtumn. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/quiet_thief_0.json" data-npc="Pixtumn" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (14 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-quiet_thief-quiet_thief_0"></span>**`quiet_thief_0`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 10 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-10); NOT reached stage 20 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-20); NOT reached stage 30 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-30); NOT reached stage 40 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-40))* → [quiet_thief_1_0](#d-quiet_thief-quiet_thief_1_0)
    - branch 2 *(if reached stage 10 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-10); NOT reached stage 20 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-20); NOT reached stage 30 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-30); NOT reached stage 30 of [A strange looking dagger](../quests/brv_dagger.md#stage-30))* → [quiet_thief_2_0](#d-quiet_thief-quiet_thief_2_0)
    - branch 3 *(if NOT reached stage 30 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-30); reached stage 30 of [A strange looking dagger](../quests/brv_dagger.md#stage-30); reached stage 10 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-10); NOT reached stage 20 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-20))* → [quiet_thief_2_2](#d-quiet_thief-quiet_thief_2_2)
    - branch 4 *(if reached stage 20 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-20); NOT reached stage 10 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-10); NOT reached stage 40 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-40); NOT reached stage 40 of [A strange looking dagger](../quests/brv_dagger.md#stage-40))* → [quiet_thief_3_0](#d-quiet_thief-quiet_thief_3_0)
    - branch 5 *(if NOT reached stage 40 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-40); reached stage 40 of [A strange looking dagger](../quests/brv_dagger.md#stage-40); reached stage 20 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-20); NOT reached stage 10 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-10))* → [quiet_thief_3_2](#d-quiet_thief-quiet_thief_3_2)
    - branch 6 → [quiet_thief_0_0](#d-quiet_thief-quiet_thief_0_0)

    <span id="d-quiet_thief-quiet_thief_1_0"></span>**`quiet_thief_1_0`** [Pixtumn](../monsters/quiet_thief.md#v-quiet_thief_1): “Psst! Hey kid, you want to buy some nice stuff?”

    - “Maybe. Show me what you have.” → [quiet_thief_1_1](#d-quiet_thief-quiet_thief_1_1)
    - “No thanks. I think maybe you don't actually own what you are selling.” → *conversation ends*
    - “Not right now.” → *conversation ends*

    <span id="d-quiet_thief-quiet_thief_2_0"></span>**`quiet_thief_2_0`** [Pixtumn](../monsters/quiet_thief.md#v-quiet_thief_2): “Hello again kid. Want another look at what I have to sell?”

    - “Was the gem I purchased originally mounted in the pommel of the dagger you have?” *(if reached stage 20 of [A strange looking dagger](../quests/brv_dagger.md#stage-20))* → [quiet_thief_2_1](#d-quiet_thief-quiet_thief_2_1)
    - “Yes, I would like to take another look.” → *shop opens*

    <span id="d-quiet_thief-quiet_thief_2_2"></span>**`quiet_thief_2_2`** [Pixtumn](../monsters/quiet_thief.md): “Since you have the gem, and you have asked about the dagger, I assume you want it. But when you want something enough, you are willing to pay more, right?”

    - “No, I don't think so.” → *conversation ends*
    - “How much are you asking?” → [quiet_thief_2_3](#d-quiet_thief-quiet_thief_2_3)
    - “Can I see what else you have to sell.” → *shop opens*

    <span id="d-quiet_thief-quiet_thief_3_0"></span>**`quiet_thief_3_0`** [Pixtumn](../monsters/quiet_thief.md#v-quiet_thief_3): “Hello again kid. Want another look at what I have to sell?”

    - “Was the gem you have originally in the pommel of the dagger I purchased?” *(if reached stage 10 of [A strange looking dagger](../quests/brv_dagger.md#stage-10))* → [quiet_thief_3_1](#d-quiet_thief-quiet_thief_3_1)
    - “Yes, I would like to take another look.” → *shop opens*

    <span id="d-quiet_thief-quiet_thief_3_2"></span>**`quiet_thief_3_2`** [Pixtumn](../monsters/quiet_thief.md): “Since you have the dagger, and you have asked about the gem, I assume you want it. But when you want something enough, you are willing to pay more, right?”

    - “No, I don't think so.” → *conversation ends*
    - “How much are you asking?” → [quiet_thief_3_3](#d-quiet_thief-quiet_thief_3_3)
    - “Can I see what else you have to sell.” → *shop opens*

    <span id="d-quiet_thief-quiet_thief_0_0"></span>**`quiet_thief_0_0`** Pixtumn: “Hello again kid. Want another look at what I have to sell?”

    - “Yes. Show me what you have.” → *shop opens*
    - “Not right now.” → *conversation ends*

    <span id="d-quiet_thief-quiet_thief_1_1"></span>**`quiet_thief_1_1`** [Pixtumn](../monsters/quiet_thief.md#v-quiet_thief_1): “Keep your voice down! We don't want to attract any attention!”

    - “OK. Don't worry. I can keep a secret.” → *shop opens*
    - “It sounds like you want to do something illegal. I don't want trouble.” → *conversation ends*

    <span id="d-quiet_thief-quiet_thief_2_1"></span>**`quiet_thief_2_1`** [Pixtumn](../monsters/quiet_thief.md): “Maybe. Why? Anyway, the dagger is no longer available, except perhaps at a special price.” — **effects:** sets stage 30 of [A strange looking dagger](../quests/brv_dagger.md#stage-30)

    - Next → [quiet_thief_2_2](#d-quiet_thief-quiet_thief_2_2)

    <span id="d-quiet_thief-quiet_thief_2_3"></span>**`quiet_thief_2_3`** Pixtumn: “I think 1,000 gold would be fair. Is that acceptable?”

    - “No. That's too much for me.” → *conversation ends*
    - “I don't think it's fair, but I'll pay it.” *(if pay 1,000 gold)* → [quiet_thief_2_4](#d-quiet_thief-quiet_thief_2_4)

    <span id="d-quiet_thief-quiet_thief_3_1"></span>**`quiet_thief_3_1`** [Pixtumn](../monsters/quiet_thief.md): “Maybe. Why? Anyway, the gem is no longer available, except perhaps at a special price.” — **effects:** sets stage 40 of [A strange looking dagger](../quests/brv_dagger.md#stage-40)

    - Next → [quiet_thief_3_2](#d-quiet_thief-quiet_thief_3_2)

    <span id="d-quiet_thief-quiet_thief_3_3"></span>**`quiet_thief_3_3`** Pixtumn: “I think 1,500 gold would be fair. Is that acceptable?”

    - “No, that's too much for me.” → *conversation ends*
    - “I don't think it's fair, but I'll pay it.” *(if pay 1,500 gold)* → [quiet_thief_3_4](#d-quiet_thief-quiet_thief_3_4)

    <span id="d-quiet_thief-quiet_thief_2_4"></span>**`quiet_thief_2_4`** Pixtumn: “Here you go kid.” — **effects:** sets stage 30 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-30), gives 1× [A strange looking dagger](../items/strange_dagger.md)


    <span id="d-quiet_thief-quiet_thief_3_4"></span>**`quiet_thief_3_4`** Pixtumn: “Here you go kid” — **effects:** sets stage 40 of [Brimhaven dagger story flags (hidden flag)](../quests/brv_dagger_nondisplay.md#stage-40), gives 1× [A strange-looking gem](../items/strange_gem.md)




### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added<br>Dialogue: 14 lines added |
| [v0.7.12](../versions/0.7.12.md) | Renamed “Shady thief” → “Pixtumn”<br>Dialogue: 2 lines changed<br>· text: “I think 1500gp would be fair. Is that acceptable?” → “I think 1500 gold would be fair. Is that acceptable?”<br>· text: “I think 1000gp would be fair. Is that acceptable?” → “I think 1000 gold would be fair. Is that acceptable?” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 2 lines changed<br>· text: “I think 1500 gold would be fair. Is that acceptable?” → “I think {1500} gold would be fair. Is that acceptable?”<br>· text: “I think 1000 gold would be fair. Is that acceptable?” → “I think {1000} gold would be fair. Is that acceptable?” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (quiet_thief)"

    | | |
    |---|---|
    | Entry ID | `quiet_thief` |
    | Spawn group | `quiet_thief` |
    | Loot table | `quiet_thief` |
    | Conversation | `quiet_thief_0` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rogue1:0` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "quiet_thief",
     "name": "Pixtumn",
     "iconID": "monsters_rogue1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "quiet_thief_0",
     "droplistID": "quiet_thief"
    }
    ```


## Brimhaven, Brimhaven inn east (quiet_thief_1) { #v-quiet_thief_1 }

**Entry ID:** `quiet_thief_1` · **Type:** Enemy

**Location:** Brimhaven: [Brimhaven inn east](../maps/brimhaven_inn_east.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [A strange looking dagger](../items/strange_dagger.md) | 100% | 1 |
| [A strange-looking gem](../items/strange_gem.md) | 100% | 1 |
| [Necklace of dexterity](../items/necklace_dexterity.md) | 100% | 1 |
| [Defender's ring](../items/ring_defender.md) | 100% | 1 |
| [Leather gloves of attack](../items/gloves_leather_attack.md) | 100% | 1 |
| [Curved dagger](../items/daggr_curv.md) | 100% | 1 |
| [Ring of surehit](../items/ring_atkch1.md) | 100% | 1 |
| [Fine leather cap](../items/hat_fine_leather.md) | 100% | 1 |
| [Fancy green hat](../items/hat_fancy_green.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brimhaven inn east](../maps/brimhaven_inn_east.md) | Brimhaven | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |
| [v0.7.12](../versions/0.7.12.md) | Loot table changed<br>Renamed “Shady thief” → “Pixtumn” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (quiet_thief_1)"

    | | |
    |---|---|
    | Entry ID | `quiet_thief_1` |
    | Spawn group | `quiet_thief_1` |
    | Loot table | `quiet_thief_1` |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rogue1:0` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "quiet_thief_1",
     "name": "Pixtumn",
     "iconID": "monsters_rogue1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "droplistID": "quiet_thief_1"
    }
    ```


## Brimhaven, Brimhaven inn east (quiet_thief_2) { #v-quiet_thief_2 }

**Entry ID:** `quiet_thief_2` · **Type:** Enemy

**Location:** Brimhaven: [Brimhaven inn east](../maps/brimhaven_inn_east.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [A strange looking dagger](../items/strange_dagger.md) | 100% | 1 |
| [Necklace of dexterity](../items/necklace_dexterity.md) | 100% | 1 |
| [Defender's ring](../items/ring_defender.md) | 100% | 1 |
| [Leather gloves of attack](../items/gloves_leather_attack.md) | 100% | 1 |
| [Curved dagger](../items/daggr_curv.md) | 100% | 1 |
| [Ring of surehit](../items/ring_atkch1.md) | 100% | 1 |
| [Fine leather cap](../items/hat_fine_leather.md) | 100% | 1 |
| [Fancy green hat](../items/hat_fancy_green.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brimhaven inn east](../maps/brimhaven_inn_east.md) | Brimhaven | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |
| [v0.7.12](../versions/0.7.12.md) | Renamed “Shady thief” → “Pixtumn” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (quiet_thief_2)"

    | | |
    |---|---|
    | Entry ID | `quiet_thief_2` |
    | Spawn group | `quiet_thief_2` |
    | Loot table | `quiet_thief_2` |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rogue1:0` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "quiet_thief_2",
     "name": "Pixtumn",
     "iconID": "monsters_rogue1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "droplistID": "quiet_thief_2"
    }
    ```


## Brimhaven, Brimhaven inn east (quiet_thief_3) { #v-quiet_thief_3 }

**Entry ID:** `quiet_thief_3` · **Type:** Enemy

**Location:** Brimhaven: [Brimhaven inn east](../maps/brimhaven_inn_east.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 1 |
| XP when defeated | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [A strange-looking gem](../items/strange_gem.md) | 100% | 1 |
| [Necklace of dexterity](../items/necklace_dexterity.md) | 100% | 1 |
| [Defender's ring](../items/ring_defender.md) | 100% | 1 |
| [Leather gloves of attack](../items/gloves_leather_attack.md) | 100% | 1 |
| [Curved dagger](../items/daggr_curv.md) | 100% | 1 |
| [Ring of surehit](../items/ring_atkch1.md) | 100% | 1 |
| [Fine leather cap](../items/hat_fine_leather.md) | 100% | 1 |
| [Fancy green hat](../items/hat_fancy_green.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brimhaven inn east](../maps/brimhaven_inn_east.md) | Brimhaven | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |
| [v0.7.12](../versions/0.7.12.md) | Renamed “Shady thief” → “Pixtumn” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (quiet_thief_3)"

    | | |
    |---|---|
    | Entry ID | `quiet_thief_3` |
    | Spawn group | `quiet_thief_3` |
    | Loot table | `quiet_thief_3` |
    | Conversation | – |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rogue1:0` |
    | Defined in | `res/raw/monsterlist_brimhaven.json` |

    Raw data:

    ```json
    {
     "id": "quiet_thief_3",
     "name": "Pixtumn",
     "iconID": "monsters_rogue1:0",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "droplistID": "quiet_thief_3"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=quiet_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=quiet_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=quiet_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=quiet_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
