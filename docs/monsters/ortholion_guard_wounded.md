# ![](../assets/icons/monsters/monsters_omi2_11.png){ .sprite } Wounded Feygard mountain scout

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

- [blackwater_mountain31](../maps/blackwater_mountain31.md)

## Quests

- [Climbing up is forbidden](../quests/Omi2_bwm1.md): stages 34, 35

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-ortholion_gw_selector"></span>**`ortholion_gw_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 34 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-34))* → [ortholion_gw_sleeping](#d-ortholion_gw_sleeping)
    - branch 2 → [ortholion_gw_1](#d-ortholion_gw_1)

    <span id="d-ortholion_gw_sleeping"></span>**`ortholion_gw_sleeping`** [Dummy NPC](../monsters/none.md): “The scout is sleeping on the ground. Her wounds don't seem to be that bad.”


    <span id="d-ortholion_gw_1"></span>**`ortholion_gw_1`** Wounded Feygard mountain scout: “*cough*, *cough* What the... *cough*. Go back home kid, quick. This place is *cough*, dangerous.”

    - “Where can I find General Ortholion?” → [ortholion_gw_2a](#d-ortholion_gw_2a)
    - “Gonna rest here first, sweet dreams.” → *conversation ends*
    - “What happened to you?” → [ortholion_gw_2b](#d-ortholion_gw_2b)

    <span id="d-ortholion_gw_2a"></span>**`ortholion_gw_2a`** Wounded Feygard mountain scout: “What? What do you have to do with *cough*, him?”

    - “[Lie] I have an important message to deliver to him. It comes from Prim.” → [ortholion_gw_3a](#d-ortholion_gw_3a)
    - “Never mind, what happened to you?” → [ortholion_gw_2b](#d-ortholion_gw_2b)

    <span id="d-ortholion_gw_2b"></span>**`ortholion_gw_2b`** Wounded Feygard mountain scout: “We were on the way to Blackwater Settlement, when we *cough*, *cough*, were attacked by a group of white wyrms. I got, uh, somewhat injured... So my general decided I should wait right here, safe from the monsters.” — **effects:** sets stage 34 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-34), clears stage 16 of [Hidden: events in bwm (hidden flag)](../quests/bwm72_beginning.md#stage-16)

    - “Hope you get better. I must leave.” → [ortholion_gw_3b](#d-ortholion_gw_3b)
    - “OK. That's everything I need to know.” → [ortholion_gw_3c](#d-ortholion_gw_3c)
    - “Feygard scum... Are you always such bigmouths? [Kill her]” → [ortholion_gw_4](#d-ortholion_gw_4)

    <span id="d-ortholion_gw_3a"></span>**`ortholion_gw_3a`** Wounded Feygard mountain scout: “I don't *cough*, think anybody would be that crazy to send a kid to a place like this. Sorry, *cough*, I don't have the energy to listen to nonsense.”


    <span id="d-ortholion_gw_3b"></span>**`ortholion_gw_3b`** Wounded Feygard mountain scout: “Thank you, thank *cough* you.”


    <span id="d-ortholion_gw_3c"></span>**`ortholion_gw_3c`** Wounded Feygard mountain scout: “What do you mean? *cough*”

    - “Nothing at all, bye.” → *conversation ends*
    - “Sweet dreams, idiot! [Kill her]” → [ortholion_gw_4](#d-ortholion_gw_4)

    <span id="d-ortholion_gw_4"></span>**`ortholion_gw_4`** Wounded Feygard mountain scout: “Wh..*cough* NO! [You manage to land a fatal blow to the already wounded Feygard scout. Once you're sure she's dead, you set her body aside, out of the cabin]” — **effects:** sets stage 35 of [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-35), removes monsters from blackwater_mountain31

    - “One less. Good.” → *NPC leaves*
    - “That was easy.” → *NPC leaves*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard_wounded.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard_wounded.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard_wounded.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=ortholion_guard_wounded.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `ortholion_guard_wounded` · Data from v0.8.18</small>
