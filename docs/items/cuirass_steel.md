---
description: "Steel cuirass is a ordinary plate mail in Andor's Trail (Use item cost +1, Re-equip cost +1, Attack chance -3, Block chance +18). How to get it: monster drops, shops."
---

# ![](../assets/icons/items/items_tometik3_1.png){ .sprite } Steel cuirass

*Ordinary plate mail.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_tometik3_1.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `cuirass_steel` |
| **Category** | Plate mail |
| **Slot** | body |
| **Proficiency** | [Heavy armor proficiency](../skills/armorProficiencyHeavy.md) |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Use item cost | +1 |
| Re-equip cost | +1 |
| Attack chance | -3 |
| Block chance | +18 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Contaminated miner's skeleton](../monsters/elm_miner3.md) | 0.4% | 1 | elm5f_1, elm5f_2, elm_4f_1 |
| [Prim guard skeleton](../monsters/elm_miner4.md) | 0.4% | 1 | elm5f_1, elm5f_2, elm_4f_1 |

### Sold by

- [Odirath](../monsters/stoutford_armorer.md) (Stoutford)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=cuirass_steel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=cuirass_steel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=cuirass_steel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=cuirass_steel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `cuirass_steel` |
    | Category ID | `plmail` |
    | Icon | `items_tometik3:1` |
    | Defined in | `res/raw/itemlist_stoutford_combined.json` |
    | Loot tables containing it | `shop_odirath`, `elm_miner2` |

    Raw data:

    ```json
    {
     "id": "cuirass_steel",
     "iconID": "items_tometik3:1",
     "name": "Steel cuirass",
     "displaytype": "ordinary",
     "category": "plmail",
     "equipEffect": {
      "increaseUseItemCost": 1,
      "increaseReequipCost": 1,
      "increaseAttackChance": -3,
      "increaseBlockChance": 18
     }
    }
    ```


<small>Data from v0.8.18</small>
