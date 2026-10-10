---
description: "Valeria is a non-player character (NPC) in Andor's Trail, found in Sullengard."
---

# ![](../assets/icons/monsters/monsters_ld1_165.png){ .sprite } Valeria

**Where to find Valeria:** Sullengard: [Sullengard 1 aunts house](../maps/sullengard1_aunts_house.md#pin-npc-sullengard_valeria)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_165.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Sullengard |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Quests

- [Search for Andor](../quests/andor.md): stage 100

## Dialogue simulator

Talk to Valeria as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_valeria_selector.json" data-npc="Valeria" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (17 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-sullengard_valeria_selector"></span>**`sullengard_valeria_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 100 of [Search for Andor](../quests/andor.md#stage-100))* → [sullengard_valentina_0](#d-sullengard_valentina_0)
    - Next *(if reached stage 100 of [Search for Andor](../quests/andor.md#stage-100))* → [sullengard_valeria_15](#d-sullengard_valeria_15)

    <span id="d-sullengard_valentina_0"></span>**`sullengard_valentina_0`** [Valentina](../monsters/crossglen_valentina.md#v-sullengard_valentina): “$playername, what are you doing here?!”

    - “Mom, I could ask you the same question.” → [sullengard_find_mother_10](#d-sullengard_find_mother_10)

    <span id="d-sullengard_valeria_15"></span>**`sullengard_valeria_15`** Valeria: “Hello $playername.”

    - “So, you are my Aunt Valeria, whom I only just learned even exists. Why am I just meeting you now?” → [sullengard_valeria_20](#d-sullengard_valeria_20)

    <span id="d-sullengard_find_mother_10"></span>**`sullengard_find_mother_10`** Valeria: “I'm your mother, answer my question.”

    - “Father sent me to look for Andor as he left shortly after you did and hasn't returned.” → [sullengard_find_mother_20](#d-sullengard_find_mother_20)

    <span id="d-sullengard_valeria_20"></span>**`sullengard_valeria_20`** Valeria: “I'm sorry $playername, but I am in no position to answer that question for you. Please do as your mother has requested of you and go home. There you will find your answer.”

    - “OK. I will do that.” → *conversation ends*
    - “But, I've already done that and she didn't answer my question.” *(if reached stage 110 of [Search for Andor](../quests/andor.md#stage-110))* → [sullengard_valeria_30](#d-sullengard_valeria_30)

    <span id="d-sullengard_find_mother_20"></span>**`sullengard_find_mother_20`** Valeria: “What?! Where is he? Why is your father not with you?”

    - “I guess because he needed to stay home and watch over the house. Or maybe he thinks I'm ready for the challenge?” → [sullengard_find_mother_30](#d-sullengard_find_mother_30)

    <span id="d-sullengard_valeria_30"></span>**`sullengard_valeria_30`** Valeria: “I'm sorry $playername, but I am in no position to answer that question for you. When your mother is ready, she will explain why.”

    - “OK...I guess I'll have to wait.” → *conversation ends*

    <span id="d-sullengard_find_mother_30"></span>**`sullengard_find_mother_30`** Valeria: “Typical Mikhail! So lazy and irresponsible.”

    - “I guess, but I can handle myself and have learned a lot about Andor.” → [sullengard_find_mother_33](#d-sullengard_find_mother_33)
    - “I totally agree with you.” → [sullengard_find_mother_35](#d-sullengard_find_mother_35)

    <span id="d-sullengard_find_mother_33"></span>**`sullengard_find_mother_33`** Valeria: “You've grown up so fast. Stop doing that. You are making me feel old.”

    - “Sorry, mother. You have still not answered my question though. What are you doing here?” → [sullengard_find_mother_40](#d-sullengard_find_mother_40)

    <span id="d-sullengard_find_mother_35"></span>**`sullengard_find_mother_35`** Valeria: “Don't you dare talk ill of your father. He may be lazy, but he is still your father.”

    - “Sorry, mother. You are right, but you have still not answered my question. What are you doing here?” → [sullengard_find_mother_40](#d-sullengard_find_mother_40)

    <span id="d-sullengard_find_mother_40"></span>**`sullengard_find_mother_40`** Valeria: “I'm visiting my sister, your aunt Valeria.”

    - “Your sister? My aunt? What are you talking about?” → [sullengard_find_mother_50](#d-sullengard_find_mother_50)

    <span id="d-sullengard_find_mother_50"></span>**`sullengard_find_mother_50`** Valeria: “Yes, $playername. This is your aunt Valeria. Please say "hi".”

    - “Um...it's nice to meet you aunt Valeria.” → [sullengard_valeria_0](#d-sullengard_valeria_0)

    <span id="d-sullengard_valeria_0"></span>**`sullengard_valeria_0`** [Valeria](../monsters/sullengard_valeria.md): “Hello $playername, it's so wonderful to finally meet you after all of these years.”

    - “But, I don't have an aunt?” *(if NOT reached stage 100 of [Search for Andor](../quests/andor.md#stage-100))* → [sullengard_find_mother_60](#d-sullengard_find_mother_60)
    - “How come mother never spoke of you or told me that she had a sister?” → [sullengard_valeria_10](#d-sullengard_valeria_10)

    <span id="d-sullengard_find_mother_60"></span>**`sullengard_find_mother_60`** [Valentina](../monsters/crossglen_valentina.md#v-sullengard_valentina): “$playername, I will explain this to you later.”

    - “OK, you promise?” → [sullengard_find_mother_70](#d-sullengard_find_mother_70)

    <span id="d-sullengard_valeria_10"></span>**`sullengard_valeria_10`** Valeria: “That is not for me to tell you. Maybe back at home, she will explain it to you.”

    - Next → [sullengard_find_mother_60](#d-sullengard_find_mother_60)

    <span id="d-sullengard_find_mother_70"></span>**`sullengard_find_mother_70`** Valeria: “Yes, but in the meantime, I'm going home and I expect you there shortly after me.”

    - “But what about my search for Andor? Father expects me to find him before I come home again.” → [sullengard_find_mother_80](#d-sullengard_find_mother_80)

    <span id="d-sullengard_find_mother_80"></span>**`sullengard_find_mother_80`** Valeria: “Just follow me home and we can talk there. I may have something to aid you in your search for Andor.” — **effects:** sets stage 100 of [Search for Andor](../quests/andor.md#stage-100), removes monsters from sullengard1_aunts_house, spawns monsters on home




## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 17 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sullengard_valeria` |
    | Type (wiki) | NPC |
    | Spawn group | `sullengard_valeria` |
    | Loot table | – |
    | Conversation | `sullengard_valeria_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:165` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_valeria",
     "name": "Valeria",
     "iconID": "monsters_ld1:165",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "sullengard_valeria",
     "phraseID": "sullengard_valeria_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_valeria.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_valeria.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_valeria.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_valeria.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
