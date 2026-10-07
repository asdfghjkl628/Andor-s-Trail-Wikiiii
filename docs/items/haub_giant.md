---
description: "Giant's hauberk is a extraordinary armor (heavy) in Andor's Trail (Max HP +3, Attack cost +1, Block chance +23, Damage resistance +1). How to get it: monster drops."
---

# ![](../assets/icons/items/items_tometik2_44.png){ .sprite } Giant's hauberk

*Extraordinary armor (heavy).*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_tometik2_44.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `haub_giant` |
| **Category** | Armor (heavy) |
| **Slot** | body |
| **Proficiency** | [Heavy armor proficiency](../skills/armorProficiencyHeavy.md) |
| **Rarity** | Extraordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.8](../versions/0.7.8.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Max HP | +3 |
| Attack cost | +1 |
| Block chance | +23 |
| Damage resistance | +1 |

### When hit

| Stat | Value |
|---|---|
| On self | [Increased defense](../conditions/increased_defense.md) (magnitude 1, 3 rounds, 15% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Arulir Pack Leader](../monsters/arulir_leader.md) | 100% | 1 | arulircave6 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.8](../versions/0.7.8.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=haub_giant.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=haub_giant.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=haub_giant.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=haub_giant.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `haub_giant` |
    | Category ID | `bdy_hv` |
    | Icon | `items_tometik2:44` |
    | Defined in | `res/raw/itemlist_arulir_mountain.json` |
    | Loot tables containing it | `arulir_leader` |

    Raw data:

    ```json
    {
     "id": "haub_giant",
     "iconID": "items_tometik2:44",
     "name": "Giant's hauberk",
     "displaytype": "extraordinary",
     "category": "bdy_hv",
     "equipEffect": {
      "increaseMaxHP": 3,
      "increaseAttackCost": 1,
      "increaseBlockChance": 23,
      "increaseDamageResistance": 1
     },
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "increased_defense",
        "magnitude": 1,
        "duration": 3,
        "chance": "15"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
