---
description: "Combat guidance for Andor's Trail v0.8.18: hit chance, damage resistance, attacks per turn breakpoints and critical hits."
---

# Combat

*Written for v0.8.18. Formulas: [Stats & Skills](../skills/index.md). Abbreviations: [Glossary](../glossary.md).*

???+ section "Check the enemy before a hard fight"

    Every [enemy page](../monsters/index.md) lists AC, BC, DR, attack cost and class. Three things decide most fights:

    - **Its BC vs. your AC.** Less than ~50 ahead and you'll miss a lot.
    - **Its DR vs. your damage.** If its DR is near your minimum damage, many hits do ~nothing.
    - **Its class.** Ghosts, constructs and demons are immune to crits.

???+ section "Accuracy: aim for a gap of 50–100"

    Hit chance follows an S-curve on (your AC − its BC):

    | Gap | Hit chance |
    |---|---|
    | 0 | 21% |
    | 50 | 50% |
    | 100 | 78% |
    | 150 | 87% |
    | 200 | 91% |

    50 → 100 buys ~28 points of hit chance; 150 → 200 buys ~4. Past 100 ahead, spend on damage or defense instead.

???+ section "DR punishes small hits"

    DR comes off **every** hit. Against 10 DR, an 8–12 weapon does 0–2 per hit; a 20–25 weapon does 10–15. Bring your hardest hitter against armored enemies, even if it swings less often. ~~Daggers vs. a golem: a long, sad afternoon.~~

    Same goes for you: your own DR ([Bark Skin](../skills/barkSkin.md), shields, armor) shines against enemies that make lots of weak attacks.

???+ section "Attacks per turn: breakpoints"

    Attacks per turn = max AP ÷ attack cost, **rounded down**. You start with 10 AP; [Combat Speed](../skills/speed.md) adds up to 2:

    | Attack cost | 10 AP | 11 AP | 12 AP |
    |---|---|---|---|
    | 2 | 5 | 5 | 6 |
    | 3 | 3 | 3 | 4 |
    | 4 | 2 | 2 | 3 |
    | 5 | 2 | 2 | 2 |
    | 6 | 1 | 1 | 2 |

    So Combat Speed is either a big upgrade or two wasted skill points, depending on your weapon. With a 5-AP weapon, neither level adds an attack. The [Jewel of Fallhaven](../items/jewel_fallhaven.md) (attack cost −1, sold by the tailor in Fallhaven) works the same way: check the breakpoint before paying.

???+ section "Crits need the right weapon and the right target"

    No critical multiplier, no crits. The multiplier comes from your **weapon** or, unarmed, from [Way of the Monk](../skills/fightstyleUnarmedUnarmored.md). Diminishing returns too: 20 CS gives 15%, 80 CS gives 35%. Ghosts, constructs and demons can't be crit at all, so a crit build needs a plan B. ~~"Hit it harder" is not a plan B.~~
