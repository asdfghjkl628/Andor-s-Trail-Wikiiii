# The fifth master

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `fifth_master` |
| **In journal** | Yes |
| **Stages** | 16 (completes at 90) |
| **Started by** | [Zaroth](../monsters/zaroth.md) ([undertell_4_00](../maps/undertell_4_00.md)), [Morvath](../monsters/morvath.md) ([undertell_00](../maps/undertell_00.md)) |
| **NPCs involved** | [Anavrin](../monsters/anavrin.md), [Durnan the Hollow](../monsters/durnan.md), [Gwendolyn](../monsters/remgard_gwendolyn.md), [Kazaul acolyte](../monsters/kazaul_acolyte.md), [Kealwea](../monsters/sullengard_priest.md), [Morvath](../monsters/morvath.md) +4 |
| **Locations** | [remgard_church](../maps/remgard_church.md), [remgard_church_basement](../maps/remgard_church_basement.md), [sullengard_church](../maps/sullengard_church.md), [undertell_00](../maps/undertell_00.md) |
| **Total XP** | 14,165 |
| **Related quests** | 5 |

</div>

## Overview

> In Undertell, the Kazaul Masters spoke to me. They claimed a forgotten ritual could seal the Rift once and for all.

## Prerequisites to start

**Route 1** ([Zaroth](../monsters/zaroth.md) ([undertell_4_00](../maps/undertell_4_00.md))):

- reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10)
- NOT reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20)

**Route 2** ([Morvath](../monsters/morvath.md) ([undertell_00](../maps/undertell_00.md))):

- reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10)
- NOT reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20)

**Route 3** ([Thalen](../monsters/thalen.md) ([undertell_3_lava_00](../maps/undertell_3_lava_00.md))):

- reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10)
- NOT reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20)

**Route 4** ([Vaelzahr](../monsters/vaelzahr.md) ([undertell_7_00](../maps/undertell_7_00.md))):

- reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10)
- NOT reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [mg2_exploded_star_nd (hidden flag)](mg2_exploded_star_nd.md#stage-91) | stage 91 reached, for stage 40 here |
| Requires | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-45) | stage 45 reached, for stages 70, 72 here |
| Blocked by | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-50) | stage 50 must NOT be reached, for stages 65, 70, 72 here |
| Unlocks | [About a girl](about_a_girl.md#stage-50) | stage 50 there needs stage 90 here |
| Unlocks | [Dominion](dominion.md#stage-50) | stage 50 there needs stage 10 here |
| Unlocks | [Undertell: What was not written](undertell_book.md#stage-30) | stage 30 there needs stage 10 here |
| Unlocks | [hidden_undertell (hidden flag)](undertell_hidden.md#stage-50) | stage 50 there needs stage 65 here |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | In Undertell, the Kazaul Masters spoke to me. They claimed a forgotten ritual could seal the Rift once and for all. | [Zaroth](../monsters/zaroth.md) ([undertell_4_00](../maps/undertell_4_00.md))<br>[Morvath](../monsters/morvath.md) ([undertell_00](../maps/undertell_00.md))<br>[Thalen](../monsters/thalen.md) ([undertell_3_lava_00](../maps/undertell_3_lava_00.md))<br>+1 more | – | – |
| <span id="stage-20"></span>20 | They told me that this ritual was stolen long ago by a Lethgar named Varnel, who fled Undertell with it. I agreed to recover it, believing it might save Dhayavar. | [Zaroth](../monsters/zaroth.md) ([undertell_4_00](../maps/undertell_4_00.md))<br>[Morvath](../monsters/morvath.md) ([undertell_00](../maps/undertell_00.md))<br>[Thalen](../monsters/thalen.md) ([undertell_3_lava_00](../maps/undertell_3_lava_00.md))<br>+1 more | stage 10 | – |
| <span id="stage-30"></span>30 | In the upper dormitory tunnels of Undertell, I met the ghost of a miner who remembered Varnel. The ghost said Varnel escaped through the northern caverns and headed east toward the Sutdover River. Could he have meant Sullengard? | [Durnan the Hollow](../monsters/durnan.md) ([undertell_1_0](../maps/undertell_1_0.md)) | stage 20 | – |
| <span id="stage-40"></span>40 | I traveled to Sullengard and spoke with Kealwea, the local priest. He recalled a relic matching my description once being sent to the Shadow church library in Remgard. | [Kealwea](../monsters/sullengard_priest.md) ([sullengard_church](../maps/sullengard_church.md)) | stage 30 | – |
| <span id="stage-50"></span>50 | In Remgard's church basement, I spoke with Gwendolyn, the librarian. She said she knew nothing of any ritual but allowed me to search the shelves myself. | [Gwendolyn](../monsters/remgard_gwendolyn.md) ([remgard_church_basement](../maps/remgard_church_basement.md)) | stage 40 | – |
| <span id="stage-55"></span>55 | I discovered a small, locked box hidden behind the books. Its surface was etched with strange curling runes and old scorch marks. The box refused to open. | walking into a blocked passage on [remgard_church_basement](../maps/remgard_church_basement.md) | stage 50 | gives 1× [Ancient locked box](../items/ancient_locked_box.md) |
| <span id="stage-58"></span>58 | After I asked Gwendolyn about the locked box that I found, she directed me to speak with Skylenar upstairs. | [Gwendolyn](../monsters/remgard_gwendolyn.md) ([remgard_church_basement](../maps/remgard_church_basement.md)) | carry 1× [Ancient locked box](../items/ancient_locked_box.md), stage 55 | – |
| <span id="stage-60"></span>60 | Skylenar told me the box was an ancient relic, sealed by dragonkind and said to open only to a dragon's claw. | [Skylenar](../monsters/skylenar.md) ([remgard_church](../maps/remgard_church.md)) | carry 1× [Ancient locked box](../items/ancient_locked_box.md), stage 58 | – |
| <span id="stage-65"></span>65 | Skylenar mentioned that some old Shadow tales spoke of ash-covered scales found deep within Undertell, hinting that one such beast may once have lived there. | [Skylenar](../monsters/skylenar.md) ([remgard_church](../maps/remgard_church.md)) | carry 1× [Ancient locked box](../items/ancient_locked_box.md), stage 58 | – |
| <span id="stage-70"></span>70 | In the glowing white house basement, I talked to Falkour the dragon. When I showed him the locked box, he recognized it as a relic once held by Varnel.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [White house basement](../maps/white_house_basement.md).</span> | walking into a blocked passage on [white_house_basement](../maps/white_house_basement.md)<br>stepping on a trigger on [white_house_basement](../maps/white_house_basement.md) | carry 1× [Ancient locked box](../items/ancient_locked_box.md), stage 65 | – |
| <span id="stage-72"></span>72 | Falkour gifted me one of his claws, saying it could break the seal, and warned me to use it only for that purpose. Time to find a safe place in this basement to open the box.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [White house basement](../maps/white_house_basement.md).</span> | walking into a blocked passage on [white_house_basement](../maps/white_house_basement.md)<br>stepping on a trigger on [white_house_basement](../maps/white_house_basement.md) | carry 1× [Ancient locked box](../items/ancient_locked_box.md), stage 65 | gives 1× [Dragon claw](../items/dragon_claw_key.md) |
| <span id="stage-75"></span>75 | Using Falkour's claw, I unlocked the ancient box. Inside were the five pages of the Kazaul ritual the Masters desired.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [White house basement](../maps/white_house_basement.md).</span> | stepping on a trigger on [white_house_basement](../maps/white_house_basement.md) | carry 1× [Ancient locked box](../items/ancient_locked_box.md), carry 1× [Dragon claw](../items/dragon_claw_key.md), hand over 1× [Ancient locked box](../items/ancient_locked_box.md), stage 72 | gives 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md) |
| <span id="stage-78"></span>78 | The Master that I brought "The Five Aspects" ritual to sent me to talk to Thalen, the Master of Knowledge. | [Zaroth](../monsters/zaroth.md) ([undertell_4_00](../maps/undertell_4_00.md))<br>[Morvath](../monsters/morvath.md) ([undertell_00](../maps/undertell_00.md))<br>[Vaelzahr](../monsters/vaelzahr.md) ([undertell_7_00](../maps/undertell_7_00.md)) | carry 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md) | sets stage 7 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-7) |
| <span id="stage-80"></span>80 | I returned the ritual to Thalen. He told me to meet the "lesser kin" at Anavrin's shrine to perform the ceremony. | [Thalen](../monsters/thalen.md) ([undertell_3_lava_00](../maps/undertell_3_lava_00.md)) | carry 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md), hand over 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md) | spawns monsters on undertell_5<br>sets stage 7 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-7) |
| <span id="stage-85"></span>85 | As the ritual completed, the Masters revealed their true intent. The rite was not to seal the Rift but to awaken the Fifth Master, whose power might reopen it. They told me the Shadow itself serves Kazaul. Their words left me doubtful, unsure whether I had been deceived or warned.<br><span class="qnote">🗺️ Part of [Undertell 5](../maps/undertell_5.md) visibly changes.</span> | [Anavrin](../monsters/anavrin.md) ([undertell_5](../maps/undertell_5.md))<br>[Kazaul acolyte](../monsters/kazaul_acolyte.md) ([undertell_5](../maps/undertell_5.md)) | stage 80 | – |
| <span id="stage-90"></span>90 | I left Undertell uncertain of what to believe. If what the Masters said is true, the Shadow may not be what it seems. Still, doubt lingers like smoke after the forge cools. **(completes quest)** | [Anavrin](../monsters/anavrin.md) ([undertell_5](../maps/undertell_5.md)) | – | 14,165 XP |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 4 routes"

    1. Talk to [Zaroth](../monsters/zaroth.md) ([undertell_4_00](../maps/undertell_4_00.md)) → the conversation leads here automatically — **conditions:** reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); NOT reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20) → **stage 10**. NPC: “[The air grows heavy as the master studies you.] You are bold to walk here. Perhaps bold enough to be of use. One of…”
    2. Talk to [Morvath](../monsters/morvath.md) ([undertell_00](../maps/undertell_00.md)) → the conversation leads here automatically — **conditions:** reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); NOT reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20) → **stage 10**. NPC: “[The air grows heavy as the master studies you.] You are bold to walk here. Perhaps bold enough to be of use. One of…”
    3. Talk to [Thalen](../monsters/thalen.md) ([undertell_3_lava_00](../maps/undertell_3_lava_00.md)) → the conversation leads here automatically — **conditions:** reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); NOT reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20) → **stage 10**. NPC: “[The air grows heavy as the master studies you.] You are bold to walk here. Perhaps bold enough to be of use. One of…”
    4. Talk to [Vaelzahr](../monsters/vaelzahr.md) ([undertell_7_00](../maps/undertell_7_00.md)) → the conversation leads here automatically — **conditions:** reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); NOT reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20) → **stage 10**. NPC: “[The air grows heavy as the master studies you.] You are bold to walk here. Perhaps bold enough to be of use. One of…”

