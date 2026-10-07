---
description: "Feygard patrol watch is an NPC who can also be fought in Andor's Trail, found in Foaming Flask Tavern, Pub."
---

# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Feygard patrol watch

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Foaming Flask Tavern, Pub |
| **Class** | Humanoid |
| **HP** | 80 |
| **XP when defeated** | 133–280 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Feygard patrol watch. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, location, combat statistics, loot or shop stock. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`feygard_patrol_watch`](#v-feygard_patrol_watch) | NPC/Enemy | Foaming Flask Tavern: [road1](../maps/road1.md#pin-npc-feygard_patrol_watch) | – | 80 |
| [`ratdom_ff_guard`](#v-ratdom_ff_guard) | NPC/Enemy | Pub: [ratdom_maze_412](../maps/ratdom_maze_412.md#pin-npc-ratdom_ff_guard) | – | 80 |

## Foaming Flask Tavern, Road1 (feygard_patrol_watch) { #v-feygard_patrol_watch }

**Entry ID:** `feygard_patrol_watch` · **Type:** NPC/Enemy

**Location:** Foaming Flask Tavern: [road1](../maps/road1.md#pin-npc-feygard_patrol_watch)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 80 |
| XP when defeated | 133 |
| Damage | 2 to 7 |
| Attack chance | 70 |
| Block chance | 80 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Feygard patrol ring](../items/ffguard_qitem.md) | 100% | 1 |
| [Small empty vial](../items/vial_empty1.md) | 100% | 1 |
| [Wooden buckler](../items/shield1.md) | 100% | 1 |
| [Iron sword](../items/ironsword1.md) | 100% | 1 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [road1](../maps/road1.md) | Foaming Flask Tavern | 1 | – |

### Quests

- [Spies in the foam](../quests/jolnor.md): stages 20, 21

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Feygard patrol watch. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ff_outsideguard_select.json" data-npc="Feygard patrol watch" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (26 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-feygard_patrol_watch-ff_outsideguard_select"></span>**`ff_outsideguard_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Spies in the foam](../quests/jolnor.md#stage-20))* → [ff_outsideguard_trouble_24](#d-feygard_patrol_watch-ff_outsideguard_trouble_24)
    - branch 2 → [ff_outsideguard_1](#d-feygard_patrol_watch-ff_outsideguard_1)

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_24"></span>**`ff_outsideguard_trouble_24`** Feygard patrol watch: “I will go inside in a minute. Will you stand watch while I go inside?” — **effects:** sets stage 20 of [Spies in the foam](../quests/jolnor.md#stage-20)

    - “Sure, I will do that.” → [ff_outsideguard_trouble_25](#d-feygard_patrol_watch-ff_outsideguard_trouble_25)
    - “[Lie] Sure, I will do that.” → [ff_outsideguard_trouble_25](#d-feygard_patrol_watch-ff_outsideguard_trouble_25)

    <span id="d-feygard_patrol_watch-ff_outsideguard_1"></span>**`ff_outsideguard_1`** Feygard patrol watch: “Hello there. Should you be here? This is a tavern, you know. The Foaming Flask, to be precise.”

    - “Who are you?” → [ff_outsideguard_2](#d-feygard_patrol_watch-ff_outsideguard_2)

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_25"></span>**`ff_outsideguard_trouble_25`** Feygard patrol watch: “Thanks a lot my friend.”


    <span id="d-feygard_patrol_watch-ff_outsideguard_2"></span>**`ff_outsideguard_2`** Feygard patrol watch: “I am a member of the royal guard patrol from Feygard.”

    - “Feygard, where is that?” → [ff_outsideguard_3](#d-feygard_patrol_watch-ff_outsideguard_3)
    - “What do you do around here?” → [ff_outsideguard_3](#d-feygard_patrol_watch-ff_outsideguard_3)

    <span id="d-feygard_patrol_watch-ff_outsideguard_3"></span>**`ff_outsideguard_3`** Feygard patrol watch: “Go talk to the captain inside if you want to talk. I must stay alert on my post.”

    - “OK. Goodbye.” → *conversation ends*
    - “Why must you stay alert outside a tavern?” *(if reached stage 10 of [Spies in the foam](../quests/jolnor.md#stage-10))* → [ff_outsideguard_trouble_1](#d-feygard_patrol_watch-ff_outsideguard_trouble_1)

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_1"></span>**`ff_outsideguard_trouble_1`** Feygard patrol watch: “Really, I cannot talk to you. I could get into trouble.”

    - “OK. I won't bother you anymore. Shadow be with you.” → [ff_outsideguard_shadow_1](#d-feygard_patrol_watch-ff_outsideguard_shadow_1)
    - “OK. I won't bother you anymore. Goodbye.” → *conversation ends*
    - “What trouble?” → [ff_outsideguard_trouble_2](#d-feygard_patrol_watch-ff_outsideguard_trouble_2)

    <span id="d-feygard_patrol_watch-ff_outsideguard_shadow_1"></span>**`ff_outsideguard_shadow_1`** Feygard patrol watch: “Shadow? How curious that you would mention that. Explain yourself!”

    - “I did not mean a thing by it. Never mind I said anything.” → [ff_outsideguard_shadow_2](#d-feygard_patrol_watch-ff_outsideguard_shadow_2)
    - “The Shadow watches over us when we sleep.” → [ff_outsideguard_shadow_3](#d-feygard_patrol_watch-ff_outsideguard_shadow_3)

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_2"></span>**`ff_outsideguard_trouble_2`** Feygard patrol watch: “No really, the captain might see me. I must be aware on my post at all times. *sigh*”

    - “OK. I won't bother you anymore. Shadow be with you.” → [ff_outsideguard_shadow_1](#d-feygard_patrol_watch-ff_outsideguard_shadow_1)
    - “OK. I won't bother you anymore. Goodbye.” → *conversation ends*
    - “Do you like your job here?” → [ff_outsideguard_trouble_3](#d-feygard_patrol_watch-ff_outsideguard_trouble_3)

    <span id="d-feygard_patrol_watch-ff_outsideguard_shadow_2"></span>**`ff_outsideguard_shadow_2`** Feygard patrol watch: “Good. Now be gone before I will have to deal with you.”


    <span id="d-feygard_patrol_watch-ff_outsideguard_shadow_3"></span>**`ff_outsideguard_shadow_3`** Feygard patrol watch: “What? Are you one of those troublemakers sent here to sabotage our mission?”

    - “The Shadow protects us.” → [ff_outsideguard_shadow_4](#d-feygard_patrol_watch-ff_outsideguard_shadow_4)
    - “Fine. I better not start a fight with the royal guard.” → *conversation ends*

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_3"></span>**`ff_outsideguard_trouble_3`** Feygard patrol watch: “My job? I guess the royal guard is OK. I mean, Feygard is a really nice place to live in.”

    - Next → [ff_outsideguard_trouble_4](#d-feygard_patrol_watch-ff_outsideguard_trouble_4)

    <span id="d-feygard_patrol_watch-ff_outsideguard_shadow_4"></span>**`ff_outsideguard_shadow_4`** Feygard patrol watch: “That does it. You better fight or flee right now kid.”

    - “Good. I have been waiting for a fight!” → [ff_outsideguard_shadow_5](#d-feygard_patrol_watch-ff_outsideguard_shadow_5)
    - “For the Shadow!” → [ff_outsideguard_shadow_5](#d-feygard_patrol_watch-ff_outsideguard_shadow_5)
    - “Never mind. I was just kidding with you.” → [ff_outsideguard_shadow_2](#d-feygard_patrol_watch-ff_outsideguard_shadow_2)

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_4"></span>**`ff_outsideguard_trouble_4`** Feygard patrol watch: “Standing guard on duty out here in the middle of nowhere is not really what I signed up for.”

    - “I bet. This place is really boring.” → [ff_outsideguard_trouble_5](#d-feygard_patrol_watch-ff_outsideguard_trouble_5)
    - “You must get tired of just standing here also.” → [ff_outsideguard_trouble_5](#d-feygard_patrol_watch-ff_outsideguard_trouble_5)

    <span id="d-feygard_patrol_watch-ff_outsideguard_shadow_5"></span>**`ff_outsideguard_shadow_5`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 21 of [Spies in the foam](../quests/jolnor.md#stage-21)

    - branch 1 → *fight starts*

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_5"></span>**`ff_outsideguard_trouble_5`** Feygard patrol watch: “Yeah I know. I would rather be inside in the tavern drinking like the senior officers and the captain. How come I have to stand out here?”

    - “At least the Shadow watches over you.” → [ff_outsideguard_shadow_1](#d-feygard_patrol_watch-ff_outsideguard_shadow_1)
    - “Why not just leave if it's not what you want to do?” → [ff_outsideguard_trouble_7](#d-feygard_patrol_watch-ff_outsideguard_trouble_7)
    - “The greater cause of the royal guard, to keep the peace, is worth it in the long run.” → [ff_outsideguard_trouble_6](#d-feygard_patrol_watch-ff_outsideguard_trouble_6)

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_7"></span>**`ff_outsideguard_trouble_7`** Feygard patrol watch: “No, my loyalty is to Feygard. If I would leave, I would also leave my loyalty behind.”

    - “What does that mean if you are not satisfied with what you do?” → [ff_outsideguard_trouble_9](#d-feygard_patrol_watch-ff_outsideguard_trouble_9)
    - “Yes, that sounds right. Feygard sounds like a nice place from what I have heard.” → [ff_outsideguard_trouble_6](#d-feygard_patrol_watch-ff_outsideguard_trouble_6)

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_6"></span>**`ff_outsideguard_trouble_6`** Feygard patrol watch: “Yes, you are right of course. Our duty is to Feygard and to keep the peace from all that want to disrupt it.”

    - “Yes. The Shadow will not look favorably upon those that disrupt the peace.” → [ff_outsideguard_shadow_1](#d-feygard_patrol_watch-ff_outsideguard_shadow_1)
    - “Yes. The troublemakers should be punished.” → [ff_outsideguard_trouble_8](#d-feygard_patrol_watch-ff_outsideguard_trouble_8)

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_9"></span>**`ff_outsideguard_trouble_9`** Feygard patrol watch: “Well, I am convinced that we must follow the laws laid down by our rulers. If we don't obey the law, what are we left with?”

    - Next → [ff_outsideguard_trouble_10](#d-feygard_patrol_watch-ff_outsideguard_trouble_10)

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_8"></span>**`ff_outsideguard_trouble_8`** Feygard patrol watch: “Right. I like you, kid. Tell you what, I could put in a good word for you in the barracks when we get back to Feygard if you want.”

    - “Sure, that sounds good to me.” → [ff_outsideguard_trouble_20](#d-feygard_patrol_watch-ff_outsideguard_trouble_20)
    - “No thanks. I have enough to do already.” → [ff_outsideguard_trouble_20](#d-feygard_patrol_watch-ff_outsideguard_trouble_20)

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_10"></span>**`ff_outsideguard_trouble_10`** Feygard patrol watch: “Chaos. Disorder. No, I prefer the lawful way of Feygard. My loyalty is firm.”

    - “Sounds good to me. Laws are made to be followed.” → [ff_outsideguard_trouble_8](#d-feygard_patrol_watch-ff_outsideguard_trouble_8)
    - “I do not agree. We should follow our heart, even if that goes against the rules.” → [ff_outsideguard_trouble_12](#d-feygard_patrol_watch-ff_outsideguard_trouble_12)

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_20"></span>**`ff_outsideguard_trouble_20`** Feygard patrol watch: “Was there anything else you wanted?”

    - “I was wondering about why you stand guard here.” → [ff_outsideguard_trouble_21](#d-feygard_patrol_watch-ff_outsideguard_trouble_21)

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_12"></span>**`ff_outsideguard_trouble_12`** Feygard patrol watch: “That troubles me. We might see each other again in the future. But then we might not be able to have this kind of civil discussion.”


    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_21"></span>**`ff_outsideguard_trouble_21`** Feygard patrol watch: “Right, we went over this before. As I said, I would rather be inside by the fire.”

    - “I could spot for you if you want to go inside.” → [ff_outsideguard_trouble_23](#d-feygard_patrol_watch-ff_outsideguard_trouble_23)
    - “Tough luck. I guess you are left out here, while your captain and buddies are inside.” → [ff_outsideguard_trouble_22](#d-feygard_patrol_watch-ff_outsideguard_trouble_22)

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_23"></span>**`ff_outsideguard_trouble_23`** Feygard patrol watch: “Really? Yes that would be great. Then I can at least get something to eat and a bit of warmth from the fire.”

    - Next → [ff_outsideguard_trouble_24](#d-feygard_patrol_watch-ff_outsideguard_trouble_24)

    <span id="d-feygard_patrol_watch-ff_outsideguard_trouble_22"></span>**`ff_outsideguard_trouble_22`** Feygard patrol watch: “Yeah, that's just my luck.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 5 lines changed<br>· text: “My job? I guess the royal guard is ok. I mean, Feygard is a really ni…” → “My job? I guess the royal guard is OK. I mean, Feygard is a really ni…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (feygard_patrol_watch)"

    | | |
    |---|---|
    | Entry ID | `feygard_patrol_watch` |
    | Spawn group | `ff_outsideguard` |
    | Loot table | `ff_outsideguard` |
    | Conversation | `ff_outsideguard_select` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_v068_npcs.json` |

    Raw data:

    ```json
    {
     "id": "feygard_patrol_watch",
     "name": "Feygard patrol watch",
     "iconID": "monsters_rltiles3:14",
     "maxHP": 80,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 2,
      "max": 7
     },
     "spawnGroup": "ff_outsideguard",
     "phraseID": "ff_outsideguard_select",
     "droplistID": "ff_outsideguard",
     "attackCost": 5,
     "attackChance": 70,
     "blockChance": 80,
     "damageResistance": 3
    }
    ```


## Pub, Ratdom maze 412 (ratdom_ff_guard) { #v-ratdom_ff_guard }

**Entry ID:** `ratdom_ff_guard` · **Type:** NPC/Enemy

**Location:** Pub: [ratdom_maze_412](../maps/ratdom_maze_412.md#pin-npc-ratdom_ff_guard)

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 80 |
| XP when defeated | 280 |
| Damage | 12 to 17 |
| Attack chance | 170 |
| Block chance | 180 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 5 AP |
| Attacks per turn | 2 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

### Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 2 to 9 |

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [ratdom_maze_412](../maps/ratdom_maze_412.md) | Pub | 1 | – |

### Quests that count defeats

- [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-173) with walking into a blocked passage on [ratdom_maze_412](../maps/ratdom_maze_412.md) checks that this enemy has been defeated.

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Feygard patrol watch. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_ff_guard.json" data-npc="Feygard patrol watch" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ratdom_ff_guard-ratdom_ff_guard"></span>**`ratdom_ff_guard`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Spies in the foam](../quests/jolnor.md#stage-20))* → [ratdom_ff_guard_20](#d-ratdom_ff_guard-ratdom_ff_guard_20)
    - branch 2 → [ratdom_ff_guard_10](#d-ratdom_ff_guard-ratdom_ff_guard_10)

    <span id="d-ratdom_ff_guard-ratdom_ff_guard_20"></span>**`ratdom_ff_guard_20`** Feygard patrol watch: “Hey, you!”

    - “Who, me?” → [ratdom_ff_guard_30](#d-ratdom_ff_guard-ratdom_ff_guard_30)
    - “Hey, you!” → [ratdom_ff_guard_30](#d-ratdom_ff_guard-ratdom_ff_guard_30)

    <span id="d-ratdom_ff_guard-ratdom_ff_guard_10"></span>**`ratdom_ff_guard_10`** Feygard patrol watch: “Go away!”


    <span id="d-ratdom_ff_guard-ratdom_ff_guard_30"></span>**`ratdom_ff_guard_30`** Feygard patrol watch: “I know your face!”

    - Next → [ratdom_ff_guard_40](#d-ratdom_ff_guard-ratdom_ff_guard_40)

    <span id="d-ratdom_ff_guard-ratdom_ff_guard_40"></span>**`ratdom_ff_guard_40`** Feygard patrol watch: “You had made me leave my post in front of the Foaming Flask!” — **effects:** removes monsters from road1

    - “Oh. It's you ...” → [ratdom_ff_guard_42](#d-ratdom_ff_guard-ratdom_ff_guard_42)

    <span id="d-ratdom_ff_guard-ratdom_ff_guard_42"></span>**`ratdom_ff_guard_42`** Feygard patrol watch: “Surprised? I'm sure you didn't think we'd see each other again.”

    - Next → [ratdom_ff_guard_50](#d-ratdom_ff_guard-ratdom_ff_guard_50)

    <span id="d-ratdom_ff_guard-ratdom_ff_guard_50"></span>**`ratdom_ff_guard_50`** Feygard patrol watch: “I have lost everything because of this! Above all, my honor!”

    - “What honor?” → [ratdom_ff_guard_60](#d-ratdom_ff_guard-ratdom_ff_guard_60)
    - “Sorry.” → [ratdom_ff_guard_60](#d-ratdom_ff_guard-ratdom_ff_guard_60)

    <span id="d-ratdom_ff_guard-ratdom_ff_guard_60"></span>**`ratdom_ff_guard_60`** Feygard patrol watch: “I took refuge in this filthy cave to be safe from the guards of Feygard.”

    - Next → [ratdom_ff_guard_70](#d-ratdom_ff_guard-ratdom_ff_guard_70)

    <span id="d-ratdom_ff_guard-ratdom_ff_guard_70"></span>**`ratdom_ff_guard_70`** Feygard patrol watch: “You will pay for it now!”

    - “But you were so stupid ...” → *fight starts*
    - “Attack!” → *fight starts*



### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 9 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_ff_guard)"

    | | |
    |---|---|
    | Entry ID | `ratdom_ff_guard` |
    | Spawn group | `ratdom_ff_guard` |
    | Loot table | `ratdom_ff_guard` |
    | Conversation | `ratdom_ff_guard` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_ff_guard",
     "name": "Feygard patrol watch",
     "iconID": "monsters_rltiles3:14",
     "maxHP": 80,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 12,
      "max": 17
     },
     "spawnGroup": "ratdom_ff_guard",
     "phraseID": "ratdom_ff_guard",
     "droplistID": "ratdom_ff_guard",
     "attackCost": 5,
     "attackChance": 170,
     "blockChance": 180,
     "damageResistance": 3
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol_watch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol_watch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol_watch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=feygard_patrol_watch.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
