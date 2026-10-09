---
description: "Road rondel is an NPC you can also fight in Andor's Trail, found in Wexlow Village."
---

# ![](../assets/icons/monsters/monsters_tometik6_1.png){ .sprite } Road rondel

**Where to find Road rondel:** [Wexlow Village, Wayto feygard duleian 1](#v-road_rondel), [Wexlow Village, Wayto feygard duleian 1](#v-road_rondel_blocker)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_tometik6_1.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Wexlow Village |
| **Class** | Humanoid |
| **HP** | 120 |
| **XP when defeated** | 310 |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Wexlow Village, Wayto feygard duleian 1 { #v-road_rondel }

**Where:** Wexlow Village: [Wayto feygard duleian 1](../maps/wayto_feygard_duleian_1.md#pin-npc-road_rondel)

### Dialogue simulator

Set your quest stages and items, then talk to Road rondel. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/road_rondel_ip.json" data-npc="Road rondel" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-road_rondel-road_rondel_ip"></span>**`road_rondel_ip`** Road rondel: “I'm so saddened by the loss of my brother, all I can do is stand here starring at these flowers.”

    - “Why'd you move so quickly?” → [road_rondel_move_hint](#d-road_rondel-road_rondel_move_hint)

    <span id="d-road_rondel-road_rondel_move_hint"></span>**`road_rondel_move_hint`** Road rondel: “[While scanning you up and down with his eyes...] There's something... about you... something warm. Ain't my place to stand in the way of that.”




### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Wexlow Village, Wayto feygard duleian 1 (2) { #v-road_rondel_blocker }

**Where:** Wexlow Village: [Wayto feygard duleian 1](../maps/wayto_feygard_duleian_1.md#pin-npc-road_rondel_blocker)

!!! warning "You can fight Road rondel"
    Answering “Well, if it's any consolation, you are about to join him.” starts a fight with Road rondel.

### Combat

| | |
|---|---|
| Class | Humanoid |
| HP | 120 |
| XP when defeated | 310 |
| Damage | 2 to 4 |
| AC | 60 |
| BC | 200 |
| DR | 8 |
| Attacks per turn | 2 (4 AP each, 10 AP) |
| Crit chance | none |


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 7 to 77 |

### Dialogue simulator

Set your quest stages and items, then talk to Road rondel. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/road_rondel_blocker_ip.json" data-npc="Road rondel" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-road_rondel_blocker-road_rondel_blocker_ip"></span>**`road_rondel_blocker_ip`** Road rondel: “Halt!”

    - “Wait a minute. Don't I know you from somewhere?” → [road_rondel_blocker_halt](#d-road_rondel_blocker-road_rondel_blocker_halt)

    <span id="d-road_rondel_blocker-road_rondel_blocker_halt"></span>**`road_rondel_blocker_halt`** Road rondel: “I said "halt"!”

    - “Yes! I know you. But I am pretty damn sure that I killed you back there [pointing southeast] on the bridge.” → [road_rondel_blocker_brother_1](#d-road_rondel_blocker-road_rondel_blocker_brother_1)

    <span id="d-road_rondel_blocker-road_rondel_blocker_brother_1"></span>**`road_rondel_blocker_brother_1`** Road rondel: “You killed my brother?!”

    - “Yes, it appears so, but I had no choice. You see, he wouldn't get out of my way. Kind of like you.” → [road_rondel_blocker_brother_2](#d-road_rondel_blocker-road_rondel_blocker_brother_2)

    <span id="d-road_rondel_blocker-road_rondel_blocker_brother_2"></span>**`road_rondel_blocker_brother_2`** Road rondel: “I am disheartened and full of rage hearing of this.”

    - “Well, if it's any consolation, you are about to join him.” *(if NOT carry 1× [Gem of warmth](../items/gem_fire.md))* → *fight starts*
    - “Step aside before I am forced to reunite you two.” *(if carry 1× [Gem of warmth](../items/gem_fire.md))* → [road_rondel_blocker_brother_3](#d-road_rondel_blocker-road_rondel_blocker_brother_3)

    <span id="d-road_rondel_blocker-road_rondel_blocker_brother_3"></span>**`road_rondel_blocker_brother_3`** Road rondel: “Of course.” — **effects:** removes monsters from wayto_feygard_duleian_1, spawns monsters on wayto_feygard_duleian_1




### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Road rondel. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, combat statistics, loot or shop stock, movement.

| Entry | Type | Section |
|---|---|---|
| `road_rondel` | NPC | [Wexlow Village, Wayto feygard duleian 1](#v-road_rondel) |
| `road_rondel_blocker` | NPC/Enemy | [Wexlow Village, Wayto feygard duleian 1](#v-road_rondel_blocker) |

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: road_rondel"

    | | |
    |---|---|
    | Entry ID | `road_rondel` |
    | Type (wiki) | NPC |
    | Spawn group | `road_rondel` |
    | Loot table | – |
    | Conversation | `road_rondel_ip` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_tometik6:1` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "road_rondel",
     "name": "Road rondel",
     "iconID": "monsters_tometik6:1",
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "road_rondel_ip"
    }
    ```

??? info "Technical information: road_rondel_blocker"

    | | |
    |---|---|
    | Entry ID | `road_rondel_blocker` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `road_rondel_blocker` |
    | Loot table | `guynmart_drp_robber` |
    | Conversation | `road_rondel_blocker_ip` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik6:1` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "road_rondel_blocker",
     "name": "Road rondel",
     "iconID": "monsters_tometik6:1",
     "maxHP": 120,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 4
     },
     "phraseID": "road_rondel_blocker_ip",
     "droplistID": "guynmart_drp_robber",
     "attackCost": 4,
     "attackChance": 60,
     "blockChance": 200,
     "damageResistance": 8
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=road_rondel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=road_rondel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=road_rondel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=road_rondel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
