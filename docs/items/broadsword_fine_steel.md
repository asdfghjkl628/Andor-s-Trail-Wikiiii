---
description: "Fine steel broadsword is a ordinary broadsword in Andor's Trail (Attack damage 4 to 11, Attack cost +6, Attack chance +20, setNonWeaponDamageModifier +145). How to get it: shops."
---

# ![](../assets/icons/items/items_weapons_6.png){ .sprite } Fine steel broadsword

*Ordinary broadsword.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_6.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `broadsword_fine_steel` |
| **Category** | Broadsword |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [One-handed sword proficiency](../skills/weaponProficiency1hsword.md) |
| **Rarity** | Ordinary |
| **Base value** | 1,206 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 4 to 11 |
| Attack cost | +6 |
| Attack chance | +20 |
| setNonWeaponDamageModifier | +145 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Siola](../monsters/siola.md)
- [Cornith](../monsters/stoutford_smith.md) (Stoutford)
- [Fiamma](../monsters/brightportsmith.md) (Brightport)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 20, "increaseA… → {"increaseAttackChance": 20, "increaseA… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=broadsword_fine_steel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=broadsword_fine_steel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=broadsword_fine_steel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=broadsword_fine_steel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `broadsword_fine_steel` |
    | Category ID | `bsword` |
    | Icon | `items_weapons:6` |
    | Defined in | `res/raw/itemlist_v0610_1.json` |
    | Loot tables containing it | `shop_siola`, `shop_cornith`, `fiamma_shop` |

    Raw data:

    ```json
    {
     "id": "broadsword_fine_steel",
     "iconID": "items_weapons:6",
     "name": "Fine steel broadsword",
     "hasManualPrice": 0,
     "baseMarketCost": 1206,
     "category": "bsword",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 4,
       "max": 11
      },
      "increaseAttackCost": 6,
      "increaseAttackChance": 20,
      "setNonWeaponDamageModifier": 145
     }
    }
    ```


<small>Data from v0.8.18</small>
