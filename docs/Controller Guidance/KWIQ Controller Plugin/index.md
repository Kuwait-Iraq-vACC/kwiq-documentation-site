---
title: KWIQ Controller Plugin
---

The KWIQ Controller Plugin is the Kuwait & Iraq vACC's own EuroScope plugin. It comes with the OKAC and ORBB sector files, so there is nothing to download separately.

It brings together:

- [Route checks](Route%20Checks.md): the flight plan check (FPC), SRD search, and event routes and VATCAN slots
- [Squawk assignment](Squawk%20Assignment.md), with codes allocated by the vACC so that no two controllers hand out the same one
- [Tag items](Tag%20Items.md), including sector indicators and vertical speed
- [RDF and the TrackAudio bridge](RDF%20and%20TrackAudio.md)
- [Procedure notifications and the pressure monitor](Notifications%20and%20Pressure%20Monitor.md)
- VCH and DiscordEuroScope, both built in
- Checks that your sector file and EuroScope version are current

Routes, events, sector indicators and settings all come from the vACC, so you don't need to edit any files to keep them up to date.

!!! warning "Don't load the built-in plugins separately"
    VCH, RDF (and afv-euroscope-bridge) and DiscordEuroScope are built into the KWIQ plugin. Loading them as well gives you two copies of their tag items and commands. Remove `VCH.dll`, `RDFPlugin.dll` and `DiscordEuroscope.dll` from **Other Set → Plug-ins** if you have them. The VATCAN Bookings plugin isn't needed either: slots now come through the KWIQ plugin.

## Installing
The sector file packages load `KWIQPlugin.dll` for you. It is the only file EuroScope loads.

The first time EuroScope starts with it, a **KWIQ First Time Download** box says the plugin will download its components. Select **OK**: the plugin is installed in `%LOCALAPPDATA%\KWIQ` and starts straight away.

If the download fails, the plugin says so, does nothing for that session and tries again the next time EuroScope starts.

## Your API Key
The plugin needs your personal API key from myKWIQ to fetch routes and settings. Home and visiting controllers, and anyone training with the vACC, can get one. Whenever there is no key, the plugin sets it up for you:

1. myKWIQ opens in your browser, along with an **API Key Setup** box in EuroScope.
2. Sign in to myKWIQ and select **Connect EuroScope**.
3. The box closes once your key is connected.

