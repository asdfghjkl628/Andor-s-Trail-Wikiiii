# ![](../assets/icons/items/items_consumables_41.png){ .sprite } Minor potion of speed

*Ordinary potion.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_consumables_41.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `pot_speed_1` |
| **Category** | Potion |
| **Rarity** | Ordinary |
| **Base value** | 261 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | Minor speed (magnitude 1, 5 rounds, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Young aulaeth](../monsters/young_aulaeth.md) | 5% | 1 | Blackwater Mountain |
| [Aulaeth](../monsters/aulaeth.md) | 5% | 1 | Blackwater Mountain |
| [Strong aulaeth](../monsters/strong_aulaeth.md) | 5% | 1 | Blackwater Mountain |

### Sold by

- [Samar](../monsters/samar.md) (Prim)

### Found in containers

- [wild16_cave](../maps/wild16_cave.md#container-1) (container 2, 5%), Flagstone Prison


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | useEffect: {"conditionsSource": [{"chance": 100, "… → {"conditionsSource": [{"chance": "100",… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_speed_1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_speed_1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_speed_1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_speed_1.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `pot_speed_1` |
    | Category ID | `pot` |
    | Icon | `items_consumables:41` |
    | Defined in | `res/raw/itemlist_v069.json` |
    | Loot tables containing it | `shop_samar`, `aulaeth`, `wild16_cave2` |

    Raw data:

    ```json
    {
     "id": "pot_speed_1",
     "iconID": "items_consumables:41",
     "name": "Minor potion of speed",
     "hasManualPrice": 1,
     "baseMarketCost": 261,
     "category": "pot",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "speed_minor",
        "magnitude": 1,
        "duration": 5,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
