---
title: Squawk Assignment
---

Squawk codes are allocated by the vACC, so two controllers never hand out the same one. The range is chosen from your FIR, the departure, the destination and the flight rules.

It works on the live network and on sweatbox. Through a proxy connection, only the codes you ask for are assigned, never automatically.

!!! info
    Squawk assignment is switched on by the vACC. The **Auto Squawk** row in the KWIQ menu shows **Off in Core** until it is.

## Automatic Assignment
The plugin gives a code to aircraft that have none, such as those on 2000, 1200 or 7000:

| Aircraft | Who assigns the code |
| -------- | -------------------- |
| On the ground and untracked | The controller providing Delivery at the departure airport |
| Tracked by you | You, as soon as the plugin sees it without a code |
| In the air and untracked | Nobody. The aircraft gets a code when a controller assumes it |
| On sweatbox | Any aircraft that nobody tracks |

Emergency codes (7500, 7600 and 7700) are never replaced.

A pilot who reconnects within 10 minutes with the same departure, destination and flight rules gets the same code back. If the departure, destination or flight rules change, the next code is a new one.

While the plugin is waiting for a code, the aircraft shows 7000. If no code comes, it tries again a minute later.

Turn automatic assignment on or off with **Auto Squawk** in the KWIQ menu, or `.kwiq squawk`.

## Assigning by Hand
Set **Open squawk assignment menu** as the left-click function on the Assigned Squawk item. The menu has:

- **Assign**: a new code from the vACC. **Force squawk recycle** does the same straight away.
- **Manual**: type a code.

A code you set from the menu, or type in EuroScope, comes back if the pilot reconnects. You can only change the code of aircraft you track, or that nobody tracks.
