# SiriCoin-py
Siricoin-py is a rpc and api wrapper.

First, install it via pip:
```
pip install siricoin
```

All commands interfacing with the node need to use an Instance of `siriCoin()`

To create a new instance, run:
```
import siricoin

siri = siricoin.siriCoin()
```
Here are some commands you can use:
```
#                      Private key               From            To            Amount
print(siri.transaction("XXXXXXXXXXXXXXXXXXXXXX", "0x4ba...b313", "0xbd...164", 1))
# returns False 

#                  Address
print(siri.balance("0x4ba...b313"))

#                     Address
print(siri.is_address("0x4ba...b313"))

```

Better docs soon™

If you face any issues, file a issue on Github.

If you want to support the developer, send SiriCoin, BNB, MATIC or ETH to the following address:
```0x4baE9F81a30b148Eb40044F6268B5496861Cb313```

This code is released under MIT License.
