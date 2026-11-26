---
title: Changelog
---

Every release of the KWIQ Controller Plugin, newest first. The plugin offers each one as EuroScope starts.

## 0.8.2

*2026-11-25*

- 0.8.2: vertical speed items in TopSky's colours, quieter squawk log (#107)
- 0.8.1: the plugin log leaves out squawk lines about aircraft far away

## 0.8.1

*2026-11-25*

- Tag items: Vertical Speed Indicator and Vertical Speed

## 0.8.0

*2026-11-24*

- FPC item: orange EVT off the event route, green EVT on it
- FPC item: cycle through every failure
- 0.8.0: the plugin keeps its own log, squawk fixes, SRD first FIR exit, sector colours from Symbology, Discord {event}, RDF on EuroScope's thread
- Squawks: a new code for every tracked aircraft without one, uncorrelated flight plans looked at (0.7.6)
- Sector indicator: the tag's colour from the profile's Symbology file
- SRD search: fill in the first FIR exit point as the destination
- Squawks: a code that doesn't count is always replaced
- Discord: fill {event} for a Core event without routes
- 0.8.0 builds on Windows again: the plugin log reads file names the C++20 way

## 0.7.5

*2026-11-21*

- Squawks: assuming an aircraft on a non-assignable code always gets a new code

## 0.7.4

*2026-11-20*

- FPC: RTE for a wrong route; one route check for the SRD and FPC items
- Let 0.5 copies update to the current version (0.7.4)

## 0.7.3

*2026-11-19*

- Organise the repository into folders
- Sector file aliases, top-down airfield ownership, review fixes, pressure monitor sender
- Sector indicators: use the loaded sector file's aliases
- Top-down airfield ownership, and fixes from the repository review
- Pressure monitor: no KWIQ sender before the message

## 0.7.2

*2026-11-19*

- Update squawk assign, FPC menu and chat tab, FIR exit, add event route EVT

## 0.7.1

*2026-11-19*

- UI split, FPC/SRD fixes, squawk logic changes, bigger SRD search menu
- Squawks: fix assignment bugs, Recycle/Conspicuity, holding code, ask Core on reconnect, sweatbox
- Move the Win32 windows out of KWIQPlugin.cpp into kwiq_ui.cpp/hpp
- FPC and SRD: accept valid flight plans
- SRD Search and Event Routes: open once, and a little larger

## 0.7.0

*2026-11-19*

- RDF: stop checking TrackAudio's version
- Semantic Versioning: version.h, one SemVer comparison, and one release per version

## 0.6.0.165

*2026-11-18*

- Pressure monitor: show TRL only when it changes

## 0.6.0.159

*2026-11-11*

- Squawk assignment: codes from Core

## 0.6.0.156

*2026-11-11*

- FPC as its own check (VFPC rules), SRD check on its own item

## 0.6.0.152

*2026-11-11*

- Event Routes: a standard dialog like SRD Search, instead of a custom window

## 0.6.0.150

*2026-11-11*

- Update SRD Search window

## 0.6.0.142

*2026-11-11*

- Build RDF and its TrackAudio bridge in, with settings from Core
- Build DiscordEuroScope in, configured in Core
- QNH monitor and procedure notifications
- Plain Windows message boxes
- KWIQ button: the vACC's logo, movable, its place saved as an offset from the bottom-right corner
- Bring RDF, DiscordEuroScope, QNH and notifications, message boxes and the logo button into main

## 0.6.0.139

*2026-11-11*

- FPC and SRD search to the FIR exit point

## 0.6.0.131

*2026-11-11*

- Change update/install logic

## 0.5.0.115

*2026-11-10*

- Refinements on main: /W4 check, response cap, web links only, no exceptions into EuroScope

## 0.5.0.97

*2026-11-10*

- Comment on pull requests when their test build is published
- Only release when the plugin's source files change
- Publish the release notes as a changelog on docs.kuwait-iraqvacc.net
- Core requests never follow redirects, so the API key stays with Core

## 0.5.0.56

*2026-10-29*

- Sector aliases by ESE position ID; only the positions Core lists get an indicator

## 0.5.0.43

*2026-10-27*

- Maintenance release.

## 0.5.0.41

*2026-10-27*

- Maintenance release.

## 0.5.0.40

*2026-10-27*

- Maintenance release.

## 0.5.0.39

*2026-10-27*

- Maintenance release.

## 0.5.0.37

*2026-10-27*

- Maintenance release.

## 0.5.0.35

*2026-10-27*

- Show all plugin and VCH messages as KWIQ Controller Plugin

## 0.5.0.32

*2026-10-27*

- Warn controllers on an incorrect EuroScope version

## 0.5.0.29

*2026-10-27*

- Sector indicator from the ESE, in the colour of its tag

## 0.5.0.27

*2026-10-27*

- VATCAN slot fetch: errors only, shown as KWIQ Events Manager

## 0.5.0.19

*2026-10-26*

- Maintenance release.

## 0.5.0.18

*2026-10-26*

- Maintenance release.

## 0.5.0.17

*2026-10-26*

- Maintenance release.

## 0.5.0.16

*2026-10-26*

- Maintenance release.

## 0.5.0.15

*2026-10-26*

- Maintenance release.

## 0.5.0.14

*2026-10-26*

- Maintenance release.

## 0.5.0.13

*2026-10-26*

- Maintenance release.

## 0.5.0.12

*2026-10-26*

- Maintenance release.

## 0.5.0.11

*2026-10-26*

- Maintenance release.

## 0.5.0.9

*2026-10-26*

- Maintenance release.

## 0.5.0.8

*2026-10-26*

- Maintenance release.

## 0.5.0.7

*2026-10-26*

- Maintenance release.

## 0.5.0.6

*2026-10-26*

- Maintenance release.
