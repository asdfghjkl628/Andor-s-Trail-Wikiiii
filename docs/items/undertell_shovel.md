---
description: "Undertell shovel is a rare pole weapon in Andor's Trail (Attack damage 4 to 7, Attack cost +7, Attack chance +20, Critical skill +10). How to get it: shops."
---

# ![](../assets/icons/items/items_misc_5_25.png){ .sprite } Undertell shovel

*Rare pole weapon.*

<div class="infobox" markdown>

<p class="ib-img"><img class="sprite" src="../../assets/icons/items/items_misc_5_25.png" alt=""></p>

| | |
|---|---|
| **Item ID** | `undertell_shovel` |
| **Category** | Pole weapon |
| **Slot** | weapon |
| **Hands** | Two-handed |
| **Proficiency** | [Pole weapon proficiency](../skills/weaponProficiencyPole.md) |
| **Rarity** | Rare |
| **Base value** | 2,194 gold |
| **Introduced** | [v0.8.18](../versions/0.8.18.md) |

</div>

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Attack damage | 4 to 7 |
| Attack cost | +7 |
| Attack chance | +20 |
| Critical skill | +10 |
| Critical multiplier | 2.0 |
| setNonWeaponDamageModifier | +128 |

### On hit

| Stat | Value |
|---|---|
| On self | [Fatigue](../conditions/fatigue2.md) (magnitude 1, 1 round, 10% chance) |
| On target | [Head wound](../conditions/head_wound.md) (magnitude 1, 2 rounds, 5% chance) |

### On kill

| Stat | Value |
|---|---|
| On self | [Increased defense](../conditions/increased_defense.md) (magnitude 1, 2 rounds) |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Sold by

- [Shy Cora](../monsters/shy_cora.md) (Undertell 01, Undertell 1 1)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=undertell_shovel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=undertell_shovel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=undertell_shovel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=undertell_shovel.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `undertell_shovel` |
    | Category ID | `pole` |
    | Icon | `items_misc_5:25` |
    | Defined in | `res/raw/itemlist_undertell.json` |
    | Loot tables containing it | `cora_dl` |

    Raw data:

    ```json
    {
     "id": "undertell_shovel",
     "iconID": "items_misc_5:25",
     "name": "Undertell shovel",
     "displaytype": "rare",
     "baseMarketCost": 2194,
     "category": "pole",
     "equipEffect": {
      "increaseAttackDamage": {
       "min": 4,
       "max": 7
      },
      "increaseAttackCost": 7,
      "increaseAttackChance": 20,
      "increaseCriticalSkill": 10,
      "setCriticalMultiplier": 2.0,
      "setNonWeaponDamageModifier": 128
     },
     "hitEffect": {
      "conditionsSource": [
       {
        "condition": "fatigue2",
        "magnitude": 1,
        "duration": 1,
        "chance": "10"
       }
      ],
      "conditionsTarget": [
       {
        "condition": "head_wound",
        "magnitude": 1,
        "duration": 2,
        "chance": "5"
       }
      ]
     },
     "killEffect": {
      "conditionsSource": [
       {
        "condition": "increased_defense",
        "magnitude": 1,
        "duration": 2,
        "chance": "100"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
