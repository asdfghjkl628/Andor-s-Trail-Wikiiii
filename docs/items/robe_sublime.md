---
description: "Robe of the Sublimate is a rare armor, cloth in Andor's Trail (Move cost -1, Use item cost -1, Re-equip cost +1, Attack chance +10). How to get it: shops. The reflection of light on this robe will confuse your enemies as you move swiftly."
---

# ![](../assets/icons/items/items_tometik2_37.png){ .sprite } Robe of the Sublimate

*Rare armor, cloth.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_tometik2_37.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `robe_sublime` |
| **Category** | Armor, cloth |
| **Slot** | body |
| **Rarity** | Rare |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

> The reflection of light on this robe will confuse your enemies as you move swiftly.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Move cost | -1 |
| Use item cost | -1 |
| Re-equip cost | +1 |
| Attack chance | +10 |
| Critical skill | +10 |
| Block chance | -5 |

### On hit

| Stat | Value |
|---|---|
| On target | [Confusion](../conditions/confusion.md) (magnitude 1, 2 rounds, 20% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Kayla](../monsters/kayla.md) (Stoutford)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=robe_sublime.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=robe_sublime.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=robe_sublime.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=robe_sublime.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `robe_sublime` |
    | Category ID | `bdy_clth` |
    | Icon | `items_tometik2:37` |
    | Defined in | `res/raw/itemlist_stoutford.json` |
    | Loot tables containing it | `kayla_shop`, `shop_kayla` |

    Raw data:

    ```json
    {
     "id": "robe_sublime",
     "iconID": "items_tometik2:37",
     "name": "Robe of the Sublimate",
     "displaytype": "rare",
     "category": "bdy_clth",
     "description": "The reflection of light on this robe will confuse your enemies as you move swiftly.",
     "equipEffect": {
      "increaseMoveCost": -1,
      "increaseUseItemCost": -1,
      "increaseReequipCost": 1,
      "increaseAttackChance": 10,
      "increaseCriticalSkill": 10,
      "increaseBlockChance": -5
     },
     "hitEffect": {
      "conditionsTarget": [
       {
        "condition": "confusion",
        "magnitude": 1,
        "duration": 2,
        "chance": "20"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
