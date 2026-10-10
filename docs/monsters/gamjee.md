---
description: "Gamjee is an NPC you can also fight in Andor's Trail, found in Gamjee well 4 1."
---

# ![](../assets/icons/monsters/monsters_cyclops_0.png){ .sprite } Gamjee

**Where to find Gamjee:** [Gamjee well 4 1](#v-gamjee), [Gamjee well 4 1](#v-gamjee_hidden), [Gamjee well 4 1](#v-gamjee_oc)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_cyclops_0.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC/Enemy (talks, but can also be fought) |
| **Found in** | Gamjee well 4 1 |
| **Class** | Giant |
| **HP** | 417 |
| **XP when defeated** | 741 |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Gamjee well 4 1 { #v-gamjee }

**Where:** [Gamjee well 4 1](../maps/gamjee_well_4_1.md#pin-npc-gamjee)

!!! warning "You can fight Gamjee"
    The conversation can lead straight into a fight with Gamjee.

    Answering “This ends now for you!” during [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-4) starts a fight with Gamjee.

    Answering “I don't believe you! I can't take that risk. This ends now” during [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-3) starts a fight with Gamjee.

### Combat

| | |
|---|---|
| Class | Giant |
| HP | 417 |
| XP when defeated | 741 |
| Damage | 10 to 13 |
| AC | 70 |
| BC | 101 |
| DR | 13 |
| Attacks per turn | 1 (6 AP each, 10 AP) |
| Crit chance | 12% (×2.0) |

**Its hits:** On target: [Concussion](../conditions/concussion.md) (magnitude 1, 2 rounds, 5% chance)

**When you hit it:** On target: [Soaked vision](../conditions/soaked_vision.md) (magnitude 1, 2 rounds, 30% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gamjee's rope](../items/gamjee_rope.md) | 100% | 1 |
| [Cragbreaker](../items/cragbreaker.md) | 100% | 1 |
| [Godwin's ring](../items/godwin_ring.md) | 100% | 1 |

### Quests that count defeats

- [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-11) with stepping on a trigger on [Gamjee well 4 1](../maps/gamjee_well_4_1.md) checks that this enemy has been defeated.
- [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-9) with stepping on a trigger on [Gamjee well 4 1](../maps/gamjee_well_4_1.md) checks that this enemy has been defeated.

### Quests

- [Echoes of enchantment](../quests/echoes_of_enchantment.md): stages 8, 12, 13
- [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md): stages 3, 4, 5, 6

### Dialogue simulator

Talk to Gamjee as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/gamjee_selector.json" data-npc="Gamjee" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (23 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-gamjee-gamjee_selector"></span>**`gamjee_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 5 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-5))* → *fight starts*
    - Next *(if NOT reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); NOT reached stage 13 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-13); NOT reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8))* → [gamjee_villagers_unknown_1](#d-gamjee-gamjee_villagers_unknown_1)
    - Next *(if reached stage 13 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-13))* → [gamjee_no_business](#d-gamjee-gamjee_no_business)
    - Next *(if reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5))* → [gamjee_villagers_known_1](#d-gamjee-gamjee_villagers_known_1)
    - Next *(if NOT reached stage 5 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-5); reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8))* → [gamjee_player_left_after_agreeing_to_help](#d-gamjee-gamjee_player_left_after_agreeing_to_help)

    <span id="d-gamjee-gamjee_villagers_unknown_1"></span>**`gamjee_villagers_unknown_1`** Gamjee: “Human, why you come here? Gamjee no hurt you if you leave now.”

    - “I'm just exploring. Who are you, and why are you here?” → [gamjee_villagers_unknown_2](#d-gamjee-gamjee_villagers_unknown_2)

    <span id="d-gamjee-gamjee_no_business"></span>**`gamjee_no_business`** Gamjee: “Why you still here? Leave now.”


    <span id="d-gamjee-gamjee_villagers_known_1"></span>**`gamjee_villagers_known_1`** Gamjee: “Human, why you come here? Gamjee no hurt you if you leave now.”

    - “I've found the people you captured. You need to let them go.” *(if NOT reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8))* → [gamjee_villagers_known_2](#d-gamjee-gamjee_villagers_known_2)
    - “I want to help you and the villagers.” *(if reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8))* → [gamjee_compromise_1](#d-gamjee-gamjee_compromise_1)

    <span id="d-gamjee-gamjee_player_left_after_agreeing_to_help"></span>**`gamjee_player_left_after_agreeing_to_help`** Gamjee: “Human, why you leave? Rude.”

    - “I want to help you and the villagers.” → [gamjee_compromise_1](#d-gamjee-gamjee_compromise_1)

    <span id="d-gamjee-gamjee_villagers_unknown_2"></span>**`gamjee_villagers_unknown_2`** Gamjee: “Gamjee guard well. Humans come, take Gamjee's well, build village. They no ask. They just take. Gamjee scared. Need protect well. You help Gamjee?”

    - “You're afraid they'll come back and take more?” → [gamjee_villagers_unknown_peace](#d-gamjee-gamjee_villagers_unknown_peace)
    - “I thought I heard somes voices earlier. Have you hurt anybody recently?” → [gamjee_villagers_unknown_3](#d-gamjee-gamjee_villagers_unknown_3)

    <span id="d-gamjee-gamjee_villagers_known_2"></span>**`gamjee_villagers_known_2`** Gamjee: “Captured? No, no! Gamjee protect them! Humans take Gamjee's well, build village. They no ask. They just take. Gamjee keep them safe here. You see, they not hurt.”

    - “Keeping them in a pit isn't protecting them. It's imprisoning them.” → [gamjee_villagers_known_3](#d-gamjee-gamjee_villagers_known_3)

    <span id="d-gamjee-gamjee_compromise_1"></span>**`gamjee_compromise_1`** Gamjee: “You help Gamjee? Humans no hurt?”

    - “I'll do what I can. Let's talk to the villagers.” *(if NOT reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8))* → [gamjee_compromise_2](#d-gamjee-gamjee_compromise_2)
    - “I'll do what I can. Let's talk to the villagers.” *(if NOT reached stage 6 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-6); reached stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8))* → [gamjee_compromise_2a](#d-gamjee-gamjee_compromise_2a)
    - “I'll do what I can. Let's talk to the villagers.” *(if reached stage 6 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-6))* → [gamjee_compromise_2](#d-gamjee-gamjee_compromise_2)

    <span id="d-gamjee-gamjee_villagers_unknown_peace"></span>**`gamjee_villagers_unknown_peace`** Gamjee: “Yes! Humans take all if no stop. Gamjee alone. If you help, tell humans Gamjee no bad. Maybe they listen. Maybe they share well, no fight. You help, no need for hurt.”

    - “I understand. I'll help you find a peaceful solution.” → [gamjee_compromise_1](#d-gamjee-gamjee_compromise_1)

    <span id="d-gamjee-gamjee_villagers_unknown_3"></span>**`gamjee_villagers_unknown_3`** Gamjee: “Me alone.”

    - “Really? I'm not so sure about that, but I'll see about that.” → *conversation ends*
    - “I don't believe you! Prove it.” → [gamjee_villagers_unknown_attack](#d-gamjee-gamjee_villagers_unknown_attack)

    <span id="d-gamjee-gamjee_villagers_known_3"></span>**`gamjee_villagers_known_3`** Gamjee: “No! Listen! Humans come, take Gamjee's well, leave Gamjee with nothing. Gamjee scared. If Gamjee let them go, they come back, take well again. They no understand, well is life for Gamjee. Please, you help. Tell humans Gamjee no bad. Maybe…”

    - “I see. You acted out of fear and desperation. I'll help you find a peaceful solution.” → [gamjee_compromise_1](#d-gamjee-gamjee_compromise_1)
    - “It's time to make me righteous!” → [gamjee_villagers_known_fight](#d-gamjee-gamjee_villagers_known_fight)

    <span id="d-gamjee-gamjee_compromise_2"></span>**`gamjee_compromise_2`** Gamjee: “Let Gamjee call human with magic water.” — **effects:** removes monsters from gamjee_well_jail_cells, spawns monsters on gamjee_well_4_1, sets stage 8 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-8)

    - “OK. Now that I have you two together, let's talk about how you guys can reach a compromise and share the well water.” → [gamjee_compromise_4](#d-gamjee-gamjee_compromise_4)

    <span id="d-gamjee-gamjee_compromise_2a"></span>**`gamjee_compromise_2a`** Gamjee: “OK.”

    - “Let's talk about how you guys can reach a compromise and share the well water.” → [gamjee_compromise_4](#d-gamjee-gamjee_compromise_4)

    <span id="d-gamjee-gamjee_villagers_unknown_attack"></span>**`gamjee_villagers_unknown_attack`** Gamjee: “No! Gamjee protect! If humans come back, they take all. Gamjee alone, scared.” — **effects:** sets stage 3 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-3), sets stage 5 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-5)

    - “I don't believe you! I can't take that risk. This ends now” → *fight starts*

    <span id="d-gamjee-gamjee_villagers_known_fight"></span>**`gamjee_villagers_known_fight`** Gamjee: “No! Gamjee protect! If humans come back, they take all. Gamjee alone, scared.” — **effects:** sets stage 4 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-4), sets stage 5 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-5)

    - “This ends now for you!” → *fight starts*

    <span id="d-gamjee-gamjee_compromise_4"></span>**`gamjee_compromise_4`** [Percival](../monsters/village_percival.md#v-troll_hollow_percival): “Why should we trust him? He's been keeping us captive!”

    - “Gamjee is afraid you'll take the well. He wants to protect it.” → [gamjee_compromise_5](#d-gamjee-gamjee_compromise_5)

    <span id="d-gamjee-gamjee_compromise_5"></span>**`gamjee_compromise_5`** [Percival](../monsters/village_percival.md#v-troll_hollow_percival): “And what about us? We need water too.”

    - Next → [gamjee_compromise_6](#d-gamjee-gamjee_compromise_6)

    <span id="d-gamjee-gamjee_compromise_6"></span>**`gamjee_compromise_6`** [Gamjee](../monsters/gamjee.md#v-gamjee_hidden): “Gamjee not want hurt. Humans need water. Gamjee need too.”

    - “Is there a way you can share the well? Maybe take turns using it?” → [gamjee_compromise_7](#d-gamjee-gamjee_compromise_7)

    <span id="d-gamjee-gamjee_compromise_7"></span>**`gamjee_compromise_7`** [Percival](../monsters/village_percival.md#v-troll_hollow_percival): “We can agree to that. As long as Gamjee doesn't threaten us anymore.”

    - Next → [gamjee_compromise_8](#d-gamjee-gamjee_compromise_8)

    <span id="d-gamjee-gamjee_compromise_8"></span>**`gamjee_compromise_8`** [Gamjee](../monsters/gamjee.md#v-gamjee_hidden): “Gamjee promise. No hurt. Protect well. Humans share. No fight.”

    - “Alright. Let's make this work.” *(if NOT reached stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12))* → [gamjee_compromise_9](#d-gamjee-gamjee_compromise_9)
    - “So our business here is done?” *(if reached stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12))* → [gamjee_compromise_10_no_ac](#d-gamjee-gamjee_compromise_10_no_ac)

    <span id="d-gamjee-gamjee_compromise_9"></span>**`gamjee_compromise_9`** Gamjee: “You human, go back village now.” — **effects:** removes monsters from gamjee_well_4_1, sets stage 6 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-6), sets stage 12 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-12), spawns monsters on wexlow_village

    - “So our business here is done?” *(if NOT reached stage 2 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-2))* → [gamjee_compromise_10_no_ac](#d-gamjee-gamjee_compromise_10_no_ac)
    - “So our business here is done?” *(if reached stage 2 of [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-2))* → [gamjee_compromise_10_oc](#d-gamjee-gamjee_compromise_10_oc)

    <span id="d-gamjee-gamjee_compromise_10_no_ac"></span>**`gamjee_compromise_10_no_ac`** Gamjee: “Not same. Take rope, use to free others from pit.” — **effects:** gives 1× [Gamjee's rope](../items/gamjee_rope.md), sets stage 13 of [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-13)


    <span id="d-gamjee-gamjee_compromise_10_oc"></span>**`gamjee_compromise_10_oc`** Gamjee: “take shiny thing back.” — **effects:** gives 1× [Oegyth crystal](../items/oegyth.md)

    - Next → [gamjee_compromise_10_no_ac](#d-gamjee-gamjee_compromise_10_no_ac)



### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 23 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Gamjee well 4 1 (2) { #v-gamjee_hidden }

**Where:** [Gamjee well 4 1](../maps/gamjee_well_4_1.md)


### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Gamjee well 4 1 (3) { #v-gamjee_oc }

**Where:** [Gamjee well 4 1](../maps/gamjee_well_4_1.md#pin-npc-gamjee_oc)

!!! warning "You can fight Gamjee"
    The conversation can lead straight into a fight with Gamjee.

    Answering “This ends now for you!” during [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-4) starts a fight with Gamjee.

    Answering “I don't believe you! I can't take that risk. This ends now” during [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md#stage-3) starts a fight with Gamjee.

### Combat

| | |
|---|---|
| Class | Giant |
| HP | 417 |
| XP when defeated | 741 |
| Damage | 10 to 13 |
| AC | 70 |
| BC | 101 |
| DR | 13 |
| Attacks per turn | 1 (6 AP each, 10 AP) |
| Crit chance | 12% (×2.0) |

**Its hits:** On target: [Concussion](../conditions/concussion.md) (magnitude 1, 2 rounds, 5% chance)

**When you hit it:** On target: [Soaked vision](../conditions/soaked_vision.md) (magnitude 1, 2 rounds, 30% chance)


<p class="verified">Verified against v0.8.18 monster data.</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gamjee's rope](../items/gamjee_rope.md) | 100% | 1 |
| [Cragbreaker](../items/cragbreaker.md) | 100% | 1 |
| [Godwin's ring](../items/godwin_ring.md) | 100% | 1 |
| [Stormcloak armor](../items/stormcloak_armor.md) | 100% | 1 |

### Quests that count defeats

- [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-11) with stepping on a trigger on [Gamjee well 4 1](../maps/gamjee_well_4_1.md) checks that this enemy has been defeated.
- [Echoes of enchantment](../quests/echoes_of_enchantment.md#stage-9) with stepping on a trigger on [Gamjee well 4 1](../maps/gamjee_well_4_1.md) checks that this enemy has been defeated.

### Quests

- [Echoes of enchantment](../quests/echoes_of_enchantment.md): stages 8, 12, 13
- [Feygard story flags (hidden flag)](../quests/feygard_nondisplayed.md): stages 3, 4, 5, 6

### Dialogue simulator

Talk to Gamjee as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/gamjee_selector.json" data-npc="Gamjee" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

The full dialogue for this entry is included in the listing for an earlier entry on this page, starting at [gamjee_selector](#d-gamjee-gamjee_selector).


### Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added<br>Dialogue: 23 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**3 entries.** The game data defines 3 separate characters named Gamjee. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, combat statistics, loot or shop stock, movement.

| Entry | Type | Section |
|---|---|---|
| `gamjee` | NPC/Enemy | [Gamjee well 4 1](#v-gamjee) |
| `gamjee_hidden` | Scenery | [Gamjee well 4 1](#v-gamjee_hidden) |
| `gamjee_oc` | NPC/Enemy | [Gamjee well 4 1](#v-gamjee_oc) |

- `gamjee_hidden` has no conversation and no combat statistics. Other conversations use it as their speaker (the `switchToNPC` field), which is how its name and picture appear in dialogue. The game data also places it on [Gamjee well 4 1](../maps/gamjee_well_4_1.md).

??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.

??? info "Technical information: gamjee"

    | | |
    |---|---|
    | Entry ID | `gamjee` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `gamjee` |
    | Loot table | `gamjee_dl` |
    | Conversation | `gamjee_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_cyclops:0` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "gamjee",
     "name": "Gamjee",
     "iconID": "monsters_cyclops:0",
     "maxHP": 417,
     "unique": 1,
     "monsterClass": "giant",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 10,
      "max": 13
     },
     "phraseID": "gamjee_selector",
     "droplistID": "gamjee_dl",
     "attackCost": 6,
     "attackChance": 70,
     "criticalSkill": 15,
     "criticalMultiplier": 2.0,
     "blockChance": 101,
     "damageResistance": 13,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "concussion",
        "magnitude": 1,
        "duration": 2,
        "chance": "5"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "soaked_vision",
        "magnitude": 1,
        "duration": 2,
        "chance": "30"
       }
      ]
     }
    }
    ```

??? info "Technical information: gamjee_hidden"

    | | |
    |---|---|
    | Entry ID | `gamjee_hidden` |
    | Type (wiki) | Scenery |
    | Spawn group | `gamjee_hidden` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_cyclops:0` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "gamjee_hidden",
     "name": "Gamjee",
     "iconID": "monsters_cyclops:0"
    }
    ```

??? info "Technical information: gamjee_oc"

    | | |
    |---|---|
    | Entry ID | `gamjee_oc` |
    | Type (wiki) | NPC/Enemy |
    | Spawn group | `gamjee_oc` |
    | Loot table | `gamjee_oc_dl` |
    | Conversation | `gamjee_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_cyclops:0` |
    | Defined in | `res/raw/monsterlist_feygard_1.json` |

    Raw data:

    ```json
    {
     "id": "gamjee_oc",
     "name": "Gamjee",
     "iconID": "monsters_cyclops:0",
     "maxHP": 417,
     "unique": 1,
     "monsterClass": "giant",
     "movementAggressionType": "none",
     "attackDamage": {
      "min": 10,
      "max": 13
     },
     "phraseID": "gamjee_selector",
     "droplistID": "gamjee_oc_dl",
     "attackCost": 6,
     "attackChance": 70,
     "criticalSkill": 15,
     "criticalMultiplier": 2.0,
     "blockChance": 101,
     "damageResistance": 13,
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "concussion",
        "magnitude": 1,
        "duration": 2,
        "chance": "5"
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "soaked_vision",
        "magnitude": 1,
        "duration": 2,
        "chance": "30"
       }
      ]
     }
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gamjee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gamjee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gamjee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gamjee.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
