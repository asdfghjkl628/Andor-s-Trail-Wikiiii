# ![](../assets/icons/monsters/monsters_ld1_98.png){ .sprite } Eatloni

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

- [brightport5](../maps/brightport5.md)

## Quests

- [Bread and circus](../quests/brightport_bakery.md): stages 25, 60, 65
- [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md): stages 157, 198, 213, 245

??? quote "Dialogue (18 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-brightport_storemaster_selector"></span>**`brightport_storemaster_selector`** *(silent check: the first matching branch below is taken)* — **effects:** clears stage 245 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-245)

    - Next *(if reached stage 25 of [Bread and circus](../quests/brightport_bakery.md#stage-25); NOT reached stage 198 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-198))* → [brightport_storemaster_apples](#d-brightport_storemaster_apples)
    - Next → [brightport_storemaster](#d-brightport_storemaster)

    <span id="d-brightport_storemaster_apples"></span>**`brightport_storemaster_apples`** Eatloni: “Have you learned what happened with the apple delivery?”

    - “I have the shipment from Deebo.” *(if reached stage 50 of [Bread and circus](../quests/brightport_bakery.md#stage-50))* → [brightport_storemaster6](#d-brightport_storemaster6)
    - “Apparantly the merchant picked them up.” *(if reached stage 30 of [Bread and circus](../quests/brightport_bakery.md#stage-30); NOT reached stage 50 of [Bread and circus](../quests/brightport_bakery.md#stage-50); NOT reached stage 40 of [Bread and circus](../quests/brightport_bakery.md#stage-40))* → [brightport_storemaster12](#d-brightport_storemaster12)
    - “I found the apples in a mountain cat nest. The poor merchant probably got eaten.” *(if reached stage 40 of [Bread and circus](../quests/brightport_bakery.md#stage-40); NOT reached stage 50 of [Bread and circus](../quests/brightport_bakery.md#stage-50))* → [brightport_storemaster9](#d-brightport_storemaster9)
    - “Not yet.” → *conversation ends*

    <span id="d-brightport_storemaster"></span>**`brightport_storemaster`** Eatloni: “Please keep off this path, you'll get under the feet of the workers.”

    - “What's up with all these crates outside?” → [brightport_storemaster2](#d-brightport_storemaster2)
    - “Allares sent me to help find the apple delivery.” *(if NOT reached stage 25 of [Bread and circus](../quests/brightport_bakery.md#stage-25); reached stage 23 of [Bread and circus](../quests/brightport_bakery.md#stage-23))* → [brightport_storemaster4](#d-brightport_storemaster4)
    - “Who are you?” → [brightport_eatloni_selector](#d-brightport_eatloni_selector)

    <span id="d-brightport_storemaster6"></span>**`brightport_storemaster6`** Eatloni: “Thank you, $playername, that's excellent. However, I haven't contacted the merchant's Guild for a reimbursement yet, so I can't repay you in full. I can only offer you half the price. Once you hand over the 30 apples.”

    - “Here you go. [Hand over the apples.]” *(if hand over 30× [Orchard apple](../items/deebo_apples.md))* → [brightport_storemaster7](#d-brightport_storemaster7)
    - “I think I might have eaten some.” *(if used 1× [Orchard apple](../items/deebo_apples.md); NOT carry 30× [Orchard apple](../items/deebo_apples.md))* → [brightport_storemaster8](#d-brightport_storemaster8)

    <span id="d-brightport_storemaster12"></span>**`brightport_storemaster12`** Eatloni: “So? He hasn't delivered them. If you went through the trouble of going there you could have at least obtained a new batch of 30 apples.”

    - “But you didn't tell me to...” → [brightport_storemaster13](#d-brightport_storemaster13)

    <span id="d-brightport_storemaster9"></span>**`brightport_storemaster9`** Eatloni: “The merchant arrived safe and sound shortly before you did. Well not quite, apparently he got robbed by highwaymen, and had to run for it with nothing but his cloak and a sack of 15 apples.”

    - “Coincidentally I found 15 apples myself.” *(if reached stage 197 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-197))* → [brightport_storemaster10](#d-brightport_storemaster10)

    <span id="d-brightport_storemaster2"></span>**`brightport_storemaster2`** Eatloni: “Our bakery bakes the finest bread in all of Dhayavar. There's bound to be a bit of a jumble getting it onto the rich folk's tables.”

    - “Is there any work for me to do here?” *(if NOT reached stage 1 of [Bread and circus](../quests/brightport_bakery.md#stage-1))* → [brightport_storemaster3](#d-brightport_storemaster3)
    - “Who are you?” → [brightport_eatloni_selector](#d-brightport_eatloni_selector)

    <span id="d-brightport_storemaster4"></span>**`brightport_storemaster4`** Eatloni: “Yes, it's unusual that it hasn't arrived. According to the contract, the merchant I hired will only get half pay for being late, that is if they even arrive.”

    - Next → [brightport_storemaster5](#d-brightport_storemaster5)

    <span id="d-brightport_eatloni_selector"></span>**`brightport_eatloni_selector`** *(silent check: the first matching branch below is taken)*

    - Next *(if NOT reached stage 245 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-245))* → [brightport_storemaster1](#d-brightport_storemaster1)
    - Next *(if reached stage 245 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-245))* → [brightport_eatloni](#d-brightport_eatloni)

    <span id="d-brightport_storemaster7"></span>**`brightport_storemaster7`** Eatloni: “Here you go, that's 700 gold, now go inside and tell my brother the apples will be coming soon, I just need to write them in my ledger.” — **effects:** sets stage 198 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-198), sets stage 60 of [Bread and circus](../quests/brightport_bakery.md#stage-60), gives 700× [Gold coins](../items/gold.md)


    <span id="d-brightport_storemaster8"></span>**`brightport_storemaster8`** Eatloni: “That's not good. I need all 30, if you don't have them then I can't repay you.”

    - “I'll be back.” → *conversation ends*

    <span id="d-brightport_storemaster13"></span>**`brightport_storemaster13`** Eatloni: “Use your brain, $playername.”


    <span id="d-brightport_storemaster10"></span>**`brightport_storemaster10`** Eatloni: “In total 30. That should be enough for the first round of baking. If you wouldn't mind giving them to me.”

    - “Here you go. [Hand over the apples.]” *(if hand over 15× [Orchard apple](../items/deebo_apples.md))* → [brightport_storemaster11](#d-brightport_storemaster11)
    - “I think I might have eaten some.” *(if NOT carry 15× [Orchard apple](../items/deebo_apples.md); used 1× [Orchard apple](../items/deebo_apples.md))* → [brightport_storemaster8](#d-brightport_storemaster8)

    <span id="d-brightport_storemaster3"></span>**`brightport_storemaster3`** Eatloni: “You're better off asking my brother Allares, you can find him in the bakery. Either way, they sure do make you youngsters work hard these days.” — **effects:** sets stage 157 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-157)


    <span id="d-brightport_storemaster5"></span>**`brightport_storemaster5`** Eatloni: “But it's not about the gold this time, we need them for an order and we can't be late ourselves. It would be nice if you could visit Deebo's Orchard south of the Duleian Road to see if the order of thirty apples has been picked up.” — **effects:** sets stage 25 of [Bread and circus](../quests/brightport_bakery.md#stage-25), sets stage 213 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-213)

    - “Sure, can do.” → *conversation ends*

    <span id="d-brightport_storemaster1"></span>**`brightport_storemaster1`** Eatloni: “I am Eatloni the storemaster. My brother Allares and I handle the storage and delivery of the bakery's goods.” — **effects:** sets stage 245 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-245)

    - “Is there any work for me to do here?” *(if NOT reached stage 1 of [Bread and circus](../quests/brightport_bakery.md#stage-1))* → [brightport_storemaster3](#d-brightport_storemaster3)
    - “That explains the mess.” → [brightport_storemaster2](#d-brightport_storemaster2)

    <span id="d-brightport_eatloni"></span>**`brightport_eatloni`** Eatloni: “Do you not have other things to occupy yourself with. Why must you bother me?”


    <span id="d-brightport_storemaster11"></span>**`brightport_storemaster11`** Eatloni: “Thank you $playername, that is excellent. Head inside and tell my brother the apples will be brought inside soon. As for your remuneration, he will reward you sufficiently.” — **effects:** sets stage 65 of [Bread and circus](../quests/brightport_bakery.md#stage-65), sets stage 198 of [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-198)




## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added<br>Dialogue: 18 lines added |
| [v0.8.18](../versions/0.8.18.md) | Dialogue: 1 line changed<br>· text: “But it's not about the gold this time, we need them for an order and …” → “But it's not about the gold this time, we need them for an order and …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakeryoutside.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakeryoutside.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakeryoutside.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=brightportbakeryoutside.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `brightportbakeryoutside` · Data from v0.8.18</small>
