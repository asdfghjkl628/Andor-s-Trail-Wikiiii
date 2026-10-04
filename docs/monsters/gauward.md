# ![](../assets/icons/monsters/monsters_mage2_0.png){ .sprite } Gauward

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

- [waterwayhouse](../maps/waterwayhouse.md)

## Quests

- [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md): stages 20

??? quote "Dialogue (13 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-gauward"></span>**`gauward`** Gauward: “What... Oh, a visitor!”

    - “What is this place?” → [gauward_1](#d-gauward_1)
    - “I have some izthiel claws to sell you.” *(if reached stage 20 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-20))* → [gauward_sell_1](#d-gauward_sell_1)

    <span id="d-gauward_1"></span>**`gauward_1`** Gauward: “This place used to be a safe house for travelers between Loneford and Brimhaven, before they had finished the path between them.”

    - Next → [gauward_2](#d-gauward_2)

    <span id="d-gauward_sell_1"></span>**`gauward_sell_1`** Gauward: “Great. How many would you like to sell?”

    - “Here's one.” *(if hand over 1× [Izthiel claw](../items/izthiel_claw.md))* → [gauward_sold_1](#d-gauward_sold_1)
    - “Here's five.” *(if hand over 5× [Izthiel claw](../items/izthiel_claw.md))* → [gauward_sold_5](#d-gauward_sold_5)
    - “Here's ten.” *(if hand over 10× [Izthiel claw](../items/izthiel_claw.md))* → [gauward_sold_10](#d-gauward_sold_10)
    - “Here's twenty.” *(if hand over 20× [Izthiel claw](../items/izthiel_claw.md))* → [gauward_sold_20](#d-gauward_sold_20)
    - “Never mind. I will be back with more izthiel claws to sell you.” → [gauward_7](#d-gauward_7)

    <span id="d-gauward_2"></span>**`gauward_2`** Gauward: “However, nowadays, hardly anyone comes here - because of those cursed creatures from the river.”

    - Next → [gauward_3](#d-gauward_3)

    <span id="d-gauward_sold_1"></span>**`gauward_sold_1`** Gauward: “Good, thank you. Here's some gold for your troubles.” — **effects:** gives [Gold coins](../items/gold.md)


    <span id="d-gauward_sold_5"></span>**`gauward_sold_5`** Gauward: “Excellent, thank you! Here's some gold for your troubles.” — **effects:** gives [Gold coins](../items/gold.md)


    <span id="d-gauward_sold_10"></span>**`gauward_sold_10`** Gauward: “Excellent, thank you! Here's some gold for your troubles.” — **effects:** gives [Gold coins](../items/gold.md)


    <span id="d-gauward_sold_20"></span>**`gauward_sold_20`** Gauward: “Oh wow, you managed to get twenty of those claws? That's excellent, thank you! Here's some gold and some extra health potions for your troubles.” — **effects:** gives [Gold coins](../items/gold.md), [Regular potion of health](../items/health.md)


    <span id="d-gauward_7"></span>**`gauward_7`** Gauward: “Good. Please do. I like knowing that their numbers are reduced at least.” — **effects:** sets stage 20 of [Placeholder for hidden quest stages (not displayed) (hidden flag)](../quests/nondisplay.md#stage-20)


    <span id="d-gauward_3"></span>**`gauward_3`** Gauward: “Izthiel, they call them.”

    - Next → [gauward_4](#d-gauward_4)

    <span id="d-gauward_4"></span>**`gauward_4`** Gauward: “Ack, if it wasn't for those things out there, I am sure a lot of people would come by here more often.”

    - “Would you like me to kill the creatures for you?” → [gauward_5](#d-gauward_5)

    <span id="d-gauward_5"></span>**`gauward_5`** Gauward: “Oh sure. I have tried that. But they just keep coming back.”

    - Next → [gauward_6](#d-gauward_6)

    <span id="d-gauward_6"></span>**`gauward_6`** Gauward: “Tell you what though. Bring me those claws of theirs, and I'll buy them from you for a good price.”

    - “OK, I will return with some of their claws.” → [gauward_7](#d-gauward_7)



## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | Dialogue: 3 lines changed<br>· text: “What.. Oh, a visitor!” → “What... Oh, a visitor!” |
| [v0.7.4](../versions/0.7.4.md) | Dialogue: 1 line changed<br>· text: “This place used to be a safe house for travellers between Loneford an…” → “This place used to be a safe house for travelers between Loneford and…” |
| [v0.7.11](../versions/0.7.11.md) | Dialogue: 1 line changed<br>· text: “This place used to be a safe house for travelers between Loneford and…” → “This place used to be a safe house for travelers between Loneford and…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gauward.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gauward.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gauward.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=gauward.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `gauward` · Data from v0.8.18</small>
