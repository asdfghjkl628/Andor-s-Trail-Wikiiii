# ![](../assets/icons/monsters/monsters_gisons_8.png){ .sprite } Undina Bogsten

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

- [mushroom_m2_4](../maps/mushroom_m2_4.md)

## Quests

- [Fungi Panic - non displayed (hidden flag)](../quests/fungi_panic_nondisplayed.md): stages 200

??? quote "Dialogue (17 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-bogsten_granny"></span>**`bogsten_granny`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if carry 1× [Gardener's gloves](../items/gardener_gloves.md))* → [bogsten_granny_94](#d-bogsten_granny_94)
    - branch 2 *(if reached stage 210 of [Fungi Panic - non displayed (hidden flag)](../quests/fungi_panic_nondisplayed.md#stage-210))* → [bogsten_granny_92](#d-bogsten_granny_92)
    - branch 3 *(if reached stage 200 of [Fungi Panic - non displayed (hidden flag)](../quests/fungi_panic_nondisplayed.md#stage-200))* → [bogsten_granny_90](#d-bogsten_granny_90)
    - branch 4 → [bogsten_granny_10](#d-bogsten_granny_10)

    <span id="d-bogsten_granny_94"></span>**`bogsten_granny_94`** Undina Bogsten: “So you've chosen my gardening gloves. A wise choice!”

    - Next → [bogsten_granny_96](#d-bogsten_granny_96)

    <span id="d-bogsten_granny_92"></span>**`bogsten_granny_92`** Undina Bogsten: “Ah, so you found your way downstairs. Smart child, it was a pleasure to meet you. Farewell!”


    <span id="d-bogsten_granny_90"></span>**`bogsten_granny_90`** Undina Bogsten: “It was a pleasure to meet you. Farewell, kid!”


    <span id="d-bogsten_granny_10"></span>**`bogsten_granny_10`** Undina Bogsten: “Bogsten, my dear great-grandchild! After all these years you come to visit me again!”

    - “Sorry, I am not of your family. I am $playername from Crossglen.” → [bogsten_granny_20](#d-bogsten_granny_20)

    <span id="d-bogsten_granny_96"></span>**`bogsten_granny_96`** Undina Bogsten: “There used to be also a family-owned cookbook. Unfortunately that has been lost. It contained valuable recipes - the mushroom soup in particular was a dream!”

    - Next → [bogsten_granny_90](#d-bogsten_granny_90)

    <span id="d-bogsten_granny_20"></span>**`bogsten_granny_20`** Undina Bogsten: “Really? My eyes don't seem to be as clear as they used to be.”

    - Next → [bogsten_granny_30](#d-bogsten_granny_30)

    <span id="d-bogsten_granny_30"></span>**`bogsten_granny_30`** Undina Bogsten: “Where is this naughty boy? He should have come for cleaning every week.”

    - “He is dead.” *(if killed 1× [Bogsten](../monsters/bogsten.md))* → [bogsten_granny_32](#d-bogsten_granny_32)
    - “I met him in the house upstairs. He was very ill.” *(if NOT killed 1× [Bogsten](../monsters/bogsten.md))* → [bogsten_granny_34](#d-bogsten_granny_34)
    - “I don't know.” → [bogsten_granny_40](#d-bogsten_granny_40)

    <span id="d-bogsten_granny_32"></span>**`bogsten_granny_32`** Undina Bogsten: “Death is not a reason to neglect one's duties!”

    - Next → [bogsten_granny_40](#d-bogsten_granny_40)

    <span id="d-bogsten_granny_34"></span>**`bogsten_granny_34`** Undina Bogsten: “Ill? You mean lazy and sleepy!”

    - Next → [bogsten_granny_40](#d-bogsten_granny_40)

    <span id="d-bogsten_granny_40"></span>**`bogsten_granny_40`** Undina Bogsten: “I never could stand that spoiled kid. He only ever comes to get new gold from the family treasure.”

    - “How ungrateful!” → [bogsten_granny_42](#d-bogsten_granny_42)

    <span id="d-bogsten_granny_42"></span>**`bogsten_granny_42`** Undina Bogsten: “Ungrateful indeed. I would rather give our gold to some random beggar than to see it squandered by him.”

    - Next → [bogsten_granny_50](#d-bogsten_granny_50)

    <span id="d-bogsten_granny_50"></span>**`bogsten_granny_50`** Undina Bogsten: “Tell me child, where are you going in the world?”

    - “My father sent me to find my brother Andor. He left some time ago and hasn't come back yet.” → [bogsten_granny_52](#d-bogsten_granny_52)

    <span id="d-bogsten_granny_52"></span>**`bogsten_granny_52`** Undina Bogsten: “It really is an honorable goal. I like you, my child. Truly.”

    - “Did you see my brother? He looks a bit like me.” → [bogsten_granny_54](#d-bogsten_granny_54)

    <span id="d-bogsten_granny_54"></span>**`bogsten_granny_54`** Undina Bogsten: “No, I haven't seen Andor. I hope that you will find him soon and that you can return to your father together.”

    - “My father will be very glad.” → [bogsten_granny_60](#d-bogsten_granny_60)

    <span id="d-bogsten_granny_60"></span>**`bogsten_granny_60`** Undina Bogsten: “How touching! I will give you something. You really deserve a little gold.”

    - “Oh, you don't have to!” → [bogsten_granny_80](#d-bogsten_granny_80)
    - “At last some gold.” → [bogsten_granny_80](#d-bogsten_granny_80)

    <span id="d-bogsten_granny_80"></span>**`bogsten_granny_80`** Undina Bogsten: “Go ye into our family tomb. You may pick something from our treasures.” — **effects:** sets stage 200 of [Fungi Panic - non displayed (hidden flag)](../quests/fungi_panic_nondisplayed.md#stage-200), removes monsters from mushroom_m2_4, spawns monsters on mushroom_m2_4




## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bogsten_granny.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bogsten_granny.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bogsten_granny.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=bogsten_granny.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `bogsten_granny` · Data from v0.8.18</small>
