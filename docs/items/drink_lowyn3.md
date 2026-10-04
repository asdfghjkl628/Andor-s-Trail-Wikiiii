# ![](../assets/icons/items/items_tometik1_12.png){ .sprite } Lowyna's rat poison

*Ordinary drink.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_tometik1_12.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `drink_lowyn3` |
| **Category** | Drink |
| **Rarity** | Ordinary |
| **Base value** | 170 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 5 to 10 |
| On self | Sustenance (magnitude 3, 20 rounds, 100% chance); Minor fatigue (magnitude 1, 5 rounds, 100% chance); Dazed (magnitude 1, 5 rounds, 100% chance); Weak Poison (magnitude 2, 10 rounds, 15% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Lowyna](../monsters/lowyna.md) (Fallhaven)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Two-teeth](../monsters/twoteeth.md) ([woodhouse1](../maps/woodhouse1.md)) | [Sweet sweet rat poison](../quests/lowyna.md#stage-40) | handed over (1×) | “Here, I got you some from Lowyna.” |
| [Two-teeth](../monsters/twoteeth.md) ([woodhouse1](../maps/woodhouse1.md)) | [Sweet sweet rat poison](../quests/lowyna.md#stage-40) | handed over (1×) | “Here, have some.” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | useEffect: {"conditionsSource": [{"chance": 100, "… → {"conditionsSource": [{"chance": "100",… |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=drink_lowyn3.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=drink_lowyn3.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=drink_lowyn3.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=drink_lowyn3.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `drink_lowyn3` |
    | Category ID | `drink` |
    | Icon | `items_tometik1:12` |
    | Defined in | `res/raw/itemlist_v070.json` |
    | Loot tables containing it | `shop_lowyna`, `drop_ratdom_kriih` |

    Raw data:

    ```json
    {
     "id": "drink_lowyn3",
     "iconID": "items_tometik1:12",
     "name": "Lowyna's rat poison",
     "hasManualPrice": 1,
     "baseMarketCost": 170,
     "category": "drink",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 5,
       "max": 10
      },
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 3,
        "duration": 20,
        "chance": "100"
       },
       {
        "condition": "fatigue_minor",
        "magnitude": 1,
        "duration": 5,
        "chance": "100"
       },
       {
        "condition": "dazed",
        "magnitude": 1,
        "duration": 5,
        "chance": "100"
       },
       {
        "condition": "poison_weak",
        "magnitude": 2,
        "duration": 10,
        "chance": "15"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
