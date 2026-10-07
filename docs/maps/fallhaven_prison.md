---
description: "Fallhaven prison is an indoor location in Andor's Trail, in Fallhaven (settlement). NPCs: Guard, Guard captain. Enemies: Prisoner. Exits to Fallhaven north-west."
---

# Fallhaven prison

<div class="infobox" markdown>

| | |
|---|---|
| **Map ID** | `fallhaven_prison` |
| **Region** | In Fallhaven (settlement) |
| **Type** | Indoors / underground |
| **Size** | 15×10 tiles |
| **Introduced** | v0.7.0 or earlier |
| **NPCs** | 2 |
| **Enemy types** | 1 |
| **Quests** | 2 |

</div>

**Fallhaven prison** is an indoor map, in Fallhaven (settlement). It has 2 NPCs and 1 kind of enemy. Exits lead to Fallhaven north-west.

## Map

<div class="map-legend" markdown="0"><label class="lg"><input type="checkbox" data-t="spawn" checked><span class="sw sw-spawn"></span><b>Red</b>&nbsp;Monsters / NPCs</label><label class="lg"><input type="checkbox" data-t="mapchange" checked><span class="sw sw-mapchange"></span><b>Blue</b>&nbsp;Exit to another map</label><label class="lg"><input type="checkbox" data-t="container" checked><span class="sw sw-container"></span><b>Yellow</b>&nbsp;Container (click to see contents)</label><label class="lg"><input type="checkbox" data-t="sign" checked><span class="sw sw-sign"></span><b>Purple</b>&nbsp;Sign</label><label class="lg"><input type="checkbox" data-t="rest" checked><span class="sw sw-rest"></span><b>Green</b>&nbsp;Resting place</label><label class="lg"><input type="checkbox" data-t="key" checked><span class="sw sw-key"></span><b>Orange dashed</b>&nbsp;Blocked until a quest step / item</label><label class="lg"><input type="checkbox" data-t="script"><span class="sw sw-script"></span><b>Grey dotted</b>&nbsp;Scripted event</label><label class="lg"><input type="checkbox" data-t="replace"><span class="sw sw-replace"></span><b>White dotted</b>&nbsp;Changes during a quest</label><label class="lg"><input type="checkbox" data-t="pin" checked><span class="sw sw-pin"></span><b>Numbers</b>&nbsp;Numbered key points (see the key below the map)</label></div>

<div class="map-wrap hide-script hide-replace" markdown="0"><img src="../../assets/maps/fallhaven_prison.webp" alt="Map of Fallhaven prison" width="480" height="320" loading="lazy"><a id="place-entrance" class="mo mo-mapchange" href="../fallhaven_nw/#place-prison" title="Exit to Fallhaven north-west" style="left:33.333%;top:90.000%;width:6.667%;height:10.000%"></a><span class="mo mo-spawn" title="Spawns: Prisoner" style="left:60.000%;top:30.000%;width:33.333%;height:30.000%"></span><span class="mo mo-spawn" title="Spawns: Guard" style="left:86.667%;top:70.000%;width:6.667%;height:10.000%"></span><span class="mo mo-spawn" title="Spawns: Guard" style="left:6.667%;top:70.000%;width:6.667%;height:10.000%"></span><span class="mo mo-spawn" title="Spawns: Guard captain" style="left:20.000%;top:40.000%;width:6.667%;height:10.000%"></span><a class="mob" href="../../monsters/prisoner/" title="Prisoner" style="left:86.667%;top:30.000%;width:6.667%;height:10.000%"><img src="../../assets/icons/monsters/monsters_rogue1_0.png" alt="Prisoner"></a><a class="mob" href="../../monsters/guard/" title="Guard" style="left:86.667%;top:70.000%;width:6.667%;height:10.000%"><img src="../../assets/icons/monsters/monsters_rltiles3_14.png" alt="Guard"></a><a class="mob" href="../../monsters/guard/" title="Guard" style="left:6.667%;top:70.000%;width:6.667%;height:10.000%"><img src="../../assets/icons/monsters/monsters_rltiles3_14.png" alt="Guard"></a><a class="mob" href="../../monsters/warden/" title="Guard captain" style="left:20.000%;top:40.000%;width:6.667%;height:10.000%"><img src="../../assets/icons/monsters/monsters_men_3.png" alt="Guard captain"></a><a class="pin pin-exit" href="#key-1" style="left:36.667%;top:95.000%" title="Exit (south): to [Fallhaven north-west](fallhaven_nw.md)">1</a><a id="pin-npc-guard" class="pin pin-npc" href="#key-2" style="left:90.000%;top:75.000%" title="[Guard](../../monsters/guard.md): NPC">2</a><a id="pin-npc-warden" class="pin pin-npc" href="#key-3" style="left:23.333%;top:45.000%" title="[Guard captain](../../monsters/warden.md): 2 quests">3</a></div>

