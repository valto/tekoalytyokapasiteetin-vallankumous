# Terminology reference — English to Finnish

**This file is the single source of truth for all translation work in this repository.** Every translator (human or AI agent) must use these exact terms consistently. Do not introduce synonyms or alternate phrasings for terms listed here, even if they sound more natural in a given sentence — consistency across 20+ documents matters more than local elegance.

This repository is a literal Finnish translation of `github.com/valto/ai-working-capacity-revolution`. Numbers, evidence-class tags, section structure, and citations are NOT translated or altered — only prose.

## A critical distinction: two unrelated five-tier systems

This package uses its own **five evidence classes** (what kind of claim a sentence is). The sister site **tekoalytalous.fi** uses a *different* five-tier system (confidence that a future development will occur: havaittu / vahva signaali / todennäköinen / mahdollinen / avoin kysymys). **These must never be merged or mapped onto each other.** A price that is an Observed Fact is not "havaittu" in tekoalytalous.fi's sense — the two systems classify different things. Always use this package's own five classes, translated below, never the tekoalytalous.fi tiers.

## Evidence classes (this package's own system — DO NOT confuse with tekoalytalous.fi's tiers)

| English | Finnish |
|---|---|
| Evidence class | näyttöluokka |
| Observed Fact | Havaittu fakta |
| Attributed Statement | Lähteeseen kohdistettu lausunto |
| Derived Calculation | Johdettu laskelma |
| Scenario Assumption | Skenaario-oletus |
| Interpretation | Tulkinta |

Inline tags in source text like `[FACT]`, `[ATTR]`, `[CALC]`, `[ASSUMPTION]`, `[INTERP]` — translate the spelled-out evidence-class name in prose, but you may keep the short bracketed tags in their English form throughout tables/inline markers for consistency with the source register's citation apparatus, UNLESS translating the full appendix/glossary text that defines them. When in doubt, spell it out in Finnish in prose and use `[FAKTA]`, `[LÄHDE]`, `[LASKELMA]`, `[OLETUS]`, `[TULKINTA]` as the short tags — apply this consistently across all documents, not mixed.

## The capacity/resource distinction (confirmed by the author — apply carefully, do not default to one term)

- **tekoälytyökapasiteetti** = the technical/quantity concept: the amount of available AI work or performance capacity. Use this for: the core chain, cost tables, $/tekoäly-työtunti figures, usage-intensity bands, production-tier arithmetic — i.e. the overwhelming majority of the whitepaper and workbooks.
- **tekoälytyöresurssi** = this same capacity viewed as an economic input/factor of production available to the economy. Use this specifically when the text is making an economic-input framing: investment-thesis language, ownership economics (Part V), macro/economy-wide framing (Parts I and VII), and anywhere the English says "AI work resource" or frames working capacity as a factor of production rather than a measured quantity.

If genuinely unsure which applies in a specific sentence, default to **tekoälytyökapasiteetti** (it is the more common case) and flag the sentence in your translation notes rather than guessing silently.

## Core chain and general AI-economy terms (reused verbatim from tekoalytalous.fi's live glossary — do not deviate)

| English | Finnish | Note |
|---|---|---|
| Energy / Electricity | sähkö | "energia" is the listed alternative on tekoalytalous.fi; prefer "sähkö" for the specific electricity-cost sense used throughout this package |
| Compute | laskenta | |
| Compute infrastructure | laskentainfrastruktuuri | |
| Compute capacity | laskentakapasiteetti | |
| AI model | tekoälymalli | |
| Inference | päättely | alt: inferenssi (used in technical contexts) |
| Inference capacity | päättelykapasiteetti | |
| Tokens | tokenit | |
| AI agent | tekoälyagentti | |
| AI factory | tekoälytehdas | |
| Inference factory | päättelytehdas | |
| AI infrastructure | tekoälyinfrastruktuuri | |
| AI-native | tekoälynatiivi | |
| AI economy | tekoälytalous | |
| Intelligence | älykkyys | |
| Outcomes | tulokset | |
| Value | arvo | |
| Working capacity (general, human+AI) | työkapasiteetti | |

## This package's own terms

