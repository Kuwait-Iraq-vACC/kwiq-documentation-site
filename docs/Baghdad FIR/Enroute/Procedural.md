---
title: Procedural
---

A radar control service is provided in all controlled airspace, and along all airways within the Baghdad FIR. The exception is segments of airways in the west of the FIR, within the **North** sector, which have limited radar coverage and are controlled **procedurally**.

## Procedural Segments

| Airway | Segment         | FIR Entry/Exit Point |
|--------|-----------------|----------------------|
| G202   | MODIK - RAPLU   | MODIK (Damascus FIR) |
| L200   | PASIP - GIBUX   | PASIP                |
| R652   | DAXAN - GIBUX   | DAXAN (Jeddah FIR)   |

Although every aircraft is visible on the scope on VATSIM, controllers should apply the procedures on this page within these segments to keep the airspace realistic.

---

## Separation

Aircraft at the same level on the procedural segments are separated **longitudinally** using time and distance estimates rather than radar.

### PASIP - GIBUX (L200)
- All traffic entering the Baghdad FIR via **PASIP** at the same level shall be separated by **80 NM in trail**, constant or increasing, until crossing **GIBUX**.
- All traffic exiting via **PASIP** at the same level shall be separated by **80 NM in trail**, constant or increasing, from **GIBUX** until leaving the FIR.
- **No level changes** are allowed between PASIP and GIBUX.

### MODIK - RAPLU (G202)
- All traffic entering the Baghdad FIR via **MODIK** at the same level shall be separated by **80 NM in trail**, constant or increasing, until crossing **RAPLU**.
- All traffic exiting via **MODIK** at the same level shall be separated by **80 NM in trail**, constant or increasing, from **RAPLU** until leaving the FIR.
- **No level changes** are allowed between MODIK and RAPLU.

### DAXAN - GIBUX (R652)
- All aircraft entering the Baghdad FIR on R652 shall cross **DAXAN at FL270 or below**.
- Between **KASIR and GIBUX**, R652 is only available from **FL285 to FL460**.

---

## Level Restrictions

The following levels are **unavailable** on the procedural segments:

| Airway | Segment       | Unavailable Levels |
|--------|---------------|--------------------|
| G202   | MODIK - RAPLU | FL240 - FL260      |
| G202   | RAPLU - PUSTO | FL245 - FL285      |
| L200   | PASIP - SEVDI | FL240 - FL260      |
| L200   | GIBUX - SILBO | FL245 - FL285      |
| M703   | KASIR - PASIP | FL240 - FL260      |

---

## Position Reports and Estimates

As there is no radar service on these segments, pilots should be asked to report when passing the FIR boundary or the end of the procedural segment.

> Controller: "IAW123, report passing GIBUX"

Controllers can record a pilot's estimate for a point by using the EuroScope `.est` command:

![estimate command.png](img/estimate%20command.png)

Once the aircraft passes the end of the procedural segment (RAPLU or GIBUX), radar identification should be established and a radar control service provided.

> Controller: "IAW123, radar identified"

### Exiting Traffic
For aircraft leaving the FIR via the procedural segments, the radar service should be terminated and the aircraft transferred to the next unit.

!!! phraseology
    **ORBB CTR**: IAW123, radar service terminated, 40 miles east of MODIK, contact Damascus Control [frequency].
