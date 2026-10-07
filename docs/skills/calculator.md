# Build calculator

Plan a character before spending level-ups and skill points. Pick a level, split your level-ups, choose skills and gear, and see your final stats, worked out
**the same way the game does it**: the formulas below are a line-by-line port of the game's own stat code for v0.8.18.

<div class="build-calc" data-src="../../assets/calc/data.json" markdown="0"><noscript>The calculator needs JavaScript.</noscript></div>

??? info "How the numbers are calculated"

    In the order the game applies them (`ActorStatsController.recalculatePlayerStats`):

    1. **Base stats + level-ups.** Starting stats, plus each level-up choice. [Fortitude](fortitude.md) adds HP to every level-up *after* you learn it; the calculator assumes you learn each level as early as allowed.
    2. **Main weapon** sets your attack cost and critical multiplier, then its stats are added.
    3. **Off-hand.** A shield adds its stats directly. A second weapon is blended in by [Dual Wield](fightstyleDualWield.md) at 25 / 50 / 100% efficiency (level 0 / 1 / 2).
    4. **Fighting styles:** two-handed, weapon & shield, dual wield, or [Way of the Monk](fightstyleUnarmedUnarmored.md) (no weapon, no off-hand, no weighted armor).
    5. **Armor and jewelry** stats are added.
    6. **Proficiencies** boost your main weapon's, shield's and armor's own bonuses by a percentage.
    7. **Skills:** Weapon Accuracy, Hard Hit, Dodge, Bark Skin, More/Better Criticals, Combat Speed.
    8. **Damage modifier.** Some weapons scale your *non-weapon* damage (base, level-ups, rings, skills) up or down.
    9. **Caps:** attack chance can't go below 0, and neither can damage.

    Percentages round down, as in the game. Effects from potions and other temporary conditions aren't included.

<p class="verified">Verified against v0.8.18 game code (ActorStatsController, ItemController, SkillController, CombatController) and item data.</p>
