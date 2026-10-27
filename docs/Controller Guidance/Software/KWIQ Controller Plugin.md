---
title: KWIQ Controller Plugin
---

The KWIQ Controller Plugin is the vACC's own EuroScope plugin. It checks flight plans against the SRD and event routes, shows VATCAN event slots, draws sector indicators on the radar screen and warns you when your sector file is out of date. VCH is built in.

Routes, events, sector indicators and settings all come from the vACC, so you don't need to edit any files to keep them up to date.

## Installing the Plugin

The plugin is included in the OKAC and ORBB sector file packages and loads with them, so there is nothing to install. The plugin keeps its own files in `%APPDATA%\KWIQ`.

!!! warning "Don't load VCH separately"
    VCH is built into the KWIQ plugin. Loading VCH as well will give you two copies of its tag items and commands. Remove it from **Other Set → Plug-ins**.

### Updates

Each time EuroScope starts, the plugin checks for a new version. If there is one, a Windows message box asks whether to install it. Click **Yes** and the new version loads straight away, with no restart needed. Click **No** to keep your current version until the next start.

The plugin never interrupts a session to update. Type `.kwiq update` to see whether a newer version is waiting.

A sector file package that comes with an older copy of the plugin doesn't replace a newer version you have already installed.

!!! info
    If the vACC can't be reached when EuroScope starts, the installed version loads as normal.

## Connecting Your API Key

The plugin needs a personal API key from myKWIQ to fetch routes and settings. The first time you start EuroScope without one, the plugin sets it up for you:

1. Your web browser opens on myKWIQ, along with an **API Key Setup** window in EuroScope.
2. Sign in to myKWIQ and click **Connect EuroScope**.
3. The key is sent to the plugin and the setup window closes.

If the browser doesn't open, click **Reopen Browser**. You can start the setup again at any time from **API Key** in the KWIQ button's menu, or with `.kwiq connect`.

To enter a key by hand, copy it from myKWIQ and type `.kwiq key <your key>`. Keys start with `kwiq_`.

!!! tip
    Your key is stored in `%APPDATA%\KWIQ\plugin-key.txt`, not in your EuroScope profile, so it is never shared along with a sector file package or your settings.

## The KWIQ Button

A small red **KWIQ** button sits at the top centre of each radar screen. Click it to open the plugin's menu:

