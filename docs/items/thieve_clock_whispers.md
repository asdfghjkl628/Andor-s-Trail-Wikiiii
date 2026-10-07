# ![](../assets/icons/items/items_tometik2_8.png){ .sprite } Thieves' cloak of whispers

*Rare armor, cloth.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_tometik2_8.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `thieve_clock_whispers` |
| **Category** | Armor, cloth |
| **Slot** | body |
| **Rarity** | Rare |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.2](../versions/0.8.2.md) |

</div>

> A thief's right of passage.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Move cost | -1 |
| Use item cost | -1 |
| Re-equip cost | +2 |
| Attack chance | +10 |
| Block chance | +20 |
| Damage resistance | -1 |

### On kill

| Stat | Value |
|---|---|
| On self | Minor speed (magnitude 1, 3 rounds, 10% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Prowling Arantxa](../monsters/sullengard_arantxa.md) (Sullengard)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.2](../versions/0.8.2.md) | Added |
| [v0.8.8](../versions/0.8.8.md) | name: Thieve's cloak of whispers → Thieves' cloak of whispers |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=thieve_clock_whispers.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=thieve_clock_whispers.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=thieve_clock_whispers.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=thieve_clock_whispers.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `thieve_clock_whispers` |
    | Category ID | `bdy_clth` |
    | Icon | `items_tometik2:8` |
    | Defined in | `res/raw/itemlist_sullengard.json` |
    | Loot tables containing it | `sullengard_arantxa_dl` |

    Raw data:

    ```json
    {
     "id": "thieve_clock_whispers",
     "iconID": "items_tometik2:8",
     "name": "Thieves' cloak of whispers",
     "displaytype": "rare",
     "category": "bdy_clth",
     "description": "A thief's right of passage.",
     "equipEffect": {
      "increaseMoveCost": -1,
      "increaseUseItemCost": -1,
      "increaseReequipCost": 2,
      "increaseAttackChance": 10,
      "increaseBlockChance": 20,
      "increaseDamageResistance": -1
     },
     "killEffect": {
      "conditionsSource": [
       {
        "condition": "speed_minor",
        "magnitude": 1,
        "duration": 3,
        "chance": "10"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
