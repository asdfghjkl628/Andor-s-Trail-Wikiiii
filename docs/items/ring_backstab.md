---
description: "Ring of backstabbing is a ordinary ring in Andor's Trail (Attack chance +17, Critical skill +7, Block chance +3). How to get it: shops."
---

# ![](../assets/icons/items/items_jewelry_2.png){ .sprite } Ring of backstabbing

*Ordinary ring.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_jewelry_2.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `ring_backstab` |
| **Category** | Ring |
| **Slot** | leftring |
| **Rarity** | Ordinary |
| **Base value** | 1,363 gold |
| **Introduced** | v0.7.0 or earlier |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack chance | +17 |
| Critical skill | +7 |
| Block chance | +3 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Dunla](../monsters/dunla.md) (Vilegard)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Nanath](../monsters/nanath.md) ([Fallhaven derelict 2](../maps/fallhaven_derelict2.md)) | – | must be carried (1×) | “I have already brought the 4 easier things.” |
| [Talion](../monsters/talion.md) | [Troubling times](../quests/troubling_times.md#stage-80) | must be carried (1×) | “I have everthing other than Luthor's ring” |
| [Talion](../monsters/talion.md) | [Troubling times](../quests/troubling_times.md#stage-280) | handed over (1×) | “Here's all you have asked for.” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_backstab.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_backstab.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_backstab.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ring_backstab.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `ring_backstab` |
    | Category ID | `ring` |
    | Icon | `items_jewelry:2` |
    | Defined in | `res/raw/itemlist_v0610_1.json` |
    | Loot tables containing it | `shop_dunla` |

    Raw data:

    ```json
    {
     "id": "ring_backstab",
     "iconID": "items_jewelry:2",
     "name": "Ring of backstabbing",
     "hasManualPrice": 0,
     "baseMarketCost": 1363,
     "category": "ring",
     "equipEffect": {
      "increaseAttackChance": 17,
      "increaseCriticalSkill": 7,
      "increaseBlockChance": 3
     }
    }
    ```


<small>Data from v0.8.18</small>
