# Elrond Playground
The purpose of this project is to play around with interacting with the [elrond](https://elrond.com/) blockchain network. There is an [elrond-sdk](https://github.com/ElrondNetwork/elrond-sdk) for facilitating this functionality.


## Useful Dev Tips and Tricks
### Internal Representations
Internally everything in EGLD is represented as 10^18 and a uint. Elrond works with 18 decimals, so in order to get a human readable number diving by 10^18. Programmatically this is represented as:

```python
import math

balance = int(egld_response.('key')) / int(math.pow(10, 18))
```

Learnt this the hard way but I found a comment [here](https://coinmarketbag.com/learn-to-code-for-elrond-part-1/) from one of the core devs mentioning it.

## Setup
Follow the instructions to setup erdpy [here](https://docs.elrond.com/sdk-and-tools/erdpy/erdpy/). If you're using the mainnet make sure the proxy appropriately:

```
erdpy config set proxy https://api.elrond.com
```

## Dependencies
Instructions on how to install erdpy can be found here:

1. [Installation instructions](https://docs.elrond.com/sdk-and-tools/https://docs.elrond.com/sdk-and-tools/erdpy/installing-erdpy/erdpy/installing-erdpy/)
2. [elrond-sdk](https://github.com/ElrondNetwork/elrond-sdk)