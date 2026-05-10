---
title: "Lint Report"
type: synthesis
tags: [lint, continuity, health]
sources: []
canon_status: canon
spoiler_level: none
era: ""
aliases: []
relationships: []
first_appearance: ""
last_updated: 2026-05-10
---

# Wiki Lint Report — 2026-05-10

## 1. Broken Wikilinks (21)

Most broken links are slug mismatches — the page exists but the wikilink text doesn't match the filename:

| Pattern | Count | Fix needed |
|---------|-------|------------|
| `[[Royce Garett]]` → file is `royce-garett.md` | 7 | Slug mismatch |
| `[[Emilie Gloomshard]]` → file is `emilie-gloomshard.md` | 6 | Slug mismatch |
| `[[Keito Jinshen]]` → file is `keito-jinshen.md` | 1 | Slug mismatch |
| `[[House Gloomshard|Marcus Finneas Gloomshard]]` | 1 | No page exists |
| `[[House Gloomshard|Adrian Marcus Gloomshard]]` | 1 | No page exists |
| `[[Master Timeline]]` → file is `master-timeline.md` | 1 | Slug mismatch |
| `[[Khinning|Godfell]]` | 1 | No page exists |
| `[[The Black Hand]]` → file is `the-black-hand.md` | 1 | Slug mismatch |
| `[[Pantheon]]` → file is `pantheon.md` | 1 | Slug mismatch |
| `[[Westbrook Associates]]` → file is `westbrook-associates.md` | 1 | Slug mismatch |

## 2. Orphan Pages (21)

Pages with no incoming wikilinks from other pages (exist in index but not cross-referenced in prose):

- `sources/the-world-of-troha.md`, `arcs/*`, `events/*`, `timeline/*`
- `characters/royce-garett.md`, `characters/emilie-gloomshard.md`, `characters/derek-sanzabar.md`, `characters/keito-jinshen.md`
- `factions/seven-drow-alliance.md`, `factions/the-black-hand.md`, `factions/westbrook-associates.md`
- `locations/zefua.md`
- `systems/conjury.md`, `systems/house-system-uym.md`, `systems/pantheon.md`, `systems/power-tiers.md`, `systems/vampirism.md`

## 3. Sparse Pages (21 pages with <3 wikilinks)

Pages that don't link out to enough related pages:
- **0 links**: `book-1-structure.md`, `quinton-keinz.md`, `master-timeline.md`
- **1 link**: `jinrui-igarashi.md`, `keon-berzgrandt.md`, `silas-eckhardt.md`, `spectr.md`
- **2 links**: 14 more pages

## 4. Alias Collisions

None found.

## 5. Canon Drift

No pages marked `contested` without explanation.

## 6. Timeline Contradictions

| Issue | Severity | Notes |
|-------|----------|-------|
| Levy dies 1913 but re-crowned 1927 | **Medium** | Intentional mystery (resurrection/fake death/body-double). No in-text explanation yet. |
| Royce age paradox | **Low** | "No older than twenty" but active since 1909. Explained by albino/vampiric condition causing youthful appearance. |
| Alex birth year | **Low** | Wiki says 1908; timeline column "1" starts 1908 implying born 1907. Off by 1 year. |
| Levy birth year | **Low** | Wiki says ~1894; timeline age 16 in 1909 implies born ~1893. Off by 1 year. |

## 7. Character Continuity

| Check | Status |
|-------|--------|
| Nora Linefeldt = Baroness Nora Lee Yang | Speculative (consistent but unconfirmed) |
| Lark at Redford Station (lie) | Intentional — mission from Lawrence |
| Alex admission rank (53 vs 7) | Resolved — 53rd is canon |

## 8. Unresolved Setup/Payoff Threads

| Thread | Status |
|--------|--------|
| Gangine consciousness integration | No payoff in current text |
| Hades electromancy unleash | Set up in Ch 26.5, no payoff |
| Irwin Pascal + Silvanox hunt outcome | Introduced, not concluded |
| La Maison Doree birthday event | Ch 32 setup, no payoff |
| The Firebrand child (1904) | Lore only, not in Book 1 |
| Tansen = lost Lee Yang heir | Lore only, Elven Revolution trilogy |
| Lark "Black Bird" arc | Placeholder (arc #11) |
| Westbrook Parasite confrontation | Planning docs only, Book 4+ |

## 9. Graph Summary

- **59 nodes**, **65 edges**
- Edge types: EXTRACTED (57), ALLY_OF (5), LOCATED_IN (2), CONFLICTS_WITH (1)
- Top hubs: Khinning (23), Troha (18), Gleadenhyme (11), Volta (7), Krillma (7), Lawrence (6)
