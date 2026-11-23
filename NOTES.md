# NOTES — news-image-20261123 research (23 Nov 2026, WIB)

Prep only — the image is NOT built yet. Build starts when the user answers
"mulai sekarang atau besok pagi". Competition: free, deadline 25 Nov 07:00 WIB,
$100 shared by top 50 (1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20).
10,684 submissions already. Our quota: 0 entries made, day cap 6.
Kit: ~/workspace/makefun/news-image-20261123-kit/ (RULES.txt read).
Starter: main.ts copies entry.png beside it to /output/entry.png.
Image: PNG/JPEG, ≤1 MiB, ≤1024×1024, deterministic, no network.
Judge: z-ai/glm-5.3-flash, no news feed, does not know the day. Criteria in
order: (1) names the day + specific events of that day, date shown;
(2) breadth across regions/fields; (3) readable from the image alone;
(4) faithful, no hype/speculation as fact; (5) clean craft, legible ~300px,
no garbled text. Front page must say "MONDAY 23 NOVEMBER 2026".

## Stories verified (each against ≥2 sources, 23 Nov 2026 news cycle)

1. **HERO — COP31 collapses, no climate deal.**
   UN climate summit in Antalya, Turkey, ended Sunday 22 Nov without a deal;
   the "Antalya Pact" rejected by the EU and others because it did not mention
   fossil fuels; longest COP in history; first major breakdown since COP15
   (Copenhagen 2009); 190+ countries, 92,000 registered. Monday 23 Nov:
   blame game — Australia's Chris Bowen (president of negotiations) under
   fire at home, Pacific island nations express despair. Sources: CNN
   (22 Nov), phys.org (22 Nov), Reuters (23 Nov), Le Monde (22 Nov).
2. **Iran war — strikes hit Bahrain.**
   Iran attacked a civilian industrial facility in Bahrain on Saturday
   (2 injured); IRGC said it launched a missile and drone assault on US
   military positions in Bahrain; Trump on Friday said Iran wants a deal
   but not one "acceptable" to him; Vance declined to say whether he would
   have authorised strikes on Iran. Sources: Just Security Early Edition
   (23 Nov), France 24 via EventGraph (23 Nov).
3. **Ukraine — Kyiv region flats hit; war spills over.**
   Russian drone strike partially destroyed an apartment building in Dymer,
   near Kyiv — 14 missing, death toll rising (11, then 15); Kryvyi Rih
   overnight strikes killed a child and a young woman, damaged 25 apartment
   buildings, a hospital and schools. NATO emergency talks after 3 Russian
   cruise missiles entered Poland. Ukraine says naval drones sank the
   Russian corvette Mercury in Benghazi, Libya; Russian cargo ship Sparta II
   set ablaze in the Baltic, drifted into Finnish waters. Sources: Just
   Security (23 Nov), Seven Lights (23 Nov), Medium strategic brief
   (23 Nov), France 24 liveblog (23 Nov).
4. **US — Democrats win the House, 258 seats.**
   North Carolina recount confirmed Democrat Chuck Hubbard's win, giving
   House Democrats at least 258 seats — their best result since 1992.
   Trump moves to block oversight before Democrats take power. Sources:
   Medium strategic brief (23 Nov), EventGraph daily brief (23 Nov, BBC).
5. **Gaza — 99% toxic, Oxfam warns.**
   New Oxfam report documents toxic contamination across nearly all of Gaza
   ("a toxic wasteland"). Israeli forces hit a truck in Gaza on Saturday
   (3 killed); PM-elect Eisenkot called West Bank settler arson attacks
   "Jewish terrorism". Sources: Medium strategic brief (23 Nov),
   News Media House (23 Nov), Just Security (23 Nov).
6. **AI — Nvidia scandal + markets slide.**
   Intelligence reports: Alice Huang kept contact with China's Ministry of
   State Security during her affair with Nvidia's Jensen Huang; Nvidia chip
   smuggling network linked to her associate. Asian markets fell sharply
   Monday on AI sustainability fears. Sources: frequentbusinesstraveler
   GEORGE (23 Nov), News Media House (23 Nov), EventGraph (23 Nov).
7. **Footer — also today.**
   Delta outage delayed 1,600+ flights as Thanksgiving travel began
   (FAA); Trump signed the Common Cents Act, ending the penny's 232-year
   run; Mexico captured drug lord "El Chapo Isidro" (Fausto Isidro Meza
   Flores) in Sinaloa; Belgium airports face shutdown in a nationwide
   austerity strike; Alcaraz beat Zverev for his first ATP Finals title.
   Sources: GEORGE (23 Nov), News Media House (23 Nov).

## Timing note (honest)

COP31's collapse was finalised Sunday 22 Nov (late, record overtime) and
the blame/fallout is Monday 23 Nov's news; the Iran/Bahrain strikes were
Saturday; the Dymer strike and the House recount confirmation are Monday.
All are "happened, or first reported, on 23 November" per the contest's
rule, and nothing in the image predates 13 November 2026. Label the image
"MONDAY 23 NOVEMBER 2026".

## Design plan (from the 21 Nov entry's lessons)

Front page, 1024×1024 PNG, drawn from scratch with PIL (flat vector,
DejaVu Sans Bold — do NOT copy the previous entry's draw script; write a
fresh builder). Masthead "THE WORLD TODAY" + date. Hero panel: COP31
(cracked globe). 2×2 grid: Iran war, Ukraine, US House, Gaza. Bottom
ticker: Nvidia/AI + Delta + El Chapo. Re-read the render twice; watch for
headline/deck overflow in cards and footer cutoff (the two defects fixed
on 21 Nov). Keep text short, large, high contrast. No photos, no
screenshots, no copied artwork.
