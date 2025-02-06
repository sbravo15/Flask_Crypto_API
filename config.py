from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables

CACHE_TYPE = os.getenv("CACHE_TYPE", "simple")
CACHE_DEFAULT_TIMEOUT = int(os.getenv("CACHE_DEFAULT_TIMEOUT", 300))
