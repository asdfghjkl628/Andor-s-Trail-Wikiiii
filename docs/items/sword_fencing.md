---
description: "Fencing blade is a ordinary rapier in Andor's Trail (Attack damage 2 to 5, Attack cost +4, Attack chance +14, Block chance +5). How to get it: shops."
---

# ![](../assets/icons/items/items_weapons_13.png){ .sprite } Fencing blade

*Ordinary rapier.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_13.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `sword_fencing` |
| **Category** | Rapier |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [One-handed sword proficiency](../skills/weaponProficiency1hsword.md) |
| **Rarity** | Ordinary |
| **Base value** | 922 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 2 to 5 |
| Attack cost | +4 |
| Attack chance | +14 |
| Block chance | +5 |
| setNonWeaponDamageModifier | +93 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Vilegard smith](../monsters/vilegard_smith.md) (Vilegard)
- [Truric](../monsters/truric.md) (Brimhaven)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 14, "increaseA… → {"increaseAttackChance": 14, "increaseA… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_fencing.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_fencing.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_fencing.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=sword_fencing.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `sword_fencing` |
    | Category ID | `rapier` |
    | Icon | `items_weapons:13` |
    | Defined in | `res/raw/itemlist_v0610_1.json` |
    | Loot tables containing it | `shop_vg_smith`, `truric` |

    Raw data:

    ```json
    {
     "id": "sword_fencing",
     "iconID": "items_weapons:13",
     "name": "Fencing blade",
     "hasManualPrice": 0,
     "baseMarketCost": 922,
     "category": "rapier",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 2,
       "max": 5
      },
      "increaseAttackCost": 4,
      "increaseAttackChance": 14,
      "increaseBlockChance": 5,
      "setNonWeaponDamageModifier": 93
     }
    }
    ```


<small>Data from v0.8.18</small>
