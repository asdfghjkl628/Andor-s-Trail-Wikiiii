---
description: "Potion of lightning attack is a extraordinary potion in Andor's Trail. How to get it: containers, quests and dialogue."
---

# ![](../assets/icons/items/items_consumables_64.png){ .sprite } Potion of lightning attack

*Extraordinary potion.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_consumables_64.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `pot_light_attack` |
| **Category** | Potion |
| **Rarity** | Extraordinary |
| **Base value** | 4,999 gold |
| **Introduced** | [v0.7.2](../versions/0.7.2.md) |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | [Lightning attack](../conditions/light_attack.md) (magnitude 1, 5 rounds) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Found in containers

- [witch_house_basement](../maps/witch_house_basement.md#container-0) (container 1, 100%)

### Quest & dialogue rewards

- From [Teksin](../monsters/teksin.md) ([waytolake11](../maps/waytolake11.md)) during [Placeholder for hidden quest stages 2 (not displayed) (hidden flag)](../quests/nondisplay_2.md#stage-150) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.2](../versions/0.7.2.md) | Added |
| [v0.8.8](../versions/0.8.8.md) | When used, condition on self: [Lightning attack](../conditions/light_attack.md) (magnitude 1, 2 rounds) → (magnitude 1, 5 rounds) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_light_attack.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_light_attack.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_light_attack.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_light_attack.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `pot_light_attack` |
    | Category ID | `pot` |
    | Icon | `items_consumables:64` |
    | Defined in | `res/raw/itemlist_trader_teksin.json` |
    | Loot tables containing it | `witch_basement_dl1` |

    Raw data:

    ```json
    {
     "id": "pot_light_attack",
     "iconID": "items_consumables:64",
     "name": "Potion of lightning attack",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 4999,
     "category": "pot",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "light_attack",
        "magnitude": 1,
        "duration": 5,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
