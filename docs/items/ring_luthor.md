---
description: "Luthor's Ring is a quest ring in Andor's Trail (Grants Life drain (magnitude 5)). How to get it: quests and dialogue."
---

# ![](../assets/icons/items/items_jewelry_0.png){ .sprite } Luthor's Ring

*Quest ring.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_jewelry_0.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `ring_luthor` |
| **Category** | Ring |
| **Slot** | leftring |
| **Rarity** | Quest |
| **Base value** | 0 gold |
| **Quest item** | Yes |
| **Introduced** | [v0.8.13](../versions/0.8.13.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Grants | [Life drain](../conditions/life_drain.md) (magnitude 5) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Sly Seraphina](../monsters/tt_seraphina.md#v-tt_seraphina5) ([Crackshot hideout 4](../maps/crackshot_hideout4.md)) during [Troubling times](../quests/troubling_times.md#stage-270) (1×)
- From [Talion](../monsters/talion.md) during [Troubling times](../quests/troubling_times.md#stage-300) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Talion](../monsters/talion.md) | [Troubling times](../quests/troubling_times.md#stage-280) | handed over (1×) | “Here's all you have asked for.” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.13](../versions/0.8.13.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_luthor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_luthor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_luthor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_luthor.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `ring_luthor` |
    | Category ID | `ring` |
    | Icon | `items_jewelry:0` |
    | Defined in | `res/raw/itemlist_troubling_times.json` |
    | Loot tables containing it | – |

    Raw data:

    ```json
    {
     "id": "ring_luthor",
     "iconID": "items_jewelry:0",
     "name": "Luthor's Ring",
     "displaytype": "quest",
     "baseMarketCost": 0,
     "category": "ring",
     "equipEffect": {
      "addedConditions": [
       {
        "condition": "life_drain",
        "magnitude": 5
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
