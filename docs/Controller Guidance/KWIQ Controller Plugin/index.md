---
title: KWIQ Controller Plugin
---

The KWIQ Controller Plugin is the Kuwait & Iraq vACC's EuroScope plugin. It comes with the OKAC and ORBB sector files, so there is nothing to download separately.

It covers event routes and VATCAN slots, the flight plan check against the SRD, SRD search, sector indicators, VCH (built in), and checks that your sector file and EuroScope version are current.

!!! info "One plugin"
    Do not load VCH separately: it is built into the KWIQ Controller Plugin.

## Installing
The sector file packages load `KWIQPlugin.dll` for you. The first time EuroScope starts with it, you are asked to allow a first time download. Select **OK**: the plugin is installed in `%LOCALAPPDATA%\KWIQ` and starts straight away.

## Your API key
The plugin needs your personal API key from myKWIQ. When there is no key, the plugin opens myKWIQ in your browser with an **API Key Setup** window:

1. Sign in to myKWIQ.
2. Select **Connect EuroScope**.
3. The window closes once your key is connected.

If no browser opens, the link is on your clipboard: paste it into your browser. You can also copy the key from myKWIQ (EuroScope Plugin) and type `.kwiq key <your key>`.

## Updates
When a new version is available, you are asked as EuroScope starts. Select **Yes** to update. The new version starts straight away, and you can view the [changelog](Changelog.md).

!!! warning "Declining an update"
    Updates are required. If you decline twice, EuroScope starts with only the outdated sector file alert and the EuroScope version check working. Restart EuroScope and accept the update to use everything else.

## The KWIQ button
The small red **KWIQ** button at the top of each radar screen opens the plugin's menu: API key, sector indicators, slot auto refresh, event routes, SRD search, sector file and update checks, refresh and status. Drag it to move it. **Hide Button** hides it, and `.kwiq button` brings it back.

## Commands
| Command | What it does |
| ------- | ------------ |
| `.kwiq status` | Shows the plugin's status |
| `.kwiq connect` | Connects your API key through myKWIQ |
| `.kwiq key <key>` | Enters your API key by hand (`.kwiq key clear` removes it) |
| `.kwiq refresh` | Downloads Core's data again |
| `.kwiq version` | Checks your sector file version |
| `.kwiq sectorfile <folder>` | Tells the plugin where your sector file package is, if it cannot find it |
| `.kwiq update` | Says whether a newer version is waiting |
| `.kwiq sector` | Turns the sector indicators on or off |
| `.kwiq autorefresh` | Turns the slot auto refresh on or off |
| `.kwiq button` | Shows or hides the KWIQ button |
| `.kwiq alert` | Previews the outdated sector file alert |

## Outdated sector file
If you log on with an outdated sector file, a red **OUTDATED SCT FILE** box is shown on every radar screen, with an alert sound, until you install the latest sector file or log off.

## Help
Ask in our [Discord server](https://discord.kuwait-iraqvacc.net).
