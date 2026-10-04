# ![](../assets/icons/monsters/monsters_gisons_11.png){ .sprite } Liberated Elytharan ghost

| Stat | Value |
|---|---|
| Class | ghost |
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

!!! note "Immune to critical hits"
    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.

## Found on

- [undertell_3_00](../maps/undertell_3_00.md)

## Quests

- [About a girl](../quests/about_a_girl.md): stages 10, 20, 30, 40, 90

??? quote "Dialogue (22 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-elytharan_liberated_ghost_selector"></span>**`elytharan_liberated_ghost_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 10 of [About a girl](../quests/about_a_girl.md#stage-10))* → [elytharan_liberated_ghost_initial](#d-elytharan_liberated_ghost_initial)
    - branch 2 *(if reached stage 10 of [About a girl](../quests/about_a_girl.md#stage-10); NOT reached stage 20 of [About a girl](../quests/about_a_girl.md#stage-20))* → [elytharan_liberated_ghost_about_girl_10](#d-elytharan_liberated_ghost_about_girl_10)
    - branch 3 *(if reached stage 20 of [About a girl](../quests/about_a_girl.md#stage-20); NOT reached stage 30 of [About a girl](../quests/about_a_girl.md#stage-30))* → [elytharan_liberated_ghost_about_girl_20](#d-elytharan_liberated_ghost_about_girl_20)
    - branch 4 *(if latest stage of [About a girl](../quests/about_a_girl.md#stage-30) is 30)* → [elytharan_liberated_ghost_about_girl_30](#d-elytharan_liberated_ghost_about_girl_30)
    - branch 5 *(if reached stage 40 of [About a girl](../quests/about_a_girl.md#stage-40); NOT reached stage 70 of [About a girl](../quests/about_a_girl.md#stage-70))* → [elytharan_liberated_ghost_about_girl_40_not_70](#d-elytharan_liberated_ghost_about_girl_40_not_70)
    - branch 6 *(if reached stage 80 of [About a girl](../quests/about_a_girl.md#stage-80); NOT reached stage 90 of [About a girl](../quests/about_a_girl.md#stage-90))* → [elytharan_liberated_ghost_about_girl_90](#d-elytharan_liberated_ghost_about_girl_90)
    - branch 7 → [elytharan_liberated_ghost_default](#d-elytharan_liberated_ghost_default)

    <span id="d-elytharan_liberated_ghost_initial"></span>**`elytharan_liberated_ghost_initial`** Liberated Elytharan ghost: “Oh thank you Elythara! We are freed at last.”

    - “Freed?” → [elytharan_liberated_ghost_freed_10](#d-elytharan_liberated_ghost_freed_10)

    <span id="d-elytharan_liberated_ghost_about_girl_10"></span>**`elytharan_liberated_ghost_about_girl_10`** [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md): “There is another. A girl. She never came back here when the shades fell. Instead, she hides east of here. Probably in a corner somewhere.” — **effects:** sets stage 10 of [About a girl](../quests/about_a_girl.md#stage-10)

    - “Why would she still hide?” → [elytharan_liberated_ghost_about_girl_10b](#d-elytharan_liberated_ghost_about_girl_10b)

    <span id="d-elytharan_liberated_ghost_about_girl_20"></span>**`elytharan_liberated_ghost_about_girl_20`** [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost2.md): “You have not forgotten her, have you?”

    - “I am still trying to understand what happened to the talisman.” → [elytharan_liberated_ghost_about_girl_20b](#d-elytharan_liberated_ghost_about_girl_20b)

    <span id="d-elytharan_liberated_ghost_about_girl_30"></span>**`elytharan_liberated_ghost_about_girl_30`** [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md): “If the talisman still exists, it will not be with the dead.”

    - “Then where should I look?” → [elytharan_liberated_ghost_about_girl_30b](#d-elytharan_liberated_ghost_about_girl_30b)

    <span id="d-elytharan_liberated_ghost_about_girl_40_not_70"></span>**`elytharan_liberated_ghost_about_girl_40_not_70`** [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md): “What are you doing here? Go find that talisman and bring it to her.”

    - “Yes, of course.” → *conversation ends*

    <span id="d-elytharan_liberated_ghost_about_girl_90"></span>**`elytharan_liberated_ghost_about_girl_90`** [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md): “She came back. We did not think she would.”

    - “I want to speak to her.” → [elytharan_liberated_ghost_about_girl_90b](#d-elytharan_liberated_ghost_about_girl_90b)

    <span id="d-elytharan_liberated_ghost_default"></span>**`elytharan_liberated_ghost_default`** Liberated Elytharan ghost: “It is so wonderful to finally be free of the evil that surrounded those shades...thank you Elythara!”

    - “What?! It was thanks to me. You guys are hopeless.” → *conversation ends*

    <span id="d-elytharan_liberated_ghost_freed_10"></span>**`elytharan_liberated_ghost_freed_10`** [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost2.md): “Yes! Freed from the rule of those Kha'zaan shades.”

    - “But that was not Elythara. That was me.” → [elytharan_liberated_ghost_freed_20](#d-elytharan_liberated_ghost_freed_20)

    <span id="d-elytharan_liberated_ghost_about_girl_10b"></span>**`elytharan_liberated_ghost_about_girl_10b`** [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost2.md): “Fear does not listen to truth. She made something to keep it away.”

    - “What did she make?” → [elytharan_liberated_ghost_about_girl_10c](#d-elytharan_liberated_ghost_about_girl_10c)

    <span id="d-elytharan_liberated_ghost_about_girl_20b"></span>**`elytharan_liberated_ghost_about_girl_20b`** [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md): “They used to gather our things. Count them. Decide what mattered.” — **effects:** sets stage 30 of [About a girl](../quests/about_a_girl.md#stage-30)

    - “Who did?” → [elytharan_liberated_ghost_about_girl_20c](#d-elytharan_liberated_ghost_about_girl_20c)

    <span id="d-elytharan_liberated_ghost_about_girl_30b"></span>**`elytharan_liberated_ghost_about_girl_30b`** Liberated Elytharan ghost: “With those who believed fear could be shaped. Go to the Masters.” — **effects:** sets stage 40 of [About a girl](../quests/about_a_girl.md#stage-40), spawns monsters on undertell_3_12

    - “Don't worry, I will take care of this for you guys.” → *conversation ends*

    <span id="d-elytharan_liberated_ghost_about_girl_90b"></span>**`elytharan_liberated_ghost_about_girl_90b`** [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost2.md): “She is here because she chose to be. Not because fear left her.”

    - “Then let me hear it from her.” → [elytharan_liberated_ghost_about_girl_90c](#d-elytharan_liberated_ghost_about_girl_90c)

    <span id="d-elytharan_liberated_ghost_freed_20"></span>**`elytharan_liberated_ghost_freed_20`** [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost.md): “Listen you, we've been hiding for Elythara knows how long, and the first thing you say to us is a lie?”

    - “But it was me, I swear to Elythara it was me.” → [elytharan_liberated_ghost_freed_30](#d-elytharan_liberated_ghost_freed_30)

    <span id="d-elytharan_liberated_ghost_about_girl_10c"></span>**`elytharan_liberated_ghost_about_girl_10c`** Liberated Elytharan ghost: “A folded coin. Copper. She believed evil could be trapped if it could not breathe.” — **effects:** sets stage 20 of [About a girl](../quests/about_a_girl.md#stage-20)

    - “Where is it now?” → [elytharan_liberated_ghost_about_girl_10d](#d-elytharan_liberated_ghost_about_girl_10d)

    <span id="d-elytharan_liberated_ghost_about_girl_20c"></span>**`elytharan_liberated_ghost_about_girl_20c`** Liberated Elytharan ghost: “Those above us. Those who studied fear instead of ending it.”

    - “The Masters?” → [elytharan_liberated_ghost_about_girl_30](#d-elytharan_liberated_ghost_about_girl_30)

    <span id="d-elytharan_liberated_ghost_about_girl_90c"></span>**`elytharan_liberated_ghost_about_girl_90c`** [Syrra](../monsters/about_a_girl_final.md): “Do not mistake silence for weakness.”

    - “You do not have to hide anymore.” → [about_girl_syrra_90](#d-about_girl_syrra_90)

    <span id="d-elytharan_liberated_ghost_freed_30"></span>**`elytharan_liberated_ghost_freed_30`** [Liberated Elytharan ghost](../monsters/elytharan_liberated_ghost2.md): “If that is true, then maybe you could help us help someone else?”

    - “Who?” → [elytharan_liberated_ghost_about_girl_10](#d-elytharan_liberated_ghost_about_girl_10)

    <span id="d-elytharan_liberated_ghost_about_girl_10d"></span>**`elytharan_liberated_ghost_about_girl_10d`** Liberated Elytharan ghost: “Lost. Taken. We do not know which. Only that it never came back.”

    - “I will look for it.” → [elytharan_liberated_ghost_about_girl_20b](#d-elytharan_liberated_ghost_about_girl_20b)

    <span id="d-about_girl_syrra_90"></span>**`about_girl_syrra_90`** Liberated Elytharan ghost: “I know. It still follows me. Just not as closely.”

    - “Fear does not decide where you stand.” → [about_girl_syrra_90b](#d-about_girl_syrra_90b)

    <span id="d-about_girl_syrra_90b"></span>**`about_girl_syrra_90b`** Liberated Elytharan ghost: “No. But it remembers. I will too.”

    - “Then this is enough.” → [about_girl_syrra_90c](#d-about_girl_syrra_90c)

    <span id="d-about_girl_syrra_90c"></span>**`about_girl_syrra_90c`** Liberated Elytharan ghost: “It is.” — **effects:** sets stage 90 of [About a girl](../quests/about_a_girl.md#stage-90)




## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 22 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elytharan_liberated_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elytharan_liberated_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elytharan_liberated_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=elytharan_liberated_ghost.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `elytharan_liberated_ghost` · Data from v0.8.18</small>
