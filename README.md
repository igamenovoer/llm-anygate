# LLM AnyGate

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Documentation](https://img.shields.io/badge/docs-mkdocs-blue)](https://igamenovoer.github.io/llm-anygate/)

A powerful tool that generates LiteLLM proxy configurations, management scripts, and testing utilities from high-level YAML configurations. Designed to free users from understanding the complexities of the LiteLLM library and quickly create local LLM proxies for use with various AI coding tools.

## Overview

LLM AnyGate simplifies the process of setting up and managing LiteLLM proxies by providing:

- **High-level YAML configuration** - Define your LLM providers and settings in simple YAML
- **Automatic proxy generation** - Generate complete LiteLLM proxy configurations  
- **Management scripts** - Start, stop, and manage your proxy instances
- **Testing utilities** - Validate your configurations and test connectivity
- **Multi-provider support** - Work with various LLM providers seamlessly

## Key Features

### 🎯 **Simplified Configuration**
Configure your LLM providers using intuitive YAML files instead of complex LiteLLM configurations:
- Provider URLs and endpoints
- Supported endpoint formats
- Context limits and model specifications
- Authentication and rate limiting

### 🚀 **Compatible with Popular AI Tools**
Works seamlessly with:
- Claude Code (Anthropic)
- Gemini CLI
- Cline
- Roo Code
- Any tool that supports OpenAI-compatible APIs

### 🔧 **Automated Setup**
- Generate complete LiteLLM proxy configurations
- Create Docker compositions for containerized deployment
- Generate management scripts (start/stop/restart)
- Automatic health checks and monitoring

### 🧪 **Built-in Testing**
- Configuration validation
- Provider connectivity testing
- Load testing utilities
- Performance benchmarking

## Installation

### From PyPI

```bash
pip install llm-anygate
```

### For Development (with Pixi)

```bash
# Clone the repository
git clone https://github.com/igamenovoer/llm-anygate.git
cd llm-anygate

# Initialize submodules
git submodule update --init --recursive

# Install pixi (if not already installed)
# See https://pixi.sh/latest/ for installation instructions

# Setup development environment
pixi install
pixi shell
```

## Quick Start

```python
from llm_anygate import Gateway, OpenAIProvider, AnthropicProvider

# Create gateway
gateway = Gateway()

# Register providers
gateway.register_provider("openai", OpenAIProvider(api_key="your-key"))
gateway.register_provider("anthropic", AnthropicProvider(api_key="your-key"))

# List available providers
print(gateway.list_providers())  # ['openai', 'anthropic']

# Use a provider
provider = gateway.get_provider("openai")
response = await provider.complete("Hello, world!")
print(response)
```

## Configuration Example

```yaml
# config.yaml
providers:
  - name: "anthropic"
    type: "claude"
    base_url: "https://api.anthropic.com"
    endpoint_format: "anthropic"
    context_limit: 200000
    models:
      - "claude-3-5-sonnet-20241022"
      - "claude-3-5-haiku-20241022"
    
  - name: "openai"
    type: "openai"
    base_url: "https://api.openai.com/v1"
    endpoint_format: "openai"
    context_limit: 128000
    models:
      - "gpt-4o"
      - "gpt-4o-mini"

proxy:
  port: 8000
  host: "0.0.0.0"
  cors_enabled: true
  rate_limit: 100
```

## Project Structure

```
llm-anygate/
├── src/llm_anygate/      # Main package source code
├── scripts/               # CLI and utility scripts  
├── tests/                 # Test suite
├── docs/                  # Documentation source
├── context/               # AI collaboration workspace
│   ├── design/           # Technical specifications
│   ├── hints/            # How-to guides
│   ├── logs/             # Development logs
│   ├── plans/            # Implementation plans
│   └── tasks/            # Current work items
├── .magic-context/        # Reusable project templates
└── .github/workflows/     # CI/CD automation
```

## Development

### Running Tests

```bash
pixi run test           # Run tests
pixi run test-cov       # Run tests with coverage
```

### Code Quality

```bash
pixi run lint           # Run linting
pixi run format         # Format code
pixi run typecheck      # Type checking
pixi run quality        # Run all checks
```

### Documentation

```bash
pixi run docs-serve     # Serve docs locally
pixi run docs-build     # Build documentation
pixi run docs-deploy    # Deploy to GitHub Pages
```

## Security

This project uses the following files to store sensitive credential information:
- `.secrets.json` - API keys and tokens
- `.hidden-env.env` - Environment variables with sensitive data

**Important**: These files are automatically excluded from git tracking via `.gitignore`. Never commit sensitive credentials to version control.

## Architecture

- **Config Parser**: Validates and processes YAML configurations
- **Proxy Generator**: Creates LiteLLM-compatible configurations
- **Script Generator**: Produces management and deployment scripts
- **Testing Suite**: Provides validation and testing utilities
- **Documentation Generator**: Creates setup guides and API documentation

## Use Cases

- **AI Development**: Quickly set up local proxies for development with AI coding assistants
- **Multi-provider Setup**: Aggregate multiple LLM providers behind a single endpoint
- **Testing & Development**: Create isolated environments for testing different LLM configurations
- **Cost Management**: Implement rate limiting and usage tracking across providers
- **Fallback Systems**: Configure automatic failover between providers

## Roadmap

- [ ] Core YAML configuration parser
- [ ] LiteLLM proxy configuration generator
- [ ] Docker composition generator
- [ ] Management script templates
- [ ] Provider connectivity testing
- [ ] Configuration validation
- [ ] Web UI for configuration management
- [ ] Metrics and monitoring integration
- [ ] Advanced routing and load balancing

## Contributing

Contributions are welcome! Please see our [Contributing Guide](docs/development/contributing.md) for details.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run quality checks (`pixi run quality`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Documentation

Full documentation is available at [https://igamenovoer.github.io/llm-anygate/](https://igamenovoer.github.io/llm-anygate/)

- [Getting Started Guide](docs/getting-started/installation.md)
- [API Reference](docs/api/gateway.md)
- [Provider Documentation](docs/guide/providers.md)
- [Development Guide](docs/development/contributing.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with modern Python packaging standards
- Uses [Pixi](https://pixi.sh/) for environment management
- Documentation powered by [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- Project structure based on [magic-context](https://github.com/igamenovoer/magic-context) templates

## Contact

- GitHub: [@igamenovoer](https://github.com/igamenovoer)
- Issues: [GitHub Issues](https://github.com/igamenovoer/llm-anygate/issues)

## Support

For questions, issues, or feature requests, please open an issue on GitHub.