| English | Finnish |
|---|---|
| AI working capacity | tekoälytyökapasiteetti |
| AI work resource | tekoälytyöresurssi |
| AI working capacity revolution | tekoälytyökapasiteetin vallankumous |
| Hardware | laitteisto |
| Digital work | digitaalinen työ |
| Agency (final step of the chain) | toimijuus |
| Owned-production cost | omistettu tuotantokustannus |
| Retail API price | vähittäis-API-hinta |
| Home tier | kotitaloustaso |
| Cooperative tier | osuustoiminnallinen taso |
| Professional tier | ammattimainen taso |
| Hyperscale tier | hyperskaalataso |
| Utilization | käyttöaste |
| Financing term | rahoitusaika |
| Human employer cost (fully loaded) | työntekijän kokonaiskustannus työnantajalle |
| Human billable / externally purchased rate | laskutettava tuntihinta |
| Cost per AI-working-hour | kustannus per tekoäly-työtunti |
| AI-working-hour (unit) | tekoäly-työtunti |
| Usage-intensity band | käyttöintensiteettivyöhyke |
| Orchestration | orkestrointi |
| Ownership stack | omistusrakenne |
| Digital sovereignty | digitaalinen suvereniteetti |
| Cooperative (AI infrastructure ownership model) | osuuskunta |
| Non-advice statement | neuvontaa koskeva vastuuvapauslauseke |
| Known limitations | tunnetut rajoitteet |
| Scenario Explorer | skenaariotyökalu |
| Perspectives & Writeups | Näkökulmat ja kirjoitukset |

## Named tiers/workbooks — proper-noun-style references (translate the descriptive part, keep numbering)

- "Global Baseline Workbook" → "Globaali perustaso -työkirja" (Release Asset #7 numbering preserved in cross-references)
- "AI Working-Capacity Conversion Workbook" → "Tekoälytyökapasiteetin muuntotyökirja"
- "Token-Factory Scenario Workbook" → "Tokenitehtaan skenaariotyökirja"
- "Investment-Thesis Notes" → "Sijoitusteesin muistiinpanot"
- "Humanoid Working-Capacity Workbook" → "Humanoidirobottien työkapasiteettityökirja"
- "Localized Scenario Workbook (EUR/Finland)" → "Paikallistettu skenaariotyökirja (EUR/Suomi)"

## Number formatting (clarified 2026-08-19 — supersedes any earlier "byte-for-byte" instruction)

Convert numbers to natural Finnish typographic convention: space as the thousands separator, comma as the decimal separator, and currency symbol/word placed the way Finnish naturally places it (e.g. "$4,699" → "4 699 dollaria" or "4 699 $"; "1,091.1" → "1 091,1"; "9,821 tokens/sec" → "9 821 tokenia/s"). This changes only the typographic *formatting* of a number, never its underlying *value* — the rule against "altering numbers" means don't change what a figure says, not that you must preserve English comma/period conventions.

**Do NOT reformat, and leave byte-for-byte identical to the English source:**
- ISO dates (`2026-08-13`)
- Section/part references (`§3.4`, `Section 15`, `Part V`) — translate "Section"/"Part" to "Osio"/"Osa" but never touch the number itself
- Version numbers and model names (`v1.0.1`, `GPT-5.6`, `CC BY 4.0`, `MLPerf v6.0`)
- File names, URLs, evidence-class bracket tags

If any already-translated file used strict byte-for-byte English number formatting (comma-thousands, period-decimals, e.g. "$4,699"), reformat it to natural Finnish convention per this section.

## Rules for all translators

1. **Never translate or alter the underlying value of**: numbers, dollar/euro figures, dates, URLs, citations, section numbers, file names, evidence-class bracket tags' position in a sentence, code blocks, CSV/formula content. (Typographic formatting of numbers should follow the Finnish-convention section above — this is about not changing what a figure says.)
2. **Always translate**: prose, headings, table headers, captions, alt text, speaker notes.
3. Keep the whitepaper's title as **"Miksi tekoälyyn investoidaan biljoonia?"** everywhere it appears (title pages, CITATION.cff, README, HTML `<title>` tags) — this reuses tekoalytalous.fi's own existing homepage phrasing verbatim.
4. Preserve every self-correction note ("Corrected 2026-08-13...", "Resolved 2026-08-14...") — translate the prose but do not remove or soften the correction itself; this package's evidence discipline depends on these staying visible.
5. If a sentence's meaning depends on an English idiom that has no natural Finnish equivalent, translate for meaning, not word-for-word — but flag anything you are not confident about rather than silently guessing.
6. Person names (Jensen Huang, Sam Altman, Mark Zuckerberg, Valto Loikkanen, Larry Fink) and company/product names (NVIDIA, DGX Spark, OpenAI, GPT-5.6, Claude, Gemini) are never translated.
