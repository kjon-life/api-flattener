from pathlib import Path
from typing import Dict, Union, Any
import yaml

class SpecificationIO:
    """Handles reading and writing OpenAPI specifications."""
    
    @staticmethod
    def read_spec(spec_path: Union[str, Path]) -> Dict[str, Any]:
        """Read an OpenAPI specification from a file.
        
        Args:
            spec_path: Path to the specification file
            
        Returns:
            Dict containing the loaded specification
            
        Raises:
            FileNotFoundError: If the specification file doesn't exist
            yaml.YAMLError: If the specification is invalid YAML
        """
        spec_path = Path(spec_path)
        if not spec_path.exists():
            raise FileNotFoundError(f"Specification file not found: {spec_path}")
            
        with open(spec_path) as f:
            return yaml.safe_load(f)
    
    @staticmethod
    def write_spec(spec: Dict[str, Any], output_path: Union[str, Path]) -> None:
        """Write an OpenAPI specification to a file.
        
        Args:
            spec: The specification to write
            output_path: Path where the specification should be written
            
        Raises:
            OSError: If the file cannot be written
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            yaml.dump(spec, f, sort_keys=False, allow_unicode=True)