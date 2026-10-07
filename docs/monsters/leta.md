---
description: "Leta is an NPC who can also be fought in Andor's Trail. Starts Missing husband."
---

# ![](../assets/icons/monsters/monsters_men_2.png){ .sprite } Leta

**Where to find Leta:** not placed on any map; appears through a quest or scripted event.

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_men_2.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC/Enemy (can be spoken to, but can also be fought) |
| **Role** | Starts [Missing husband](../quests/leta.md) |
| **Class** | Humanoid |
| **HP** | 1 |
| **XP when defeated** | 1 |
| **Entry ID** | `leta` |
| **Introduced** | v0.7.0 or earlier |

</div>

!!! warning "Can be fought"
    This entry can be talked to, but it can also become an opponent: a conversation with this character can end in combat (a dialogue branch leads to a fight).

No combat statistics are defined for this entry in the game data. Where the story leads to a fight, the game normally uses a separate hostile entry.

## Quests

- [A familiar shadow](../quests/familiar_shadow.md): stage 40
- [Missing husband](../quests/leta.md): stages 10, 30, 50, 70, 100
- [Thief apprentice](../quests/Thieves01.md): stage 25

## Dialogue simulator

Set the quest stages, items and other conditions that apply to your game, then start the conversation with Leta. The simulator applies the game's own rules: it performs the same silent checks, offers only the options that would be shown in the game, and applies their effects (quest stages, items handed over, rewards) as the conversation proceeds.

