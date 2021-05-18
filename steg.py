# Run with Python 2
# Steg Program
# Group: The Star
# Members: Andrew Leblanc, Brian Mulhair, Troy Chiasson, Jordan Lewis, Bryce Ditto, Brendan Buck, Abram Bender, Will Coker

import argparse
import sys
from binascii import hexlify

sentinel = '00ff0000ff00'
sentinelHex = hexlify(sentinel)
sentinelHex = map(''.join, zip(sentinelHex[::2], sentinelHex[1::2]))


# main function
def main():
    # if neither -s or -r are present OR both are present
    if (not args.store and not args.retrieve) | (args.store and
                                                 args.retrieve):
        print("Select either to store or retrieve hidden file")
        sys.exit()
    # if neither -b or -B are present OR both are present
    elif (not args.bit and not args.byte) | (args.bit and args.byte):
        print("Select either byte or bit method")
        sys.exit()
    # if no offset is specified
    elif (args.offset is None):
        print("Offset required")
        sys.exit()
    # if no wrapper file is specified
    elif (args.wrapperFile is None):
        print("Wrapper file required")
        sys.exit()
    # if trying to store a file and no file to store is provided
    elif (args.store and args.hiddenFile is None):
        print("File required to hide")
        sys.exit()

    # wrapper file as hex
    wrapperFileHex = bytearray(open(args.wrapperFile, 'rb').read())

    # if trying to store with bit method
    if (args.bit and args.store):
        hiddenFileHex = hexlify(open(args.hiddenFile, 'rb').read())
        hiddenFileHex = map(''.join, zip(
            hiddenFileHex[::2], hiddenFileHex[1::2]))
        if (args.interval is None):
            interval = 1
        else:
            interval = args.interval
        return bitStore(args.offset, interval, wrapperFileHex, hiddenFileHex)

    # if trying to retrieve with bit method
    if (args.bit and args.retrieve):
        if (args.interval is None):
            interval = 1
        else:
            interval = args.interval

        string = bitRetrieve(args.offset, interval, wrapperFileHex)
        sentinelIndex = string.find(sentinel.decode("hex"))
        if (sentinelIndex != -1):
            return string[:sentinelIndex]
        return "Nothing was found"

    # if trying to store with byte method
    if (args.byte and args.store):
        hiddenFileHex = hexlify(open(args.hiddenFile, 'rb').read())
        hiddenFileHex = map(''.join, zip(
            hiddenFileHex[::2], hiddenFileHex[1::2]))
        if (args.interval is None):
            interval = 1
        else:
            interval = args.interval
        return byteStore(args.offset, interval, wrapperFileHex, hiddenFileHex)

    # if trying to recieve with byte method
    if (args.byte and args.retrieve):
        string = byteRetrieve(args.offset, args.interval, wrapperFileHex)
        sentinelIndex = string.find(sentinel.decode("hex"))
        if (sentinelIndex != -1):
            return string[:sentinelIndex]
        return "Nothing was found"

# store method using bytes


def byteStore(offset, interval, wrapperFileHex, hiddenFileHex):
    o = offset
    i = 0
    while (i < len(hiddenFileHex)):
        wrapperFileHex[o] = hiddenFileHex[i]
        o += interval
        i += 1

    i = 0
    while (i < len(sentinelHex)):
        wrapperFileHex[o] = sentinelHex[i]
        o += interval
        i += 1

    return "".join(wrapperFileHex).decode("hex")


# retrieve method using bytes
def byteRetrieve(offset, interval, wrapperFileHex):
    string = ""
    o = offset
    while (o < len(wrapperFileHex)):
        b = wrapperFileHex[o]
        string += chr(b)
        o += interval
    return string


# store method using bits
def bitStore(offset, interval, wrapperFileHex, hiddenFileHex):
    o = offset
    i = 0
    string = ""
    while (i < len(hiddenFileHex)):
        hiddenByte = int(hiddenFileHex[i], 16)
        for j in range(8):
            wrapperByte = int(wrapperFileHex[o], 16)
            wrapperByte &= 11111110
            wrapperByte |= ((hiddenByte & 10000000) >> 7)
            wrapperFileHex[o] = hexlify('%x' % wrapperByte)
            if (j != 7):
                hiddenByte = hiddenByte << 1
            o += interval
        i += 1

    u = 0
    while (u < len(sentinelHex)):
        sentinelByte = int(sentinelHex[u], 16)
        for k in range(8):
            wrapperByte = int(wrapperFileHex[o], 16)
            wrapperByte &= 11111110
            wrapperByte |= ((sentinelByte & 10000000) >> 7)
            wrapperFileHex[o] = hexlify('%x' % wrapperByte)
            if (k != 7):
                sentinelByte = sentinelByte << 1
            o += interval
        u += 1

    string += "".join(wrapperFileHex)
    return string.decode("hex")


# retrieve method using bits
def bitRetrieve(offset, interval, wrapperFileHex):
    o = offset
    string = ""

    try:
        while (o < len(wrapperFileHex)):
            byte = 00000000
            for k in range(8):
                wrapperByte = wrapperFileHex[o]
                bit = wrapperByte & 0o1
                byte |= bit
                if (k != 7):
                    byte = byte << 1
                o += interval

            string += chr(byte)

    except:
        return string

    return string


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-s', '--store', default=False, action='store_true')
parser.add_argument('-r', '--retrieve', default=False, action='store_true')
parser.add_argument('-b', '--bit', default=False, action='store_true')
parser.add_argument('-B', '--byte', default=False, action='store_true')
parser.add_argument('-o', '--offset', type=int)
parser.add_argument('-i', '--interval', type=int)
parser.add_argument('-w', '--wrapperFile', type=str)
parser.add_argument('-h', '--hiddenFile', type=str)
args = parser.parse_args()

if __name__ == '__main__':
    print main()
