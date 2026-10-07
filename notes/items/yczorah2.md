## Trivia

**v0.8.7 change.** In v0.8.7, released in September 2023, the Yczorah nucleus's max AP bonus was reduced from +2 to +1. No other statistic of the item changed.[^ycz1] [verified: v0.8.7 | game files]

The reduction matters more than its size suggests, because attacks per turn are max AP divided by attack cost, rounded down.[^ycz2] The nucleus has an attack cost of 7, so two attacks per turn need 14 AP. A character with the base 10 AP, [Combat Speed](../skills/speed.md) at level 2 and no other AP bonuses had exactly 14 AP with the nucleus before v0.8.7, and 13 AP afterwards, which is one attack per turn. [verified: v0.8.18 | game files]

[^ycz1]: Game data change in commit [5b63709](https://github.com/AndorsTrailRelease/andors-trail/commit/5b637099a1dc88cf6a3fabf3951c7ff765be27a8) ("Changes from next_release", 30 August 2023), `AndorsTrail/res/raw/itemlist_omi2.json`, first included in release [v0.8.7](https://github.com/AndorsTrailRelease/andors-trail/releases/tag/v0.8.7). See also [Version 0.8.7](../versions/0.8.7.md) on this wiki.
[^ycz2]: See [How combat works](../skills/index.md) and the [Combat](../strategy/combat.md) strategy page.
