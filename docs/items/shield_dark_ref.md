# ![](../assets/icons/items/items_armours_3_24.png){ .sprite } Shield of dark reflections

*Extraordinary shield, metal (heavy).*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_armours_3_24.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `shield_dark_ref` |
| **Category** | Shield, metal (heavy) |
| **Slot** | shield |
| **Rarity** | Extraordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.11](../versions/0.8.11.md) |

</div>

> When you look into the polished surface, you see a terrifying reflection of yourself.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack chance | -3 |
| Block chance | +17 |
| Damage resistance | +1 |

### When hit

| Stat | Value |
|---|---|
| On target | Fear (magnitude 1, 4 rounds, 18% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

As of v0.8.18, nothing in the game data gives this item: no monster drops it, no shop sells it, no container holds it and no dialogue hands it out.


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.11](../versions/0.8.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shield_dark_ref.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shield_dark_ref.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shield_dark_ref.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=shield_dark_ref.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `shield_dark_ref` |
    | Category ID | `shld_mtl_hv` |
    | Icon | `items_armours_3:24` |
    | Defined in | `res/raw/itemlist_laeroth.json` |
    | Loot tables containing it | – |

    Raw data:

    ```json
    {
     "id": "shield_dark_ref",
     "iconID": "items_armours_3:24",
     "name": "Shield of dark reflections",
     "displaytype": "extraordinary",
     "category": "shld_mtl_hv",
     "description": "When you look into the polished surface, you see a terrifying reflection of yourself.",
     "equipEffect": {
      "increaseAttackChance": -3,
      "increaseBlockChance": 17,
      "increaseDamageResistance": 1
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "fear",
        "magnitude": 1,
        "duration": 4,
        "chance": "18"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
