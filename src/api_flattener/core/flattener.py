# src/api_flattener/core/flattener.py
from pathlib import Path
from typing import Dict, Union, Any
import yaml
import jsonref

class APIFlattener:
    """Main class for flattening OpenAPI specifications."""
    
    def __init__(self, base_path: Union[str, Path] = None):
        """Initialize the flattener with an optional base path for resolving references.
        
        Args:
            base_path: Base directory path for resolving local references
        """
        self.base_path = Path(base_path) if base_path else Path.cwd()
    
    def flatten_spec(self, spec_path: Union[str, Path]) -> Dict[str, Any]:
        """Flatten an OpenAPI specification by resolving all references.
        
        Args:
            spec_path: Path to the OpenAPI specification file
            
        Returns:
            Dict containing the flattened specification
            
        Raises:
            FileNotFoundError: If the specification file doesn't exist
            ValueError: If the specification is invalid
        """
        spec_path = Path(spec_path)
        if not spec_path.exists():
            raise FileNotFoundError(f"Specification file not found: {spec_path}")
            
        with open(spec_path) as f:
            spec = yaml.safe_load(f)
            
        return self._resolve_references(spec, spec_path)
    
    def _resolve_references(self, spec: Dict[str, Any], spec_path: Path) -> Dict[str, Any]:
        """Resolve all references in the specification.
        
        Args:
            spec: The loaded specification dictionary
            spec_path: Path to the specification file for relative reference resolution
            
        Returns:
            Dict containing the specification with resolved references
        """
        # Use jsonref to resolve all references
        base_uri = f"file://{spec_path.parent.absolute()}/"
        return jsonref.JsonRef.replace_refs(
            spec,
            base_uri=base_uri,
            loader=jsonref.JsonLoader(
                cache_results=True
            )
        )