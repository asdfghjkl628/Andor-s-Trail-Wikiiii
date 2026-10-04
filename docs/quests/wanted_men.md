# Wanted men

<div class="infobox" markdown>

| | |
|---|---|
| **Quest ID** | `wanted_men` |
| **In journal** | Yes |
| **Stages** | 19 (completes at 57, 70, 80) |
| **Started by** | stepping on a trigger on [aidem_camp](../maps/aidem_camp.md) |
| **NPCs involved** | [Defy](../monsters/aidem_camp_defy.md), [Defy](../monsters/defy_wild6house.md), [Defy](../monsters/aidem_base_defy.md), [Rennik](../monsters/wild6_house_thief.md), [Troublemaker](../monsters/troublemaker.md) |
| **Locations** | [aidem_base_2](../maps/aidem_base_2.md), [aidem_camp](../maps/aidem_camp.md), [fallhaven_derelict2](../maps/fallhaven_derelict2.md), [fallhaven_derelict2_t](../maps/fallhaven_derelict2_t.md) |
| **Total XP** | 51,385 |
| **Related quests** | 6 |

</div>

## Overview

> Off the main road, southeast of Deebo's Orchard, I've stumbled across a group of sketchy looking men with familiar voices.

## Prerequisites to start

Start with stepping on a trigger on [aidem_camp](../maps/aidem_camp.md). Required:

- NOT reached stage 10 of [Wanted men](../quests/wanted_men.md#stage-10)
- reached stage 39 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-39)


<p class="verified">Verified against v0.8.18 quest and dialogue data.</p>
## Dependencies

*Quest logic, read from the dialogue conditions.*

