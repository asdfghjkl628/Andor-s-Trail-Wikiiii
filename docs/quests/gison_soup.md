# Delicious soup

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `gison_soup` |
| **In journal** | Yes |
| **Stages** | 17 (completes at 50, 100, 110) |
| **Started by** | [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)), [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) |
| **NPCs involved** | [Alaun](../monsters/alaun.md), [Gison](../monsters/gison.md), [Nimael](../monsters/nimael.md) |
| **Locations** | [fallhaven_alaun](../maps/fallhaven_alaun.md), [mywild20_houseleft](../maps/mywild20_houseleft.md) |
| **Total XP** | 250 |
| **Related quests** | 3 |

</div>

## Overview

> In a hut southwest from Fallhaven I met Alaun. He asked me to bring him some of the delicious soup made by Gison with forest mushrooms. Gison's house lies to the south.

## Prerequisites to start

Start with [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)). Required:

- NOT reached stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Alaun soup rewards (hidden flag)](alaun_soup_reward.md#stage-10) | stage 10 reached, for stages 30, 35 here |
| Requires | [Alaun soup rewards (hidden flag)](alaun_soup_reward.md#stage-15) | stage 15 reached, for stages 30, 35 here |
| Requires | [Alaun soup rewards (hidden flag)](alaun_soup_reward.md#stage-20) | stage 20 reached, for stages 30, 35 here |
| Unlocks | [Alaun soup rewards (hidden flag)](alaun_soup_reward.md#stage-11) | stage 11 there needs stage 20 here |
| Unlocks | [Alaun soup rewards (hidden flag)](alaun_soup_reward.md#stage-16) | stage 16 there needs stage 20 here |
| Unlocks | [Alaun soup rewards (hidden flag)](alaun_soup_reward.md#stage-21) | stage 21 there needs stage 20 here |
| Unlocks | [Alaun soup rewards (hidden flag)](alaun_soup_reward.md#stage-30) | stage 30 there needs stages 10, 50 here |
| Unlocks | [A raid for a cookbook](gison_cookbook.md#stage-10) | stage 10 there needs stage 100 here |
| Unlocks | [A raid for a cookbook](gison_cookbook.md#stage-15) | stage 15 there needs stage 100 here |
| Unlocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-20) | stage 20 there needs stage 120 here |
| Blocks | [Alaun soup rewards (hidden flag)](alaun_soup_reward.md#stage-10) | reaching stage 10 here closes stage 10 there |
| Blocks | [Alaun soup rewards (hidden flag)](alaun_soup_reward.md#stage-11) | reaching stages 30, 50 here closes stage 11 there |
| Blocks | [Alaun soup rewards (hidden flag)](alaun_soup_reward.md#stage-15) | reaching stage 10 here closes stage 15 there |
| Blocks | [Alaun soup rewards (hidden flag)](alaun_soup_reward.md#stage-16) | reaching stages 30, 50 here closes stage 16 there |
| Blocks | [Alaun soup rewards (hidden flag)](alaun_soup_reward.md#stage-20) | reaching stage 10 here closes stage 20 there |
| Blocks | [Alaun soup rewards (hidden flag)](alaun_soup_reward.md#stage-21) | reaching stages 30, 50 here closes stage 21 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | In a hut southwest from Fallhaven I met Alaun. He asked me to bring him some of the delicious soup made by Gison with forest mushrooms. Gison's house lies to the south. | [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) | – | sets stage 10 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-10)<br>sets stage 15 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-15)<br>sets stage 20 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-20) |
| <span id="stage-20"></span>20 | I found Gison's house and should deliver the soup to Alaun while it is hot. | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | stage 10, stage 30 | gives 1× [Gison's mushroom soup](../items/gison_soup.md)<br>starts timer “gison_soup” |
| <span id="stage-22"></span>22 | Gison gave me a new soup for 5 gold. | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | pay 5 gold, stage 20 | gives 1× [Gison's mushroom soup](../items/gison_soup.md)<br>starts timer “gison_soup” |
| <span id="stage-24"></span>24 | Gison gave me a new soup for 50 gold. | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | pay 50 gold, stage 20, stage 22 | gives 1× [Gison's mushroom soup](../items/gison_soup.md)<br>starts timer “gison_soup” |
| <span id="stage-26"></span>26 | Gison gave me a new soup for 500 gold. | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | pay 500 gold, stage 20, stage 24 | gives 1× [Gison's mushroom soup](../items/gison_soup.md)<br>starts timer “gison_soup” |
| <span id="stage-28"></span>28 | Gison gave me a new soup for 5000 gold. I should really go to Alaun now. | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | pay 5,000 gold, stage 20, stage 26 | gives 1× [Gison's mushroom soup](../items/gison_soup.md)<br>starts timer “gison_soup” |
| <span id="stage-30"></span>30 | Alaun received the soup. I should take the empty bottle back to Gison. | [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) | hand over 1× [Gison's mushroom soup](../items/gison_soup.md), stage 20 | gives 10× [Gold coins](../items/gold.md)<br>gives 5× [Bread](../items/bread.md)<br>gives 1× [Empty bottle](../items/bottle_empty.md)<br>sets stage 11 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-11)<br>gives 15× [Gold coins](../items/gold.md)<br>sets stage 16 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-16)<br>gives 20× [Gold coins](../items/gold.md)<br>sets stage 21 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-21) |
| <span id="stage-35"></span>35 | Alaun told me that Nimael also makes soup. | [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) | hand over 1× [Gison's mushroom soup](../items/gison_soup.md), stage 20 | gives 10× [Gold coins](../items/gold.md)<br>gives 5× [Bread](../items/bread.md)<br>gives 1× [Empty bottle](../items/bottle_empty.md)<br>sets stage 11 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-11)<br>gives 15× [Gold coins](../items/gold.md)<br>sets stage 16 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-16)<br>gives 20× [Gold coins](../items/gold.md)<br>sets stage 21 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-21) |
| <span id="stage-40"></span>40 | Gison thanked me for bringing the empty bottle back to him. | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | hand over 1× [Empty bottle](../items/bottle_empty.md), stage 20, stage 30 | 50 XP |
| <span id="stage-50"></span>50 | I spent 5555 gold on buying mushroom soup! Am I crazy?  There is no soup left for Alaun now. **(completes quest)** | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | stage 20, stage 28 | – |
| <span id="stage-60"></span>60 | Gison insisted his soup is better than Nimael's. | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | stage 30, stage 35, stage 40 | – |
| <span id="stage-70"></span>70 | Nimael insisted her soup is better than Gison's. | [Nimael](../monsters/nimael.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | stage 35 | – |
| <span id="stage-80"></span>80 | Gison gave me a taste of both soups. | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | stage 30, stage 35, stage 40, stage 70 | – |
| <span id="stage-90"></span>90 | Nimael gave me a taste of both soups. | [Nimael](../monsters/nimael.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | stage 35, stage 60 | – |
| <span id="stage-100"></span>100 | Gison said he would talk to Nimael about selling both soups in Fallhaven. **(completes quest)** | [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | stage 30, stage 35, stage 40, stage 70 | 100 XP<br>gives 2× [Gison's mushroom soup](../items/gison_soup.md)<br>starts timer “del_soup” |
| <span id="stage-110"></span>110 | Nimael said she would talk to Gison about selling both soups in Fallhaven. **(completes quest)** | [Nimael](../monsters/nimael.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | stage 35, stage 60 | 100 XP<br>gives 2× [Nimael's vegetable soup](../items/nimael_soup.md)<br>starts timer “del_soup” |
| <span id="stage-120"></span>120 | Nimael and Gison have been successful in selling more soup in Fallhaven by cooperating and creating more recipes. | [Nimael](../monsters/nimael.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) | – | – |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 3 routes"

    1. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “Sounds easy, I'll do it!” — **conditions:** NOT reached stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10) → **stage 10**; also sets stage 10 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-10). NPC: “That's really nice of you.”
    2. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “Sounds good. I will do it.” — **conditions:** NOT reached stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10) → **stage 10**; also sets stage 15 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-15). NPC: “That's nice of you.”
    3. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “Sounds good. I will do it.” — **conditions:** NOT reached stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10) → **stage 10**; also sets stage 20 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-20). NPC: “OK, please bring it hot!”

???+ note "Stage 20: 1 route"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “Alaun sent me to bring him some of your delicious soup.” — **conditions:** reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); reached stage 10 of [Delicious soup](../quests/gison_soup.md#stage-10); NOT reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20) → **stage 20**; also gives 1× [Gison's mushroom soup](../items/gison_soup.md), starts timer “gison_soup”. NPC: “Here you go. [He gives you a container with the soup.]”

???+ note "Stage 22: 1 route"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “Yes, ok. Here are 5 gold pieces.” — **conditions:** reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); NOT carry 1× [Gison's mushroom soup](../items/gison_soup.md); NOT reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); pay 5 gold → **stage 22**; also gives 1× [Gison's mushroom soup](../items/gison_soup.md), starts timer “gison_soup”. NPC: “[Gison gives you a new bottle with hot soup.] Here you go.”

???+ note "Stage 24: 1 route"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “Yes, ok. Here are 50 gold pieces.” — **conditions:** reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); NOT carry 1× [Gison's mushroom soup](../items/gison_soup.md); NOT reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); reached stage 22 of [Delicious soup](../quests/gison_soup.md#stage-22); pay 50 gold → **stage 24**; also gives 1× [Gison's mushroom soup](../items/gison_soup.md), starts timer “gison_soup”. NPC: “[Gison gives you a new bottle with hot soup.] Here you go.”

???+ note "Stage 26: 1 route"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “Yes, ok. Here are 500 gold pieces.” — **conditions:** reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); NOT carry 1× [Gison's mushroom soup](../items/gison_soup.md); NOT reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); reached stage 24 of [Delicious soup](../quests/gison_soup.md#stage-24); pay 500 gold → **stage 26**; also gives 1× [Gison's mushroom soup](../items/gison_soup.md), starts timer “gison_soup”. NPC: “[Gison gives you a new bottle with hot soup.] Here you go.”

???+ note "Stage 28: 1 route"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “Yes, ok. Here are 5,000 gold pieces.” — **conditions:** reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); NOT carry 1× [Gison's mushroom soup](../items/gison_soup.md); NOT reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); reached stage 26 of [Delicious soup](../quests/gison_soup.md#stage-26); pay 5,000 gold → **stage 28**; also gives 1× [Gison's mushroom soup](../items/gison_soup.md), starts timer “gison_soup”. NPC: “[Gison gives you a new bottle with hot soup.] Here you go. I can't give you more. Take this one to Alaun now, greedy…”

???+ note "Stage 30: 3 routes"

    1. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “Gison gave me some of his soup.” — **conditions:** reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); NOT reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); NOT reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50); reached stage 10 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-10); hand over 1× [Gison's mushroom soup](../items/gison_soup.md) → **stage 30**; also gives 10× [Gold coins](../items/gold.md), gives 5× [Bread](../items/bread.md), gives 1× [Empty bottle](../items/bottle_empty.md), sets stage 11 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-11). NPC: “Here is the money I promised you. And as a bonus I will give you some of this bread. Next time I will buy Nimael's soup.”
    2. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “Gison gave me some of his soup.” — **conditions:** reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); NOT reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); NOT reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50); reached stage 15 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-15); hand over 1× [Gison's mushroom soup](../items/gison_soup.md) → **stage 30**; also gives 15× [Gold coins](../items/gold.md), gives 1× [Empty bottle](../items/bottle_empty.md), sets stage 16 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-16). NPC: “Here is the money I promised you. Next time I will buy Nimael's soup.”
    3. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “Gison gave me some of his soup.” — **conditions:** reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); NOT reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); NOT reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50); reached stage 20 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-20); hand over 1× [Gison's mushroom soup](../items/gison_soup.md) → **stage 30**; also gives 20× [Gold coins](../items/gold.md), gives 1× [Empty bottle](../items/bottle_empty.md), sets stage 21 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-21). NPC: “Here is the money I promised you. Next time I will buy Nimael's soup.”

???+ note "Stage 35: 3 routes"

    1. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “Gison gave me some of his soup.” — **conditions:** reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); NOT reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); NOT reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50); reached stage 10 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-10); hand over 1× [Gison's mushroom soup](../items/gison_soup.md) → **stage 35**; also gives 10× [Gold coins](../items/gold.md), gives 5× [Bread](../items/bread.md), gives 1× [Empty bottle](../items/bottle_empty.md), sets stage 11 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-11). NPC: “Here is the money I promised you. And as a bonus I will give you some of this bread. Next time I will buy Nimael's soup.”
    2. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “Gison gave me some of his soup.” — **conditions:** reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); NOT reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); NOT reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50); reached stage 15 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-15); hand over 1× [Gison's mushroom soup](../items/gison_soup.md) → **stage 35**; also gives 15× [Gold coins](../items/gold.md), gives 1× [Empty bottle](../items/bottle_empty.md), sets stage 16 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-16). NPC: “Here is the money I promised you. Next time I will buy Nimael's soup.”
    3. Talk to [Alaun](../monsters/alaun.md) ([fallhaven_alaun](../maps/fallhaven_alaun.md)) → choose “Gison gave me some of his soup.” — **conditions:** reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); NOT reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); NOT reached stage 50 of [Delicious soup](../quests/gison_soup.md#stage-50); reached stage 20 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-20); hand over 1× [Gison's mushroom soup](../items/gison_soup.md) → **stage 35**; also gives 20× [Gold coins](../items/gold.md), gives 1× [Empty bottle](../items/bottle_empty.md), sets stage 21 of [Alaun soup rewards (hidden flag)](../quests/alaun_soup_reward.md#stage-21). NPC: “Here is the money I promised you. Next time I will buy Nimael's soup.”

???+ note "Stage 40: 2 routes"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “Yes I have. Here is it. [You give Gison the empty bottle.]” — **conditions:** reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); latest stage of [Delicious soup](../quests/gison_soup.md#stage-30) is 30; hand over 1× [Empty bottle](../items/bottle_empty.md) → **stage 40**. NPC: “Oh good. Thanks.”
    2. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “I want to return your bottle.” — **conditions:** reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); hand over 1× [Empty bottle](../items/bottle_empty.md) → **stage 40**. NPC: “Thank you.”

