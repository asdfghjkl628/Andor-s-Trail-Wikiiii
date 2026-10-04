# ![](../assets/icons/monsters/monsters_ld1_168.png){ .sprite } Grazia

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 3 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Found on

- [way_to_sullengard_east4_bridge](../maps/way_to_sullengard_east4_bridge.md)

## Quests

- [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md): stages 17, 18

??? quote "Dialogue (12 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-sull_ravine_grazia_0"></span>**`sull_ravine_grazia_0`** *(silent check: the first matching branch below is taken)*

    - Next *(if reached stage 18 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-18))* → *conversation ends*
    - Next *(if reached stage 29 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-29))* → [sull_ravine_grazia_60](#d-sull_ravine_grazia_60)
    - Next → [sull_ravine_grazia_1](#d-sull_ravine_grazia_1)

    <span id="d-sull_ravine_grazia_60"></span>**`sull_ravine_grazia_60`** [Grazia](../monsters/sull_ravine_grazia.md): “Thank you so much. I can now continue onto my destination.” — **effects:** sets stage 18 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-18), removes monsters from way_to_sullengard_east4, spawns monsters on sullengard2_northwest_house

    - “Where were you coming from anyway?” → [sull_ravine_grazia_70](#d-sull_ravine_grazia_70)

    <span id="d-sull_ravine_grazia_1"></span>**`sull_ravine_grazia_1`** Grazia: “Please, please, you have to help me! I tried to, but I am too scared.”

    - “Tried to do what?” → [sull_ravine_grazia_10](#d-sull_ravine_grazia_10)

    <span id="d-sull_ravine_grazia_70"></span>**`sull_ravine_grazia_70`** Grazia: “I have been traveling from Nor City to Sullengard to visit my aunt and uncle and to help them prepare for the Sullengard beer festival next month. I hope to see you soon.”

    - “Yeah, about seeing you soon. Where is Sullengard?” *(if NOT reached stage 19 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-19))* → [sull_ravine_grazia_80](#d-sull_ravine_grazia_80)
    - “I'm looking forward to it.” *(if reached stage 19 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-19))* → [sull_ravine_grazia_90](#d-sull_ravine_grazia_90)

    <span id="d-sull_ravine_grazia_10"></span>**`sull_ravine_grazia_10`** Grazia: “I tried to do what Hadena said, but I just can't do it.”

    - “Do what?!” → [sull_ravine_grazia_20](#d-sull_ravine_grazia_20)
    - “Who is Hadena?” *(if NOT reached stage 16 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-16))* → [sull_ravine_grazia_15](#d-sull_ravine_grazia_15)

    <span id="d-sull_ravine_grazia_80"></span>**`sull_ravine_grazia_80`** Grazia: “Oh, you've never been there? It is southwest of here.”

    - Next → [sull_ravine_grazia_90](#d-sull_ravine_grazia_90)

    <span id="d-sull_ravine_grazia_90"></span>**`sull_ravine_grazia_90`** Grazia: “I have to go now. See you there.” — **effects:** sets stage 18 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-18), removes monsters from way_to_sullengard_east4_bridge, spawns monsters on sullengard2_northwest_house


    <span id="d-sull_ravine_grazia_20"></span>**`sull_ravine_grazia_20`** Grazia: “To cross the bridge of course.”

    - “Why? It seems easy enough and from here, the bridge looks safe. What's the problem?” → [sull_ravine_grazia_30](#d-sull_ravine_grazia_30)

    <span id="d-sull_ravine_grazia_15"></span>**`sull_ravine_grazia_15`** Grazia: “Oh, she is a lady who lives in that cabin that you just walked past.”

    - “Oh, I see. Now what is it that you are trying to do?” → [sull_ravine_grazia_20](#d-sull_ravine_grazia_20)

    <span id="d-sull_ravine_grazia_30"></span>**`sull_ravine_grazia_30`** Grazia: “The wind! It is very scary when the entire bridge sways back and forth while you are crossing over it.”

    - “I'll tell you what, let's cross it together.” → [sull_ravine_grazia_40](#d-sull_ravine_grazia_40)

    <span id="d-sull_ravine_grazia_40"></span>**`sull_ravine_grazia_40`** Grazia: “How? It's not wide enough for both of us.”

    - “I will go first and you can follow close behind. Sound OK with you?” → [sull_ravine_grazia_50](#d-sull_ravine_grazia_50)

    <span id="d-sull_ravine_grazia_50"></span>**`sull_ravine_grazia_50`** Grazia: “Yes. Thank you.” — **effects:** sets stage 17 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-17)

    - “No problem. Let's go now.” → *conversation ends*



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sull_ravine_grazia.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sull_ravine_grazia.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sull_ravine_grazia.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=sull_ravine_grazia.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `sull_ravine_grazia` · Data from v0.8.18</small>
