from hydra.core.global_hydra import GlobalHydra
from hydra.core.hydra_config import HydraConfig

# Initialize Hydra
GlobalHydra.instance().clear()
HydraConfig.instance().get("job", "list_configs")

# Print configuration search paths
print("Config search path:")
for path in HydraConfig.get().config_search_path:
    print(f"\t{path}")
