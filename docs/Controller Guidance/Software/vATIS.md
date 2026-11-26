---
title: vATIS
---

vATIS is the only approved ATIS client in the Kuwait & Iraq vACC.

## Installing the Profiles

vATIS **4.1.0-beta.21 or newer** is required. Older versions don't support the conditional messages and formatting the profiles use.

| Profile | Stations | Download |
| ------- | -------- | -------- |
| OKAC – Kuwait | OKKK, OKAS | [OKAC.json](https://raw.githubusercontent.com/Kuwait-Iraq-vACC/kwiq-vATIS-Profiles/refs/heads/main/OKAC/OKAC.json "Opens in a new tab"){target="_blank"} |
| ORBB – Baghdad | ORBI, ORER, ORMM, ORNI | [ORBB.json](https://raw.githubusercontent.com/Kuwait-Iraq-vACC/kwiq-vATIS-Profiles/refs/heads/main/ORBB/ORBB.json "Opens in a new tab"){target="_blank"} |

1. Right-click the link and choose **Save link as**.
2. In vATIS, open **Profiles → Import** and select the file.

The profiles update automatically each time vATIS starts. Any changes you make to a station locally are overwritten by the next update, so suggest permanent changes on [GitHub](https://github.com/Kuwait-Iraq-vACC/kwiq-vATIS-Profiles "Opens in a new tab"){target="_blank"} instead.

## Selecting a Preset

Select the preset that matches the runway configuration in use. Preset names follow the runway configurations and modes in each aerodrome's SOP.

### Kuwait (OKKK)

| Preset | Arrivals | Departures |
| ------ | -------- | ---------- |
| 34 ARR \| 33L DEP | 34 | 33L |
| 16 ARR \| 15R DEP | 16 | 15R |
| 34 \| SRO | 34 | 34 |
| 16 \| SRO | 16 | 16 |
| 33L \| SRO | 33L | 33L |
| 15R \| SRO | 15R | 15R |
| 34/33L \| DUAL ARRDEP | 34, 33L | 34, 33L |
| 16/15R \| DUAL ARRDEP | 16, 15R | 16, 15R |

The OKKK ATIS uses the same format as the real Kuwait D-ATIS:

```
OKKK ARR ATIS B
0852Z ARR RWY34 DEP RWY33L TRL FL150
WIND 010/11KT CAVOK T41 DP11 QNH 1010HPA
NOSIG
CONFIRM ATIS B
```

### Baghdad FIR

The Baghdad FIR stations use a standard ICAO layout, because Iraq has no real-world D-ATIS. Preset letters are the same as the runway modes in the SOPs:

- **ORBI:** Modes A–F, see [Baghdad Tower](../../Baghdad%20FIR/Aerodrome/ORBI%20-%20Baghdad/Baghdad%20Tower.md). Modes A and C add `RWY33L` / `RWY15R FOR VFR AND MIL TFC ONLY`.
- **ORER:** Mode A (18), Mode B (36) and Mode A LVP, see [Erbil Tower](../../Baghdad%20FIR/Aerodrome/ORER%20-%20Erbil/Erbil%20Tower.md).
- **ORNI:** Modes A–D, see [Al-Najaf Tower](../../Baghdad%20FIR/Aerodrome/ORNI%20-%20Al-Najaf/Al-Najaf%20Tower.md). Modes A and B add `OPPOSITE DIRECTION OPS IN PROGRESS`.
- **ORMM:** 32 (preferential, ILS) or 14 (visual approach).

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

## Automatic Messages

Some airport conditions switch on and off by themselves, based on who is online or on the METAR. **Leave them ticked** and don't type them into the free text as well. A ticked message that has a condition only appears while that condition is met.

| Station | Message | Shown when |
| ------- | ------- | ---------- |
| OKKK | `ATC CLEARANCE WITH GND 121.7` | GMC-E (**OKKK_E_GND**) is online and DEL is offline |
| OKKK | `ATC CLEARANCE WITH TWR FREQ 118.3` | TWR is online and neither DEL nor GND is |
| All | `LOW VISIBILITY PROCEDURES IN OPERATION` | RVR below 550 m, visibility below 800 m or ceiling below 200 ft |

The ATIS letter does **not** change when a controller logs on or off. The text updates under the same letter.

## Transition Level

The transition level is part of every preset, so controllers don't set it. On the Baghdad FIR stations it changes automatically with the QNH.

| FIR | Transition Altitude | Transition Level |
| --- | ------------------- | ---------------- |
| Kuwait | 13 000 ft | FL150 |
| Baghdad | 14 000 ft | FL160, or FL170 when QNH is below 980 hPa |

## NOTAMs and Remarks

Common NOTAMs, such as OKKK `V4 CLOSED DUE TO MAINTENANCE`, are in each station's NOTAMs list. Tick them when they apply. The OKKK `RWY 33L/15R CLOSED FROM 1700 UTC UNTIL 0100 UTC` NOTAM only appears between 1700Z and 0100Z, even when ticked.

Anything else can be typed into the free text, which appears before the transition level on OKKK and after it on the Baghdad FIR stations.
