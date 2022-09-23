'''
Pyscan NFC library
Copyright (c) 2019, Pycom Limited.

Based on a library for NXP's MFRC630 NFC IC https://github.com/iwanders/MFRC630

The MIT License (MIT)

Copyright (c) 2016 Ivor Wanders

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

import time, binascii

class MFRC630:

    NFC_I2CADDR = const(0x28)
    # commands
    MFRC630_CMD_IDLE = const(0x00)  # (no arguments) ; no action, cancels current command execution. */
    MFRC630_CMD_LPCD = const(0x01)  # (no arguments) ; low-power card detection. */
    MFRC630_CMD_LOADKEY = const(0x02)  # (keybyte1), (keybyte2), (keybyte3), (keybyte4), (keybyte5),
    MFRC630_CMD_MFAUTHENT = const(0x03)  # 60h or 61h, (block address), (card serial number byte0), (card
    MFRC630_CMD_RECEIVE = const(0x05)  # (no arguments) ; activates the receive circuit. */
    MFRC630_CMD_TRANSMIT = const(0x06)  # bytes to send: byte1, byte2, ...;  transmits data from the FIFO
    MFRC630_CMD_TRANSCEIVE = const(0x07)  # bytes to send: byte1, byte2, ....;  transmits data from the FIFO
    MFRC630_CMD_WRITEE2 = const(0x08)  # addressH, addressL, data; gets one byte from FIFO buffer and
    MFRC630_CMD_WRITEE2PAGE = const(0x09)  # (page Address), data0, [data1..data63]; gets up to 64 bytes (one
    MFRC630_CMD_READE2 = const(0x0A)  # addressH, address L, length; reads data from the EEPROM and copies
    MFRC630_CMD_LOADREG = const(0x0C)  # (EEPROM addressH), (EEPROM addressL), RegAdr, (number of Register
    MFRC630_CMD_LOADPROTOCOL = const(0x0D)  # (Protocol number RX), (Protocol number TX) reads data from the
    MFRC630_CMD_LOADKEYE2 = const(0x0E)  # KeyNr; copies a key from the EEPROM into the key buffer. */
    MFRC630_CMD_STOREKEYE2 = const(0x0F)  # KeyNr, byte1, byte2, byte3, byte4, byte5, byte6; stores a MIFARE
    MFRC630_CMD_READRNR = const(0x1C)  # (no arguments) ; Copies bytes from the Random Number generator
    MFRC630_CMD_SOFTRESET = const(0x1F)  # (no arguments) ; resets the MFRC630. */

    MFRC630_STATUS_STATE_IDLE = const(0b000)  # Status register; Idle
    MFRC630_STATUS_STATE_TXWAIT = const(0b001)  # Status register; Tx wait
    MFRC630_STATUS_STATE_TRANSMITTING = const(0b011)  # Status register; Transmitting.
    MFRC630_STATUS_STATE_RXWAIT = const(0b101)  # Status register; Rx wait.
    MFRC630_STATU