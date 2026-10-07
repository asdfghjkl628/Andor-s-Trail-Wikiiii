---
description: "Emberwylde is a extraordinary armor (light) in Andor's Trail (Max HP +4, Block chance +11, Damage resistance +2, Grants Concentration (magnitude 1)). How to get it: monster drops."
---

# ![](../assets/icons/items/items_tometik2_69.png){ .sprite } Emberwylde

*Extraordinary armor (light).*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_tometik2_69.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `emberwylde` |
| **Category** | Armor (light) |
| **Slot** | body |
| **Proficiency** | [Light armor proficiency](../skills/armorProficiencyLight.md) |
| **Rarity** | Extraordinary |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.14](../versions/0.8.14.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Max HP | +4 |
| Block chance | +11 |
| Damage resistance | +2 |
| Grants | Concentration (magnitude 1) |

### On kill

| Stat | Value |
|---|---|
| On self | Cinder rage (magnitude 1, 3 rounds, 25% chance) |

### When hit

| Stat | Value |
|---|---|
| On target | Ablaze (magnitude 2, 2 rounds, 8% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Pyreling behemoth](../monsters/Pyreling_behemoth.md) | 100% | 1 | galmore_71 |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.14](../versions/0.8.14.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=emberwylde.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=emberwylde.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=emberwylde.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=emberwylde.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `emberwylde` |
    | Category ID | `bdy_lt` |
    | Icon | `items_tometik2:69` |
    | Defined in | `res/raw/itemlist_mt_galmore2.json` |
    | Loot tables containing it | `Pyreling_behemoth_dl` |

    Raw data:

    ```json
    {
     "id": "emberwylde",
     "iconID": "items_tometik2:69",
     "name": "Emberwylde",
     "displaytype": "extraordinary",
     "category": "bdy_lt",
     "equipEffect": {
      "increaseMaxHP": 4,
      "increaseBlockChance": 11,
      "increaseDamageResistance": 2,
      "addedConditions": [
       {
        "condition": "g03_concentration",
        "magnitude": 1
       }
      ]
     },
     "hitReceivedEffect": {
      "conditionsTarget": [
       {
        "condition": "fire",
        "magnitude": 2,
        "duration": 2,
        "chance": "8"
       }
      ]
     },
     "killEffect": {
      "conditionsSource": [
       {
        "condition": "cinder_rage",
        "magnitude": 1,
        "duration": 3,
        "chance": "25"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