<div class="dlg-sim" data-src="../../assets/dialogue/leta_selector.json" data-npc="Leta" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (31 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-leta_selector"></span>**`leta_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [A familiar shadow](../quests/familiar_shadow.md#stage-30))* → [galmore_marked_stone_leta_5](#d-galmore_marked_stone_leta_5)
    - branch 2 → [leta1](#d-leta1)

    <span id="d-galmore_marked_stone_leta_5"></span>**`galmore_marked_stone_leta_5`** [Dummy NPC](../monsters/none.md): “Clearly more agitated than usual, pacing and muttering.”

    - Next → [galmore_marked_stone_leta_10](#d-galmore_marked_stone_leta_10)

    <span id="d-leta1"></span>**`leta1`** [Leta](../monsters/leta.md): “Hey, this is my house, get out of here!”

    - “But I was just ...” → [leta2](#d-leta2)
    - “What about your husband Oromir?” → [leta_oromir_select](#d-leta_oromir_select)
    - “Umar sent me.” *(if reached stage 20 of [Thief apprentice](../quests/Thieves01.md#stage-20); NOT reached stage 25 of [Thief apprentice](../quests/Thieves01.md#stage-25))* → [leta_guild_1a](#d-leta_guild_1a)
    - “Umar sent me.” *(if reached stage 25 of [Thief apprentice](../quests/Thieves01.md#stage-25))* → [leta_guild_1b](#d-leta_guild_1b)

    <span id="d-galmore_marked_stone_leta_10"></span>**`galmore_marked_stone_leta_10`** [Leta](../monsters/leta.md): “I am most certainly not in the mood to deal with you right now. Why can't Mikhail ever control his kids?”

    - “Leta, are you all right? Mikhail said you've been acting strange.” → [galmore_marked_stone_leta_30](#d-galmore_marked_stone_leta_30)

    <span id="d-leta2"></span>**`leta2`** Leta: “Beat it kid, get out of my house!”

    - “What about your husband Oromir?” → [leta_oromir_select](#d-leta_oromir_select)

    <span id="d-leta_oromir_select"></span>**`leta_oromir_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 100 of [Missing husband](../quests/leta.md#stage-100))* → [leta_oromir_complete2](#d-leta_oromir_complete2)
    - branch 2 *(if NOT reached stage 105 of [Missing husband](../quests/leta.md#stage-105); NOT reached stage 100 of [Missing husband](../quests/leta.md#stage-100))* → [leta_oromir1](#d-leta_oromir1)
    - branch 3 *(if reached stage 105 of [Missing husband](../quests/leta.md#stage-105))* → [leta_oromir_complete2_helped_oromir](#d-leta_oromir_complete2_helped_oromir)

    <span id="d-leta_guild_1a"></span>**`leta_guild_1a`** Leta: “Umar you say? I don't know any Umar!”

    - “[Whispering] You are no one. No one knows you. No one has seen you.” → [leta_guild_2](#d-leta_guild_2)

    <span id="d-leta_guild_1b"></span>**`leta_guild_1b`** Leta: “I gave you all the information I have gathered. Now leave me alone.”

    - “OK, bye.” → *conversation ends*
    - “Shadow be with you.” → *conversation ends*

    <span id="d-galmore_marked_stone_leta_30"></span>**`galmore_marked_stone_leta_30`** Leta: “Strange? Who does he think he is, meddling in my life? I'm fine! Just...leave me alone!”

    - “You don't seem fine. You've been pacing, muttering to yourself. Something isn't right.” → [galmore_marked_stone_leta_40n](#d-galmore_marked_stone_leta_40n)

    <span id="d-leta_oromir_complete2"></span>**`leta_oromir_complete2`** Leta: “Thanks for telling me about Oromir earlier. I will go get him in just a minute.”


    <span id="d-leta_oromir1"></span>**`leta_oromir1`** Leta: “Do you know anything about my husband? He should be here helping me with the farm today, but he seems to be missing as usual. Sigh.”

    - “I have no idea.” → [leta_oromir2](#d-leta_oromir2)
    - “Yes, I found him. He is hiding among some trees to the east.” *(if reached stage 20 of [Missing husband](../quests/leta.md#stage-20); NOT reached stage 35 of [Missing husband](../quests/leta.md#stage-35); NOT reached stage 45 of [Missing husband](../quests/leta.md#stage-45); NOT reached stage 40 of [Missing husband](../quests/leta.md#stage-40); NOT reached stage 60 of [Missing husband](../quests/leta.md#stage-60); NOT reached stage 80 of [Missing husband](../quests/leta.md#stage-80); NOT reached stage 25 of [Missing husband](../quests/leta.md#stage-25))* → [leta_oromir1_trees](#d-leta_oromir1_trees)
    - “[Lie] I have no idea.” *(if reached stage 25 of [Missing husband](../quests/leta.md#stage-25); NOT reached stage 35 of [Missing husband](../quests/leta.md#stage-35); NOT reached stage 45 of [Missing husband](../quests/leta.md#stage-45))* → [leta_oromir1_trees_help](#d-leta_oromir1_trees_help)
    - “[Lie] I have no idea.” *(if reached stage 35 of [Missing husband](../quests/leta.md#stage-35); NOT reached stage 45 of [Missing husband](../quests/leta.md#stage-45))* → [leta_oromir1_behind_inn_help](#d-leta_oromir1_behind_inn_help)
    - “[Lie] I have no idea.” *(if reached stage 45 of [Missing husband](../quests/leta.md#stage-45))* → [leta_oromir1_behind_haystack_help](#d-leta_oromir1_behind_haystack_help)
    - “He's found a new hiding spot.” *(if reached stage 40 of [Missing husband](../quests/leta.md#stage-40); NOT reached stage 60 of [Missing husband](../quests/leta.md#stage-60); NOT reached stage 80 of [Missing husband](../quests/leta.md#stage-80))* → [leta_oromir1_behind_inn_10](#d-leta_oromir1_behind_inn_10)
    - “He's found another new hiding spot. Give him credit, he is great at avoiding work.” *(if reached stage 60 of [Missing husband](../quests/leta.md#stage-60); NOT reached stage 80 of [Missing husband](../quests/leta.md#stage-80))* → [leta_oromir1_behind_haystack_10](#d-leta_oromir1_behind_haystack_10)
    - “He's in your basement.” *(if reached stage 80 of [Missing husband](../quests/leta.md#stage-80))* → [leta_oromir1_basement_10](#d-leta_oromir1_basement_10)

    <span id="d-leta_oromir_complete2_helped_oromir"></span>**`leta_oromir_complete2_helped_oromir`** Leta: “What about him?”

    - “Nevermind. I have to be on my way.” → *conversation ends*
    - “I'm wondering, how long are you going to make him stay in the basement for?” → [leta_oromir_complete2_helped_oromir_10](#d-leta_oromir_complete2_helped_oromir_10)

    <span id="d-leta_guild_2"></span>**`leta_guild_2`** Leta: “How do you ...? Whatever, you are one of us.”

    - “Umar sent me to get your journal.” → [leta_guild_3](#d-leta_guild_3)

    <span id="d-galmore_marked_stone_leta_40n"></span>**`galmore_marked_stone_leta_40n`** [Dummy NPC](../monsters/none.md): “[Voice trembling but defensive.]”

    - Next → [galmore_marked_stone_leta_40](#d-galmore_marked_stone_leta_40)

    <span id="d-leta_oromir2"></span>**`leta_oromir2`** Leta: “If you see him, tell him to hurry back here and help me with the housework. Now get out of here!” — **effects:** sets stage 10 of [Missing husband](../quests/leta.md#stage-10)


    <span id="d-leta_oromir1_trees"></span>**`leta_oromir1_trees`** Leta: “Hiding is he? That's not surprising. Tell him to hurry back here and help me with the housework.” — **effects:** sets stage 30 of [Missing husband](../quests/leta.md#stage-30), removes monsters from crossglen, spawns monsters on crossglen


    <span id="d-leta_oromir1_trees_help"></span>**`leta_oromir1_trees_help`** Leta: “If you see him, tell him to hurry back here and help me with the housework. Now get out of here!” — **effects:** sets stage 10 of [Missing husband](../quests/leta.md#stage-10), removes monsters from crossglen, spawns monsters on crossglen


    <span id="d-leta_oromir1_behind_inn_help"></span>**`leta_oromir1_behind_inn_help`** Leta: “If you see him, tell him to hurry back here and help me with the housework. Now get out of here!” — **effects:** sets stage 10 of [Missing husband](../quests/leta.md#stage-10), removes monsters from crossglen, spawns monsters on crossglen


    <span id="d-leta_oromir1_behind_haystack_help"></span>**`leta_oromir1_behind_haystack_help`** Leta: “If you see him, tell him to hurry back here and help me with the housework. Now get out of here!” — **effects:** sets stage 10 of [Missing husband](../quests/leta.md#stage-10), removes monsters from crossglen, spawns monsters on crossglen_farmhouse_basement


    <span id="d-leta_oromir1_behind_inn_10"></span>**`leta_oromir1_behind_inn_10`** Leta: “Where?”

    - “Tucked away between the back of the inn and the woods.” → [leta_oromir1_behind_inn_20](#d-leta_oromir1_behind_inn_20)

    <span id="d-leta_oromir1_behind_haystack_10"></span>**`leta_oromir1_behind_haystack_10`** Leta: “Where?”

    - “Hiding behind a haystack.” → [leta_oromir1_behind_haystack_20](#d-leta_oromir1_behind_haystack_20)

    <span id="d-leta_oromir1_basement_10"></span>**`leta_oromir1_basement_10`** Leta: “What?! How? Oh, it doesn't matter. Thank you for finding him.” — **effects:** sets stage 100 of [Missing husband](../quests/leta.md#stage-100)


    <span id="d-leta_oromir_complete2_helped_oromir_10"></span>**`leta_oromir_complete2_helped_oromir_10`** Leta: “This is my house! I don't have to answer to you. Now get out of here!”


    <span id="d-leta_guild_3"></span>**`leta_guild_3`** Leta: “Here. Make sure you don't raise any suspicion on your future jobs. Bye kid.” — **effects:** gives 1× [Leta's Journal](../items/Leta_journal.md), sets stage 25 of [Thief apprentice](../quests/Thieves01.md#stage-25)


    <span id="d-galmore_marked_stone_leta_40"></span>**`galmore_marked_stone_leta_40`** [Leta](../monsters/leta.md): “Not right? Not right! What would you know about it? You don't know what I've seen, what I've felt!”

    - Next → [galmore_marked_stone_leta_40n2](#d-galmore_marked_stone_leta_40n2)

    <span id="d-leta_oromir1_behind_inn_20"></span>**`leta_oromir1_behind_inn_20`** Leta: “Hiding is he? That's not surprising. Tell him to hurry back here and help me with the housework.” — **effects:** removes monsters from crossglen, sets stage 50 of [Missing husband](../quests/leta.md#stage-50), spawns monsters on crossglen


    <span id="d-leta_oromir1_behind_haystack_20"></span>**`leta_oromir1_behind_haystack_20`** Leta: “Hiding is he? That's not surprising. Tell him to hurry back here and help me with the housework.” — **effects:** removes monsters from crossglen, sets stage 70 of [Missing husband](../quests/leta.md#stage-70), spawns monsters on crossglen_farmhouse_basement


    <span id="d-galmore_marked_stone_leta_40n2"></span>**`galmore_marked_stone_leta_40n2`** [Dummy NPC](../monsters/none.md): “Leta pauses, clutching her head as if in pain. Her voice shifting, darker and more guttural.”

    - “Leta, talk to me. What's going on?” → [galmore_marked_stone_leta_50](#d-galmore_marked_stone_leta_50)

    <span id="d-galmore_marked_stone_leta_50"></span>**`galmore_marked_stone_leta_50`** [Leta](../monsters/leta.md): “You want to know? You want to understand? Fine. You'll see...but you won't like what you find.”

    - Next → [galmore_marked_stone_leta_narrator](#d-galmore_marked_stone_leta_narrator)

    <span id="d-galmore_marked_stone_leta_narrator"></span>**`galmore_marked_stone_leta_narrator`** [Dummy NPC](../monsters/none.md): “A dark aura surrounds Leta as a spirit begins its manifestation. Leta lets out a cry and vanishes as the spirit rises.” — **effects:** sets stage 40 of [A familiar shadow](../quests/familiar_shadow.md#stage-40), spawns monsters on crossglen_farmhouse, removes monsters from crossglen_farmhouse, removes monsters from crossglen_farmhouse_basement, removes monsters from crossglen, removes monsters from crossglen_farmhouse_basement

    - Next → [galmore_marked_stone_spirit](#d-galmore_marked_stone_spirit)

    <span id="d-galmore_marked_stone_spirit"></span>**`galmore_marked_stone_spirit`** [Dark spirit](../monsters/crossglen_dark_spirit.md): “[taunting] You shouldn't have meddled, little one. This vessel belongs to me now, and so does its anger!”

    - “Die!” → *fight starts*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 2 lines changed |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 4 lines added, 1 line changed |
| [v0.7.12](../versions/0.7.12.md) | Dialogue: 11 lines added, 2 lines changed |
| [v0.8.14](../versions/0.8.14.md) | phraseID: leta1 → leta_selector<br>Dialogue: 10 lines added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `leta` |
    | Spawn group | `leta` |
    | Loot table | – |
    | Conversation | `leta_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_men:2` |
    | Defined in | `res/raw/monsterlist_crossglen_npcs.json` |

    Raw data:

    ```json
    {
     "id": "leta",
     "name": "Leta",
     "iconID": "monsters_men:2",
     "monsterClass": "humanoid",
     "spawnGroup": "leta",
     "phraseID": "leta_selector"
    }
    ```


??? info "How the XP value is calculated"

    The game computes each enemy's experience value when it loads the data (`MonsterTypeParser.java`):

    XP = ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × critical multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉

    Percentages are used as fractions (e.g. 60% = 0.6). Enemies whose attacks inflict a condition are worth 50 XP more. The More Exp skill adds a percentage on top.


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leta.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leta.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leta.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=leta.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
