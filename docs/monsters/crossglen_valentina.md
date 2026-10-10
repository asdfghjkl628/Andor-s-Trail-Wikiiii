---
description: "Valentina is a non-player character (NPC) in Andor's Trail, found in Crossglen, Sullengard."
---

# ![](../assets/icons/monsters/monsters_ld1_167.png){ .sprite } Valentina

**Where to find Valentina:** [Crossglen, Home](#v-crossglen_valentina), [Sullengard, Sullengard 1 aunts house](#v-sullengard_valentina)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_ld1_167.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Crossglen, Sullengard |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Crossglen, Home { #v-crossglen_valentina }

**Where:** Crossglen: [Home](../maps/home.md#pin-npc-crossglen_valentina)

### Quests

- [Search for Andor](../quests/andor.md): stage 110

### Dialogue simulator

Talk to Valentina as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/crossglen_valentina_selector.json" data-npc="Valentina" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (12 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-crossglen_valentina-crossglen_valentina_selector"></span>**`crossglen_valentina_selector`** *(silent check: the first matching branch below is taken)*

    - “Can we talk about Andor?” *(if reached stage 26 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-26))* → [crossglen_valentina_andor_10](#d-crossglen_valentina-crossglen_valentina_andor_10)
    - “I would like to learn more about Aunt Valeria.” *(if reached stage 26 of [Sullengard story flags (hidden flag)](../quests/sullengard_hidden.md#stage-26))* → [crossglen_valentina_valeria_10](#d-crossglen_valentina-crossglen_valentina_valeria_10)
    - “What's wrong?” → [crossglen_valentina_10](#d-crossglen_valentina-crossglen_valentina_10)

    <span id="d-crossglen_valentina-crossglen_valentina_andor_10"></span>**`crossglen_valentina_andor_10`** Valentina: “I should be able to help you, but first you have to tell me where have you been?”

    - “I've traveled great distances from home and have seen my fair share of Dhayavar during my search for Andor.” *(if reached stage 72 of [Search for Andor](../quests/andor.md#stage-72); reached stage 85 of [Search for Andor](../quests/andor.md#stage-85); reached stage 170 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-170); reached stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60))* → [crossglen_valentina_andor_20](#d-crossglen_valentina-crossglen_valentina_andor_20)
    - “I've been around a lot of Dhayavar and have spoken to a lot of people about Andor.” *(if reached stage 72 of [Search for Andor](../quests/andor.md#stage-72); reached stage 85 of [Search for Andor](../quests/andor.md#stage-85); reached stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60))* → [crossglen_valentina_andor_20](#d-crossglen_valentina-crossglen_valentina_andor_20)
    - “I've talked with a potion maker.” *(if reached stage 72 of [Search for Andor](../quests/andor.md#stage-72); NOT reached stage 85 of [Search for Andor](../quests/andor.md#stage-85); NOT reached stage 170 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-170); NOT reached stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60))* → [crossglen_valentina_andor_21](#d-crossglen_valentina-crossglen_valentina_andor_21)
    - “I've been to Remgard looking for Andor” *(if NOT reached stage 72 of [Search for Andor](../quests/andor.md#stage-72); NOT reached stage 85 of [Search for Andor](../quests/andor.md#stage-85); reached stage 170 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-170); NOT reached stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60))* → [crossglen_valentina_andor_21](#d-crossglen_valentina-crossglen_valentina_andor_21)
    - “I've been to this really cool place called Blackwater settlement.” *(if NOT reached stage 72 of [Search for Andor](../quests/andor.md#stage-72); NOT reached stage 85 of [Search for Andor](../quests/andor.md#stage-85); NOT reached stage 170 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-170); reached stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60))* → [crossglen_valentina_andor_21](#d-crossglen_valentina-crossglen_valentina_andor_21)
    - “I've not gone much past Sullengard.” *(if NOT reached stage 85 of [Search for Andor](../quests/andor.md#stage-85); NOT reached stage 72 of [Search for Andor](../quests/andor.md#stage-72); NOT reached stage 170 of [General story flags 2 (hidden flag)](../quests/nondisplay_2.md#stage-170); NOT reached stage 60 of [The agent and the beast](../quests/bwm_agent.md#stage-60))* → [crossglen_valentina_andor_21](#d-crossglen_valentina-crossglen_valentina_andor_21)
    - “I've been running around a lot, but I've not learned much.” → [crossglen_valentina_andor_21](#d-crossglen_valentina-crossglen_valentina_andor_21)

    <span id="d-crossglen_valentina-crossglen_valentina_valeria_10"></span>**`crossglen_valentina_valeria_10`** Valentina: “Right now? No. I am not ready to discuss this with you.”

    - “Well, I look forward to a time where you will be ready.” → *conversation ends*

    <span id="d-crossglen_valentina-crossglen_valentina_10"></span>**`crossglen_valentina_10`** Valentina: “Do you really need to ask me that? Please leave my house and come back when I have calmed down.”

    - “OK mother.” → *conversation ends*

    <span id="d-crossglen_valentina-crossglen_valentina_andor_20"></span>**`crossglen_valentina_andor_20`** Valentina: “I see my child. I can also see that your confidence and skills have grown tremendously, but tell me, with all this adventuring, have you been to Brightport yet?”

    - “[While holding back a smirk, you lie] Yes, why?” → [crossglen_valentina_andor_25](#d-crossglen_valentina-crossglen_valentina_andor_25)
    - “No. Should I have?” → [crossglen_valentina_andor_30](#d-crossglen_valentina-crossglen_valentina_andor_30)

    <span id="d-crossglen_valentina-crossglen_valentina_andor_21"></span>**`crossglen_valentina_andor_21`** Valentina: “I see my child. Tell me, with your limited adventuring, have you made it to Brightport yet?”

    - “No. Should I have?” → [crossglen_valentina_andor_30](#d-crossglen_valentina-crossglen_valentina_andor_30)
    - “[While holding back a smirk, you lie] Yes, why?” → [crossglen_valentina_andor_25](#d-crossglen_valentina-crossglen_valentina_andor_25)

    <span id="d-crossglen_valentina-crossglen_valentina_andor_25"></span>**`crossglen_valentina_andor_25`** Valentina: “Don't you remember who lives there?”

    - “Umm...no, no I don't.” → [crossglen_valentina_andor_40](#d-crossglen_valentina-crossglen_valentina_andor_40)

    <span id="d-crossglen_valentina-crossglen_valentina_andor_30"></span>**`crossglen_valentina_andor_30`** Valentina: “What? Why not? Don't you remember who lives there?”

    - “Umm...no, no I don't.” → [crossglen_valentina_andor_40](#d-crossglen_valentina-crossglen_valentina_andor_40)

    <span id="d-crossglen_valentina-crossglen_valentina_andor_40"></span>**`crossglen_valentina_andor_40`** Valentina: “Andor's best friend from school, Stanwick. If you remember, they are very close friends. Maybe Stanwick has seen Andor?”

    - “Oh, Stanwick, of course.” → [crossglen_valentina_andor_50](#d-crossglen_valentina-crossglen_valentina_andor_50)
    - “Stanwick? I never liked that kid. He's really annoying and always picked on me. I really don't want to talk to him.” → [crossglen_valentina_andor_50](#d-crossglen_valentina-crossglen_valentina_andor_50)
    - “Are you sure that this is worth it? All the information that I have is pointing me to Nor City.” *(if reached stage 80 of [Search for Andor](../quests/andor.md#stage-80))* → [crossglen_valentina_andor_55](#d-crossglen_valentina-crossglen_valentina_andor_55)

    <span id="d-crossglen_valentina-crossglen_valentina_andor_50"></span>**`crossglen_valentina_andor_50`** Valentina: “Yes, I think you should go to Brightport and seek him out. Maybe, just maybe, he could be helpful to us for once.” — **effects:** sets stage 110 of [Search for Andor](../quests/andor.md#stage-110)

    - “Thanks, mother. I will go to Brightport next.” → *conversation ends*

    <span id="d-crossglen_valentina-crossglen_valentina_andor_55"></span>**`crossglen_valentina_andor_55`** Valentina: “Nor City?! What do you know about Nor City?”

    - “Well, I know there is a lady named 'Lydalon' there.” → [crossglen_valentina_andor_60](#d-crossglen_valentina-crossglen_valentina_andor_60)

    <span id="d-crossglen_valentina-crossglen_valentina_andor_60"></span>**`crossglen_valentina_andor_60`** Valentina: “Oh, OK. Just be careful there. Anyways...”

    - Next → [crossglen_valentina_andor_50](#d-crossglen_valentina-crossglen_valentina_andor_50)



### Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 11 lines added |
| [v0.8.4](../versions/0.8.4.md) | Dialogue: 1 line added, 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Sullengard, Sullengard 1 aunts house { #v-sullengard_valentina }

**Where:** Sullengard: [Sullengard 1 aunts house](../maps/sullengard1_aunts_house.md#pin-npc-sullengard_valentina)

### Quests

- [Search for Andor](../quests/andor.md): stage 100

### Dialogue simulator

Talk to Valentina as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_valentina_0.json" data-npc="Valentina" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (13 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-sullengard_valentina-sullengard_valentina_0"></span>**`sullengard_valentina_0`** [Valentina](../monsters/crossglen_valentina.md#v-sullengard_valentina): “$playername, what are you doing here?!”

    - “Mom, I could ask you the same question.” → [sullengard_find_mother_10](#d-sullengard_valentina-sullengard_find_mother_10)

    <span id="d-sullengard_valentina-sullengard_find_mother_10"></span>**`sullengard_find_mother_10`** Valentina: “I'm your mother, answer my question.”

    - “Father sent me to look for Andor as he left shortly after you did and hasn't returned.” → [sullengard_find_mother_20](#d-sullengard_valentina-sullengard_find_mother_20)

    <span id="d-sullengard_valentina-sullengard_find_mother_20"></span>**`sullengard_find_mother_20`** Valentina: “What?! Where is he? Why is your father not with you?”

    - “I guess because he needed to stay home and watch over the house. Or maybe he thinks I'm ready for the challenge?” → [sullengard_find_mother_30](#d-sullengard_valentina-sullengard_find_mother_30)

    <span id="d-sullengard_valentina-sullengard_find_mother_30"></span>**`sullengard_find_mother_30`** Valentina: “Typical Mikhail! So lazy and irresponsible.”

    - “I guess, but I can handle myself and have learned a lot about Andor.” → [sullengard_find_mother_33](#d-sullengard_valentina-sullengard_find_mother_33)
    - “I totally agree with you.” → [sullengard_find_mother_35](#d-sullengard_valentina-sullengard_find_mother_35)

    <span id="d-sullengard_valentina-sullengard_find_mother_33"></span>**`sullengard_find_mother_33`** Valentina: “You've grown up so fast. Stop doing that. You are making me feel old.”

    - “Sorry, mother. You have still not answered my question though. What are you doing here?” → [sullengard_find_mother_40](#d-sullengard_valentina-sullengard_find_mother_40)

    <span id="d-sullengard_valentina-sullengard_find_mother_35"></span>**`sullengard_find_mother_35`** Valentina: “Don't you dare talk ill of your father. He may be lazy, but he is still your father.”

    - “Sorry, mother. You are right, but you have still not answered my question. What are you doing here?” → [sullengard_find_mother_40](#d-sullengard_valentina-sullengard_find_mother_40)

    <span id="d-sullengard_valentina-sullengard_find_mother_40"></span>**`sullengard_find_mother_40`** Valentina: “I'm visiting my sister, your aunt Valeria.”

    - “Your sister? My aunt? What are you talking about?” → [sullengard_find_mother_50](#d-sullengard_valentina-sullengard_find_mother_50)

    <span id="d-sullengard_valentina-sullengard_find_mother_50"></span>**`sullengard_find_mother_50`** Valentina: “Yes, $playername. This is your aunt Valeria. Please say "hi".”

    - “Um...it's nice to meet you aunt Valeria.” → [sullengard_valeria_0](#d-sullengard_valentina-sullengard_valeria_0)

    <span id="d-sullengard_valentina-sullengard_valeria_0"></span>**`sullengard_valeria_0`** [Valeria](../monsters/sullengard_valeria.md): “Hello $playername, it's so wonderful to finally meet you after all of these years.”

    - “But, I don't have an aunt?” *(if NOT reached stage 100 of [Search for Andor](../quests/andor.md#stage-100))* → [sullengard_find_mother_60](#d-sullengard_valentina-sullengard_find_mother_60)
    - “How come mother never spoke of you or told me that she had a sister?” → [sullengard_valeria_10](#d-sullengard_valentina-sullengard_valeria_10)

    <span id="d-sullengard_valentina-sullengard_find_mother_60"></span>**`sullengard_find_mother_60`** [Valentina](../monsters/crossglen_valentina.md#v-sullengard_valentina): “$playername, I will explain this to you later.”

    - “OK, you promise?” → [sullengard_find_mother_70](#d-sullengard_valentina-sullengard_find_mother_70)

    <span id="d-sullengard_valentina-sullengard_valeria_10"></span>**`sullengard_valeria_10`** Valentina: “That is not for me to tell you. Maybe back at home, she will explain it to you.”

    - Next → [sullengard_find_mother_60](#d-sullengard_valentina-sullengard_find_mother_60)

    <span id="d-sullengard_valentina-sullengard_find_mother_70"></span>**`sullengard_find_mother_70`** Valentina: “Yes, but in the meantime, I'm going home and I expect you there shortly after me.”

    - “But what about my search for Andor? Father expects me to find him before I come home again.” → [sullengard_find_mother_80](#d-sullengard_valentina-sullengard_find_mother_80)

    <span id="d-sullengard_valentina-sullengard_find_mother_80"></span>**`sullengard_find_mother_80`** Valentina: “Just follow me home and we can talk there. I may have something to aid you in your search for Andor.” — **effects:** sets stage 100 of [Search for Andor](../quests/andor.md#stage-100), removes monsters from sullengard1_aunts_house, spawns monsters on home




### Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 13 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>



## Behind the scenes

*How the game data handles this character. Not needed for playing.*

**2 entries.** The game data defines 2 separate characters named Valentina. The game makes a new entry whenever a character needs different behaviour (another conversation later in a quest, another place, other stats). Some are the same person at different points in the story; others just share a generic name. Here they differ in: conversation, location.

| Entry | Type | Section |
|---|---|---|
| `crossglen_valentina` | NPC | [Crossglen, Home](#v-crossglen_valentina) |
| `sullengard_valentina` | NPC | [Sullengard, Sullengard 1 aunts house](#v-sullengard_valentina) |

??? info "Technical information: crossglen_valentina"

    | | |
    |---|---|
    | Entry ID | `crossglen_valentina` |
    | Type (wiki) | NPC |
    | Spawn group | `crossglen_valentina` |
    | Loot table | – |
    | Conversation | `crossglen_valentina_selector` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:167` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "crossglen_valentina",
     "name": "Valentina",
     "iconID": "monsters_ld1:167",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "crossglen_valentina",
     "phraseID": "crossglen_valentina_selector"
    }
    ```

??? info "Technical information: sullengard_valentina"

    | | |
    |---|---|
    | Entry ID | `sullengard_valentina` |
    | Type (wiki) | NPC |
    | Spawn group | `sullengard_valentina` |
    | Loot table | – |
    | Conversation | `sullengard_valentina_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_ld1:167` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_valentina",
     "name": "Valentina",
     "iconID": "monsters_ld1:167",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "sullengard_valentina",
     "phraseID": "sullengard_valentina_0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossglen_valentina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossglen_valentina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossglen_valentina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=crossglen_valentina.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
