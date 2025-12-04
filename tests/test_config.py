from ape_ethereum.transactions import TransactionType

from ape_hyperliquid.config import LOCAL_GAS_LIMIT, HyperliquidConfig


def test_gas_limit(hyperliquid):
    assert hyperliquid.config.local.gas_limit == LOCAL_GAS_LIMIT


def test_default_transaction_type(hyperliquid):
    assert hyperliquid.config.mainnet.default_transaction_type == TransactionType.DYNAMIC


def test_mainnet_fork_not_configured():
    obj = HyperliquidConfig.model_validate({})
    assert obj.mainnet_fork.required_confirmations == 0


def test_custom_network():
    data = {"apenet": {"required_confirmations": 333}}
    obj = HyperliquidConfig.model_validate(data)
    assert obj.apenet.required_confirmations == 333
