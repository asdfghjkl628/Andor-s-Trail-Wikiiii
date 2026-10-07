---
description: "Giant hammer is a ordinary giant hammer in Andor's Trail (Attack damage 4 to 7, Attack cost +10, setNonWeaponDamageModifier +215, Attack chance +5). How to get it: shops."
---

# ![](../assets/icons/items/items_weapons_45.png){ .sprite } Giant hammer

*Ordinary giant hammer.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_45.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `hammer1` |
| **Category** | Giant hammer |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | [Blunt weapon proficiency](../skills/weaponProficiencyBlunt.md) |
| **Rarity** | Ordinary |
| **Base value** | 121 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 4 to 7 |
| Attack cost | +10 |
| setNonWeaponDamageModifier | +215 |
| Attack chance | +5 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Vilegard smith](../monsters/vilegard_smith.md) (Vilegard)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 5, "increaseAt… → {"increaseAttackChance": 5, "increaseAt… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hammer1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hammer1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hammer1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=hammer1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `hammer1` |
    | Category ID | `hammer2h` |
    | Icon | `items_weapons:45` |
    | Defined in | `res/raw/itemlist_weapons.json` |
    | Loot tables containing it | `shop_vg_smith` |

    Raw data:

    ```json
    {
     "id": "hammer1",
     "iconID": "items_weapons:45",
     "name": "Giant hammer",
     "baseMarketCost": 121,
     "category": "hammer2h",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 4,
       "max": 7
      },
      "increaseAttackCost": 10,
      "setNonWeaponDamageModifier": 215,
      "increaseAttackChance": 5
     }
    }
    ```


<small>Data from v0.8.18</small>
