# ![](../assets/icons/monsters/monsters_rltiles1_20.png){ .sprite } Radiant guardian

| Stat | Value |
|---|---|
| Class | demon |
| HP | 320 |
| Max AP | 10 |
| Attack cost | 3 |
| Move cost | 5 |
| Damage | 2 to 7 |
| Attack chance | 80 |
| Block chance | 120 |
| Damage resistance | 4 |
| Critical skill | 40 |
| Critical multiplier | 2.0 |

!!! note "Immune to critical hits"
    Ghosts, constructs and demons can't be critically hit. Your crit build will have to sit this one out.

## On hit

- **Heal HP:** 5
- **On target:** Minor weapon feebleness (magnitude 2, 3 rounds, 20% chance)

## Drops

| Item | Chance | Qty |
|---|---|---|
| [Gold coins](../items/gold.md) | 100% | 0 to 20 |
| [Regular potion of health](../items/health.md) | 100% | 1 to 2 |
| [Sharpened gem](../items/gem4.md) | 100% | 1 |
| [Small rock](../items/rock.md) | 100% | 1 |

## Found on

- [waytobrimhavencave3a](../maps/waytobrimhavencave3a.md)

## Quests

- [An involuntary carrier](../quests/toszylae.md): stages 20, 21, 42, 45

??? quote "Dialogue (15 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-toszylae_guard"></span>**`toszylae_guard`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 45 of [An involuntary carrier](../quests/toszylae.md#stage-45))* → [toszylae_guard_8](#d-toszylae_guard_8)
    - branch 2 *(if reached stage 42 of [An involuntary carrier](../quests/toszylae.md#stage-42))* → [toszylae_guard_5](#d-toszylae_guard_5)
    - branch 3 → [toszylae_guard_1](#d-toszylae_guard_1)

    <span id="d-toszylae_guard_8"></span>**`toszylae_guard_8`** Radiant guardian: “[It raises its claw-like hands above its head, looking to get ready to strike at you]” — **effects:** sets stage 45 of [An involuntary carrier](../quests/toszylae.md#stage-45)

    - “[Attack]” → *fight starts*

    <span id="d-toszylae_guard_5"></span>**`toszylae_guard_5`** Radiant guardian: “[Its eyes pulsate in an intense glow as the creature starts moving towards you]”

    - Next → [toszylae_guard_6](#d-toszylae_guard_6)

    <span id="d-toszylae_guard_1"></span>**`toszylae_guard_1`** Radiant guardian: “[The horrifying creature looks down on you with its burning eyes, and speaks in a wheezing voice]”

    - Next → [toszylae_guard_s](#d-toszylae_guard_s)

    <span id="d-toszylae_guard_6"></span>**`toszylae_guard_6`** Radiant guardian: “[The guardian gives off a laughter that makes the hair on the back of your neck stand up]”

    - Next → [toszylae_guard_7](#d-toszylae_guard_7)

    <span id="d-toszylae_guard_s"></span>**`toszylae_guard_s`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 32 of [An involuntary carrier](../quests/toszylae.md#stage-32))* → [toszylae_guard_3_1](#d-toszylae_guard_3_1)
    - branch 2 *(if reached stage 15 of [An involuntary carrier](../quests/toszylae.md#stage-15))* → [toszylae_guard_2_1](#d-toszylae_guard_2_1)
    - branch 3 → [toszylae_guard_1_1](#d-toszylae_guard_1_1)

    <span id="d-toszylae_guard_7"></span>**`toszylae_guard_7`** Radiant guardian: “Kazaul'te vaarmun iktel urul.”

    - Next → [toszylae_guard_8](#d-toszylae_guard_8)

    <span id="d-toszylae_guard_3_1"></span>**`toszylae_guard_3_1`** Radiant guardian: “Kulauil hamar urum Kazaul'te. Kazaul hamat urul.”

    - “Klaatu varmun ur Kazaul'te” → [toszylae_guard_2_n](#d-toszylae_guard_2_n)
    - “Klaatu ur Kazaul'te” → [toszylae_guard_2_n](#d-toszylae_guard_2_n)
    - “Klatam ur turum Kazaul'te” → [toszylae_guard_4](#d-toszylae_guard_4)
    - “Klaatu ... verata ... n ... nick... [hide the rest in a well-timed cough].” → [toszylae_guard_2_n](#d-toszylae_guard_2_n)

    <span id="d-toszylae_guard_2_1"></span>**`toszylae_guard_2_1`** Radiant guardian: “Kulauil hamar urum Kazaul'te. Kazaul hamat urul.” — **effects:** sets stage 20 of [An involuntary carrier](../quests/toszylae.md#stage-20)

    - “This must be the phrase that Ulirfendor was looking for.” → [toszylae_guard_2_n](#d-toszylae_guard_2_n)

    <span id="d-toszylae_guard_1_1"></span>**`toszylae_guard_1_1`** Radiant guardian: “Kulauil hamar urum Kazaul'te. Kazaul hamat urul.”

    - “What?” → [toszylae_guard_1_n](#d-toszylae_guard_1_n)
    - “Kazaul something?” → [toszylae_guard_1_n](#d-toszylae_guard_1_n)

    <span id="d-toszylae_guard_2_n"></span>**`toszylae_guard_2_n`** Radiant guardian: “[The creature turns away]”

    - “[Attack]” → [toszylae_guard_2_n2](#d-toszylae_guard_2_n2)
    - “[Leave the creature]” → *conversation ends*

    <span id="d-toszylae_guard_4"></span>**`toszylae_guard_4`** Radiant guardian: “Kulum Kazaul.” — **effects:** sets stage 42 of [An involuntary carrier](../quests/toszylae.md#stage-42)

    - Next → [toszylae_guard_5](#d-toszylae_guard_5)

    <span id="d-toszylae_guard_1_n"></span>**`toszylae_guard_1_n`** Radiant guardian: “[The creature turns away]”

    - “[Attack]” → [toszylae_guard_1_n2](#d-toszylae_guard_1_n2)
    - “[Leave the creature]” → *conversation ends*

    <span id="d-toszylae_guard_2_n2"></span>**`toszylae_guard_2_n2`** Radiant guardian: “[As you try to make your attack against the guardian, your arms are held back by an enormous force]” — **effects:** sets stage 21 of [An involuntary carrier](../quests/toszylae.md#stage-21)


    <span id="d-toszylae_guard_1_n2"></span>**`toszylae_guard_1_n2`** Radiant guardian: “[As you try to make your attack against the guardian, your arms are held back by an enormous force]”




## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | hitEffect: {"conditionsTarget": [{"chance": 20, "c… → {"conditionsTarget": [{"chance": "20", …<br>Dialogue: 11 lines changed<br>· text: “(The guardian gives off a laughter that makes the hair on the back of…” → “[The guardian gives off a laughter that makes the hair on the back of…”<br>· text: “(The horrifying creature looks down on you with its burning eyes, and…” → “[The horrifying creature looks down on you with its burning eyes, and…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=toszylae_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=toszylae_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=toszylae_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=toszylae_guard.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `toszylae_guard` · Data from v0.8.18</small>
