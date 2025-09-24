import os
from algokit_utils import(
    AlgoAmount,
    AlgorandClient,
    PaymentParams,
    AssetCreateParams,
    AssetOptInParams,
    AssetTransferParams

)

from dotenv import load_dotenv

load_dotenv()
PASSPHRASE = os.environ.get("PASSPHRASE")

print("--------------------------------------------")
print("Processing account...")

algorand = AlgorandClient.testnet()

cuenta_1 = algorand.account.from_mnemonic(mnemonic=PASSPHRASE)
print(f"Esta es la cuenta con la que vamos a trabajar {cuenta_1.address}")

cuenta_1_info = algorand.account.get_information(cuenta_1)
print(f"El saldo de la cuenta es: {cuenta_1_info.amount.algo}")

cuenta_2= algorand.account.random()
print(f"Esta es la cuenta 2 {cuenta_2.address}")

#vamos a enviar ALGOS a la cuenta 2
pay_result = algorand.send.payment(
    PaymentParams(
        sender = cuenta_1.address,
        receiver = cuenta_2.address,
        amount = AlgoAmount(algo=0.5),
        static_fee = AlgoAmount(algo=0.001)
    )
)

print(
    f"\nTransacción de pago confirmada con el TxnID: {pay_result.tx_id}. \n Puedes ver la transacción acá https://lora.algokit.io/testnet/transaction/{pay_result.tx_id}."
)

cuenta_2_info = algorand.account.get_information(cuenta_2)
print(f"El saldo de la cuenta es: {cuenta_2_info.amount.algo}")

create_asset_result = algorand.send.asset_create(
    AssetCreateParams(
        sender = cuenta_1.address,
        asset_name = "Demo ACM",
        unit_name = "DACM",
        total = 10000000,
        decimals = 1,
        note = b'Demo ACM creacion de tokens',
        static_fee = AlgoAmount(algo=0.001)
    )
)

created_asset = create_asset_result.asset_id
print(
    f"\nAsset ID {created_asset} create transaction confirmed with TxnID: {create_asset_result.tx_id}."
)
print(
    f"\nView it on Lora at https://lora.algokit.io/testnet/asset/{created_asset}."
)

cuenta_2_opt_in_result = algorand.send.asset_opt_in(
    AssetOptInParams(
        sender = cuenta_2.address,
        asset_id = created_asset,
        static_fee = AlgoAmount(algo=0.001)
    )
)

print(f"\nAsset opt-in transaction confirmed with TxnID: {cuenta_2_opt_in_result.tx_id}. \nView it on Lora at https://lora.algokit.io/testnet/transaction/{cuenta_2_opt_in_result.tx_id}."
)


send_asset_result = algorand.send.asset_transfer(
    AssetTransferParams(
        sender = cuenta_1.address,
        receiver = cuenta_2.address,
        asset_id = created_asset,
        amount = 3_000,
        note = b'pago por participar en el workshop',
        static_fee = AlgoAmount(algo=0.001)
    )
        
)

cuenta_2_info = algorand.account.get_information(cuenta_2.address)
print(
    f"\nCuenta 2 's account information from algod's /v2/accounts/{{address}} REST API endpoint: \n{cuenta_2_info}."
    )
print(
    f"\nLearn about and explore the algod REST API at https://dev.algorand.io/reference/rest-api/overview/#algod-rest-endpoints."
    )