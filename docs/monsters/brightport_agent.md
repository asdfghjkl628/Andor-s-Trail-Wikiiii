# ![](../assets/icons/monsters/monsters_rltiles1_84.png){ .sprite } Nor agent

| Stat | Value |
|---|---|
| Class | ? |
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

- [brightport_abandoned](../maps/brightport_abandoned.md)
- [brightport_jail](../maps/brightport_jail.md)

## Quests

- [Boxed in](../quests/brightport_thieves.md): stages 20, 30, 32
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 141, 142, 143, 158, 208

??? quote "Dialogue (16 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_agent"></span>**`brightport_agent`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120); reached stage 30 of [Boxed in](../quests/brightport_thieves.md#stage-30))* → [brightport_agent6alt](#d-brightport_agent6alt)
    - Next *(if reached stage 30 of [Boxed in](../quests/brightport_thieves.md#stage-30); reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60))* → [brightport_agent6_alt](#d-brightport_agent6_alt)
    - Next *(if reached stage 30 of [Boxed in](../quests/brightport_thieves.md#stage-30); NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60))* → [brightport_agent6](#d-brightport_agent6)
    - Next *(if NOT 10 rounds passed since timer “Brightport_package”)* → [brightport_agent1](#d-brightport_agent1)
    - Next *(if 10 rounds passed since timer “Brightport_package”)* → [brightport_agent2](#d-brightport_agent2)

    <span id="d-brightport_agent6alt"></span>**`brightport_agent6alt`** [Nor agent](../monsters/brightport_agent.md): “That is my partner on the lookout, the signal means the guards are coming.” — **effects:** sets stage 30 of [Boxed in](../quests/brightport_thieves.md#stage-30)

    - “I'll be fine, I'm in good standing with the guards.” → [brightport_agent8](#d-brightport_agent8)

    <span id="d-brightport_agent6_alt"></span>**`brightport_agent6_alt`** [Nor agent](../monsters/brightport_agent.md): “That is my partner on the lookout, the signal means the guards are coming.” — **effects:** sets stage 30 of [Boxed in](../quests/brightport_thieves.md#stage-30)

    - “I have the captain under my thumb, they can't touch me.” → [brightport_agent8](#d-brightport_agent8)

    <span id="d-brightport_agent6"></span>**`brightport_agent6`** [Nor agent](../monsters/brightport_agent.md): “That is my partner on the lookout, the signal means the guards are coming.” — **effects:** sets stage 30 of [Boxed in](../quests/brightport_thieves.md#stage-30)

    - Next → [brightport_crate_selector](#d-brightport_crate_selector)

    <span id="d-brightport_agent1"></span>**`brightport_agent1`** Nor agent: “That was a quick arrival.” — **effects:** sets stage 20 of [Boxed in](../quests/brightport_thieves.md#stage-20)

    - “Do you have a package for me?” → [brightport_agent3](#d-brightport_agent3)

    <span id="d-brightport_agent2"></span>**`brightport_agent2`** Nor agent: “You took your time.” — **effects:** sets stage 20 of [Boxed in](../quests/brightport_thieves.md#stage-20)

    - “Do you have a package for me?” → [brightport_agent3](#d-brightport_agent3)

    <span id="d-brightport_agent8"></span>**`brightport_agent8`** Nor agent: “Then take the package and deliver it, I will escape through the chimney. Shadow be with you.” — **effects:** sets stage 32 of [Boxed in](../quests/brightport_thieves.md#stage-32), gives 1× [Package](../items/brightportpackage.md), removes monsters from brightport_abandoned, starts timer “brightporthide”


    <span id="d-brightport_crate_selector"></span>**`brightport_crate_selector`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (30%))* → [brightport_crate1](#d-brightport_crate1)
    - branch 2 *(if random chance (40%))* → [brightport_crate2](#d-brightport_crate2)
    - branch 3 *(if random chance (100%))* → [brightport_crate3](#d-brightport_crate3)

    <span id="d-brightport_agent3"></span>**`brightport_agent3`** Nor agent: “Package? I'm just a traveler taking refuge in this building, I don't know what you want.”

    - “Hey, you clearly were expecting me!” → [brightport_agent4](#d-brightport_agent4)
    - “If it's a code word I'm supposed to use, no one told me anything.” → [brightport_agent4](#d-brightport_agent4)

    <span id="d-brightport_crate1"></span>**`brightport_crate1`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 141 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-141)

    - Next → [brightport_agent7](#d-brightport_agent7)

    <span id="d-brightport_crate2"></span>**`brightport_crate2`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 142 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-142)

    - Next → [brightport_agent7](#d-brightport_agent7)

    <span id="d-brightport_crate3"></span>**`brightport_crate3`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 143 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-143)

    - Next → [brightport_agent7](#d-brightport_agent7)

    <span id="d-brightport_agent4"></span>**`brightport_agent4`** Nor agent: “I was testing you, here is the package.”

    - Next → [brightport_agent5](#d-brightport_agent5)

    <span id="d-brightport_agent7"></span>**`brightport_agent7`** Nor agent: “Take this package and hide somewhere before the guards get here, I will escape through the chimney. Shadow be with you.” — **effects:** sets stage 32 of [Boxed in](../quests/brightport_thieves.md#stage-32), gives 1× [Package](../items/brightportpackage.md), removes monsters from brightport_abandoned, starts timer “brightporthide”, sets stage 208 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-208)


    <span id="d-brightport_agent5"></span>**`brightport_agent5`** [Dummy NPC](../monsters/none.md): “As the courier is taking something out of his robe you hear a whistle.” — **effects:** sets stage 158 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-158)

    - Next → [brightport_agent6_selector](#d-brightport_agent6_selector)

    <span id="d-brightport_agent6_selector"></span>**`brightport_agent6_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120))* → [brightport_agent6alt](#d-brightport_agent6alt)
    - Next *(if NOT reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60); NOT reached stage 120 of [Priceful vengeance](../quests/brightport_goons.md#stage-120))* → [brightport_agent6](#d-brightport_agent6)
    - Next *(if reached stage 60 of [Priceful vengeance](../quests/brightport_goons.md#stage-60))* → [brightport_agent6_alt](#d-brightport_agent6_alt)



## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 16 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_agent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_agent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_agent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightport_agent.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brightport_agent` · Data from v0.8.18</small>
