# ![](../assets/icons/items/items_consumables_51.png){ .sprite } Blackwater brew

*Ordinary potion.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_consumables_51.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `bwm_brew` |
| **Category** | Potion |
| **Rarity** | Ordinary |
| **Base value** | 57 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 15 |
| On self | Intoxicated (magnitude 1, 10 rounds, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Feygard scout](../monsters/ortholion_guard2.md) | 10% | 1-20 | Prim |
| [Strong gornaud](../monsters/strong_gornaud.md) | 5% | 10 | Blackwater Mountain |

### Sold by

- [Mazeg](../monsters/mazeg.md) (blackwater_mountain43)
- [Feygard scout](../monsters/ortholion_guard6.md) (Prim)

### Found in containers

- [blackwater_mountain74](../maps/blackwater_mountain74.md#container-0) (container 1, 100%)
- [elm_mine2](../maps/elm_mine2.md#container-0) (container 1, 50%)
- [elm_mine2](../maps/elm_mine2.md#container-2) (container 3, 66.6667%)


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

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_brew.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_brew.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_brew.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bwm_brew.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `bwm_brew` |
    | Category ID | `pot` |
    | Icon | `items_consumables:51` |
    | Defined in | `res/raw/itemlist_v069.json` |
    | Loot tables containing it | `shop_mazeg`, `gornaud_3`, `bwm74_drop1`, `ortholion_guard2`, `elm2_passage2`, `elm2_chest` |

    Raw data:

    ```json
    {
     "id": "bwm_brew",
     "iconID": "items_consumables:51",
     "name": "Blackwater brew",
     "hasManualPrice": 1,
     "baseMarketCost": 57,
     "category": "pot",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 15,
       "max": 15
      },
      "conditionsSource": [
       {
        "condition": "intoxicated",
        "magnitude": 1,
        "duration": 10,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
