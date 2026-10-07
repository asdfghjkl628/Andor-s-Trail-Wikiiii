---
description: "Iron spear is a ordinary pole weapon in Andor's Trail (Attack damage 2 to 3, Attack cost +6, Attack chance +8, Block chance +4). How to get it: shops."
---

# ![](../assets/icons/items/items_weapons_28.png){ .sprite } Iron spear

*Ordinary pole weapon.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_28.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `spear_iron` |
| **Category** | Pole weapon |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | [Pole weapon proficiency](../skills/weaponProficiencyPole.md) |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.12](../versions/0.7.12.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 2 to 3 |
| Attack cost | +6 |
| Attack chance | +8 |
| Block chance | +4 |
| setNonWeaponDamageModifier | +150 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Audir](../monsters/audir.md)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.12](../versions/0.7.12.md) | Added |
| [v0.7.13](../versions/0.7.13.md) | When equipped, attack chance: added (+8) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=spear_iron.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=spear_iron.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=spear_iron.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=spear_iron.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `spear_iron` |
    | Category ID | `pole` |
    | Icon | `items_weapons:28` |
    | Defined in | `res/raw/itemlist_brimhaven_2.json` |
    | Loot tables containing it | `shop_audir` |

    Raw data:

    ```json
    {
     "id": "spear_iron",
     "iconID": "items_weapons:28",
     "name": "Iron spear",
     "displaytype": "ordinary",
     "category": "pole",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 2,
       "max": 3
      },
      "increaseAttackCost": 6,
      "increaseAttackChance": 8,
      "increaseBlockChance": 4,
      "setNonWeaponDamageModifier": 150
     }
    }
    ```


<small>Data from v0.8.18</small>
