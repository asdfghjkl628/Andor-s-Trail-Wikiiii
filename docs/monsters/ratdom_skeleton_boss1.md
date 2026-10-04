# ![](../assets/icons/monsters/monsters_tometik8_43.png){ .sprite } Roskelt

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

- [ratdom_maze_415](../maps/ratdom_maze_415.md)

## Quests

- [Skeleton brothers](../quests/ratdom_skeleton.md): stages 41, 52, 61, 90
- [Yellow is it](../quests/ratdom_quest.md): stages 37

??? quote "Dialogue (21 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ratdom_skeleton_boss1"></span>**`ratdom_skeleton_boss1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-90))* → [ratdom_skeleton_boss_90](#d-ratdom_skeleton_boss_90)
    - branch 2 *(if reached stage 71 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-71); reached stage 61 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-61))* → [ratdom_skeleton_boss_70](#d-ratdom_skeleton_boss_70)
    - branch 3 *(if reached stage 61 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-61))* → [ratdom_skeleton_boss_60](#d-ratdom_skeleton_boss_60)
    - branch 4 *(if reached stage 51 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-51))* → [ratdom_skeleton_boss_51](#d-ratdom_skeleton_boss_51)
    - branch 5 *(if reached stage 41 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-41))* → [ratdom_skeleton_boss_40](#d-ratdom_skeleton_boss_40)
    - branch 6 → [ratdom_skeleton_boss_11](#d-ratdom_skeleton_boss_11)

    <span id="d-ratdom_skeleton_boss_90"></span>**`ratdom_skeleton_boss_90`** Roskelt: “Thank you again for your effort.”

    - “It could have been a bit more gold.” → [ratdom_skeleton_boss_90_10](#d-ratdom_skeleton_boss_90_10)

    <span id="d-ratdom_skeleton_boss_70"></span>**`ratdom_skeleton_boss_70`** Roskelt: “Mortal! Did you fulfil your task?”

    - “Yes. Your brother is dead.” → [ratdom_skeleton_boss_70_10](#d-ratdom_skeleton_boss_70_10)

    <span id="d-ratdom_skeleton_boss_60"></span>**`ratdom_skeleton_boss_60`** Roskelt: “Mortal! Did you fulfil your task?”

    - “To kill your brother? No, not yet.” → [ratdom_skeleton_boss_60_10](#d-ratdom_skeleton_boss_60_10)

    <span id="d-ratdom_skeleton_boss_51"></span>**`ratdom_skeleton_boss_51`** Roskelt: “Mortal! Did you fulfil your task?”

    - “I delivered your message, but Bloskelt was just laughing.” → [ratdom_skeleton_boss_51_10](#d-ratdom_skeleton_boss_51_10)

    <span id="d-ratdom_skeleton_boss_40"></span>**`ratdom_skeleton_boss_40`** Roskelt: “Mortal! Where is my brother?”

    - “I didn't find him yet.” → [ratdom_skeleton_boss_40_10](#d-ratdom_skeleton_boss_40_10)

    <span id="d-ratdom_skeleton_boss_11"></span>**`ratdom_skeleton_boss_11`** Roskelt: “Mortal - What are you doing in my realm?”

    - “I have lost my way. Could you help me?” *(if NOT reached stage 42 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-42))* → [ratdom_skeleton_boss_11_10](#d-ratdom_skeleton_boss_11_10)
    - “I have come to kill you.” *(if reached stage 62 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-62))* → [ratdom_skeleton_boss_10_20](#d-ratdom_skeleton_boss_10_20)
    - “Who are you?” *(if NOT reached stage 62 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-62))* → [ratdom_skeleton_boss_11_30](#d-ratdom_skeleton_boss_11_30)

    <span id="d-ratdom_skeleton_boss_90_10"></span>**`ratdom_skeleton_boss_90_10`** Roskelt: “What? Do I hear ungrateful words?”

    - “Eh, no, it is nothing. Bye.” → *conversation ends*
    - “I will take my gold now - attack!” → *fight starts*

    <span id="d-ratdom_skeleton_boss_70_10"></span>**`ratdom_skeleton_boss_70_10`** Roskelt: “Good. I will shower you with gold, jewels and bones.” — **effects:** sets stage 90 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-90), gives 18× [Gold coins](../items/gold.md), gives 2× [Glass gem](../items/gem1.md), sets stage 37 of [Yellow is it](../quests/ratdom_quest.md#stage-37), gives 1× [Rib bones of a rat](../items/ratdom_rat_skelett_ribs.md)

    - “Hm, not much of a shower ... and ugh - there are even rat bones included.” → [ratdom_skeleton_boss_70_20](#d-ratdom_skeleton_boss_70_20)

    <span id="d-ratdom_skeleton_boss_60_10"></span>**`ratdom_skeleton_boss_60_10`** Roskelt: “Then what do you want here? Go and do it.”


    <span id="d-ratdom_skeleton_boss_51_10"></span>**`ratdom_skeleton_boss_51_10`** Roskelt: “Then go again. And kill him.” — **effects:** sets stage 61 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-61)

    - “Kill him? But it is your brother?” → [ratdom_skeleton_boss_50_20](#d-ratdom_skeleton_boss_50_20)

    <span id="d-ratdom_skeleton_boss_40_10"></span>**`ratdom_skeleton_boss_40_10`** Roskelt: “Then look again, thoroughly.”


    <span id="d-ratdom_skeleton_boss_11_10"></span>**`ratdom_skeleton_boss_11_10`** Roskelt: “Of course I could. But why should I?”

    - “Yes, right. Why should you?” → [ratdom_skeleton_boss_11](#d-ratdom_skeleton_boss_11)

    <span id="d-ratdom_skeleton_boss_10_20"></span>**`ratdom_skeleton_boss_10_20`** Roskelt: “Mortal! You amuse me. I will have you as my jester.”

    - “We'll see! Let's fight!” → *fight starts*

    <span id="d-ratdom_skeleton_boss_11_30"></span>**`ratdom_skeleton_boss_11_30`** Roskelt: “I am Roskelt, the Great. King of the caves. Nobody equals me.”

    - “I have lost my way. Could you help me?” *(if NOT reached stage 42 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-42))* → [ratdom_skeleton_boss_11_10](#d-ratdom_skeleton_boss_11_10)
    - “Aha.” *(if NOT reached stage 42 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-42))* → [ratdom_skeleton_boss_11_40](#d-ratdom_skeleton_boss_11_40)
    - “Interesting. Bloskelt said the same.” *(if reached stage 42 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-42))* → [ratdom_skeleton_boss_11_50](#d-ratdom_skeleton_boss_11_50)

    <span id="d-ratdom_skeleton_boss_70_20"></span>**`ratdom_skeleton_boss_70_20`** Roskelt: “What? Do I hear ungrateful words?”

    - “No, everything is well.” → *conversation ends*
    - “Enough! Let's fight!” → *fight starts*

    <span id="d-ratdom_skeleton_boss_50_20"></span>**`ratdom_skeleton_boss_50_20`** Roskelt: “Yes, that's why. Hurry now.”

    - “Oh, OK.” → *conversation ends*

    <span id="d-ratdom_skeleton_boss_11_40"></span>**`ratdom_skeleton_boss_11_40`** Roskelt: “There is just one being that denies me my rightful title. Bloskelt, my wretched brother.”

    - Next → [ratdom_skeleton_boss_11_42](#d-ratdom_skeleton_boss_11_42)

    <span id="d-ratdom_skeleton_boss_11_50"></span>**`ratdom_skeleton_boss_11_50`** Roskelt: “My brother again! He always tries to mock me! And surely you are now going to tell me, that I should surrender?”

    - “Eh, yes. How did you know?” → [ratdom_skeleton_boss_11_52](#d-ratdom_skeleton_boss_11_52)

    <span id="d-ratdom_skeleton_boss_11_42"></span>**`ratdom_skeleton_boss_11_42`** Roskelt: “You go and find Bloskelt! Tell him that he shall come to me to surrender! He would receive the grace of a quick, almost painless death.” — **effects:** sets stage 41 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-41)

    - “How generous.” → *conversation ends*

    <span id="d-ratdom_skeleton_boss_11_52"></span>**`ratdom_skeleton_boss_11_52`** Roskelt: “HAHAHA! I will not give up and surrender to him! Never! Tell him that. HAHAHAHA!” — **effects:** sets stage 52 of [Skeleton brothers](../quests/ratdom_skeleton.md#stage-52)

    - “I will go and tell Bloskelt. Although the messenger of bad news always gets into trouble ...” → *conversation ends*



## Version history

| Version | Change |
|---|---|
| [v0.8.5](../versions/0.8.5.md) | Added<br>Dialogue: 21 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skeleton_boss1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skeleton_boss1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skeleton_boss1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ratdom_skeleton_boss1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `ratdom_skeleton_boss1` · Data from v0.8.18</small>
