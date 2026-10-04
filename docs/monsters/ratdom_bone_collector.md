# ![](../assets/icons/monsters/monsters_ld1_63.png){ .sprite } Loirash

| Stat | Value |
|---|---|
| Class | ? |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 5 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [ratdom_maze_464](../maps/ratdom_maze_464.md)
- [ratdom_maze_634](../maps/ratdom_maze_634.md)

## Quests

- [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md): stages 121

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Loirash. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_bone_collector.json" data-npc="Loirash" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (11 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ratdom_bone_collector"></span>**`ratdom_bone_collector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if carry 1× [Leg bone of a rat](../items/ratdom_rat_skelett_leg_coll.md))* → [ratdom_bone_collector_50](#d-ratdom_bone_collector_50)
    - branch 2 *(if reached stage 121 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-121))* → [ratdom_bone_collector_20](#d-ratdom_bone_collector_20)
    - branch 3 → [ratdom_bone_collector_10](#d-ratdom_bone_collector_10)

    <span id="d-ratdom_bone_collector_50"></span>**`ratdom_bone_collector_50`** [Loirash](../monsters/ratdom_bone_collector.md): “Looks like you have something that doesn't belong to you?”

    - “Yes. I found this old leg bone of a rat. Can I purchase it?” → [ratdom_bone_collector_52](#d-ratdom_bone_collector_52)
    - “[Lie] No. I haven't taken anything.” *(if hand over 1× [Leg bone of a rat](../items/ratdom_rat_skelett_leg_coll.md))* → [ratdom_bone_collector_54](#d-ratdom_bone_collector_54)

    <span id="d-ratdom_bone_collector_20"></span>**`ratdom_bone_collector_20`** [Loirash](../monsters/ratdom_bone_collector.md): “This cave is a great source of bones of high quality, so I will stay until my instrument is complete.” — **effects:** sets stage 121 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-121)

    - “May I have a look?” → [ratdom_bone_collector_22](#d-ratdom_bone_collector_22)
    - “OK. Have fun.” → *conversation ends*

    <span id="d-ratdom_bone_collector_10"></span>**`ratdom_bone_collector_10`** [Loirash](../monsters/ratdom_bone_collector.md): “Oh, a visitor - how unusual!”

    - Next → [ratdom_bone_collector_12](#d-ratdom_bone_collector_12)

    <span id="d-ratdom_bone_collector_52"></span>**`ratdom_bone_collector_52`** Loirash: “Well, no. This is my favorite bone, it makes a good sound. Put it back, please.”


    <span id="d-ratdom_bone_collector_54"></span>**`ratdom_bone_collector_54`** Loirash: “Yes you have. I'd better put it back again. This is a very valuable bone, you know? [Loirash takes the bone from you]” — **effects:** clears stage 120 of [ratdom_nondisplay (hidden flag)](../quests/ratdom_nondisplay.md#stage-120)

    - “I see.” → *conversation ends*

    <span id="d-ratdom_bone_collector_22"></span>**`ratdom_bone_collector_22`** Loirash: “Sure. Feel free.”


    <span id="d-ratdom_bone_collector_12"></span>**`ratdom_bone_collector_12`** Loirash: “I am Loirash. Nice to meet you.”

    - “Hi, nice to meet you.” → [ratdom_bone_collector_14](#d-ratdom_bone_collector_14)
    - “What are you doing here?” → [ratdom_bone_collector_16](#d-ratdom_bone_collector_16)

    <span id="d-ratdom_bone_collector_14"></span>**`ratdom_bone_collector_14`** Loirash: “You're probably wondering what I'm doing here deep in this dark cave.”

    - Next → [ratdom_bone_collector_16](#d-ratdom_bone_collector_16)

    <span id="d-ratdom_bone_collector_16"></span>**`ratdom_bone_collector_16`** Loirash: “I am an instrument maker. Professional musical instruments, you know?”

    - Next → [ratdom_bone_collector_18](#d-ratdom_bone_collector_18)

    <span id="d-ratdom_bone_collector_18"></span>**`ratdom_bone_collector_18`** Loirash: “At the moment I'm working on a new instrument made entirely of bone. I expect a sound from it that sends chills down the spine.”

    - “It's already doing that to me.” → [ratdom_bone_collector_20](#d-ratdom_bone_collector_20)



## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 11 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_bone_collector.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_bone_collector.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_bone_collector.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_bone_collector.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `ratdom_bone_collector` · Data from v0.8.18</small>
