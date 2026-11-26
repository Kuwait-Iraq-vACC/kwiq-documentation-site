---
title: Tag Items
---

Add the plugin's items to your tags and lists in the usual way. They are listed under **KWIQ Controller Plugin**.

## Tag Items
| Tag Item | Shows |
| -------- | ----- |
| FPC | The [flight plan check](Route%20Checks.md#flight-plan-check-fpc): `OK`, `VFR`, what failed, or `EVT` for an event flight |
| SRD | The same as FPC. It is kept so existing tag layouts still work |
| Event Route | `OK` (green) or `CHK` (red) on event days, for event city pairs |
| Event Flag | `EV` if the pilot has a VATCAN slot |
| Event Slot | The pilot's slot time |
| Sector Indicator | The [sector](#sector-indicators) of the controller tracking the aircraft |
| RDF state | `!` while the aircraft is transmitting |
| Vertical Speed Indicator | `+` climbing, `-` descending or level |
| Vertical Speed | The vertical speed in hundreds of feet per minute: `+10` is 1,000 ft/min up, `-15` is 1,500 ft/min down, and level flight is `-00` |

The vertical speed items always show something, even when there is no radar target. They are drawn in TopSky's tag colours for the aircraft's state, read from your `TopSkySettings.txt`, so they match the rest of the tag.

## Tag Functions
| Tag Function | What it does |
| ------------ | ------------ |
| Explain FPC result | Explains the FPC result in its own **KWIQ FPC** chat tab |
| Open FPC menu | Opens the **Check FP** menu: show the checks, or disable the check for this flight |
| Explain SRD result | The same as Explain FPC result |
| Open event routes window | Lists today's event routes |
| Open SRD search window | Opens the SRD search, filled in from the flight plan |
| Open squawk assignment menu | Assigns a new [squawk](Squawk%20Assignment.md) from the vACC, or lets you type one |
| Force squawk recycle | Assigns a new squawk from the vACC straight away |

We recommend these left-click functions:

| Tag Item | Left-click function |
| -------- | ------------------- |
| FPC | Explain FPC result, or Open FPC menu |
| SRD | Explain SRD result |
| Event Route | Open event routes window |
| Assigned Squawk | Open squawk assignment menu |

**Open SRD search window** can go on any item.

## Sector Indicators
The plugin draws a short sector indicator above each aircraft tracked by a controller whose position has one, such as **SR** for ORBB_S_CTR. This shows at a glance who is working each aircraft.

The indicators are set by the vACC for each sector file, and follow the position EuroScope identifies the controller as. A relief callsign, or a controller covering a listed position, shows that position's indicator.

Each indicator is drawn in the colour of the aircraft's tag, taken from your profile's Symbology file. The same text is available in tags as the **Sector Indicator** item. Turn the indicators on the radar screen on or off from the KWIQ button, or with `.kwiq sector`.

## VCH
VCH is built in. Its tag items and functions, such as Pending request, Hold Short, CTL and Reminder, keep their original names. See [VCH on GitHub](https://github.com/DrFreas/VCH "Opens in a new tab"){target="_blank"} for how to set them up.
