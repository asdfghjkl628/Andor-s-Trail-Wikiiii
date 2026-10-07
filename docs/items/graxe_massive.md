---
description: "Massive greataxe is a ordinary greataxe in Andor's Trail (Attack damage 6 to 13, Attack cost +10, Attack chance +25, Block chance -6). How to get it: monster drops, shops."
---

# ![](../assets/icons/items/items_misc_5_41.png){ .sprite } Massive greataxe

*Ordinary greataxe.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_5_41.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `graxe_massive` |
| **Category** | Greataxe |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | [Axe proficiency](../skills/weaponProficiencyAxe.md) |
| **Rarity** | Ordinary |
| **Base value** | 1,548 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 6 to 13 |
| Attack cost | +10 |
| Attack chance | +25 |
| Block chance | -6 |
| Damage resistance | -1 |
| setNonWeaponDamageModifier | +202 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Gunfryk](../monsters/brightportguardcaptain.md) | 100% | 1 | Brightport |

### Sold by

- [Agthor](../monsters/agthor.md) (Fallhaven)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.10](../versions/0.7.10.md) | When equipped, non-weapon damage modifier (%): added (202) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=graxe_massive.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=graxe_massive.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=graxe_massive.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=graxe_massive.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `graxe_massive` |
    | Category ID | `axe2h` |
    | Icon | `items_misc_5:41` |
    | Defined in | `res/raw/itemlist_v070.json` |
    | Loot tables containing it | `shop_agthor`, `brightport_gunfryk` |

    Raw data:

    ```json
    {
     "id": "graxe_massive",
     "iconID": "items_misc_5:41",
     "name": "Massive greataxe",
     "baseMarketCost": 1548,
     "category": "axe2h",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 6,
       "max": 13
      },
      "increaseAttackCost": 10,
      "increaseAttackChance": 25,
      "increaseBlockChance": -6,
      "increaseDamageResistance": -1,
      "setNonWeaponDamageModifier": 202
     }
    }
    ```


<small>Data from v0.8.18</small>
