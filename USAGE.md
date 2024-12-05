# api_flattener usage
# execute following in shell
# tested w zsh and python = "^3.11"

from api_flattener.core.flattener import APIFlattener
from api_flattener.utils.io import SpecificationIO

flattener = APIFlattener()
spec = flattener.flatten_spec("https://aimod.dev.musubilabs.ai/openapi.json")

# Let's examine the structure
print(type(spec))
# Look at the top-level keys
print(spec.keys())
# Look at a sample of the content
print(list(spec.items())[:2])
# Save the flattened spec to a file
import json
with open('api_spec.json', 'w', encoding='utf-8') as f:
    json.dump(spec, f, indent=2, default=str)



# Inspect in the shell
!cat api_spec.json

