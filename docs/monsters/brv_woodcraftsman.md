# ![](../assets/icons/monsters/monsters_tometik2_63.png){ .sprite } Wood craftsman

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

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Woodcutter's axe](../items/axe1.md) | 100% | 1 |
| [Woodcutter's hatchet](../items/woodcutter_hatchet.md) | 100% | 2 |
| [Wooden buckler](../items/shield1.md) | 100% | 5 |
| [Wooden shield](../items/shield_wooden.md) | 100% | 2 |
| [Woodcutter's gloves](../items/gloves_woodcutter.md) | 100% | 1 |
| [Woodcutter's boots](../items/woodcutter_boots.md) | 100% | 1 |

## Found on

- [brimhaven2_woodcutter](../maps/brimhaven2_woodcutter.md)

## Quests

- [It makes no fence](../quests/tunlon_fence.md): stages 220, 235, 240

??? quote "Dialogue (15 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brv_woodcraftsman_0"></span>**`brv_woodcraftsman_0`** Wood craftsman: “Hello, we sell the finest wood products and tools. Do you want to buy some?”

    - “Yes” → *shop opens*
    - “No, I just want to look around.” → [brv_woodcraftsman_2](#d-brv_woodcraftsman_2)
    - “I am looking for my brother, Andor. He looks a bit like me.” → [brv_woodcraftsman_1](#d-brv_woodcraftsman_1)
    - “Hello. The woodcutter in Loneford said that you can make me fences for a shepherd. Is that true?” *(if reached stage 210 of [It makes no fence](../quests/tunlon_fence.md#stage-210); NOT reached stage 220 of [It makes no fence](../quests/tunlon_fence.md#stage-220))* → [brv_woodcraftsman_fence1](#d-brv_woodcraftsman_fence1)
    - “Here is your wood.” *(if reached stage 230 of [It makes no fence](../quests/tunlon_fence.md#stage-230); hand over 1× [Pile of wood](../items/tunlon_wood.md); NOT reached stage 240 of [It makes no fence](../quests/tunlon_fence.md#stage-240))* → [brv_woodcraftsman_fence2](#d-brv_woodcraftsman_fence2)
    - “Ah, you are back.” *(if reached stage 235 of [It makes no fence](../quests/tunlon_fence.md#stage-235); NOT reached stage 240 of [It makes no fence](../quests/tunlon_fence.md#stage-240))* → [brv_woodcraftsman_fence3](#d-brv_woodcraftsman_fence3)

    <span id="d-brv_woodcraftsman_2"></span>**`brv_woodcraftsman_2`** Wood craftsman: “Take your time.”


    <span id="d-brv_woodcraftsman_1"></span>**`brv_woodcraftsman_1`** Wood craftsman: “I only know a goblin that looks like you. [Laughs]”


    <span id="d-brv_woodcraftsman_fence1"></span>**`brv_woodcraftsman_fence1`** Wood craftsman: “[laughing] Haha! Yes, that's my job.”

    - Next → [brv_woodcraftsman_fence1a](#d-brv_woodcraftsman_fence1a)

    <span id="d-brv_woodcraftsman_fence2"></span>**`brv_woodcraftsman_fence2`** Wood craftsman: “Perfect! Thank you for helping out, kid. Just wait a few minutes.” — **effects:** sets stage 235 of [It makes no fence](../quests/tunlon_fence.md#stage-235)

    - Next → [brv_woodcraftsman_fence3](#d-brv_woodcraftsman_fence3)

    <span id="d-brv_woodcraftsman_fence3"></span>**`brv_woodcraftsman_fence3`** Wood craftsman: “This is some good looking wood I must say. Very easy to process.”

    - Next → [brv_woodcraftsman_fence4](#d-brv_woodcraftsman_fence4)

    <span id="d-brv_woodcraftsman_fence1a"></span>**`brv_woodcraftsman_fence1a`** Wood craftsman: “But I'm afraid I haven't got enough wood right now. Please go back to Loneford's woodcutter. We have a deal that he supplies me with wood.” — **effects:** sets stage 220 of [It makes no fence](../quests/tunlon_fence.md#stage-220)

    - “Fine, I'm on my way.” → *conversation ends*

    <span id="d-brv_woodcraftsman_fence4"></span>**`brv_woodcraftsman_fence4`** Wood craftsman: “These posts will be standing for a long time. I guarantee you that.”

    - “Are you done soon?” → [brv_woodcraftsman_fence4a](#d-brv_woodcraftsman_fence4a)

    <span id="d-brv_woodcraftsman_fence4a"></span>**`brv_woodcraftsman_fence4a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if random chance (10%))* → [brv_woodcraftsman_fence5](#d-brv_woodcraftsman_fence5)
    - branch 2 *(if random chance (20%))* → [brv_woodcraftsman_fence4d](#d-brv_woodcraftsman_fence4d)
    - branch 3 *(if random chance (50%))* → [brv_woodcraftsman_fence4c](#d-brv_woodcraftsman_fence4c)
    - branch 4 → [brv_woodcraftsman_fence4b](#d-brv_woodcraftsman_fence4b)

    <span id="d-brv_woodcraftsman_fence5"></span>**`brv_woodcraftsman_fence5`** Wood craftsman: “Finished. That's 200 gold pieces. What do you say?”

    - “200 ... gold pieces - well, OK.” *(if pay 200 gold)* → [brv_woodcraftsman_fence6](#d-brv_woodcraftsman_fence6)
    - “That is too much!” → [brv_woodcraftsman_fence7](#d-brv_woodcraftsman_fence7)

    <span id="d-brv_woodcraftsman_fence4d"></span>**`brv_woodcraftsman_fence4d`** Wood craftsman: “[Swearing]”

    - Next → [brv_woodcraftsman_fence4a](#d-brv_woodcraftsman_fence4a)

    <span id="d-brv_woodcraftsman_fence4c"></span>**`brv_woodcraftsman_fence4c`** Wood craftsman: “[Hammering]”

    - Next → [brv_woodcraftsman_fence4a](#d-brv_woodcraftsman_fence4a)

    <span id="d-brv_woodcraftsman_fence4b"></span>**`brv_woodcraftsman_fence4b`** Wood craftsman: “[Sawing]”

    - Next → [brv_woodcraftsman_fence4a](#d-brv_woodcraftsman_fence4a)

    <span id="d-brv_woodcraftsman_fence6"></span>**`brv_woodcraftsman_fence6`** Wood craftsman: “Thank you. Bye!” — **effects:** sets stage 240 of [It makes no fence](../quests/tunlon_fence.md#stage-240), gives [New fence](../items/tunlon_fence2.md)


    <span id="d-brv_woodcraftsman_fence7"></span>**`brv_woodcraftsman_fence7`** Wood craftsman: “No gold - no fences.”

    - “Well ... OK.” *(if pay 200 gold)* → [brv_woodcraftsman_fence6](#d-brv_woodcraftsman_fence6)



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_woodcraftsman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_woodcraftsman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_woodcraftsman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brv_woodcraftsman.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brv_woodcraftsman` · Data from v0.8.18</small>
