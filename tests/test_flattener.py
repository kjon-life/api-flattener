# tests/test_flattener.py
from pathlib import Path
import pytest
import yaml
from api_flattener.core.flattener import APIFlattener

@pytest.fixture
def simple_spec(tmp_path):
    """Create a simple OpenAPI spec with references for testing."""
    components = tmp_path / "components.yaml"
    components.write_text("""
    schemas:
      Error:
        type: object
        properties:
          code:
            type: integer
          message:
            type: string
    """)
    
    main_spec = tmp_path / "openapi.yaml"
    main_spec.write_text("""
    openapi: 3.0.0
    info:
      title: Test API
      version: 1.0.0
    paths:
      /test:
        get:
          responses:
            '400':
              $ref: './components.yaml#/schemas/Error'
    """)
    
    return main_spec

def test_flatten_spec_resolves_references(simple_spec):
    """Test that references are properly resolved during flattening."""
    flattener = APIFlattener()
    flattened = flattener.flatten_spec(simple_spec)
    
    # Verify the reference was resolved
    error_response = flattened['paths']['/test']['get']['responses']['400']
    assert 'type' in error_response
    assert error_response['type'] == 'object'
    assert 'properties' in error_response
    assert set(error_response['properties'].keys()) == {'code', 'message'}

def test_flatten_spec_invalid_path():
    """Test that appropriate error is raised for invalid spec path."""
    flattener = APIFlattener()
    with pytest.raises(FileNotFoundError):
        flattener.flatten_spec('nonexistent.yaml')