---
description: "Lost traveler is a non-player character (NPC) in Andor's Trail, found in Sullengard."
---

# ![](../assets/icons/monsters/monsters_tometik2_55.png){ .sprite } Lost traveler

**Where to find Lost traveler:** Sullengard: [Sullengard inn](../maps/sullengard_inn.md#pin-npc-sullengard_inn_traveler)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_tometik2_55.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Sullengard |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

## Quests

- [Recovering stolen property](../quests/sullengard_recover_items.md): stage 50

## Dialogue simulator

Talk to Lost traveler as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/sullengard_inn_traveler_0.json" data-npc="Lost traveler" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (14 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-sullengard_inn_traveler_0"></span>**`sullengard_inn_traveler_0`** Lost traveler: “Hey there.”

    - “You look worried.” → [sullengard_inn_traveler_10](#d-sullengard_inn_traveler_10)
    - “We need to talk.” *(if latest stage of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-40) is 40)* → [sullengard_inn_traveler_40](#d-sullengard_inn_traveler_40)
    - “Sorry, but I have to be on my way.” → *conversation ends*

    <span id="d-sullengard_inn_traveler_10"></span>**`sullengard_inn_traveler_10`** Lost traveler: “That's a keen eye you have. Yes, I am worried.”

    - “Why, what is the problem?” → [sullengard_inn_traveler_20](#d-sullengard_inn_traveler_20)

    <span id="d-sullengard_inn_traveler_40"></span>**`sullengard_inn_traveler_40`** Lost traveler: “It's nice to see you again, fellow traveler.”

    - “You won't be thinking that after I tell you what I know! I am here to serve you justice.” → [sullengard_inn_traveler_50](#d-sullengard_inn_traveler_50)

    <span id="d-sullengard_inn_traveler_20"></span>**`sullengard_inn_traveler_20`** Lost traveler: “At this point, just the fact that I am lost a little bit. You see, I am travelling to Nor City from the west and I got lost.”

    - “Well, rest up tonight and head east from here. Follow the road and you'll find the Duleian road and go east from there.” → [sullengard_inn_traveler_30](#d-sullengard_inn_traveler_30)

    <span id="d-sullengard_inn_traveler_50"></span>**`sullengard_inn_traveler_50`** Lost traveler: “What are you talking about? What do you think you know?”

    - “What did you do with the items you stole from the armory?” → [sullengard_inn_traveler_60](#d-sullengard_inn_traveler_60)

    <span id="d-sullengard_inn_traveler_30"></span>**`sullengard_inn_traveler_30`** Lost traveler: “Thank you so much.”


    <span id="d-sullengard_inn_traveler_60"></span>**`sullengard_inn_traveler_60`** Lost traveler: “Me? You have the wrong guy, friend.”

    - “Stop right there! I know you tried to sell them to the thief. Start talking now!” → [sullengard_inn_traveler_70](#d-sullengard_inn_traveler_70)

    <span id="d-sullengard_inn_traveler_70"></span>**`sullengard_inn_traveler_70`** Lost traveler: “What proof do you have?”

    - “I know that you tried to sell the stolen items from the armory to Prowling Arantxa. I just don't know for sure that…” → [sullengard_inn_traveler_80](#d-sullengard_inn_traveler_80)

    <span id="d-sullengard_inn_traveler_80"></span>**`sullengard_inn_traveler_80`** Lost traveler: “Yes, I did try to sell those items. I needed the gold! Is that a crime? I was out of supplies, lost and in desperate need of a place to heal and rest. With only enough gold to rent a room here in this inn, I needed gold in order to…”

    - Next → [sullengard_inn_traveler_90](#d-sullengard_inn_traveler_90)

    <span id="d-sullengard_inn_traveler_90"></span>**`sullengard_inn_traveler_90`** Lost traveler: “After watching Zaccheria's routine for a couple of days, I noticed he goes to the tavern every night at the same time and stays there for the same amount of time every time. So I took my opportunity.”

    - “Where is Zaccheria's inventory? He wants it back and I am here to see to it that he does get it back.” → [sullengard_inn_traveler_100](#d-sullengard_inn_traveler_100)

    <span id="d-sullengard_inn_traveler_100"></span>**`sullengard_inn_traveler_100`** Lost traveler: “I bet you'd like to know. But you will not get that information for free. I expect to get paid.”

    - “Paid?! Are you serious? You want me to pay you for crimes that you committed?” → [sullengard_inn_traveler_110](#d-sullengard_inn_traveler_110)

    <span id="d-sullengard_inn_traveler_110"></span>**`sullengard_inn_traveler_110`** Lost traveler: “Well, if you want to know the location of those items, then you will pay me.”

    - “How much?!” → [sullengard_inn_traveler_120](#d-sullengard_inn_traveler_120)

    <span id="d-sullengard_inn_traveler_120"></span>**`sullengard_inn_traveler_120`** Lost traveler: “10,000 gold! And not a piece less or no stolen property for you.”

    - “No way.” → *conversation ends*
    - “Whatever. I can spare it.” *(if pay 10,000 gold)* → [sullengard_inn_traveler_130](#d-sullengard_inn_traveler_130)

    <span id="d-sullengard_inn_traveler_130"></span>**`sullengard_inn_traveler_130`** Lost traveler: “Excellent. Nice doing 'business' with you. I hid them somewhere east of town. Close by, but I doubt you can find it easily. ['the lost traveler' then runs off]” — **effects:** sets stage 50 of [Recovering stolen property](../quests/sullengard_recover_items.md#stage-50), removes monsters from sullengard_inn




## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added<br>Dialogue: 14 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “10000 gold! And not a piece less or no stolen property for you.” → “{10000} gold! And not a piece less or no stolen property for you.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `sullengard_inn_traveler` |
    | Type (wiki) | NPC |
    | Spawn group | `sullengard_inn_traveler` |
    | Loot table | – |
    | Conversation | `sullengard_inn_traveler_0` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_tometik2:55` |
    | Defined in | `res/raw/monsterlist_sullengard.json` |

    Raw data:

    ```json
    {
     "id": "sullengard_inn_traveler",
     "name": "Lost traveler",
     "iconID": "monsters_tometik2:55",
     "unique": 1,
     "monsterClass": "humanoid",
     "spawnGroup": "sullengard_inn_traveler",
     "phraseID": "sullengard_inn_traveler_0"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_inn_traveler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_inn_traveler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_inn_traveler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sullengard_inn_traveler.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
