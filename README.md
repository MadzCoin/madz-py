# SiriCoin-py
Siricoin-py is a rpc and api wrapper.

First, install it via pip:
```
pip install siricoin
```

To create a new instance, run:
```
from siricoin import siriCoin

siri = siriCoin()
```
Here some commands you may use:
```
#                      Private key               From            To            Amount
print(siri.transaction("XXXXXXXXXXXXXXXXXXXXXX", "0x4ba...b313", "0xbd...164", 1))

#                  Address
print(siri.balance("0x4ba...b313"))

#                     Address
print(siri.is_address("0x4ba...b313"))
```
If you face any issues, file a issue here.

If you want to support the developer, send SiriCoin, BNB, MATIC or ETH to the following address:
```0x4baE9F81a30b148Eb40044F6268B5496861Cb313```

This code is released under MIT License.
