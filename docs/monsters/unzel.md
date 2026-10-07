---
description: "Unzel is an NPC who can also be fought in Andor's Trail, found in Blackwater Mountain."
---

# ![](../assets/icons/monsters/monsters_men_8.png){ .sprite } Unzel

**Where to find Unzel:** Blackwater Mountain: [wild6](../maps/wild6.md#pin-npc-unzel)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_8.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Blackwater Mountain |
| **Class** | Humanoid |
| **HP** | 59 |
| **XP when defeated** | 93 |
| **Entry ID** | `unzel` |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 59 |
| XP when defeated | 93 |
| Damage | 5 to 9 |
| Attack chance | 80 |
| Block chance | 40 |
| Damage resistance | 2 |
| Max AP | 10 |
| Attack cost | 9 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 30 |
| Critical multiplier | 3.0 |
| Critical hit chance | 19% |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 16 to 30 |
| [Regular potion of health](../items/health.md) | 100% | 1 |
| [Unzel's ring](../items/ring_unzel.md) | 100% | 1 |
| [Unzel's defensive boots](../items/boots_unzel.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [wild6](../maps/wild6.md) | Blackwater Mountain | 1 | – |

## Quests

- [Missing pieces](../quests/vacor.md): stages 50, 51, 53, 61
- [Old friends?](../quests/kaverin.md): stage 30

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Unzel. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/unzel.json" data-npc="Unzel" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (31 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-unzel"></span>**`unzel`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Old friends?](../quests/kaverin.md#stage-30))* → [unzel_msg_r0](#d-unzel_msg_r0)
    - branch 2 *(if reached stage 61 of [Missing pieces](../quests/vacor.md#stage-61))* → [unzel_40](#d-unzel_40)
    - branch 3 *(if reached stage 51 of [Missing pieces](../quests/vacor.md#stage-51))* → [unzel_return_1](#d-unzel_return_1)
    - branch 4 → [unzel_1](#d-unzel_1)

    <span id="d-unzel_msg_r0"></span>**`unzel_msg_r0`** Unzel: “Hello again. Thank you for your help with defeating Vacor and bringing me the message from Kaverin.”

    - Next → [unzel_msg5](#d-unzel_msg5)

    <span id="d-unzel_40"></span>**`unzel_40`** Unzel: “Thank you for your help. Now we are safe from Vacor's rift spell.”

    - “I have a message for you from Kaverin in Remgard.” *(if reached stage 25 of [Old friends?](../quests/kaverin.md#stage-25); carry 1× [Kaverin's sealed message](../items/kaverin_message.md))* → [unzel_msg1](#d-unzel_msg1)

    <span id="d-unzel_return_1"></span>**`unzel_return_1`** Unzel: “Welcome back. Did you talk to Vacor?”

    - “Yes, I have dealt with him.” *(if hand over 1× [Vacor's ring](../items/ring_vacor.md))* → [unzel_30](#d-unzel_30)
    - “No, not yet.” → *conversation ends*

    <span id="d-unzel_1"></span>**`unzel_1`** Unzel: “Hello. I'm Unzel.”

    - “Is this your camp?” → [unzel_2](#d-unzel_2)
    - “I am sent by Vacor to kill you.” *(if reached stage 40 of [Missing pieces](../quests/vacor.md#stage-40))* → [unzel_3](#d-unzel_3)

    <span id="d-unzel_msg5"></span>**`unzel_msg5`** Unzel: “Your help could prove more valuable than you might realize.”

    - Next → [unzel_msg6](#d-unzel_msg6)

    <span id="d-unzel_msg1"></span>**`unzel_msg1`** Unzel: “Kaverin, my old friend! It's good to hear that he is still alive. What is the message?”

    - “Here it is.” *(if hand over 1× [Kaverin's sealed message](../items/kaverin_message.md))* → [unzel_msg2](#d-unzel_msg2)

    <span id="d-unzel_30"></span>**`unzel_30`** Unzel: “You killed him? You have my thanks friend. Now we are safe from Vacor's rift spell. Here, take these coins for your help.” — **effects:** sets stage 61 of [Missing pieces](../quests/vacor.md#stage-61), gives [Gold coins](../items/gold.md)

    - “Shadow be with you.” → *conversation ends*
    - “Thank you.” → *conversation ends*

    <span id="d-unzel_2"></span>**`unzel_2`** Unzel: “Yes, this is my camp. Lovely place, isn't it?”

    - “Bye.” → *conversation ends*

    <span id="d-unzel_3"></span>**`unzel_3`** Unzel: “Vacor sent you huh? I guess I should have figured he would send someone sooner or later.”

    - Next → [unzel_4](#d-unzel_4)

    <span id="d-unzel_msg6"></span>**`unzel_msg6`** Unzel: “Say hello to my old friend Kaverin the next time you see him, will you?”


    <span id="d-unzel_msg2"></span>**`unzel_msg2`** Unzel: “Hmm, yes... Let's see... [Unzel opens the sealed message and reads it]” — **effects:** sets stage 30 of [Old friends?](../quests/kaverin.md#stage-30)

    - Next → [unzel_msg3](#d-unzel_msg3)

    <span id="d-unzel_4"></span>**`unzel_4`** Unzel: “Very well then. Kill me if you must, or allow me to tell you my side of the story.”

    - “Hah, I will enjoy killing you!” → [unzel_fight](#d-unzel_fight)
    - “I will listen to your story.” → [unzel_5](#d-unzel_5)

    <span id="d-unzel_msg3"></span>**`unzel_msg3`** Unzel: “Yes, this makes sense with what I have seen.”

    - Next → [unzel_msg4](#d-unzel_msg4)

    <span id="d-unzel_fight"></span>**`unzel_fight`** Unzel: “Very well, let's fight then.” — **effects:** sets stage 53 of [Missing pieces](../quests/vacor.md#stage-53)

    - “A fight it is!” → *fight starts*

    <span id="d-unzel_5"></span>**`unzel_5`** Unzel: “Thank you for listening.”

    - Next → [unzel_10](#d-unzel_10)

    <span id="d-unzel_msg4"></span>**`unzel_msg4`** Unzel: “Thank you for bringing it to me.”

    - Next → [unzel_msg5](#d-unzel_msg5)

    <span id="d-unzel_10"></span>**`unzel_10`** Unzel: “Vacor and I used to travel together, but he started to get obsessed with his spell making.”

    - Next → [unzel_11](#d-unzel_11)

    <span id="d-unzel_11"></span>**`unzel_11`** Unzel: “He even started to question the Shadow. I knew I had to do something to stop him!”

    - Next → [unzel_12](#d-unzel_12)

    <span id="d-unzel_12"></span>**`unzel_12`** Unzel: “I started questioning him about what he was up to, but he just wanted to keep on going.”

    - Next → [unzel_13](#d-unzel_13)

    <span id="d-unzel_13"></span>**`unzel_13`** Unzel: “After a while, he became obsessed with the thought of a rift spell. He said it would grant him unlimited powers against the Shadow.”

    - Next → [unzel_14](#d-unzel_14)

    <span id="d-unzel_14"></span>**`unzel_14`** Unzel: “So, there was only one thing I could do. I left him and needed to stop him from trying to create the rift spell.”

    - Next → [unzel_15](#d-unzel_15)

    <span id="d-unzel_15"></span>**`unzel_15`** Unzel: “I sent some friends to take the spell from him.”

    - Next → [unzel_16_select](#d-unzel_16_select)

    <span id="d-unzel_16_select"></span>**`unzel_16_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 50 of [Missing pieces](../quests/vacor.md#stage-50))* → [unzel_16_2](#d-unzel_16_2)
    - branch 2 → [unzel_16_1](#d-unzel_16_1)

    <span id="d-unzel_16_2"></span>**`unzel_16_2`** Unzel: “So, here we are.”

    - Next → [unzel_19](#d-unzel_19)

    <span id="d-unzel_16_1"></span>**`unzel_16_1`** Unzel: “So, here we are.”

    - “I killed the four bandits you sent after Vacor.” → [unzel_17](#d-unzel_17)

    <span id="d-unzel_19"></span>**`unzel_19`** Unzel: “Either you side with Vacor and his rift spell, or side with the Shadow, and help me get rid of him. Who will you help?” — **effects:** sets stage 50 of [Missing pieces](../quests/vacor.md#stage-50)

    - “I will side with you. The Shadow must not be disturbed.” → [unzel_20](#d-unzel_20)
    - “I will side with Vacor.” → [unzel_fight](#d-unzel_fight)

    <span id="d-unzel_17"></span>**`unzel_17`** Unzel: “What? You killed my four friends? Argh, I feel the rage coming.”

    - Next → [unzel_18](#d-unzel_18)

    <span id="d-unzel_20"></span>**`unzel_20`** Unzel: “Thank you my friend. We will keep the Shadow safe from Vacor.” — **effects:** sets stage 51 of [Missing pieces](../quests/vacor.md#stage-51)

    - Next → [unzel_21](#d-unzel_21)

    <span id="d-unzel_18"></span>**`unzel_18`** Unzel: “However, I also realize that all this is the making of Vacor. I'll give you a choice now. Choose wisely.”

    - Next → [unzel_19](#d-unzel_19)

    <span id="d-unzel_21"></span>**`unzel_21`** Unzel: “You should go talk to him about the Shadow.”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Formatting change only (no gameplay effect)<br>Dialogue: 6 lines changed<br>· text: “Hmmm, yes... Let's see... (Unzel opens the sealed message and reads i…” → “Hmm, yes... Let's see... [Unzel opens the sealed message and reads it]” |
| [v0.7.4](../versions/0.7.4.md) | Attack cost: 10 → 9 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `unzel` |
    | Spawn group | `unzel` |
    | Loot table | `unzel` |
    | Conversation | `unzel` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:8` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "unzel",
     "name": "Unzel",
     "iconID": "monsters_men:8",
     "maxHP": 59,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 5,
      "max": 9
     },
     "spawnGroup": "unzel",
     "phraseID": "unzel",
     "droplistID": "unzel",
     "attackCost": 9,
     "attackChance": 80,
     "criticalSkill": 30,
     "criticalMultiplier": 3.0,
     "blockChance": 40,
     "damageResistance": 2
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=unzel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=unzel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=unzel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=unzel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
