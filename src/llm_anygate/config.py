"""Configuration management for LLM AnyGate."""

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


class ProviderConfig(BaseModel):
    """Configuration for a single provider."""
    
    provider_type: str = Field(description="Type of provider (openai, anthropic, etc.)")
    api_key: Optional[str] = Field(default=None, description="API key for authentication")
    model: Optional[str] = Field(default=None, description="Model to use")
    base_url: Optional[str] = Field(default=None, description="Base URL for API")
    extra_params: Dict[str, Any] = Field(default_factory=dict, description="Additional parameters")


class Config(BaseModel):
    """Main configuration for LLM AnyGate."""
    
    providers: Dict[str, ProviderConfig] = Field(
        default_factory=dict,
        description="Provider configurations keyed by name"
    )
    default_provider: Optional[str] = Field(
        default=None,
        description="Default provider to use"
    )
    timeout: float = Field(
        default=30.0,
        description="Request timeout in seconds"
    )
    retry_attempts: int = Field(
        default=3,
        description="Number of retry attempts on failure"
    )
    
    @classmethod
    def from_file(cls, path: str) -> "Config":
        """Load configuration from a file.
        
        Args:
            path: Path to configuration file (JSON or YAML)
            
        Returns:
            Config instance
        """
        import json
        from pathlib import Path
        
        file_path = Path(path)
        if file_path.suffix == ".json":
            with open(file_path) as f:
                data = json.load(f)
            return cls(**data)
        else:
            raise ValueError(f"Unsupported configuration file format: {file_path.suffix}")