---
description: "Valugha's gloves is a extraordinary gloves, cloth in Andor's Trail (Attack damage 0 to 1, Use item cost -1, Attack chance +12, Block chance +10). How to get it: monster drops."
---

# ![](../assets/icons/items/items_japozero_229.png){ .sprite } Valugha's gloves

*Extraordinary gloves, cloth.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_japozero_229.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `valugha_gloves` |
| **Category** | Gloves, cloth |
| **Slot** | hand |
| **Rarity** | Extraordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 0 to 1 |
| Use item cost | -1 |
| Attack chance | +12 |
| Block chance | +10 |
| Grants | Clumsiness () |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Kazaul statue](../monsters/dds_kazaul_statue.md) | 100% | 1 | Mt. Galmore |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=valugha_gloves.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=valugha_gloves.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=valugha_gloves.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=valugha_gloves.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `valugha_gloves` |
    | Category ID | `hnd_cloth` |
    | Icon | `items_japozero:229` |
    | Defined in | `res/raw/itemlist_mt_galmore2.json` |
    | Loot tables containing it | `dds_kazaul_statue_dl` |

    Raw data:

    ```json
    {
     "id": "valugha_gloves",
     "iconID": "items_japozero:229",
     "name": "Valugha's gloves",
     "displaytype": "extraordinary",
     "category": "hnd_cloth",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 0,
       "max": 1
      },
      "increaseUseItemCost": -1,
      "increaseAttackChance": 12,
      "increaseBlockChance": 10,
      "addedConditions": [
       {
        "condition": "clumsiness"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
