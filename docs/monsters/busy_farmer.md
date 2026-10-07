---
description: "Busy farmer is a non-player character (NPC) in Andor's Trail, found in Fallhaven, Stoutford."
---

# ![](../assets/icons/monsters/monsters_man1_0.png){ .sprite } Busy farmer

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_man1_0.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Fallhaven, Stoutford |
| **Entries in game data** | 3 |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! info "3 entries in the game data"
    The game data defines 3 separate characters named Busy farmer. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another location, other stats). Some are the same person at different story points; others just share a generic name. Here the entries differ in: conversation, location. Each entry has its own section below.

| Entry | Type | Location | Role |
|---|---|---|---|
| [`busy_farmer`](#v-busy_farmer) | NPC | Fallhaven: [Fallhaven farmer](../maps/fallhaven_farmer.md#pin-npc-busy_farmer), Fallhaven: [Fallhaven south-east](../maps/fallhaven_se.md#pin-npc-busy_farmer) | – |
| [`fallhaven_outdoor_farmer`](#v-fallhaven_outdoor_farmer) | NPC | Fallhaven: [Fallhaven south-east](../maps/fallhaven_se.md#pin-npc-fallhaven_outdoor_farmer) | – |
| [`stoutford_farmer2`](#v-stoutford_farmer2) | NPC | Stoutford: [Stoutford farmhouse 2](../maps/stoutford_farmhouse2.md#pin-npc-stoutford_farmer2) | – |

## Fallhaven, Fallhaven farmer and 1 more (busy_farmer) { #v-busy_farmer }

**Entry ID:** `busy_farmer` · **Type:** NPC

**Location:** Fallhaven: [Fallhaven farmer](../maps/fallhaven_farmer.md#pin-npc-busy_farmer), Fallhaven: [Fallhaven south-east](../maps/fallhaven_se.md#pin-npc-busy_farmer)

### Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Fallhaven farmer](../maps/fallhaven_farmer.md) | Fallhaven | 1 | – |
| [Fallhaven south-east](../maps/fallhaven_se.md) | Fallhaven | 1 | – |

### Dialogue simulator

Set your quest stages and items, then talk to Busy farmer. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/fallhaven_farmer1.json" data-npc="Busy farmer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-busy_farmer-fallhaven_farmer1"></span>**`fallhaven_farmer1`** Busy farmer: “Hello there. Please do not bother me, I have a lot of work to do.”




### Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Renamed “Busy Farmer” → “Busy farmer” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (busy_farmer)"

    | | |
    |---|---|
    | Entry ID | `busy_farmer` |
    | Spawn group | `fallhaven_farmer1` |
    | Loot table | – |
    | Conversation | `fallhaven_farmer1` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_fallhaven_npcs.json` |

    Raw data:

    ```json
    {
     "id": "busy_farmer",
     "name": "Busy farmer",
     "iconID": "monsters_man1:0",
     "monsterClass": "humanoid",
     "spawnGroup": "fallhaven_farmer1",
     "phraseID": "fallhaven_farmer1"
    }
    ```


## Fallhaven, Fallhaven south-east (fallhaven_outdoor_farmer) { #v-fallhaven_outdoor_farmer }

**Entry ID:** `fallhaven_outdoor_farmer` · **Type:** NPC

**Location:** Fallhaven: [Fallhaven south-east](../maps/fallhaven_se.md#pin-npc-fallhaven_outdoor_farmer)

### Quests

- [A Wicked witch](../quests/wicked_witch.md): stages 20, 30, 40

### Dialogue simulator

Set your quest stages and items, then talk to Busy farmer. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/fallhaven_outdoor_farmer_10.json" data-npc="Busy farmer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (20 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_10"></span>**`fallhaven_outdoor_farmer_10`** Busy farmer: “Hello there. Please do not bother me, I have a lot of work to do.”

    - “Can I have just one minute of your time, please?” *(if reached stage 10 of [A Wicked witch](../quests/wicked_witch.md#stage-10); NOT reached stage 40 of [A Wicked witch](../quests/wicked_witch.md#stage-40))* → [fallhaven_outdoor_farmer_20](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_20)
    - “Could you tell me the story about the wicked witch again?” *(if reached stage 20 of [A Wicked witch](../quests/wicked_witch.md#stage-20); NOT reached stage 40 of [A Wicked witch](../quests/wicked_witch.md#stage-40))* → [fallhaven_outdoor_farmer_77](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_77)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_20"></span>**`fallhaven_outdoor_farmer_20`** Busy farmer: “I suppose.”

    - “Great! I was wondering if you know anything about a kidnapping or a witch?” → [fallhaven_outdoor_farmer_30](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_30)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_77"></span>**`fallhaven_outdoor_farmer_77`** Busy farmer: “My story starts a very long time ago, when I was just a kid.”

    - “Great, more stories with grandpa.” → [fallhaven_outdoor_farmer_78](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_78)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_30"></span>**`fallhaven_outdoor_farmer_30`** Busy farmer: “[Taken aback by the question] What did you just ask me?”

    - “I asked if you know anything about a witch and the possibility that she took a girl.” → [fallhaven_outdoor_farmer_40](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_40)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_78"></span>**`fallhaven_outdoor_farmer_78`** Busy farmer: “You see, one day, my best friend Addie and I were playing amongst the trees south of town when we encountered her.”

    - Next → [fallhaven_outdoor_farmer_79](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_79)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_40"></span>**`fallhaven_outdoor_farmer_40`** Busy farmer: “Leave me alone! I don't want to talk about her!”

    - “Ok. I'm sorry I asked.” → *conversation ends*
    - “So you know something about the kidnapping?” → [fallhaven_outdoor_farmer_45](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_45)
    - “What about the witch? Do you know something about her?” → [fallhaven_outdoor_farmer_50](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_50)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_79"></span>**`fallhaven_outdoor_farmer_79`** Busy farmer: “She was a young beautiful woman, but terrifyingly alluring. So much so, that she easily coerced us into following her into her house.” — **effects:** sets stage 20 of [A Wicked witch](../quests/wicked_witch.md#stage-20)

    - “I see. What happened next?” → [fallhaven_outdoor_farmer_80](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_80)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_45"></span>**`fallhaven_outdoor_farmer_45`** Busy farmer: “Nope!”

    - “Are you sure?” → [fallhaven_outdoor_farmer_40](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_40)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_50"></span>**`fallhaven_outdoor_farmer_50`** Busy farmer: “I may, but I don't want to tell you about her as I am terrified of her.”

    - “Wow! Now I have to learn what you know. Please tell me your story.” → [fallhaven_outdoor_farmer_60](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_60)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_80"></span>**`fallhaven_outdoor_farmer_80`** Busy farmer: “Now, I will tell you right now that I have chosen to block out most of the details as it was such a painful experience.”

    - “Understandable.” → [fallhaven_outdoor_farmer_81](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_81)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_60"></span>**`fallhaven_outdoor_farmer_60`** Busy farmer: “No way! I have no way to protect myself and believe me, I will need to if I tell you anything.”

    - “I will protect you. Trust me.” → [fallhaven_outdoor_farmer_65](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_65)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_81"></span>**`fallhaven_outdoor_farmer_81`** Busy farmer: “All I remember was being kept in a dark room for what felt like weeks without food and being alone. You see, the witch kept Addie in another room ... I think.”

    - “You think?” → [fallhaven_outdoor_farmer_82](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_82)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_65"></span>**`fallhaven_outdoor_farmer_65`** Busy farmer: “[Laughing uncontrollably] ... You? You are just a child of a farmer. So you are weaker than I am.”

    - “You know my father?” → [fallhaven_outdoor_farmer_66](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_66)
    - “I can protect you.” → [fallhaven_outdoor_farmer_70](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_70)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_82"></span>**`fallhaven_outdoor_farmer_82`** Busy farmer: “Yes. You see, after I escaped, I never saw Addie again.” — **effects:** sets stage 30 of [A Wicked witch](../quests/wicked_witch.md#stage-30)

    - “That's terrible.” → [fallhaven_outdoor_farmer_83](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_83)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_66"></span>**`fallhaven_outdoor_farmer_66`** Busy farmer: “Of course I do. He lives a stones throw away from me and we are both farmers.”

    - “Oh. I didn't know. But I can protect you.” → [fallhaven_outdoor_farmer_70](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_70)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_70"></span>**`fallhaven_outdoor_farmer_70`** Busy farmer: “And how can you do that? Have you ever done anything like this before?”

    - “Well, actually, I have. In fact, I just finished protecting this entire town from a giant snake.” → [fallhaven_outdoor_farmer_75](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_75)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_83"></span>**`fallhaven_outdoor_farmer_83`** Busy farmer: “After a couple of weeks passed, I saw a chance to escape and I took it. Never to look back and never to talk about it. Well, until now.”

    - “Thank you for telling me your story. I want to stop this witch once and for all. Where can I find her?” → [fallhaven_outdoor_farmer_84](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_84)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_75"></span>**`fallhaven_outdoor_farmer_75`** Busy farmer: “That was you?”

    - “Yes.” → [fallhaven_outdoor_farmer_76](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_76)

    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_84"></span>**`fallhaven_outdoor_farmer_84`** Busy farmer: “Thank you! You can find her house just south of here. You can't miss it as it is covered in beautiful flowers.” — **effects:** sets stage 40 of [A Wicked witch](../quests/wicked_witch.md#stage-40)


    <span id="d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_76"></span>**`fallhaven_outdoor_farmer_76`** Busy farmer: “Well, if that's the case, then I will tell you my story.”

    - “Thank you.” → [fallhaven_outdoor_farmer_77](#d-fallhaven_outdoor_farmer-fallhaven_outdoor_farmer_77)



### Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added<br>Dialogue: 20 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (fallhaven_outdoor_farmer)"

    | | |
    |---|---|
    | Entry ID | `fallhaven_outdoor_farmer` |
    | Spawn group | `fallhaven_outdoor_farmer` |
    | Loot table | – |
    | Conversation | `fallhaven_outdoor_farmer_10` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_mt_galmore.json` |

    Raw data:

    ```json
    {
     "id": "fallhaven_outdoor_farmer",
     "name": "Busy farmer",
     "iconID": "monsters_man1:0",
     "monsterClass": "humanoid",
     "spawnGroup": "fallhaven_outdoor_farmer",
     "phraseID": "fallhaven_outdoor_farmer_10"
    }
    ```


## Stoutford, Stoutford farmhouse 2 (stoutford_farmer2) { #v-stoutford_farmer2 }

**Entry ID:** `stoutford_farmer2` · **Type:** NPC

**Location:** Stoutford: [Stoutford farmhouse 2](../maps/stoutford_farmhouse2.md#pin-npc-stoutford_farmer2)

### Dialogue simulator

Set your quest stages and items, then talk to Busy farmer. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/stoutford_farmer2.json" data-npc="Busy farmer" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (1 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-stoutford_farmer2-stoutford_farmer2"></span>**`stoutford_farmer2`** Busy farmer: “Hello there. Please do not bother me, I have a lot of work to do.”




### Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 1 line added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information (stoutford_farmer2)"

    | | |
    |---|---|
    | Entry ID | `stoutford_farmer2` |
    | Spawn group | `stoutford_farmer2` |
    | Loot table | – |
    | Conversation | `stoutford_farmer2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_man1:0` |
    | Defined in | `res/raw/monsterlist_stoutford_combined.json` |

    Raw data:

    ```json
    {
     "id": "stoutford_farmer2",
     "name": "Busy farmer",
     "iconID": "monsters_man1:0",
     "monsterClass": "humanoid",
     "spawnGroup": "stoutford_farmer2",
     "phraseID": "stoutford_farmer2"
    }
    ```



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=busy_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=busy_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=busy_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=busy_farmer.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
