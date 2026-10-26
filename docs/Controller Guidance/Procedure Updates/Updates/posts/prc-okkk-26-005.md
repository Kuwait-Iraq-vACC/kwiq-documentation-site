---
date: 2026-10-26
categories:
  - Procedure Changes
tags:
  - OKKK
---

# PRC-OKKK-26-005 — Kuwait (OKKK) vATIS Profile Update

<div class="brief" markdown>

| Reference                     | PRC-OKKK-26-005                                   |
| ----------------------------- | ------------------------------------------------- |
| **Effective Date**            | 26/10/2026                                        |
| **Status**                    | <span class="status status--active">Active</span> |
| **Applies To**                | OKKK (ATIS), all OKKK positions                   |
| **Docs Updated**              | Yes                                               |

</div>

<!-- more -->

## Summary

The OKKK ATIS now uses the format of the real Kuwait D-ATIS. The preset names and some airport conditions have changed, and a few messages now switch on and off by themselves.

```
OKKK ARR ATIS B
0852Z ARR RWY34 DEP RWY33L TRL FL150
WIND 010/11KT CAVOK T41 DP11 QNH 1010HPA
NOSIG
CONFIRM ATIS B
```

| Old Preset | New Preset |
| ---------- | ---------- |
| ~~33L DEP \| 34 ARR~~ | **34 ARR \| 33L DEP** |
| ~~15R DEP \| 16 ARR~~ | **16 ARR \| 15R DEP** |
| ~~33L/34 \| DUAL RWY CONFIG~~ | **34/33L \| DUAL ARRDEP** |
| ~~15R/16 \| DUAL RWY CONFIG~~ | **16/15R \| DUAL ARRDEP** |

The SRO presets (34, 16, 33L, 15R) keep their names.

## Controller Actions

- **Use vATIS 4.1.0-beta.21 or newer.** The OKAC profile updates automatically when vATIS starts.
- **Select the preset** for the runway configuration in use.
- **Leave the automatic messages ticked:**
  - `ATC CLEARANCE WITH GND 121.7` appears while GMC-E (**OKKK_E_GND**) is online and DEL is offline.
  - `ATC CLEARANCE WITH TWR FREQ 118.3` appears while TWR is online and neither DEL nor GND is.
  - `LOW VISIBILITY PROCEDURES IN OPERATION` appears when the METAR meets LVP conditions.
  - Don't type these into the free text.
- **Tick NOTAMs from the list when they apply**, such as `V4 CLOSED DUE TO MAINTENANCE`. The `RWY 33L/15R CLOSED FROM 1700 UTC UNTIL 0100 UTC` NOTAM only appears between 1700Z and 0100Z.
- **Pilots are asked to confirm the ATIS letter** (`CONFIRM ATIS B`), as on the real D-ATIS. The clearance procedure is unchanged.

## Documentation Status

A new [vATIS](../../../Software/vATIS.md) page has been added under Controller Guidance → Software.

---

Spotted an error, or want to suggest a change? Email [operations@kuwait-iraqvacc.net](mailto:operations@kuwait-iraqvacc.net?subject=Documentation%20Change%20-%20PRC-OKKK-26-005)
