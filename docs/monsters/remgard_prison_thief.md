# ![](../assets/icons/monsters/monsters_rogue1_0.png){ .sprite } Tember

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

- [remgard_prison](../maps/remgard_prison.md)

## Quests

- [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md): stages 139

??? quote "Dialogue (23 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-remgard_prison_thief"></span>**`remgard_prison_thief`** Tember: “Hi $playername. Got comfortable already?”

    - “What the ...” → [remgard_prison_thief_10](#d-remgard_prison_thief_10)

    <span id="d-remgard_prison_thief_10"></span>**`remgard_prison_thief_10`** Tember: “Don't look startled. You should have expected this from us thieves.”

    - Next → [remgard_prison_thief_12](#d-remgard_prison_thief_12)

    <span id="d-remgard_prison_thief_12"></span>**`remgard_prison_thief_12`** Tember: “Especially when you have carried such a lot of bonemeal potions with you.”

    - “Hey, what do you know about it?” → [remgard_prison_thief_14](#d-remgard_prison_thief_14)

    <span id="d-remgard_prison_thief_14"></span>**`remgard_prison_thief_14`** Tember: “We know everything.”

    - “Yeah, obviously.” → [remgard_prison_thief_20](#d-remgard_prison_thief_20)

    <span id="d-remgard_prison_thief_20"></span>**`remgard_prison_thief_20`** Tember: “We are thankful for your potions, and we are always grateful.”

    - Next → [remgard_prison_thief_22](#d-remgard_prison_thief_22)

    <span id="d-remgard_prison_thief_22"></span>**`remgard_prison_thief_22`** Tember: “So we offer you half of your stock. And your freedom. Deal?”

    - “Do I have a choice?” → [remgard_prison_thief_30](#d-remgard_prison_thief_30)
    - “OK.” → [remgard_prison_thief_50](#d-remgard_prison_thief_50)

    <span id="d-remgard_prison_thief_30"></span>**`remgard_prison_thief_30`** Tember: “Sure you do. You could get nothing and stay here to starve.”

    - “Ah no. Let's have the first offer.” → [remgard_prison_thief_50](#d-remgard_prison_thief_50)

    <span id="d-remgard_prison_thief_50"></span>**`remgard_prison_thief_50`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if NOT carry 1× [Bonemeal potion](../items/bonemeal_potion.md); NOT carry 1× [Lodar's bonemeal potion](../items/pot_bm_lodar.md))* → [remgard_prison_thief_52](#d-remgard_prison_thief_52)
    - branch 2 → [remgard_prison_thief_54](#d-remgard_prison_thief_54)

    <span id="d-remgard_prison_thief_52"></span>**`remgard_prison_thief_52`** Tember: “Here we go. I will count out loud, so you can check that I don't cheat.”

    - “[muttering] Cheat - with my own potions ...” → [remgard_prison_getback](#d-remgard_prison_getback)

    <span id="d-remgard_prison_thief_54"></span>**`remgard_prison_thief_54`** Tember: “You already have your share. You do not try to cheat, do you? In that case I would be very disappointed.”

    - “No, no. Everything is awful.” → [remgard_prison_thief_110](#d-remgard_prison_thief_110)

    <span id="d-remgard_prison_getback"></span>**`remgard_prison_getback`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if faction “feygard_patrol_bmp” ≥ 1000)* → [remgard_prison_getback_1000](#d-remgard_prison_getback_1000)
    - branch 2 *(if faction “feygard_patrol_bmp” ≥ 100)* → [remgard_prison_getback_100](#d-remgard_prison_getback_100)
    - branch 3 *(if faction “feygard_patrol_bmp” ≥ 10)* → [remgard_prison_getback_10](#d-remgard_prison_getback_10)
    - branch 4 *(if faction “feygard_patrol_bmp” ≥ 1)* → [remgard_prison_getback_1](#d-remgard_prison_getback_1)
    - branch 5 *(if faction “feygard_patrol_bmp2” ≥ 1000)* → [remgard_prison_getback2_1000](#d-remgard_prison_getback2_1000)
    - branch 6 *(if faction “feygard_patrol_bmp2” ≥ 100)* → [remgard_prison_getback2_100](#d-remgard_prison_getback2_100)
    - branch 7 *(if faction “feygard_patrol_bmp2” ≥ 10)* → [remgard_prison_getback2_10](#d-remgard_prison_getback2_10)
    - branch 8 *(if faction “feygard_patrol_bmp2” ≥ 1)* → [remgard_prison_getback2_1](#d-remgard_prison_getback2_1)
    - branch 9 → [remgard_prison_thief_100](#d-remgard_prison_thief_100)

    <span id="d-remgard_prison_thief_110"></span>**`remgard_prison_thief_110`** Tember: “Now it's all settled. We may leave now.”

    - “What? How can we leave?” → [remgard_prison_thief_112](#d-remgard_prison_thief_112)

    <span id="d-remgard_prison_getback_1000"></span>**`remgard_prison_getback_1000`** Tember: “1,000 bonemeal potions.” — **effects:** faction “feygard_patrol_bmp” -1000, gives 1000× [Bonemeal potion](../items/bonemeal_potion.md)

    - Next → [remgard_prison_getback](#d-remgard_prison_getback)

    <span id="d-remgard_prison_getback_100"></span>**`remgard_prison_getback_100`** Tember: “100 bonemeal potions.” — **effects:** faction “feygard_patrol_bmp” -100, gives 100× [Bonemeal potion](../items/bonemeal_potion.md)

    - Next → [remgard_prison_getback](#d-remgard_prison_getback)

    <span id="d-remgard_prison_getback_10"></span>**`remgard_prison_getback_10`** Tember: “10 bonemeal potions.” — **effects:** faction “feygard_patrol_bmp” -10, gives 10× [Bonemeal potion](../items/bonemeal_potion.md)

    - Next → [remgard_prison_getback](#d-remgard_prison_getback)

    <span id="d-remgard_prison_getback_1"></span>**`remgard_prison_getback_1`** Tember: “1 bonemeal potion.” — **effects:** faction “feygard_patrol_bmp” -1, gives 1× [Bonemeal potion](../items/bonemeal_potion.md)

    - Next → [remgard_prison_getback](#d-remgard_prison_getback)

    <span id="d-remgard_prison_getback2_1000"></span>**`remgard_prison_getback2_1000`** Tember: “1,000 exotic bonemeal potions.” — **effects:** faction “feygard_patrol_bmp2” -1000, gives 1000× [Lodar's bonemeal potion](../items/pot_bm_lodar.md)

    - Next → [remgard_prison_getback](#d-remgard_prison_getback)

    <span id="d-remgard_prison_getback2_100"></span>**`remgard_prison_getback2_100`** Tember: “100 exotic bonemeal potions.” — **effects:** faction “feygard_patrol_bmp2” -100, gives 100× [Lodar's bonemeal potion](../items/pot_bm_lodar.md)

    - Next → [remgard_prison_getback](#d-remgard_prison_getback)

    <span id="d-remgard_prison_getback2_10"></span>**`remgard_prison_getback2_10`** Tember: “10 exotic bonemeal potions.” — **effects:** faction “feygard_patrol_bmp2” -10, gives 10× [Lodar's bonemeal potion](../items/pot_bm_lodar.md)

    - Next → [remgard_prison_getback](#d-remgard_prison_getback)

    <span id="d-remgard_prison_getback2_1"></span>**`remgard_prison_getback2_1`** Tember: “1 exotic bonemeal potion.” — **effects:** faction “feygard_patrol_bmp2” -1, gives 1× [Lodar's bonemeal potion](../items/pot_bm_lodar.md)

    - Next → [remgard_prison_getback](#d-remgard_prison_getback)

    <span id="d-remgard_prison_thief_100"></span>**`remgard_prison_thief_100`** Tember: “Ha ha ha! That was fun, wasn't it?”

    - “Hmpf.” → [remgard_prison_thief_110](#d-remgard_prison_thief_110)

    <span id="d-remgard_prison_thief_112"></span>**`remgard_prison_thief_112`** Tember: “Oh, that is easy. Check the back wall - it is fake. We had it exchanged secretly, and those stupid guards haven't found out yet.” — **effects:** sets stage 139 of [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md#stage-139)

    - “Oh really?” → [remgard_prison_thief_200](#d-remgard_prison_thief_200)

    <span id="d-remgard_prison_thief_200"></span>**`remgard_prison_thief_200`** Tember: “Bye now. I will keep an eye on you.”

    - “Bye.” → *NPC leaves*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=remgard_prison_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=remgard_prison_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=remgard_prison_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=remgard_prison_thief.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `remgard_prison_thief` · Data from v0.8.18</small>
