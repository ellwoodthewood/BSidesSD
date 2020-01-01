Flashed bootloader with SEGGER JLink. Connected vref, reset, swdio, swclk, and gnd. Power is supplied by USB.

Pre-built bootloaders available here: https://github.com/adafruit/uf2-samdx1/releases use "trinket_m0"

Used `JFlashLite` to flash the UF2 bootloader pre-compiled from Adafruit.

After reset red led pulses quickly - seems to indicate in bootloader mode but no drive mounted.

`dmesg` output:
```
[178777.669750] usb 1-1-port1: Cannot enable. Maybe the USB cable is bad?
[178778.521747] usb 1-1-port1: Cannot enable. Maybe the USB cable is bad?
[178778.522555] usb 1-1-port1: attempt power cycle
[178779.693608] usb 1-1-port1: Cannot enable. Maybe the USB cable is bad?
[178780.545718] usb 1-1-port1: Cannot enable. Maybe the USB cable is bad?
[178780.546497] usb 1-1-port1: unable to enumerate USB device
```

Found D+ and D- shorted. Isolated to pins 2 & 3 on microUSB connector (not surprised).

Confirmed short removed. Mass storage device mounted from UF2 bootloader. Excelsior! 

Downloaded CircuitPython 5.0.0-beta2 from: https://circuitpython.org/board/trinket_m0/

Copied .uf2 file to **TRINKETBOOT** drive that was mounted. Red LED flashes then new drive **CIRCUITPY** mounted.

Contents to `boot_out.txt` file on drive contains:

```
Adafruit CircuitPython 5.0.0-beta.2 on 2019-12-20; Adafruit Trinket M0 with samd21e18
```

First LED turns green (then yellow later). This should not work as Trinket M0 has APA102 not WS2812B LEDs. Need to write some python now.

Needed Neopixel library. Added neopixel.mpy to **lib/** directory.

Able to control LEDs 2 to 5 but LED 1 still green/yellow/white clearly getting some noise

First LED not due to noise. This is python code crashing/returning to circuitpython control where an APA102 LED is expected thus bad data is sent. Will create an issue to custom build CP for our WS2812B trinket m0.
