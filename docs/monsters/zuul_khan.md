# ![](../assets/icons/monsters/monsters_rltiles2_88.png){ .sprite } Zuul'khan

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_88.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `zuul_khan` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 175 |
| **XP when killed** | 214 |
| **Found in** | bogsten4 |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 175 |
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
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 1 to 10 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [bogsten4](../maps/bogsten4.md) | – | 1 | – |


## Quests that count kills

- [Fungi panic](../quests/fungi_panic.md#stage-90) with stepping on a trigger on [bogsten4](../maps/bogsten4.md) checks that you've killed at least 1
- A conversation with [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) checks that you've killed at least 1
- [Fungi panic](../quests/fungi_panic.md#stage-161) with [Black fog](../monsters/zuul_khan1_blocker.md) ([bogsten4](../maps/bogsten4.md)) checks that you've killed at least 1


## Quests

- [Fungi panic](../quests/fungi_panic.md): stages 70, 72, 80, 115, 135, 150, 155

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Zuul'khan. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/zuul_khan.json" data-npc="Zuul&#x27;khan" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (46 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-zuul_khan"></span>**`zuul_khan`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 155 of [Fungi panic](../quests/fungi_panic.md#stage-155))* → [zuul_khan_155](#d-zuul_khan_155)
    - branch 2 *(if reached stage 150 of [Fungi panic](../quests/fungi_panic.md#stage-150))* → [zuul_khan_150](#d-zuul_khan_150)
    - branch 3 *(if carry 1× [Bogsten's staff](../items/bogsten_staff.md))* → [zuul_khan_115_10](#d-zuul_khan_115_10)
    - branch 4 *(if wearing [Bogsten's staff](../items/bogsten_staff.md))* → [zuul_khan_115_10](#d-zuul_khan_115_10)
    - branch 5 *(if reached stage 115 of [Fungi panic](../quests/fungi_panic.md#stage-115))* → [zuul_khan_115](#d-zuul_khan_115)
    - branch 6 *(if reached stage 70 of [Fungi panic](../quests/fungi_panic.md#stage-70))* → [zuul_khan_70](#d-zuul_khan_70)
    - branch 7 → [zuul_khan_10](#d-zuul_khan_10)

    <span id="d-zuul_khan_155"></span>**`zuul_khan_155`** Zuul'khan: “Don't disturb me! I am practicing dangerous spells.”


    <span id="d-zuul_khan_150"></span>**`zuul_khan_150`** [Dummy NPC](../monsters/none.md): “Zuul'khan towers over you and starts muttering strange words.”

    - “I'm feeling dizzy...” → [zuul_khan_150_10](#d-zuul_khan_150_10)

    <span id="d-zuul_khan_115_10"></span>**`zuul_khan_115_10`** Zuul'khan: “Bogsten is dead. Finally.”

    - “Yes. Now where is my reward?” → [zuul_khan_115_20](#d-zuul_khan_115_20)

    <span id="d-zuul_khan_115"></span>**`zuul_khan_115`** Zuul'khan: “Is Bogsten dead already?”

    - “No, not yet.” → *conversation ends*
    - “I have killed him.” *(if killed 1× [Bogsten](../monsters/bogsten.md))* → [zuul_khan_115_10](#d-zuul_khan_115_10)

    <span id="d-zuul_khan_70"></span>**`zuul_khan_70`** Zuul'khan: “I see that you have their family necklace. So you must die now.”

    - “I'll have to thank Bogsten: This sounds like a fun fight.” → [zuul_khan_70_24](#d-zuul_khan_70_24)
    - “You shouldn't kill me. I could be of use.” → [zuul_khan_70_84](#d-zuul_khan_70_84)
    - “Please. I will crawl before you. Don't hurt me.” → [zuul_khan_70_82](#d-zuul_khan_70_82)

    <span id="d-zuul_khan_10"></span>**`zuul_khan_10`** Zuul'khan: “Oh kid, you look like someone nice. I don't want you to be injured because of me. I urge you to leave!”

    - “What's going on?” → [zuul_khan_12](#d-zuul_khan_12)

    <span id="d-zuul_khan_150_10"></span>**`zuul_khan_150_10`** [Zuul'khan](../monsters/zuul_khan.md): “Done. You will never fear any of these fungi spores anymore.” — **effects:** sets stage 155 of [Fungi panic](../quests/fungi_panic.md#stage-155), applies condition spore_poison, +1 [Spore poison immunity](../skills/sporeImmunity.md)

    - “Oh wow.” → [zuul_khan_150_20](#d-zuul_khan_150_20)

    <span id="d-zuul_khan_115_20"></span>**`zuul_khan_115_20`** Zuul'khan: “Give me the staff first.”

    - “Here it is.” *(if hand over 1× [Bogsten's staff](../items/bogsten_staff.md))* → [zuul_khan_115_50](#d-zuul_khan_115_50)
    - “Here it is.” *(if wearing (and give up) [Bogsten's staff](../items/bogsten_staff.md))* → [zuul_khan_115_50](#d-zuul_khan_115_50)
    - “No, I have changed my mind. I'll rather keep Bogsten's staff.” → [zuul_khan_115_22](#d-zuul_khan_115_22)

    <span id="d-zuul_khan_70_24"></span>**`zuul_khan_70_24`** Zuul'khan: “Then our little conversation is over now.”

    - “Attack!” → [zuul_khan_70_30](#d-zuul_khan_70_30)
    - “Hm, wait. Let me think again.” → [zuul_khan_70_20](#d-zuul_khan_70_20)
    - “I wish we could talk a little more.” → [zuul_khan_50](#d-zuul_khan_50)

    <span id="d-zuul_khan_70_84"></span>**`zuul_khan_70_84`** Zuul'khan: “Hmm. Maybe.”

    - Next → [zuul_khan_70_20](#d-zuul_khan_70_20)

    <span id="d-zuul_khan_70_82"></span>**`zuul_khan_70_82`** Zuul'khan: “Disgusting. Away with you!”


    <span id="d-zuul_khan_12"></span>**`zuul_khan_12`** Zuul'khan: “Give me your hand! ... No don't! ... Give me ...”

    - Next → [zuul_khan_14](#d-zuul_khan_14)

    <span id="d-zuul_khan_150_20"></span>**`zuul_khan_150_20`** Zuul'khan: “Leave me now! I have to regain my practice of spells.”


    <span id="d-zuul_khan_115_50"></span>**`zuul_khan_115_50`** Zuul'khan: “Finally I got the staff back!” — **effects:** sets stage 150 of [Fungi panic](../quests/fungi_panic.md#stage-150)

    - “My reward...?” → [zuul_khan_150](#d-zuul_khan_150)

    <span id="d-zuul_khan_115_22"></span>**`zuul_khan_115_22`** Zuul'khan: “You won't betray me, you little fool!”

    - “Who is betraying here? Where is my dearly earned reward!” → [zuul_khan_115_20](#d-zuul_khan_115_20)
    - “Little in height - but strong! Attack!” → [zuul_khan_115_24](#d-zuul_khan_115_24)

    <span id="d-zuul_khan_70_30"></span>**`zuul_khan_70_30`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 80 of [Fungi panic](../quests/fungi_panic.md#stage-80)

    - branch 1 → *fight starts*

    <span id="d-zuul_khan_70_20"></span>**`zuul_khan_70_20`** Zuul'khan: “Go and kill Bogsten up there.”

    - Next → [zuul_khan_70_22](#d-zuul_khan_70_22)

    <span id="d-zuul_khan_50"></span>**`zuul_khan_50`** Zuul'khan: “You may have a last wish. What do you want?”

    - “Tell me why you are here in Bogsten's caves?” → [zuul_khan_60](#d-zuul_khan_60)

    <span id="d-zuul_khan_14"></span>**`zuul_khan_14`** Zuul'khan: “I'm hurt ... I'll hurt ... Never do! ... Help! ... Kill! ... your hand - pleease ...”

    - “* Reach out your hand *” → [zuul_khan_20](#d-zuul_khan_20)
    - “Attack!” → [zuul_khan_16](#d-zuul_khan_16)
    - “I better go.” → *conversation ends*

    <span id="d-zuul_khan_115_24"></span>**`zuul_khan_115_24`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 135 of [Fungi panic](../quests/fungi_panic.md#stage-135)

    - branch 1 → *fight starts*

    <span id="d-zuul_khan_70_22"></span>**`zuul_khan_70_22`** Zuul'khan: “Kill Bogsten and bring me his staff as evidence.” — **effects:** sets stage 72 of [Fungi panic](../quests/fungi_panic.md#stage-72)

    - “What would I gain from this?” → [zuul_khan_70_40](#d-zuul_khan_70_40)
    - “No. I'd rather kill you.” → [zuul_khan_70_24](#d-zuul_khan_70_24)

    <span id="d-zuul_khan_60"></span>**`zuul_khan_60`** Zuul'khan: “Bogsten's cave? Oh how I hate that name!”

    - Next → [zuul_khan_60_20](#d-zuul_khan_60_20)

    <span id="d-zuul_khan_20"></span>**`zuul_khan_20`** Zuul'khan: “Hahaha! AHAHAHAHA! I am free again!”

    - “Who are you?” → [zuul_khan_30](#d-zuul_khan_30)
    - “What are you?” → [zuul_khan_22](#d-zuul_khan_22)

    <span id="d-zuul_khan_16"></span>**`zuul_khan_16`** Zuul'khan: “No! Don't do me wrong!”

    - Next → [zuul_khan_12](#d-zuul_khan_12)

    <span id="d-zuul_khan_70_40"></span>**`zuul_khan_70_40`** Zuul'khan: “Ah. You are not as stupid as you look, kid.”

    - Next → [zuul_khan_70_42](#d-zuul_khan_70_42)

    <span id="d-zuul_khan_60_20"></span>**`zuul_khan_60_20`** Zuul'khan: “It was the Bogstens who imprisoned me here, long years ago. With a petrifying spell. I did nothing evil to them, except ... Well, I did almost nothing evil to them.”

    - Next → [zuul_khan_60_30](#d-zuul_khan_60_30)

    <span id="d-zuul_khan_30"></span>**`zuul_khan_30`** Zuul'khan: “I am the Archmancer of the underground. Widely known as Master of the Fungi and Commander to anything that crawls.”

    - Next → [zuul_khan_32](#d-zuul_khan_32)

    <span id="d-zuul_khan_22"></span>**`zuul_khan_22`** Zuul'khan: “Be nice, kid.”

    - “OK. Who are you?” → [zuul_khan_30](#d-zuul_khan_30)

    <span id="d-zuul_khan_70_42"></span>**`zuul_khan_70_42`** Zuul'khan: “I'll give you two things.”

    - Next → [zuul_khan_70_44](#d-zuul_khan_70_44)

    <span id="d-zuul_khan_60_30"></span>**`zuul_khan_60_30`** Zuul'khan: “More than a century ago, I found the way to command the crawling species of the underground and to bend the fungi to my will.”

    - Next → [zuul_khan_60_40](#d-zuul_khan_60_40)

    <span id="d-zuul_khan_32"></span>**`zuul_khan_32`** Zuul'khan: “I am the great Zuul'khan!”

    - “Great.” → [zuul_khan_34](#d-zuul_khan_34)

    <span id="d-zuul_khan_70_44"></span>**`zuul_khan_70_44`** Zuul'khan: “I'll spare your life.”

    - “Generously.” → [zuul_khan_70_46](#d-zuul_khan_70_46)

    <span id="d-zuul_khan_60_40"></span>**`zuul_khan_60_40`** Zuul'khan: “I chose this place to practice my arts and prepare an army of Fungi.”

    - Next → [zuul_khan_60_50](#d-zuul_khan_60_50)

    <span id="d-zuul_khan_34"></span>**`zuul_khan_34`** Zuul'khan: “Great and strong, yes.”

    - “Aha.” → [zuul_khan_40](#d-zuul_khan_40)

    <span id="d-zuul_khan_70_46"></span>**`zuul_khan_70_46`** Zuul'khan: “And I'll provide you with a permanent immunity to the spore poison.”

    - “Agreed. I'll go upstairs and finish Bogsten.” → [zuul_khan_70_50](#d-zuul_khan_70_50)
    - “Forget it. Attack!” → [zuul_khan_70_30](#d-zuul_khan_70_30)

    <span id="d-zuul_khan_60_50"></span>**`zuul_khan_60_50`** Zuul'khan: “The Bogstens must have heard about my activities in the caves under their house and became suspicious.”

    - Next → [zuul_khan_60_60](#d-zuul_khan_60_60)

    <span id="d-zuul_khan_40"></span>**`zuul_khan_40`** Zuul'khan: “You are the first human I've seen in such a long time.”

    - Next → [zuul_khan_42](#d-zuul_khan_42)

    <span id="d-zuul_khan_70_50"></span>**`zuul_khan_70_50`** Zuul'khan: “Do so.” — **effects:** sets stage 115 of [Fungi panic](../quests/fungi_panic.md#stage-115)


    <span id="d-zuul_khan_60_60"></span>**`zuul_khan_60_60`** Zuul'khan: “Lotho Bogsten sneaked down here and caught me unawares.”

    - Next → [zuul_khan_60_70](#d-zuul_khan_60_70)

    <span id="d-zuul_khan_42"></span>**`zuul_khan_42`** Zuul'khan: “And I am the last human you will ever see.”

    - “You threaten me?” → [zuul_khan_50](#d-zuul_khan_50)

    <span id="d-zuul_khan_60_70"></span>**`zuul_khan_60_70`** Zuul'khan: “I didn't expect petrifying. Who would use such a weak spell that has to be renewed every few weeks?”

    - Next → [zuul_khan_60_80](#d-zuul_khan_60_80)

    <span id="d-zuul_khan_60_80"></span>**`zuul_khan_60_80`** Zuul'khan: “I could not move but I noticed everything that was happening around me. Lotho Bogsten visited me regularly and renewed the spell.”

    - Next → [zuul_khan_60_100](#d-zuul_khan_60_100)

    <span id="d-zuul_khan_60_100"></span>**`zuul_khan_60_100`** Zuul'khan: “Finally, after long, long years, Lotho Bogsten must have died. Fortunately, his son is not so dutiful.”

    - “He had children?” → [zuul_khan_60_120](#d-zuul_khan_60_120)

    <span id="d-zuul_khan_60_120"></span>**`zuul_khan_60_120`** Zuul'khan: “Indeed he had a son. But that lazybones didn't come as regularly as needed. The spell wore off, and I could move again.”

    - Next → [zuul_khan_60_140](#d-zuul_khan_60_140)

    <span id="d-zuul_khan_60_140"></span>**`zuul_khan_60_140`** Zuul'khan: “AHAHAHAHA!” — **effects:** sets stage 70 of [Fungi panic](../quests/fungi_panic.md#stage-70)

    - Next → [zuul_khan_70](#d-zuul_khan_70)



## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 46 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=zuul_khan.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `zuul_khan` |
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


<small>Data from v0.8.18</small>
