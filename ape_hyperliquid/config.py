from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from ape.types import GasLimit

from ape_ethereum.ecosystem import BaseEthereumConfig, NetworkConfig
from ape_ethereum.transactions import TransactionType as EthTransactionType

# NOTE: Use a hard-coded gas limit for testing
#   because the block gasLimit is extremely high in Arbitrum networks.
LOCAL_GAS_LIMIT = 30_000_000


def _create_config(
    required_confirmations: int = 1,
    block_time: int = 1,
    cls: type = NetworkConfig,
    **kwargs,
) -> NetworkConfig:
    return cls(
        required_confirmations=required_confirmations,
        block_time=block_time,
        default_transaction_type=EthTransactionType.DYNAMIC,
        **kwargs,
    )


class HyperliquidConfig(BaseEthereumConfig):
    DEFAULT_TRANSACTION_TYPE: ClassVar[int] = EthTransactionType.STATIC.value
    DEFAULT_LOCAL_GAS_LIMIT: ClassVar["GasLimit"] = LOCAL_GAS_LIMIT
    mainnet: NetworkConfig = _create_config()
    testnet: NetworkConfig = _create_config()
    builder_code: str = "ApeWorX Builder Code"
