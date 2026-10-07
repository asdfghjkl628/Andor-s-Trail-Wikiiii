---
description: "Engraved steel helmet is a rare headwear, metal (heavy) in Andor's Trail (Attack damage 0, Max HP +2, Re-equip cost 0, Attack chance -1). How to get it: monster drops."
---

# ![](../assets/icons/items/items_armours_25.png){ .sprite } Engraved steel helmet

*Rare headwear, metal (heavy).*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_armours_25.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `brimhaven_engraved_steel_helmet` |
| **Category** | Headwear, metal (heavy) |
| **Slot** | head |
| **Proficiency** | [Heavy armor proficiency](../skills/armorProficiencyHeavy.md) |
| **Rarity** | Rare |
| **Base value** | 0 gold |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 0 |
| Max HP | +2 |
| Re-equip cost | 0 |
| Attack chance | -1 |
| Block chance | +6 |
| Damage resistance | 0 |

### When hit

| Stat | Value |
|---|---|
| On self | [Bark skin](../conditions/barkskin.md) (magnitude 1, 2 rounds, 5% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Ancient basilisk](../monsters/old_basilisk.md) | 100% | 1 | basiliskcave2 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brimhaven_engraved_steel_helmet.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brimhaven_engraved_steel_helmet.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brimhaven_engraved_steel_helmet.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brimhaven_engraved_steel_helmet.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `brimhaven_engraved_steel_helmet` |
    | Category ID | `hd_mtl_hv` |
    | Icon | `items_armours:25` |
    | Defined in | `res/raw/itemlist_brimhaven.json` |
    | Loot tables containing it | `old_basilisk` |

    Raw data:

    ```json
    {
     "id": "brimhaven_engraved_steel_helmet",
     "iconID": "items_armours:25",
     "name": "Engraved steel helmet",
     "displaytype": "rare",
     "category": "hd_mtl_hv",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 0,
       "max": 0
      },
      "increaseMaxHP": 2,
      "increaseReequipCost": 0,
      "increaseAttackChance": -1,
      "increaseBlockChance": 6,
      "increaseDamageResistance": 0
     },
     "hitReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "barkskin",
        "magnitude": 1,
        "duration": 2,
        "chance": "5"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