| Relationship | Quest | Detail |
|---|---|---|
| Requires | [Thief apprentice](Thieves01.md#stage-60) | stage 60 reached, for stages 45, 50, 55, 65, 80 here |
| Requires | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-39) | stage 39 reached, for stage 10 here |
| Requires | [Sutdove_nondisplay (hidden flag)](sutdover_hidden.md#stage-2) | stage 2 reached, for stage 57 here |
| Unlocks | [laeroth_nondisplay (hidden flag)](laeroth_nondisplay.md#stage-107) | stage 107 there needs stage 80 here |
| Unlocks | [Placeholder for hidden quest stages (not displayed) (hidden flag)](nondisplay.md#stage-60) | stage 60 there needs stage 77 here |
| Unlocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-40) | stage 40 there needs stage 57 here |
| Unlocks | [Troubling times](troubling_times.md#stage-10) | stage 10 there needs stages 70, 77, 80 here |
| Unlocks | [Troubling times](troubling_times.md#stage-20) | stage 20 there needs stage 70 here |
| Unlocks | [Troubling times](troubling_times.md#stage-30) | stage 30 there needs stages 77, 80 here |
| Unlocks | [Troubling times](troubling_times.md#stage-40) | stage 40 there needs stage 80 here |
| Unlocks | [Troubling times](troubling_times.md#stage-50) | stage 50 there needs stage 80 here |
| Blocks | [sullengard_nondisplay (hidden flag)](sullengard_hidden.md#stage-41) | reaching stage 15 here closes stage 41 there |
| Blocks | [Sutdove_nondisplay (hidden flag)](sutdover_hidden.md#stage-2) | reaching stage 57 here closes stage 2 there |

## Stages

| Stage | Journal entry | Triggered by | Needs | Rewards |
|---|---|---|---|---|
| <span id="stage-10"></span>10 | Off the main road, southeast of Deebo's Orchard, I've stumbled across a group of sketchy looking men with familiar voices.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Aidem camp](../maps/aidem_camp.md).</span> | stepping on a trigger on [aidem_camp](../maps/aidem_camp.md) | – | – |
| <span id="stage-15"></span>15 | The sketchy looking men with familiar voices turned out to be the Aidem thieves from Sullengard. They were hiding-out in the woods.<br><span class="qnote">⚡ A scripted event can now trigger on [Aidem camp](../maps/aidem_camp.md).</span><br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Aidem camp](../maps/aidem_camp.md).</span> | stepping on a trigger on [aidem_camp](../maps/aidem_camp.md) | stage 10 | – |
| <span id="stage-20"></span>20 | While speaking with Defy, I've learned the he and his men have a grudge against the Thieves' Guild and they want to "hit them where it really hurts". Whatever that means. | [Defy](../monsters/aidem_camp_defy.md) ([aidem_camp](../maps/aidem_camp.md)) | – | – |
| <span id="stage-25"></span>25 | Defy has revealed the location of the Thieves' Guild's vault of treasure - an underground storage unit accessible from the vacant house south of Fallhaven. | [Defy](../monsters/aidem_camp_defy.md) ([aidem_camp](../maps/aidem_camp.md)) | – | – |
| <span id="stage-30"></span>30 | Defy has asked me to convince Troublemaker to let me borrow the key long enough that I can bring it back to Defy.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Wild6 house](../maps/wild6_house.md).</span><br><span class="qnote">🗺️ Part of [Wild6 house](../maps/wild6_house.md) visibly changes.</span> | [Defy](../monsters/aidem_camp_defy.md) ([aidem_camp](../maps/aidem_camp.md)) | – | – |
| <span id="stage-35"></span>35 | Defy has agreed to pay me 20 percent of the looted Thieves' Guild treasure if I get the key from Troublemaker and hand it over to him. | [Defy](../monsters/aidem_camp_defy.md) ([aidem_camp](../maps/aidem_camp.md)) | – | – |
| <span id="stage-40"></span>40 | Defy has instructed me to bring Troublemaker's key to him at their new hideout located west of the Sutdover River, where the rail tracks end.<br><span class="qnote">🔓 You can finally access a previously blocked area on [Galmore 10a](../maps/galmore_10a.md).</span> | [Defy](../monsters/aidem_camp_defy.md) ([aidem_camp](../maps/aidem_camp.md)) | – | removes monsters from aidem_camp<br>spawns monsters on aidem_base_2 |
| <span id="stage-45"></span>45 | I have talked my way into acquiring the Thieves' Guild's vault key from Troublemaker, but I must return it to him quickly after I am done with it. | [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 40 | gives [Thieves' vault key](../items/thieves_vault_key.md) |
| <span id="stage-50"></span>50 | I told Troublemaker all that I knew about Defy, his men, and the "Lost Traveler", Alaric and how they hired me to help rob the Thieves' Guild. | [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | – | – |
| <span id="stage-55"></span>55 | Troublemaker has asked me to help him trap Defy by providing Defy with a fake key. When Defy arrives at the secret vault, the Guild members will be waiting for him. | [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | stage 50 | gives [Fake Thieve's Guild vault key](../items/thieves_vault_key_fake.md) |
| <span id="stage-56"></span>56 | I gave Defy the fake version of the vault key that Troublemaker gave me. In return, Defy has given me a fake version of Troublemaker's vault key and has instructed me to return it to Troublemaker. Defy then told me to report back to the vault in order to collect my share of the gold. He has no idea that the key I gave him is a fake. | [Defy](../monsters/aidem_base_defy.md) ([aidem_base_2](../maps/aidem_base_2.md)) | hand over 1× [Fake Thieve's Guild vault key](../items/thieves_vault_key_fake.md) | gives [Aidem fake vault key](../items/aidem_fake_vault_key.md)<br>removes monsters from aidem_base_2<br>spawns monsters on wild6_house |
| <span id="stage-57"></span>57 | I have reported back to the vacant house and I met Rennik there. He informed me that the Thieves' Guild has apprehended all five men and that they are now in the Guild jail. **(completes quest)** | [Rennik](../monsters/wild6_house_thief.md) ([wild6_house](../maps/wild6_house.md)) | – | 19,797 XP<br>spawns monsters on guildbrig2 |
| <span id="stage-60"></span>60 | Defy has given me a fake version of Troublemaker's vault key and has instructed me to return it to Troublemaker. Then I should report back to the vault in order to collect my share of the gold. | [Defy](../monsters/aidem_base_defy.md) ([aidem_base_2](../maps/aidem_base_2.md)) | hand over 1× [Thieves' vault key](../items/thieves_vault_key.md), stage 45 | gives [Aidem fake vault key](../items/aidem_fake_vault_key.md) |
| <span id="stage-65"></span>65 | I have given the fake Aidem key to Troublemaker as a replacement for the real vault key. | [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | hand over 1× [Aidem fake vault key](../items/aidem_fake_vault_key.md), stage 60 | removes monsters from aidem_base_2<br>spawns monsters on wild6_house<br>faction “factionCountThieves” set to -8 |
| <span id="stage-70"></span>70 | I reported back to Defy and he rewarded me with 25000 gold. **(completes quest)** | [Defy](../monsters/defy_wild6house.md) ([wild6_house](../maps/wild6_house.md)) | stage 65 | 14,700 XP<br>gives [Gold coins](../items/gold.md) |
| <span id="stage-75"></span>75 | I told Defy that I was keeping the key for myself and plan to loot the Thieves' Guild's vault myself. A fight ensued. | [Defy](../monsters/aidem_base_defy.md) ([aidem_base_2](../maps/aidem_base_2.md)) | carry 1× [Thieves' vault key](../items/thieves_vault_key.md), stage 45 | – |
| <span id="stage-76"></span>76 | I have killed Defy, his three henchmen and Alaric. I really should go back to Fallhaven and talk to Troublemaker again.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Aidem base 2](../maps/aidem_base_2.md).</span> | stepping on a trigger on [aidem_base_2](../maps/aidem_base_2.md) | – | – |
| <span id="stage-77"></span>77 | I've unlocked the hatch leading to the vault. It's time to head down.<br><span class="qnote">👣 Reached by stepping onto a trigger spot on [Wild6 house](../maps/wild6_house.md).</span><br><span class="qnote">🗺️ Part of [Wild6 house](../maps/wild6_house.md) visibly changes.</span> | stepping on a trigger on [wild6_house](../maps/wild6_house.md) | carry 1× [Thieves' vault key](../items/thieves_vault_key.md), stage 76 | changes map wild6_house |
| <span id="stage-80"></span>80 | I informed Troublemaker that Defy and his men are now dead. **(completes quest)** | [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) | hand over 1× [Defy's ring](../items/defy_ring.md), hand over 1× [Grabby's ring](../items/grabby_ring.md), hand over 1× [Greedy's ring](../items/greedy_ring.md), hand over 1× [Zachlanny ring](../items/zachlanny_ring.md), stage 76 | 16,888 XP<br>faction “factionCountThieves” set to 3 |

<p class="verified">Verified against v0.8.18 quest, dialogue and map data.</p>
## How each stage is reached

*Every dialogue route found in the game data, including alternatives that end up in the same place. "Conditions" are everything checked along that dialogue path. To test a specific situation, open the NPC's page and use its **Dialogue simulator**.*

???+ note "Stage 10: 1 route"

    1. stepping on a trigger on [aidem_camp](../maps/aidem_camp.md) → the conversation leads here automatically — **conditions:** NOT reached stage 10 of [Wanted men](../quests/wanted_men.md#stage-10); reached stage 39 of [sullengard_nondisplay (hidden flag)](../quests/sullengard_hidden.md#stage-39) → **stage 10**. NPC: “I heard nothing. Greedy, you need to relax. Here, have a Bandit's Brew.”

???+ note "Stage 15: 1 route"

    1. stepping on a trigger on [aidem_camp](../maps/aidem_camp.md) → choose “Wait a minute, I recognize those guys.” — **conditions:** latest stage of [Wanted men](../quests/wanted_men.md#stage-10) is 10 → **stage 15**. NPC: “Ugh. Whatever.”

???+ note "Stage 20: 2 routes"

    1. Talk to [Defy](../monsters/aidem_camp_defy.md) ([aidem_camp](../maps/aidem_camp.md)) → choose “Who's that?” → **stage 20**. NPC: “I'm talking about the Thieves' Guild.”
    2. Talk to [Defy](../monsters/aidem_camp_defy.md) ([aidem_camp](../maps/aidem_camp.md)) → choose “The Thieves' Guild?” → **stage 20**. NPC: “Exactly!”

???+ note "Stage 25: 1 route"

    1. Talk to [Defy](../monsters/aidem_camp_defy.md) ([aidem_camp](../maps/aidem_camp.md)) → choose “Of course I am.” → **stage 25**. NPC: “The entrance to it is found inside that house. It's hidden and secured. You will need to find the passage that leads…”

???+ note "Stage 30: 1 route"

    1. Talk to [Defy](../monsters/aidem_camp_defy.md) ([aidem_camp](../maps/aidem_camp.md)) → choose “Then what do you need from me?” → **stage 30**. NPC: “What I need from you is more of an inside job. I need you to get the key to the vault from Troublemaker without him…”

???+ note "Stage 35: 1 route"

    1. Talk to [Defy](../monsters/aidem_camp_defy.md) ([aidem_camp](../maps/aidem_camp.md)) → choose “I'll do it for twice that amount. 20 percent.” → **stage 35**. NPC: “Fine! [Shh] I'll take it out of Greedy's portion. He'll never know the difference.”

???+ note "Stage 40: 1 route"

    1. Talk to [Defy](../monsters/aidem_camp_defy.md) ([aidem_camp](../maps/aidem_camp.md)) → choose “Sounds good, but where is your hideout?” → **stage 40**; also removes monsters from aidem_camp, spawns monsters on aidem_base_2, spawns monsters on aidem_base_2. NPC: “It's where the rail tracks end. West of the Sutdover River.”

???+ note "Stage 45: 1 route"

    1. Talk to [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Great! Just tell me where to go and you can consider it done.” — **conditions:** latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60; latest stage of [Wanted men](../quests/wanted_men.md#stage-40) is 40 → **stage 45**; also gives [Thieves' vault key](../items/thieves_vault_key.md). NPC: “Well, it's not that easy. You need more than the location. You need this key.”

???+ note "Stage 50: 1 route"

    1. Talk to [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Well, I agreed to, but only because I want to help you guys catch him.” — **conditions:** latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60; reached stage 50 of [Wanted men](../quests/wanted_men.md#stage-50); NOT reached stage 55 of [Wanted men](../quests/wanted_men.md#stage-55) → **stage 50**. NPC: “Really? What did you say?”

???+ note "Stage 55: 1 route"

    1. Talk to [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Thanks a lot. I do feel a lot smarter now than I did before joining your guild.” — **conditions:** latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60; reached stage 50 of [Wanted men](../quests/wanted_men.md#stage-50); NOT reached stage 55 of [Wanted men](../quests/wanted_men.md#stage-55) → **stage 55**; also gives [Fake Thieve's Guild vault key](../items/thieves_vault_key_fake.md). NPC: “Listen, kid. Let's use this to our advantage. Take this fake key, bring it to Defy and we will be waiting for them at…”

???+ note "Stage 56: 1 route"

    1. Talk to [Defy](../monsters/aidem_base_defy.md) ([aidem_base_2](../maps/aidem_base_2.md)) → choose “Yes, Here it is. [Handing over the fake key]” — **conditions:** NOT reached stage 56 of [Wanted men](../quests/wanted_men.md#stage-56); hand over 1× [Fake Thieve's Guild vault key](../items/thieves_vault_key_fake.md) → **stage 56**; also gives [Aidem fake vault key](../items/aidem_fake_vault_key.md), removes monsters from aidem_base_2, spawns monsters on wild6_house, removes monsters from aidem_base_2. NPC: “Thank you so much. Now take this fake key that Zachlanny's has made and return it to Troublemaker before he suspects…”

???+ note "Stage 57: 1 route"

    1. Talk to [Rennik](../monsters/wild6_house_thief.md) ([wild6_house](../maps/wild6_house.md)) → choose “That's great news indeed. Where are they now?” — **conditions:** NOT reached stage 57 of [Wanted men](../quests/wanted_men.md#stage-57); reached stage 2 of [Sutdove_nondisplay (hidden flag)](../quests/sutdover_hidden.md#stage-2) → **stage 57**; also spawns monsters on guildbrig2. NPC: “We are keeping them in our holding cage in Fallhaven.”

???+ note "Stage 60: 1 route"

    1. Talk to [Defy](../monsters/aidem_base_defy.md) ([aidem_base_2](../maps/aidem_base_2.md)) → choose “Yes. Here it is.” — **conditions:** reached stage 45 of [Wanted men](../quests/wanted_men.md#stage-45); NOT reached stage 60 of [Wanted men](../quests/wanted_men.md#stage-60); hand over 1× [Thieves' vault key](../items/thieves_vault_key.md) → **stage 60**; also gives [Aidem fake vault key](../items/aidem_fake_vault_key.md). NPC: “Thank you so much. Now take this fake key that Zachlanny's has made and return it to Troublemaker before he suspects…”

???+ note "Stage 65: 1 route"

    1. Talk to [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “[Lie] I have deposited the 10,000 gold. Here is your key back, as promised.” — **conditions:** latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60; latest stage of [Wanted men](../quests/wanted_men.md#stage-60) is 60; hand over 1× [Aidem fake vault key](../items/aidem_fake_vault_key.md) → **stage 65**; also removes monsters from aidem_base_2, spawns monsters on wild6_house, faction “factionCountThieves” set to -8, removes monsters from aidem_base_2. NPC: “Thank you very much!”

???+ note "Stage 70: 1 route"

    1. Talk to [Defy](../monsters/defy_wild6house.md) ([wild6_house](../maps/wild6_house.md)) → the conversation leads here automatically — **conditions:** reached stage 65 of [Wanted men](../quests/wanted_men.md#stage-65) → **stage 70**; also gives [Gold coins](../items/gold.md). NPC: “Here is your reward for your role in our success.”

???+ note "Stage 75: 1 route"

    1. Talk to [Defy](../monsters/aidem_base_defy.md) ([aidem_base_2](../maps/aidem_base_2.md)) → choose “You heard me the first time. I'm keeping the key and looting the vault myself.” — **conditions:** reached stage 45 of [Wanted men](../quests/wanted_men.md#stage-45); NOT reached stage 60 of [Wanted men](../quests/wanted_men.md#stage-60); carry 1× [Thieves' vault key](../items/thieves_vault_key.md) → **stage 75**. NPC: “I will be taking that key now!”

???+ note "Stage 76: 1 route"

    1. stepping on a trigger on [aidem_base_2](../maps/aidem_base_2.md) → the conversation leads here automatically — **conditions:** killed 1× [Greedy](../monsters/aidem_base_greedy_aggressive.md); killed 1× [Grabby](../monsters/aidem_base_grabby_aggressive.md); killed 1× [Zachlanny](../monsters/aidem_base_zachlanny_aggressive.md); killed 1× [Alaric](../monsters/aidem_base_alaric_aggressive.md); killed 1× [Defy](../monsters/aidem_base_defy.md) → **stage 76**. NPC: “I have killed Defy, his three helpers and Alaric. I really should go back to Fallhaven and talk to Troublemaker again.”

???+ note "Stage 77: 1 route"

    1. stepping on a trigger on [wild6_house](../maps/wild6_house.md) → choose “Yes.” — **conditions:** latest stage of [Wanted men](../quests/wanted_men.md#stage-76) is 76; carry 1× [Thieves' vault key](../items/thieves_vault_key.md) → **stage 77**; also changes map wild6_house. NPC: “The lock creaks open, revealing a staircase.”

???+ note "Stage 80: 1 route"

    1. Talk to [Troublemaker](../monsters/troublemaker.md) ([fallhaven_derelict2](../maps/fallhaven_derelict2.md)) → choose “Yes. I looted their rings. [Shows them to Troublemaker]” — **conditions:** latest stage of [Thief apprentice](../quests/Thieves01.md#stage-60) is 60; latest stage of [Wanted men](../quests/wanted_men.md#stage-76) is 76; hand over 1× [Defy's ring](../items/defy_ring.md); hand over 1× [Greedy's ring](../items/greedy_ring.md); hand over 1× [Grabby's ring](../items/grabby_ring.md); hand over 1× [Zachlanny ring](../items/zachlanny_ring.md) → **stage 80**; also faction “factionCountThieves” set to 3. NPC: “Well, this is great news indeed. However, we would like to have them alive.”


<p class="verified">Verified against v0.8.18 dialogue data.</p>

## Version history

| Version | Change |
|---|---|
| [v0.8.8](../versions/0.8.8.md) | Added<br>Dialogue: 20 lines added |
| [v0.8.10](../versions/0.8.10.md) | Dialogue: 1 line changed |
| [v0.8.13](../versions/0.8.13.md) | stage 20 journal text changed; stage 25 journal text changed; stage 35 journal text changed; stage 45 journal text changed; stage 50 journal text changed; stage 57 journal text changed (+1 more)<br>Dialogue: 1 line changed<br>· text: “I'm talking about the Thieves Guild.” → “I'm talking about the Thieves' Guild.” |
| [v0.8.14](../versions/0.8.14.md) | stage 50 journal text changed<br>Dialogue: 1 line changed<br>· text: “Well, this is great news indeed. We however would like to have them a…” → “Well, this is great news indeed. However, we would like to have them …” |

<p class="verified">Verified against v0.8.18 and every earlier release back to v0.7.0 (game data compared release by release).</p>

## Community notes

<small>Written by players, not generated from game data. **Walkthrough**: step-by-step help for players · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Bugs**: known glitches and workarounds · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Walkthrough

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wanted_men.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wanted_men.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wanted_men.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Bugs

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wanted_men.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/quests?filename=wanted_men.md&value=%23%23%20Walkthrough%0A%0A%3C%21--%20step-by-step%20help%20for%20players%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Bugs%0A%0A%3C%21--%20known%20glitches%20and%20workarounds%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


??? info "Technical information"

    | | |
    |---|---|
    | Quest ID | `wanted_men` |
    | showInLog | 1 |
    | Stage IDs | 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 56, 57, 60, 65, 70, 75, 76, 77, 80 |
    | Dialogue nodes setting stages | 10: `aidem_camp_easedrop_20`, 15: `aidem_camp_easdrop_35`, 20: `aidem_camp_defy_76a`, 20: `aidem_camp_defy_77`, 25: `aidem_camp_defy_85`, 30: `aidem_camp_defy_88`, 35: `aidem_camp_defy_90`, 40: `aidem_camp_defy_100`, 45: `troublemaker_wm_20`, 50: `troublemaker_wm_report_20`, 55: `troublemaker_wm_report_30`, 56: `aidem_base_defy_help_tg_10`, 57: `thief_rennik_30`, 60: `aidem_base_defy_help_20`, 65: `troublemaker_wm_return_fake_key_10`, 70: `defy_wild6house_10`, 75: `aidem_base_defy_dont_help_20`, 76: `aidem_base_thieves_killed`, 77: `wild6_house_hatch_20`, 80: `troublemaker_wm_deffy_killed_40` |
    | Dialogue nodes clearing stages | – |
    | Source files | `res/raw/questlist*.json`, `res/raw/conversationlist*.json` |


<small>Data from v0.8.18</small>
