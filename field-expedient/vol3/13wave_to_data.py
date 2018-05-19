#!/usr/bin/env python

import io
import sys
from struct import *

waveformFileName = 'ook.bin'
payloadLength = 92

# Open the input file in read-only binary mode and read contents into a list
waveformData = None
with io.open(waveformFileName, 'rb') as waveformFile:
    waveformData = list(waveformFile.read())

# The last symbol of the preamble contains a value greater than 1; split the list where the values are greater than 1
segmentList = []
tempSegment = []
for symbolByte in waveformData:
    if ord(symbolByte) > 1:
        segmentList.append(tempSegment)

        # Start new segment with the correct bit (correlator adds 2 so to reverse it just subtract 2)
        tempSegment = [chr(ord(symbolByte) - 2)]

    else:
        tempSegment.append(symbolByte)

# Truncate each segment to the size of the payload
payloadList = []
for segment in segmentList:
    payload = segment[:payloadLength]
    payloadList.append(payload)


for payload in payloadList:
    payloadStr = ''
    for byte in payload:
        payloadStr += chr(ord(byte) + ord('0'))
    print payloadStr