??? abstract "Key to the numbers on the map"

    | # | What | Details |
    |---|---|---|
    | <span id="key-1"></span>1 | Exit (south) | to [Fallhaven north-west](fallhaven_nw.md) |
    | <span id="key-2"></span>2 | [Guard](../monsters/guard.md) | NPC |
    | <span id="key-3"></span>3 | [Guard captain](../monsters/warden.md) | 2 quests |


<p class="verified">Verified against v0.8.18 map data.</p>

## Connections

| Direction | Leads to | Region there | Map # |
|---|---|---|---|
| South | [Fallhaven north-west](fallhaven_nw.md) | Fallhaven | 1 |

## NPCs

- [Guard](../monsters/guard.md) (#2)
- [Guard captain](../monsters/warden.md) — quests: [A path to the Duleian Road](../quests/pathway_fallhaven.md), [Night visit](../quests/farrik.md) (#3)

## Enemies

| Enemy | HP | Damage | Up to | Notes |
|---|---|---|---|---|
| [Prisoner](../monsters/prisoner.md) | 1 | 0–0 | 1 | – |

<small>“Up to” is the most that can be alive at once from the spawn areas on this map.</small>

## Quests

- [A path to the Duleian Road](../quests/pathway_fallhaven.md): [Guard captain](../monsters/warden.md) is involved
- [Night visit](../quests/farrik.md): [Guard captain](../monsters/warden.md) is involved


## Version history

| Version | Change |
|---|---|
| [v0.7.0](../versions/0.7.0.md) | Present in v0.7.0 (earliest release tracked) |
| [v0.7.1](../versions/0.7.1.md) | map layout or objects changed |
| [v0.7.2](../versions/0.7.2.md) | map layout or objects changed |
| [v0.8.2](../versions/0.8.2.md) | map layout or objects changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=fallhaven_prison.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=fallhaven_prison.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=fallhaven_prison.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*No notes yet. Contributions are welcome: [add a note](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=fallhaven_prison.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Map ID | `fallhaven_prison` |
    | File | `res/xml/fallhaven_prison.tmx` |
    | Size | 15×10 tiles (480×320 px) |
    | outdoors property | – |
    | Layers drawn | ground, objects, above |
    | Tilesets | map_bed_1, map_border_1, map_bridge_1, map_bridge_2, map_broken_1, map_cavewall_1, map_cavewall_2, map_cavewall_3, map_cavewall_4, map_chair_table_1, map_chair_table_2, map_crate_1, map_cupboard_1, map_curtain_1, map_entrance_1, map_entrance_2, map_fence_1, map_fence_2, map_fence_3, map_fence_4, map_ground_1, map_ground_2, map_ground_3, map_ground_4, map_ground_5, map_ground_6, map_ground_7, map_ground_8, map_house_1, map_house_2, map_indoor_1, map_indoor_2, map_kitchen_1, map_outdoor_1, map_pillar_1, map_pillar_2, map_plant_1, map_plant_2, map_rock_1, map_rock_2, map_roof_1, map_roof_2, map_roof_3, map_shop_1, map_sign_ladder_1, map_table_1, map_trail_1, map_transition_1, map_transition_2, map_transition_3, map_transition_4, map_transition_5, map_tree_1, map_tree_2, map_wall_1, map_wall_2, map_wall_3, map_wall_4, map_window_1, map_window_2 |
    | Map objects | spawn: 4, mapchange: 1 |
    | World map position | – |


<small>Data from v0.8.18</small>
