---
description: "Bronze coin is a rare other in Andor's Trail. How to get it: containers."
---

# ![](../assets/icons/items/items_japozero_360.png){ .sprite } Bronze coin

*Rare other.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_japozero_360.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `bronze_coin` |
| **Category** | Other |
| **Rarity** | Rare |
| **Base value** | 5 gold |
| **Introduced** | [v0.8.8](../versions/0.8.8.md) |

</div>

## How to get it

### Found in containers

- [thieves_vault](../maps/thieves_vault.md#container-8) (container 9, 100%), Blackwater Mountain


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>

## Uses

Where the game checks for this item in dialogue:

| With | Quest | What happens to it | Option |
|---|---|---|---|
| [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) | – | must be carried (50×) | “[Lie]I have these bronze and silver coins that I "acquired" in a game of chance.” |
| [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3) ([waytobrimhaven3](../maps/waytobrimhaven3.md)) | – | must be carried (50×) | “[Lie] I have these bronze and silver coins that I "acquired" in a game of chance” |
| [Forenza](../monsters/forenza.md#v-forenza_waytobrimhaven3) ([waytobrimhaven3](../maps/waytobrimhaven3.md)), [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) | [laeroth_nondisplay (hidden flag)](../quests/laeroth_nondisplay.md#stage-107) | handed over (5×) | “Well, something is better than nothing.” |

<p class="verified">Verified against v0.8.18 dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bronze_coin.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bronze_coin.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bronze_coin.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=bronze_coin.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `bronze_coin` |
    | Category ID | `other` |
    | Icon | `items_japozero:360` |
    | Defined in | `res/raw/itemlist_mt_galmore.json` |
    | Loot tables containing it | `thieves_vault_bronze` |

    Raw data:

    ```json
    {
     "id": "bronze_coin",
     "iconID": "items_japozero:360",
     "name": "Bronze coin",
     "displaytype": "rare",
     "hasManualPrice": 1,
     "baseMarketCost": 5,
     "category": "other"
    }
    ```


<small>Data from v0.8.18</small>
