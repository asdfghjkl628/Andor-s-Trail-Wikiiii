---
description: "Raw lamb meat is a ordinary food in Andor's Trail. How to get it: monster drops, shops."
---

# ![](../assets/icons/items/items_japozero_519.png){ .sprite } Raw lamb meat

*Ordinary food.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_japozero_519.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `lamb_meat_raw` |
| **Category** | Food |
| **Rarity** | Ordinary |
| **Base value** | 32 gold |
| **Introduced** | [v0.8.10](../versions/0.8.10.md) |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 5 |
| On self | [Sustenance](../conditions/food.md) (magnitude 2, 10 rounds); [Food-poisoning](../conditions/foodp.md) (magnitude 2, 12 rounds, 25% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Mountain Sheep](../monsters/bwm_sheep1.md) | 20% | 1 | Blackwater Mountain |

### Sold by

- [Tunlon](../monsters/tunlon.md) (Blackwater Mountain)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Gael](../monsters/gael.md) ([Mywild 20 houseright](../maps/mywild20_houseright.md)) | – | handed over (10×) | “Here, I have 10 nice pieces of lamb meat for you. Maybe not as good as snake tho” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.10](../versions/0.8.10.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=lamb_meat_raw.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=lamb_meat_raw.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=lamb_meat_raw.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=lamb_meat_raw.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `lamb_meat_raw` |
    | Category ID | `food` |
    | Icon | `items_japozero:519` |
    | Defined in | `res/raw/itemlist_bwmfill.json` |
    | Loot tables containing it | `tunlon`, `bwm_sheep` |

    Raw data:

    ```json
    {
     "id": "lamb_meat_raw",
     "iconID": "items_japozero:519",
     "name": "Raw lamb meat",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 32,
     "category": "food",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 5,
       "max": 5
      },
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 2,
        "duration": 10,
        "chance": "100"
       },
       {
        "condition": "foodp",
        "magnitude": 2,
        "duration": 12,
        "chance": "25"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
