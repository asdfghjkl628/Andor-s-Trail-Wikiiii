# Combat tips

*Written for v0.8.18. The formulas behind these tips are on [Stats & Skills](../skills/index.md).*

???+ section "Read the monster's page before a hard fight"

    Every [monster page](../monsters/index.md) lists its attack chance, block chance, damage resistance, attack cost and class. Three numbers decide most fights:

    - **Its block chance vs. your attack chance.** If your attack chance is less than about 50 above its block chance, you'll miss a lot.
    - **Its damage resistance vs. your damage.** If its damage resistance is close to your minimum damage, many of your hits do almost nothing.
    - **Its class.** Ghosts, constructs and demons are immune to critical hits.

???+ section "Accuracy: aim for a gap of 50–100"

    Hit chance follows an S-curve on the gap between your attack chance and the target's block chance:

    | Gap | Hit chance |
    |---|---|
    | 0 | 21% |
    | 50 | 50% |
    | 100 | 78% |
    | 150 | 87% |
    | 200 | 91% |

    Going from a 50 gap to 100 gains about 28 points of hit chance. Going from 150 to 200 gains about 4. Once you're 100 or more ahead of what you usually fight, extra accuracy is mostly wasted, and damage or defense will serve you better.

???+ section "Armor punishes small hits"

    The target's damage resistance is subtracted from **every** hit. Against a monster with 10 damage resistance, a weapon hitting for 8–12 does 0–2 per hit, while one hitting for 20–25 does 10–15. Against heavily armored enemies, switch to your hardest-hitting weapon, even if it attacks less often.

    The same works in reverse: your own damage resistance ([Bark Skin](../skills/barkSkin.md), shields, armor) is strongest against monsters that hit often for small amounts.

???+ section "Attacks per turn: look for breakpoints"

    Attacks per turn = max AP ÷ attack cost, **rounded down**. You start with 10 AP, and [Combat Speed](../skills/speed.md) adds up to 2 more:

    | Attack cost | 10 AP | 11 AP | 12 AP |
    |---|---|---|---|
    | 2 | 5 | 5 | 6 |
    | 3 | 3 | 3 | 4 |
    | 4 | 2 | 2 | 3 |
    | 5 | 2 | 2 | 2 |
    | 6 | 1 | 1 | 2 |

    Combat Speed is a huge upgrade with some weapons and useless with others. With a 5-AP weapon, both levels give you nothing. The [Jewel of Fallhaven](../items/jewel_fallhaven.md) (attack cost −1, sold by the tailor in Fallhaven) works the same way: check whether it pushes you over a breakpoint before buying it.

???+ section "Critical hits need the right weapon and target"

    Critical skill does nothing unless your **weapon** gives a critical multiplier, so check the weapon's page first. Crit chance also has diminishing returns (20 critical skill gives 15%, 80 gives 35%). Against ghosts, constructs and demons, crits never happen, so a crit-focused hero should carry a backup plan for those fights.
