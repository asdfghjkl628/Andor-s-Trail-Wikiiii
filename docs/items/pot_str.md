---
description: "Minor potion of strength is a ordinary potion in Andor's Trail. How to get it: quests and dialogue."
---

# ![](../assets/icons/items/items_tometik1_21.png){ .sprite } Minor potion of strength

*Ordinary potion.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_tometik1_21.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `pot_str` |
| **Category** | Potion |
| **Rarity** | Ordinary |
| **Base value** | 120 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| On self | [Strength](../conditions/str.md) (magnitude 1, 5 rounds) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Lodar](../monsters/lodar.md) ([Lodarhouse 1](../maps/lodarhouse1.md)) (100%)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Arghest](../monsters/arghest.md) ([Blackwater mountain 13](../maps/blackwater_mountain13.md)) | [Blackwater Mountain events (hidden flag)](../quests/bwm72_beginning.md#stage-22) | handed over (1×) | “Would you like this 'Minor potion of strength'?” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.2](../versions/0.7.2.md) | When used, condition on self: [Strength](../conditions/str.md) (magnitude 1, 5 rounds) → (magnitude 1, 5 rounds) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_str.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_str.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_str.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=pot_str.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `pot_str` |
    | Category ID | `pot` |
    | Icon | `items_tometik1:21` |
    | Defined in | `res/raw/itemlist_v070.json` |
    | Loot tables containing it | `lodar_pot_str`, `lodar_pot_str_x5`, `lodar_pot_str_x10` |

    Raw data:

    ```json
    {
     "id": "pot_str",
     "iconID": "items_tometik1:21",
     "name": "Minor potion of strength",
     "hasManualPrice": 1,
     "baseMarketCost": 120,
     "category": "pot",
     "useEffect": {
      "conditionsSource": [
       {
        "condition": "str",
        "magnitude": 1,
        "duration": 5,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
