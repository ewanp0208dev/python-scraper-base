import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from .headers import get_realistic_headers


def create_session(
    retries: int = 3,
    backoff_factor: float = 0.5,
    timeout: int = 10
) -> requests.Session:
    """
    Create a configured requests.Session object with retry support.
    
    Args:
        retries (int): Number of retry attempts for failed requests.
        backoff_factor (float): Factor for calculating wait time between retries.
        timout (int): Default timeout in seconds for requests made with the session.
        
    Returns:
        requests.Session: A configured session with headers and retry strategy
    """
    
    session = requests.Session()
    
    retry_strategy = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        status_forcelist=[403,429,500,502,503,504],
        allowed_methods=["GET", "HEAD"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    headers = get_realistic_headers()
    session.headers.update(headers)
    
    session.request_timeout = timeout
    return session