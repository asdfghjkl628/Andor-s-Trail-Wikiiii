---
description: "Agent's cloak is a rare armor, cloth in Andor's Trail (Max HP +8, Move cost -1, Attack chance +4, Critical skill 0). How to get it: quests and dialogue. Whoever dons this makes it clear: the one who sent them expects no failure."
---

# ![](../assets/icons/items/items_tometik2_4.png){ .sprite } Agent's cloak

*Rare armor, cloth.*

<div class="infobox" markdown>

<p class="ib-img">![](../../assets/icons/items/items_tometik2_4.png){ .sprite }</p>

| | |
|---|---|
| **Item ID** | `brightport_cloak` |
| **Category** | Armor, cloth |
| **Slot** | body |
| **Rarity** | Rare |
| **Base value** | 0 gold |
| **Introduced** | [v0.8.16.1](../versions/0.8.16.1.md) |

</div>

> Whoever dons this makes it clear: the one who sent them expects no failure.

## Statistics

### When equipped

| Stat | Value |
|---|---|
| Max HP | +8 |
| Move cost | -1 |
| Attack chance | +4 |
| Critical skill | 0 |
| Block chance | +13 |
| Damage resistance | 0 |

<p class="verified">Verified against v0.8.18 item data.</p>

## How to get it

### Quest & dialogue rewards

- From [Gunfryk](../monsters/brightportguardcaptain.md#v-brightport_gunfrykstill) ([brightport_bakery](../maps/brightport_bakery.md)) during [Boxed in](../quests/brightport_thieves.md#stage-60) (1×)


<p class="verified">Verified against v0.8.18 item, loot, map and dialogue data.</p>


## Version history

| Version | Change |
|---|---|
| [v0.8.16.1](../versions/0.8.16.1.md) | Added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Strategy**: how and when to use it · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Strategy

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_cloak.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_cloak.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_cloak.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/items?filename=brightport_cloak.md&value=%23%23%20Strategy%0A%0A%3C%21--%20how%20and%20when%20to%20use%20it%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Item ID | `brightport_cloak` |
    | Category ID | `bdy_clth` |
    | Icon | `items_tometik2:4` |
    | Defined in | `res/raw/itemlist_brightport.json` |
    | Loot tables containing it | – |

    Raw data:

    ```json
    {
     "id": "brightport_cloak",
     "iconID": "items_tometik2:4",
     "name": "Agent's cloak",
     "displaytype": "rare",
     "category": "bdy_clth",
     "description": "Whoever dons this makes it clear: the one who sent them expects no failure.",
     "equipEffect": {
      "increaseMaxHP": 8,
      "increaseMoveCost": -1,
      "increaseAttackChance": 4,
      "increaseCriticalSkill": 0,
      "increaseBlockChance": 13,
      "increaseDamageResistance": 0
     },
     "missEffect": {},
     "missReceivedEffect": {
      "conditionsSource": [
       {
        "condition": "brightport_shadow",
        "magnitude": 1,
        "duration": 2,
        "chance": "40"
       }
      ]
     }
    }
    ```


<small>Data from v0.8.18</small>
