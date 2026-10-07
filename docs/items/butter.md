# ![](../assets/icons/items/items_misc_2_164.png){ .sprite } Butter

*Ordinary food.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_2_164.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `butter` |
| **Category** | Food |
| **Rarity** | Ordinary |
| **Base value** | 10 gold |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

## Statistics

### When used

| Stat | Value |
|---|---|
| Heal HP | 1 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Arlish](../monsters/arlish.md) (Brimhaven)

### Quest & dialogue rewards

- From [Androni](../monsters/brightport_chef.md) ([brightport_bakery1](../maps/brightport_bakery1.md)) during [brightport_nondisplay (hidden flag)](../quests/brightport_nondisplay.md#stage-188) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) | [A Feygard delicacy](../quests/feygard_delicacy.md#stage-7) | handed over (1×) | “Here, take them all.” |
| [Philippa](../monsters/village_philippa.md) ([wexlow_village_se_house](../maps/wexlow_village_se_house.md)) | – | must be carried (1×) | “(automatic)” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=butter.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=butter.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=butter.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=butter.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `butter` |
    | Category ID | `food` |
    | Icon | `items_misc_2:164` |
    | Defined in | `res/raw/itemlist_feygard_1.json` |
    | Loot tables containing it | `arlish` |

    Raw data:

    ```json
    {
     "id": "butter",
     "iconID": "items_misc_2:164",
     "name": "Butter",
     "displaytype": "ordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 10,
     "category": "food",
     "useEffect": {
      "increaseCurrentHP": {
       "min": 1,
       "max": 1
      }
     }
    }
    ```


<small>Data from v0.8.18</small>
