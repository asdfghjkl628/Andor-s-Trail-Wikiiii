# ![](../assets/icons/monsters/monsters_men_3.png){ .sprite } Feygard soldier

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 1 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [remgard0](../maps/remgard0.md)

## Quests

- [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md): stages 141

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_patrol2_roaming"></span>**`brv_patrol2_roaming`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141))* → [brv_patrol2_roaming_20](#d-brv_patrol2_roaming_20)
    - branch 2 → [brv_patrol2_roaming_10](#d-brv_patrol2_roaming_10)

    <span id="d-brv_patrol2_roaming_20"></span>**`brv_patrol2_roaming_20`** Feygard soldier: “You again. You have to wait while I check your belongings.”

    - Next → [brv_patrol2_roaming_11](#d-brv_patrol2_roaming_11)

    <span id="d-brv_patrol2_roaming_10"></span>**`brv_patrol2_roaming_10`** Feygard soldier: “You are carrying a lot of gear. Any disallowed substances? You have to wait while I check your belongings.”

    - Next → [brv_patrol2_roaming_11](#d-brv_patrol2_roaming_11)

    <span id="d-brv_patrol2_roaming_11"></span>**`brv_patrol2_roaming_11`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 142 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-142))* → [brv_patrol2_roaming_100](#d-brv_patrol2_roaming_100)
    - branch 2 → [brv_patrol2_bonemeals_removed](#d-brv_patrol2_bonemeals_removed)

    <span id="d-brv_patrol2_roaming_100"></span>**`brv_patrol2_roaming_100`** Feygard soldier: “Everything is OK. Stay clean.” — **effects:** sets stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141), clears stage 140 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map, removes monsters from the map


    <span id="d-brv_patrol2_bonemeals_removed"></span>**`brv_patrol2_bonemeals_removed`** Feygard soldier: “What's this? Smells like Bonemeal! Bonemeal is illegal and forbidden by the law of Feygard. I will have to confiscate it. [He gives you back all your belongings but keeps the Bonemeals] And we have to arrest you of course. Report to…” — **effects:** sets stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141), clears stage 140 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map, changes map remgard0, clears stage 138 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-138), clears stage 139 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-139), starts timer “remgard_prison”, removes monsters from remgard_prison




## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added<br>Dialogue: 6 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=patrol2_captain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=patrol2_captain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=patrol2_captain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=patrol2_captain.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `patrol2_captain` · Data from v0.8.18</small>
