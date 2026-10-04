# ![](../assets/icons/monsters/monsters_men_3.png){ .sprite } Blackwater chamber guard

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 60 |
| Max AP | 10 |
| Attack cost | 5 |
| Move cost | 5 |
| Damage | 3 to 6 |
| Attack chance | 60 |
| Block chance | 70 |
| Damage resistance | 3 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [blackwater_mountain45](../maps/blackwater_mountain45.md)

## Quests

- [Clouded intent](../quests/prim_hunt.md): stages 140

??? quote "Dialogue (10 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-blackwater_throneguard"></span>**`blackwater_throneguard`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 240 of [The agent and the beast](../quests/bwm_agent.md#stage-240))* → [blackwater_throneguard_5](#d-blackwater_throneguard_5)
    - branch 2 *(if reached stage 140 of [Clouded intent](../quests/prim_hunt.md#stage-140))* → [blackwater_throneguard_5](#d-blackwater_throneguard_5)
    - branch 3 *(if reached stage 250 of [The agent and the beast](../quests/bwm_agent.md#stage-250); reached stage 250 of [Clouded intent](../quests/prim_hunt.md#stage-250))* → [blackwater_throneguard_10](#d-blackwater_throneguard_10)
    - branch 4 *(if reached stage 250 of [The agent and the beast](../quests/bwm_agent.md#stage-250); reached stage 251 of [Clouded intent](../quests/prim_hunt.md#stage-251))* → [blackwater_throneguard_10](#d-blackwater_throneguard_10)
    - branch 5 *(if reached stage 251 of [The agent and the beast](../quests/bwm_agent.md#stage-251); reached stage 250 of [Clouded intent](../quests/prim_hunt.md#stage-250))* → [blackwater_throneguard_10](#d-blackwater_throneguard_10)
    - branch 6 *(if reached stage 251 of [The agent and the beast](../quests/bwm_agent.md#stage-251); reached stage 251 of [Clouded intent](../quests/prim_hunt.md#stage-251))* → [blackwater_throneguard_10](#d-blackwater_throneguard_10)
    - branch 7 → [blackwater_throneguard_1](#d-blackwater_throneguard_1)

    <span id="d-blackwater_throneguard_5"></span>**`blackwater_throneguard_5`** Blackwater chamber guard: “Oh, it is you.”

    - Next → [blackwater_throneguard_2](#d-blackwater_throneguard_2)

    <span id="d-blackwater_throneguard_10"></span>**`blackwater_throneguard_10`** Blackwater chamber guard: “Hey, psst.”

    - “What?” → [blackwater_throneguard_11](#d-blackwater_throneguard_11)
    - “If you want to say something, speak loudly.” → [blackwater_throneguard_1](#d-blackwater_throneguard_1)

    <span id="d-blackwater_throneguard_1"></span>**`blackwater_throneguard_1`** Blackwater chamber guard: “Only residents of Blackwater mountain or faction members are allowed in here.”

    - “Here, I have a written permit to enter.” *(if hand over 1× [Forged papers for Blackwater](../items/bwm_permit.md))* → [blackwater_throneguard_3](#d-blackwater_throneguard_3)

    <span id="d-blackwater_throneguard_2"></span>**`blackwater_throneguard_2`** Blackwater chamber guard: “I will let you through. Please go right ahead.”

    - “Thank you.” → *NPC leaves*
    - “Yes, get out of my way.” → *NPC leaves*

    <span id="d-blackwater_throneguard_11"></span>**`blackwater_throneguard_11`** Blackwater chamber guard: “Harlenn is a wise and strong leader, but unfortunately just as stubborn as Guthbered.”

    - Next → [blackwater_throneguard_12](#d-blackwater_throneguard_12)

    <span id="d-blackwater_throneguard_3"></span>**`blackwater_throneguard_3`** Blackwater chamber guard: “A permit you say? Let me see that.” — **effects:** sets stage 140 of [Clouded intent](../quests/prim_hunt.md#stage-140)

    - Next → [blackwater_throneguard_4](#d-blackwater_throneguard_4)

    <span id="d-blackwater_throneguard_12"></span>**`blackwater_throneguard_12`** Blackwater chamber guard: “Thank you for not inciting the argument any further. Maybe someday there will be something like peace again.”

    - “I wish it for you. Can I go in here?” → [blackwater_throneguard_13](#d-blackwater_throneguard_13)

    <span id="d-blackwater_throneguard_4"></span>**`blackwater_throneguard_4`** Blackwater chamber guard: “Well, it has the signature and all. I guess it checks out all right.”

    - Next → [blackwater_throneguard_2](#d-blackwater_throneguard_2)

    <span id="d-blackwater_throneguard_13"></span>**`blackwater_throneguard_13`** Blackwater chamber guard: “OK. I trust you not to do any mischief.”

    - “Sure.” → [blackwater_throneguard_2](#d-blackwater_throneguard_2)
    - “[Lie] Sure.” → [blackwater_throneguard_2](#d-blackwater_throneguard_2)



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=blackwater_chamber_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=blackwater_chamber_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=blackwater_chamber_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=blackwater_chamber_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `blackwater_chamber_guard` · Data from v0.8.18</small>
