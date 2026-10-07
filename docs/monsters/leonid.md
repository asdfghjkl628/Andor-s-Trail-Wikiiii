---
description: "Leonid is an NPC who can also be fought in Andor's Trail. Starts Disallowed substance."
---

# ![](../assets/icons/monsters/monsters_men_3.png){ .sprite } Leonid

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_3.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Role** | Starts [Disallowed substance](../quests/bonemeal.md) |
| **Class** | Humanoid |
| **HP** | 300 |
| **XP when defeated** | 210 |
| **Entries in game data** | 2 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "2 entries in the game data"
    The game's data files define 2 separate characters named Leonid. Andor's Trail stores a character as a new entry whenever it needs different behaviour, for example a different conversation at a later stage of a quest, a different location, or different combat statistics. Some entries represent the same person at different points in the story; others are different people who share a generic name. Here the entries differ in: conversation, combat statistics. This page combines them; each entry is described in its own section below.

| Entry | Type | Location | Role | HP |
|---|---|---|---|---|
| [`leonid`](#v-leonid) | NPC | Not on a map | starts [Disallowed substance](../quests/bonemeal.md) | – |
| [`ratdom_leonid`](#v-ratdom_leonid) | Enemy | Not on a map | – | 300 |

## Not placed on a map (leonid) { #v-leonid }

**Entry ID:** `leonid` · **Type:** NPC · **Role:** Starts [Disallowed substance](../quests/bonemeal.md)

**Location:** not placed on any map; this entry is added to the world by a quest or scripted event.

### Quests

- [Disallowed substance](../quests/bonemeal.md): stage 10
- [Search for Andor](../quests/andor.md): stage 10
- [TODO (hidden flag)](../quests/crossglen.md): stage 1

### Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Leonid. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/leonid1.json" data-npc="Leonid" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (15 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-leonid-leonid1"></span>**`leonid1`** Leonid: “Hello kid. You're Mikhail's youngest child aren't you? With that brother of yours. I'm Leonid, steward of Crossglen village.”

    - “Have you seen my brother Andor?” → [leonid_andor](#d-leonid-leonid_andor)
    - “What can you tell me about Crossglen?” → [leonid_crossglen](#d-leonid-leonid_crossglen)
    - “Never mind, see you later.” → [leonid_bye](#d-leonid-leonid_bye)

    <span id="d-leonid-leonid_andor"></span>**`leonid_andor`** Leonid: “Your brother? No, I haven't seen him here today. I think I saw him in here yesterday talking to Gruil. Maybe he knows more?” — **effects:** sets stage 10 of [Search for Andor](../quests/andor.md#stage-10)

    - “Thanks, I'll go talk to Gruil. There was something more I wanted to talk about.” → [leonid_continue](#d-leonid-leonid_continue)
    - “Thanks, I'll go talk to Gruil.” → [leonid_bye](#d-leonid-leonid_bye)

    <span id="d-leonid-leonid_crossglen"></span>**`leonid_crossglen`** Leonid: “As you know, this is Crossglen village. Mostly a farming community.”

    - Next → [leonid_crossglen1](#d-leonid-leonid_crossglen1)

    <span id="d-leonid-leonid_bye"></span>**`leonid_bye`** Leonid: “Shadow be with you.”

    - “Shadow be with you.” → *conversation ends*

    <span id="d-leonid-leonid_continue"></span>**`leonid_continue`** Leonid: “Anything else I can help you with?”

    - “Have you seen my brother Andor?” → [leonid_andor](#d-leonid-leonid_andor)
    - “What can you tell me about Crossglen?” → [leonid_crossglen](#d-leonid-leonid_crossglen)
    - “Never mind, see you later.” → [leonid_bye](#d-leonid-leonid_bye)

    <span id="d-leonid-leonid_crossglen1"></span>**`leonid_crossglen1`** Leonid: “We have Audir with his smithy to the southwest, Leta and her husband's cabin to the west, this town hall here and your father's cabin to the northwest.”

    - Next → [leonid_crossglen2](#d-leonid-leonid_crossglen2)

    <span id="d-leonid-leonid_crossglen2"></span>**`leonid_crossglen2`** Leonid: “That's pretty much it. We try to live a peaceful life.”

    - “Has there been any recent activity in the village?” → [leonid_crossglen3](#d-leonid-leonid_crossglen3)
    - “Let's go back to the other things we talked about.” → [leonid_continue](#d-leonid-leonid_continue)

    <span id="d-leonid-leonid_crossglen3"></span>**`leonid_crossglen3`** Leonid: “There were some recent disturbances some weeks ago that you may have noticed. Some villagers got into a fight over the new decree from Lord Geomyr.”

    - Next → [leonid_crossglen4](#d-leonid-leonid_crossglen4)

    <span id="d-leonid-leonid_crossglen4"></span>**`leonid_crossglen4`** Leonid: “Lord Geomyr issued a statement regarding the unlawful use of bonemeal as healing substance. Some villagers argued that we should oppose Lord Geomyr's word and still use it.” — **effects:** sets stage 10 of [Disallowed substance](../quests/bonemeal.md#stage-10)

    - Next → [leonid_crossglen4_1](#d-leonid-leonid_crossglen4_1)

    <span id="d-leonid-leonid_crossglen4_1"></span>**`leonid_crossglen4_1`** Leonid: “Tharal, our priest, was particularly upset and suggested we do something about Lord Geomyr.”

    - Next → [leonid_crossglen5](#d-leonid-leonid_crossglen5)

    <span id="d-leonid-leonid_crossglen5"></span>**`leonid_crossglen5`** Leonid: “Other villagers argued that we should follow Lord Geomyr's decree. Personally, I haven't decided what my thoughts are.”

    - Next → [leonid_crossglen6](#d-leonid-leonid_crossglen6)

    <span id="d-leonid-leonid_crossglen6"></span>**`leonid_crossglen6`** Leonid: “On one hand, Lord Geomyr supports Crossglen with a lot of protection. [Points to the soldiers in the hall]”

    - Next → [leonid_crossglen7](#d-leonid-leonid_crossglen7)

    <span id="d-leonid-leonid_crossglen7"></span>**`leonid_crossglen7`** Leonid: “But on the other hand, the tax and the recent changes of what's allowed are really taking a toll on Crossglen.”

    - Next → [leonid_crossglen8](#d-leonid-leonid_crossglen8)

    <span id="d-leonid-leonid_crossglen8"></span>**`leonid_crossglen8`** Leonid: “Someone should go to Castle Geomyr and talk to the steward about our situation here in Crossglen.” — **effects:** sets stage 1 of [TODO (hidden flag)](../quests/crossglen.md#stage-1)

    - Next → [leonid_crossglen9](#d-leonid-leonid_crossglen9)

    <span id="d-leonid-leonid_crossglen9"></span>**`leonid_crossglen9`** Leonid: “In the meantime, we've banned all use of bonemeal as a healing substance.”

    - “Thank you for the information. There was something more I wanted to ask you.” → [leonid_continue](#d-leonid-leonid_continue)
    - “Thank you for the information. Bye.” → [leonid_bye](#d-leonid-leonid_bye)



### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed<br>· text: “Lord Geomyr issued a statement regarding the unlawful use of Bonemeal…” → “Lord Geomyr issued a statement regarding the unlawful use of bonemeal…”<br>· text: “On one hand, Lord Geomyr supports Crossglen with a lot of protection.…” → “On one hand, Lord Geomyr supports Crossglen with a lot of protection.…” |
| [v0.8.3](../versions/0.8.3.md) | Dialogue: 1 line changed<br>· text: “Hello kid. You're Mikhail's son aren't you? With that brother of your…” → “Hello kid. You're Mikhail's youngest child aren't you? With that brot…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (leonid)"

    | | |
    |---|---|
    | Entry ID | `leonid` |
    | Spawn group | `leonid` |
    | Loot table | – |
    | Conversation | `leonid1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:3` |
    | Defined in | `res/raw/monsterlist_crossglen_npcs.json` |

    Raw data:

    ```json
    {
     "id": "leonid",
     "name": "Leonid",
     "iconID": "monsters_men:3",
     "monsterClass": "humanoid",
     "spawnGroup": "leonid",
     "phraseID": "leonid1"
    }
    ```


## Not placed on a map (ratdom_leonid) { #v-ratdom_leonid }

**Entry ID:** `ratdom_leonid` · **Type:** Enemy

**Location:** not placed on any map; this entry is added to the world by a quest or scripted event.

### Combat statistics

| Statistic | Value |
|---|---|
| Class | Humanoid |
| HP | 300 |
| XP when defeated | 210 |
| Damage | 3 to 8 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 5 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Critical hit chance | None (requires both critical skill and a critical multiplier) |


<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


### Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (ratdom_leonid)"

    | | |
    |---|---|
    | Entry ID | `ratdom_leonid` |
    | Spawn group | `ratdom_leonid` |
    | Loot table | – |
    | Conversation | – |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:3` |
    | Defined in | `res/raw/monsterlist_ratdom.json` |

    Raw data:

    ```json
    {
     "id": "ratdom_leonid",
     "name": "Leonid",
     "iconID": "monsters_men:3",
     "maxHP": 300,
     "maxAP": 10,
     "moveCost": 5,
     "monsterClass": "humanoid",
     "attackDamage": {
      "min": 3,
      "max": 8
     },
     "spawnGroup": "ratdom_leonid"
    }
    ```



??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leonid.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leonid.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leonid.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leonid.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
