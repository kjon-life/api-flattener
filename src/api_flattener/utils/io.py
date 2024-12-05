# src/api_flattener/utils/io.py
from pathlib import Path
from typing import Dict, Union, Any
import yaml
import requests
from urllib.parse import urlparse

class SpecificationIO:
    """Handles reading and writing OpenAPI specifications."""
    
    @staticmethod
    def read_spec(spec_path: Union[str, Path]) -> Dict[str, Any]:
        """Read an OpenAPI specification from a file or URL.
        
        Args:
            spec_path: Path or URL to the specification
            
        Returns:
            Dict containing the loaded specification
        """
        # Check if it's a URL
        parsed = urlparse(str(spec_path))
        if parsed.scheme in ('http', 'https'):
            response = requests.get(spec_path)
            response.raise_for_status()
            return response.json()
            
        # Handle local file
        spec_path = Path(spec_path)
        if not spec_path.exists():
            raise FileNotFoundError(f"Specification file not found: {spec_path}")
            
        with open(spec_path) as f:
            return yaml.safe_load(f)