---
description: "Pyrite scimitar is a rare shortsword in Andor's Trail (Attack damage 4 to 12, Attack cost +4, Attack chance +20, Critical skill +2). How to get it: monster drops. A ceremonial temple weapon, the soft metal makes it a poor choice for defense."
---

# ![](../assets/icons/items/items_phoenix01_59.png){ .sprite } Pyrite scimitar

*Rare shortsword.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_phoenix01_59.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `brightport_sword` |
| **Category** | Shortsword |
| **Slot** | weapon |
| **Hands** | One-handed |
| **Proficiency** | [Dagger proficiency](../skills/weaponProficiencyDagger.md) |
| **Rarity** | Rare |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

> A ceremonial temple weapon, the soft metal makes it a poor choice for defense.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 4 to 12 |
| Attack cost | +4 |
| Attack chance | +20 |
| Critical skill | +2 |
| Block chance | -3 |
| Damage resistance | -1 |
| Critical multiplier | 2.0 |
| setNonWeaponDamageModifier | +96 |

### On hit

| Stat | Value |
|---|---|
| On self | [Soft metal](../conditions/brightport_scimitar.md) (magnitude 2, 1 round, 45% chance) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Dropped by

| Monster | Chance | Qty | Found in |
|---|---|---|---|
| [Lizardman corsair](../monsters/brightport_redlizard.md) | 1% | 1 | Brightport, Buried citadel |
| [Lizardman fencer](../monsters/brightport_redlizard2.md) | 1% | 1 | Buried citadel, Brightport |


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_sword.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_sword.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_sword.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_sword.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `brightport_sword` |
    | Category ID | `ssword` |
    | Icon | `items_phoenix01:59` |
    | Defined in | `res/raw/itemlist_brightport.json` |
    | Loot tables containing it | `brightport_redlizard` |

    Raw data:

    ```json
    {
     "id": "brightport_sword",
     "iconID": "items_phoenix01:59",
     "name": "Pyrite scimitar",
     "displaytype": "rare",
     "category": "ssword",
     "description": "A ceremonial temple weapon, the soft metal makes it a poor choice for defense.",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 4,
       "max": 12
      },
      "increaseAttackCost": 4,
      "increaseAttackChance": 20,
      "increaseCriticalSkill": 2,
      "increaseBlockChance": -3,
      "increaseDamageResistance": -1,
      "setCriticalMultiplier": 2.0,
      "setNonWeaponDamageModifier": 96
     },
     "hitEffect": {
      "conditionsSource": [
       {
        "condition": "brightport_scimitar",
        "magnitude": 2,
        "duration": 1,
        "chance": "45"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
