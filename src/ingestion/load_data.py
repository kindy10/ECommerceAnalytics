from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA_PATH = (
	PROJECT_ROOT/"data/raw/Online Retail.xlsx")


def load_raw_data()->pd.DataFrame:
	"""
	Load the original Online Retail dataset.
	
	Returns:
		pandas.DataFrame:Raw transaction data.
	"""
	if not RAW_DATA_PATH.exists():
		raise FileNoteFoundError(f"Dataset not found:{RAW_DATA_PATH}")
	
	return pd.read_excel(RAW_DATA_PATH)
