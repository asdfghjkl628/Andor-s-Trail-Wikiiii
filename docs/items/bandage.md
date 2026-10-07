---
description: "Bandage is a quest healing item in Andor's Trail. How to get it: quests and dialogue."
---

# ![](../assets/icons/items/items_misc_53.png){ .sprite } Bandage

*Quest healing item.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_53.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `bandage` |
| **Category** | Healing item |
| **Rarity** | Quest |
| **Base value** | 256 gold |
| **Quest item** | Yes |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 12 to 24 |
| On self | Bleeding wound (magnitude -99, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Thoronir](../monsters/thoronir.md) ([fallhaven_church](../maps/fallhaven_church.md)) during [Thief apprentice](../quests/Thieves01.md#stage-50) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Fanamor](../monsters/fanamor.md) ([crossroads](../maps/crossroads.md)) | [Thief apprentice](../quests/Thieves01.md#stage-55) | handed over (1×) | “Yes, I have it!” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bandage.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bandage.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bandage.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bandage.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `bandage` |
    | Category ID | `healing` |
    | Icon | `items_misc:53` |
    | Defined in | `res/raw/itemlist_omicronrg9.json` |
    | Loot tables containing it | – |

    Raw data:

    ```json
    {
     "id": "bandage",
     "iconID": "items_misc:53",
     "name": "Bandage",
     "displaytype": "quest",
     "baseMarketCost": 256,
     "category": "healing",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 12,
       "max": 24
      },
      "conditionsSource": [
       {
        "condition": "bleeding_wound",
        "magnitude": -99,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
