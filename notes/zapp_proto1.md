Flashed bootloader with SEGGER JLink. Connected vref, reset, swdio, swclk, and gnd. Power is supplied by USB.

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
