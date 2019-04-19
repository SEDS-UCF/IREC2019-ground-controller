import tetherCom as yamville
import yamDecoder

yamville.sendYam([1, 7, [1, 2, 3, 4, 57, 18, 19, 20]])

while True:
    yamville.harvestYams()

    yam = yamville.grabNextYam()

    if yam is not None:
        yamDecoder.decodeYam(yam)
