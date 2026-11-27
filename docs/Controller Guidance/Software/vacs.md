---
title: vacs
---

vacs is an open source communication system for controller-to-controller coordination on VATSIM. It replaces typing in private chat with a quick phone call to your neighbour.

vacs is strongly recommended whenever you control in the Kuwait & Iraq vACC. Both the Kuwait (OKAC) and Baghdad (ORBB) layouts are built in, so there is nothing extra to download.

## Installing

1. Go to [vacs.network](https://vacs.network/ "Opens in a new tab"){target="_blank"}.
2. Under **Download latest**, click **Windows**.
3. Run the installer and launch vacs.

macOS and Linux downloads are on the same page.

## First-Time Setup

Open **Settings** and set these up before your first session:

1. **Audio:** Choose your headset as the input and output device.
2. **Transmit mode:** Choose **Push-to-Talk** and bind a key. This is the key you hold to talk on a call.
3. **Radio integration:** Choose **TrackAudio** if you use [TrackAudio](../Audio%20Clients/TrackAudio.md). vacs then handles your radio PTT too.

!!! warning
    If you use the TrackAudio integration, don't set the same key as PTT inside TrackAudio as well, or the two will conflict.

## Connecting

1. Log in to VATSIM in EuroScope and set your primary frequency.
2. In vacs, press **Login via VATSIM** and sign in with your VATSIM account.
3. Press **Connect**.

vacs loads the OKAC or ORBB layout automatically. Online positions appear as keys along the bottom of the screen.

## Making a Call

1. Click the key of the position you want to call. Keys with **black** text are online.
2. The indicator in the top-left turns **orange** while ringing and **green** once you're connected.
3. Press **END** to hang up.

For anything time-critical, press **PRIO** first, then click the position. The other controller hears a different ring and sees a yellow border.

!!! tip
    Only use **PRIO** when the coordination is genuinely urgent, such as a conflict or a missed release.

## Receiving a Call

1. A **flashing green** key shows who is calling.
2. Click it to answer.
3. Press **END** to hang up.

To decline, simply don't answer. The call ends on its own.

## More Help

The full [vacs documentation](https://docs.vacs.network/ "Opens in a new tab"){target="_blank"} covers conference calls, all settings and troubleshooting.