# ![](../assets/icons/monsters/monsters_rltiles1_86.png){ .sprite } Aulowenn

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles1_86.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `aulowenn` |
| **Type** | NPC |
| **Class** | Humanoid |
| **HP** | 194 |
| **XP when killed** | 324 |
| **Found in** | lodar13 |
| **Introduced** | v0.7.0 or earlier |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 194 |
| Damage | 0 to 9 |
| Attack chance | 120 |
| Block chance | 90 |
| Damage resistance | 5 |
| Max AP | 10 |
| Attack cost | 3 AP |
| Attacks per turn | 3 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Drops

| Item | Chance | Qty |
|---|---|---|
| [Aulowenn's signet ring](../items/aulowenn.md) | 100% | 1 |
| [Gleaming claymore of ruin](../items/clmr_ruin.md) | 100% | 1 |
| [Gold coins](../items/gold.md) | 100% | 50 to 150 |
| [Polished ring](../items/ring2.md) | 100% | 1 |

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [lodar13](../maps/lodar13.md) | – | 1 | – |


## Quests

- [No rest for the guilty](../quests/lodar13_rest.md): stages 10, 11, 31, 40, 60, 65

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Aulowenn. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/aulowenn0.json" data-npc="Aulowenn" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (36 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-aulowenn0"></span>**`aulowenn0`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 31 of [No rest for the guilty](../quests/lodar13_rest.md#stage-31))* → [aulowenn_atk](#d-aulowenn_atk)
    - branch 2 *(if reached stage 60 of [No rest for the guilty](../quests/lodar13_rest.md#stage-60))* → [aulowenn_wb0](#d-aulowenn_wb0)
    - branch 3 *(if reached stage 40 of [No rest for the guilty](../quests/lodar13_rest.md#stage-40))* → [aulowenn_k0](#d-aulowenn_k0)
    - branch 4 *(if reached stage 11 of [No rest for the guilty](../quests/lodar13_rest.md#stage-11))* → [aulowenn_ms0](#d-aulowenn_ms0)
    - branch 5 → [aulowenn1](#d-aulowenn1)

    <span id="d-aulowenn_atk"></span>**`aulowenn_atk`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [No rest for the guilty](../quests/lodar13_rest.md#stage-30))* → [aulowenn_atk1](#d-aulowenn_atk1)
    - branch 2 → [aulowenn_atk0](#d-aulowenn_atk0)

    <span id="d-aulowenn_wb0"></span>**`aulowenn_wb0`** Aulowenn: “Welcome back my friend. Thank you for helping me defeat that foul creature that was haunting the grave of my fellow guards.”

    - Next → [aulowenn_k1](#d-aulowenn_k1)

    <span id="d-aulowenn_k0"></span>**`aulowenn_k0`** Aulowenn: “Excellent. Maybe now my brethren can rest peacefully. Thank you so much for helping me.” — **effects:** sets stage 40 of [No rest for the guilty](../quests/lodar13_rest.md#stage-40)

    - Next → [aulowenn_k1](#d-aulowenn_k1)

    <span id="d-aulowenn_ms0"></span>**`aulowenn_ms0`** Aulowenn: “Hello again. Were you successful in defeating that beast?”

    - “What was I supposed to do again?” → [aulowenn16](#d-aulowenn16)
    - “Yes, I defeated the creature.” *(if hand over 1× [Tiqui's shield](../items/tiqui.md))* → [aulowenn_k0](#d-aulowenn_k0)
    - “Not yet. I'll do it soon enough though.” → [aulowenn21](#d-aulowenn21)
    - “I don't think I should get involved in this.” → [aulowenn21b](#d-aulowenn21b)
    - “I'll go visit the graves, but I can't promise that I'll kill anyone.” → [aulowenn21b](#d-aulowenn21b)
    - “I met Tiqui by those graves. He had an interesting tale to tell.” *(if reached stage 22 of [No rest for the guilty](../quests/lodar13_rest.md#stage-22))* → [aulowenn_tq0](#d-aulowenn_tq0)

    <span id="d-aulowenn1"></span>**`aulowenn1`** Aulowenn: “Halt! Do not come any closer. The contents of these crates is property of Feygard.”

    - “I mean you no harm. Who are you?” → [aulowenn2](#d-aulowenn2)
    - “Sure. I'll just stay right here. Who are you?” → [aulowenn2](#d-aulowenn2)
    - “Fine. I will leave.” → *conversation ends*

    <span id="d-aulowenn_atk1"></span>**`aulowenn_atk1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 65 of [No rest for the guilty](../quests/lodar13_rest.md#stage-65)

    - branch 1 → [aulowenn_atk0](#d-aulowenn_atk0)

    <span id="d-aulowenn_atk0"></span>**`aulowenn_atk0`** Aulowenn: “For Feygard!” — **effects:** sets stage 31 of [No rest for the guilty](../quests/lodar13_rest.md#stage-31)

    - “Attack!” → *fight starts*

    <span id="d-aulowenn_k1"></span>**`aulowenn_k1`** Aulowenn: “In return, you are very welcome to use my bed to rest whenever you wish.” — **effects:** sets stage 60 of [No rest for the guilty](../quests/lodar13_rest.md#stage-60)


    <span id="d-aulowenn16"></span>**`aulowenn16`** Aulowenn: “As I mentioned, some of my men were killed by the local creatures here. We buried them to the east of here.”

    - Next → [aulowenn17](#d-aulowenn17)

    <span id="d-aulowenn21"></span>**`aulowenn21`** Aulowenn: “Good. Return here once you are done.”


    <span id="d-aulowenn21b"></span>**`aulowenn21b`** Aulowenn: “You do as you wish. I'll be here regardless.”


    <span id="d-aulowenn_tq0"></span>**`aulowenn_tq0`** Aulowenn: “You actually listened to it? Please, indulge me, what lies did it have you believe?”

    - “He told me that you have been killing off his kin.” → [aulowenn_tq1](#d-aulowenn_tq1)

    <span id="d-aulowenn2"></span>**`aulowenn2`** Aulowenn: “I am Aulowenn of Feygard.”

    - “What are you doing out here?” → [aulowenn3](#d-aulowenn3)

    <span id="d-aulowenn17"></span>**`aulowenn17`** Aulowenn: “I haven't been there for a few days now, but last I visited the graves, there was one of those foul creatures standing over the graves.”

    - Next → [aulowenn18](#d-aulowenn18)

    <span id="d-aulowenn_tq1"></span>**`aulowenn_tq1`** Aulowenn: “Of course we have! They've been attacking us, and we've taken precautions by hunting them so they can't kill more of us.”

    - Next → [aulowenn_tq2](#d-aulowenn_tq2)

    <span id="d-aulowenn3"></span>**`aulowenn3`** Aulowenn: “I'm guarding these crates. That's what I do. At least until my company gets back from their scouting party.”

    - Next → [aulowenn4](#d-aulowenn4)

    <span id="d-aulowenn18"></span>**`aulowenn18`** Aulowenn: “I've seen that particular creature there before, it seems to be haunting the graves of my fellow men.”

    - Next → [aulowenn19](#d-aulowenn19)

    <span id="d-aulowenn_tq2"></span>**`aulowenn_tq2`** Aulowenn: “To think that they believe they have a chance against the forces of Feygard. Hah! We will cut them down like sheep once the reinforcements get here.”

    - “I should leave before there is more bloodshed.” → [aulowenn21b](#d-aulowenn21b)
    - “I don't like your tone. They haven't done anything to you.” → [aulowenn_tq4](#d-aulowenn_tq4)
    - “I was also asked to take care of you, and I intend to do just that.” → [aulowenn_tq3](#d-aulowenn_tq3)

    <span id="d-aulowenn4"></span>**`aulowenn4`** Aulowenn: “Oh I hope they do get back. Come to think of it, they have been away for quite some time now.”

    - Next → [aulowenn5](#d-aulowenn5)

    <span id="d-aulowenn19"></span>**`aulowenn19`** Aulowenn: “Of course, it must be up to no good. I would like your help in either removing or defeating that thing.”

    - “So, you want me to go visit the graves to the east and defeat whatever creature is there?” → [aulowenn20](#d-aulowenn20)

    <span id="d-aulowenn_tq4"></span>**`aulowenn_tq4`** Aulowenn: “Hah! See, there are those lies that I told you about. They. Attacked. Us. Get it?”

    - “You will be no match for me.” → [aulowenn_atk](#d-aulowenn_atk)
    - “I should leave before there is more bloodshed.” → *conversation ends*

    <span id="d-aulowenn_tq3"></span>**`aulowenn_tq3`** Aulowenn: “Hah! Take care of me? That will be the day.”

    - “You will be no match for me.” → [aulowenn_atk](#d-aulowenn_atk)
    - “I should leave before there is more bloodshed.” → *conversation ends*

    <span id="d-aulowenn5"></span>**`aulowenn5`** Aulowenn: “I sure hope they are well. Unlike the others...”

    - “What about the others?” → [aulowenn6](#d-aulowenn6)

    <span id="d-aulowenn20"></span>**`aulowenn20`** Aulowenn: “Yes, that's it. I should also warn you that those creatures are intelligible, so I would urge you to act quickly when encountering it, before it can spew its foul lies.” — **effects:** sets stage 11 of [No rest for the guilty](../quests/lodar13_rest.md#stage-11)

    - “Sounds easy enough. I'll do it.” → [aulowenn21](#d-aulowenn21)
    - “Great, more blood for my sword. I'll do it.” → [aulowenn21](#d-aulowenn21)
    - “Anything to help a fellow Feygard friend.” → [aulowenn21a](#d-aulowenn21a)
    - “I don't think I should get involved in this.” → [aulowenn21b](#d-aulowenn21b)
    - “I'll go visit the graves, but I can't promise that I'll kill anyone.” → [aulowenn21b](#d-aulowenn21b)
    - “I have already killed it.” *(if hand over 1× [Tiqui's shield](../items/tiqui.md))* → [aulowenn_k0](#d-aulowenn_k0)

    <span id="d-aulowenn6"></span>**`aulowenn6`** Aulowenn: “In my squad, we were a band of six guards that, together with other squads, were sent out here to find a dangerous madman that takes his refuge somewhere in the nearby hills around here.”

    - Next → [aulowenn7](#d-aulowenn7)

    <span id="d-aulowenn21a"></span>**`aulowenn21a`** Aulowenn: “Glory to Feygard. Return here once you are done.”


    <span id="d-aulowenn7"></span>**`aulowenn7`** Aulowenn: “But something started to happen once we got here. Some of my fellow guards started acting ... odd.”

    - Next → [aulowenn8](#d-aulowenn8)

    <span id="d-aulowenn8"></span>**`aulowenn8`** Aulowenn: “I don't know if it was just me imagining things or if something truly happened to them. Anyway, one by one, we started to get fewer and fewer.”

    - Next → [aulowenn9](#d-aulowenn9)

    <span id="d-aulowenn9"></span>**`aulowenn9`** Aulowenn: “Some of my men were killed by the creatures that live in these woods, some ran away by themselves and some have never come back from their scouting trips.” — **effects:** sets stage 10 of [No rest for the guilty](../quests/lodar13_rest.md#stage-10)

    - “What do you think has happened to them?” → [aulowenn10](#d-aulowenn10)

    <span id="d-aulowenn10"></span>**`aulowenn10`** Aulowenn: “I have two theories. My first thought is that some of the local creatures that we've been having problems with here might have captured them, or even killed them. I know for a fact that some were killed by the creatures, since we even…”

    - Next → [aulowenn11](#d-aulowenn11)

    <span id="d-aulowenn11"></span>**`aulowenn11`** Aulowenn: “The creatures in these woods are intelligible, but fierce. Luckily, we've been able to kill them off before they've been able to spew their foul lies. There are still a few of them around though.”

    - Next → [aulowenn12](#d-aulowenn12)

    <span id="d-aulowenn12"></span>**`aulowenn12`** Aulowenn: “My second theory is that the madman that we are looking for must have done something to them. Maybe the madman has smeared some of his madness onto them.”

    - Next → [aulowenn13](#d-aulowenn13)

    <span id="d-aulowenn13"></span>**`aulowenn13`** Aulowenn: “Regardless, there isn't much that I am able to do here. I need to guard these crates.”

    - Next → [aulowenn14](#d-aulowenn14)

    <span id="d-aulowenn14"></span>**`aulowenn14`** Aulowenn: “Also, I do hope that those creatures that seem to live here don't return. They've been a real pest.”

    - “Anything I can do to help?” → [aulowenn15](#d-aulowenn15)
    - “Good luck with that. Goodbye.” → *conversation ends*

    <span id="d-aulowenn15"></span>**`aulowenn15`** Aulowenn: “Oh yes, would you? There is one thing you could do.”

    - Next → [aulowenn16](#d-aulowenn16)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 5 lines changed<br>· text: “I sure hope they are well. Unlike the others..” → “I sure hope they are well. Unlike the others...”<br>· text: “But something started to happen once we got here. Some of my fellow g…” → “But something started to happen once we got here. Some of my fellow g…” |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed<br>· text: “I don't know if was just me imagining things or if something truly ha…” → “I don't know if it was just me imagining things or if something truly…” |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line changed |
| [v0.8.7](../versions/0.8.7.md) | monsterClass added (humanoid) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aulowenn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aulowenn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aulowenn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=aulowenn.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `aulowenn` |
    | Spawn group | `aulowenn` |
    | Loot table | `aulowenn` |
    | Conversation | `aulowenn0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles1:86` |
    | Defined in | `res/raw/monsterlist_v070_npcs.json` |

    Raw data:

    ```json
    {
     "id": "aulowenn",
     "name": "Aulowenn",
     "iconID": "monsters_rltiles1:86",
     "maxHP": 194,
     "maxAP": 10,
     "moveCost": 5,
     "unique": 1,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 0,
      "max": 9
     },
     "phraseID": "aulowenn0",
     "droplistID": "aulowenn",
     "attackCost": 3,
     "attackChance": 120,
     "blockChance": 90,
     "damageResistance": 5
    }
    ```


<small>Data from v0.8.18</small>
