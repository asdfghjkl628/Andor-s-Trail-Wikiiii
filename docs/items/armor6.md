---
description: "Dented bronze plate is a ordinary armor (heavy) in Andor's Trail (Max HP +6, Move cost +1, Attack cost 0, Attack chance -8). How to get it: monster drops, containers. This armor has definitely seen better days."
---

# ![](../assets/icons/items/items_armours_20.png){ .sprite } Dented bronze plate

*Ordinary armor (heavy).*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_armours_20.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `armor6` |
| **Category** | Armor (heavy) |
| **Slot** | body |
| **Proficiency** | [Heavy armor proficiency](../skills/armorProficiencyHeavy.md) |
| **Rarity** | Ordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.14](../versions/0.7.14.md) |

</div>

> This armor has definitely seen better days.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Max HP | +6 |
| Move cost | +1 |
| Attack cost | 0 |
| Attack chance | -8 |
| Critical skill | 0 |
| Block chance | +13 |
| Damage resistance | 0 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Kazarite golem](../monsters/elm_golem1.md) | 1% | 1 | elm5f_1, elm5f_2, elm_3f |
| [Dried kazarite golem](../monsters/elm_golem2.md) | 1% | 1 | elm5f_1, elm5f_2, elm_3f |

### Found in containers

- [elm_4f_2](../maps/elm_4f_2.md#container-0) (container 1, 1%)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.14](../versions/0.7.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armor6.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armor6.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armor6.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=armor6.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `armor6` |
    | Category ID | `bdy_hv` |
    | Icon | `items_armours:20` |
    | Defined in | `res/raw/itemlist_omi2.json` |
    | Loot tables containing it | `elm_golem` |

    Raw data:

    ```json
    {
     "id": "armor6",
     "iconID": "items_armours:20",
     "name": "Dented bronze plate",
     "displaytype": "ordinary",
     "category": "bdy_hv",
     "description": "This armor has definitely seen better days.",
     "equipEffect": {
      "increaseMaxHP": 6,
      "increaseMoveCost": 1,
      "increaseAttackCost": 0,
      "increaseAttackChance": -8,
      "increaseCriticalSkill": 0,
      "increaseBlockChance": 13,
      "increaseDamageResistance": 0
     }
    }
    ```


<small>Data from v0.8.18</small>
