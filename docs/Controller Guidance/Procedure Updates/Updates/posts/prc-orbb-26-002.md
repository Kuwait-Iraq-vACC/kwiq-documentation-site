---
date: 2026-10-26
categories:
  - Procedure Changes
tags:
  - ORBB
---

# PRC-ORBB-26-002 — Baghdad FIR vATIS Profile Update

<div class="brief" markdown>

| Reference                     | PRC-ORBB-26-002                                   |
| ----------------------------- | ------------------------------------------------- |
| **Effective Date**            | 26/10/2026                                        |
| **Status**                    | <span class="status status--active">Active</span> |
| **Applies To**                | ORBI, ORER, ORMM, ORNI (ATIS)                     |
| **Docs Updated**              | Yes                                               |

</div>

<!-- more -->

## Summary

The Baghdad FIR ATIS stations now use a standard ICAO layout, because Iraq has no real-world D-ATIS. The presets now follow the runway modes in the SOPs, and the transition level follows AIP Iraq ENR 1.7.

```
ORBI ATIS INFO K 0300Z
EXPECT ILS APCH RWY33R OR RNP APCH RWY33L
DEP RWY33R OR RWY33L
TRL FL160
WIND 140/12KT
VIS 4000M DU
CLD SCT 4000 BKN 10000 CB
T22 DP09
QNH 1004HPA
TEMPO 3000 TSRA
CONFIRM ATIS K
```

The old preset letters didn't match the SOPs. Select presets by their new names:

| Station | Old Preset | New Preset |
| ------- | ---------- | ---------- |
| ORBI | MODE A: 33R | **MODE A: 33R** (33L VFR/MIL only) |
| ORBI | — | **MODE B: 33R** |
| ORBI | ~~MODE B: 15L~~ | **MODE C: 15L** (15R VFR/MIL only) |
| ORBI | — | **MODE D: 15L ARR \| 15L/R DEP** |
| ORBI | ~~MODE C: 33L/R~~ | **MODE E: 33L/R** |
| ORBI | ~~MODE D: 15L/R~~ | **MODE F: 15L/R** |
| ORER | ~~18~~ | **MODE A: 18** |
| ORER | ~~36~~ | **MODE B: 36** |
| ORER | ~~LVP 18~~ | **MODE A: 18 LVP** |
| ORNI | — | **MODE A: 28 ARR \| 10 DEP** |
| ORNI | — | **MODE B: 10 ARR \| 28 DEP** |
| ORNI | ~~MODE A: 28~~ | **MODE C: 28** |
| ORNI | ~~MODE B: 10~~ | **MODE D: 10** |

ORMM keeps its 32 and 14 presets.

## Controller Actions

- **Use vATIS 4.1.0-beta.21 or newer.** The ORBB profile updates automatically when vATIS starts.
- **Select the preset** for the runway mode in use. The mode letter on the ATIS now matches the SOP.
- **Don't set the transition level.** It is TRL FL160, changing to FL170 when QNH is below 980 hPa (TA 14 000 ft).
- **Leave `LOW VISIBILITY PROCEDURES IN OPERATION` ticked.** It only appears when the METAR meets LVP conditions.
- **Ask pilots to confirm the ATIS letter on first contact.** The ATIS now ends with `CONFIRM ATIS` and asks them to confirm it to Ground, or Tower at ORER.

## Documentation Status

A new [vATIS](../../../Software/vATIS.md) page has been added under Controller Guidance → Software.

---

Spotted an error, or want to suggest a change? Email [operations@kuwait-iraqvacc.net](mailto:operations@kuwait-iraqvacc.net?subject=Documentation%20Change%20-%20PRC-ORBB-26-002)
