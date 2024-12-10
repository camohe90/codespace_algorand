from algokit_utils.beta.algorand_client import (AlgorandClient, ) # Import what you need here

# Client to connect to localnet
algorand = AlgorandClient.default_local_net()

# Import dispenser from KMD 
dispenser = algorand.account.dispenser()
print("Dispenser Address: ", dispenser.address)
