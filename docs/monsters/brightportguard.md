---
description: "Brightport guard is an NPC who can also be fought in Andor's Trail, found in Brightport."
---

# ![](../assets/icons/monsters/monsters_ld1_94.png){ .sprite } Brightport guard

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_94.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Brightport |
| **Class** | Humanoid |
| **HP** | 120 |
| **XP when defeated** | 315 |
| **Entries in game data** | 9 |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

!!! info "9 entries in the game data"
    The game data defines 9 separate characters named Brightport guard. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location, combat statistics, faction, appearance, movement. Each entry has its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`brightportguard`](#v-brightportguard) | NPC | Brightport: [Brightport 1](../maps/brightport1.md#pin-npc-brightportguard), Brightport: [Brightport 5](../maps/brightport5.md#pin-npc-brightportguard) (+1 more) | – | – |
| [`brightport_guardbase`](#v-brightport_guardbase) | NPC | Brightport: [Brightport 9](../maps/brightport9.md#pin-npc-brightport_guardbase) | – | – |
| [`brightport_guardcrate`](#v-brightport_guardcrate) | NPC | Brightport: [Brightport abandoned](../maps/brightport_abandoned.md#pin-npc-brightport_guardcrate) | – | – |
| [`brightport_guardfight`](#v-brightport_guardfight) | Enemy | Brightport: [Brightport abandoned](../maps/brightport_abandoned.md) | – | 120 |
| [`brightport_guardgoons`](#v-brightport_guardgoons) | NPC | Brightport: [Brightport benbyr](../maps/brightport_benbyr.md#pin-npc-brightport_guardgoons) | – | – |
| [`brightport_jailguard`](#v-brightport_jailguard) | NPC | Brightport: [Brightport jail](../maps/brightport_jail.md#pin-npc-brightport_jailguard) | – | – |
| [`brightportchapelguard`](#v-brightportchapelguard) | NPC | Brightport: [Brightport 7](../maps/brightport7.md#pin-npc-brightportchapelguard) | – | – |
| [`brightportguard2`](#v-brightportguard2) | NPC | Brightport: [Brightport 5](../maps/brightport5.md#pin-npc-brightportguard2) | – | – |
| [`brightportnorthguard`](#v-brightportnorthguard) | NPC | Brightport: [Brightport 4](../maps/brightport4.md#pin-npc-brightportnorthguard) | – | – |

## Brightport, Brightport 1 and 2 more (brightportguard) { #v-brightportguard }

**Entry ID:** `brightportguard` · **Type:** NPC

**Location:** Brightport: [Brightport 1](../maps/brightport1.md#pin-npc-brightportguard), Brightport: [Brightport 5](../maps/brightport5.md#pin-npc-brightportguard), Brightport: [Brightport guards 2](../maps/brightport_guards2.md#pin-npc-brightportguard)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brightport 1](../maps/brightport1.md) | Brightport | 1 | – |
| [Brightport 5](../maps/brightport5.md) | Brightport | 1 | – |
| [Brightport guards 2](../maps/brightport_guards2.md) | Brightport | 1 | – |

### Dialogue simulator

Set your quest stages and items, then talk to Brightport guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_guard1.json" data-npc="Brightport guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightportguard-brightport_guard1"></span>**`brightport_guard1`** [Brightport guard](../monsters/brightportguard.md): “Keep yourself safe.”




### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brightportguard)"

    | | |
    |---|---|
    | Entry ID | `brightportguard` |
    | Spawn group | `brightportguards` |
    | Loot table | – |
    | Conversation | `brightport_guard1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:94` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportguard",
     "name": "Brightport guard",
     "iconID": "monsters_ld1:94",
     "unique": 1,
     "spawnGroup": "brightportguards",
     "faction": "",
     "phraseID": "brightport_guard1"
    }
    ```


## Brightport, Brightport 9 (brightport_guardbase) { #v-brightport_guardbase }

**Entry ID:** `brightport_guardbase` · **Type:** NPC

**Location:** Brightport: [Brightport 9](../maps/brightport9.md#pin-npc-brightport_guardbase)

### Dialogue simulator

Set your quest stages and items, then talk to Brightport guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_guardbase.json" data-npc="Brightport guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (4 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_guardbase-brightport_guardbase"></span>**`brightport_guardbase`** Brightport guard: “Another uneventful day out in the boonies.”

    - “Seems like a pretty nice place to me.” → [brightport_guardbase1](#d-brightport_guardbase-brightport_guardbase1)

    <span id="d-brightport_guardbase-brightport_guardbase1"></span>**`brightport_guardbase1`** Brightport guard: “You kidding? Feygard's much grander, if I knew that I'd be sent here I wouldn't have joined the academy.”

    - “Academy? Where is that?” → [brightport_guardbase2](#d-brightport_guardbase-brightport_guardbase2)

    <span id="d-brightport_guardbase-brightport_guardbase2"></span>**`brightport_guardbase2`** Brightport guard: “Feygard's military academy, the most famous military institution in all of Dhayavar, you should have already been taught that.”

    - “Can I join it too?” → [brightport_guardbase3](#d-brightport_guardbase-brightport_guardbase3)
    - “Now, I know. Bye.” → *conversation ends*

    <span id="d-brightport_guardbase-brightport_guardbase3"></span>**`brightport_guardbase3`** Brightport guard: “Well, to put it mildly, no. You need citizenship and some well-off connections. Sorry to shatter your dream.”

    - “I'll get there someday.” → *conversation ends*
    - “I wasn't planning on doing that either way.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 4 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brightport_guardbase)"

    | | |
    |---|---|
    | Entry ID | `brightport_guardbase` |
    | Spawn group | `brightport_guardbase` |
    | Loot table | – |
    | Conversation | `brightport_guardbase` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:94` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_guardbase",
     "name": "Brightport guard",
     "iconID": "monsters_ld1:94",
     "phraseID": "brightport_guardbase"
    }
    ```


## Brightport, Brightport abandoned (brightport_guardcrate) { #v-brightport_guardcrate }

**Entry ID:** `brightport_guardcrate` · **Type:** NPC

**Location:** Brightport: [Brightport abandoned](../maps/brightport_abandoned.md#pin-npc-brightport_guardcrate)

### Quests

- [Boxed in](../quests/brightport_thieves.md): stage 35
- [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md): stages 144, 159, 173, 209, 210, 220

### Dialogue simulator

Set your quest stages and items, then talk to Brightport guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_crateguard_selector.json" data-npc="Brightport guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (26 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_guardcrate-brightport_crateguard_selector"></span>**`brightport_crateguard_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 210 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-210))* → [brightport_guardcrate17](#d-brightport_guardcrate-brightport_guardcrate17)
    - Next *(if reached stage 209 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-209))* → [brightport_guardcrate14](#d-brightport_guardcrate-brightport_guardcrate14)
    - Next *(if reached stage 173 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-173))* → [brightport_crateguard_arrest3](#d-brightport_guardcrate-brightport_crateguard_arrest3)
    - Next *(if reached stage 159 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-159))* → [brightport_crateguard_arrest](#d-brightport_guardcrate-brightport_crateguard_arrest)
    - Next → [brightport_crateguard](#d-brightport_guardcrate-brightport_crateguard)

    <span id="d-brightport_guardcrate-brightport_guardcrate17"></span>**`brightport_guardcrate17`** Brightport guard: “Agreed. You're coming with us. The commander can sort this out.” — **effects:** sets stage 210 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-210)

    - Next → [brightport_crateguard_packageselector](#d-brightport_guardcrate-brightport_crateguard_packageselector)

    <span id="d-brightport_guardcrate-brightport_guardcrate14"></span>**`brightport_guardcrate14`** [Brightport guard](../monsters/brightportguard.md#v-brightport_guardcrate): “Enough games. You're coming with us.” — **effects:** sets stage 209 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-209)

    - Next → [brightport_crateguard_packageselector](#d-brightport_guardcrate-brightport_crateguard_packageselector)

    <span id="d-brightport_guardcrate-brightport_crateguard_arrest3"></span>**`brightport_crateguard_arrest3`** Brightport guard: “I don't think so, we follow the law not the commander. You will be coming with us. We'll interrogate you later about what you were doing here.” — **effects:** sets stage 173 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-173)

    - Next → [brightport_crateguard_packageselector](#d-brightport_guardcrate-brightport_crateguard_packageselector)

    <span id="d-brightport_guardcrate-brightport_crateguard_arrest"></span>**`brightport_crateguard_arrest`** Brightport guard: “Ha! The commander can forgive a mistake or two. Grab him. We'll interrogate him later” — **effects:** sets stage 159 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-159)

    - Next → [brightport_crateguard_packageselector](#d-brightport_guardcrate-brightport_crateguard_packageselector)

    <span id="d-brightport_guardcrate-brightport_crateguard"></span>**`brightport_crateguard`** Brightport guard: “Halt! What are you doing here?”

    - “I'm searching for my brother Andor, have you seen him?” *(if NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); NOT reached stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120))* → [brightport_crateguard8](#d-brightport_guardcrate-brightport_crateguard8)
    - “That's private. Nothing you need to worry about.” *(if reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60))* → [brightport_crateguard0](#d-brightport_guardcrate-brightport_crateguard0)
    - “Gentlemen. Has sir Gunfryk not told you to keep your noses out of places they don't belong?” *(if reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60))* → [brightport_crateguard2](#d-brightport_guardcrate-brightport_crateguard2)
    - “I was patrolling the place to keep it safe from troublemakers, obviously.” *(if reached stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120))* → [brightport_crateguard3](#d-brightport_guardcrate-brightport_crateguard3)

    <span id="d-brightport_guardcrate-brightport_crateguard_packageselector"></span>**`brightport_crateguard_packageselector`** *(silent check: the first matching branch below is taken)*

    - Next *(if hand over 1× [Package](../items/brightportpackage.md))* → [brightport_crate_failure_arrest](#d-brightport_guardcrate-brightport_crate_failure_arrest)
    - Next → [brightport_crate_failure_arrest](#d-brightport_guardcrate-brightport_crate_failure_arrest)

    <span id="d-brightport_guardcrate-brightport_crateguard8"></span>**`brightport_crateguard8`** Brightport guard: “And we're supposed to believe that?”

    - Next → [brightport_crateguard9](#d-brightport_guardcrate-brightport_crateguard9)

    <span id="d-brightport_guardcrate-brightport_crateguard0"></span>**`brightport_crateguard0`** Brightport guard: “What's with that tone?! We came here on a simple patrol but I think we might have caught a spy. We should arrest him, right partner?”

    - “Think about it twice. You try and arrest me, and by tomorrow morning you might find yourself discharged, or on a…” → [brightport_crateguard_arrest_selector](#d-brightport_guardcrate-brightport_crateguard_arrest_selector)

    <span id="d-brightport_guardcrate-brightport_crateguard2"></span>**`brightport_crateguard2`** Brightport guard: “Ha, you're funny kid. And suspicious. Funny and suspicious. The commander himself ordered us to go on a patrol. So I think we've caught a troublemaker.”

    - “He might have ordered you to come here, but did he not tell you to keep your hands off Barthold and his friends? I…” → [brightport_crateguard_arrest2](#d-brightport_guardcrate-brightport_crateguard_arrest2)

    <span id="d-brightport_guardcrate-brightport_crateguard3"></span>**`brightport_crateguard3`** Brightport guard: “Wait, I think I know you. You're the kid who helped us with capturing those two criminals!”

    - Next → [brightport_crateguard4](#d-brightport_guardcrate-brightport_crateguard4)

    <span id="d-brightport_guardcrate-brightport_crate_failure_arrest"></span>**`brightport_crate_failure_arrest`** Brightport guard: “The guards grab you by your shoulders and restrain you. You try shaking them off, but you can't resist them. They put a blindfold over your eyes, and next thing you know, you're in a jail cell.” — **effects:** moves you to [Brightport jail](../maps/brightport_jail.md), sets stage 144 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-144), clears stage 158 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-158), removes monsters from brightport_abandoned, starts timer “brightport_jail”, sets stage 220 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-220)


    <span id="d-brightport_guardcrate-brightport_crateguard9"></span>**`brightport_crateguard9`** Brightport guard: “Calm down, our duty is to protect the citizens of this town. Maybe that cloaked figure was his brother.”

    - Next → [brightport_guardcrate10](#d-brightport_guardcrate-brightport_guardcrate10)

    <span id="d-brightport_guardcrate-brightport_crateguard_arrest_selector"></span>**`brightport_crateguard_arrest_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if random chance (5%))* → [brightport_crateguard_arrest](#d-brightport_guardcrate-brightport_crateguard_arrest)
    - Next *(if random chance (100%))* → [brightport_crateguard1](#d-brightport_guardcrate-brightport_crateguard1)

    <span id="d-brightport_guardcrate-brightport_crateguard_arrest2"></span>**`brightport_crateguard_arrest2`** *(silent check: the first matching branch below is taken)*

    - Next *(if random chance (5%))* → [brightport_crateguard_arrest3](#d-brightport_guardcrate-brightport_crateguard_arrest3)
    - Next *(if random chance (100%))* → [brightport_crateguard7](#d-brightport_guardcrate-brightport_crateguard7)

    <span id="d-brightport_guardcrate-brightport_crateguard4"></span>**`brightport_crateguard4`** Brightport guard: “I guess you were the one the lookout spotted, so there is nothing else suspicious here. Either way, you did some impressive work with those two, but you shouldn't be hanging out around here. It's dangerous.”

    - “Anything for the glory of Feygard.” → [brightport_crateguard5](#d-brightport_guardcrate-brightport_crateguard5)

    <span id="d-brightport_guardcrate-brightport_guardcrate10"></span>**`brightport_guardcrate10`** Brightport guard: “Hmph, fine. We'll ask you a few questions then. What would your brother be doing here?”

    - “We were playing hide and seek.” → [brightport_guardcrate11](#d-brightport_guardcrate-brightport_guardcrate11)
    - “I don't know, I've been looking everywhere I can.” → [brightport_guardcrate15](#d-brightport_guardcrate-brightport_guardcrate15)

    <span id="d-brightport_guardcrate-brightport_crateguard1"></span>**`brightport_crateguard1`** Brightport guard: “Alright, alright, no need to get worked up. I think I've heard your name mentioned by the captain, so we'll trust him with this.”

    - Next → [brightport_crateguard6](#d-brightport_guardcrate-brightport_crateguard6)

    <span id="d-brightport_guardcrate-brightport_crateguard7"></span>**`brightport_crateguard7`** Brightport guard: “Alright, got it. Never thought the commander would let someone suspicious like you run around, but we'll trust his judgment.”

    - Next → [brightport_crateguard6](#d-brightport_guardcrate-brightport_crateguard6)

    <span id="d-brightport_guardcrate-brightport_crateguard5"></span>**`brightport_crateguard5`** Brightport guard: “That's the spirit. We'll be heading back now, so follow behind us. Wouldn't want a future knight of Feygard getting hurt.”

    - “Sure, I'll be right behind you.” → [brightport_crateguard6](#d-brightport_guardcrate-brightport_crateguard6)

    <span id="d-brightport_guardcrate-brightport_guardcrate11"></span>**`brightport_guardcrate11`** Brightport guard: “Hide and seek. In an abandoned structure, ways from town?”

    - Next → [brightport_guardcrate12](#d-brightport_guardcrate-brightport_guardcrate12)

    <span id="d-brightport_guardcrate-brightport_guardcrate15"></span>**`brightport_guardcrate15`** Brightport guard: “You expect us to believe your brother's been the one wandering around this ruin?”

    - Next → [brightport_guardcrate16](#d-brightport_guardcrate-brightport_guardcrate16)

    <span id="d-brightport_guardcrate-brightport_crateguard6"></span>**`brightport_crateguard6`** [Dummy NPC](../monsters/none.md): “The two guards exchange a glance, then turn and leave the building.” — **effects:** removes monsters from brightport_abandoned, sets stage 144 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-144), clears stage 158 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-158), sets stage 35 of [Boxed in](../quests/brightport_thieves.md#stage-35)


    <span id="d-brightport_guardcrate-brightport_guardcrate12"></span>**`brightport_guardcrate12`** Brightport guard: “And I suppose your friends are hiding in the jail cell too, huh?”

    - Next → [brightport_guardcrate13](#d-brightport_guardcrate-brightport_guardcrate13)

    <span id="d-brightport_guardcrate-brightport_guardcrate16"></span>**`brightport_guardcrate16`** Brightport guard: “Sounds like an excuse to me. No one just wanders in here.”

    - Next → [brightport_guardcrate17](#d-brightport_guardcrate-brightport_guardcrate17)

    <span id="d-brightport_guardcrate-brightport_guardcrate13"></span>**`brightport_guardcrate13`** [Dummy NPC](../monsters/none.md): “The guards both laugh.”

    - Next → [brightport_guardcrate14](#d-brightport_guardcrate-brightport_guardcrate14)



### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 26 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brightport_guardcrate)"

    | | |
    |---|---|
    | Entry ID | `brightport_guardcrate` |
    | Spawn group | `brightport_guardcrate` |
    | Loot table | – |
    | Conversation | `brightport_crateguard_selector` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:94` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_guardcrate",
     "name": "Brightport guard",
     "iconID": "monsters_ld1:94",
     "movementAggressionType": "wholeMap",
     "phraseID": "brightport_crateguard_selector"
    }
    ```


## Brightport, Brightport abandoned (brightport_guardfight) { #v-brightport_guardfight }

**Entry ID:** `brightport_guardfight` · **Type:** Enemy

**Location:** Brightport: [Brightport abandoned](../maps/brightport_abandoned.md)

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 120 |
| XP when defeated | 315 |
| Damage | 10 to 25 |
| Attack chance | 140 |
| Block chance | 130 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Brightport abandoned](../maps/brightport_abandoned.md) | Brightport | 2 | Appears later, during a quest |

### Quests that count defeats

- [Priceful vengeance](../quests/brightport_goons.md#stage-70) with stepping on a trigger on [Brightport abandoned](../maps/brightport_abandoned.md) checks that at least 2 of these enemies have been defeated.


### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brightport_guardfight)"

    | | |
    |---|---|
    | Entry ID | `brightport_guardfight` |
    | Spawn group | `brightport_guardfight` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:95` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_guardfight",
     "name": "Brightport guard",
     "iconID": "monsters_ld1:95",
     "maxHP": 120,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "movementAggressionType": "wholeMap",
     "attackDamage": {
      "min": 10,
      "max": 25
     },
     "attackCost": 5,
     "attackChance": 140,
     "blockChance": 130,
     "damageResistance": 3
    }
    ```


## Brightport, Brightport benbyr (brightport_guardgoons) { #v-brightport_guardgoons }

**Entry ID:** `brightport_guardgoons` · **Type:** NPC

**Location:** Brightport: [Brightport benbyr](../maps/brightport_benbyr.md#pin-npc-brightport_guardgoons)

### Dialogue simulator

Set your quest stages and items, then talk to Brightport guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_guards.json" data-npc="Brightport guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_guardgoons-brightport_guards"></span>**`brightport_guards`** Brightport guard: “You're the kid who gave us the information on these two right? Good work on that.”




### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brightport_guardgoons)"

    | | |
    |---|---|
    | Entry ID | `brightport_guardgoons` |
    | Spawn group | `brightport_guardgoons` |
    | Loot table | – |
    | Conversation | `brightport_guards` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:95` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_guardgoons",
     "name": "Brightport guard",
     "iconID": "monsters_ld1:95",
     "phraseID": "brightport_guards"
    }
    ```


## Brightport, Brightport jail (brightport_jailguard) { #v-brightport_jailguard }

**Entry ID:** `brightport_jailguard` · **Type:** NPC

**Location:** Brightport: [Brightport jail](../maps/brightport_jail.md#pin-npc-brightport_jailguard)

### Dialogue simulator

Set your quest stages and items, then talk to Brightport guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_jailguard.json" data-npc="Brightport guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightport_jailguard-brightport_jailguard"></span>**`brightport_jailguard`** Brightport guard: “I'm on cooking duty today, feels nice to enjoy the weather without that bulky armor on.”

    - “Do you often use that jail cell?” → [brightport_jailguard1](#d-brightport_jailguard-brightport_jailguard1)

    <span id="d-brightport_jailguard-brightport_jailguard1"></span>**`brightport_jailguard1`** Brightport guard: “No, not at all. Rarely do we ever put anyone in there, and even then, it's mostly drunks to cool off for a night. On the rare occasion we do have a criminal, they are sent to court and then to the Feygard prison.”




### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brightport_jailguard)"

    | | |
    |---|---|
    | Entry ID | `brightport_jailguard` |
    | Spawn group | `brightport_jailguard` |
    | Loot table | – |
    | Conversation | `brightport_jailguard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_karvis2:2` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_jailguard",
     "name": "Brightport guard",
     "iconID": "monsters_karvis2:2",
     "phraseID": "brightport_jailguard"
    }
    ```


## Brightport, Brightport 7 (brightportchapelguard) { #v-brightportchapelguard }

**Entry ID:** `brightportchapelguard` · **Type:** NPC

**Location:** Brightport: [Brightport 7](../maps/brightport7.md#pin-npc-brightportchapelguard)

### Dialogue simulator

Set your quest stages and items, then talk to Brightport guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_guard.json" data-npc="Brightport guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightportchapelguard-brightport_guard"></span>**`brightport_guard`** Brightport guard: “I hope my shift ends soon! I was staring at the surface of the lake when I spotted a pair of yellow eyes looking at me from under the surface!”




### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brightportchapelguard)"

    | | |
    |---|---|
    | Entry ID | `brightportchapelguard` |
    | Spawn group | `brightportchapelguard` |
    | Loot table | – |
    | Conversation | `brightport_guard` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_ld1:95` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportchapelguard",
     "name": "Brightport guard",
     "iconID": "monsters_ld1:95",
     "maxHP": 120,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "phraseID": "brightport_guard",
     "attackCost": 5,
     "attackChance": 160,
     "blockChance": 130
    }
    ```


## Brightport, Brightport 5 (brightportguard2) { #v-brightportguard2 }

**Entry ID:** `brightportguard2` · **Type:** NPC

**Location:** Brightport: [Brightport 5](../maps/brightport5.md#pin-npc-brightportguard2)

### Quests

- [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md): stage 232

### Dialogue simulator

Set your quest stages and items, then talk to Brightport guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightportguard_1_selector.json" data-npc="Brightport guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightportguard2-brightportguard_1_selector"></span>**`brightportguard_1_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 144 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-144); NOT reached stage 220 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-220); NOT reached stage 232 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-232))* → [brightportguard_afterhide](#d-brightportguard2-brightportguard_afterhide)
    - Next *(if reached stage 220 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-220); NOT reached stage 232 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-232))* → [brightportguard_2](#d-brightportguard2-brightportguard_2)
    - Next → [brightportguard_1](#d-brightportguard2-brightportguard_1)

    <span id="d-brightportguard2-brightportguard_afterhide"></span>**`brightportguard_afterhide`** Brightport guard: “Hey, did you not meet with my comrades? They came back from a patrol just now.” — **effects:** sets stage 232 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-232)

    - “Uhh no, bye.” → *conversation ends*

    <span id="d-brightportguard2-brightportguard_2"></span>**`brightportguard_2`** Brightport guard: “Hmm? I think I saw my comrades carry you away from this direction before...” — **effects:** sets stage 232 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-232)

    - “Oops, gotta go.” → *conversation ends*

    <span id="d-brightportguard2-brightportguard_1"></span>**`brightportguard_1`** Brightport guard: “Halt! If you value your life, stay off this path.” — **effects:** clears stage 232 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-232)

    - “Ha, I can handle myself. Don't worry about me.” → [brightportguard_1reply](#d-brightportguard2-brightportguard_1reply)
    - “What's wrong with this road?” → [brightportguard_1reply1](#d-brightportguard2-brightportguard_1reply1)
    - “[Slip past him.]” → *conversation ends*

    <span id="d-brightportguard2-brightportguard_1reply"></span>**`brightportguard_1reply`** [Brightport guard](../monsters/brightportguard.md#v-brightportguard2): “Sure, kid. You do seem to be carrying some shiny equipment. Just don't blame me if you get eaten by a scary lizardman.”

    - “Lizardmen?” → [brightportguard_1reply2](#d-brightportguard2-brightportguard_1reply2)

    <span id="d-brightportguard2-brightportguard_1reply1"></span>**`brightportguard_1reply1`** [Brightport guard](../monsters/brightportguard.md#v-brightportguard2): “If you go that way, all you'll find is a shack, some trees, and the mountain. What's really scary are the nasty lizardmen who occasionally stumble up on the shore.”

    - “Lizardmen?” → [brightportguard_1reply2](#d-brightportguard2-brightportguard_1reply2)
    - “Guess I'll turn around.” → [brightportguard_1reply3](#d-brightportguard2-brightportguard_1reply3)

    <span id="d-brightportguard2-brightportguard_1reply2"></span>**`brightportguard_1reply2`** [Brightport guard](../monsters/brightportguard.md): “Terrifying, humanoid creatures with blood-red scales instead of skin, and the head of a giant Erumen lizard.”

    - Next → [brightportguard_1_reply4](#d-brightportguard2-brightportguard_1_reply4)

    <span id="d-brightportguard2-brightportguard_1reply3"></span>**`brightportguard_1reply3`** [Brightport guard](../monsters/brightportguard.md#v-brightportguard2): “Take care, and don't slack off in school, or else you'll end up slaying sewer rats down in Nor City. [laughs]”


    <span id="d-brightportguard2-brightportguard_1_reply4"></span>**`brightportguard_1_reply4`** [Brightport guard](../monsters/brightportguard.md): “Just the thought gives me shivers.”

    - “Guess I'll go back.” → [brightportguard_1reply3](#d-brightportguard2-brightportguard_1reply3)



### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brightportguard2)"

    | | |
    |---|---|
    | Entry ID | `brightportguard2` |
    | Spawn group | `brightportguard2` |
    | Loot table | – |
    | Conversation | `brightportguard_1_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:95` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportguard2",
     "name": "Brightport guard",
     "iconID": "monsters_ld1:95",
     "unique": 1,
     "phraseID": "brightportguard_1_selector"
    }
    ```


## Brightport, Brightport 4 (brightportnorthguard) { #v-brightportnorthguard }

**Entry ID:** `brightportnorthguard` · **Type:** NPC

**Location:** Brightport: [Brightport 4](../maps/brightport4.md#pin-npc-brightportnorthguard)

### Quests

- [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md): stage 251

### Dialogue simulator

Set your quest stages and items, then talk to Brightport guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_guard_north1.json" data-npc="Brightport guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-brightportnorthguard-brightport_guard_north1"></span>**`brightport_guard_north1`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 249 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-249))* → [brightport_guard_north0](#d-brightportnorthguard-brightport_guard_north0)
    - Next *(if reached stage 250 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-250))* → [brightport_guard_north2](#d-brightportnorthguard-brightport_guard_north2)

    <span id="d-brightportnorthguard-brightport_guard_north0"></span>**`brightport_guard_north0`** Brightport guard: “Coming in from the north? Then you must have seen the terrible state of the forest. Some say it's a curse sent upon Brightport by the Shadow for what happened at the Great Water Temple.”

    - “Can you tell me more about that?” → [brightport_guard_north3](#d-brightportnorthguard-brightport_guard_north3)

    <span id="d-brightportnorthguard-brightport_guard_north2"></span>**`brightport_guard_north2`** Brightport guard: “The road north runs through that forsaken forest, but it's still better than heading south. Keep yourself safe.”

    - “What's happening to the south?” → [brightport_guard_north4](#d-brightportnorthguard-brightport_guard_north4)

    <span id="d-brightportnorthguard-brightport_guard_north3"></span>**`brightport_guard_north3`** Brightport guard: “I wouldn't know. I'm from Feygard, but you could ask at the small temple in town.” — **effects:** sets stage 251 of [Brightport story flags (hidden flag)](../quests/brightport_nondisplay.md#stage-251)


    <span id="d-brightportnorthguard-brightport_guard_north4"></span>**`brightport_guard_north4`** Brightport guard: “The deer started attacking people. It's odd, but they tend to stay away if you're traveling in a group.”

    - “Terrible times to be a lone traveler.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (brightportnorthguard)"

    | | |
    |---|---|
    | Entry ID | `brightportnorthguard` |
    | Spawn group | `brightportnorthguard` |
    | Loot table | – |
    | Conversation | `brightport_guard_north1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:94` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightportnorthguard",
     "name": "Brightport guard",
     "iconID": "monsters_ld1:94",
     "phraseID": "brightport_guard_north1"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportguard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
