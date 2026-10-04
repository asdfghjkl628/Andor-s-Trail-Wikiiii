# ![](../assets/icons/monsters/monsters_tometik8_46.png){ .sprite } Lord Erwyn

| Stat | Value |
|---|---|
| Class | undead |
| HP | 110 |
| Max AP | 10 |
| Attack cost | 5 |
| Move cost | 10 |
| Damage | 13 to 22 |
| Attack chance | 130 |
| Block chance | 80 |
| Damage resistance | 5 |
| Critical skill | 20 |
| Critical multiplier | 3.0 |

## On hit

- **Heal HP:** 3
- **On target:** Weak Poison (magnitude 2, 4 rounds, 40% chance)

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Lord Erwyn's ring](../items/erwyn_ring.md) | 100% | 1 |

## Found on

- [stoutford_castle0](../maps/stoutford_castle0.md)

## Quests

- [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md): stages 48, 148

??? quote "Dialogue (9 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-stoutford_castle_3"></span>**`stoutford_castle_3`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 148 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-148); reached stage 49 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-49))* → [stoutford_castle_3_2](#d-stoutford_castle_3_2)
    - branch 2 *(if reached stage 148 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-148))* → [stoutford_castle_3a](#d-stoutford_castle_3a)
    - branch 3 → [stoutford_castle_3_1](#d-stoutford_castle_3_1)

    <span id="d-stoutford_castle_3_2"></span>**`stoutford_castle_3_2`** [Lord Erwyn](../monsters/erwyn2.md): “Did you come to serve me? On your knees!”

    - “What would I gain from that?” → [stoutford_castle_3b](#d-stoutford_castle_3b)
    - “You are very rude and poorly educated. Maybe I should introduce myself? $playername is my name.” → [stoutford_castle_3c](#d-stoutford_castle_3c)
    - “I will serve you - my weapon. Attack!” → [stoutford_castle_5](#d-stoutford_castle_5)

    <span id="d-stoutford_castle_3a"></span>**`stoutford_castle_3a`** [Lord Erwyn](../monsters/erwyn.md): “Did you come to serve me? On your knees!”

    - “What would I gain from that?” → [stoutford_castle_3b](#d-stoutford_castle_3b)
    - “You are very rude and poorly educated. Maybe I should introduce myself? $playername is my name.” → [stoutford_castle_3c](#d-stoutford_castle_3c)
    - “I will serve you - my weapon. Attack!” → [stoutford_castle_5](#d-stoutford_castle_5)

    <span id="d-stoutford_castle_3_1"></span>**`stoutford_castle_3_1`** [Dummy NPC](../monsters/none.md): “You see a heavily armed and cloaked skeleton moving towards you. This must be Lord Erwyn himself.” — **effects:** sets stage 148 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-148)

    - Next → [stoutford_castle_3_1a](#d-stoutford_castle_3_1a)

    <span id="d-stoutford_castle_3b"></span>**`stoutford_castle_3b`** Lord Erwyn: “Gain? I am the one who gains!”

    - “No, that's not acceptable. Do you have anything better to offer?” → [stoutford_castle_4](#d-stoutford_castle_4)

    <span id="d-stoutford_castle_3c"></span>**`stoutford_castle_3c`** Lord Erwyn: “Your name does not matter. Are you going to kneel now?”

    - “No. The floor is not clean here.” → [stoutford_castle_4](#d-stoutford_castle_4)

    <span id="d-stoutford_castle_5"></span>**`stoutford_castle_5`** *(silent check: the first matching branch below is taken)* — **effects:** sets stage 48 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-48)

    - branch 1 → *fight starts*

    <span id="d-stoutford_castle_3_1a"></span>**`stoutford_castle_3_1a`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 49 of [stn_nondisplay (hidden flag)](../quests/stn_nondisplay.md#stage-49))* → [stoutford_castle_3_2](#d-stoutford_castle_3_2)
    - branch 2 → [stoutford_castle_3a](#d-stoutford_castle_3a)

    <span id="d-stoutford_castle_4"></span>**`stoutford_castle_4`** Lord Erwyn: “You shall die now mortal!”

    - “No, you are going to die once and for all!” → [stoutford_castle_5](#d-stoutford_castle_5)
    - “For the Shadow!” → [stoutford_castle_5](#d-stoutford_castle_5)



## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added<br>Dialogue: 9 lines added |
| [v0.7.4](../versions/0.7.4.md) | attackCost: 53 → 5; attackDamage: {"max": 7, "min": 5} → {"max": 22, "min": 13}; damageResistance added (5); hitEffect: {"conditionsTarget": [{"chance": "40", … → {"conditionsTarget": [{"chance": "40", … |
| [v0.7.8](../versions/0.7.8.md) | Dialogue: 1 line changed<br>· text: “Gain? I am the the one who gains!” → “Gain? I am the one who gains!” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=erwyn2.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `erwyn2` · Data from v0.8.18</small>
