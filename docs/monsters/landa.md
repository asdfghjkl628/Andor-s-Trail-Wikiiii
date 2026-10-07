# ![](../assets/icons/monsters/monsters_men_0.png){ .sprite } Landa

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_0.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `landa` |
| **Type** | NPC |
| **Class** | Humanoid |
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
| [loneford6](../maps/loneford6.md) | Loneford | 1 | – |


## Quests

- [Flows through the veins](../quests/loneford.md): stages 30, 31, 35

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Landa. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/landa.json" data-npc="Landa" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (21 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-landa"></span>**`landa`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 35 of [Flows through the veins](../quests/loneford.md#stage-35))* → [landa_already_1](#d-landa_already_1)
    - branch 2 → [landa_1](#d-landa_1)

    <span id="d-landa_already_1"></span>**`landa_already_1`** Landa: “You again? I already told you. Get out of here before anyone sees you talking to me.”


    <span id="d-landa_1"></span>**`landa_1`** Landa: “Wha? You!? No, get away from me!”

    - “I heard that you saw something that you won't talk about.” *(if reached stage 25 of [Flows through the veins](../quests/loneford.md#stage-25))* → [landa_2](#d-landa_2)

    <span id="d-landa_2"></span>**`landa_2`** Landa: “[Landa gives you a terrified look]”

    - Next → [landa_3](#d-landa_3)

    <span id="d-landa_3"></span>**`landa_3`** Landa: “You were there! I ssssaw you!”

    - Next → [landa_4](#d-landa_4)

    <span id="d-landa_4"></span>**`landa_4`** Landa: “Or was it you? No, it looked like you, and I have a good memory! [Bites lip]”

    - “Calm down.” → [landa_5](#d-landa_5)

    <span id="d-landa_5"></span>**`landa_5`** Landa: “Get away from me, whatever you did over there, it's your business and I don't want any trouble!”

    - “You must have me confused with someone else.” → [landa_6](#d-landa_6)

    <span id="d-landa_6"></span>**`landa_6`** Landa: “Please don't hurt me!”

    - “Landa, you must have me confused with someone else! What was it you saw?” → [landa_7](#d-landa_7)

    <span id="d-landa_7"></span>**`landa_7`** Landa: “No, you are smaller than him.”

    - “Are you going to tell me what it was you saw?” → [landa_8](#d-landa_8)

    <span id="d-landa_8"></span>**`landa_8`** Landa: “The boy. He was doing something. I tried to sneak up closer to see what it was he was doing, I did. But he ran away before I could see.”

    - Next → [landa_9](#d-landa_9)

    <span id="d-landa_9"></span>**`landa_9`** Landa: “He did something by the well here in Loneford.”

    - “When was this?” → [landa_10](#d-landa_10)

    <span id="d-landa_10"></span>**`landa_10`** Landa: “It was in the middle of the night, on the day before everything started. The day after, I was sleeping it off during the day, so I didn't notice all the turmoil about when they brought Hesor back.”

    - Next → [landa_11](#d-landa_11)

    <span id="d-landa_11"></span>**`landa_11`** Landa: “Almost the whole village wanted to see what had happened to Hesor. I kept to myself and didn't dare talk to anyone.” — **effects:** sets stage 30 of [Flows through the veins](../quests/loneford.md#stage-30)

    - Next → [landa_12](#d-landa_12)

    <span id="d-landa_12"></span>**`landa_12`** Landa: “The same day, others started to get pale as well. I could see it in their faces.”

    - Next → [landa_13](#d-landa_13)

    <span id="d-landa_13"></span>**`landa_13`** Landa: “The following night, I was getting ready to go to the well myself to look for any traces of what the boy had done.”

    - Next → [landa_14](#d-landa_14)

    <span id="d-landa_14"></span>**`landa_14`** Landa: “I peeked out the window to see if there was anyone that might see me. Instead, I saw someone skulking around the well, filling up several vials with both dirt around the well, and water from the well itself.”

    - Next → [landa_15](#d-landa_15)

    <span id="d-landa_15"></span>**`landa_15`** Landa: “I am sure it was Buceth, from the chapel. I have a good eye for people, and a good memory. Yes, I am sure it was Buceth.”

    - Next → [landa_16](#d-landa_16)

    <span id="d-landa_16"></span>**`landa_16`** Landa: “Also, isn't it strange how Buceth has not gotten ill, while all the others in the village have gotten ill?” — **effects:** sets stage 31 of [Flows through the veins](../quests/loneford.md#stage-31)

    - Next → [landa_17](#d-landa_17)

    <span id="d-landa_17"></span>**`landa_17`** Landa: “He must be up to something. He and that boy that looked like you. Are you sure it wasn't you?” — **effects:** sets stage 35 of [Flows through the veins](../quests/loneford.md#stage-35)

    - Next → [landa_18](#d-landa_18)

    <span id="d-landa_18"></span>**`landa_18`** Landa: “Never mind. Please don't tell anyone that I told you all this.”

    - Next → [landa_19](#d-landa_19)

    <span id="d-landa_19"></span>**`landa_19`** Landa: “Now, get out of here kid, before anyone sees you talking to me. [Looks around anxiously]”

    - “Thank you Landa. Your secret is safe with me.” → *conversation ends*
    - “Thank you Landa. I'll consider it.” → *conversation ends*
    - “Are you done? Phew, I thought you were never going to stop talking.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 5 lines changed<br>· text: “Now, get out of here kid, before anyone sees you talking to me. *Look…” → “Now, get out of here kid, before anyone sees you talking to me. [Look…”<br>· text: “Or was it you? No, it looked like you, and I have a good memory! *bit…” → “Or was it you? No, it looked like you, and I have a good memory! [Bit…” |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 1 line changed<br>· text: “Also, isn't it strange how Buceth has not gotten ill, while all the o…” → “Also, isn't it strange how Buceth has not gotten ill, while all the o…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=landa.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=landa.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=landa.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=landa.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `landa` |
    | Spawn group | `landa` |
    | Loot table | – |
    | Conversation | `landa` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:0` |
    | Defined in | `res/raw/monsterlist_v0610_npcs1.json` |

    Raw data:

    ```json
    {
     "id": "landa",
     "name": "Landa",
     "iconID": "monsters_men:0",
     "monsterClass": "humanoid",
     "spawnGroup": "landa",
     "phraseID": "landa"
    }
    ```


<small>Data from v0.8.18</small>
