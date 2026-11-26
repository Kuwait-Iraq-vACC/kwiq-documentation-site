---
title: Route Checks
---

The plugin checks flight plans against the vACC's SRD and event routes. Both come from the vACC, so they are always current.

## Flight Plan Check (FPC)
The **FPC** item checks the filed route, cruising level and equipment against the vACC's rules for the departure airport. The **SRD** item shows the same result.

| Result | Meaning |
| ------ | ------- |
| `OK` (green) | The flight plan conforms |
| `VFR` | The flight is VFR, so it isn't checked |
| `SID` | The SID has rules of its own, and the flight fits none of them |
| `RTE` | The filed route isn't valid out of this airport |
| `ENG` | The engine type isn't allowed on this route |
| `E/O` | The cruising level should be even, or odd |
| `MIN` | The level is below the lowest allowed |
| `MAX` | The level is above the highest allowed |
| `FLR` | The level isn't allowed on this route. Shown in yellow when it is the only failure |
| `NAV` | The aircraft's equipment isn't allowed on this route |
| `EVT` (orange) | An event flight that isn't on its event route |
| `EVT` (green) | An event flight on its event route |
| `-` (grey) | The check is disabled for this flight |
| *Blank* | There are no rules for this airport |

With more than one failure, the item cycles through them, two seconds each.

The route is only checked up to the first FIR exit point on it, whether internal (between OKAC and ORBB) or external. What is filed after that isn't ours to check. `DCT`, speed/level groups, and the aerodrome's VOR at either end of the route (left out by pilots who file a SID or STAR) don't count.

### Explaining a Result
**Explain FPC result** lists everything that was checked in its own **KWIQ FPC** chat tab, including the routes and levels that are allowed. For example:

```
route not valid out of ORBI, it must follow one of: NAMDI M860 NINVA / TAGRU L718 KABAN / NOLDO B411 PAXAT
```

**Open FPC menu** opens the **Check FP** menu:

- **Show Checks** is the same as Explain FPC result.
- **Disable** turns the check off for that flight, so its FPC item shows a grey `-`. **Enable** turns it back on. A flight stays disabled until its flight plan disconnects.

### Event Flights
On an event day, a flight with an event route for its departure and destination shows `EVT` instead of the usual result: green if the filed route is exactly one of the event routes, or orange if it isn't. Only a SID, STAR, `DCT`, speed/level changes and the aerodrome's VOR may differ. An extra point, a missing one or another order shows orange `EVT`. **Explain FPC result** says which event route was expected.

## SRD Search
The SRD search window finds routes between two airports or waypoints. Open it with **SRD Search** in the KWIQ menu, or with **Open SRD search window** on any tag item.

1. Enter the **Origin Fix or Airfield** and the **Destination Fix or Airfield**.
2. Optionally, enter the **Cruising Altitude or Level**: `350` is FL350, `35000` is feet.
3. Select **Search**, or press ++enter++.

Opened from a tag, the search is filled in from that flight plan and runs straight away. For a flight leaving the vACC's airspace, the destination is the first FIR exit point on its route.

The **Search Results** show each route's **Min** level (`MC` when there is no minimum), **Max** level (`-` when there is no limit), whether it includes Free Route Airspace (**FRA**), and the **Route String**. Click a route to see its **Notes**, then select **Copy Route String To Clipboard**.

EuroScope keeps running while the window is open. Close it with **Close** or ++esc++.

## Event Routes and Slots
On an event day, the **Event Route** item shows `OK` (green) if every point of an event route for that city pair is on the filed route, in order, or `CHK` (red) if not. It is blank for flights that aren't part of the event.

The **event routes window** lists the event's routes for today (UTC), with the **Airports** and **Route String** of each. Open it with **Event Routes** in the KWIQ menu, or **Open event routes window** on the Event Route item. Select a route and use **Copy Route String To Clipboard**.

### VATCAN Slots
The plugin fetches VATCAN slots itself, using the event's code from the vACC, so you no longer need to enter a code or load the VATCAN Bookings plugin. The **Event Flag** item shows `EV` for pilots with a slot, and the **Event Slot** item shows their slot time.

Slots refresh automatically. Turn this off with **Slot Auto Refresh** in the KWIQ menu, or `.kwiq autorefresh`.
