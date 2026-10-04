# ![](../assets/icons/monsters/monsters_tometik7_38.png){ .sprite } Sly Seraphina

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

- [crackshot_hideout4](../maps/crackshot_hideout4.md)

## Quests

- [Troubling times](../quests/troubling_times.md): stages 260, 270
- [troubling_times_nd (hidden flag)](../quests/troubling_times_nd.md): stages 10

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Sly Seraphina. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/tt_sly5.json" data-npc="Sly Seraphina" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (14 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-tt_sly5"></span>**`tt_sly5`** Sly Seraphina: “Suits me, this place. Don't you think?”

    - “Better help me search.” *(if reached stage 10 of [troubling_times_nd (hidden flag)](../quests/troubling_times_nd.md#stage-10); 8 rounds passed since timer “tt_search”)* → [tt_sly5_10](#d-tt_sly5_10)
    - “[Sarcastic] Truly royal.” → [tt_sly5_2](#d-tt_sly5_2)
    - “This throne looks familiar to me.” → [tt_sly5_8](#d-tt_sly5_8)

    <span id="d-tt_sly5_10"></span>**`tt_sly5_10`** Sly Seraphina: “Of course I'll help you. What are you looking for?” — **effects:** sets stage 260 of [Troubling times](../quests/troubling_times.md#stage-260)

    - “Luthor's ring, of course. I just can't find it.” → [tt_sly5_12](#d-tt_sly5_12)

    <span id="d-tt_sly5_2"></span>**`tt_sly5_2`** Sly Seraphina: “Royal, yes.”

    - Next → [tt_sly5_3](#d-tt_sly5_3)

    <span id="d-tt_sly5_8"></span>**`tt_sly5_8`** Sly Seraphina: “So you've been to King Luthor's tomb. Yes, we have ... borrowed ... his throne.”

    - “Oh.” → [tt_sly5](#d-tt_sly5)

    <span id="d-tt_sly5_12"></span>**`tt_sly5_12`** Sly Seraphina: “Ah - you are looking for this ring here, am I right?”

    - “What? And I've been searching here for hours!” → [tt_sly5_20](#d-tt_sly5_20)

    <span id="d-tt_sly5_3"></span>**`tt_sly5_3`** Sly Seraphina: “In fact, I am King Luthor's heir. He's my ancestor.” — **effects:** sets stage 10 of [troubling_times_nd (hidden flag)](../quests/troubling_times_nd.md#stage-10)

    - “Really?” → [tt_sly5_4](#d-tt_sly5_4)

    <span id="d-tt_sly5_20"></span>**`tt_sly5_20`** Sly Seraphina: “Well, you were so engrossed in the matter that I didn't want to disturb you.”

    - “[Grumble]” → [tt_sly5_22](#d-tt_sly5_22)

    <span id="d-tt_sly5_4"></span>**`tt_sly5_4`** Sly Seraphina: “How else would I be able to wear his gloves without getting hurt?”

    - “True.” → [tt_sly5_6](#d-tt_sly5_6)

    <span id="d-tt_sly5_22"></span>**`tt_sly5_22`** Sly Seraphina: “Okay, we're done here. We should get out of here now.”

    - Next → [tt_sly5_24](#d-tt_sly5_24)

    <span id="d-tt_sly5_6"></span>**`tt_sly5_6`** Sly Seraphina: “Nothing to be proud of though. Forget it, child. I should have kept quiet about it.”


    <span id="d-tt_sly5_24"></span>**`tt_sly5_24`** Sly Seraphina: “The monsters will come back. Then the door should be closed and sealed. From the outside.”

    - “And all the riches?” → [tt_sly5_26](#d-tt_sly5_26)

    <span id="d-tt_sly5_26"></span>**`tt_sly5_26`** Sly Seraphina: “Don't leave anything here you want to keep. We'll never go back in here.”

    - Next → [tt_sly5_30](#d-tt_sly5_30)

    <span id="d-tt_sly5_30"></span>**`tt_sly5_30`** Sly Seraphina: “Here, catch the ring! Keep it safe and take it to Talion. I'm off.” — **effects:** spawns monsters on lake_shore_road_9, spawns monsters on lake_shore_road_9, removes monsters from crackshot_hideout4, sets stage 270 of [Troubling times](../quests/troubling_times.md#stage-270), gives 1× [Luthor's Ring](../items/ring_luthor.md)

    - “Wait ...” → [tt_sly5_32](#d-tt_sly5_32)

    <span id="d-tt_sly5_32"></span>**`tt_sly5_32`** [Dummy NPC](../monsters/none.md): “A light breeze remains where Seraphina had just been sitting.”




## Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added<br>Dialogue: 14 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=tt_seraphina5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `tt_seraphina5` · Data from v0.8.18</small>