| Menu Item | What it does |
| --------- | ------------ |
| API Key | Shows whether a key is connected, and starts the setup |
| Sector Indicators | Turns the [sector indicators](#sector-indicators) on or off |
| Slot Auto Refresh | Turns automatic VATCAN slot updates on or off |
| Event Routes | Opens the [event routes window](#event-routes-and-slots) |
| SRD Search | Opens the [SRD search window](#srd-search) |
| Sector File | Checks your sector file version |
| Plugin Updates | Checks for a newer plugin version |
| Refresh Data | Downloads routes, events and settings again |
| Status | Shows the plugin's status in the chat |
| Hide Button | Hides the button. Type `.kwiq button` to show it again |

Drag the button to move it. Its position is saved with your settings.

## Tag Items

Add the plugin's items to your tags and lists in the usual way. They are listed under **KWIQ Controller Plugin**.

| Tag Item | Shows |
| -------- | ----- |
| FPC | The flight plan check against the SRD: `OK`, `RTE`, `MIN` or `MAX` |
| Event Route | `OK` or `CHK` on event days, for event city pairs |
| Event Flag | `EV` if the pilot has a VATCAN slot |
| Event Slot | The pilot's slot time |
| Sector Indicator | The sector of the controller tracking the aircraft |

| Tag Function | What it does |
| ------------ | ------------ |
| Explain FPC result | Explains the FPC result in the chat |
| Open event routes window | Lists today's event routes |
| Open SRD search window | Opens the SRD search, filled in from the selected flight plan |

We recommend setting **Explain FPC result** as the left-click function on the FPC item, and **Open event routes window** on the Event Route item.

VCH's tag items and functions keep their original names. See [VCH on GitHub](https://github.com/DrFreas/VCH "Opens in a new tab"){target="_blank"} for how to set them up.

## Flight Plan Check (FPC)

The FPC item compares the filed route and cruising level with the SRD for the departure and destination.

| Result | Meaning |
| ------ | ------- |
| `OK` (green) | The route and level conform to the SRD |
| `RTE` (red) | The filed route doesn't match any SRD route for this pair |
| `MIN` (red) | The route is valid, but the level is below the SRD minimum |
| `MAX` (red) | The route is valid, but the level is above the SRD maximum |
| *Blank* | There is no SRD route for this pair |

A route matches when every waypoint and airway in the SRD route appears in the filed route, in the same order. Extra elements, such as a SID, STAR or an additional waypoint, are allowed. `DCT`, speed/level groups and anything after a `/` are ignored.

If an SRD route exists for the airport pair, only that route is checked. Otherwise, SRD routes between waypoints apply when both waypoints are on the filed route.

Left-click the FPC item (with **Explain FPC result** set) to see the reason in the chat, including the expected routes or the allowed levels.

### SRD Search

The SRD search window finds routes by departure, destination and level. Departure and destination can be airports or waypoints, and any field can be left empty.

Opened from a tag, the search is filled in from that flight plan. Click **Copy** next to a route to copy it to the clipboard. Up to 12 results are shown, so narrow the search if there are more.

## Event Routes and Slots

On an event day, the **Event Route** item shows `OK` (green) if the filed route matches an event route for that city pair, or `CHK` (red) if it doesn't. It is blank for flights that aren't part of the event.

The **event routes window** lists the routes that apply today (UTC), with a **Copy** button for each.

The plugin fetches VATCAN slots by itself using the event's code, so you no longer need to enter a code. The **Event Flag** and **Event Slot** items show which pilots have a slot and when. Slots refresh automatically, which you can turn off from the KWIQ button.

## Sector Indicators

The plugin draws a short sector indicator above each aircraft tracked by a controller who has one, such as **SR** for ORBB_S_CTR or **BGD** for Baghdad Approach. This shows at a glance who is working each aircraft.

The same text is available in tags as the **Sector Indicator** item. Turn the indicators on the radar screen on or off from the KWIQ button, or with `.kwiq sector`.

## Outdated Sector File Alert

Once you log on, the plugin compares your sector file with the current OKAC or ORBB release. If yours is out of date, a red **OUTDATED SCT FILE** box appears in the middle of every radar screen and an alert sound plays. It stays until you update the sector file or log off.

Update to the latest package from the vACC's downloads to clear it.

The plugin reads your version from `Plugins\AIRAC_VERSION.txt` in the sector file package. If it can't find the file, it says so in the chat and doesn't check the version. Tell it where your package is with:

```
.kwiq sectorfile <package folder or AIRAC_VERSION.txt path>
```

Type `.kwiq sectorfile` on its own to go back to finding it automatically. Type `.kwiq alert` to preview the alert for 15 seconds.

## Commands

| Command | What it does |
| ------- | ------------ |
| `.kwiq connect` | Connects your API key through myKWIQ |
| `.kwiq key <key>` | Enters an API key by hand. `.kwiq key` shows which key is in use, `.kwiq key clear` removes it |
| `.kwiq button` | Hides or shows the KWIQ button |
| `.kwiq status` | Shows the plugin version, API key, sector file versions, SRD and event status |
| `.kwiq refresh` | Downloads routes, events and settings again |
| `.kwiq sector` | Turns the sector indicators on the radar screen on or off |
| `.kwiq autorefresh` | Turns automatic slot updates on or off |
| `.kwiq update` | Says whether a newer plugin version is waiting |
| `.kwiq version` | Checks your sector file version |
| `.kwiq sectorfile <path>` | Sets where your sector file package is |
| `.kwiq alert` | Previews the outdated sector file alert |

VCH's own `.vch` commands work as before.

## Troubleshooting

??? question "The chat says the plugin is loaded twice"
    Two copies of the plugin are loaded, so the second one does nothing. Remove one of them in **Other Set → Plug-ins**.

??? question "The chat says this copy of the plugin cannot update itself"
    You have loaded the plugin's internal file, `KWIQPluginCore.dll`, instead of `KWIQPlugin.dll`. Remove it in **Other Set → Plug-ins** and reinstall the latest sector file package.

??? question "Core did not accept your API key"
    Your key is no longer valid, for example because it was removed on myKWIQ. Connect it again from the KWIQ button, or with `.kwiq connect`.

??? question "The tag items are blank"
    The FPC and Event Route items are blank when there is no SRD or event route for the flight. If every item is blank, type `.kwiq status`. If it says **DISABLED by Core**, the plugin has been switched off by the vACC or your version is too old. Restart EuroScope to update.

??? question "Cannot tell whether your sector file is OKAC or ORBB"
    Use `.kwiq sectorfile` with the path to your package folder, or to its `Plugins\AIRAC_VERSION.txt`.
