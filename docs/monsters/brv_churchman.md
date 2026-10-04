# ![](../assets/icons/monsters/monsters_rltiles2_136.png){ .sprite } Seviron

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 10 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [brimhaven_church](../maps/brimhaven_church.md)
- [brimhaven_church_upstairs](../maps/brimhaven_church_upstairs.md)

## Quests

- [A cat and mouse game](../quests/cat_and_mouse.md): stages 10, 20, 30, 50, 60, 70, 80

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Seviron. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/brv_churchman_start.json" data-npc="Seviron" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (27 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_churchman_start"></span>**`brv_churchman_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-60); NOT reached stage 70 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-70); NOT reached stage 80 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-80); NOT reached stage 90 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-90); carry 1× [Trapped mouse](../items/trapped_mouse.md))* → [brv_churchman_mouse1](#d-brv_churchman_mouse1)
    - branch 2 *(if reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20); reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30); NOT reached stage 50 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-50))* → [brv_churchman_b1](#d-brv_churchman_b1)
    - branch 3 *(if reached stage 10 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-10); reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20); NOT reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30))* → [brv_churchman_i1](#d-brv_churchman_i1)
    - branch 4 *(if reached stage 10 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-10); NOT reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20); reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30))* → [brv_churchman_i1](#d-brv_churchman_i1)
    - branch 5 *(if reached stage 10 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-10); NOT reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20); NOT reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30))* → [brv_churchman_i1](#d-brv_churchman_i1)
    - branch 6 *(if reached stage 50 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-50); NOT reached stage 60 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-60))* → [brv_churchman_trap1](#d-brv_churchman_trap1)
    - branch 7 *(if reached stage 60 of [brv_nondisplay2 (hidden flag)](../quests/brv_nondisplay2.md#stage-60))* → [brv_churchman_banned](#d-brv_churchman_banned)
    - branch 8 *(if NOT reached stage 10 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-10))* → [brv_churchman](#d-brv_churchman)
    - branch 9 → [brv_churchman_default1](#d-brv_churchman_default1)

    <span id="d-brv_churchman_mouse1"></span>**`brv_churchman_mouse1`** Seviron: “What do you intend to do with the mouse?”

    - “I'll give it to the cat. That should solve the problem.” *(if hand over 1× [Trapped mouse](../items/trapped_mouse.md))* → [brv_churchman_trap3a](#d-brv_churchman_trap3a)
    - “I'll release it outside.” → [brv_churchman_trap3b](#d-brv_churchman_trap3b)

    <span id="d-brv_churchman_b1"></span>**`brv_churchman_b1`** Seviron: “Do you have the bottle?”

    - “Yes. Here it is.” *(if hand over 1× [Large empty bottle](../items/large_bottle.md))* → [brv_churchman_b2](#d-brv_churchman_b2)
    - “No, not yet. I'm still looking for one.” → *conversation ends*

    <span id="d-brv_churchman_i1"></span>**`brv_churchman_i1`** Seviron: “Do you have the items we need for the trap?”

    - “I have the rocks.” *(if hand over 3× [Small rock](../items/rock.md); NOT reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30); NOT carry 1× [Cheese](../items/cheese.md); NOT reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20))* → [brv_churchman_09a](#d-brv_churchman_09a)
    - “I have the rocks.” *(if hand over 3× [Small rock](../items/rock.md); reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30); NOT reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20))* → [brv_churchman_09c](#d-brv_churchman_09c)
    - “I have the cheese.” *(if hand over 1× [Cheese](../items/cheese.md); NOT reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20); NOT carry 3× [Small rock](../items/rock.md); NOT reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30))* → [brv_churchman_09b](#d-brv_churchman_09b)
    - “I have the cheese.” *(if hand over 1× [Cheese](../items/cheese.md); reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20); NOT reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30))* → [brv_churchman_09c](#d-brv_churchman_09c)
    - “I have the rocks and the cheese.” *(if hand over 3× [Small rock](../items/rock.md); hand over 1× [Cheese](../items/cheese.md); NOT reached stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20); NOT reached stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30))* → [brv_churchman_09c](#d-brv_churchman_09c)
    - “No, not yet.” → *conversation ends*

    <span id="d-brv_churchman_trap1"></span>**`brv_churchman_trap1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 40 of [nondisplay_bhvt (hidden flag)](../quests/nondisplay_bhvt.md#stage-40))* → [brv_churchman_trap2](#d-brv_churchman_trap2)
    - branch 2 → [brv_churchman_trap3](#d-brv_churchman_trap3)

    <span id="d-brv_churchman_banned"></span>**`brv_churchman_banned`** Seviron: “Go away, naughty kid!”


    <span id="d-brv_churchman"></span>**`brv_churchman`** Seviron: “Hello. I am Seviron. You are not supposed to be up here.”

    - “What is this room used for?” → [brv_churchman_01](#d-brv_churchman_01)
    - “I'm looking for my brother, Andor. He looks a bit like me. Have you seen him?” → [brv_churchman_01a](#d-brv_churchman_01a)
    - “Sorry, I'll leave.” → *conversation ends*

    <span id="d-brv_churchman_default1"></span>**`brv_churchman_default1`** Seviron: “Hello again. Is there something I can help you with?”

    - “I'm looking for my brother, Andor. He looks a bit like me.” → [Brv_churchman_default2](#d-Brv_churchman_default2)
    - “No thanks. I'll be going.” → *conversation ends*

    <span id="d-brv_churchman_trap3a"></span>**`brv_churchman_trap3a`** Seviron: “Hmm. I'm sure the cat will be happy, but I doubt the mouse will!” — **effects:** sets stage 70 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-70), gives [Large empty bottle](../items/large_bottle.md)


    <span id="d-brv_churchman_trap3b"></span>**`brv_churchman_trap3b`** Seviron: “Well, don't release it in the town. It will just go into another building.” — **effects:** sets stage 80 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-80)


    <span id="d-brv_churchman_b2"></span>**`brv_churchman_b2`** Seviron: “Excellent. I'll set the trap. This will require some patience though, so you should come back later to see if it worked.” — **effects:** sets stage 50 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-50), starts timer “mouse_trap”


    <span id="d-brv_churchman_09a"></span>**`brv_churchman_09a`** Seviron: “Thanks. Now we just need the cheese and the bottle.” — **effects:** sets stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20)


    <span id="d-brv_churchman_09c"></span>**`brv_churchman_09c`** Seviron: “Thanks. Now we just need the bottle. You should ask around town. Someone must have one.” — **effects:** sets stage 20 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-20), sets stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30)


    <span id="d-brv_churchman_09b"></span>**`brv_churchman_09b`** Seviron: “Thanks. Now we just need the rocks and the bottle.” — **effects:** sets stage 30 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-30)


    <span id="d-brv_churchman_trap2"></span>**`brv_churchman_trap2`** Seviron: “We caught the mouse! Here it is, in the bottle. You can decide what to do with it. And here's a little gold for your help.” — **effects:** sets stage 60 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-60), gives [Trapped mouse](../items/trapped_mouse.md), [Gold coins](../items/gold.md)

    - “I'll give it to the cat. That should solve the problem!” *(if hand over 1× [Trapped mouse](../items/trapped_mouse.md))* → [brv_churchman_trap3a](#d-brv_churchman_trap3a)
    - “I'll release it outside.” → [brv_churchman_trap3b](#d-brv_churchman_trap3b)

    <span id="d-brv_churchman_trap3"></span>**`brv_churchman_trap3`** Seviron: “Sorry, the mouse is still running around. We will get it though. Be patient.”


    <span id="d-brv_churchman_01"></span>**`brv_churchman_01`** Seviron: “This is the church bell tower.”

    - Next → [brv_churchman_02](#d-brv_churchman_02)

    <span id="d-brv_churchman_01a"></span>**`brv_churchman_01a`** Seviron: “No. Irritating children do not usually come up here. You are an exception.”

    - “Hmm. OK. What is this room?” → [brv_churchman_01](#d-brv_churchman_01)
    - “Sorry. I'll leave.” → *conversation ends*

    <span id="d-Brv_churchman_default2"></span>**`Brv_churchman_default2`** Seviron: “Sorry, I haven't seen anyone like that.”


    <span id="d-brv_churchman_02"></span>**`brv_churchman_02`** Seviron: “We use the bells to both notify townsfolk when there is a service, and to warn of danger to the town.”

    - Next → [brv_churchman_03](#d-brv_churchman_03)

    <span id="d-brv_churchman_03"></span>**`brv_churchman_03`** Seviron: “I am the bell-ringer. Unfortunately, I also have to guard the bells from Quasi. He likes to ring them even when there is no reason to do so.”

    - “Who is Quasi?” *(if NOT reached stage 30 of [nondisplay_bhvt (hidden flag)](../quests/nondisplay_bhvt.md#stage-30); NOT reached stage 10 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-10))* → [brv_churchman_04a](#d-brv_churchman_04a)
    - “Quasi is...interesting.” *(if reached stage 30 of [nondisplay_bhvt (hidden flag)](../quests/nondisplay_bhvt.md#stage-30); NOT reached stage 10 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-10))* → [brv_churchman_04b](#d-brv_churchman_04b)
    - “OK. Thanks. I'm looking for my brother, Andor. Have you seen him?” → [brv_churchman_01a](#d-brv_churchman_01a)

    <span id="d-brv_churchman_04a"></span>**`brv_churchman_04a`** Seviron: “Quasi is the grave digger. He is usually in the basement. Sometimes he is trouble, but mostly he is useful. Anyway, he has nowhere else to go, so he lives in the church.”

    - Next → [brv_churchman_05](#d-brv_churchman_05)

    <span id="d-brv_churchman_04b"></span>**`brv_churchman_04b`** Seviron: “Yes, that is one way to put it. He is useful, so he lives here in the church. He has nowhere else to go anyway, so we accommodate him.”

    - Next → [brv_churchman_05](#d-brv_churchman_05)

    <span id="d-brv_churchman_05"></span>**`brv_churchman_05`** Seviron: “Is there anything else I can help you with? You are distracting me from watching the cat and the mouse on the other side of the room.”

    - Next → [brv_churchman_06](#d-brv_churchman_06)

    <span id="d-brv_churchman_06"></span>**`brv_churchman_06`** Seviron: “The mice like to chew the bell rope, which is a problem. So we brought in the cat to control them. That particular mouse seems to be very good at evading the cat though. It knows just when to turn, and just where to hide where the cat…”

    - “Can I help in some way?” → [brv_churchman_07](#d-brv_churchman_07)
    - “I need to find my brother. Bye.” → *conversation ends*
    - “Good luck with that! I have more important things to deal with. Bye.” → *conversation ends*

    <span id="d-brv_churchman_07"></span>**`brv_churchman_07`** Seviron: “You could help me trap it. I need some cheese, a large empty bottle, and some rocks that we can use to prop up the bottle at an angle. If the mouse crawls in to get the cheese, it will not be able to get out again.”

    - “OK. I'll help.” → [brv_churchman_08](#d-brv_churchman_08)
    - “Sorry. I don't have time for that. I have to go.” → *conversation ends*

    <span id="d-brv_churchman_08"></span>**`brv_churchman_08`** Seviron: “Thanks. Just bring me the items. I think three rocks should be enough.” — **effects:** sets stage 10 of [A cat and mouse game](../quests/cat_and_mouse.md#stage-10)

    - “I have the rocks.” *(if hand over 3× [Small rock](../items/rock.md); NOT carry 1× [Cheese](../items/cheese.md))* → [brv_churchman_09a](#d-brv_churchman_09a)
    - “I have the cheese.” *(if hand over 1× [Cheese](../items/cheese.md); NOT carry 3× [Small rock](../items/rock.md))* → [brv_churchman_09b](#d-brv_churchman_09b)
    - “I have the rocks and the cheese.” *(if hand over 3× [Small rock](../items/rock.md); hand over 1× [Cheese](../items/cheese.md))* → [brv_churchman_09c](#d-brv_churchman_09c)
    - “I'll go and get the items you asked for.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added<br>Dialogue: 26 lines added |
| [v0.7.13](../versions/0.7.13.md) | Dialogue: 1 line added, 2 lines changed |
| [v0.7.15](../versions/0.7.15.md) | Dialogue: 2 lines changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_churchman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_churchman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_churchman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_churchman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brv_churchman` · Data from v0.8.18</small>
