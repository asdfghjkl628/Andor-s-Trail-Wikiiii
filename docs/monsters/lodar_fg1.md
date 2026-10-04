# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Feygard guard

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `lodar_fg1` |
| **Type** | NPC |
| **Class** | ? |
| **HP** | 1 |
| **Found in** | Loneford |
| **Introduced** | v0.7.0 or earlier |

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
| [lodar2](../maps/lodar2.md) | Loneford | 1 | – |


## Quests

- [A lost potion](../quests/lodar.md): stages 50, 51

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Feygard guard. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/lodar_fg1.json" data-npc="Feygard guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (22 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-lodar_fg1"></span>**`lodar_fg1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 51 of [A lost potion](../quests/lodar.md#stage-51))* → [lodar_fg1_r1](#d-lodar_fg1_r1)
    - branch 2 *(if reached stage 50 of [A lost potion](../quests/lodar.md#stage-50))* → [lodar_fg1_r2](#d-lodar_fg1_r2)
    - branch 3 → [lodar_fg1_1](#d-lodar_fg1_1)

    <span id="d-lodar_fg1_r1"></span>**`lodar_fg1_r1`** Feygard guard: “Oh, it's you again.”

    - Next → [lodar_fg1_17](#d-lodar_fg1_17)

    <span id="d-lodar_fg1_r2"></span>**`lodar_fg1_r2`** Feygard guard: “Oh, it's you again.”

    - Next → [lodar_fg1_2](#d-lodar_fg1_2)

    <span id="d-lodar_fg1_1"></span>**`lodar_fg1_1`** Feygard guard: “You there! What are you doing here?”

    - Next → [lodar_fg1_2](#d-lodar_fg1_2)

    <span id="d-lodar_fg1_17"></span>**`lodar_fg1_17`** Feygard guard: “I don't know if it's the twisty paths themselves or something that the madman has done that caused my fellow guards to behave the way they have - but consider yourself warned if you venture further into the forest!” — **effects:** sets stage 51 of [A lost potion](../quests/lodar.md#stage-51)

    - “I can handle myself.” → [lodar_fg1_18](#d-lodar_fg1_18)
    - “Your fellow guards must have been weak. I'm surely not as weak as them.” → [lodar_fg1_18](#d-lodar_fg1_18)
    - “OK, I'll be on the look-out for any dangers.” → [lodar_fg1_18](#d-lodar_fg1_18)

    <span id="d-lodar_fg1_2"></span>**`lodar_fg1_2`** Feygard guard: “This place is not safe. I urge you to turn back and to venture no further into this cursed forest.”

    - “I think I can handle myself.” → [lodar_fg1_3](#d-lodar_fg1_3)
    - “Cursed forest?” → [lodar_fg1_3](#d-lodar_fg1_3)
    - “OK, I'll turn back. Thanks for the warning.” → *conversation ends*

    <span id="d-lodar_fg1_18"></span>**`lodar_fg1_18`** Feygard guard: “Consider yourself warned. I can't come help you if something happens.”

    - “Goodbye.” → *NPC leaves*

    <span id="d-lodar_fg1_3"></span>**`lodar_fg1_3`** Feygard guard: “This place - oh why did we ever agree to go on this mission?”

    - “What mission?” → [lodar_fg1_4](#d-lodar_fg1_4)
    - “What has happened?” → [lodar_fg1_4](#d-lodar_fg1_4)

    <span id="d-lodar_fg1_4"></span>**`lodar_fg1_4`** Feygard guard: “Me and some other guards were sent here to find a madman that is wanted by the Feygard authorities.”

    - Next → [lodar_fg1_5](#d-lodar_fg1_5)

    <span id="d-lodar_fg1_5"></span>**`lodar_fg1_5`** Feygard guard: “The madman is wanted for a number of crimes committed against Feygard, none of which I am allowed to disclose.”

    - Next → [lodar_fg1_6](#d-lodar_fg1_6)

    <span id="d-lodar_fg1_6"></span>**`lodar_fg1_6`** Feygard guard: “At first, it seemed like just any ordinary mission - go find some crazy fool.”

    - Next → [lodar_fg1_7](#d-lodar_fg1_7)

    <span id="d-lodar_fg1_7"></span>**`lodar_fg1_7`** Feygard guard: “But once we got here, it started happening. One by one, my fellow guards got more and more ... well ... I don't know how to put it, but something started to happen to them.”

    - Next → [lodar_fg1_8a](#d-lodar_fg1_8a)

    <span id="d-lodar_fg1_8a"></span>**`lodar_fg1_8a`** Feygard guard: “Now, these flies that inhabit these woods can drive a grown man mad, I'll tell you that. But that wasn't it. There was something else.”

    - Next → [lodar_fg1_8](#d-lodar_fg1_8)

    <span id="d-lodar_fg1_8"></span>**`lodar_fg1_8`** Feygard guard: “The first guard said he had seen something among the trees, and went to look for it. We never saw him again.”

    - Next → [lodar_fg1_9](#d-lodar_fg1_9)

    <span id="d-lodar_fg1_9"></span>**`lodar_fg1_9`** Feygard guard: “Some time later, one of the other guards seemed like he didn't know who we were, and ran off into the forest.”

    - Next → [lodar_fg1_10](#d-lodar_fg1_10)

    <span id="d-lodar_fg1_10"></span>**`lodar_fg1_10`** Feygard guard: “Another guard said he'd nearly gotten lost in a what he called the 'green maze'.”

    - “So it's only you left?” → [lodar_fg1_11](#d-lodar_fg1_11)

    <span id="d-lodar_fg1_11"></span>**`lodar_fg1_11`** Feygard guard: “Yes, it seems so. None of the scouts have come back. Or rather, the ones that have come back have been ... afflicted by something.”

    - “What could be causing them to behave that way?” → [lodar_fg1_12](#d-lodar_fg1_12)

    <span id="d-lodar_fg1_12"></span>**`lodar_fg1_12`** Feygard guard: “I don't know. Maybe something in the woods.”

    - Next → [lodar_fg1_13](#d-lodar_fg1_13)

    <span id="d-lodar_fg1_13"></span>**`lodar_fg1_13`** Feygard guard: “Maybe it's something that the madman that we were looking for has done.” — **effects:** sets stage 50 of [A lost potion](../quests/lodar.md#stage-50)

    - “Any signs of the madman?” → [lodar_fg1_14](#d-lodar_fg1_14)
    - “That's a really touching story. I really need to get going.” → [lodar_fg1_16](#d-lodar_fg1_16)

    <span id="d-lodar_fg1_14"></span>**`lodar_fg1_14`** Feygard guard: “No, none.”

    - “I'll keep my eyes open for any dangers when traveling through the forest myself.” → [lodar_fg1_15](#d-lodar_fg1_15)
    - “Best of luck on your mission.” → [lodar_fg1_16](#d-lodar_fg1_16)

    <span id="d-lodar_fg1_16"></span>**`lodar_fg1_16`** Feygard guard: “Thank you.”

    - Next → [lodar_fg1_15](#d-lodar_fg1_15)

    <span id="d-lodar_fg1_15"></span>**`lodar_fg1_15`** Feygard guard: “Oh, before you go. As I told you before, one of the guards mentioned 'the green maze', that apparently is somewhere around here.”

    - “What about it?” → [lodar_fg1_17](#d-lodar_fg1_17)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 5 lines changed<br>· text: “But once we got here, it started happening. One by one, my fellow gua…” → “But once we got here, it started happening. One by one, my fellow gua…”<br>· text: “Yes, it seems so. None of the scouts have come back. Or rather, the o…” → “Yes, it seems so. None of the scouts have come back. Or rather, the o…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar_fg1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar_fg1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar_fg1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=lodar_fg1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `lodar_fg1` |
    | Spawn group | `lodar_fg1` |
    | Loot table | – |
    | Conversation | `lodar_fg1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_v070_lodarnpcs.json` |

    Raw data:

    ```json
    {
     "id": "lodar_fg1",
     "name": "Feygard guard",
     "iconID": "monsters_rltiles3:14",
     "unique": 1,
     "spawnGroup": "lodar_fg1",
     "phraseID": "lodar_fg1"
    }
    ```


<small>Data from v0.8.18</small>
