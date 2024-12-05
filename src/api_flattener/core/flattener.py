from pathlib import Path
from typing import Dict, Union, Any
import requests
import yaml
import json
import jsonref

class APIFlattener:
    def __init__(self, base_path: Union[str, Path] = None):
        self.base_path = Path(base_path) if base_path else Path.cwd()
    
    def flatten_spec(self, spec_path: Union[str, Path]) -> Dict[str, Any]:
        # Handle URL-based specs
        if str(spec_path).startswith(('http://', 'https://')):
            response = requests.get(spec_path)
            response.raise_for_status()
            spec_data = response.json()
            # Convert to string and back through jsonref
            return jsonref.loads(json.dumps(spec_data))
        
        # Handle file-based specs
        spec_path = Path(spec_path)
        if not spec_path.exists():
            raise FileNotFoundError(f"Specification file not found: {spec_path}")
        
        with open(spec_path) as f:
            spec_data = yaml.safe_load(f)
            return jsonref.loads(json.dumps(spec_data))