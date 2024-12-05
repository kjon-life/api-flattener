from typing import Dict, Any, Set
from pathlib import Path
import jsonref
from urllib.parse import urlparse

class ReferenceResolver:
    """Handles resolution of JSON references in OpenAPI specifications."""
    
    def __init__(self, base_path: Path = None):
        """Initialize the resolver.
        
        Args:
            base_path: Base path for resolving relative references
        """
        self.base_path = base_path or Path.cwd()
        self.resolved_refs: Set[str] = set()
        
    def resolve(self, spec: Dict[str, Any], spec_path: Path) -> Dict[str, Any]:
        """Resolve all references in a specification.
        
        Args:
            spec: The specification containing references
            spec_path: Path to the specification file
            
        Returns:
            Dict containing the specification with resolved references
        """
        base_uri = f"file://{spec_path.parent.absolute()}/"
        
        # Create a loader that tracks resolved references
        loader = self._create_loader()
        
        return jsonref.JsonRef.replace_refs(
            spec,
            base_uri=base_uri,
            loader=loader,
            proxies=False  # Disable remote reference resolution if needed
        )
    
    def _create_loader(self) -> jsonref.JsonLoader:
        """Create a JSON loader that tracks resolved references."""
        def load_uri(uri: str, **kwargs):
            self.resolved_refs.add(uri)
            return jsonref.JsonLoader(cache_results=True).load_uri(uri, **kwargs)
            
        return jsonref.JsonLoader(load_uri=load_uri)
    
    def get_resolved_refs(self) -> Set[str]:
        """Get the set of references that have been resolved.
        
        Returns:
            Set of URI strings for resolved references
        """
        return self.resolved_refs