???+ note "Stage 50: 1 route"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “No ... ehm ... Maybe you could give me some more?” — **conditions:** reached stage 20 of [Delicious soup](../quests/gison_soup.md#stage-20); NOT carry 1× [Gison's mushroom soup](../items/gison_soup.md); NOT reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); reached stage 28 of [Delicious soup](../quests/gison_soup.md#stage-28) → **stage 50**. NPC: “I'm sorry for Alaun. I guess he has to get some himself.”

???+ note "Stage 60: 1 route"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “Alaun told me that your wife also makes very good soup.” — **conditions:** reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); reached stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35); NOT reached stage 100 of [Delicious soup](../quests/gison_soup.md#stage-100); NOT reached stage 110 of [Delicious soup](../quests/gison_soup.md#stage-110); reached stage 40 of [Delicious soup](../quests/gison_soup.md#stage-40) → **stage 60**. NPC: “Yes, but it is not as good as mine.”

???+ note "Stage 70: 1 route"

    1. Talk to [Nimael](../monsters/nimael.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “Alaun told me that you also make very good soup.” — **conditions:** reached stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35); NOT reached stage 100 of [Delicious soup](../quests/gison_soup.md#stage-100); NOT reached stage 110 of [Delicious soup](../quests/gison_soup.md#stage-110) → **stage 70**. NPC: “Yes. Vegetables with forest herbs. It is even better than my husband's mushroom soup.”

???+ note "Stage 80: 1 route"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “Your wife disagrees.” — **conditions:** reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); reached stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35); NOT reached stage 100 of [Delicious soup](../quests/gison_soup.md#stage-100); NOT reached stage 110 of [Delicious soup](../quests/gison_soup.md#stage-110); reached stage 40 of [Delicious soup](../quests/gison_soup.md#stage-40); reached stage 70 of [Delicious soup](../quests/gison_soup.md#stage-70) → **stage 80**. NPC: “Well, here is a small taste of mine, and a small taste of hers. I am sure you will agree with me.”

???+ note "Stage 90: 1 route"

    1. Talk to [Nimael](../monsters/nimael.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “Your husband disagrees.” — **conditions:** reached stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35); NOT reached stage 100 of [Delicious soup](../quests/gison_soup.md#stage-100); NOT reached stage 110 of [Delicious soup](../quests/gison_soup.md#stage-110); reached stage 60 of [Delicious soup](../quests/gison_soup.md#stage-60) → **stage 90**. NPC: “Well, here is a small taste of mine, and a small taste of his. I am sure you will agree with me.”

???+ note "Stage 100: 1 route"

    1. Talk to [Gison](../monsters/gison.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “I think they are both good. One is not better than the other, just different. Different people have…” — **conditions:** reached stage 30 of [Delicious soup](../quests/gison_soup.md#stage-30); reached stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35); NOT reached stage 100 of [Delicious soup](../quests/gison_soup.md#stage-100); NOT reached stage 110 of [Delicious soup](../quests/gison_soup.md#stage-110); reached stage 40 of [Delicious soup](../quests/gison_soup.md#stage-40); reached stage 70 of [Delicious soup](../quests/gison_soup.md#stage-70) → **stage 100**; also gives 2× [Gison's mushroom soup](../items/gison_soup.md), starts timer “del_soup”. NPC: “For a kid, that's a very insightful comment. I will talk to my wife about how we can better sell both soups to the…”

???+ note "Stage 110: 1 route"

    1. Talk to [Nimael](../monsters/nimael.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → choose “I think they are both good. One is not better than the other, just different. Different people have…” — **conditions:** reached stage 35 of [Delicious soup](../quests/gison_soup.md#stage-35); NOT reached stage 100 of [Delicious soup](../quests/gison_soup.md#stage-100); NOT reached stage 110 of [Delicious soup](../quests/gison_soup.md#stage-110); reached stage 60 of [Delicious soup](../quests/gison_soup.md#stage-60) → **stage 110**; also gives 2× [Nimael's vegetable soup](../items/nimael_soup.md), starts timer “del_soup”. NPC: “For a kid, that's a very insightful comment. I will talk to my husband about how we can better sell both soups to the…”

???+ note "Stage 120: 1 route"

    1. Talk to [Nimael](../monsters/nimael.md) ([mywild20_houseleft](../maps/mywild20_houseleft.md)) → the conversation leads here automatically — **conditions:** 1500 rounds passed since timer “del_soup”; NOT reached stage 120 of [Delicious soup](../quests/gison_soup.md#stage-120) → **stage 120**. NPC: “Thanks to your advice, we have been successful selling more soup to the townsfolk in Fallhaven. We have even…”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.7.13](../versions/0.7.13.md) | Added<br>Dialogue: 21 lines added |
| [v0.7.15](../versions/0.7.15.md) | Dialogue: 1 line changed<br>· text: “Thanks to your advice, we have been successful selling more soup to t…” → “Thanks to your advice, we have been successful selling more soup to t…” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=gison_soup.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=gison_soup.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=gison_soup.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=gison_soup.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=gison_soup.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `gison_soup` |
    | showInLog | 1 |
    | Stage IDs | 10, 20, 22, 24, 26, 28, 30, 35, 40, 50, 60, 70, 80, 90, 100, 110, 120 |
    | Dialogue nodes setting stages | 10: `alaun_startquest10`, 10: `alaun_startquest15`, 10: `alaun_startquest20`, 20: `gison_p1_10_3`, 22: `gison_p1_20_nosoup_5go`, 24: `gison_p1_20_nosoup_50go`, 26: `gison_p1_20_nosoup_500go`, 28: `gison_p1_20_nosoup_5000go`, 30: `alaun_return10`, 30: `alaun_return15`, 30: `alaun_return20`, 35: `alaun_return10`, 35: `alaun_return15`, 35: `alaun_return20`, 40: `gison_p1_20_3`, 40: `gison_p1_30_1`, 50: `gison_p1_20_nosoup_endquest`, 60: `gison_arg_10`, 70: `nimael_arg_10`, 80: `gison_arg_20`, 90: `nimael_arg_20`, 100: `gison_arg_30`, 110: `nimael_arg_30`, 120: `nimael_b2` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
