from dataclasses import dataclass
from pathlib import Path

# Entity-Return type of a fuction from data_ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path