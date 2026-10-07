---
description: "Feygard patrol guard is a non-player character (NPC) in Andor's Trail, found in Prim."
---

# ![](../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite } Feygard patrol guard

**Where to find Feygard patrol guard:** Prim: [Blackwater mountain 10](../maps/blackwater_mountain10.md#pin-npc-ortholion_guard3), [Elm mine 2](../maps/elm_mine2.md#pin-npc-ortholion_guard3)

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_rltiles3_14.png){ .sprite }</p>

| | |
|---|---|
| **Type** | NPC (can be spoken to; cannot be attacked) |
| **Found in** | Prim |
| **Entry ID** | `ortholion_guard3` |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [Blackwater mountain 10](../maps/blackwater_mountain10.md) | Prim | 3 | Appears later, during a quest |
| [Elm mine 2](../maps/elm_mine2.md) | – | 2 | – |

## Dialogue simulator

Set your quest stages and items, then talk to Feygard patrol guard. Same rules as the game: same checks, same options, same effects.

<div class="dlg-sim" data-src="../../assets/dialogue/ortholion_guard3_selector.json" data-npc="Feygard patrol guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (15 lines)"

    *Exactly as in the game files. Each line appears once; links jump to where a choice leads.*

    <span id="d-ortholion_guard3_selector"></span>**`ortholion_guard3_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 54 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-54))* → [ortholion_guard3_5](#d-ortholion_guard3_5)
    - branch 2 *(if reached stage 47 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-47))* → [ortholion_guard3_2](#d-ortholion_guard3_2)
    - branch 3 *(if latest stage of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-46) is 46)* → [ortholion_guard3_8](#d-ortholion_guard3_8)
    - branch 4 *(if random chance (1/2%))* → [ortholion_guard3_1](#d-ortholion_guard3_1)
    - branch 5 → [ortholion_guard3_1b](#d-ortholion_guard3_1b)

    <span id="d-ortholion_guard3_5"></span>**`ortholion_guard3_5`** Feygard patrol guard: “Ahem... the general is waiting for you in the dining room.”

    - “The general was waiting for you down in the mine.” → [ortholion_guard3_6a](#d-ortholion_guard3_6a)
    - “Thank you, sir.” → *conversation ends*
    - “Do you have anything to trade?” → [ortholion_guard3_6b](#d-ortholion_guard3_6b)

    <span id="d-ortholion_guard3_2"></span>**`ortholion_guard3_2`** Feygard patrol guard: “Hey kid! You shouldn't be here, there are dangerous animals.”

    - “Are you scared of the snakes?” → [ortholion_guard3_3](#d-ortholion_guard3_3)
    - “OK, goodbye.” → *conversation ends*
    - “I can handle myself.” → *conversation ends*

    <span id="d-ortholion_guard3_8"></span>**`ortholion_guard3_8`** Feygard patrol guard: “I hate these escorting trips. It's not like the general really needs us for this.”

    - Next → [ortholion_guard3_9](#d-ortholion_guard3_9)

    <span id="d-ortholion_guard3_1"></span>**`ortholion_guard3_1`** Feygard patrol guard: “Out of my sight kid. I'm on duty.”


    <span id="d-ortholion_guard3_1b"></span>**`ortholion_guard3_1b`** Feygard patrol guard: “We soldiers of Feygard have come to this lonely place by direct command of General Ortholion, and do not have time to waste talking to a kid.”


    <span id="d-ortholion_guard3_6a"></span>**`ortholion_guard3_6a`** Feygard patrol guard: “What do you mean kid?! We had to... guard this place right here. We were sure our mighty general Ortholion was handling the problem!”

    - “I will report your inefficiency.” → *conversation ends*
    - “It was me who solved the problem!” → [ortholion_guard3_7](#d-ortholion_guard3_7)

    <span id="d-ortholion_guard3_6b"></span>**`ortholion_guard3_6b`** Feygard patrol guard: “No, I do not.”

    - “So cold...” → *conversation ends*
    - “Fine. Keep the good work, hah!” → *conversation ends*

    <span id="d-ortholion_guard3_3"></span>**`ortholion_guard3_3`** Feygard patrol guard: “Eh? No. We are...Uhm, the rearguard, keeping the others safe. After all, this is the mines only entrance.”

    - “Yeah, sure. See you later, cowards.” → *conversation ends*
    - “Where's the general?” → [ortholion_guard3_4](#d-ortholion_guard3_4)

    <span id="d-ortholion_guard3_9"></span>**`ortholion_guard3_9`** Feygard patrol guard: “The trip here was anything but safe. I miss my former post in Crossglen.”

    - “Oh, so you are one of those good for nothing, always drunk, soldiers?” → [ortholion_guard3_10](#d-ortholion_guard3_10)

    <span id="d-ortholion_guard3_7"></span>**`ortholion_guard3_7`** Feygard patrol guard: “HAH! Out of my sight.”


    <span id="d-ortholion_guard3_4"></span>**`ortholion_guard3_4`** Feygard patrol guard: “Our... mighty general has already caught that Shadow fanatic...Yes. Deep in the mine, that's where he is. He's coming back...Probably.”

    - “Aha, so no idea. Thanks anyway.” → *conversation ends*
    - “Good. Gonna check that out, bye.” → *conversation ends*

    <span id="d-ortholion_guard3_10"></span>**`ortholion_guard3_10`** Feygard patrol guard: “Yes, I w... Hey! What did you just say?”

    - “I have important information to deliver!” → [ortholion_guard3_11a](#d-ortholion_guard3_11a)
    - “I am proud of you, drunkard. Where's your boss?” → [ortholion_guard3_11b](#d-ortholion_guard3_11b)

    <span id="d-ortholion_guard3_11a"></span>**`ortholion_guard3_11a`** Feygard patrol guard: “Whatever it is, it is none of my concern. Go talk with our mountain scout, she's the one in charge, *hic*.”

    - “Blackwater brew, eh? Truly disappointing. Goodbye.” → *conversation ends*
    - “OK sir, many thanks.” → *conversation ends*

    <span id="d-ortholion_guard3_11b"></span>**`ortholion_guard3_11b`** Feygard patrol guard: “[looks at you perplexed] Uhh... *hic* Over there. *points at the mountain scout*”

    - “Finally, bye.” → *conversation ends*
    - “Thanks, and sleep it off... Sigh.” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 10 lines added |
| [v0.8.8](../versions/0.8.8.md) | Dialogue: 5 lines added, 3 lines changed<br>· text: “Our... mighty general has already caught that Shadow fanatic...Yes. D…” → “Our... mighty general has already caught that Shadow fanatic...Yes. D…”<br>· text: “We soldiers of Feygard have come to this lonely place by direct comma…” → “We soldiers of Feygard have come to this lonely place by direct comma…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “Yes sir, I w... Hey! What did you just say?” → “Yes, I w... Hey! What did you just say?” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


??? info "Technical information"

    | | |
    |---|---|
    | Entry ID | `ortholion_guard3` |
    | Spawn group | `ortholion_guard3` |
    | Loot table | – |
    | Conversation | `ortholion_guard3_selector` |
    | Faction | – |
    | Movement | none |
    | Icon | `monsters_rltiles3:14` |
    | Defined in | `res/raw/monsterlist_omi2.json` |

    Raw data:

    ```json
    {
     "id": "ortholion_guard3",
     "name": "Feygard patrol guard",
     "iconID": "monsters_rltiles3:14",
     "monsterClass": "humanoid",
     "movementAggressionType": "none",
     "spawnGroup": "ortholion_guard3",
     "phraseID": "ortholion_guard3_selector"
    }
    ```


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard3.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Data from v0.8.18</small>