???+ note "Stage 20: 4 routes"

    1. Talk to [Zaroth](../monsters/zaroth.md) ([undertell_4_00](../maps/undertell_4_00.md)) → choose “You want me to find this ritual?” — **conditions:** reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); NOT reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20) → **stage 20**. NPC: “Yes. The Ritual of Five Aspects lies lost among your kind. Long ago, a mortal scribe named Varnel served the Kazaul,…”
    2. Talk to [Morvath](../monsters/morvath.md) ([undertell_00](../maps/undertell_00.md)) → choose “You want me to find this ritual?” — **conditions:** reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); NOT reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20) → **stage 20**. NPC: “Yes. The Ritual of Five Aspects lies lost among your kind. Long ago, a mortal scribe named Varnel served the Kazaul,…”
    3. Talk to [Thalen](../monsters/thalen.md) ([undertell_3_lava_00](../maps/undertell_3_lava_00.md)) → choose “You want me to find this ritual?” — **conditions:** reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); NOT reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20) → **stage 20**. NPC: “Yes. The Ritual of Five Aspects lies lost among your kind. Long ago, a mortal scribe named Varnel served the Kazaul,…”
    4. Talk to [Vaelzahr](../monsters/vaelzahr.md) ([undertell_7_00](../maps/undertell_7_00.md)) → choose “You want me to find this ritual?” — **conditions:** reached stage 10 of [The fifth master](../quests/fifth_master.md#stage-10); NOT reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20) → **stage 20**. NPC: “Yes. The Ritual of Five Aspects lies lost among your kind. Long ago, a mortal scribe named Varnel served the Kazaul,…”

???+ note "Stage 30: 1 route"

    1. Talk to [Durnan the Hollow](../monsters/durnan.md) ([undertell_1_0](../maps/undertell_1_0.md)) → choose “Thank you, Durnan.” — **conditions:** reached stage 20 of [The fifth master](../quests/fifth_master.md#stage-20); NOT reached stage 40 of [The fifth master](../quests/fifth_master.md#stage-40) → **stage 30**. NPC: “If you find what he carried...bury it deep, far from here. The chains broke too late for us. Now...let me rest.”

???+ note "Stage 40: 1 route"

    1. Talk to [Kealwea](../monsters/sullengard_priest.md) ([sullengard_church](../maps/sullengard_church.md)) → choose “Ruins to the west, perhaps where Varnel perished.” — **conditions:** reached stage 91 of [mg2_exploded_star_nd (hidden flag)](../quests/mg2_exploded_star_nd.md#stage-91); reached stage 30 of [The fifth master](../quests/fifth_master.md#stage-30); NOT reached stage 50 of [The fifth master](../quests/fifth_master.md#stage-50) → **stage 40**. NPC: “If you seek that ritual, Remgard's church library is where your path leads.”

???+ note "Stage 50: 1 route"

    1. Talk to [Gwendolyn](../monsters/remgard_gwendolyn.md) ([remgard_church_basement](../maps/remgard_church_basement.md)) → choose “I'm searching for something called "The Ritual of Five Aspects". Have you ever heard of it?” — **conditions:** reached stage 40 of [The fifth master](../quests/fifth_master.md#stage-40); NOT reached stage 55 of [The fifth master](../quests/fifth_master.md#stage-55) → **stage 50**. NPC: “"The Ritual of Five Aspects"? No, I can't say that I have. The name sounds ominous though. You're welcome to look…”

???+ note "Stage 55: 1 route"

    1. walking into a blocked passage on [remgard_church_basement](../maps/remgard_church_basement.md) → choose “[Pull the box free.]” — **conditions:** reached stage 50 of [The fifth master](../quests/fifth_master.md#stage-50); NOT reached stage 55 of [The fifth master](../quests/fifth_master.md#stage-55) → **stage 55**; also gives 1× [Ancient locked box](../items/ancient_locked_box.md). NPC: “You lift out a small wooden box covered in dull runes. Its hinges are sealed shut, and there's no visible lock, only a…”

???+ note "Stage 58: 1 route"

    1. Talk to [Gwendolyn](../monsters/remgard_gwendolyn.md) ([remgard_church_basement](../maps/remgard_church_basement.md)) → choose “Do you know who might have the key?” — **conditions:** carry 1× [Ancient locked box](../items/ancient_locked_box.md); latest stage of [The fifth master](../quests/fifth_master.md#stage-55) is 55 → **stage 58**. NPC: “Hmm...the church keeps spare keys in the rectory upstairs, I think. You might ask Skylenar - he oversees most of…”

???+ note "Stage 60: 1 route"

    1. Talk to [Skylenar](../monsters/skylenar.md) ([remgard_church](../maps/remgard_church.md)) → choose “What kind of seals?” — **conditions:** reached stage 58 of [The fifth master](../quests/fifth_master.md#stage-58); carry 1× [Ancient locked box](../items/ancient_locked_box.md) → **stage 60**. NPC: “Relics from before the rise of the Shadow. Some were bound by the breath of dragonkind. Only a claw or fang from those…”

???+ note "Stage 65: 1 route"

    1. Talk to [Skylenar](../monsters/skylenar.md) ([remgard_church](../maps/remgard_church.md)) → choose “Where would I find a dragon in this age?” — **conditions:** reached stage 58 of [The fifth master](../quests/fifth_master.md#stage-58); carry 1× [Ancient locked box](../items/ancient_locked_box.md); NOT reached stage 50 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-50) → **stage 65**. NPC: “I have never seen one, and few alive have. I have heard the oldest priests whisper of strange remains found deep…”

???+ note "Stage 70: 2 routes"

    1. walking into a blocked passage on [white_house_basement](../maps/white_house_basement.md) → choose “Do you recognize it?” — **conditions:** carry 1× [Ancient locked box](../items/ancient_locked_box.md); reached stage 65 of [The fifth master](../quests/fifth_master.md#stage-65); NOT reached stage 72 of [The fifth master](../quests/fifth_master.md#stage-72) → **stage 70**. NPC: “This scent...old fire and fear. I remember this relic. It passed through the hands of a mortal named Varnel, long…”
    2. stepping on a trigger on [white_house_basement](../maps/white_house_basement.md) → choose “Do you recognize it?” — **conditions:** reached stage 45 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-45); NOT reached stage 50 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-50); carry 1× [Ancient locked box](../items/ancient_locked_box.md); reached stage 65 of [The fifth master](../quests/fifth_master.md#stage-65); NOT reached stage 72 of [The fifth master](../quests/fifth_master.md#stage-72) → **stage 70**. NPC: “This scent...old fire and fear. I remember this relic. It passed through the hands of a mortal named Varnel, long…”

???+ note "Stage 72: 2 routes"

    1. walking into a blocked passage on [white_house_basement](../maps/white_house_basement.md) → choose “What do you mean?” — **conditions:** carry 1× [Ancient locked box](../items/ancient_locked_box.md); reached stage 65 of [The fifth master](../quests/fifth_master.md#stage-65); NOT reached stage 72 of [The fifth master](../quests/fifth_master.md#stage-72) → **stage 72**; also gives 1× [Dragon claw](../items/dragon_claw_key.md). NPC: “I lend you this fragment of me, not for greed but for truth. Take this claw. Its edge remembers the heat of the first…”
    2. stepping on a trigger on [white_house_basement](../maps/white_house_basement.md) → choose “What do you mean?” — **conditions:** reached stage 45 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-45); NOT reached stage 50 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-50); carry 1× [Ancient locked box](../items/ancient_locked_box.md); reached stage 65 of [The fifth master](../quests/fifth_master.md#stage-65); NOT reached stage 72 of [The fifth master](../quests/fifth_master.md#stage-72) → **stage 72**; also gives 1× [Dragon claw](../items/dragon_claw_key.md). NPC: “I lend you this fragment of me, not for greed but for truth. Take this claw. Its edge remembers the heat of the first…”

???+ note "Stage 75: 1 route"

    1. stepping on a trigger on [white_house_basement](../maps/white_house_basement.md) → choose “Yes, let's do this.” — **conditions:** latest stage of [The fifth master](../quests/fifth_master.md#stage-72) is 72; carry 1× [Dragon claw](../items/dragon_claw_key.md); carry 1× [Ancient locked box](../items/ancient_locked_box.md); hand over 1× [Ancient locked box](../items/ancient_locked_box.md) → **stage 75**; also gives 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md). NPC: “After placing the claw in the keyhole, the box lights up red and crumbles in your hand. Revealing an ancient parcment…”

???+ note "Stage 78: 3 routes"

    1. Talk to [Zaroth](../monsters/zaroth.md) ([undertell_4_00](../maps/undertell_4_00.md)) → choose “Thalen? What will he do with it?” — **conditions:** carry 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md) → **stage 78**; also sets stage 7 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-7). NPC: “He will guide your unlearned hands. He alone can draw the pattern that binds the Five. Without him, the ritual is only…”
    2. Talk to [Morvath](../monsters/morvath.md) ([undertell_00](../maps/undertell_00.md)) → choose “Thalen? What will he do with it?” — **conditions:** carry 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md) → **stage 78**; also sets stage 7 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-7). NPC: “He will guide your unlearned hands. He alone can draw the pattern that binds the Five. Without him, the ritual is only…”
    3. Talk to [Vaelzahr](../monsters/vaelzahr.md) ([undertell_7_00](../maps/undertell_7_00.md)) → choose “Thalen? What will he do with it?” — **conditions:** carry 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md) → **stage 78**; also sets stage 7 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-7). NPC: “He will guide your unlearned hands. He alone can draw the pattern that binds the Five. Without him, the ritual is only…”

???+ note "Stage 80: 1 route"

    1. Talk to [Thalen](../monsters/thalen.md) ([undertell_3_lava_00](../maps/undertell_3_lava_00.md)) → choose “Then I will take it to the shrine.” — **conditions:** carry 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md); hand over 1× [The Ritual of Five Aspects](../items/ancient_kazaul_ritual.md) → **stage 80**; also spawns monsters on undertell_5, sets stage 7 of [hidden_undertell (hidden flag)](../quests/undertell_hidden.md#stage-7). NPC: “No. Give it to me and I will give it to the kin. You have done what none of the living could. Do not fail now, mortal.…”

???+ note "Stage 85: 2 routes"

    1. Talk to [Anavrin](../monsters/anavrin.md) ([undertell_5](../maps/undertell_5.md)) → the conversation leads here automatically — **conditions:** reached stage 80 of [The fifth master](../quests/fifth_master.md#stage-80); NOT reached stage 85 of [The fifth master](../quests/fifth_master.md#stage-85) → **stage 85**. NPC: “You have undone silence itself, mortal. The rift shall open again, and through it we will see our dominion restored.”
    2. Talk to [Kazaul acolyte](../monsters/kazaul_acolyte.md) ([undertell_5](../maps/undertell_5.md)) → choose “What...what have I done?” → **stage 85**. NPC: “You have undone silence itself, mortal. The rift shall open again, and through it we will see our dominion restored.”

???+ note "Stage 90: 1 route"

    1. Talk to [Anavrin](../monsters/anavrin.md) ([undertell_5](../maps/undertell_5.md)) → choose “You lie. The Shadow is not Kazaul.” — **conditions:** NOT reached stage 90 of [The fifth master](../quests/fifth_master.md#stage-90) → **stage 90**. NPC: “Perhaps. Or perhaps you already know the truth, but your heart fears its shape. Leave now, child of dust. The Fifth is…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.18](../versions/0.8.18.md) | Added<br>Dialogue: 16 lines added |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fifth_master.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fifth_master.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fifth_master.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fifth_master.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=fifth_master.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `fifth_master` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 30, 40, 50, 55, 58, 60, 65, 70, 72, 75, 78, 80, 85, 90 |
    | Dialogue nodes setting stages | 10: `the_fifth_master_10`, 20: `the_fifth_master_20`, 30: `undertell_ghost_durnan_50`, 40: `sullengard_kealwea_kazaul_4`, 50: `gwendolyn_kazaul_10`, 55: `remgard_library_shelf_search_20`, 58: `gwendolyn_kazaul_locked_box_20`, 60: `skylenar_kazaul_20`, 65: `skylenar_kazaul_30`, 70: `dragon_box_20`, 72: `dragon_box_40`, 75: `wh_basement_unlock_box_20`, 78: `masters_send_to_thalen_20`, 80: `thalen_receives_ritual_30`, 85: `anavrin_resurrection_30`, 90: `anavrin_revelation_40` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
