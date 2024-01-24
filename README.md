# odos-python-sdk
A client library for accessing Odos API

## Usage
First, create a client:

```python
from odos_python_sdk import Client

client = Client(base_url="https://api.odos.xyz")
```

Then you can call your endpoint and use your models:

```python
from odos_python_sdk.models import SupportedChains
from odos_python_sdk.api.information import get_chain_ids_info_chains_get
from odos_python_sdk.types import Response

with client as client:
    supported_chains: SupportedChains = get_chain_ids_info_chains_get.sync(client=client)
    # or if you need more info (e.g. status_code)
    response: Response[SupportedChains] = get_chain_ids_info_chains_get.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from odos_python_sdk.models import SupportedChains
from odos_python_sdk.api.information import get_chain_ids_info_chains_get
from odos_python_sdk.types import Response

async with client as client:
    supported_chains: SupportedChains = await get_chain_ids_info_chains_get.asyncio(client=client)
    # or if you need more info (e.g. status_code)
    response: Response[SupportedChains] = await get_chain_ids_info_chains_get.asyncio_detailed(client=client)
```

### All possible endpoints

```shell
├── information
│   ├── get_chain_ids_info_chains_get
│   ├── get_contract_info_info_contract_info_version_chain_id_get
│   ├── get_current_block_info_current_block_chain_id_get
│   ├── get_executor_info_executor_version_chain_id_get
│   ├── get_liquidity_sources_info_liquidity_sources_chain_id_get
│   ├── get_router_info_router_version_chain_id_get
│   └── get_token_map_info_tokens_chain_id_get
├── pricing
│   ├── get_chain_token_prices_pricing_token_chain_id_get
│   ├── get_currencies_pricing_currencies_get
│   └── get_token_price_pricing_token_chain_id_token_addr_get
└── smart_order_routing
    ├── assemble_sor_assemble_post
    ├── quote_sor_quote_v2_post
    └── quote_zap_sor_quote_v2_zap_post
```

### Models

- AssemblePathRequest
- ChainTokenPriceMap
- ChainTokenPriceMapTokenprices
- ContractInfo
- ContractInfoErc20AbiType0
- ContractInfoRouterAbiType0
- CurrencyInfo
- CurrencyInfoList
- CurrentBlockNumber
- ExecutorAddress
- HTTPValidationError
- LiquiditySources
- PathRequestV2
- PathResponse
- PathVizImageConfig
- QuoteResponse
- QuoteResponsePathVizType0
- RouterAddress
- Simulation
- SimulationError
- SupportedChains
- Toke
- TokenAmount
- TokenMap
- TokenMapTokenmap
- TokenPrice
- TokenProportion
- Transaction
- ValidationError