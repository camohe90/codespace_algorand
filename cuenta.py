from algokit_utils import(
    AlgorandClient,
)

from algosdk import mnemonic

algorand = AlgorandClient.testnet()

cuenta_1= algorand.account.random()

print(cuenta_1.address)
print(cuenta_1.private_key)
print(f"frase semilla {mnemonic.from_private_key(cuenta_1.private_key)}")