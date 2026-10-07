---
description: "Nimael's vegetable soup is a rare food in Andor's Trail. How to get it: quests and dialogue. A delicious smelling soup, with a strong smell of potent herbs."
---

# ![](../assets/icons/items/items_tometik1_2.png){ .sprite } Nimael's vegetable soup

*Rare food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_tometik1_2.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `nimael_soup` |
| **Category** | Food |
| **Rarity** | Rare |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

> A delicious smelling soup, with a strong smell of potent herbs.

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | Sustenance (magnitude 3, 10 rounds, 100% chance); Regeneration (magnitude 1, 5 rounds, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Nimael](../monsters/nimael.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) during [Delicious soup](../quests/gison_soup.md#stage-110) (2×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Gael](../monsters/gael.md) ([mywild20_houseright](../maps/mywild20_houseright.md)) | – | must be carried (1×) | “(automatic)” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=nimael_soup.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=nimael_soup.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=nimael_soup.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=nimael_soup.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `nimael_soup` |
    | Category ID | `food` |
    | Icon | `items_tometik1:2` |
    | Defined in | `res/raw/itemlist_fungi_panic.json` |
    | Loot tables containing it | – |

    Raw data:

    ```json
    {
     "id": "nimael_soup",
     "iconID": "items_tometik1:2",
     "name": "Nimael's vegetable soup",
     "displaytype": "rare",
     "category": "food",
     "description": "A delicious smelling soup, with a strong smell of potent herbs.",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "food",
        "magnitude": 3,
        "duration": 10,
        "chance": "100"
       },
       {
        "condition": "regen2",
        "magnitude": 1,
        "duration": 5,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
