"""Core gateway functionality for LLM AnyGate."""

from typing import Any, Dict, List, Optional
from .providers import Provider


class Gateway:
    """Main gateway class for managing multiple LLM providers."""
    
    def __init__(self) -> None:
        """Initialize the Gateway."""
        self.providers: Dict[str, Provider] = {}
    
    def register_provider(self, name: str, provider: Provider) -> None:
        """Register a new LLM provider.
        
        Args:
            name: Unique name for the provider
            provider: Provider instance to register
        """
        self.providers[name] = provider
    
    def get_provider(self, name: str) -> Optional[Provider]:
        """Get a registered provider by name.
        
        Args:
            name: Name of the provider
            
        Returns:
            Provider instance or None if not found
        """
        return self.providers.get(name)
    
    def list_providers(self) -> List[str]:
        """List all registered provider names.
        
        Returns:
            List of provider names
        """
        return list(self.providers.keys())