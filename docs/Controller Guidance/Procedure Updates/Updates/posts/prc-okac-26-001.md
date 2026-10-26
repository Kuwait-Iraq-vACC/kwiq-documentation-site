---
date: 2026-10-26
categories:
  - Procedure Changes
tags:
  - OKAC
---

# PRC-OKAC-26-001 — Kuwait FIR vATIS Profile Update

<div class="brief" markdown>

| Reference                     | PRC-OKAC-26-001                                   |
| ----------------------------- | ------------------------------------------------- |
| **Effective Date**            | 26/10/2026                                        |
| **Status**                    | <span class="status status--active">Active</span> |
| **Applies To**                | OKKK, OKAS (ATIS)                                 |
| **Docs Updated**              | Yes                                               |

</div>

<!-- more -->

## Summary

The Kuwait FIR vATIS profile has been updated. The OKKK ATIS now uses the format of the real Kuwait D-ATIS, the preset names and some airport conditions have changed, and a few messages now switch on and off by themselves.

```
OKKK ARR ATIS B
0852Z ARR RWY34 DEP RWY33L TRL FL150
WIND 010/11KT CAVOK T41 DP11 QNH 1010HPA
NOSIG
CONFIRM ATIS B
```

| Station | Old Preset | New Preset |
| ------- | ---------- | ---------- |
| OKKK | ~~33L DEP \| 34 ARR~~ | **34 ARR \| 33L DEP** |
| OKKK | ~~15R DEP \| 16 ARR~~ | **16 ARR \| 15R DEP** |
| OKKK | ~~33L/34 \| DUAL RWY CONFIG~~ | **34/33L \| DUAL ARRDEP** |
| OKKK | ~~15R/16 \| DUAL RWY CONFIG~~ | **16/15R \| DUAL ARRDEP** |

The OKKK SRO presets (34, 16, 33L, 15R) keep their names.

## Controller Actions

- **Use vATIS 4.1.0-beta.21 or newer.** The OKAC profile updates automatically when vATIS starts.
- **Select the preset** for the runway configuration in use.
- **Don't set the transition level.** It is TRL FL150 (TA 13 000 ft) throughout the Kuwait FIR.
- **Leave the automatic messages ticked:**
    - `LOW VISIBILITY PROCEDURES IN OPERATION` appears on every station when the METAR meets LVP conditions.
    - OKKK: `ATC CLEARANCE WITH GND 121.7` appears while GMC-E (**OKKK_E_GND**) is online and DEL is offline.
    - OKKK: `ATC CLEARANCE WITH TWR FREQ 118.3` appears while TWR is online and neither DEL nor GND is.
    - Don't type these into the free text.
- **Tick NOTAMs from the list when they apply**, such as OKKK `V4 CLOSED DUE TO MAINTENANCE`. The OKKK `RWY 33L/15R CLOSED FROM 1700 UTC UNTIL 0100 UTC` NOTAM only appears between 1700Z and 0100Z.
- **Pilots are asked to confirm the ATIS letter** (`CONFIRM ATIS B`), as on the real D-ATIS. The clearance procedure is unchanged.

## Documentation Status

A new [vATIS](../../../Software/vATIS.md) page has been added under Controller Guidance → Software.

---

Spotted an error, or want to suggest a change? Email [operations@kuwait-iraqvacc.net](mailto:operations@kuwait-iraqvacc.net?subject=Documentation%20Change%20-%20PRC-OKAC-26-001)
