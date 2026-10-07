---
description: "Hagale is an NPC who can also be fought in Andor's Trail, found in Fallhaven."
---

# ![](../assets/icons/monsters/monsters_ld1_111.png){ .sprite } Hagale

**Where to find Hagale:** Fallhaven: [woodsettlement0](../maps/woodsettlement0.md#pin-npc-algore)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_111.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Found in** | Fallhaven |
| **Class** | Humanoid |
| **HP** | 150 |
| **XP when defeated** | 439 |
| **Entry ID** | `algore` |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

## Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 150 |
| XP when defeated | 439 |
| Damage | 10 to 15 |
| Attack chance | 120 |
| Block chance | 90 |
| Damage resistance | 3 |
| Max AP | 10 |
| Attack cost | 2 AP |
| Attacks per turn | 5 |
| Move cost | 5 AP |
| Critical skill | 20 |
| Critical multiplier | 2.0 |
| Critical hit chance | 15% |

**On hit:** Heal HP: 5 to 10


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 200 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [woodsettlement0](../maps/woodsettlement0.md) | Fallhaven | 1 | – |

## Quests that count defeats

- [Fungi Panic - non displayed (hidden flag)](../quests/fungi_panic_nondisplayed.md#stage-20) with stepping on a trigger on [woodsettlement0](../maps/woodsettlement0.md) checks that this enemy has been defeated.

## Quests

- [Mine for the taking](../quests/graveyard_quest.md): stages 35, 40, 90, 95, 100, 105

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Hagale. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/algore_begin.json" data-npc="Hagale" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (35 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-algore_begin"></span>**`algore_begin`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 95 of [Mine for the taking](../quests/graveyard_quest.md#stage-95))* → [algore_special](#d-algore_special)
    - Next *(if reached stage 35 of [Mine for the taking](../quests/graveyard_quest.md#stage-35); NOT reached stage 40 of [Mine for the taking](../quests/graveyard_quest.md#stage-40); hand over 2× [Lowyna's special brew](../items/drink_lowyn2.md))* → [algore_11](#d-algore_11)
    - Next *(if reached stage 100 of [Mine for the taking](../quests/graveyard_quest.md#stage-100))* → [algore_special2](#d-algore_special2)
    - Next → [algore_01](#d-algore_01)

    <span id="d-algore_special"></span>**`algore_special`** Hagale: “Thanks for letting me have the sword kid. I decided that with the money I can get for this I can rebuild my life. I'm going to sober up and start trading again. I'll be leaving here soon.”

    - “Best of luck!” → *conversation ends*

    <span id="d-algore_11"></span>**`algore_11`** Hagale: “Alright kid! [Hagale immediately opens one of the bottles and takes a big swig, which he loudly swallows before wiping his mouth on the sleeve of his tattered shirt] Yeah, I know something about that chest ... *burp* ... I almost opened it.”

    - Next → [algore_20](#d-algore_20)

    <span id="d-algore_special2"></span>**`algore_special2`** Hagale: “Thanks for the gold kid. I decided that with the money I can rebuild my life. I'm going to sober up and start trading again. I'll be leaving here soon.”

    - “Good luck!” → *conversation ends*

    <span id="d-algore_01"></span>**`algore_01`** Hagale: “Hey kid! Why don't you be a good little boy and fetch me some Lowyna's special brew?”

    - Next → [algore_00](#d-algore_00)

    <span id="d-algore_20"></span>**`algore_20`** Hagale: “I heard rumors about an unguarded treasure chest. I heard that the key that opened it, hung around the neck of an undead roaming the cemetery south of the chest. I also heard that the entrance to the cemetery was sealed by magic.”

    - Next → [algore_30](#d-algore_30)

    <span id="d-algore_00"></span>**`algore_00`** Hagale: “[This man smells of alcohol and some plant-like substance; he is clearly intoxicated]”

    - “I defeated the undead monster and opened the chest. I found a powerful sword inside.” *(if reached stage 80 of [Mine for the taking](../quests/graveyard_quest.md#stage-80); NOT reached stage 90 of [Mine for the taking](../quests/graveyard_quest.md#stage-90); NOT reached stage 95 of [Mine for the taking](../quests/graveyard_quest.md#stage-95); NOT reached stage 100 of [Mine for the taking](../quests/graveyard_quest.md#stage-100); NOT reached stage 105 of [Mine for the taking](../quests/graveyard_quest.md#stage-105))* → [algore_99](#d-algore_99)
    - “I heard you were interested in that unattended treasure chest by the Waterway house.” *(if reached stage 30 of [Mine for the taking](../quests/graveyard_quest.md#stage-30); NOT reached stage 40 of [Mine for the taking](../quests/graveyard_quest.md#stage-40))* → [algore_10](#d-algore_10)
    - “Don't breathe on me! I'm leaving!” → *conversation ends*

    <span id="d-algore_30"></span>**`algore_30`** Hagale: “I thought nothing more of it. I was a simple trader in Loneford with a beautiful wife and daughter. [Hagale takes another long swig from the bottle of Lowyna's special brew]”

    - Next → [algore_31](#d-algore_31)

    <span id="d-algore_99"></span>**`algore_99`** Hagale: “You actually opened the chest? That sword must be worth a lot of money ... could buy a lot of Lowyna's special brew ... Sorry kid, but I need that sword!”

    - “I went through hell to get this sword. I won't give it to you without a fight.” *(if carry 1× [LifeTaker](../items/lifetaker.md))* → [algore_99a](#d-algore_99a)
    - “I went through a lot to get this sword ... but you suffered more than me. I won't fight you. If you want it that…” *(if hand over 1× [LifeTaker](../items/lifetaker.md))* → [algore_99b](#d-algore_99b)
    - “Yes, I have the sword, see here!” *(if wearing [LifeTaker](../items/lifetaker.md))* → [algore_99c](#d-algore_99c)
    - “I did find the sword, but I don't have it anymore.” *(if NOT carry 1× [LifeTaker](../items/lifetaker.md); NOT wearing [LifeTaker](../items/lifetaker.md))* → [algore_99d](#d-algore_99d)

    <span id="d-algore_10"></span>**`algore_10`** Hagale: “Oh yeah? What's it to you kid? ... BURP ... If you want to know, it will cost you two bottles of Lowyna's special brew.” — **effects:** sets stage 35 of [Mine for the taking](../quests/graveyard_quest.md#stage-35)


    <span id="d-algore_31"></span>**`algore_31`** Hagale: “That was until I had to travel to Remgard to purchase some new inventory. I normally make the trip alone. This time however, my wife and daughter decided to accompany me to Remgard.”

    - Next → [algore_32](#d-algore_32)

    <span id="d-algore_99a"></span>**`algore_99a`** Hagale: “Let's go.” — **effects:** sets stage 90 of [Mine for the taking](../quests/graveyard_quest.md#stage-90)

    - “I'm sorry it has come to this.” → *fight starts*

    <span id="d-algore_99b"></span>**`algore_99b`** Hagale: “Alright hand it over. Be quick about it.” — **effects:** sets stage 95 of [Mine for the taking](../quests/graveyard_quest.md#stage-95)

    - “I hope you find peace.” → *conversation ends*

    <span id="d-algore_99c"></span>**`algore_99c`** Hagale: “Hey kid! Stop waving that thing at me! If you want to talk to me, put it away first!”


    <span id="d-algore_99d"></span>**`algore_99d`** Hagale: “So where is it?”

    - “I dropped it somewhere.” → [algore_99e](#d-algore_99e)
    - “I sold it.” → [algore_99f](#d-algore_99f)

    <span id="d-algore_32"></span>**`algore_32`** Hagale: “We were only halfway there when we were attacked by Plaguestriders. My daughter and I managed to escape... [Hagale takes another long swig from the bottle of Lowyna's special brew] ...but my wife did not survive.”

    - Next → [algore_33](#d-algore_33)

    <span id="d-algore_99e"></span>**`algore_99e`** Hagale: “Not too bright, are you kid? Perhaps you should go and pick it up again.”


    <span id="d-algore_99f"></span>**`algore_99f`** Hagale: “I gave you the text you needed to get that sword. I think some of that gold should be mine. If you don't give me some then I'll take it from you.”

    - “OK, OK. I guess it's fair that you should get a share. Here's 1,000 gold.” *(if pay 1,000 gold)* → [algore_99g](#d-algore_99g)
    - “No way! I fought to get the sword, and the profit is mine!” → [algore_99i](#d-algore_99i)

    <span id="d-algore_33"></span>**`algore_33`** Hagale: “My daughter was afflicted by a nasty form of blistering skin. I rushed her back to Loneford. I thought with rest, good food, and water she could pull through ... but although the blisters were gradually healing, my daughter's health…”

    - Next → [algore_40](#d-algore_40)

    <span id="d-algore_99g"></span>**`algore_99g`** Hagale: “Thanks kid. It's good to see you have some honor.” — **effects:** sets stage 100 of [Mine for the taking](../quests/graveyard_quest.md#stage-100)


    <span id="d-algore_99i"></span>**`algore_99i`** Hagale: “We'll see about that.” — **effects:** sets stage 105 of [Mine for the taking](../quests/graveyard_quest.md#stage-105)

    - “Yes, we will!” → *fight starts*

    <span id="d-algore_40"></span>**`algore_40`** Hagale: “[Hagale takes another swig from the bottle of Lowyna's special brew] I realized that she wouldn't make it. I watched as she suffered in agonizing pain. I knew without treatment she would die in a matter of weeks.”

    - Next → [algore_41](#d-algore_41)

    <span id="d-algore_41"></span>**`algore_41`** Hagale: “I had to do something. I went to Fallhaven and begged Thoronir to make me a bonemeal potion. Although it would have cured my daughter completely, he refused because Lord Geomyr banned all use of bonemeal as a healing substance! [Hagale…”

    - Next → [algore_50](#d-algore_50)

    <span id="d-algore_50"></span>**`algore_50`** Hagale: “Still, I did not give up. I thought that if I opened the chest and gave its treasure as a gift to Lord Geomyr, I could plead with him to lift the bonemeal ban in time to save my daughter. It sounds stupid but I was desperate.”

    - Next → [algore_51](#d-algore_51)

    <span id="d-algore_51"></span>**`algore_51`** Hagale: “I searched the land for information about the chest and graveyard. I spent my entire fortune in the process. My last few coins resulted in a tip that directed me to a group of bandits.”

    - Next → [algore_60](#d-algore_60)

    <span id="d-algore_60"></span>**`algore_60`** Hagale: “A few days later, I tracked the bandits down. I begged and pleaded but they would not volunteer any information. They were obviously after the chest themselves, and they attacked me.”

    - Next → [algore_61](#d-algore_61)

    <span id="d-algore_61"></span>**`algore_61`** Hagale: “I may be a trader, but traders have to learn how to protect themselves. The first few went down easily, but the leader was an experienced fighter. We fought for over an hour, but eventually I managed to kill him. I searched the body and…”

    - Next → [algore_70](#d-algore_70)

    <span id="d-algore_70"></span>**`algore_70`** Hagale: “The text described a cemetery sealed by magic to contain a powerful undead monster roaming within it. My source was correct, it was a reference to the cemetery south of that chest.”

    - Next → [algore_x81](#d-algore_x81)

    <span id="d-algore_x81"></span>**`algore_x81`** Hagale: “The magical barrier at the cemetery could only be penetrated by someone carrying the text, which contained several magical inscriptions.”

    - Next → [algore_x82](#d-algore_x82)

    <span id="d-algore_x82"></span>**`algore_x82`** Hagale: “I took the best weapons and armor from the bandits, and made my way to the cemetery. Carrying the ancient text in my front pouch, I approached the entrance to the cemetery. I was only a few feet away when the text began to glow.”

    - Next → [algore_85](#d-algore_85)

    <span id="d-algore_85"></span>**`algore_85`** Hagale: “The ground began to tremble and darkness filled the sky. This was followed by a cracking sound, the loudest sound my ears ever heard, making a gust of cold air rush past me. Then, corpses began to claw their way to the surface. The odor…”

    - Next → [algore_86](#d-algore_86)

    <span id="d-algore_86"></span>**`algore_86`** Hagale: “Suddenly, a horde of undead attacked me. I fought them off as best I could but there were just too many. I barely escaped with my life and I never went back.”

    - Next → [algore_86b](#d-algore_86b)

    <span id="d-algore_86b"></span>**`algore_86b`** Hagale: “My daughter passed away shortly after I returned. I failed my wife and my daughter. I lost everything. I buried my family in Loneford, gave up my trade, and came here. Now, I drink Lowyna's special brew all day ... it helps me forget.”

    - “I'm sorry for your losses. You have suffered a lot. I want to finish what you started. Do you still have that text?” → [algore_87](#d-algore_87)

    <span id="d-algore_87"></span>**`algore_87`** Hagale: “[Hagale finishes the second bottle of Lowyna's special brew] Sure do. I hope you know what you're doing kid.” — **effects:** sets stage 40 of [Mine for the taking](../quests/graveyard_quest.md#stage-40), gives 1× [Ancient text](../items/graveyardtext.md)

    - Next → [algore_88](#d-algore_88)

    <span id="d-algore_88"></span>**`algore_88`** Hagale: “Good luck.”




## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 35 lines added |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 2 lines changed<br>· text: “The magical barrier at the cemetary could only be penetrated by someo…” → “The magical barrier at the cemetery could only be penetrated by someo…” |
| [v0.7.9](../versions/0.7.9.md) | Dialogue: 1 line changed<br>· text: “Lets go.” → “Let's go.” |
| [v0.7.10](../versions/0.7.10.md) | Dialogue: 1 line changed |
| [v0.7.11](../versions/0.7.11.md) | Dialogue: 1 line changed<br>· text: “The ground began to tremble and darkness filled the sky. This was fol…” → “The ground began to tremble and darkness filled the sky. This was fol…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `algore` |
    | Spawn group | `algore` |
    | Loot table | `gold200` |
    | Conversation | `algore_begin` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:111` |
    | Defined in | `res/raw/monsterlist_graveyard1.json` |

    Raw data:

    ```json
    {
     "id": "algore",
     "name": "Hagale",
     "iconID": "monsters_ld1:111",
     "maxHP": 150,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 10,
      "max": 15
     },
     "spawnGroup": "algore",
     "phraseID": "algore_begin",
     "droplistID": "gold200",
     "attackCost": 2,
     "attackChance": 120,
     "criticalSkill": 20,
     "criticalMultiplier": 2.0,
     "blockChance": 90,
     "damageResistance": 3,
     "hitEffect": {
      "increaseCurrentHP": {
       "min": 5,
       "max": 10
      }
     }
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=algore.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=algore.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=algore.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=algore.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
