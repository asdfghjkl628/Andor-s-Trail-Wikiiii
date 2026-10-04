# ![](../assets/icons/monsters/monsters_tometik8_44.png){ .sprite } Bloskelt

| Stat | Value |
|---|---|
| Class | construct |
| HP | 100 |
| Max AP | 10 |
| Attack cost | 5 |
| Move cost | 10 |
| Damage | 15 to 30 |
| Attack chance | 100 |
| Block chance | 0 |
| Damage resistance | 5 |
| Critical skill | 0 |
| Critical multiplier | 0 |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.

## Found on

- [ratdom_maze_416](../maps/ratdom_maze_416.md)

## Quests

- [Skeleton brothers](../quests/ratdom_skeleton.md): stages 42, 51, 62, 90
- [Yellow is it](../quests/ratdom_quest.md): stages 37

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Bloskelt. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/ratdom_skeleton_boss2.json" data-npc="Bloskelt" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (21 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ratdom_skeleton_boss2"></span>**`ratdom_skeleton_boss2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-90))* → [ratdom_skeleton_boss_90](#d-ratdom_skeleton_boss_90)
    - branch 2 *(if reached stage 72 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-72); reached stage 62 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-62))* → [ratdom_skeleton_boss_70](#d-ratdom_skeleton_boss_70)
    - branch 3 *(if reached stage 62 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-62))* → [ratdom_skeleton_boss_60](#d-ratdom_skeleton_boss_60)
    - branch 4 *(if reached stage 52 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-52))* → [ratdom_skeleton_boss_52](#d-ratdom_skeleton_boss_52)
    - branch 5 *(if reached stage 42 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-42))* → [ratdom_skeleton_boss_40](#d-ratdom_skeleton_boss_40)
    - branch 6 → [ratdom_skeleton_boss_12](#d-ratdom_skeleton_boss_12)

    <span id="d-ratdom_skeleton_boss_90"></span>**`ratdom_skeleton_boss_90`** Bloskelt: “Thank you again for your effort.”

    - “It could have been a bit more gold.” → [ratdom_skeleton_boss_90_10](#d-ratdom_skeleton_boss_90_10)

    <span id="d-ratdom_skeleton_boss_70"></span>**`ratdom_skeleton_boss_70`** Bloskelt: “Mortal! Did you fulfil your task?”

    - “Yes. Your brother is dead.” → [ratdom_skeleton_boss_70_10](#d-ratdom_skeleton_boss_70_10)

    <span id="d-ratdom_skeleton_boss_60"></span>**`ratdom_skeleton_boss_60`** Bloskelt: “Mortal! Did you fulfil your task?”

    - “To kill your brother? No, not yet.” → [ratdom_skeleton_boss_60_10](#d-ratdom_skeleton_boss_60_10)

    <span id="d-ratdom_skeleton_boss_52"></span>**`ratdom_skeleton_boss_52`** Bloskelt: “Mortal! Did you fulfil your task?”

    - “I delivered your message, but Roskelt was just laughing.” → [ratdom_skeleton_boss_52_10](#d-ratdom_skeleton_boss_52_10)

    <span id="d-ratdom_skeleton_boss_40"></span>**`ratdom_skeleton_boss_40`** Bloskelt: “Mortal! Where is my brother?”

    - “I didn't find him yet.” → [ratdom_skeleton_boss_40_10](#d-ratdom_skeleton_boss_40_10)

    <span id="d-ratdom_skeleton_boss_12"></span>**`ratdom_skeleton_boss_12`** Bloskelt: “Mortal - What are you doing in my realm?”

    - “I have lost my way. Could you help me?” *(if NOT reached stage 41 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-41))* → [ratdom_skeleton_boss_12_10](#d-ratdom_skeleton_boss_12_10)
    - “I have come to kill you.” *(if reached stage 61 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-61))* → [ratdom_skeleton_boss_10_20](#d-ratdom_skeleton_boss_10_20)
    - “Who are you?” *(if NOT reached stage 61 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-61))* → [ratdom_skeleton_boss_12_30](#d-ratdom_skeleton_boss_12_30)

    <span id="d-ratdom_skeleton_boss_90_10"></span>**`ratdom_skeleton_boss_90_10`** Bloskelt: “What? Do I hear ungrateful words?”

    - “Eh, no, it is nothing. Bye.” → *conversation ends*
    - “I will take my gold now - attack!” → *fight starts*

    <span id="d-ratdom_skeleton_boss_70_10"></span>**`ratdom_skeleton_boss_70_10`** Bloskelt: “Good. I will shower you with gold, jewels and bones.” — **effects:** sets stage 90 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-90), gives 18× [Gold coins](../items/gold.md), gives 2× [Glass gem](../items/gem1.md), sets stage 37 of [Yellow is it](../quests/ratdom_quest.md#stage-37), gives 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md)

    - “Hm, not much of a shower ... and ugh - there are even rat bones included.” → [ratdom_skeleton_boss_70_20](#d-ratdom_skeleton_boss_70_20)

    <span id="d-ratdom_skeleton_boss_60_10"></span>**`ratdom_skeleton_boss_60_10`** Bloskelt: “Then what do you want here? Go and do it.”


    <span id="d-ratdom_skeleton_boss_52_10"></span>**`ratdom_skeleton_boss_52_10`** Bloskelt: “Then go again. And kill him.” — **effects:** sets stage 62 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-62)

    - “Kill him? But it is your brother?” → [ratdom_skeleton_boss_50_20](#d-ratdom_skeleton_boss_50_20)

    <span id="d-ratdom_skeleton_boss_40_10"></span>**`ratdom_skeleton_boss_40_10`** Bloskelt: “Then look again, thoroughly.”


    <span id="d-ratdom_skeleton_boss_12_10"></span>**`ratdom_skeleton_boss_12_10`** Bloskelt: “Of course I could. But why should I?”

    - “Yes, right. Why should you?” → [ratdom_skeleton_boss_12](#d-ratdom_skeleton_boss_12)

    <span id="d-ratdom_skeleton_boss_10_20"></span>**`ratdom_skeleton_boss_10_20`** Bloskelt: “Mortal! You amuse me. I will have you as my jester.”

    - “We'll see! Let's fight!” → *fight starts*

    <span id="d-ratdom_skeleton_boss_12_30"></span>**`ratdom_skeleton_boss_12_30`** Bloskelt: “I am Bloskelt, the Great. King of the caves. Nobody equals me.”

    - “I have lost my way. Could you help me?” *(if NOT reached stage 41 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-41))* → [ratdom_skeleton_boss_12_10](#d-ratdom_skeleton_boss_12_10)
    - “Aha.” *(if NOT reached stage 41 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-41))* → [ratdom_skeleton_boss_12_40](#d-ratdom_skeleton_boss_12_40)
    - “Interesting. Roskelt said the same.” *(if reached stage 41 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-41))* → [ratdom_skeleton_boss_12_50](#d-ratdom_skeleton_boss_12_50)

    <span id="d-ratdom_skeleton_boss_70_20"></span>**`ratdom_skeleton_boss_70_20`** Bloskelt: “What? Do I hear ungrateful words?”

    - “No, everything is well.” → *conversation ends*
    - “Enough! Let's fight!” → *fight starts*

    <span id="d-ratdom_skeleton_boss_50_20"></span>**`ratdom_skeleton_boss_50_20`** Bloskelt: “Yes, that's why. Hurry now.”

    - “Oh, OK.” → *conversation ends*

    <span id="d-ratdom_skeleton_boss_12_40"></span>**`ratdom_skeleton_boss_12_40`** Bloskelt: “There is just one being that denies me my rightful title. Roskelt, my wretched brother.”

    - Next → [ratdom_skeleton_boss_12_42](#d-ratdom_skeleton_boss_12_42)

    <span id="d-ratdom_skeleton_boss_12_50"></span>**`ratdom_skeleton_boss_12_50`** Bloskelt: “My brother again! He always tries to mock me! And surely you are now going to tell me, that I should surrender?”

    - “Eh, yes. How did you know?” → [ratdom_skeleton_boss_12_52](#d-ratdom_skeleton_boss_12_52)

    <span id="d-ratdom_skeleton_boss_12_42"></span>**`ratdom_skeleton_boss_12_42`** Bloskelt: “You go and find Roskelt! Tell him that he shall come to me to surrender! He would receive the grace of a quick, almost painless death.” — **effects:** sets stage 42 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-42)

    - “How generous.” → *conversation ends*

    <span id="d-ratdom_skeleton_boss_12_52"></span>**`ratdom_skeleton_boss_12_52`** Bloskelt: “HAHAHA! I will not give up and surrender to him! Never! Tell him that. HAHAHAHA!” — **effects:** sets stage 51 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-51)

    - “I will go and tell Roskelt. Although the messenger of bad news always gets into trouble ...” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 21 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skeleton_boss2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skeleton_boss2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skeleton_boss2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skeleton_boss2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `ratdom_skeleton_boss2` · Data from v0.8.18</small>
