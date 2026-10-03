# Combat tips

*Written for v0.8.18. The formulas behind these tips are on [Stats & Skills](../skills/index.md).*

???+ section "Read the monster's page before a hard fight"

    Every [monster page](../monsters/index.md) lists its attack chance, block chance, damage resistance, attack cost and class. Ten seconds of reading beats a trip back to the last resting spot. Three numbers decide most fights:

    - **Its block chance vs. your attack chance.** If you're not at least ~50 above it, expect to whiff. A lot.
    - **Its damage resistance vs. your damage.** If its damage resistance is close to your minimum damage, many of your hits will do roughly nothing.
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

    Going from a 50 gap to 100 buys about 28 points of hit chance. Going from 150 to 200 buys about 4. Once you're 100+ ahead of what you usually fight, more accuracy is mostly decoration, and damage or defense will do more for you.

???+ section "Armor punishes small hits"

    The target's damage resistance comes off **every** hit. Against 10 damage resistance, a weapon hitting for 8–12 does 0–2 per hit, while one hitting for 20–25 does 10–15. Against heavily armored enemies, bring your hardest-hitting weapon, even if it swings less often. A dagger build against a high-armor monster is a long, sad afternoon.

    It works the other way too: your own damage resistance ([Bark Skin](../skills/barkSkin.md), shields, armor) is at its best against monsters that pepper you with lots of small hits.

???+ section "Attacks per turn: look for breakpoints"

    Attacks per turn = max AP ÷ attack cost, **rounded down**. You start with 10 AP, and [Combat Speed](../skills/speed.md) adds up to 2 more:

    | Attack cost | 10 AP | 11 AP | 12 AP |
    |---|---|---|---|
    | 2 | 5 | 5 | 6 |
    | 3 | 3 | 3 | 4 |
    | 4 | 2 | 2 | 3 |
    | 5 | 2 | 2 | 2 |
    | 6 | 1 | 1 | 2 |

    So Combat Speed is either a massive upgrade or two wasted skill points, depending entirely on your weapon. With a 5-AP weapon, both levels give you exactly nothing.[^ap] The [Jewel of Fallhaven](../items/jewel_fallhaven.md) (attack cost −1, sold by the tailor in Fallhaven) works the same way: check whether it actually tips you over a breakpoint before handing over the gold.

    [^ap]: The leftover AP isn't completely useless, since you can spend it on moving or using items. But you didn't spend two skill points to walk around more.

???+ section "Crits need the right weapon and the right target"

    Critical skill does nothing unless your **weapon** gives a critical multiplier, so check the weapon's page first. Crit chance also has diminishing returns: 20 critical skill gives 15%, and you need 80 to reach 35%. And against ghosts, constructs and demons, crits simply don't happen, so a crit-focused hero should carry a plan B for those fights. ~~"Hit it harder" is not a plan B.~~
