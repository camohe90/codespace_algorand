from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    AssetOptInParams,
    AssetTransferParams,
    PayParams
)

# Clietn connect to localnet
algorand = AlgorandClient.default_local_net() # not the main net for developing

# Import dispenser from Key Management Payment Dispenser (KMD)
dispenser = algorand.account.dispenser()

print("Dispenser address", dispenser.address)

creator = algorand.account.random()
print("Creator address:", creator.address)
#algorand.account.get_information(creator.address))

# Fund creator account
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=creator.address,
        amount=10_000_000 # 10 algos
    )
)

print(algorand.account.get_information(creator.address))

# Mint tokens
sent_txn = algorand.send.asset_create(
    AssetCreateParams(
        sender=creator.address,
        total=100,
        asset_name="Edu4Teen",
        unit_name="E4T"
    )
)

asset_id = sent_txn["confirmation"]["asset-index"]
print("Asset ID", asset_id) # Four digit number

# Crete second account
receiver_acct = algorand.account.random()

# Fund creator account
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=receiver_acct.address,
        amount=10_000_000 # 10 algos
    )
)
#algorand.account.get_information(receiver_acct.address))


asset_transfer = algorand.send.asset_transfer(
    AssetTransferParams(
        sender=creator.address, # has the E4T token
        receiver=receiver_acct,
        asset_id=asset_id,
        amount=10
    )
)


# Create group transaction
group_txn = algorand.new_group()
group_txn.add_asset_opt_in(
    AssetOptInParams(
        sender=receiver_acct.address,
        asset_id=asset_id
    )
)

group_txn.add_payment(
    PayParams(
        sender=receiver_acct.address,
        receiver=creator.address,
        amount=1_000_000 # 1 algo is 1 million microalgos
    )
)


group_txn.add_asset_transfer(
    AssetTransferParams(
        sender=creator.address, # has the E4T token
        receiver=receiver_acct.address,
        asset_id=asset_id,
        amount=10
    )
)

group_txn.execute()
print("receiver account asset balance:", algorand.account.get_information(receiver_acct)['assets'][0]['amount'])