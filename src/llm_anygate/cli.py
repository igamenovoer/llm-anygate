"""Command-line interface for LLM AnyGate."""

import asyncio
import sys
from typing import Optional

from .core import Gateway
from .providers import OpenAIProvider, AnthropicProvider


def main() -> int:
    """Main entry point for the CLI.
    
    Returns:
        Exit code
    """
    print("LLM AnyGate CLI")
    print("=" * 40)
    
    # Example usage
    gateway = Gateway()
    
    # Register providers
    gateway.register_provider("openai", OpenAIProvider())
    gateway.register_provider("anthropic", AnthropicProvider())
    
    # List available providers
    print("\nAvailable providers:")
    for provider_name in gateway.list_providers():
        provider = gateway.get_provider(provider_name)
        if provider:
            info = provider.get_info()
            print(f"  - {provider_name}: {info['provider']}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())