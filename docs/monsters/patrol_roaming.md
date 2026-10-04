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

- [brimhaven4](../maps/brimhaven4.md)
- [crossroads](../maps/crossroads.md)
- [fields6](../maps/fields6.md)
- [remgard0](../maps/remgard0.md)
- [road1](../maps/road1.md)
- [roadbeforecrossroads2](../maps/roadbeforecrossroads2.md)
- [roadbeforecrossroads6](../maps/roadbeforecrossroads6.md)
- [wild6](../maps/wild6.md)

## Quests

- [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md): stages 141

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_patrol_roaming"></span>**`brv_patrol_roaming`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141))* → [brv_patrol_roaming_20](#d-brv_patrol_roaming_20)
    - branch 2 → [brv_patrol_roaming_10](#d-brv_patrol_roaming_10)

    <span id="d-brv_patrol_roaming_20"></span>**`brv_patrol_roaming_20`** Feygard soldier: “You again. You have to wait while I check your belongings.”

    - Next → [brv_patrol_roaming_11](#d-brv_patrol_roaming_11)

    <span id="d-brv_patrol_roaming_10"></span>**`brv_patrol_roaming_10`** Feygard soldier: “You are carrying a lot of gear. Any disallowed substances? You have to wait while I check your belongings.”

    - Next → [brv_patrol_roaming_11](#d-brv_patrol_roaming_11)

    <span id="d-brv_patrol_roaming_11"></span>**`brv_patrol_roaming_11`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT reached stage 142 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-142))* → [brv_patrol_roaming_100](#d-brv_patrol_roaming_100)
    - branch 2 → [brv_patrol_bonemeals_removed](#d-brv_patrol_bonemeals_removed)

    <span id="d-brv_patrol_roaming_100"></span>**`brv_patrol_roaming_100`** Feygard soldier: “Everything is OK. Stay clean.” — **effects:** sets stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141), clears stage 140 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map


    <span id="d-brv_patrol_bonemeals_removed"></span>**`brv_patrol_bonemeals_removed`** Feygard soldier: “What's this? Smells like Bonemeal! Bonemeal is illegal and forbidden by the law of Feygard. I will have to confiscate it. [He gives you back all your belongings but keeps the Bonemeals] Keep away from illegal stuff. Now go on your way.” — **effects:** sets stage 141 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-141), clears stage 140 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-140), removes monsters from the map

    - “Hey, what the ...?” *(if reached stage 40 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-40))* → [brv_patrol_bonemeals_removed_bur](#d-brv_patrol_bonemeals_removed_bur)
    - “Phew, at least they didn't find my iron reserve in the bonemeal box.” *(if reached stage 42 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-42))* → *conversation ends*
    - “Phew, at least they had let me go.” *(if NOT reached stage 40 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-40); NOT reached stage 42 of [bwmfill_nondisplay (hidden flag)](../quests/bwmfill_nondisplay.md#stage-42))* → *conversation ends*

    <span id="d-brv_patrol_bonemeals_removed_bur"></span>**`brv_patrol_bonemeals_removed_bur`** [Dummy NPC](../monsters/none.md): “One of the guards winks at you while putting the confiscated bonemeal potions back in your pouch.”

    - “???” → [brv_patrol_bonemeals_removed_bur_10](#d-brv_patrol_bonemeals_removed_bur_10)

    <span id="d-brv_patrol_bonemeals_removed_bur_10"></span>**`brv_patrol_bonemeals_removed_bur_10`** Feygard soldier: “You'll be speechless - the guard is Burhczyd in the uniform of the Feygard Guard!”

    - Next → [brv_patrol_bonemeals_removed_bur_20](#d-brv_patrol_bonemeals_removed_bur_20)

    <span id="d-brv_patrol_bonemeals_removed_bur_20"></span>**`brv_patrol_bonemeals_removed_bur_20`** Feygard soldier: “Before you react, the guards have moved on.”




## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=patrol_roaming.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=patrol_roaming.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=patrol_roaming.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=patrol_roaming.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `patrol_roaming` · Data from v0.8.18</small>
