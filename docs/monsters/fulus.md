# ![](../assets/icons/monsters/monsters_karvis2_3.png){ .sprite } Fulus

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

- [blackwater_mountain28](../maps/blackwater_mountain28.md)

## Quests

- [Awoken from slumber](../quests/bjorgur_grave.md): stages 20, 51, 60

??? quote "Dialogue (17 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-fulus_start"></span>**`fulus_start`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 60 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-60))* → [fulus_return_1](#d-fulus_return_1)
    - branch 2 *(if reached stage 51 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-51))* → [fulus_return_3](#d-fulus_return_3)
    - branch 3 *(if reached stage 40 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-40))* → [fulus_return_4](#d-fulus_return_4)
    - branch 4 *(if reached stage 20 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-20))* → [fulus_return_2](#d-fulus_return_2)
    - branch 5 → [fulus_1](#d-fulus_1)

    <span id="d-fulus_return_1"></span>**`fulus_return_1`** Fulus: “Hello again, friend. Thank you for your assistance in obtaining that dagger earlier.”


    <span id="d-fulus_return_3"></span>**`fulus_return_3`** Fulus: “What?! Sigh. Stupid kid. That dagger is worth a fortune. We could have been rich! Rich I tell you!” — **effects:** sets stage 51 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-51)


    <span id="d-fulus_return_4"></span>**`fulus_return_4`** Fulus: “Hello again. Have you been able to retrieve that dagger from Bjorgur's family grave yet?”

    - “I have already helped Bjorgur return the dagger to its original place.” → [fulus_return_3](#d-fulus_return_3)

    <span id="d-fulus_return_2"></span>**`fulus_return_2`** Fulus: “Hello again. Have you been able to retrieve that dagger from Bjorgur's family grave yet?”

    - “No, not yet.” → [fulus_9](#d-fulus_9)
    - “I decided to help Bjorgur instead.” *(if reached stage 40 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-40))* → [fulus_return_3](#d-fulus_return_3)
    - “What was I supposed to do again?” → [fulus_3](#d-fulus_3)
    - “Yes. Here it is.” *(if hand over 1× [Bjorgur's family dagger](../items/bjorgur_dagger.md))* → [fulus_complete_1](#d-fulus_complete_1)

    <span id="d-fulus_1"></span>**`fulus_1`** Fulus: “Hello there. You seem like just the type of person I am looking for.”

    - Next → [fulus_2](#d-fulus_2)

    <span id="d-fulus_9"></span>**`fulus_9`** Fulus: “Now hurry up. I really need that dagger soon.”


    <span id="d-fulus_3"></span>**`fulus_3`** Fulus: “For some time, I have known about a certain valuable dagger that a certain family used to possess here in Prim.”

    - Next → [fulus_4](#d-fulus_4)

    <span id="d-fulus_complete_1"></span>**`fulus_complete_1`** Fulus: “Oh wow, you actually managed to get the dagger? Thank you kid. This is worth a lot. Here, take these coins as compensation for your efforts!” — **effects:** sets stage 60 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-60), gives [Gold coins](../items/gold.md)

    - Next → [fulus_complete_2](#d-fulus_complete_2)

    <span id="d-fulus_2"></span>**`fulus_2`** Fulus: “Would you be interested in hearing about a business proposal I have?”

    - “Sure. What is the proposal?” → [fulus_3](#d-fulus_3)
    - “If it leads to something for me to gain, then sure.” → [fulus_3](#d-fulus_3)
    - “I couldn't possibly think you would have anything worthwhile to offer me, but let's hear it anyways.” → [fulus_3](#d-fulus_3)

    <span id="d-fulus_4"></span>**`fulus_4`** Fulus: “This dagger is extremely valuable to me, for personal reasons.”

    - “I don't like where this is going. I better not get involved in your shady business.” → [fulus_5](#d-fulus_5)
    - “I like where this is going, please continue.” → [fulus_6](#d-fulus_6)
    - “Tell me more.” → [fulus_6](#d-fulus_6)
    - “I have already helped Bjorgur return the dagger to its original place.” *(if reached stage 40 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-40))* → [fulus_return_3](#d-fulus_return_3)

    <span id="d-fulus_complete_2"></span>**`fulus_complete_2`** Fulus: “Thank you again. Now, let's see ... how much should we sell this dagger for?”


    <span id="d-fulus_5"></span>**`fulus_5`** Fulus: “Fine. Suit yourself, you goody two-shoes.”


    <span id="d-fulus_6"></span>**`fulus_6`** Fulus: “The family in question is Bjorgur's family.”

    - Next → [fulus_7](#d-fulus_7)

    <span id="d-fulus_7"></span>**`fulus_7`** Fulus: “Now, I happen to know that this particular dagger can be found in their family tomb that has been opened by other ... people ... recently.”

    - Next → [fulus_8](#d-fulus_8)

    <span id="d-fulus_8"></span>**`fulus_8`** Fulus: “What I want is simple. You go get that dagger and bring it to me, and I will reward you handsomely.”

    - “Sounds easy enough. I'll do it.” → [fulus_10](#d-fulus_10)
    - “No, I had better not get involved in your shady business.” → [fulus_5](#d-fulus_5)
    - “I have already helped Bjorgur return the dagger to its original place.” *(if reached stage 40 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-40))* → [fulus_return_3](#d-fulus_return_3)

    <span id="d-fulus_10"></span>**`fulus_10`** Fulus: “Good. Return to me once you have it. Maybe you can talk to Bjorgur about directions to the tomb. His house is just outside here in Prim. Just don't mention anything about our plan to him!” — **effects:** sets stage 20 of [Awoken from slumber](../quests/bjorgur_grave.md#stage-20)

    - Next → [fulus_9](#d-fulus_9)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 6 lines changed<br>· text: “Thank you again. Now, let's see.. how much should we sell this dagger…” → “Thank you again. Now, let's see ... how much should we sell this dagg…”<br>· text: “Now, I happen to know that this particular dagger can be found in the…” → “Now, I happen to know that this particular dagger can be found in the…” |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line added, 1 line changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fulus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fulus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fulus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=fulus.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `fulus` · Data from v0.8.18</small>
