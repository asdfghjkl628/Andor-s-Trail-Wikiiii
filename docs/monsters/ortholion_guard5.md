# ![](../assets/icons/monsters/monsters_omi2_11.png){ .sprite } Feygard mountain scout

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 3 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [blackwater_mountain10](../maps/blackwater_mountain10.md)

## Quests

- [Climbing up is forbidden](../quests/Omi2_bwm1.md): stages 47

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-fms_selector"></span>**`fms_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 47 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-47))* → [fms_3](#d-fms_3)
    - branch 2 *(if reached stage 46 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-46))* → [fms_1](#d-fms_1)
    - branch 3 → [fms_0](#d-fms_0)

    <span id="d-fms_3"></span>**`fms_3`** Feygard mountain scout: “I'll lead the way. Thank you kid, now go back to the village. It's safer there.” — **effects:** sets stage 47 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-47), removes monsters from blackwater_mountain10, removes monsters from blackwater_mountain10, removes monsters from blackwater_mountain10, removes monsters from blackwater_mountain10

    - “I can handle myself, thanks.” → *NPC leaves*
    - “Be careful, I heard mountain wolves are a trouble for Feygard soldiers.” → *NPC leaves*
    - “I will. Bye.” → *NPC leaves*

    <span id="d-fms_1"></span>**`fms_1`** Feygard mountain scout: “Hey! You alright?”

    - “Yeah, bye.” → *conversation ends*
    - “I lost 10,000 gold over here.” → [fms_2a](#d-fms_2a)
    - “[Shows the signet] Your general has gone to Elm mine. He could be in trouble.” *(if carry 1× [Ortholion's signet](../items/ortholion_signet.md))* → [fms_2b](#d-fms_2b)

    <span id="d-fms_0"></span>**`fms_0`** Feygard mountain scout: “Hey kid! Go back to your village and play inside!”

    - “Play? Hah!” → *conversation ends*

    <span id="d-fms_2a"></span>**`fms_2a`** Feygard mountain scout: “Yeah, sure. We are here posted by command of General Orhtolion of Feygard. You have no business here.”

    - “[shows the signet] Yeah, sure. Now hurry up! Your general is waiting for you in the Elm mine.” *(if carry 1× [Ortholion's signet](../items/ortholion_signet.md))* → [fms_2b](#d-fms_2b)
    - “What a boring girl! Bye.” → *conversation ends*

    <span id="d-fms_2b"></span>**`fms_2b`** Feygard mountain scout: “[shouts] Hey, slackers! You're moving now. It's an order. Prepare yourselves, we are going to the Elm mine, our general needs us!”

    - Next → [fms_3](#d-fms_3)



## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 6 lines added |
| [v0.7.15](../versions/0.7.15.md) | Dialogue: 2 lines changed |
| [v0.8.12.1](../versions/0.8.12.1.md) | Dialogue: 3 lines changed<br>· text: “*shouts* Hey, slackers! You're moving now. It's an order. Prepare you…” → “[shouts] Hey, slackers! You're moving now. It's an order. Prepare you…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard5.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `ortholion_guard5` · Data from v0.8.18</small>
