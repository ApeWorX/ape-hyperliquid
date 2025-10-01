from ape import plugins


@plugins.register(plugins.Config)
def config_class():
    from .config import HyperliquidConfig

    return HyperliquidConfig


@plugins.register(plugins.EcosystemPlugin)
def ecosystems():
    from .ecosystems import HyperEVM

    yield HyperEVM


@plugins.register(plugins.NetworkPlugin)
def networks():
    from ape.api.networks import (
        LOCAL_NETWORK_NAME,
        ForkedNetworkAPI,
        NetworkAPI,
        create_network_type,
    )

    from .ecosystems import NETWORKS

    for network_name, network_params in NETWORKS.items():
        yield "hyperliquid", network_name, create_network_type(*network_params)
        yield "hyperliquid", f"{network_name}-fork", ForkedNetworkAPI

    # NOTE: This works for development providers, as they get chain_id from themselves
    yield "hyperliquid", LOCAL_NETWORK_NAME, NetworkAPI


@plugins.register(plugins.ProviderPlugin)
def providers():
    from ape.api.networks import LOCAL_NETWORK_NAME
    from ape_node import Node
    from ape_test import LocalProvider

    from .ecosystems import NETWORKS

    for network_name in NETWORKS:
        yield "hyperliquid", network_name, Node

    yield "hyperliquid", LOCAL_NETWORK_NAME, LocalProvider


def __getattr__(name: str):
    if name == "HyperEVM":
        from .ecosystems import HyperEVM

        return HyperEVM

    elif name == "HyperliquidConfig":
        from .config import HyperliquidConfig

        return HyperliquidConfig

    elif name == "NETWORKS":
        from .ecosystems import NETWORKS

        return NETWORKS

    else:
        raise AttributeError(name)


__all__ = [
    "Hyperliquid",
    "HyperEVM",
    "HyperliquidConfig",
    "NETWORKS",
]
