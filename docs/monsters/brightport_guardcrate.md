# ![](../assets/icons/monsters/monsters_ld1_94.png){ .sprite } Brightport guard

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/monsters/monsters_ld1_94.png){ .sprite }</p>

| | |
|---|---|
| **Monster ID** | `brightport_guardcrate` |
| **Type** | NPC |
| **Class** | ? |
| **HP** | 1 |
| **Found in** | Brightport |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

## Combat stats

| Stat | Value |
|---|---|
| HP | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Max AP | 10 |
| Attack cost | 10 AP |
| Attacks per turn | 1 |
| Move cost | 10 AP |
| Critical skill | 0 |
| Critical multiplier | – |
| Crit chance | none (needs critical skill and a multiplier) |

**XP formula** (from the game's loader): ⌈(attacks per turn × attack chance × average damage × (1 + critical skill × multiplier) × 3 + HP × (1 + block chance) + 9 × damage resistance) × 0.7⌉, +50 if its hits inflict a condition. More Exp adds a percentage on top.

<p class="verified">Verified against v0.8.18 monster data and game code (`MonsterTypeParser.java`).</p>


## Locations

| Map | Region | Up to | Notes |
|---|---|---|---|
| [brightport_abandoned](../maps/brightport_abandoned.md) | Brightport | 2 | appears later in a quest |


## Quests

- [Boxed in](../quests/brightport_thieves.md): stages 35
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 144, 159, 173, 209, 210, 220

## Dialogue simulator

Set up your situation (quest stages, items, kills…), then talk to Brightport guard. The simulator follows the game's own rules: it takes the same silent checks, offers only the options you'd really see, and applies their effects (quest stages, items handed over, rewards) as you go.

<div class="dlg-sim" data-src="../../assets/dialogue/brightport_crateguard_selector.json" data-npc="Brightport guard" markdown="0"><noscript>The simulator needs JavaScript. The full dialogue is listed below.</noscript></div>

<p class="verified">Rules verified against v0.8.18 game code (ConversationController.java) and dialogue data.</p>

??? quote "Dialogue (26 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_crateguard_selector"></span>**`brightport_crateguard_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 210 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-210))* → [brightport_guardcrate17](#d-brightport_guardcrate17)
    - Next *(if reached stage 209 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-209))* → [brightport_guardcrate14](#d-brightport_guardcrate14)
    - Next *(if reached stage 173 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-173))* → [brightport_crateguard_arrest3](#d-brightport_crateguard_arrest3)
    - Next *(if reached stage 159 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-159))* → [brightport_crateguard_arrest](#d-brightport_crateguard_arrest)
    - Next → [brightport_crateguard](#d-brightport_crateguard)

    <span id="d-brightport_guardcrate17"></span>**`brightport_guardcrate17`** Brightport guard: “Agreed. You're coming with us. The commander can sort this out.” — **effects:** sets stage 210 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-210)

    - Next → [brightport_crateguard_packageselector](#d-brightport_crateguard_packageselector)

    <span id="d-brightport_guardcrate14"></span>**`brightport_guardcrate14`** [Brightport guard](../monsters/brightport_guardcrate.md): “Enough games. You're coming with us.” — **effects:** sets stage 209 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-209)

    - Next → [brightport_crateguard_packageselector](#d-brightport_crateguard_packageselector)

    <span id="d-brightport_crateguard_arrest3"></span>**`brightport_crateguard_arrest3`** Brightport guard: “I don't think so, we follow the law not the commander. You will be coming with us. We'll interrogate you later about what you were doing here.” — **effects:** sets stage 173 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-173)

    - Next → [brightport_crateguard_packageselector](#d-brightport_crateguard_packageselector)

    <span id="d-brightport_crateguard_arrest"></span>**`brightport_crateguard_arrest`** Brightport guard: “Ha! The commander can forgive a mistake or two. Grab him. We'll interrogate him later” — **effects:** sets stage 159 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-159)

    - Next → [brightport_crateguard_packageselector](#d-brightport_crateguard_packageselector)

    <span id="d-brightport_crateguard"></span>**`brightport_crateguard`** Brightport guard: “Halt! What are you doing here?”

    - “I'm searching for my brother Andor, have you seen him?” *(if NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); NOT reached stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120))* → [brightport_crateguard8](#d-brightport_crateguard8)
    - “That's private. Nothing you need to worry about.” *(if reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60))* → [brightport_crateguard0](#d-brightport_crateguard0)
    - “Gentlemen. Has sir Gunfryk not told you to keep your noses out of places they don't belong?” *(if reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60))* → [brightport_crateguard2](#d-brightport_crateguard2)
    - “I was patrolling the place to keep it safe from troublemakers, obviously.” *(if reached stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120))* → [brightport_crateguard3](#d-brightport_crateguard3)

    <span id="d-brightport_crateguard_packageselector"></span>**`brightport_crateguard_packageselector`** *(silent check: the first matching branch below is taken)*

    - Next *(if hand over 1× [Package](../items/brightportpackage.md))* → [brightport_crate_failure_arrest](#d-brightport_crate_failure_arrest)
    - Next → [brightport_crate_failure_arrest](#d-brightport_crate_failure_arrest)

    <span id="d-brightport_crateguard8"></span>**`brightport_crateguard8`** Brightport guard: “And we're supposed to believe that?”

    - Next → [brightport_crateguard9](#d-brightport_crateguard9)

    <span id="d-brightport_crateguard0"></span>**`brightport_crateguard0`** Brightport guard: “What's with that tone?! We came here on a simple patrol but I think we might have caught a spy. We should arrest him, right partner?”

    - “Think about it twice. You try and arrest me, and by tomorrow morning you might find yourself discharged, or on a…” → [brightport_crateguard_arrest_selector](#d-brightport_crateguard_arrest_selector)

    <span id="d-brightport_crateguard2"></span>**`brightport_crateguard2`** Brightport guard: “Ha, you're funny kid. And suspicious. Funny and suspicious. The commander himself ordered us to go on a patrol. So I think we've caught a troublemaker.”

    - “He might have ordered you to come here, but did he not tell you to keep your hands off Barthold and his friends? I…” → [brightport_crateguard_arrest2](#d-brightport_crateguard_arrest2)

    <span id="d-brightport_crateguard3"></span>**`brightport_crateguard3`** Brightport guard: “Wait, I think I know you. You're the kid who helped us with capturing those two criminals!”

    - Next → [brightport_crateguard4](#d-brightport_crateguard4)

    <span id="d-brightport_crate_failure_arrest"></span>**`brightport_crate_failure_arrest`** Brightport guard: “The guards grab you by your shoulders and restrain you. You try shaking them off, but you can't resist them. They put a blindfold over your eyes, and next thing you know, you're in a jail cell.” — **effects:** moves you to [brightport_jail](../maps/brightport_jail.md), sets stage 144 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-144), clears stage 158 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-158), removes monsters from brightport_abandoned, starts timer “brightport_jail”, sets stage 220 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-220)


    <span id="d-brightport_crateguard9"></span>**`brightport_crateguard9`** Brightport guard: “Calm down, our duty is to protect the citizens of this town. Maybe that cloaked figure was his brother.”

    - Next → [brightport_guardcrate10](#d-brightport_guardcrate10)

    <span id="d-brightport_crateguard_arrest_selector"></span>**`brightport_crateguard_arrest_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if random chance (5%))* → [brightport_crateguard_arrest](#d-brightport_crateguard_arrest)
    - Next *(if random chance (100%))* → [brightport_crateguard1](#d-brightport_crateguard1)

    <span id="d-brightport_crateguard_arrest2"></span>**`brightport_crateguard_arrest2`** *(silent check: the first matching branch below is taken)*

    - Next *(if random chance (5%))* → [brightport_crateguard_arrest3](#d-brightport_crateguard_arrest3)
    - Next *(if random chance (100%))* → [brightport_crateguard7](#d-brightport_crateguard7)

    <span id="d-brightport_crateguard4"></span>**`brightport_crateguard4`** Brightport guard: “I guess you were the one the lookout spotted, so there is nothing else suspicious here. Either way, you did some impressive work with those two, but you shouldn't be hanging out around here. It's dangerous.”

    - “Anything for the glory of Feygard.” → [brightport_crateguard5](#d-brightport_crateguard5)

    <span id="d-brightport_guardcrate10"></span>**`brightport_guardcrate10`** Brightport guard: “Hmph, fine. We'll ask you a few questions then. What would your brother be doing here?”

    - “We were playing hide and seek.” → [brightport_guardcrate11](#d-brightport_guardcrate11)
    - “I don't know, I've been looking everywhere I can.” → [brightport_guardcrate15](#d-brightport_guardcrate15)

    <span id="d-brightport_crateguard1"></span>**`brightport_crateguard1`** Brightport guard: “Alright, alright, no need to get worked up. I think I've heard your name mentioned by the captain, so we'll trust him with this.”

    - Next → [brightport_crateguard6](#d-brightport_crateguard6)

    <span id="d-brightport_crateguard7"></span>**`brightport_crateguard7`** Brightport guard: “Alright, got it. Never thought the commander would let someone suspicious like you run around, but we'll trust his judgment.”

    - Next → [brightport_crateguard6](#d-brightport_crateguard6)

    <span id="d-brightport_crateguard5"></span>**`brightport_crateguard5`** Brightport guard: “That's the spirit. We'll be heading back now, so follow behind us. Wouldn't want a future knight of Feygard getting hurt.”

    - “Sure, I'll be right behind you.” → [brightport_crateguard6](#d-brightport_crateguard6)

    <span id="d-brightport_guardcrate11"></span>**`brightport_guardcrate11`** Brightport guard: “Hide and seek. In an abandoned structure, ways from town?”

    - Next → [brightport_guardcrate12](#d-brightport_guardcrate12)

    <span id="d-brightport_guardcrate15"></span>**`brightport_guardcrate15`** Brightport guard: “You expect us to believe your brother's been the one wandering around this ruin?”

    - Next → [brightport_guardcrate16](#d-brightport_guardcrate16)

    <span id="d-brightport_crateguard6"></span>**`brightport_crateguard6`** [Dummy NPC](../monsters/none.md): “The two guards exchange a glance, then turn and leave the building.” — **effects:** removes monsters from brightport_abandoned, sets stage 144 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-144), clears stage 158 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-158), sets stage 35 of [Boxed in](../quests/brightport_thieves.md#stage-35)


    <span id="d-brightport_guardcrate12"></span>**`brightport_guardcrate12`** Brightport guard: “And I suppose your friends are hiding in the jail cell too, huh?”

    - Next → [brightport_guardcrate13](#d-brightport_guardcrate13)

    <span id="d-brightport_guardcrate16"></span>**`brightport_guardcrate16`** Brightport guard: “Sounds like an excuse to me. No one just wanders in here.”

    - Next → [brightport_guardcrate17](#d-brightport_guardcrate17)

    <span id="d-brightport_guardcrate13"></span>**`brightport_guardcrate13`** [Dummy NPC](../monsters/none.md): “The guards both laugh.”

    - Next → [brightport_guardcrate14](#d-brightport_guardcrate14)



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 26 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_guardcrate.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_guardcrate.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_guardcrate.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_guardcrate.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Monster ID | `brightport_guardcrate` |
    | Spawn group | `brightport_guardcrate` |
    | Loot table | – |
    | Conversation | `brightport_crateguard_selector` |
    | Faction | – |
    | Movement | wholeMap |
    | Icon | `monsters_ld1:94` |
    | Defined in | `res/raw/monsterlist_brightport.json` |

    Raw data:

    ```json
    {
     "id": "brightport_guardcrate",
     "name": "Brightport guard",
     "iconID": "monsters_ld1:94",
     "movementAggressionType": "wholeMap",
     "phraseID": "brightport_crateguard_selector"
    }
    ```


<small>Data from v0.8.18</small>
