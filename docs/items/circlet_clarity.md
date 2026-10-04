# ![](../assets/icons/items/items_newb_258.png){ .sprite } Circlet of clarity

*Extraordinary ring.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_newb_258.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `circlet_clarity` |
| **Category** | Ring |
| **Slot** | leftring |
| **Rarity** | Extraordinary |
| **Base value** | 4,127 gold |
| **Introduced** | [v0.8.12.1](../versions/0.8.12.1.md) |

</div>

> An ancient artifact that shields the wearer from mental afflictions, offering protection and peace of mind.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Max HP | -15 |
| Attack chance | -10 |
| Block chance | -10 |
| Damage resistance | +3 |

### On kill

| Stat | Value |
|---|---|
| On self | Confusion (magnitude -99, 4 rounds, 100% chance) |

### When hit

| Stat | Value |
|---|---|
| On self | Dazed (magnitude -99, 3 rounds, 100% chance); Mind fog (magnitude -99, 2 rounds, 100% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Forenza](../monsters/forenza_waytobrimhaven3.md) ([waytobrimhaven3](../maps/waytobrimhaven3.md)), [Gylew](../monsters/gylew.md) ([waterway5](../maps/waterway5.md)) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.12.1](../versions/0.8.12.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=circlet_clarity.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=circlet_clarity.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=circlet_clarity.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=circlet_clarity.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `circlet_clarity` |
    | Category ID | `ring` |
    | Icon | `items_newb:258` |
    | Defined in | `res/raw/itemlist_feygard_1.json` |
    | Loot tables containing it | – |

    Raw data:

    ```json
    {
     "id": "circlet_clarity",
     "iconID": "items_newb:258",
     "name": "Circlet of clarity",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 4127,
     "category": "ring",
     "description": "An ancient artifact that shields the wearer from mental afflictions, offering protection and peace of mind.",
     "equipEffect": {
      "increaseMaxHP": -15,
      "increaseAttackChance": -10,
      "increaseBlockChance": -10,
      "increaseDamageResistance": 3
     },
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "dazed",
        "magnitude": -99,
        "duration": 3,
        "chance": "100"
       },
       {
        "condition": "mind_fog",
        "magnitude": -99,
        "duration": 2,
        "chance": "100"
       }
      ]
     },
     "killEffect": {
      "conditionsSource": [
       {
        "condition": "confusion",
        "magnitude": -99,
        "duration": 4,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
