---
description: "Combat guidance for Andor's Trail v0.8.18: hit chance, damage resistance, attacks per turn breakpoints and critical hits."
---

# Combat

*Written for v0.8.18. The underlying formulas are described on [Stats & Skills](../skills/index.md).*

???+ section "Check the enemy's statistics before a difficult fight"

    Each page on [Monsters & NPCs](../monsters/index.md) lists the enemy's attack chance, block chance, damage resistance, attack cost and class. Three values determine the outcome of most fights:

    - **Its block chance compared with your attack chance.** Below a difference of about 50, many attacks will miss.
    - **Its damage resistance compared with your damage.** If its damage resistance is close to your minimum damage, many hits will deal little or no damage.
    - **Its class.** Ghosts, constructs and demons are immune to critical hits.

???+ section "Accuracy: aim for a difference of 50 to 100"

    Hit chance follows an S-shaped curve based on the difference between your attack chance and the target's block chance:

    | Difference | Hit chance |
    |---|---|
    | 0 | 21% |
    | 50 | 50% |
    | 100 | 78% |
    | 150 | 87% |
    | 200 | 91% |

    Increasing the difference from 50 to 100 adds about 28 percentage points of hit chance; increasing it from 150 to 200 adds about 4. Once you are 100 or more above the enemies you usually face, further accuracy has little effect, and damage or defense is the better investment.

???+ section "Damage resistance reduces small hits the most"

    The target's damage resistance is subtracted from **every** hit. Against 10 damage resistance, a weapon dealing 8–12 damage deals 0–2 per hit, while a weapon dealing 20–25 deals 10–15. Against heavily armored enemies, a weapon with high damage per hit is preferable even if it attacks less often.

    The same applies in reverse: your own damage resistance ([Bark Skin](../skills/barkSkin.md), shields and armor) is most effective against enemies that make many weak attacks.

???+ section "Attacks per turn: breakpoints"

    Attacks per turn = max AP ÷ attack cost, **rounded down**. Characters start with 10 AP, and [Combat Speed](../skills/speed.md) adds up to 2 more:

    | Attack cost | 10 AP | 11 AP | 12 AP |
    |---|---|---|---|
    | 2 | 5 | 5 | 6 |
    | 3 | 3 | 3 | 4 |
    | 4 | 2 | 2 | 3 |
    | 5 | 2 | 2 | 2 |
    | 6 | 1 | 1 | 2 |

    The value of Combat Speed therefore depends on your weapon. With a weapon that costs 5 AP per attack, neither level adds an attack (the remaining AP can still be used to move or use items). The [Jewel of Fallhaven](../items/jewel_fallhaven.md) (attack cost −1, sold by the tailor in Fallhaven) works the same way: it is worth buying only if it reaches a new breakpoint with your weapon.

???+ section "Critical hits"

    Critical skill has no effect without a critical multiplier, which comes from the **weapon** (shown on its page) or from [Way of the Monk](../skills/fightstyleUnarmedUnarmored.md) when fighting unarmed. Critical hit chance has diminishing returns: 20 critical skill gives 15%, and 80 is needed for 35%. Ghosts, constructs and demons cannot receive critical hits, so a character built around critical hits should have an alternative approach for those enemies.
