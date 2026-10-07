---
description: "Yczorah nucleus is a legendary scepter in Andor's Trail (Attack damage 2 to 5, Max HP +12, Max AP +1, Move cost -1). How to get it: monster drops. The spherical, polished stone on its tip drags your glance unavoidably towards it."
---

# ![](../assets/icons/items/items_misc_6_1.png){ .sprite } Yczorah nucleus

*Legendary scepter.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_6_1.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `yczorah2` |
| **Category** | Scepter |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md) |
| **Rarity** | Legendary |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

> The spherical, polished stone on its tip drags your glance unavoidably towards it.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 2 to 5 |
| Max HP | +12 |
| Max AP | +1 |
| Move cost | -1 |
| Attack cost | +7 |
| Attack chance | +14 |
| Critical skill | +12 |
| Block chance | -3 |
| Damage resistance | -2 |
| Critical multiplier | 1.5 |
| setNonWeaponDamageModifier | +188 |

### On hit

| Stat | Value |
|---|---|
| On self | [Sustenance](../conditions/food.md) (magnitude 2, 2 rounds, 5% chance) |
| On target | [Bleeding wound](../conditions/bleeding_wound.md) (magnitude 2, 2 rounds, 10% chance) |

### When hit

| Stat | Value |
|---|---|
| Heal HP | 0 to 5 |
| On target | [Nausea](../conditions/nausea.md) (magnitude 4, 3 rounds, 20% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Yczorah marauder](../monsters/elm_yczorah1.md) | 0.01% | 1 | elm5f_1, elm5f_2 |
| [Yczorah](../monsters/elm_yzczorah2.md) | 0.01% | 1 | elm5f_1, elm5f_2 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |
| [v0.7.17](../versions/0.7.17.md) | Base value (gold): added (0)<br>Price now set manually instead of calculated from its statistics |
| [v0.8.7](../versions/0.8.7.md) | When equipped, max AP: +2 → +1 |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/edit/main/notes/items/yczorah2.md).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/edit/main/notes/items/yczorah2.md).*

### Trivia

**v0.8.7 change.** In v0.8.7, released in September 2023, the Yczorah nucleus's max AP bonus was reduced from +2 to +1. No other statistic of the item changed.[^ycz1] <span class="verified">Verified in v0.8.7 · Source: game files</span>

The reduction matters more than its size suggests, because attacks per turn are max AP divided by attack cost, rounded down.[^ycz2] The nucleus has an attack cost of 7, so two attacks per turn need 14 AP. A character with the base 10 AP, [Combat Speed](../skills/speed.md) at level 2 and no other AP bonuses had exactly 14 AP with the nucleus before v0.8.7, and 13 AP afterwards, which is one attack per turn. <span class="verified">Verified in v0.8.18 · Source: game files</span>

[^ycz1]: Game data change in commit [5b63709](https://github.com/AndorsTrailRelease/andors-trail/commit/5b637099a1dc88cf6a3fabf3951c7ff765be27a8) ("Changes from next_release", 30 August 2023), `AndorsTrail/res/raw/itemlist_omi2.json`, first included in release [v0.8.7](https://github.com/AndorsTrailRelease/andors-trail/releases/tag/v0.8.7). See also [Version 0.8.7](../versions/0.8.7.md) on this wiki.
[^ycz2]: See [How combat works](../skills/index.md) and the [Combat](../strategy/combat.md) strategy page.

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/edit/main/notes/items/yczorah2.md).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `yczorah2` |
    | Category ID | `scepter` |
    | Icon | `items_misc_6:1` |
    | Defined in | `res/raw/itemlist_omi2.json` |
    | Loot tables containing it | `elm_yczorah` |

    Raw data:

    ```json
    {
     "id": "yczorah2",
     "iconID": "items_misc_6:1",
     "name": "Yczorah nucleus",
     "displaytype": "legendary",
     "hasManualPrice": 1,
     "baseMarketCost": 0,
     "category": "scepter",
     "description": "The spherical, polished stone on its tip drags your glance unavoidably towards it.",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 2,
       "max": 5
      },
      "increaseMaxHP": 12,
      "increaseMaxAP": 1,
      "increaseMoveCost": -1,
      "increaseAttackCost": 7,
      "increaseAttackChance": 14,
      "increaseCriticalSkill": 12,
      "increaseBlockChance": -3,
      "increaseDamageResistance": -2,
      "setCriticalMultiplier": 1.5,
      "setNonWeaponDamageModifier": 188
     },
     "hitEffect": {
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 2,
        "duration": 2,
        "chance": "5"
       }
      ],
      "conditionsTarget": [
       {
        "condition": "bleeding_wound",
        "magnitude": 2,
        "duration": 2,
        "chance": "10"
       }
      ]
     },
     "hitReceivedEffect": {
      "increaseCurrentHP": {
       "min": 0,
       "max": 5
      },
      "conditionsTarget": [
       {
        "condition": "nausea",
        "magnitude": 4,
        "duration": 3,
        "chance": "20"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
