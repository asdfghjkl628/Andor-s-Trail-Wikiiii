# ![](../assets/icons/monsters/monsters_men_4.png){ .sprite } Gabriel

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_4.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `gabriel` |
| **Type** | NPC |
| **Class** | ? |
| **HP** | 1 |
| **Found in** | Vilegard |
| **Introduced** | [v0.8.3](../versions/0.8.3.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 1 |
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
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [vilegard_s](../maps/vilegard_s.md) | Vilegard | 1 | – |


## Quests

- [The Dead are Walking](../quests/dead_walking.md): stages 0, 70

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Gabriel. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/gabriel.json" data-npc="Gabriel" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (32 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-gabriel"></span>**`gabriel`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 70 of [The Dead are Walking](../quests/dead_walking.md#stage-70))* → [gabriel_shadow](#d-gabriel_shadow)
    - branch 2 *(if NOT reached stage 0 of [The Dead are Walking](../quests/dead_walking.md#stage-0))* → [gabriel_shh](#d-gabriel_shh)
    - branch 3 *(if NOT reached stage 60 of [The Dead are Walking](../quests/dead_walking.md#stage-60))* → [gabriel_daw_incomplete](#d-gabriel_daw_incomplete)
    - branch 4 *(if latest stage of [The Dead are Walking](../quests/dead_walking.md#stage-60) is 60)* → [gabriel_daw_complete_0](#d-gabriel_daw_complete_0)

    <span id="d-gabriel_shadow"></span>**`gabriel_shadow`** Gabriel: “Shadow be with you.”

    - “Can you tell me more about the Shadow?” → [priest_shadow_1](#d-priest_shadow_1)

    <span id="d-gabriel_shh"></span>**`gabriel_shh`** Gabriel: “Shh!”

    - “What? Why?” → [gabriel_shh](#d-gabriel_shh)
    - “[You just nod up and down]” → [gabriel_daw_10](#d-gabriel_daw_10)

    <span id="d-gabriel_daw_incomplete"></span>**`gabriel_daw_incomplete`** Gabriel: “Why are you still here when the noises persist?”

    - “Can you explain to me again what it is that you want me to do?” → [gabriel_daw_incomplete_10](#d-gabriel_daw_incomplete_10)
    - “You're not the boss of me, Shadow man. I will address your problem when I am ready to do so.” → *conversation ends*

    <span id="d-gabriel_daw_complete_0"></span>**`gabriel_daw_complete_0`** Gabriel: “The noise, it's gone! Was it you? Did you stop it?”

    - “Yes. It was me.” → [gabriel_daw_complete_10](#d-gabriel_daw_complete_10)

    <span id="d-priest_shadow_1"></span>**`priest_shadow_1`** Gabriel: “The Shadow protects us. It keeps us safe and comforts us when we sleep.”

    - Next → [priest_shadow_2](#d-priest_shadow_2)

    <span id="d-gabriel_daw_10"></span>**`gabriel_daw_10`** Gabriel: “Do you hear it?”

    - “[You just nod up and down]” → [gabriel_daw_10_rec](#d-gabriel_daw_10_rec)
    - “[Lie] Umm I sure do.” → [gabriel_daw_20](#d-gabriel_daw_20)
    - “No, sir, I do not.” → [gabriel_daw_30](#d-gabriel_daw_30)

    <span id="d-gabriel_daw_incomplete_10"></span>**`gabriel_daw_incomplete_10`** Gabriel: “The noise, my child! It's coming from over there. [He points east]”

    - Next → [gabriel_daw_incomplete_20](#d-gabriel_daw_incomplete_20)

    <span id="d-gabriel_daw_complete_10"></span>**`gabriel_daw_complete_10`** Gabriel: “Well, for that, I am eternally grateful.”

    - “How 'grateful' are you?” → [gabriel_daw_complete_15](#d-gabriel_daw_complete_15)
    - “I will do anything for the Shadow.” → [gabriel_daw_complete_13](#d-gabriel_daw_complete_13)

    <span id="d-priest_shadow_2"></span>**`priest_shadow_2`** Gabriel: “It follows us wherever we go. Go with the Shadow my child.”

    - “Shadow be with you.” → *conversation ends*
    - “Whatever, bye.” → *conversation ends*

    <span id="d-gabriel_daw_10_rec"></span>**`gabriel_daw_10_rec`** Gabriel: “Speak, child.”

    - Next → [gabriel_daw_10](#d-gabriel_daw_10)

    <span id="d-gabriel_daw_20"></span>**`gabriel_daw_20`** Gabriel: “What do you hear?”

    - “The Shadow. It talks to me too.” → [gabriel_daw_20_lie](#d-gabriel_daw_20_lie)
    - “The birds are singing today. I also like to listen to them.” → [gabriel_daw_20_birds](#d-gabriel_daw_20_birds)

    <span id="d-gabriel_daw_30"></span>**`gabriel_daw_30`** Gabriel: “It's coming from over there. [He points east]”

    - Next → [gabriel_daw_35](#d-gabriel_daw_35)

    <span id="d-gabriel_daw_incomplete_20"></span>**`gabriel_daw_incomplete_20`** Gabriel: “I asked you to go investigate the noise and stop it if it is a threat”

    - “Oh yeah. Sorry. I will get on top of that right away.” → *conversation ends*

    <span id="d-gabriel_daw_complete_15"></span>**`gabriel_daw_complete_15`** Gabriel: “I will get to that momentarily.”

    - Next → [gabriel_daw_complete_20](#d-gabriel_daw_complete_20)

    <span id="d-gabriel_daw_complete_13"></span>**`gabriel_daw_complete_13`** Gabriel: “Thank you, my child.”

    - Next → [gabriel_daw_complete_20](#d-gabriel_daw_complete_20)

    <span id="d-gabriel_daw_20_lie"></span>**`gabriel_daw_20_lie`** Gabriel: “You lie!”


    <span id="d-gabriel_daw_20_birds"></span>**`gabriel_daw_20_birds`** Gabriel: “No! Not that.”


    <span id="d-gabriel_daw_35"></span>**`gabriel_daw_35`** Gabriel: “Clear your mind and you will hear it.”

    - “You are crazy. I'm out of here.” → *conversation ends*
    - “How do I clear my mind?” → [gabriel_daw_40](#d-gabriel_daw_40)

    <span id="d-gabriel_daw_complete_20"></span>**`gabriel_daw_complete_20`** Gabriel: “Please tell me what was causing the noise?”

    - “A demonic creature and its minions rose from their graves and were roaming the forest.” → [gabriel_daw_complete_30](#d-gabriel_daw_complete_30)

    <span id="d-gabriel_daw_40"></span>**`gabriel_daw_40`** Gabriel: “Close your eyes.”

    - “Yeah, you're scaring me. Maybe I'll come back later.” → *conversation ends*
    - “Sure. I'll close my eyes now, but don't try anything that you will regret.” → [gabriel_daw_50](#d-gabriel_daw_50)

    <span id="d-gabriel_daw_complete_30"></span>**`gabriel_daw_complete_30`** Gabriel: “Anything else?”

    - “They inhabited this abandoned house in the forest and were doing some sort of ritual. I think that they were planning…” → [gabriel_daw_complete_40](#d-gabriel_daw_complete_40)

    <span id="d-gabriel_daw_50"></span>**`gabriel_daw_50`** Gabriel: “Do you hear it now?”

    - “Yes, I think so. It sounds like moaning of some kind.” → [gabriel_daw_60](#d-gabriel_daw_60)

    <span id="d-gabriel_daw_complete_40"></span>**`gabriel_daw_complete_40`** Gabriel: “This is indeed alarming. But we are so grateful for your work here.”

    - “How 'grateful' are you?” → [gabriel_daw_complete_50](#d-gabriel_daw_complete_50)
    - “I will do anything for the Shadow.” → [gabriel_daw_complete_49](#d-gabriel_daw_complete_49)

    <span id="d-gabriel_daw_60"></span>**`gabriel_daw_60`** Gabriel: “Yes! Finally. Someone else that can hear it.”

    - “This is scaring me. I'm going home to father.” → *conversation ends*
    - “What is it?” → [gabriel_daw_70](#d-gabriel_daw_70)

    <span id="d-gabriel_daw_complete_50"></span>**`gabriel_daw_complete_50`** Gabriel: “Very! In fact, here are 3,000 gold pieces for all your trouble.” — **effects:** gives [Gold coins](../items/gold.md), sets stage 70 of [The Dead are Walking](../quests/dead_walking.md#stage-70)


    <span id="d-gabriel_daw_complete_49"></span>**`gabriel_daw_complete_49`** Gabriel: “Walk with the Shadow, my child.” — **effects:** sets stage 70 of [The Dead are Walking](../quests/dead_walking.md#stage-70), faction “factionCountShadow” set to 2


    <span id="d-gabriel_daw_70"></span>**`gabriel_daw_70`** Gabriel: “I have no idea and the other villagers think I am crazy. Do you think I'm crazy?”

    - “Maybe, but I'm intrigued, so I will say 'no'.” → [gabriel_daw_80](#d-gabriel_daw_80)
    - “Oh, absolutely.” → *conversation ends*

    <span id="d-gabriel_daw_80"></span>**`gabriel_daw_80`** Gabriel: “OK. I fear that whatever it is, it is coming for this church and the village.”

    - Next → [gabriel_daw_85](#d-gabriel_daw_85)

    <span id="d-gabriel_daw_85"></span>**`gabriel_daw_85`** Gabriel: “I am not an adventurer, and I am certainly not a fighter.”

    - “Obviously.” → [gabriel_daw_90](#d-gabriel_daw_90)

    <span id="d-gabriel_daw_90"></span>**`gabriel_daw_90`** Gabriel: “I need someone willing and able. Will you go investigate the noise and stop it if it is a threat?”

    - “Of course. Anything for the Shadow.” → [gabriel_daw_100](#d-gabriel_daw_100)
    - “If there is a reward, why not?” → [gabriel_daw_100](#d-gabriel_daw_100)
    - “I don't think I am ready.” → *conversation ends*

    <span id="d-gabriel_daw_100"></span>**`gabriel_daw_100`** Gabriel: “Outstanding. Report back to me when you are done.” — **effects:** sets stage 0 of [The Dead are Walking](../quests/dead_walking.md#stage-0)




## Version history

| Version | Change |
|---|---|
| [v0.8.3](../versions/0.8.3.md) | Added<br>Dialogue: 30 lines added |
| [v0.8.14](../versions/0.8.14.md) | Dialogue: 1 line changed |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “Very! In fact, here are 3000 gold pieces for all your trouble.” → “Very! In fact, here are {3000} gold pieces for all your trouble.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gabriel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gabriel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gabriel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gabriel.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `gabriel` |
    | Spawn group | `gabriel` |
    | Loot table | – |
    | Conversation | `gabriel` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:4` |
    | Defined in | `res/raw/monsterlist_haunted_forest.json` |

    Raw data:

    ```json
    {
     "id": "gabriel",
     "name": "Gabriel",
     "iconID": "monsters_men:4",
     "phraseID": "gabriel"
    }
    ```


<small>Data from v0.8.18</small>
