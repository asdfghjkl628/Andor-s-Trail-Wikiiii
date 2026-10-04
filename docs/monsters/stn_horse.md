# ![](../assets/icons/monsters/monsters_ld2_66.png){ .sprite } Horse

| Stat | Value |
|---|---|
| Class | animal |
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

- [stoutford_castle_stable](../maps/stoutford_castle_stable.md)

## Quests

- [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md): stages 6

??? quote "Dialogue (6 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-stn_horse"></span>**`stn_horse`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 6 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-6))* → [stn_horse_90](#d-stn_horse_90)
    - branch 2 → [stn_horse_10](#d-stn_horse_10)

    <span id="d-stn_horse_90"></span>**`stn_horse_90`** Horse: “Neigh.”


    <span id="d-stn_horse_10"></span>**`stn_horse_10`** Horse: “Neigh!”

    - “Oh, nice to meet you.” → [stn_horse_12](#d-stn_horse_12)

    <span id="d-stn_horse_12"></span>**`stn_horse_12`** Horse: “Neigh!!!”

    - “One might think that you want something from me.” → [stn_horse_20](#d-stn_horse_20)
    - “Haha, I think I'm going crazy. Horses can't talk.” → *conversation ends*
    - “Neigh.” → [stn_horse_12](#d-stn_horse_12)

    <span id="d-stn_horse_20"></span>**`stn_horse_20`** Horse: “Neigh! Neigh!!! neigh.”

    - “Oh I see now. They left you here without anything to drink. Wait, Here is a bucket of water.” → [stn_horse_30](#d-stn_horse_30)
    - “You are becoming gradually more annoying. I'm leaving now.” → *conversation ends*

    <span id="d-stn_horse_30"></span>**`stn_horse_30`** Horse: “[After drinking greedily] Neiiieieiiigh!!” — **effects:** sets stage 6 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-6)

    - “There, now you feel better! I have to leave now.” → [stn_horse_90](#d-stn_horse_90)



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_horse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_horse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_horse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=stn_horse.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `stn_horse` · Data from v0.8.18</small>
