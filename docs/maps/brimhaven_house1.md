# Brimhaven house1

<div class="infobox" markdown>

| | |
|---|---|
| **Map ID** | `brimhaven_house1` |
| **Type** | Indoors / underground |
| **Size** | 16×9 tiles |
| **Introduced** | [v0.7.11](../versions/0.7.11.md) |
| **NPCs** | 2 |
| **Quests** | 3 |

</div>

**Brimhaven house1** is an indoor map. It has 2 NPCs, and no enemies. Exits lead to Brimhaven8.

## Map

<div class="map-legend" markdown="0"><label class="lg"><input type="checkbox" data-t="spawn" checked><span class="sw sw-spawn"></span><b>Red</b>&nbsp;Monsters / NPCs</label><label class="lg"><input type="checkbox" data-t="mapchange" checked><span class="sw sw-mapchange"></span><b>Blue</b>&nbsp;Exit to another map</label><label class="lg"><input type="checkbox" data-t="container" checked><span class="sw sw-container"></span><b>Yellow</b>&nbsp;Container (click to see contents)</label><label class="lg"><input type="checkbox" data-t="sign" checked><span class="sw sw-sign"></span><b>Purple</b>&nbsp;Sign</label><label class="lg"><input type="checkbox" data-t="rest" checked><span class="sw sw-rest"></span><b>Green</b>&nbsp;Resting place</label><label class="lg"><input type="checkbox" data-t="key" checked><span class="sw sw-key"></span><b>Orange dashed</b>&nbsp;Blocked until a quest step / item</label><label class="lg"><input type="checkbox" data-t="script"><span class="sw sw-script"></span><b>Grey dotted</b>&nbsp;Scripted event</label><label class="lg"><input type="checkbox" data-t="replace"><span class="sw sw-replace"></span><b>White dotted</b>&nbsp;Changes during a quest</label><label class="lg"><input type="checkbox" data-t="pin" checked><span class="sw sw-pin"></span><b>Numbers</b>&nbsp;Numbered key points (see the key below the map)</label></div>

<div class="map-wrap hide-script hide-replace" markdown="0"><img src="../../assets/maps/brimhaven_house1.webp" alt="Map of Brimhaven house1" width="512" height="288" loading="lazy"><a id="place-entrance" class="mo mo-mapchange" href="../brimhaven8/#place-entrance" title="Exit to Brimhaven8" style="left:43.750%;top:88.889%;width:6.250%;height:11.111%"></a><span class="mo mo-spawn" title="Spawns: Alkapoan" style="left:12.500%;top:44.444%;width:75.000%;height:33.333%"></span><span class="mo mo-spawn" title="Spawns: Alkapoan (only appears later, during a quest)" style="left:50.000%;top:33.333%;width:6.250%;height:22.222%"></span><span class="mo mo-spawn" title="Spawns: Mustura (only appears later, during a quest)" style="left:56.250%;top:33.333%;width:6.250%;height:22.222%"></span><a class="mob" href="../../monsters/brv_richman/" title="Alkapoan" style="left:12.500%;top:55.556%;width:6.250%;height:11.111%"><img src="../../assets/icons/monsters/monsters_tometik1_2.png" alt="Alkapoan"></a><a class="mob mob-later" href="../../monsters/brv_richman/" title="Alkapoan (appears later in a quest)" style="left:50.000%;top:44.444%;width:6.250%;height:11.111%"><img src="../../assets/icons/monsters/monsters_tometik1_2.png" alt="Alkapoan"></a><a class="mob mob-later" href="../../monsters/brv_guard_captain/" title="Mustura (appears later in a quest)" style="left:56.250%;top:33.333%;width:6.250%;height:11.111%"><img src="../../assets/icons/monsters/monsters_ld2_49.png" alt="Mustura"></a><a class="pin pin-exit" href="#key-1" style="left:46.875%;top:94.444%" title="Exit (south): to [Brimhaven8](../brimhaven8.md)">1</a><a class="pin pin-npc" href="#key-2" style="left:15.625%;top:61.111%" title="[Alkapoan](../../monsters/brv_richman.md): 3 quests">2</a><a class="pin pin-npc" href="#key-3" style="left:59.375%;top:38.889%" title="[Mustura](../../monsters/brv_guard_captain.md): 2 quests">3</a></div>

