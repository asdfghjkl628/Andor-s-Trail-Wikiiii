---
description: "Botisto is a non-player character (NPC) in Andor's Trail, found in Mushroom m 2 4b."
---

# ![](../assets/icons/monsters/monsters_gisons_10.png){ .sprite } Botisto

**Where to find Botisto:** [Mushroom m 2 4b](../maps/mushroom_m2_4b.md#pin-npc-bogsten_gambler2)

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/monsters/monsters_gisons_10.png" alt=""></p>

| | |
|---|---|
| **Type** | NPC (talk only; never fought) |
| **Found in** | Mushroom m 2 4b |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

## Dialogue simulator

Talk to Botisto as you would in the game. When the conversation depends on your progress (a quest, an item, a dice roll…), the simulator asks you. Try another answer with **Undo**.

<div class="dlg-sim" data-src="../../assets/dialogue/bogsten_gambler2.json" data-npc="Botisto" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Follows the game's own conversation rules (v0.8.18).</p>

??? quote "Dialogue (45 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-bogsten_gambler2"></span>**`bogsten_gambler2`** Botisto: “Let's have another Skat game - Bogal, you bid.”

    - Next → [bogsten_gambler_18](#d-bogsten_gambler_18)

    <span id="d-bogsten_gambler_18"></span>**`bogsten_gambler_18`** [Bogal](../monsters/bogsten_gambler1.md): “18”

    - Next → [bogsten_gambler_18a](#d-bogsten_gambler_18a)

    <span id="d-bogsten_gambler_18a"></span>**`bogsten_gambler_18a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (10%))* → [bogsten_gambler_out](#d-bogsten_gambler_out)
    - branch 2 → [bogsten_gambler_20](#d-bogsten_gambler_20)

    <span id="d-bogsten_gambler_out"></span>**`bogsten_gambler_out`** [Bogal](../monsters/bogsten_gambler1.md): “OK. It's your game.”


    <span id="d-bogsten_gambler_20"></span>**`bogsten_gambler_20`** [Bogal](../monsters/bogsten_gambler1.md): “20”

    - Next → [bogsten_gambler_20a](#d-bogsten_gambler_20a)

    <span id="d-bogsten_gambler_20a"></span>**`bogsten_gambler_20a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (10%))* → [bogsten_gambler_out](#d-bogsten_gambler_out)
    - branch 2 → [bogsten_gambler_22](#d-bogsten_gambler_22)

    <span id="d-bogsten_gambler_22"></span>**`bogsten_gambler_22`** [Bogal](../monsters/bogsten_gambler1.md): “2”

    - Next → [bogsten_gambler_22a](#d-bogsten_gambler_22a)

    <span id="d-bogsten_gambler_22a"></span>**`bogsten_gambler_22a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (10%))* → [bogsten_gambler_out](#d-bogsten_gambler_out)
    - branch 2 → [bogsten_gambler_23](#d-bogsten_gambler_23)

    <span id="d-bogsten_gambler_23"></span>**`bogsten_gambler_23`** [Bogal](../monsters/bogsten_gambler1.md): “0”

    - Next → [bogsten_gambler_23a](#d-bogsten_gambler_23a)

    <span id="d-bogsten_gambler_23a"></span>**`bogsten_gambler_23a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (10%))* → [bogsten_gambler_out](#d-bogsten_gambler_out)
    - branch 2 → [bogsten_gambler_24](#d-bogsten_gambler_24)

    <span id="d-bogsten_gambler_24"></span>**`bogsten_gambler_24`** [Bogal](../monsters/bogsten_gambler1.md): “4”

    - Next → [bogsten_gambler_24a](#d-bogsten_gambler_24a)

    <span id="d-bogsten_gambler_24a"></span>**`bogsten_gambler_24a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (20%))* → [bogsten_gambler_24b](#d-bogsten_gambler_24b)
    - branch 2 *(if random chance (20%))* → [bogsten_gambler_out](#d-bogsten_gambler_out)
    - branch 3 → [bogsten_gambler_27](#d-bogsten_gambler_27)

    <span id="d-bogsten_gambler_24b"></span>**`bogsten_gambler_24b`** [Bollo](../monsters/bogsten_gambler3.md): “Ah, good. I already thought you wanted to play Null.”

    - Next → [bogsten_gambler_27](#d-bogsten_gambler_27)

    <span id="d-bogsten_gambler_27"></span>**`bogsten_gambler_27`** [Bogal](../monsters/bogsten_gambler1.md): “7”

    - Next → [bogsten_gambler_27a](#d-bogsten_gambler_27a)

    <span id="d-bogsten_gambler_27a"></span>**`bogsten_gambler_27a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (20%))* → [bogsten_gambler_out](#d-bogsten_gambler_out)
    - branch 2 → [bogsten_gambler_30](#d-bogsten_gambler_30)

    <span id="d-bogsten_gambler_30"></span>**`bogsten_gambler_30`** [Bogal](../monsters/bogsten_gambler1.md): “30”

    - Next → [bogsten_gambler_30a](#d-bogsten_gambler_30a)

    <span id="d-bogsten_gambler_30a"></span>**`bogsten_gambler_30a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (20%))* → [bogsten_gambler_out](#d-bogsten_gambler_out)
    - branch 2 → [bogsten_gambler_33](#d-bogsten_gambler_33)

    <span id="d-bogsten_gambler_33"></span>**`bogsten_gambler_33`** [Bogal](../monsters/bogsten_gambler1.md): “33”

    - Next → [bogsten_gambler_33a](#d-bogsten_gambler_33a)

    <span id="d-bogsten_gambler_33a"></span>**`bogsten_gambler_33a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (20%))* → [bogsten_gambler_33b](#d-bogsten_gambler_33b)
    - branch 2 *(if random chance (20%))* → [bogsten_gambler_out](#d-bogsten_gambler_out)
    - branch 3 → [bogsten_gambler_36](#d-bogsten_gambler_36)

    <span id="d-bogsten_gambler_33b"></span>**`bogsten_gambler_33b`** [Bollo](../monsters/bogsten_gambler3.md): “Hey, you've forgotten 30!”

    - Next → [bogsten_gambler_33b_2](#d-bogsten_gambler_33b_2)

    <span id="d-bogsten_gambler_36"></span>**`bogsten_gambler_36`** [Bogal](../monsters/bogsten_gambler1.md): “36”

    - Next → [bogsten_gambler_36a](#d-bogsten_gambler_36a)

    <span id="d-bogsten_gambler_33b_2"></span>**`bogsten_gambler_33b_2`** [Bogal](../monsters/bogsten_gambler1.md): “Nonsense. I've been playing Skat for over 150 years now. I wouldn't make such a silly mistake.”

    - Next → [bogsten_gambler_36](#d-bogsten_gambler_36)

    <span id="d-bogsten_gambler_36a"></span>**`bogsten_gambler_36a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (20%))* → [bogsten_gambler_36b](#d-bogsten_gambler_36b)
    - branch 2 *(if random chance (20%))* → [bogsten_gambler_out](#d-bogsten_gambler_out)
    - branch 3 → [bogsten_gambler_40](#d-bogsten_gambler_40)

    <span id="d-bogsten_gambler_36b"></span>**`bogsten_gambler_36b`** [Botisto](../monsters/bogsten_gambler2.md): “Don't you dare play clubs!”

    - Next → [bogsten_gambler_36b_2](#d-bogsten_gambler_36b_2)

    <span id="d-bogsten_gambler_40"></span>**`bogsten_gambler_40`** [Bogal](../monsters/bogsten_gambler1.md): “40”

    - Next → [bogsten_gambler_40a](#d-bogsten_gambler_40a)

    <span id="d-bogsten_gambler_36b_2"></span>**`bogsten_gambler_36b_2`** [Bogal](../monsters/bogsten_gambler1.md): “I'm old enough to decide that on my own. * giggle *”

    - Next → [bogsten_gambler_40](#d-bogsten_gambler_40)

    <span id="d-bogsten_gambler_40a"></span>**`bogsten_gambler_40a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (20%))* → [bogsten_gambler_40b](#d-bogsten_gambler_40b)
    - branch 2 *(if random chance (20%))* → [bogsten_gambler_out](#d-bogsten_gambler_out)
    - branch 3 → [bogsten_gambler_44](#d-bogsten_gambler_44)

    <span id="d-bogsten_gambler_40b"></span>**`bogsten_gambler_40b`** [Bollo](../monsters/bogsten_gambler3.md): “You already said 30.”

    - Next → [bogsten_gambler_40b_2](#d-bogsten_gambler_40b_2)

    <span id="d-bogsten_gambler_44"></span>**`bogsten_gambler_44`** [Bogal](../monsters/bogsten_gambler1.md): “44”

    - Next → [bogsten_gambler_44a](#d-bogsten_gambler_44a)

    <span id="d-bogsten_gambler_40b_2"></span>**`bogsten_gambler_40b_2`** [Bogal](../monsters/bogsten_gambler1.md): “I said FORTY, you deaf idiot!”

    - Next → [bogsten_gambler_40b_3](#d-bogsten_gambler_40b_3)

    <span id="d-bogsten_gambler_44a"></span>**`bogsten_gambler_44a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (20%))* → [bogsten_gambler_out](#d-bogsten_gambler_out)
    - branch 2 → [bogsten_gambler_48](#d-bogsten_gambler_48)

    <span id="d-bogsten_gambler_40b_3"></span>**`bogsten_gambler_40b_3`** [Bollo](../monsters/bogsten_gambler3.md): “Who's an idiot??”

    - Next → [bogsten_gambler_40b_4](#d-bogsten_gambler_40b_4)

    <span id="d-bogsten_gambler_48"></span>**`bogsten_gambler_48`** [Bogal](../monsters/bogsten_gambler1.md): “48”

    - Next → [bogsten_gambler_48a](#d-bogsten_gambler_48a)

    <span id="d-bogsten_gambler_40b_4"></span>**`bogsten_gambler_40b_4`** [Botisto](../monsters/bogsten_gambler2.md): “Both of you. Now go on, Bogal.”

    - Next → [bogsten_gambler_44](#d-bogsten_gambler_44)

    <span id="d-bogsten_gambler_48a"></span>**`bogsten_gambler_48a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (50%))* → [bogsten_gambler_48b](#d-bogsten_gambler_48b)
    - branch 2 *(if random chance (20%))* → [bogsten_gambler_out](#d-bogsten_gambler_out)
    - branch 3 → [bogsten_gambler_50](#d-bogsten_gambler_50)

    <span id="d-bogsten_gambler_48b"></span>**`bogsten_gambler_48b`** [Botisto](../monsters/bogsten_gambler2.md): “Why is this kid staring at us? Hey, you! Never seen a Skat game?”

    - “Eh...” → [bogsten_gambler_48b_2](#d-bogsten_gambler_48b_2)
    - “Sure. I'm a Skat pro myself.” → [bogsten_gambler_48b_3](#d-bogsten_gambler_48b_3)
    - “No. My father always forbade me to gamble.” → [bogsten_gambler_48b_2](#d-bogsten_gambler_48b_2)

    <span id="d-bogsten_gambler_50"></span>**`bogsten_gambler_50`** [Bogal](../monsters/bogsten_gambler1.md): “50”

    - Next → [bogsten_gambler_50a](#d-bogsten_gambler_50a)

    <span id="d-bogsten_gambler_48b_2"></span>**`bogsten_gambler_48b_2`** Botisto: “Oh dear. Go on, Bogal. I don't want to rot here.”

    - Next → [bogsten_gambler_50](#d-bogsten_gambler_50)

    <span id="d-bogsten_gambler_48b_3"></span>**`bogsten_gambler_48b_3`** Botisto: “Well, whoever would believe that ...”

    - “Hee!” → [bogsten_gambler_50](#d-bogsten_gambler_50)

    <span id="d-bogsten_gambler_50a"></span>**`bogsten_gambler_50a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (20%))* → [bogsten_gambler_out](#d-bogsten_gambler_out)
    - branch 2 → [bogsten_gambler_50b](#d-bogsten_gambler_50b)

    <span id="d-bogsten_gambler_50b"></span>**`bogsten_gambler_50b`** [Bogal](../monsters/bogsten_gambler1.md): “50 - still yes?? You must be cheating!”

    - Next → [bogsten_gambler_50b_2](#d-bogsten_gambler_50b_2)

    <span id="d-bogsten_gambler_50b_2"></span>**`bogsten_gambler_50b_2`** [Bollo](../monsters/bogsten_gambler3.md): “Cheating - me? Dare to say that again!”

    - Next → [bogsten_gambler_50b_3](#d-bogsten_gambler_50b_3)

    <span id="d-bogsten_gambler_50b_3"></span>**`bogsten_gambler_50b_3`** [Bogal](../monsters/bogsten_gambler1.md): “We all know that you always do. Calm down.”

    - Next → [bogsten_gambler_50b_4](#d-bogsten_gambler_50b_4)

    <span id="d-bogsten_gambler_50b_4"></span>**`bogsten_gambler_50b_4`** [Bollo](../monsters/bogsten_gambler3.md): “Oooh! If you were not already dead, you would be now!”

    - “But gentlemen! It's just a game!” → [bogsten_gambler_50b_5](#d-bogsten_gambler_50b_5)

    <span id="d-bogsten_gambler_50b_5"></span>**`bogsten_gambler_50b_5`** [Botisto](../monsters/bogsten_gambler2.md): “Just a game? Get out! Away with you!”




## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 45 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Behind the scenes

*How the game data handles this character. Not needed for playing.*

??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `bogsten_gambler2` |
    | Type (wiki) | NPC |
    | Spawn group | `bogsten_gambler2` |
    | Loot table | – |
    | Conversation | `bogsten_gambler2` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_gisons:10` |
    | Defined in | `res/raw/monsterlist_fungi_panic.json` |

    Raw data:

    ```json
    {
     "id": "bogsten_gambler2",
     "name": "Botisto",
     "iconID": "monsters_gisons:10",
     "moveCost": 10,
     "monsterClass": "humanoid",
     "spawnGroup": "bogsten_gambler2",
     "phraseID": "bogsten_gambler2"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bogsten_gambler2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bogsten_gambler2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bogsten_gambler2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bogsten_gambler2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
