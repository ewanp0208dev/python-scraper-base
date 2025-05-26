import os
import hashlib

CACHE_DIR = ".cache"
os.makedirs(CACHE_DIR, exist_ok=True)


def _url_to_cache_path(url: str) -> str:
    hash_name = hashlib.md5(url.encode("utf-8")).hexdigest()
    return os.path.join(CACHE_DIR, f"{hash_name}.html")


def load_from_cache(url: str) -> str | None:
    path = _url_to_cache_path(url)
    if not os.path.exists(path):
        return None
    
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
    
def save_to_cache(url: str, html: str):
    path = _url_to_cache_path(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)