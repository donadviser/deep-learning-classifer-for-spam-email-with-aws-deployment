from pathlib import Path
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%Y%m%d_%H%M%S")

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("config/schema.yaml")