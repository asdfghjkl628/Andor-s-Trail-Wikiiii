---
description: "Black greataxe is a ordinary greataxe in Andor's Trail (Attack damage 2 to 4, Attack cost +8, Attack chance +10, Block chance +8). How to get it: shops, containers."
---

# ![](../assets/icons/items/items_weapons_3_37.png){ .sprite } Black greataxe

*Ordinary greataxe.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_weapons_3_37.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `graxe_black` |
| **Category** | Greataxe |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | [Axe proficiency](../skills/weaponProficiencyAxe.md) |
| **Rarity** | Ordinary |
| **Base value** | 1 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 2 to 4 |
| Attack cost | +8 |
| Attack chance | +10 |
| Block chance | +8 |
| setNonWeaponDamageModifier | +191 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Hadracor](../monsters/hadracor.md) (Crossroads Guardhouse)

### Found in containers

- [galmore_64](../maps/galmore_64.md#container-0) (container 1, 100%), Mt. Galmore


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.10](../versions/0.7.10.md) | equipEffect: {"increaseAttackChance": 10, "increaseA… → {"increaseAttackChance": 10, "increaseA… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=graxe_black.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=graxe_black.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=graxe_black.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=graxe_black.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `graxe_black` |
    | Category ID | `axe2h` |
    | Icon | `items_weapons_3:37` |
    | Defined in | `res/raw/itemlist_v070.json` |
    | Loot tables containing it | `shop_hadracor`, `galmore64_dl` |

    Raw data:

    ```json
    {
     "id": "graxe_black",
     "iconID": "items_weapons_3:37",
     "name": "Black greataxe",
     "baseMarketCost": 1,
     "category": "axe2h",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 2,
       "max": 4
      },
      "increaseAttackCost": 8,
      "increaseAttackChance": 10,
      "increaseBlockChance": 8,
      "setNonWeaponDamageModifier": 191
     }
    }
    ```


<small>Data from v0.8.18</small>
