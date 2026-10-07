---
description: "Curative potion against mushroom wounding is a ordinary potion in Andor's Trail. How to get it: quests and dialogue. Ask your potion maker about risks and side effects."
---

# ![](../assets/icons/items/items_consumables_62.png){ .sprite } Curative potion against mushroom wounding

*Ordinary potion.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_consumables_62.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `fungi_panic_cure` |
| **Category** | Potion |
| **Rarity** | Ordinary |
| **Base value** | 150 gold |
| **Introduced** | [v0.7.13](../versions/0.7.13.md) |

</div>

> Ask your potion maker about risks and side effects.

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | Food-poisoning (magnitude 22, 1 rounds, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Potion merchant](../monsters/potion_merchant.md) ([fallhaven_potions](../maps/fallhaven_potions.md)) during [Fungi panic](../quests/fungi_panic.md#stage-50) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Bogsten](../monsters/bogsten.md) ([bogsten1](../maps/bogsten1.md)) | [Fungi panic](../quests/fungi_panic.md#stage-52) | handed over (1×) | “Yes, I have got a potion for you.” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=fungi_panic_cure.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=fungi_panic_cure.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=fungi_panic_cure.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=fungi_panic_cure.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `fungi_panic_cure` |
    | Category ID | `pot` |
    | Icon | `items_consumables:62` |
    | Defined in | `res/raw/itemlist_fungi_panic.json` |
    | Loot tables containing it | – |

    Raw data:

    ```json
    {
     "id": "fungi_panic_cure",
     "iconID": "items_consumables:62",
     "name": "Curative potion against mushroom wounding",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 150,
     "category": "pot",
     "description": "Ask your potion maker about risks and side effects.",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "foodp",
        "magnitude": 22,
        "duration": 1,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
