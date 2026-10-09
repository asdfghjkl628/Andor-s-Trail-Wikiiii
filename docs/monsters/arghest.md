---
description: "Arghest is a non-player character (NPC) in Andor's Trail, found in Prim."
---

# ![](../assets/icons/monsters/monsters_rltiles2_81.png){ .sprite } Arghest

**Where to find Arghest:** Prim: [Blackwater mountain 13](../maps/blackwater_mountain13.md#pin-npc-arghest)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles2_81.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Prim |
| **Entry ID** | `arghest` |
| **Introduced** | v0.7.0 or earlier |

</div>

## Quests

- [Well rested](../quests/prim_innquest.md): stages 20, 30, 40
- [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md): stage 22

## Dialogue simulator

Set your quest stages and items, then talk to Arghest. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/arghest_start.json" data-npc="Arghest" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (29 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-arghest_start"></span>**`arghest_start`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 47 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-47); NOT reached stage 22 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-22))* → [arghest_alert](#d-arghest_alert)
    - branch 2 *(if reached stage 40 of [Well rested](../quests/prim_innquest.md#stage-40))* → [arghest_return_1](#d-arghest_return_1)
    - branch 3 *(if reached stage 30 of [Well rested](../quests/prim_innquest.md#stage-30))* → [arghest_return_2](#d-arghest_return_2)
    - branch 4 → [arghest_1](#d-arghest_1)

    <span id="d-arghest_alert"></span>**`arghest_alert`** Arghest: “Hey, do you know what's happening here? These serious-looking soldiers entered the mine without permission.”

    - “They're soldiers of Feygard. I came along with them. Don't worry.” → [arghest_alert_2](#d-arghest_alert_2)
    - “I'll investigate. Bye.” → *conversation ends*

    <span id="d-arghest_return_1"></span>**`arghest_return_1`** Arghest: “Welcome back. Thanks for your help earlier. I hope the room at the inn can be of use to you.”

    - “You are welcome. Goodbye.” → *conversation ends*
    - “Can I enter the mine?” *(if NOT reached stage 22 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-22))* → [arghest_6](#d-arghest_6)
    - “Can I enter the mine?” *(if reached stage 22 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-22))* → [arghest_15](#d-arghest_15)

    <span id="d-arghest_return_2"></span>**`arghest_return_2`** Arghest: “Welcome back. Did you bring me the 5 bottles of milk that I requested?”

    - “No, not yet. I'm working on it.” → [arghest_return_3](#d-arghest_return_3)
    - “Yes, here you go, enjoy!” *(if hand over 5× [Milk](../items/milk.md))* → [arghest_return_4](#d-arghest_return_4)
    - “Yes, but this nearly cost me a fortune!” *(if hand over 5× [Milk](../items/milk.md))* → [arghest_return_4](#d-arghest_return_4)

    <span id="d-arghest_1"></span>**`arghest_1`** Arghest: “Hello there.”

    - “What is this place?” → [arghest_2](#d-arghest_2)
    - “Who are you?” → [arghest_5](#d-arghest_5)
    - “Did you rent the back room at the inn in Prim?” *(if reached stage 10 of [Well rested](../quests/prim_innquest.md#stage-10))* → [arghest_8](#d-arghest_8)

    <span id="d-arghest_alert_2"></span>**`arghest_alert_2`** Arghest: “You'd better be telling me the truth. I will report it later.”

    - “Have you seen a guy with a cloak around here?” → [arghest_alert_3](#d-arghest_alert_3)
    - “Yeah, whatever. We will talk later.” → *conversation ends*

    <span id="d-arghest_6"></span>**`arghest_6`** Arghest: “No. The mine is closed.”

    - “OK, goodbye.” → *conversation ends*
    - “Please?” → [arghest_7](#d-arghest_7)

    <span id="d-arghest_15"></span>**`arghest_15`** Arghest: “Suit yourself... But no one else went in there in weeks.”

    - “Thanks, bye.” → *conversation ends*
    - “If you say so.” → *conversation ends*

    <span id="d-arghest_return_3"></span>**`arghest_return_3`** Arghest: “OK then. Return to me once you have them.”

    - “Will do. Goodbye.” → *conversation ends*

    <span id="d-arghest_return_4"></span>**`arghest_return_4`** Arghest: “Thank you my friend! Now I can restock my supply.” — **effects:** sets stage 40 of [Well rested](../quests/prim_innquest.md#stage-40)

    - Next → [arghest_return_5](#d-arghest_return_5)

    <span id="d-arghest_2"></span>**`arghest_2`** Arghest: “This is the old Elm mine of Prim.”

    - Next → [arghest_3](#d-arghest_3)

    <span id="d-arghest_5"></span>**`arghest_5`** Arghest: “I am Arghest. I guard the entrance here to make sure no one enters the old mine.”

    - “What is this place?” → [arghest_2](#d-arghest_2)
    - “Can I enter the mine?” *(if NOT reached stage 22 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-22))* → [arghest_6](#d-arghest_6)
    - “Can I enter the mine?” *(if reached stage 22 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-22))* → [arghest_15](#d-arghest_15)

    <span id="d-arghest_8"></span>**`arghest_8`** Arghest: “'Inn in Prim' - you sound funny.”

    - Next → [arghest_9](#d-arghest_9)

    <span id="d-arghest_alert_3"></span>**`arghest_alert_3`** Arghest: “I was taking a break in the beds over there, so no idea. Sorry. No one usually comes here but you and those ... noisy soldiers.”

    - “Maybe you should take another break now?” → [arghest_alert_4](#d-arghest_alert_4)
    - “Can I do something for you?” → [arghest_alert_5](#d-arghest_alert_5)

    <span id="d-arghest_7"></span>**`arghest_7`** Arghest: “I said no. Visitors are not allowed in there.”

    - “Please?” → [arghest_6](#d-arghest_6)
    - “Just a quick peek?” → [arghest_6](#d-arghest_6)

    <span id="d-arghest_return_5"></span>**`arghest_return_5`** Arghest: “These bottles look excellent. Now I can last a while longer in here.”

    - Next → [arghest_return_6](#d-arghest_return_6)

    <span id="d-arghest_3"></span>**`arghest_3`** Arghest: “We used to mine a lot here. But that was before the attacks started.”

    - Next → [arghest_4](#d-arghest_4)

    <span id="d-arghest_9"></span>**`arghest_9`** Arghest: “Yes, I rent it. I stay there to rest when my shift ends.”

    - Next → [arghest_10](#d-arghest_10)

    <span id="d-arghest_alert_4"></span>**`arghest_alert_4`** Arghest: “I'd prefer something to drink. No milk this time, better something to warm my body.”

    - “What exactly are you thinking of?” → [arghest_alert_5](#d-arghest_alert_5)

    <span id="d-arghest_alert_5"></span>**`arghest_alert_5`** Arghest: “Once I had got a potion from some crazy old guy in a foreign wood. That would be great now. 'Lodar' he was called.”

    - “Would you like this 'Minor potion of strength'?” *(if hand over 1× [Minor potion of strength](../items/pot_str.md))* → [arghest_alert_8](#d-arghest_alert_8)
    - “I have this 'Improved defense' potion. Here, take it.” *(if hand over 1× [Potion of improved defense](../items/pot_def.md))* → [arghest_alert_8](#d-arghest_alert_8)
    - “What about his famous 'Perilous concoction'?” *(if hand over 1× [Lodar's perilous concoction](../items/pot_rnd.md))* → [arghest_alert_8](#d-arghest_alert_8)

    <span id="d-arghest_return_6"></span>**`arghest_return_6`** Arghest: “Oh, and about the room in the inn - you are welcome to use it in any way you see fit. Quite a cozy place to rest if you ask me.”

    - “Thanks Arghest. Goodbye.” → *conversation ends*
    - “Finally, I thought I would never be able to rest here!” → *conversation ends*

    <span id="d-arghest_4"></span>**`arghest_4`** Arghest: “The attacks on Prim by the beasts, the bandits and the disappearances really reduced our numbers. Now we cannot keep up the mining activity any longer.”

    - “Who are you?” → [arghest_5](#d-arghest_5)

    <span id="d-arghest_10"></span>**`arghest_10`** Arghest: “However, now that we guards aren't as plentiful as we used to be, it has been a while since I could rest in there.”

    - “Mind if I use the room at the inn to rest in?” → [arghest_11](#d-arghest_11)
    - “Are you still going to use it?” → [arghest_11](#d-arghest_11)

    <span id="d-arghest_alert_8"></span>**`arghest_alert_8`** Arghest: “Really? Many many thanks - you make my old heart cry!” — **effects:** sets stage 22 of [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-22)

    - “[muttering] I hope so. The potion was expensive enough!” → [arghest_alert_9](#d-arghest_alert_9)

    <span id="d-arghest_11"></span>**`arghest_11`** Arghest: “Well, I would like to still keep the option of using it. But I guess someone else could rest there now that I'm not actively using it.” — **effects:** sets stage 20 of [Well rested](../quests/prim_innquest.md#stage-20)

    - Next → [arghest_12](#d-arghest_12)

    <span id="d-arghest_alert_9"></span>**`arghest_alert_9`** Arghest: “You may enter the mine now. But you have to find out for yourself, I won't go looking for you.”

    - “Great.” → *conversation ends*
    - “At last.” → *conversation ends*
    - “Don't worry, I won't cause too much trouble.” → *conversation ends*

    <span id="d-arghest_12"></span>**`arghest_12`** Arghest: “Tell you what, if you bring me some more supplies to keep me occupied here, I guess you could have my permission to use it even though I have rented it.”

    - Next → [arghest_13](#d-arghest_13)

    <span id="d-arghest_13"></span>**`arghest_13`** Arghest: “I have plenty of meat here, but I ran out of milk some weeks ago. Do you think you could help me restock my milk supply?”

    - “Sure, no problem. I'll get you your bottles of milk. How much do you need?” → [arghest_14](#d-arghest_14)
    - “Sure, if it leads to me being able to rest here. I'm in.” → [arghest_14](#d-arghest_14)

    <span id="d-arghest_14"></span>**`arghest_14`** Arghest: “Bring me 5 bottles of milk. That should be enough.” — **effects:** sets stage 30 of [Well rested](../quests/prim_innquest.md#stage-30)

    - “I'll go buy some.” → *conversation ends*
    - “OK. I'll be right back.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 5 lines changed<br>· text: “Ok then. Return to me once you have them.” → “OK then. Return to me once you have them.” |
| [v0.7.14](../versions/0.7.14.md) | Dialogue: 8 lines added, 4 lines changed<br>· text: “The attacks on Prim by the beasts and the bandits really reduced our …” → “The attacks on Prim by the beasts, the bandits and the disappearances…” |
| [v0.7.15](../versions/0.7.15.md) | Dialogue: 2 lines changed |
| [v0.8.4](../versions/0.8.4.md) | Dialogue: 1 line changed<br>· text: “You'd better telling me the truth. I will report it later.” → “You'd better be telling me the truth. I will report it later.” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `arghest` |
    | Spawn group | `arghest` |
    | Loot table | – |
    | Conversation | `arghest_start` |
    | Faction | – |
    | Movement | – |
    | Icon | `monsters_rltiles2:81` |
    | Defined in | `res/raw/monsterlist_v069_npcs.json` |

    Raw data:

    ```json
    {
     "id": "arghest",
     "name": "Arghest",
     "iconID": "monsters_rltiles2:81",
     "monsterClass": "humanoid",
     "spawnGroup": "arghest",
     "phraseID": "arghest_start"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arghest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arghest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arghest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=arghest.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