If no browser opens, the link is on your clipboard: paste it into your browser. Select **OK** in the setup box to open the page again. You can start the setup at any time from **API Key** in the [KWIQ menu](#the-kwiq-button), or with `.kwiq connect`.

To enter a key by hand, copy it from myKWIQ (**EuroScope Plugin**) and type `.kwiq key <your key>`.

!!! tip
    Your key is kept in `%LOCALAPPDATA%\KWIQ\settings`, not in your EuroScope profile, so it is never shared along with a sector file package or your settings.

!!! info "EuroScope on a Mac or Linux"
    The setup also works with EuroScope through Wine or CrossOver: the link opens in your system browser.

## Updates
Each time EuroScope starts, the plugin checks for a new version. When there is one, a **KWIQ Automatic Update** box asks whether to install it. Select **Yes**: the new version starts straight away, with no restart needed, and you are offered the [changelog](Changelog.md).

!!! warning "Updates are required"
    If you decline twice, EuroScope starts with only the outdated sector file alert and the EuroScope version check working. There are no tag items (VCH's included), menu or commands until you restart EuroScope and accept the update.

The plugin never interrupts a session to update. Type `.kwiq update` to see whether a newer version is waiting. If the vACC can't be reached when EuroScope starts, the installed version loads as normal.

## The KWIQ Button
The vACC's logo sits in the bottom-right corner of each radar screen. Click it (left or right) to open the plugin's menu:

| Menu Item | What it does |
| --------- | ------------ |
| API Key | Shows whether a key is connected, and starts the setup |
| Sector Indicators | Turns the [sector indicators](Tag%20Items.md#sector-indicators) on or off |
| RDF Drawing | Turns [RDF](RDF%20and%20TrackAudio.md) drawing on or off for yourself |
| TrackAudio | Shows the [TrackAudio bridge](RDF%20and%20TrackAudio.md#the-trackaudio-bridge)'s connection. Click it to sync the channels again |
| DiscordEuroScope | Turns [Discord Rich Presence](#discordeuroscope) on or off for yourself |
| Notifications | Lists [procedure notifications](Notifications%20and%20Pressure%20Monitor.md) and how many are unread |
| Slot Auto Refresh | Turns automatic VATCAN slot updates on or off |
| Auto Squawk | Turns [automatic squawk assignment](Squawk%20Assignment.md) on or off |
| Event Routes | Opens the [event routes window](Route%20Checks.md#event-routes-and-slots) |
| SRD Search | Opens the [SRD search window](Route%20Checks.md#srd-search) |
| Sector File | Checks your sector file version |
| Plugin Updates | Checks for a newer plugin version |
| Refresh Data | Downloads routes, events and settings again |
| Status | Shows the plugin's status in the chat |
| Hide Button | Hides the button. Type `.kwiq button` to show it again |

Drag the button anywhere on the radar screen. Its place is saved in your profile, and it follows the window as it is resized.

## Outdated Sector File Alert
Once you log on, the plugin compares your sector file with the current OKAC or ORBB release. If yours is out of date, a red **OUTDATED SCT FILE** box flashes in the middle of every radar screen and an alert sound plays. It stays until you install the latest sector file or log off.

The plugin reads your version from `Plugins\AIRAC_VERSION.txt` in the sector file package. If it can't find the file, it doesn't check the version. Tell it where your package is with:

```
.kwiq sectorfile <package folder or AIRAC_VERSION.txt path>
```

Type `.kwiq sectorfile` on its own to go back to finding it automatically. Type `.kwiq alert` to preview the alert for 15 seconds.

## EuroScope Version Check
As EuroScope starts, the plugin checks that you are using the [approved EuroScope version](../Software/EuroScope%20Setup.md). On any other version, an **Incorrect EuroScope Version** box says so, and **OK** opens the EuroScope setup guide. `.kwiq status` shows your EuroScope version.

## DiscordEuroScope
DiscordEuroScope (Discord Rich Presence) is built in and on by default. It shows your position, frequency and traffic on your Discord profile, with messages and buttons set by the vACC. Turn it off for yourself with **DiscordEuroScope** in the KWIQ menu, `.kwiq discord` or the [Configurator](../Software/Configurator.md).

## Commands
| Command | What it does |
| ------- | ------------ |
| `.kwiq status` | Shows the plugin version, API key, sector file and EuroScope versions, and what has been downloaded |
| `.kwiq connect` | Connects your API key through myKWIQ |
| `.kwiq key <key>` | Enters an API key by hand. `.kwiq key` says whether one is connected, `.kwiq key clear` removes it |
| `.kwiq refresh` | Downloads routes, events and settings again |
| `.kwiq update` | Says whether a newer plugin version is waiting |
| `.kwiq version` | Checks your sector file version |
| `.kwiq sectorfile <path>` | Tells the plugin where your sector file package is, if it can't find it |
| `.kwiq alert` | Previews the outdated sector file alert |
| `.kwiq button` | Hides or shows the KWIQ button |
| `.kwiq sector` | Turns the sector indicators on or off |
| `.kwiq autorefresh` | Turns the slot auto refresh on or off |
| `.kwiq squawk` | Turns automatic squawk assignment on or off |
| `.kwiq qnh <ICAO>` | Shows an airport's QNH and transition level |
| `.kwiq notifications` | Lists procedure notifications |
| `.kwiq discord` | Turns DiscordEuroScope on or off for yourself |
| `.kwiq log` | Opens the folder of the [plugin's log](#the-plugins-log). `.kwiq log verbose` adds more detail until EuroScope restarts |
| `.rdf draw on`, `off` or `core` | Turns RDF drawing on or off for yourself, or back to the vACC's setting |
| `.rdf refresh` | Syncs the voice channels from TrackAudio again |
| `.rdf reload` | Reconnects to TrackAudio |

VCH's own `.vch` commands work as before.

## The Plugin's Log
The plugin keeps its own log next to `KWIQPlugin.dll` in the sector file package, or in `%LOCALAPPDATA%\KWIQ\logs` if it can't write there. There is one file per day, kept for 7 days. Type `.kwiq log` to open the folder.

If something isn't working, send the log with your report. Your API key is never written to it.

## Troubleshooting
??? question "The plugin is reduced and only the sector file alert works"
    You declined an update. Restart EuroScope and select **Yes** when asked to update.

??? question "The API Key Setup box keeps coming back"
    Your key is missing, or no longer valid, for example because it was removed on myKWIQ. Sign in to myKWIQ and select **Connect EuroScope**, or type `.kwiq connect`. If you have left the roster or are suspended, the plugin only says so in the chat.

??? question "The tag items are blank"
    The FPC and Event Route items are blank when there are no rules or event routes for the flight. If every item is blank, type `.kwiq status`. If it says the plugin is **DISABLED**, it has been switched off by the vACC or your version is too old. Restart EuroScope to update.

??? question "The KWIQ plugin is loaded twice"
    Two copies of `KWIQPlugin.dll` are loaded, for example one from OKAC and one from ORBB, so the second does nothing. Remove one of them in **Other Set → Plug-ins**.

??? question "This copy of the plugin cannot update itself"
    You have loaded `KWIQPluginCore.dll` instead of `KWIQPlugin.dll`. Remove it in **Other Set → Plug-ins** and load `KWIQPlugin.dll` from your sector file package, or download it again from myKWIQ (**EuroScope Plugin**).

??? question "RDF is off, because another RDF plugin or afv-euroscope-bridge is loaded"
    RDF is built in. Remove `RDFPlugin.dll` or afv-euroscope-bridge in **Other Set → Plug-ins** and restart EuroScope.

??? question "VCH's tag items and commands are there twice"
    VCH is loaded on its own as well. Remove `VCH.dll` in **Other Set → Plug-ins**.

??? question "The plugin can't tell whether your sector file is OKAC or ORBB"
    Use `.kwiq sectorfile` with the path to your package folder, or to its `Plugins\AIRAC_VERSION.txt`.

## Help
Ask in our [Discord server](https://discord.kuwait-iraqvacc.net).
