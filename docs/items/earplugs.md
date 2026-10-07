---
description: "Earplugs is a quest other in Andor's Trail. How to get it: shops, quests and dialogue."
---

# ![](../assets/icons/items/items_misc_2_128.png){ .sprite } Earplugs

*Quest other.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_misc_2_128.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `earplugs` |
| **Category** | Other |
| **Rarity** | Quest |
| **Base value** | 100 gold |
| **Quest item** | Yes |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## How to get it

### Sold by

- [Leofric](../monsters/leofric.md#v-leofric_remgard) (Remgard)

### Quest & dialogue rewards

- From [Thyrope Splathershed](../monsters/ll2_mapmaker.md) ([remgard_tavern0](../maps/remgard_tavern0.md)) (4×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Thyrope Splathershed](../monsters/ll2_mapmaker.md) ([remgard_tavern0](../maps/remgard_tavern0.md)) | – | must be carried (4×) | “I have earplugs now.” |
| walking into a blocked passage on [mountainlake21](../maps/mountainlake21.md) | [Lake Laeroth nondisplay (hidden flag)](../quests/ll2_nd.md#stage-100) | handed over (4×) | “Look, I have earplugs here, take them and you can drive through here as often as” |
| walking into a blocked passage on [mountainlake21](../maps/mountainlake21.md) | – | must be carried (1×) | “Look, I have earplugs here, take them and you can drive through here as often as” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=earplugs.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=earplugs.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=earplugs.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=earplugs.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `earplugs` |
    | Category ID | `other` |
    | Icon | `items_misc_2:128` |
    | Defined in | `res/raw/itemlist_lake_laeroth_2.json` |
    | Loot tables containing it | `leofric_remgard` |

    Raw data:

    ```json
    {
     "id": "earplugs",
     "iconID": "items_misc_2:128",
     "name": "Earplugs",
     "displaytype": "quest",
     "hasManualPrice": 1,
     "baseMarketCost": 100,
     "category": "other"
    }
    ```


<small>Data from v0.8.18</small>
