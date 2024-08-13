from fasthtml.fastapp import *
from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    AssetTransferParams,
    PayParams,
    AssetOptInParams,
)
import uvicorn
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO)

def render(creator_address, receiver_address, asset_id):
    result = f"""
    \nCreator Address: {creator_address}
    \nReceiver Address: {receiver_address}
    \nAsset ID: {asset_id}
    """
    return Div(result, id='result')

# Unpack only the necessary values from fast_app
app, rt = fast_app('data/algorand.db')

@rt("/")
async def get(request):
    new_frm = Form(Group(Button("Run Script", hx_post="/run-script", target_id="result", hx_swap="innerHTML")),
                   id='form')
    # Add a result div here
    result_placeholder = Div(id='result')
    return Titled('Algorand Token Creation and Transfer', new_frm, result_placeholder)


@rt("/run-script")
async def post(request):
    logging.info("Form submitted! Running Algorand setup...")
    result = setup_algorand()
    return render(result['creator_address'], result['receiver_address'], result['asset_id'])

def setup_algorand():
    algorand = AlgorandClient.default_local_net()
    dispenser = algorand.account.dispenser()

    # Create and fund a new account (creator)
    creator = algorand.account.random()
    algorand.send.payment(
        PayParams(
            sender=dispenser.address,
            receiver=creator.address,
            amount=10_000_000  # Fund with 10 Algos
        )
    )

    # Create a new Algorand Standard Asset (ASA)
    sent_txn = algorand.send.asset_create(
        AssetCreateParams(
            sender=creator.address,
            total=1000,
            asset_name="algofam",
            unit_name="FAM",
            manager=creator.address,
            clawback=creator.address,
            freeze=creator.address
        )
    )

    asset_id = sent_txn["confirmation"]["asset-index"]

    # Create and fund another new account (receiver)
    receiver = algorand.account.random()
    algorand.send.payment(
        PayParams(
            sender=dispenser.address,
            receiver=receiver.address,
            amount=10_000_000  # Fund with 10 Algos
        )
    )

    # Opt-in the receiver account to the newly created ASA
    algorand.send.asset_opt_in(
        AssetOptInParams(
            sender=receiver.address,
            asset_id=asset_id
        )
    )

    # Transfer 10 units of the ASA from creator to receiver
    algorand.send.asset_transfer(
        AssetTransferParams(
            sender=creator.address,
            receiver=receiver.address,
            asset_id=asset_id,
            amount=10  # Transfer amount
        )
    )

    return {
        "creator_address": creator.address,
        "receiver_address": receiver.address,
        "asset_id": asset_id
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
