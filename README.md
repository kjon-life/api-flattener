

# Hello! 

I've been a builder 🍀 all my life making systems that work for enterprise, production loads. I am an `avocational` product manager, because enterprise "products" _are_ **the systems we build** to solve problems.

It's a subtle, distinct difference: Individuals buy products, enterprise buys solutions. 

Everything we build has far-reaching effects, and embedded everywhere are APIs to interact with them.

This is a tool for rapidly scaling and iterating on API specifications.

<img align="right" width="300" src="https://user-images.githubusercontent.com/76539355/214731371-78cb7bcb-996d-4108-9872-7af758ed5647.png" alt="A Maia">


# 🧰  &middot; API Flattener   
 ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/kjon-life/api-flattener) 
 ![GitHub License](https://img.shields.io/github/license/kjon-life/api-flattener)
 ![GitHub top language](https://img.shields.io/github/languages/top/kjon-life/api-flattener)

A Python package for flattening OpenAPI specifications by resolving and inlining referenced components.

## Known Issues

- [ ] Correct the OpenAPI version. OpenAPI "3.1.0" is generated.
- [ ] Correct workflow. [kjon-life/api-flattener](https://github.com/kjon-life/api-flattener/actions/runs/1011111111111111111) Test workflow run is failing.
- [ ] Correct the license. MIT license is not correct.
- [ ] Implement the CLI.

## Features

- Resolves `$ref` components in OpenAPI/Swagger specifications
- Supports both local and remote references
- Maintains spec validity during flattening
- Command-line interface for easy usage
- Preserves original specification structure

## Installation

```bash
pip install api-flattener
```

Or with Poetry:

```bash
poetry add api-flattener
```

## Usage

- See [USAGE.md](USAGE.md) as this [README](README.md) is for prior release (will be updated soon).

### Command Line Interface

Flatten an OpenAPI specification:

```bash
api-flatten flatten input.yaml output.yaml
```

With a custom base path for resolving references:

```bash
api-flatten flatten input.yaml output.yaml --base-path ./schemas
```

### Python API

```python
from api_flattener.core.flattener import APIFlattener

# Initialize flattener
flattener = APIFlattener()

# Flatten a specification
flattened_spec = flattener.flatten_spec("path/to/spec.yaml")
```

## Development

This project uses Poetry for dependency management. To get started:

1. Clone the repository:
   ```bash
   git clone git@github.com:yourusername/api-flattener.git
   cd api-flattener
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

4. Run tests:
   ```bash
   pytest
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Proposed Architecture:
```bash
src/
├── api_flattener/  # Main package directory (use underscores for Python)
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── flattener.py      # Main flattening logic
│   │   └── validator.py      # Schema validation
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── reference.py      # Reference handling
│   │   └── io.py            # File I/O operations
│   └── cli/
│       ├── __init__.py
│       └── commands.py       # Click CLI implementation
│
tests/
├── __init__.py
├── test_flattener.py
├── test_validator.py
└── fixtures/               # Test API specs
    ├── simple.yaml
    └── nested.yaml
```

### Tech stack:
* Pythone - for rapid development

### History:  

### Roadmap: Effortless login, and the developer experience
[Q4](not available) Candidates:  
* Dynamic - suite for log in, wallet creation, and user management    
* SpruceID - a future where users control their identity & data    
* fission - identity, data, and compute solutions for the future of the Internet  
* Backstage - open source framework for developer experience
   
### Release 0.0.0  
In progress

### Acknowledgements:

[WIP]

## Development Process

### Releases

[WIP]

### Version Schedule

[WIP]

### For Contributors
- [Contribution Guidelines](CONTRIBUTING.md)
- [Development Setup](docs/development/setup.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)


### About Me:  
- I work in the intersections of programming, performance, and revenue.  
- I am deeply curious about MACHINE LEARNING RESEARCH, the way we present and consume information, and natural language processing. 
- I enjoy walking, buskers, cold plunging, '67-'73 Chevy trucks, and Chagaccino!  

To connect:  
- Mention me in an issue or pull request: @kjon-life  
- My friends connect on [Instagram: @kilo.jon](https://www.instagram.com/kilo.jon/)   
- [LinkedIn](https://www.linkedin.com/in/jonhwilliams) for professional connections.


___ 
## Legal & Intellectual Property

Rua Vertex™ ℠ is a registered brand of Rua Vertex, LLC. We're innovators in management consulting and machine learning research. While we love sharing and collaborating, we need to protect our intellectual property:

- Our name and brand marks are protected
- Our methods and technologies are proprietary
- Patents pending on our processes and systems
- All rights reserved on our creative worksgit add .

For detailed information, see:
- [WIP:  LEGAL.md](./LEGAL.md) - Complete IP notice and usage rights
- [WIP:  PATENTS.md](./PATENTS.md) - Patent and innovation protection
- [LICENSE](./LICENSE.md) - Terms of use

Questions? Reach out to legal@ruavertex.com

© 2024 Rua Vertex, LLC