??? abstract "Key to the numbers on the map"

    | # | What | Details |
    |---|---|---|
    | <span id="key-1"></span>1 | Exit (south) | to [Brimhaven8](../brimhaven8.md) |
    | <span id="key-2"></span>2 | [Alkapoan](../monsters/brv_richman.md) | 3 quests |
    | <span id="key-3"></span>3 | [Mustura](../monsters/brv_guard_captain.md) | 2 quests |


<p class="verified">Verified against v0.8.18 map data.</p>

## Connections

| Direction | Leads to | Region there | Map # |
|---|---|---|---|
| South | [Brimhaven8](brimhaven8.md) | Brimhaven | 1 |

## NPCs

- [Alkapoan](../monsters/brv_richman.md) — quests: [A place to forge](../quests/place_to_forge.md), [Much water](../quests/brv_flood.md), [Search for Andor](../quests/andor.md) (#2)
- [Mustura](../monsters/brv_guard_captain.md) — quests: [A place to forge](../quests/place_to_forge.md), [Much water](../quests/brv_flood.md) (#3)

## Quests

- [A place to forge](../quests/place_to_forge.md): [Alkapoan](../monsters/brv_richman.md) is involved; [Mustura](../monsters/brv_guard_captain.md) is involved
- [Much water](../quests/brv_flood.md): [Alkapoan](../monsters/brv_richman.md) is involved; [Mustura](../monsters/brv_guard_captain.md) is involved
- [Search for Andor](../quests/andor.md): [Alkapoan](../monsters/brv_richman.md) is involved
- [brv_nondisplay (hidden flag)](../quests/brv_nondisplay.md): [Alkapoan](../monsters/brv_richman.md) is involved; [Mustura](../monsters/brv_guard_captain.md) is involved
- [galmore_nondisplayed (hidden flag)](../quests/galmore_nondisplayed.md): [Alkapoan](../monsters/brv_richman.md) is involved
- [hidden_undertell (hidden flag)](../quests/undertell_hidden.md): [Alkapoan](../monsters/brv_richman.md) is involved; [Mustura](../monsters/brv_guard_captain.md) is involved


## Version history

| Version | Change |
|---|---|
| [v0.7.11](../versions/0.7.11.md) | Added |
| [v0.8.2](../versions/0.8.2.md) | map layout or objects changed |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>


## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=brimhaven_house1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=brimhaven_house1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=brimhaven_house1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/maps?filename=brimhaven_house1.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Map ID | `brimhaven_house1` |
    | File | `res/xml/brimhaven_house1.tmx` |
    | Size | 16×9 tiles (512×288 px) |
    | outdoors property | – |
    | Layers drawn | ground, objects, above |
    | Tilesets | map_bed_1, map_border_1, map_bridge_1, map_bridge_2, map_broken_1, map_cavewall_1, map_cavewall_2, map_cavewall_3, map_cavewall_4, map_chair_table_1, map_chair_table_2, map_crate_1, map_cupboard_1, map_curtain_1, map_entrance_1, map_entrance_2, map_fence_1, map_fence_2, map_fence_3, map_fence_4, map_ground_1, map_ground_2, map_ground_3, map_ground_4, map_ground_5, map_ground_6, map_ground_7, map_ground_8, map_house_1, map_house_2, map_indoor_1, map_indoor_2, map_kitchen_1, map_outdoor_1, map_pillar_1, map_pillar_2, map_plant_1, map_plant_2, map_rock_1, map_rock_2, map_roof_1, map_roof_2, map_roof_3, map_shop_1, map_sign_ladder_1, map_table_1, map_trail_1, map_transition_1, map_transition_2, map_transition_3, map_transition_4, map_transition_5, map_tree_1, map_tree_2, map_wall_1, map_wall_2, map_wall_3, map_wall_4, map_window_1, map_window_2 |
    | Map objects | spawn: 3, mapchange: 1 |
    | World map position | – |


<small>Data from v0.8.18</small>
