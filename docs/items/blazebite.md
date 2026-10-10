---
description: "Blazebite is a extraordinary shortsword in Andor's Trail (Attack damage 4 to 6, Attack cost +4, Attack chance +30, Block chance -10). How to get it: monster drops. A short sword wreathed in searing flames, scorching foes with each swift strike."
---

# ![](../assets/icons/items/items_weapons_78.png){ .sprite } Blazebite

*Extraordinary shortsword.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_weapons_78.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `blazebite` |
| **Category** | Shortsword |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Dagger proficiency](../skills/weaponProficiencyDagger.md) |
| **Rarity** | Extraordinary |
| **Base value** | 1,665 gold |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

> A short sword wreathed in searing flames, scorching foes with each swift strike.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 4 to 6 |
| Attack cost | +4 |
| Attack chance | +30 |
| Block chance | -10 |
| setNonWeaponDamageModifier | +97 |

### On hit

| Stat | Value |
|---|---|
| On target | [Ablaze](../conditions/fire.md) (magnitude 2, 4 rounds, 15% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Pyreling behemoth](../monsters/Pyreling_behemoth.md) | 100% | 1 | Galmore 71 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=blazebite.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=blazebite.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=blazebite.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=blazebite.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `blazebite` |
    | Category ID | `ssword` |
    | Icon | `items_weapons:78` |
    | Defined in | `res/raw/itemlist_mt_galmore2.json` |
    | Loot tables containing it | `Pyreling_behemoth_dl` |

    Raw data:

    ```json
    {
     "id": "blazebite",
     "iconID": "items_weapons:78",
     "name": "Blazebite",
     "displaytype": "extraordinary",
     "hasManualPrice": 0,
     "baseMarketCost": 1665,
     "category": "ssword",
     "description": "A short sword wreathed in searing flames, scorching foes with each swift strike.",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 4,
       "max": 6
      },
      "increaseAttackCost": 4,
      "increaseAttackChance": 30,
      "increaseBlockChance": -10,
      "setNonWeaponDamageModifier": 97
     },
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "fire",
        "magnitude": 2,
        "duration": 4,
        "chance": "15"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
