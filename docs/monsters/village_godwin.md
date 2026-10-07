---
description: "Godwin is an NPC who can also be fought in Andor's Trail, found in Wexlow Village, gamjee_well_jail_cells."
---

# ![](../assets/icons/monsters/monsters_ld1_134.png){ .sprite } Godwin

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_134.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Wexlow Village, gamjee_well_jail_cells |
| **Class** | Humanoid |
| **HP** | 1 |
| **XP when defeated** | 1 |
| **Entries in game data** | 2 |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Godwin. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, movement. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`village_godwin`](#v-village_godwin) | NPC | Wexlow Village: [wexlow_village](../maps/wexlow_village.md#pin-npc-village_godwin) | – | – |
| [`troll_hollow_godwin`](#v-troll_hollow_godwin) | Enemy | [gamjee_well_jail_cells](../maps/gamjee_well_jail_cells.md) | – | 1 |

## Wexlow Village, Wexlow village (village_godwin) { #v-village_godwin }

**Entry ID:** `village_godwin` · **Type:** NPC

**Location:** Wexlow Village: [wexlow_village](../maps/wexlow_village.md#pin-npc-village_godwin)

### Quests

- [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md): stages 7, 13, 14, 15

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Godwin. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/village_godwin_selector.json" data-npc="Godwin" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (12 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-village_godwin-village_godwin_selector"></span>**`village_godwin_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7))* → [village_godwin_lost_ring_1](#d-village_godwin-village_godwin_lost_ring_1)
    - Next *(if reached stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7))* → [village_godwin_has_ring](#d-village_godwin-village_godwin_has_ring)

    <span id="d-village_godwin-village_godwin_lost_ring_1"></span>**`village_godwin_lost_ring_1`** Godwin: “Have you by any chance seen my wedding ring? Oh my, Godelieve is going to kill me when she sees it's missing.”

    - “What does it look like?” → [village_godwin_lost_ring_2](#d-village_godwin-village_godwin_lost_ring_2)

    <span id="d-village_godwin-village_godwin_has_ring"></span>**`village_godwin_has_ring`** Godwin: “A crisis has been averted thanks to you.”

    - “You should do a better job protecting that ring.” → *conversation ends*

    <span id="d-village_godwin-village_godwin_lost_ring_2"></span>**`village_godwin_lost_ring_2`** Godwin: “Um, let me think. Oh, yeah, I remember. It's black, gold and covered in emeralds.”

    - “"Oh, yeah, I remember"? What? Don't you know what it looks like?” → [village_godwin_lost_ring_3](#d-village_godwin-village_godwin_lost_ring_3)
    - “Actually, this is your lucky day. I have it here.” *(if carry 1× [Godwin's ring](../items/godwin_ring.md))* → [village_godwin_lost_ring_4](#d-village_godwin-village_godwin_lost_ring_4)

    <span id="d-village_godwin-village_godwin_lost_ring_3"></span>**`village_godwin_lost_ring_3`** Godwin: “Leave me alone. I don't need you questioning me under this stressful situation.”


    <span id="d-village_godwin-village_godwin_lost_ring_4"></span>**`village_godwin_lost_ring_4`** Godwin: “Your messing with me, right? Give it to me, please.”

    - “Sure. Here, it's yours.” *(if hand over 1× [Godwin's ring](../items/godwin_ring.md))* → [village_godwin_lost_ring_give_ring_free](#d-village_godwin-village_godwin_lost_ring_give_ring_free)
    - “What do you want to give me in exchange for your wife not "killing you"?” → [village_godwin_lost_ring_5](#d-village_godwin-village_godwin_lost_ring_5)

    <span id="d-village_godwin-village_godwin_lost_ring_give_ring_free"></span>**`village_godwin_lost_ring_give_ring_free`** Godwin: “Thank you so much! I really appreciate you just giving it to me. Here are a few coins for your trouble.” — **effects:** sets stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7), gives 100× [Gold coins](../items/gold.md), sets stage 13 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-13)


    <span id="d-village_godwin-village_godwin_lost_ring_5"></span>**`village_godwin_lost_ring_5`** Godwin: “Give you? How about 2,000 gold coins?”

    - “Sounds good.” *(if hand over 1× [Godwin's ring](../items/godwin_ring.md))* → [village_godwin_lost_ring_take_ring](#d-village_godwin-village_godwin_lost_ring_take_ring)
    - “Hey Godelieve, did you hear what happened to Godwin?” → [village_godwin_lost_ring_godelieve](#d-village_godwin-village_godwin_lost_ring_godelieve)

    <span id="d-village_godwin-village_godwin_lost_ring_take_ring"></span>**`village_godwin_lost_ring_take_ring`** Godwin: “Thank you so much! Here take these coins.” — **effects:** gives 2000× [Gold coins](../items/gold.md), sets stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7), sets stage 14 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-14)


    <span id="d-village_godwin-village_godwin_lost_ring_godelieve"></span>**`village_godwin_lost_ring_godelieve`** [Godelieve](../monsters/village_godelieve.md#v-village_godelieve_hidden): “No. What happened?”

    - “Well, he los...” → [village_godwin_lost_ring_godelieve_2](#d-village_godwin-village_godwin_lost_ring_godelieve_2)

    <span id="d-village_godwin-village_godwin_lost_ring_godelieve_2"></span>**`village_godwin_lost_ring_godelieve_2`** [Godwin](../monsters/village_godwin.md): “NEVER MIND! Godelieve, this kid is being silly. You can go back to whatever it is that you were doing.”

    - “3,000 gold or no ring.” *(if hand over 1× [Godwin's ring](../items/godwin_ring.md))* → [village_godwin_lost_ring_3k](#d-village_godwin-village_godwin_lost_ring_3k)

    <span id="d-village_godwin-village_godwin_lost_ring_3k"></span>**`village_godwin_lost_ring_3k`** Godwin: “Fine! Take the coins you thief.” — **effects:** gives 3000× [Gold coins](../items/gold.md), sets stage 7 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-7), sets stage 15 of [feygard_nondisplayed (hidden flag)](../quests/feygard_nondisplayed.md#stage-15)

    - “I will put them to good use.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 12 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 2 lines changed<br>· text: “Give you? How about 2000 gold coins?” → “Give you? How about {2000} gold coins?” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (village_godwin)"

    | | |
    |---|---|
    | Entry ID | `village_godwin` |
    | Spawn group | `village_godwin` |
    | Loot table | – |
    | Conversation | `village_godwin_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:134` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "village_godwin",
     "name": "Godwin",
     "iconID": "monsters_ld1:134",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "village_godwin_selector"
    }
    ```


## Gamjee well jail cells (troll_hollow_godwin) { #v-troll_hollow_godwin }

**Entry ID:** `troll_hollow_godwin` · **Type:** Enemy

**Location:** [gamjee_well_jail_cells](../maps/gamjee_well_jail_cells.md)

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

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [gamjee_well_jail_cells](../maps/gamjee_well_jail_cells.md) | – | 1 | – |


### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (troll_hollow_godwin)"

    | | |
    |---|---|
    | Entry ID | `troll_hollow_godwin` |
    | Spawn group | `troll_hollow_godwin` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:134` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "troll_hollow_godwin",
     "name": "Godwin",
     "iconID": "monsters_ld1:134",
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godwin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godwin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godwin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=village_godwin.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
