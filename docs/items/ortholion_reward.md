---
description: "Ortholion's talisman is a extraordinary necklace in Andor's Trail (Attack damage 2 to 4, Max HP +5, Block chance +12, Grants immunity to Fear). How to get it: quests and dialogue. You feel warm and comfortable while holding it."
---

# ![](../assets/icons/items/items_necklaces_1_15.png){ .sprite } Ortholion's talisman

*Extraordinary necklace.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_necklaces_1_15.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `ortholion_reward` |
| **Category** | Necklace |
| **Slot** | neck |
| **Rarity** | Extraordinary |
| **Base value** | 5,836 gold |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

> You feel warm and comfortable while holding it.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 2 to 4 |
| Max HP | +5 |
| Block chance | +12 |
| Grants | immunity to [Fear](../conditions/fear.md) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [General Ortholion](../monsters/ortholion.md) ([Blackwater mountain 29](../maps/blackwater_mountain29.md)), walking into a blocked passage on [Elm 5f 2](../maps/elm5f_2.md) during [Climbing up is forbidden](../quests/Omi2_bwm1.md#stage-62) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |
| [v0.8.4](../versions/0.8.4.md) | Description text changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ortholion_reward.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ortholion_reward.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ortholion_reward.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=ortholion_reward.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `ortholion_reward` |
    | Category ID | `neck` |
    | Icon | `items_necklaces_1:15` |
    | Defined in | `res/raw/itemlist_omi2.json` |
    | Loot tables containing it | – |

    Raw data:

    ```json
    {
     "id": "ortholion_reward",
     "iconID": "items_necklaces_1:15",
     "name": "Ortholion's talisman",
     "displaytype": "extraordinary",
     "hasManualPrice": 1,
     "baseMarketCost": 5836,
     "category": "neck",
     "description": "You feel warm and comfortable while holding it.",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 2,
       "max": 4
      },
      "increaseMaxHP": 5,
      "increaseBlockChance": 12,
      "addedConditions": [
       {
        "condition": "fear",
        "magnitude": -99
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
