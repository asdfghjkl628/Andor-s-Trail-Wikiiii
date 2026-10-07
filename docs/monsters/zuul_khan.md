---
description: "Zuul'khan is an NPC who can also be fought in Andor's Trail, found in bogsten4, mywildcave4, mushroom_m2_3, mushroom_m2_6, mushroom_m2_8, mushroom_m3_1. Teaches Spore poison immunity."
---

# ![](../assets/icons/monsters/monsters_rltiles2_88.png){ .sprite } Zuul'khan

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_88.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Role** | Teaches [Spore poison immunity](../skills/sporeImmunity.md) |
| **Found in** | bogsten4, mywildcave4, mushroom_m2_3, mushroom_m2_6, mushroom_m2_8, mushroom_m3_1 |
| **Class** | Humanoid |
| **HP** | 175 |
| **XP when defeated** | 214–266 |
| **Entries in game data** | 6 |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

!!! info "6 entries in the game data"
    The game's data files define 6 separate characters named Zuul'khan. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, combat statistics, loot or shop stock. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`zuul_khan`](#v-zuul_khan) | NPC/Enemy | [bogsten4](../maps/bogsten4.md#pin-npc-zuul_khan) | teaches [Spore poison immunity](../skills/sporeImmunity.md) | 175 |
| [`gison_thiefboss`](#v-gison_thiefboss) | NPC/Enemy | [mywildcave4](../maps/mywildcave4.md#pin-npc-gison_thiefboss) | – | 175 |
| [`zuul_khan2`](#v-zuul_khan2) | NPC/Enemy | [mushroom_m2_3](../maps/mushroom_m2_3.md#pin-npc-zuul_khan2) | – | 175 |
| [`zuul_khan3`](#v-zuul_khan3) | NPC/Enemy | [mushroom_m2_6](../maps/mushroom_m2_6.md#pin-npc-zuul_khan3) | – | 175 |
| [`zuul_khan4`](#v-zuul_khan4) | NPC/Enemy | [mushroom_m2_8](../maps/mushroom_m2_8.md#pin-npc-zuul_khan4) | – | 175 |
| [`zuul_khan9`](#v-zuul_khan9) | NPC/Enemy | [mushroom_m3_1](../maps/mushroom_m3_1.md#pin-npc-zuul_khan9) | – | 175 |

## Bogsten4 (zuul_khan) { #v-zuul_khan }

**Entry ID:** `zuul_khan` · **Type:** NPC/Enemy · **Role:** Teaches [Spore poison immunity](../skills/sporeImmunity.md)

**Location:** [bogsten4](../maps/bogsten4.md#pin-npc-zuul_khan)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 175 |
| XP when defeated | 214 |
| Damage | 3 to 6 |
| Attack chance | 110 |
| Block chance | 40 |
| Damage resistance | 0 |
| Max AP | 20 |
| Attack cost | 5 AP |
| Attacks per turn | 4 |
| Move cost | 6 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 1 to 10 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [bogsten4](../maps/bogsten4.md) | – | 1 | – |

### Quests that count defeats

- [Fungi panic](../quests/fungi_panic.md#stage-90) with stepping on a trigger on [bogsten4](../maps/bogsten4.md) checks that this enemy has been defeated.
- A conversation with [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) checks that this enemy has been defeated.
- [Fungi panic](../quests/fungi_panic.md#stage-161) with [Black fog](../monsters/zuul_khan1_blocker.md) ([bogsten4](../maps/bogsten4.md)) checks that this enemy has been defeated.

### Quests

- [Fungi panic](../quests/fungi_panic.md): stages 70, 72, 80, 115, 135, 150, 155

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Zuul'khan. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/zuul_khan.json" data-npc="Zuul&#x27;khan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (46 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-zuul_khan-zuul_khan"></span>**`zuul_khan`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 155 of [Fungi panic](../quests/fungi_panic.md#stage-155))* → [zuul_khan_155](#d-zuul_khan-zuul_khan_155)
    - branch 2 *(if reached stage 150 of [Fungi panic](../quests/fungi_panic.md#stage-150))* → [zuul_khan_150](#d-zuul_khan-zuul_khan_150)
    - branch 3 *(if carry 1× [Bogsten's staff](../items/bogsten_staff.md))* → [zuul_khan_115_10](#d-zuul_khan-zuul_khan_115_10)
    - branch 4 *(if wearing [Bogsten's staff](../items/bogsten_staff.md))* → [zuul_khan_115_10](#d-zuul_khan-zuul_khan_115_10)
    - branch 5 *(if reached stage 115 of [Fungi panic](../quests/fungi_panic.md#stage-115))* → [zuul_khan_115](#d-zuul_khan-zuul_khan_115)
    - branch 6 *(if reached stage 70 of [Fungi panic](../quests/fungi_panic.md#stage-70))* → [zuul_khan_70](#d-zuul_khan-zuul_khan_70)
    - branch 7 → [zuul_khan_10](#d-zuul_khan-zuul_khan_10)

    <span id="d-zuul_khan-zuul_khan_155"></span>**`zuul_khan_155`** Zuul'khan: “Don't disturb me! I am practicing dangerous spells.”


    <span id="d-zuul_khan-zuul_khan_150"></span>**`zuul_khan_150`** [Dummy NPC](../monsters/none.md): “Zuul'khan towers over you and starts muttering strange words.”

    - “I'm feeling dizzy...” → [zuul_khan_150_10](#d-zuul_khan-zuul_khan_150_10)

    <span id="d-zuul_khan-zuul_khan_115_10"></span>**`zuul_khan_115_10`** Zuul'khan: “Bogsten is dead. Finally.”

    - “Yes. Now where is my reward?” → [zuul_khan_115_20](#d-zuul_khan-zuul_khan_115_20)

    <span id="d-zuul_khan-zuul_khan_115"></span>**`zuul_khan_115`** Zuul'khan: “Is Bogsten dead already?”

    - “No, not yet.” → *conversation ends*
    - “I have killed him.” *(if killed 1× [Bogsten](../monsters/bogsten.md))* → [zuul_khan_115_10](#d-zuul_khan-zuul_khan_115_10)

    <span id="d-zuul_khan-zuul_khan_70"></span>**`zuul_khan_70`** Zuul'khan: “I see that you have their family necklace. So you must die now.”

    - “I'll have to thank Bogsten: This sounds like a fun fight.” → [zuul_khan_70_24](#d-zuul_khan-zuul_khan_70_24)
    - “You shouldn't kill me. I could be of use.” → [zuul_khan_70_84](#d-zuul_khan-zuul_khan_70_84)
    - “Please. I will crawl before you. Don't hurt me.” → [zuul_khan_70_82](#d-zuul_khan-zuul_khan_70_82)

    <span id="d-zuul_khan-zuul_khan_10"></span>**`zuul_khan_10`** Zuul'khan: “Oh kid, you look like someone nice. I don't want you to be injured because of me. I urge you to leave!”

    - “What's going on?” → [zuul_khan_12](#d-zuul_khan-zuul_khan_12)

    <span id="d-zuul_khan-zuul_khan_150_10"></span>**`zuul_khan_150_10`** [Zuul'khan](../monsters/zuul_khan.md): “Done. You will never fear any of these fungi spores anymore.” — **effects:** sets stage 155 of [Fungi panic](../quests/fungi_panic.md#stage-155), applies condition spore_poison, +1 [Spore poison immunity](../skills/sporeImmunity.md)

    - “Oh wow.” → [zuul_khan_150_20](#d-zuul_khan-zuul_khan_150_20)

    <span id="d-zuul_khan-zuul_khan_115_20"></span>**`zuul_khan_115_20`** Zuul'khan: “Give me the staff first.”

    - “Here it is.” *(if hand over 1× [Bogsten's staff](../items/bogsten_staff.md))* → [zuul_khan_115_50](#d-zuul_khan-zuul_khan_115_50)
    - “Here it is.” *(if wearing (and give up) [Bogsten's staff](../items/bogsten_staff.md))* → [zuul_khan_115_50](#d-zuul_khan-zuul_khan_115_50)
    - “No, I have changed my mind. I'll rather keep Bogsten's staff.” → [zuul_khan_115_22](#d-zuul_khan-zuul_khan_115_22)

    <span id="d-zuul_khan-zuul_khan_70_24"></span>**`zuul_khan_70_24`** Zuul'khan: “Then our little conversation is over now.”

    - “Attack!” → [zuul_khan_70_30](#d-zuul_khan-zuul_khan_70_30)
    - “Hm, wait. Let me think again.” → [zuul_khan_70_20](#d-zuul_khan-zuul_khan_70_20)
    - “I wish we could talk a little more.” → [zuul_khan_50](#d-zuul_khan-zuul_khan_50)

    <span id="d-zuul_khan-zuul_khan_70_84"></span>**`zuul_khan_70_84`** Zuul'khan: “Hmm. Maybe.”

    - Next → [zuul_khan_70_20](#d-zuul_khan-zuul_khan_70_20)

    <span id="d-zuul_khan-zuul_khan_70_82"></span>**`zuul_khan_70_82`** Zuul'khan: “Disgusting. Away with you!”


    <span id="d-zuul_khan-zuul_khan_12"></span>**`zuul_khan_12`** Zuul'khan: “Give me your hand! ... No don't! ... Give me ...”

    - Next → [zuul_khan_14](#d-zuul_khan-zuul_khan_14)

    <span id="d-zuul_khan-zuul_khan_150_20"></span>**`zuul_khan_150_20`** Zuul'khan: “Leave me now! I have to regain my practice of spells.”


    <span id="d-zuul_khan-zuul_khan_115_50"></span>**`zuul_khan_115_50`** Zuul'khan: “Finally I got the staff back!” — **effects:** sets stage 150 of [Fungi panic](../quests/fungi_panic.md#stage-150)

    - “My reward...?” → [zuul_khan_150](#d-zuul_khan-zuul_khan_150)

    <span id="d-zuul_khan-zuul_khan_115_22"></span>**`zuul_khan_115_22`** Zuul'khan: “You won't betray me, you little fool!”

    - “Who is betraying here? Where is my dearly earned reward!” → [zuul_khan_115_20](#d-zuul_khan-zuul_khan_115_20)
    - “Little in height - but strong! Attack!” → [zuul_khan_115_24](#d-zuul_khan-zuul_khan_115_24)

    <span id="d-zuul_khan-zuul_khan_70_30"></span>**`zuul_khan_70_30`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 80 of [Fungi panic](../quests/fungi_panic.md#stage-80)

    - branch 1 → *fight starts*

    <span id="d-zuul_khan-zuul_khan_70_20"></span>**`zuul_khan_70_20`** Zuul'khan: “Go and kill Bogsten up there.”

    - Next → [zuul_khan_70_22](#d-zuul_khan-zuul_khan_70_22)

    <span id="d-zuul_khan-zuul_khan_50"></span>**`zuul_khan_50`** Zuul'khan: “You may have a last wish. What do you want?”

    - “Tell me why you are here in Bogsten's caves?” → [zuul_khan_60](#d-zuul_khan-zuul_khan_60)

    <span id="d-zuul_khan-zuul_khan_14"></span>**`zuul_khan_14`** Zuul'khan: “I'm hurt ... I'll hurt ... Never do! ... Help! ... Kill! ... your hand - pleease ...”

    - “* Reach out your hand *” → [zuul_khan_20](#d-zuul_khan-zuul_khan_20)
    - “Attack!” → [zuul_khan_16](#d-zuul_khan-zuul_khan_16)
    - “I better go.” → *conversation ends*

    <span id="d-zuul_khan-zuul_khan_115_24"></span>**`zuul_khan_115_24`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 135 of [Fungi panic](../quests/fungi_panic.md#stage-135)

    - branch 1 → *fight starts*

    <span id="d-zuul_khan-zuul_khan_70_22"></span>**`zuul_khan_70_22`** Zuul'khan: “Kill Bogsten and bring me his staff as evidence.” — **effects:** sets stage 72 of [Fungi panic](../quests/fungi_panic.md#stage-72)

    - “What would I gain from this?” → [zuul_khan_70_40](#d-zuul_khan-zuul_khan_70_40)
    - “No. I'd rather kill you.” → [zuul_khan_70_24](#d-zuul_khan-zuul_khan_70_24)

    <span id="d-zuul_khan-zuul_khan_60"></span>**`zuul_khan_60`** Zuul'khan: “Bogsten's cave? Oh how I hate that name!”

    - Next → [zuul_khan_60_20](#d-zuul_khan-zuul_khan_60_20)

    <span id="d-zuul_khan-zuul_khan_20"></span>**`zuul_khan_20`** Zuul'khan: “Hahaha! AHAHAHAHA! I am free again!”

    - “Who are you?” → [zuul_khan_30](#d-zuul_khan-zuul_khan_30)
    - “What are you?” → [zuul_khan_22](#d-zuul_khan-zuul_khan_22)

    <span id="d-zuul_khan-zuul_khan_16"></span>**`zuul_khan_16`** Zuul'khan: “No! Don't do me wrong!”

    - Next → [zuul_khan_12](#d-zuul_khan-zuul_khan_12)

    <span id="d-zuul_khan-zuul_khan_70_40"></span>**`zuul_khan_70_40`** Zuul'khan: “Ah. You are not as stupid as you look, kid.”

    - Next → [zuul_khan_70_42](#d-zuul_khan-zuul_khan_70_42)

    <span id="d-zuul_khan-zuul_khan_60_20"></span>**`zuul_khan_60_20`** Zuul'khan: “It was the Bogstens who imprisoned me here, long years ago. With a petrifying spell. I did nothing evil to them, except ... Well, I did almost nothing evil to them.”

    - Next → [zuul_khan_60_30](#d-zuul_khan-zuul_khan_60_30)

    <span id="d-zuul_khan-zuul_khan_30"></span>**`zuul_khan_30`** Zuul'khan: “I am the Archmancer of the underground. Widely known as Master of the Fungi and Commander to anything that crawls.”

    - Next → [zuul_khan_32](#d-zuul_khan-zuul_khan_32)

    <span id="d-zuul_khan-zuul_khan_22"></span>**`zuul_khan_22`** Zuul'khan: “Be nice, kid.”

    - “OK. Who are you?” → [zuul_khan_30](#d-zuul_khan-zuul_khan_30)

    <span id="d-zuul_khan-zuul_khan_70_42"></span>**`zuul_khan_70_42`** Zuul'khan: “I'll give you two things.”

    - Next → [zuul_khan_70_44](#d-zuul_khan-zuul_khan_70_44)

    <span id="d-zuul_khan-zuul_khan_60_30"></span>**`zuul_khan_60_30`** Zuul'khan: “More than a century ago, I found the way to command the crawling species of the underground and to bend the fungi to my will.”

    - Next → [zuul_khan_60_40](#d-zuul_khan-zuul_khan_60_40)

    <span id="d-zuul_khan-zuul_khan_32"></span>**`zuul_khan_32`** Zuul'khan: “I am the great Zuul'khan!”

    - “Great.” → [zuul_khan_34](#d-zuul_khan-zuul_khan_34)

    <span id="d-zuul_khan-zuul_khan_70_44"></span>**`zuul_khan_70_44`** Zuul'khan: “I'll spare your life.”

    - “Generously.” → [zuul_khan_70_46](#d-zuul_khan-zuul_khan_70_46)

    <span id="d-zuul_khan-zuul_khan_60_40"></span>**`zuul_khan_60_40`** Zuul'khan: “I chose this place to practice my arts and prepare an army of Fungi.”

    - Next → [zuul_khan_60_50](#d-zuul_khan-zuul_khan_60_50)

    <span id="d-zuul_khan-zuul_khan_34"></span>**`zuul_khan_34`** Zuul'khan: “Great and strong, yes.”

    - “Aha.” → [zuul_khan_40](#d-zuul_khan-zuul_khan_40)

    <span id="d-zuul_khan-zuul_khan_70_46"></span>**`zuul_khan_70_46`** Zuul'khan: “And I'll provide you with a permanent immunity to the spore poison.”

    - “Agreed. I'll go upstairs and finish Bogsten.” → [zuul_khan_70_50](#d-zuul_khan-zuul_khan_70_50)
    - “Forget it. Attack!” → [zuul_khan_70_30](#d-zuul_khan-zuul_khan_70_30)

    <span id="d-zuul_khan-zuul_khan_60_50"></span>**`zuul_khan_60_50`** Zuul'khan: “The Bogstens must have heard about my activities in the caves under their house and became suspicious.”

    - Next → [zuul_khan_60_60](#d-zuul_khan-zuul_khan_60_60)

    <span id="d-zuul_khan-zuul_khan_40"></span>**`zuul_khan_40`** Zuul'khan: “You are the first human I've seen in such a long time.”

    - Next → [zuul_khan_42](#d-zuul_khan-zuul_khan_42)

    <span id="d-zuul_khan-zuul_khan_70_50"></span>**`zuul_khan_70_50`** Zuul'khan: “Do so.” — **effects:** sets stage 115 of [Fungi panic](../quests/fungi_panic.md#stage-115)


    <span id="d-zuul_khan-zuul_khan_60_60"></span>**`zuul_khan_60_60`** Zuul'khan: “Lotho Bogsten sneaked down here and caught me unawares.”

    - Next → [zuul_khan_60_70](#d-zuul_khan-zuul_khan_60_70)

    <span id="d-zuul_khan-zuul_khan_42"></span>**`zuul_khan_42`** Zuul'khan: “And I am the last human you will ever see.”

    - “You threaten me?” → [zuul_khan_50](#d-zuul_khan-zuul_khan_50)

    <span id="d-zuul_khan-zuul_khan_60_70"></span>**`zuul_khan_60_70`** Zuul'khan: “I didn't expect petrifying. Who would use such a weak spell that has to be renewed every few weeks?”

    - Next → [zuul_khan_60_80](#d-zuul_khan-zuul_khan_60_80)

    <span id="d-zuul_khan-zuul_khan_60_80"></span>**`zuul_khan_60_80`** Zuul'khan: “I could not move but I noticed everything that was happening around me. Lotho Bogsten visited me regularly and renewed the spell.”

    - Next → [zuul_khan_60_100](#d-zuul_khan-zuul_khan_60_100)

    <span id="d-zuul_khan-zuul_khan_60_100"></span>**`zuul_khan_60_100`** Zuul'khan: “Finally, after long, long years, Lotho Bogsten must have died. Fortunately, his son is not so dutiful.”

    - “He had children?” → [zuul_khan_60_120](#d-zuul_khan-zuul_khan_60_120)

    <span id="d-zuul_khan-zuul_khan_60_120"></span>**`zuul_khan_60_120`** Zuul'khan: “Indeed he had a son. But that lazybones didn't come as regularly as needed. The spell wore off, and I could move again.”

    - Next → [zuul_khan_60_140](#d-zuul_khan-zuul_khan_60_140)

    <span id="d-zuul_khan-zuul_khan_60_140"></span>**`zuul_khan_60_140`** Zuul'khan: “AHAHAHAHA!” — **effects:** sets stage 70 of [Fungi panic](../quests/fungi_panic.md#stage-70)

    - Next → [zuul_khan_70](#d-zuul_khan-zuul_khan_70)



### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 46 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (zuul_khan)"

    | | |
    |---|---|
    | Entry ID | `zuul_khan` |
    | Spawn group | `zuul_khan` |
    | Loot table | `zuul_khan` |
    | Conversation | `zuul_khan` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:88` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "zuul_khan",
     "name": "Zuul'khan",
     "iconID": "monsters_rltiles2:88",
     "maxHP": 175,
     "maxAP": 20,
     "moveCost": 6,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "zuul_khan",
     "phraseID": "zuul_khan",
     "droplistID": "zuul_khan",
     "attackCost": 5,
     "attackChance": 110,
     "blockChance": 40
    }
    ```


## Mywildcave4 (gison_thiefboss) { #v-gison_thiefboss }

**Entry ID:** `gison_thiefboss` · **Type:** NPC/Enemy

**Location:** [mywildcave4](../maps/mywildcave4.md#pin-npc-gison_thiefboss)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 175 |
| XP when defeated | 266 |
| Damage | 3 to 6 |
| Attack chance | 120 |
| Block chance | 60 |
| Damage resistance | 1 |
| Max AP | 20 |
| Attack cost | 5 AP |
| Attacks per turn | 4 |
| Move cost | 6 AP |
| Critical skill | 20 |
| Critical multiplier | 2.0 |
| Critical hit chance | 15% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mywildcave4](../maps/mywildcave4.md) | – | 1 | – |

### Quests that count defeats

- [Fungi panic](../quests/fungi_panic.md#stage-170) with [Black fog](../monsters/zuul_khan1_blocker.md#v-zuul_khan9_blocker) ([mushroom_m3_1](../maps/mushroom_m3_1.md)) checks that this enemy has been defeated.

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Zuul'khan. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/gison_thiefboss.json" data-npc="Zuul&#x27;khan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (5 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-gison_thiefboss-gison_thiefboss"></span>**`gison_thiefboss`** Zuul'khan: “[muttering ominous words]”

    - “Hi!” → [gison_thiefboss_10](#d-gison_thiefboss-gison_thiefboss_10)

    <span id="d-gison_thiefboss-gison_thiefboss_10"></span>**`gison_thiefboss_10`** Zuul'khan: “What ...? You again? How did you get in here?”

    - “I have come to retrieve a book that does not belong to you.” → [gison_thiefboss_20](#d-gison_thiefboss-gison_thiefboss_20)

    <span id="d-gison_thiefboss-gison_thiefboss_20"></span>**`gison_thiefboss_20`** Zuul'khan: “Ha! You made a serious error coming here. I have a use for you though.”

    - “You want me to help you?” → [gison_thiefboss_30](#d-gison_thiefboss-gison_thiefboss_30)

    <span id="d-gison_thiefboss-gison_thiefboss_30"></span>**`gison_thiefboss_30`** Zuul'khan: “Not exactly. My fungi leader is almost ready. It just needs to be fed some more to grow in strength.”

    - “Fed? On what?” → [gison_thiefboss_40](#d-gison_thiefboss-gison_thiefboss_40)

    <span id="d-gison_thiefboss-gison_thiefboss_40"></span>**`gison_thiefboss_40`** Zuul'khan: “One thing it likes is annoying children, like you. Thank you for volunteering!”

    - “Sorry, I don't think so. I will destroy you and your fungi leader!” → *fight starts*
    - “Sorry for disturbing you. I will leave immediately.” → *conversation ends*



### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 5 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (gison_thiefboss)"

    | | |
    |---|---|
    | Entry ID | `gison_thiefboss` |
    | Spawn group | `gison_thiefboss` |
    | Loot table | – |
    | Conversation | `gison_thiefboss` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:88` |
    | Defined in | `res/raw/monsterlist_gison.json` |

    Raw data:

    ```json
    {
     "id": "gison_thiefboss",
     "name": "Zuul'khan",
     "iconID": "monsters_rltiles2:88",
     "maxHP": 175,
     "maxAP": 20,
     "moveCost": 6,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "gison_thiefboss",
     "phraseID": "gison_thiefboss",
     "attackCost": 5,
     "attackChance": 120,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 60,
     "damageResistance": 1
    }
    ```


## Mushroom m2 3 (zuul_khan2) { #v-zuul_khan2 }

**Entry ID:** `zuul_khan2` · **Type:** NPC/Enemy

**Location:** [mushroom_m2_3](../maps/mushroom_m2_3.md#pin-npc-zuul_khan2)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 175 |
| XP when defeated | 214 |
| Damage | 3 to 6 |
| Attack chance | 110 |
| Block chance | 40 |
| Damage resistance | 0 |
| Max AP | 20 |
| Attack cost | 5 AP |
| Attacks per turn | 4 |
| Move cost | 6 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Insect wing](../items/insectwing.md) | 100% | 1 to 2 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mushroom_m2_3](../maps/mushroom_m2_3.md) | – | 1 | – |

### Quests that count defeats

- [Fungi panic](../quests/fungi_panic.md#stage-162) with [Black fog](../monsters/zuul_khan1_blocker.md#v-zuul_khan2_blocker) ([mushroom_m2_3](../maps/mushroom_m2_3.md)) checks that this enemy has been defeated.

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Zuul'khan. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/zuul_khan2.json" data-npc="Zuul&#x27;khan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (3 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-zuul_khan2-zuul_khan2"></span>**`zuul_khan2`** Zuul'khan: “You again! How did you get into here?”

    - “I could ask you the same.” → [zuul_khan2_10](#d-zuul_khan2-zuul_khan2_10)

    <span id="d-zuul_khan2-zuul_khan2_10"></span>**`zuul_khan2_10`** Zuul'khan: “Do not disturb me. I have to concentrate in building my fungi army.”

    - “By reading a book? Is reading a book the lazy way to create an army?” → [zuul_khan2_20](#d-zuul_khan2-zuul_khan2_20)

    <span id="d-zuul_khan2-zuul_khan2_20"></span>**`zuul_khan2_20`** Zuul'khan: “That did it. Silence now, or ...”

    - “Attack?” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 3 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (zuul_khan2)"

    | | |
    |---|---|
    | Entry ID | `zuul_khan2` |
    | Spawn group | `zuul_khan2` |
    | Loot table | `zuul_khan2` |
    | Conversation | `zuul_khan2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:88` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "zuul_khan2",
     "name": "Zuul'khan",
     "iconID": "monsters_rltiles2:88",
     "maxHP": 175,
     "maxAP": 20,
     "moveCost": 6,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "zuul_khan2",
     "phraseID": "zuul_khan2",
     "droplistID": "zuul_khan2",
     "attackCost": 5,
     "attackChance": 110,
     "blockChance": 40
    }
    ```


## Mushroom m2 6 (zuul_khan3) { #v-zuul_khan3 }

**Entry ID:** `zuul_khan3` · **Type:** NPC/Enemy

**Location:** [mushroom_m2_6](../maps/mushroom_m2_6.md#pin-npc-zuul_khan3)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 175 |
| XP when defeated | 214 |
| Damage | 3 to 6 |
| Attack chance | 110 |
| Block chance | 40 |
| Damage resistance | 0 |
| Max AP | 20 |
| Attack cost | 5 AP |
| Attacks per turn | 4 |
| Move cost | 6 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Claws](../items/claws.md) | 100% | 1 to 2 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mushroom_m2_6](../maps/mushroom_m2_6.md) | – | 1 | – |

### Quests that count defeats

- [Fungi panic](../quests/fungi_panic.md#stage-163) with [Black fog](../monsters/zuul_khan1_blocker.md#v-zuul_khan3_blocker) ([mushroom_m2_6](../maps/mushroom_m2_6.md)) checks that this enemy has been defeated.

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Zuul'khan. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/zuul_khan3.json" data-npc="Zuul&#x27;khan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-zuul_khan3-zuul_khan3"></span>**`zuul_khan3`** Zuul'khan: “You again!”

    - “Coocoo! Trying to read again?” → [zuul_khan3_10](#d-zuul_khan3-zuul_khan3_10)

    <span id="d-zuul_khan3-zuul_khan3_10"></span>**`zuul_khan3_10`** Zuul'khan: “Go away you annoying child! I must create the leader for my fungi army!”

    - “We'll see.” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (zuul_khan3)"

    | | |
    |---|---|
    | Entry ID | `zuul_khan3` |
    | Spawn group | `zuul_khan3` |
    | Loot table | `zuul_khan3` |
    | Conversation | `zuul_khan3` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:88` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "zuul_khan3",
     "name": "Zuul'khan",
     "iconID": "monsters_rltiles2:88",
     "maxHP": 175,
     "maxAP": 20,
     "moveCost": 6,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "zuul_khan3",
     "phraseID": "zuul_khan3",
     "droplistID": "zuul_khan3",
     "attackCost": 5,
     "attackChance": 110,
     "blockChance": 40
    }
    ```


## Mushroom m2 8 (zuul_khan4) { #v-zuul_khan4 }

**Entry ID:** `zuul_khan4` · **Type:** NPC/Enemy

**Location:** [mushroom_m2_8](../maps/mushroom_m2_8.md#pin-npc-zuul_khan4)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 175 |
| XP when defeated | 214 |
| Damage | 3 to 6 |
| Attack chance | 110 |
| Block chance | 40 |
| Damage resistance | 0 |
| Max AP | 20 |
| Attack cost | 5 AP |
| Attacks per turn | 4 |
| Move cost | 6 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Rat tail](../items/rat_tail.md) | 100% | 1 to 2 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mushroom_m2_8](../maps/mushroom_m2_8.md) | – | 1 | – |

### Quests that count defeats

- [Fungi panic](../quests/fungi_panic.md#stage-164) with [Black fog](../monsters/zuul_khan1_blocker.md#v-zuul_khan4_blocker) ([mushroom_m2_8](../maps/mushroom_m2_8.md)) checks that this enemy has been defeated.

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Zuul'khan. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/zuul_khan4.json" data-npc="Zuul&#x27;khan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (2 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-zuul_khan4-zuul_khan4"></span>**`zuul_khan4`** Zuul'khan: “I grow weary of you.”

    - “Why?” → [zuul_khan4_10](#d-zuul_khan4-zuul_khan4_10)

    <span id="d-zuul_khan4-zuul_khan4_10"></span>**`zuul_khan4_10`** Zuul'khan: “You interrupt my spells that will make my fungi leader invincible! Ha Ha! So now you must die!”

    - “Eh - no, I don't think so.” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 2 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (zuul_khan4)"

    | | |
    |---|---|
    | Entry ID | `zuul_khan4` |
    | Spawn group | `zuul_khan4` |
    | Loot table | `zuul_khan4` |
    | Conversation | `zuul_khan4` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:88` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "zuul_khan4",
     "name": "Zuul'khan",
     "iconID": "monsters_rltiles2:88",
     "maxHP": 175,
     "maxAP": 20,
     "moveCost": 6,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "zuul_khan4",
     "phraseID": "zuul_khan4",
     "droplistID": "zuul_khan4",
     "attackCost": 5,
     "attackChance": 110,
     "blockChance": 40
    }
    ```


## Mushroom m3 1 (zuul_khan9) { #v-zuul_khan9 }

**Entry ID:** `zuul_khan9` · **Type:** NPC/Enemy

**Location:** [mushroom_m3_1](../maps/mushroom_m3_1.md#pin-npc-zuul_khan9)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 175 |
| XP when defeated | 214 |
| Damage | 3 to 6 |
| Attack chance | 110 |
| Block chance | 40 |
| Damage resistance | 0 |
| Max AP | 20 |
| Attack cost | 5 AP |
| Attacks per turn | 4 |
| Move cost | 6 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Bone](../items/bone.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [mushroom_m3_1](../maps/mushroom_m3_1.md) | – | 1 | – |

### Quests that count defeats

- [Fungi panic](../quests/fungi_panic.md#stage-169) with [Black fog](../monsters/zuul_khan1_blocker.md#v-zuul_khan9_blocker) ([mushroom_m3_1](../maps/mushroom_m3_1.md)) checks that this enemy has been defeated.
- A conversation with [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) checks that this enemy has been defeated.
- A conversation with [Nimael](../monsters/nimael.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) checks that this enemy has been defeated.

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Zuul'khan. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/zuul_khan9.json" data-npc="Zuul&#x27;khan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (7 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-zuul_khan9-zuul_khan9"></span>**`zuul_khan9`** Zuul'khan: “You again! How did you get into here?”

    - “I could ask you the same.” → [zuul_khan9_10](#d-zuul_khan9-zuul_khan9_10)

    <span id="d-zuul_khan9-zuul_khan9_10"></span>**`zuul_khan9_10`** Zuul'khan: “May I finally practice my black magic in peace?”

    - “No, not if I can help it. By the way - your book looks strange.” → [zuul_khan9_20](#d-zuul_khan9-zuul_khan9_20)

    <span id="d-zuul_khan9-zuul_khan9_20"></span>**`zuul_khan9_20`** Zuul'khan: “What do you mean?”

    - “It is a cookbook. I see lots of delicious recipes.” → [zuul_khan9_30](#d-zuul_khan9-zuul_khan9_30)

    <span id="d-zuul_khan9-zuul_khan9_30"></span>**`zuul_khan9_30`** Zuul'khan: “Oh that. That's a good cover. I got the book from a 'friend'. In between there are recipes of a completely different kind.”

    - “You mean these strange letters next to the recipe of the Delicious Mushroom Soup?” → [zuul_khan9_40](#d-zuul_khan9-zuul_khan9_40)

    <span id="d-zuul_khan9-zuul_khan9_40"></span>**`zuul_khan9_40`** Zuul'khan: “Be glad that you can't decipher these letters. They are dangerous.”

    - Next → [zuul_khan9_42](#d-zuul_khan9-zuul_khan9_42)

    <span id="d-zuul_khan9-zuul_khan9_42"></span>**`zuul_khan9_42`** Zuul'khan: “It takes great power to tame these spells. My fungi leader grows in strength every day!”

    - “At school I was good at spelling: A B C ...” → [zuul_khan9_90](#d-zuul_khan9-zuul_khan9_90)

    <span id="d-zuul_khan9-zuul_khan9_90"></span>**`zuul_khan9_90`** Zuul'khan: “I've had enough of your cheekiness now. These were your last words!”

    - “We'll see...” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 7 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (zuul_khan9)"

    | | |
    |---|---|
    | Entry ID | `zuul_khan9` |
    | Spawn group | `zuul_khan9` |
    | Loot table | `zuul_khan9` |
    | Conversation | `zuul_khan9` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:88` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "zuul_khan9",
     "name": "Zuul'khan",
     "iconID": "monsters_rltiles2:88",
     "maxHP": 175,
     "maxAP": 20,
     "moveCost": 6,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 6
     },
     "spawnGroup": "zuul_khan9",
     "phraseID": "zuul_khan9",
     "droplistID": "zuul_khan9",
     "attackCost": 5,
     "attackChance": 110,
     "blockChance": 40
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
