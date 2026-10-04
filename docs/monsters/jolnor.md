# ![](../assets/icons/monsters/monsters_men2_8.png){ .sprite } Jolnor

| Stat | Value |
|---|---|
| Class | humanoid |
| HP | 0 |
| Max AP | 10 |
| Attack cost | 10 |
| Move cost | 10 |
| Damage | 0 |
| Attack chance | 0 |
| Block chance | 0 |
| Damage resistance | 0 |
| Critical skill | 0 |
| Critical multiplier | 0 |

## Shop stock

| Item | Chance | Qty |
|---|---|---|
| [Minor potion of health](../items/health_minor2.md) | 100% | 10 |
| [Regular potion of health](../items/health.md) | 100% | 10 |
| [Major potion of health](../items/health_major2.md) | 100% | 10 |
| [Defender's stone](../items/necklace_defender_stone.md) | 100% | 1 |
| [Shielding necklace](../items/necklace_shield2.md) | 100% | 1 |
| [Ring of damage +3](../items/ring_dmg_3.md) | 100% | 1 |
| [Defender's ring](../items/ring_defender.md) | 100% | 1 |
| [Ring of damage +6](../items/ring_dmg6.md) | 100% | 1 |
| [Ring of the guardian](../items/ring_guardian.md) | 100% | 1 |
| [Robe of the protector](../items/robe_protector.md) | 100% | 1 |

## Found on

- [vilegard_chapel](../maps/vilegard_chapel.md)

## Quests

- [Kaori's errands](../quests/kaori.md): stages 5
- [Shadows](../quests/shadows.md): stages 110, 120
- [Spies in the foam](../quests/jolnor.md): stages 10, 30
- [Trusting an outsider](../quests/vilegard.md): stages 20, 30
- [Uncertain cause](../quests/wrye.md): stages 10

??? quote "Dialogue (61 lines)"

    *What the dialogue says, exactly as in the game files. Lines are listed once; links jump to the line a choice leads to.*

    <span id="d-jolnor_select_1"></span>**`jolnor_select_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Trusting an outsider](../quests/vilegard.md#stage-30))* → [jolnor_default_3](#d-jolnor_default_3)
    - branch 2 *(if reached stage 20 of [Trusting an outsider](../quests/vilegard.md#stage-20))* → [jolnor_default_2](#d-jolnor_default_2)
    - branch 3 → [jolnor_default](#d-jolnor_default)

    <span id="d-jolnor_default_3"></span>**`jolnor_default_3`** Jolnor: “Walk with the Shadow my friend.”

    - “Can you tell me again what this place is?” → [jolnor_chapel_1](#d-jolnor_chapel_1)
    - “I require healing. Can I see what items you have available?” → [jolnor_shop_1](#d-jolnor_shop_1)
    - “I need some help finding out who is responsible for casting a Shadow spell that causes a person to become noticeable.” *(if reached stage 50 of [Troubling times](../quests/troubling_times.md#stage-50); NOT reached stage 70 of [Troubling times](../quests/troubling_times.md#stage-70))* → [tt_jolnor_10](#d-tt_jolnor_10)
    - “What blessings can you provide?” *(if reached stage 100 of [Shadows](../quests/shadows.md#stage-100); NOT reached stage 110 of [Shadows](../quests/shadows.md#stage-110))* → [dds_jolnor_10](#d-dds_jolnor_10)
    - “About Fatigue and Life drain ...” *(if reached stage 110 of [Shadows](../quests/shadows.md#stage-110); NOT reached stage 120 of [Shadows](../quests/shadows.md#stage-120))* → [dds_jolnor_100](#d-dds_jolnor_100)
    - “The blessing has worn off too early. Could you give it again?” *(if reached stage 110 of [Shadows](../quests/shadows.md#stage-110); NOT reached stage 160 of [Shadows](../quests/shadows.md#stage-160); NOT affected by shadowsleep)* → [dds_talion_130](#d-dds_talion_130)

    <span id="d-jolnor_default_2"></span>**`jolnor_default_2`** Jolnor: “Walk with the Shadow my child.”

    - “Can you tell me again what this place is?” → [jolnor_chapel_1](#d-jolnor_chapel_1)
    - “Let's talk about those missions for gaining trust that you talked about earlier.” → [jolnor_quests_1](#d-jolnor_quests_1)
    - “I require healing. Can I see what items you have available?” → [jolnor_shop_1](#d-jolnor_shop_1)

    <span id="d-jolnor_default"></span>**`jolnor_default`** Jolnor: “Walk with the Shadow my child.”

    - “What is this place?” → [jolnor_chapel_1](#d-jolnor_chapel_1)
    - “I was told to talk to you about why everyone in Vilegard is suspicious of outsiders.” *(if reached stage 10 of [Trusting an outsider](../quests/vilegard.md#stage-10))* → [jolnor_suspicious_1](#d-jolnor_suspicious_1)

    <span id="d-jolnor_chapel_1"></span>**`jolnor_chapel_1`** Jolnor: “This is Vilegard's place of worship for the Shadow. We praise the Shadow in all its might and glory.”

    - “Can you tell me more about the Shadow?” → [jolnor_shadow_1](#d-jolnor_shadow_1)
    - “I require healing. Can I see what items you have available?” → [jolnor_shop_1](#d-jolnor_shop_1)
    - “Whatever. Just show me your goods.” → [jolnor_shop_1](#d-jolnor_shop_1)

    <span id="d-jolnor_shop_1"></span>**`jolnor_shop_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Trusting an outsider](../quests/vilegard.md#stage-30))* → *shop opens*
    - branch 2 → [jolnor_shop_2](#d-jolnor_shop_2)

    <span id="d-tt_jolnor_10"></span>**`tt_jolnor_10`** Jolnor: “Excuse me? I don't know what you want from me.”

    - “Never mind.” → [jolnor_default_3](#d-jolnor_default_3)

    <span id="d-dds_jolnor_10"></span>**`dds_jolnor_10`** Jolnor: “I don't provide any blessings.”

    - “But Talion said that you could.” → [dds_jolnor_20](#d-dds_jolnor_20)

    <span id="d-dds_jolnor_100"></span>**`dds_jolnor_100`** Jolnor: “Well, ask away.”

    - “Can you also give 'blessings' of Fatigue and Life Drain” → [dds_jolnor_110](#d-dds_jolnor_110)

    <span id="d-dds_talion_130"></span>**`dds_talion_130`** Jolnor: “That's no problem at all.”

    - “I'm glad about that.” → [dds_talion_132](#d-dds_talion_132)

    <span id="d-jolnor_quests_1"></span>**`jolnor_quests_1`** Jolnor: “I would suggest you help Kaori, Wrye and me to gain our trust.”

    - “About that guard outside the Foaming Flask tavern...” → [jolnor_guard_select](#d-jolnor_guard_select)
    - “About those tasks...” → [jolnor_quests_2](#d-jolnor_quests_2)
    - “Never mind, let's get back to those other topics.” → [jolnor_select_1](#d-jolnor_select_1)

    <span id="d-jolnor_suspicious_1"></span>**`jolnor_suspicious_1`** Jolnor: “Suspicious? No, I wouldn't call it suspicion. I would rather call it that we are careful nowadays.”

    - Next → [jolnor_suspicious_2](#d-jolnor_suspicious_2)

    <span id="d-jolnor_shadow_1"></span>**`jolnor_shadow_1`** Jolnor: “The Shadow protects us from the dangers of the night. It keeps us safe and comforts us when we sleep.”

    - Next → [jolnor_select_1](#d-jolnor_select_1)

    <span id="d-jolnor_shop_2"></span>**`jolnor_shop_2`** Jolnor: “I don't trust you enough yet to feel comfortable trading with you.”

    - “Why are you that suspicious?” → [jolnor_suspicious_1](#d-jolnor_suspicious_1)
    - “Very well.” → [jolnor_select_1](#d-jolnor_select_1)

    <span id="d-dds_jolnor_20"></span>**`dds_jolnor_20`** Jolnor: “Oh, you mean Shadow Sleepiness?”

    - “Yes.” → [dds_jolnor_22](#d-dds_jolnor_22)

    <span id="d-dds_jolnor_110"></span>**`dds_jolnor_110`** Jolnor: “Borvis can't even manage those?! How unworthy!”

    - “Well, could you?” → [dds_jolnor_112](#d-dds_jolnor_112)

    <span id="d-dds_talion_132"></span>**`dds_talion_132`** Jolnor: “It'll just cost you another 300 gold pieces.”

    - “Sure, I am wealthy enough.” *(if have 300 gold)* → [dds_jolnor_62](#d-dds_jolnor_62)
    - “I don't have that much with me. I'll be back.” *(if NOT have 300 gold)* → *conversation ends*

    <span id="d-jolnor_guard_select"></span>**`jolnor_guard_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Spies in the foam](../quests/jolnor.md#stage-30))* → [jolnor_guard_completed](#d-jolnor_guard_completed)
    - branch 2 → [jolnor_guard_1](#d-jolnor_guard_1)

    <span id="d-jolnor_quests_2"></span>**`jolnor_quests_2`** Jolnor: “Yes, what about them?”

    - “What was I supposed to do again?” → [jolnor_suspicious_2](#d-jolnor_suspicious_2)
    - “I have done all the tasks you asked me to do.” *(if reached stage 30 of [Spies in the foam](../quests/jolnor.md#stage-30))* → [jolnor_quests_select_1](#d-jolnor_quests_select_1)
    - “Never mind, let's get back to those other topics.” → [jolnor_select_1](#d-jolnor_select_1)

    <span id="d-jolnor_suspicious_2"></span>**`jolnor_suspicious_2`** Jolnor: “In order to gain the trust of the village, an outsider must prove that they are not here to cause trouble.”

    - “Sounds like a good idea. There are a lot of selfish people out there.” → [jolnor_suspicious_3](#d-jolnor_suspicious_3)
    - “That sounds really unnecessary. Why not trust people in the first place?” → [jolnor_suspicious_4](#d-jolnor_suspicious_4)

    <span id="d-dds_jolnor_22"></span>**`dds_jolnor_22`** Jolnor: “So Talion still can't tell a blessing from a spell.”

    - Next → [dds_jolnor_24](#d-dds_jolnor_24)

    <span id="d-dds_jolnor_112"></span>**`dds_jolnor_112`** Jolnor: “Of course I could, if I wanted to.”

    - “If you say so.” → [dds_jolnor_120](#d-dds_jolnor_120)

    <span id="d-dds_jolnor_62"></span>**`dds_jolnor_62`** Jolnor: “Well, give me the 300 gold.”

    - “Sure, here.” *(if pay 300 gold)* → [dds_jolnor_70](#d-dds_jolnor_70)

    <span id="d-jolnor_guard_completed"></span>**`jolnor_guard_completed`** Jolnor: “Yes, you dealt with him earlier. Thank you for your help.”

    - Next → [jolnor_quests_1](#d-jolnor_quests_1)

    <span id="d-jolnor_guard_1"></span>**`jolnor_guard_1`** Jolnor: “Yes, what about him. Have you removed him yet?”

    - “Yes, he will leave his post as soon as this shift is over.” *(if reached stage 20 of [Spies in the foam](../quests/jolnor.md#stage-20))* → [jolnor_guard_2](#d-jolnor_guard_2)
    - “Yes, he is removed.” *(if hand over 1× [Feygard patrol ring](../items/ffguard_qitem.md))* → [jolnor_guard_2](#d-jolnor_guard_2)
    - “No, but I am working on it.” → [jolnor_gaintrust_14](#d-jolnor_gaintrust_14)

    <span id="d-jolnor_quests_select_1"></span>**`jolnor_quests_select_1`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 20 of [Kaori's errands](../quests/kaori.md#stage-20))* → [jolnor_quests_select_2](#d-jolnor_quests_select_2)
    - branch 2 → [jolnor_quests_kaori_1](#d-jolnor_quests_kaori_1)

    <span id="d-jolnor_suspicious_3"></span>**`jolnor_suspicious_3`** Jolnor: “Yes, right. You seem to understand us well, I like that.”

    - “Is there anything I can do to gain your trust?” → [jolnor_gaintrust_select](#d-jolnor_gaintrust_select)

    <span id="d-jolnor_suspicious_4"></span>**`jolnor_suspicious_4`** Jolnor: “We have learned from history not to trust outsiders, and you are an outsider. Why should we trust you?”

    - “What can I do to gain your trust?” → [jolnor_gaintrust_select](#d-jolnor_gaintrust_select)
    - “You are right. You probably should not trust me.” → *conversation ends*

    <span id="d-dds_jolnor_24"></span>**`dds_jolnor_24`** Jolnor: “He never could.”

    - “Now what?” → [dds_jolnor_26](#d-dds_jolnor_26)

    <span id="d-dds_jolnor_120"></span>**`dds_jolnor_120`** Jolnor: “There's one priest, Favlon, who can give you both. However, he went researching in the area west of Sullengard and hasn't been seen since.” — **effects:** sets stage 120 of [Shadows](../quests/shadows.md#stage-120), spawns monsters on nw_sullengard_1

    - “West of Sullengard. Sigh.” → *conversation ends*

    <span id="d-dds_jolnor_70"></span>**`dds_jolnor_70`** [Dummy NPC](../monsters/none.md): “Jolnor is chanting, murmuring, gesticulating.”

    - “[Thinking to himself] He's probably just doing this to distract me so I can't figure out how to do it.” → [dds_jolnor_80](#d-dds_jolnor_80)

    <span id="d-jolnor_guard_2"></span>**`jolnor_guard_2`** Jolnor: “Very good. Thank you for your help.” — **effects:** sets stage 30 of [Spies in the foam](../quests/jolnor.md#stage-30)

    - “No problem. Let's get back to those other tasks we talked about.” → [jolnor_quests_2](#d-jolnor_quests_2)

    <span id="d-jolnor_gaintrust_14"></span>**`jolnor_gaintrust_14`** Jolnor: “Good. Report back to me when you are done.”

    - Next → [jolnor_gaintrust_15](#d-jolnor_gaintrust_15)

    <span id="d-jolnor_quests_select_2"></span>**`jolnor_quests_select_2`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 90 of [Uncertain cause](../quests/wrye.md#stage-90))* → [jolnor_quests_completed](#d-jolnor_quests_completed)
    - branch 2 → [jolnor_quests_wrye_1](#d-jolnor_quests_wrye_1)

    <span id="d-jolnor_quests_kaori_1"></span>**`jolnor_quests_kaori_1`** Jolnor: “You still need to help Kaori with her task.”

    - Next → [jolnor_select_1](#d-jolnor_select_1)

    <span id="d-jolnor_gaintrust_select"></span>**`jolnor_gaintrust_select`** *(silent check: the first matching branch below is taken)*

    - branch 1 *(if reached stage 30 of [Trusting an outsider](../quests/vilegard.md#stage-30))* → [jolnor_gaintrust_return_2](#d-jolnor_gaintrust_return_2)
    - branch 2 *(if reached stage 20 of [Trusting an outsider](../quests/vilegard.md#stage-20))* → [jolnor_gaintrust_return](#d-jolnor_gaintrust_return)
    - branch 3 → [jolnor_gaintrust_1](#d-jolnor_gaintrust_1)

    <span id="d-dds_jolnor_26"></span>**`dds_jolnor_26`** Jolnor: “If Talion says - OK, it's yours for only 300 gold. Though it's not a blessing as such...”

    - “Great!” *(if pay 300 gold)* → [dds_jolnor_50](#d-dds_jolnor_50)
    - “That is too much. I'd offer you 50 gold at the most.” → [dds_jolnor_28](#d-dds_jolnor_28)
    - “300? I have to get some gold first.” *(if NOT have 300 gold)* → *conversation ends*

    <span id="d-dds_jolnor_80"></span>**`dds_jolnor_80`** [Jolnor](../monsters/jolnor.md): “Here you go. Take it to Borvis with care.” — **effects:** applies condition shadowsleep, sets stage 110 of [Shadows](../quests/shadows.md#stage-110)

    - “Thank you. Bye.” → *conversation ends*
    - “Please, I still have a question.” → [dds_jolnor_100](#d-dds_jolnor_100)

    <span id="d-jolnor_gaintrust_15"></span>**`jolnor_gaintrust_15`** Jolnor: “So, in order to gain our trust here in Vilegard, I would suggest you help Kaori, Wrye and me.” — **effects:** sets stage 20 of [Trusting an outsider](../quests/vilegard.md#stage-20)

    - “Thank you for the information. I will be back when I have something to report.” → *conversation ends*

    <span id="d-jolnor_quests_completed"></span>**`jolnor_quests_completed`** Jolnor: “Good. You helped all three of us.” — **effects:** sets stage 30 of [Trusting an outsider](../quests/vilegard.md#stage-30)

    - Next → [jolnor_quests_completed_2](#d-jolnor_quests_completed_2)

    <span id="d-jolnor_quests_wrye_1"></span>**`jolnor_quests_wrye_1`** Jolnor: “You still need to help Wrye with her task.”

    - Next → [jolnor_select_1](#d-jolnor_select_1)

    <span id="d-jolnor_gaintrust_return_2"></span>**`jolnor_gaintrust_return_2`** Jolnor: “With your help earlier, you have already gained our trust.”

    - Next → [jolnor_default_3](#d-jolnor_default_3)

    <span id="d-jolnor_gaintrust_return"></span>**`jolnor_gaintrust_return`** Jolnor: “As I said before, you have to help some people here in Vilegard to gain our trust.”

    - Next → [jolnor_quests_1](#d-jolnor_quests_1)

    <span id="d-jolnor_gaintrust_1"></span>**`jolnor_gaintrust_1`** Jolnor: “If you do us a favor, we might consider trusting you. There are three people I can think of that are influential here in Vilegard, that you should try to help.”

    - Next → [jolnor_gaintrust_2](#d-jolnor_gaintrust_2)

    <span id="d-dds_jolnor_50"></span>**`dds_jolnor_50`** Jolnor: “What do you want it for?”

    - “Well, Borvis wanted it to break through a Shadow shield, as someone is misusing Shadow powers to the south of Stoutford.” → [dds_jolnor_60](#d-dds_jolnor_60)

    <span id="d-dds_jolnor_28"></span>**`dds_jolnor_28`** Jolnor: “Your choice. Come again, when you are wiser.”


    <span id="d-jolnor_quests_completed_2"></span>**`jolnor_quests_completed_2`** Jolnor: “I suppose that shows some dedication, and that we are ready to trust you now.”

    - Next → [jolnor_quests_completed_3](#d-jolnor_quests_completed_3)

    <span id="d-jolnor_gaintrust_2"></span>**`jolnor_gaintrust_2`** Jolnor: “First, there is Kaori. She lives up in the northern part of Vilegard. Ask her if she wants help with anything.” — **effects:** sets stage 5 of [Kaori's errands](../quests/kaori.md#stage-5)

    - “OK. Talk to Kaori. Got it.” → [jolnor_gaintrust_3](#d-jolnor_gaintrust_3)

    <span id="d-dds_jolnor_60"></span>**`dds_jolnor_60`** Jolnor: “Tsk! Tsk! Not strong enough, is he? Sending a kid to do a priest's duty?”

    - Next → [dds_jolnor_62](#d-dds_jolnor_62)

    <span id="d-jolnor_quests_completed_3"></span>**`jolnor_quests_completed_3`** Jolnor: “You have our thanks, friend. You will always find shelter here in Vilegard. We welcome you into our village.”

    - Next → [jolnor_select_1](#d-jolnor_select_1)

    <span id="d-jolnor_gaintrust_3"></span>**`jolnor_gaintrust_3`** Jolnor: “Then there is Wrye. Wrye also lives up in the northern part of Vilegard. Many people here in Vilegard seek her advice on various things.”

    - Next → [jolnor_gaintrust_4](#d-jolnor_gaintrust_4)

    <span id="d-jolnor_gaintrust_4"></span>**`jolnor_gaintrust_4`** Jolnor: “She recently lost her son in a tragic way. If you can gain her trust, you will have a strong ally here.” — **effects:** sets stage 10 of [Uncertain cause](../quests/wrye.md#stage-10)

    - “Talk to Wrye. Got it.” → [jolnor_gaintrust_5](#d-jolnor_gaintrust_5)

    <span id="d-jolnor_gaintrust_5"></span>**`jolnor_gaintrust_5`** Jolnor: “And last but not least, I have a favor to ask of you as well.”

    - “What favor is that?” → [jolnor_gaintrust_6](#d-jolnor_gaintrust_6)

    <span id="d-jolnor_gaintrust_6"></span>**`jolnor_gaintrust_6`** Jolnor: “North of Vilegard is a tavern called the Foaming Flask. In my opinion, this tavern is a guard station in guise for Feygard.”

    - Next → [jolnor_gaintrust_7](#d-jolnor_gaintrust_7)

    <span id="d-jolnor_gaintrust_7"></span>**`jolnor_gaintrust_7`** Jolnor: “The tavern is almost always visited by the Feygard royal guard of Lord Geomyr.”

    - Next → [jolnor_gaintrust_8](#d-jolnor_gaintrust_8)

    <span id="d-jolnor_gaintrust_8"></span>**`jolnor_gaintrust_8`** Jolnor: “They are probably here to spy on us, since we are followers of the Shadow. Lord Geomyr's forces always try to make life difficult for us and the Shadow.”

    - “Yes, they seem like troublemakers all around.” → [jolnor_gaintrust_9](#d-jolnor_gaintrust_9)
    - “I am sure they have their reasons for doing what they do.” → [jolnor_gaintrust_10](#d-jolnor_gaintrust_10)

    <span id="d-jolnor_gaintrust_9"></span>**`jolnor_gaintrust_9`** Jolnor: “Right. Troublemakers indeed.”

    - “What do you want me to do?” → [jolnor_gaintrust_11](#d-jolnor_gaintrust_11)

    <span id="d-jolnor_gaintrust_10"></span>**`jolnor_gaintrust_10`** Jolnor: “Yes, their reason is to make life miserable for us, I am sure.”

    - “What do you want me to do?” → [jolnor_gaintrust_11](#d-jolnor_gaintrust_11)

    <span id="d-jolnor_gaintrust_11"></span>**`jolnor_gaintrust_11`** Jolnor: “My reports say that there is a guard stationed outside the tavern, to keep an eye on potential dangers.”

    - Next → [jolnor_gaintrust_12](#d-jolnor_gaintrust_12)

    <span id="d-jolnor_gaintrust_12"></span>**`jolnor_gaintrust_12`** Jolnor: “I want you to make sure the guard disappears somehow. How you do that is purely up to you.” — **effects:** sets stage 10 of [Spies in the foam](../quests/jolnor.md#stage-10)

    - “I am not sure I should upset the Feygard patrol guards. This could really get me into trouble.” → [jolnor_gaintrust_13](#d-jolnor_gaintrust_13)
    - “For the Shadow, I will do as you ask.” → [jolnor_gaintrust_14](#d-jolnor_gaintrust_14)
    - “OK, I hope this leads to some treasure in the end.” → [jolnor_gaintrust_14](#d-jolnor_gaintrust_14)

    <span id="d-jolnor_gaintrust_13"></span>**`jolnor_gaintrust_13`** Jolnor: “It's your choice. You can at least go check out the tavern and see if you find anything suspicious.”

    - “Maybe.” → [jolnor_gaintrust_15](#d-jolnor_gaintrust_15)



## Community notes

<small>Written by players, not generated from game data. **Observations**: what players notice in-game · **Lore**: the in-world story · **Trivia**: real-world facts, references, development history · **Theory / speculation**: unconfirmed ideas; may just be unfinished content</small>

### Observations

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jolnor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Lore

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jolnor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Trivia

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jolnor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*

### Theory / speculation

*Nothing here yet. Know something? [Add it](https://github.com/asdfghjkl628/Andor-s-Trail-Wikiiii/new/main/notes/monsters?filename=jolnor.md&value=%23%23%20Observations%0A%0A%3C%21--%20what%20players%20notice%20in-game%20--%3E%0A%0A%23%23%20Lore%0A%0A%3C%21--%20the%20in-world%20story%20--%3E%0A%0A%23%23%20Trivia%0A%0A%3C%21--%20real-world%20facts%2C%20references%2C%20development%20history%20--%3E%0A%0A%23%23%20Theory%20/%20speculation%0A%0A%3C%21--%20unconfirmed%20ideas%3B%20may%20just%20be%20unfinished%20content%20--%3E%0A).*


<small>Monster ID: `jolnor` · Data from v0.8.18</small>
