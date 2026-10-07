# ![](../assets/icons/items/items_consumables_16.png){ .sprite } Green Pepper

*Ordinary food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_consumables_16.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `green_pepper` |
| **Category** | Food |
| **Rarity** | Ordinary |
| **Base value** | 16 gold |
| **Introduced** | [v0.8.10](../versions/0.8.10.md) |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 1 to 2 |
| On self | Sustenance (magnitude 3, 4 rounds, 100% chance); Thirst (magnitude 1, 5 rounds, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Tunlon](../monsters/tunlon2.md) | 70% | 1-2 | Blackwater Mountain |

### Sold by

- [Tunlon](../monsters/tunlon.md) (Blackwater Mountain)

### Found in containers

- [bwmfill2](../maps/bwmfill2.md#container-0) (container 1, 100%), Blackwater Mountain


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Crescenzio](../monsters/brightport_chef2.md) ([brightport_bakery1](../maps/brightport_bakery1.md)) | [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-189) | handed over (1×) | “Here's 1 green pepper and rice.” |
| [Crescenzio](../monsters/brightport_chef2.md) ([brightport_bakery1](../maps/brightport_bakery1.md)) | [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-189) | handed over (5×) | “Here are 5 green peppers and rice.” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.10](../versions/0.8.10.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=green_pepper.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=green_pepper.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=green_pepper.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=green_pepper.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `green_pepper` |
    | Category ID | `food` |
    | Icon | `items_consumables:16` |
    | Defined in | `res/raw/itemlist_bwmfill.json` |
    | Loot tables containing it | `bwmfill2_container`, `tunlon`, `tunlon2` |

    Raw data:

    ```json
    {
     "id": "green_pepper",
     "iconID": "items_consumables:16",
     "name": "Green Pepper",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 16,
     "category": "food",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 2
      },
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 3,
        "duration": 4,
        "chance": "100"
       },
       {
        "condition": "thirst",
        "magnitude": 1,
        "duration": 5,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
