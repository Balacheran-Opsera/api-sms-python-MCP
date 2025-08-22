"""
MCP tool for Gestion repertoire (modification)
"""

import json
import requests
from typing import Dict, Any, Optional


def put_repertoire(keyid: str, repertoireEdit: str, repertoireId: str, champ22: str, champ6: str, champ4: str, champ20: str, champ10: str, champ11: str, champ8: str, champ17: str, champ3: str, champ27: str, champ9: str, champ19: str, champ16: str, champ5: str, champ24: str, champ2: str, champ12: str, champ21: str, champ26: str, champ18: str, champ15: str, champ14: str, champ25: str, num: str, champ7: str, champ13: str, champ23: str, champ1: str) -> str:
    """
    Gestion repertoire (modification)
    """
    try:
        # Get configuration
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body
        request_data = {
        "keyid": keyid,
        "repertoireEdit": repertoireEdit,
        "repertoireId": repertoireId,
        "champ22": champ22,
        "champ6": champ6,
        "champ4": champ4,
        "champ20": champ20,
        "champ10": champ10,
        "champ11": champ11,
        "champ8": champ8,
        "champ17": champ17,
        "champ3": champ3,
        "champ27": champ27,
        "champ9": champ9,
        "champ19": champ19,
        "champ16": champ16,
        "champ5": champ5,
        "champ24": champ24,
        "champ2": champ2,
        "champ12": champ12,
        "champ21": champ21,
        "champ26": champ26,
        "champ18": champ18,
        "champ15": champ15,
        "champ14": champ14,
        "champ25": champ25,
        "num": num,
        "champ7": champ7,
        "champ13": champ13,
        "champ23": champ23,
        "champ1": champ1
        }
        
        # Remove None values
        request_data = {k: v for k, v in request_data.items() if v is not None}
        
        # Make API call
        url = f"{config.base_url}/repertoire"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.put(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


def get_config():
    """Get configuration from environment or config file."""
    import os
    from pathlib import Path
    
    class Config:
        def __init__(self):
            self.base_url = os.getenv("API_BASE_URL")
            self.bearer_token = os.getenv("API_BEARER_TOKEN")
            
            # Try to load from config file if env vars not set
            if not self.base_url or not self.bearer_token:
                config_path = Path.home() / ".api" / "config.json"
                if config_path.exists():
                    with open(config_path, 'r') as f:
                        config_data = json.load(f)
                        self.base_url = self.base_url or config_data.get("baseURL")
                        self.bearer_token = self.bearer_token or config_data.get("bearerToken")
    
    return Config()
