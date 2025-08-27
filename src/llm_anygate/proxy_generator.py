"""Generate LiteLLM proxy project structure."""

import os
import stat
from pathlib import Path

from llm_anygate.config_converter import create_full_config
from llm_anygate.templates import (
    get_env_template,
    get_readme_template,
)


class ProxyGenerator:
    """Generator for LiteLLM proxy projects."""

    def __init__(self) -> None:
        """Initialize the proxy generator."""
        pass

    def create_project(
        self,
        project_dir: Path,
        model_config_path: Path,
        port: int = 4567,
        master_key: str = "sk-dummy",
    ) -> bool:
        """Create a complete LiteLLM proxy project.

        Args:
            project_dir: Directory to create the project in
            model_config_path: Path to the model config YAML
            port: Port for the proxy server
            master_key: Master key for authentication

        Returns:
            True if successful, False otherwise
        """
        try:
            # Check if project directory already exists
            if project_dir.exists():
                print(f"Error: Project directory already exists: {project_dir}")
                return False

            # Check if model config exists
            if not model_config_path.exists():
                print(f"Error: Model config file not found: {model_config_path}")
                return False

            # Create project directory
            project_dir.mkdir(parents=True, exist_ok=True)
            print(f"Creating project at: {project_dir}")

            # Generate LiteLLM config
            config_path = project_dir / "config.yaml"
            print("Generating LiteLLM configuration...")
            create_full_config(
                model_config_path=model_config_path,
                output_path=config_path,
                port=port,
                master_key=master_key,
            )

            # Create .env.template file
            env_template_path = project_dir / ".env.template"
            print("Creating environment template...")
            self._create_file(env_template_path, get_env_template(master_key))

            # Create README.md
            readme_path = project_dir / "README.md"
            print("Creating README...")
            self._create_file(readme_path, get_readme_template(port, master_key))

            # Create anygate configuration
            print("Creating anygate configuration...")
            anygate_config_path = project_dir / "anygate.yaml"
            self._create_anygate_config(
                anygate_config_path, 
                str(model_config_path.resolve()),
                port, 
                master_key
            )

            # Create .gitignore
            gitignore_path = project_dir / ".gitignore"
            self._create_file(gitignore_path, self._get_gitignore_content())

            print(f"\nProject created successfully at: {project_dir}")
            return True

        except Exception as e:
            print(f"Error creating project: {e}")
            return False

    def _create_file(self, path: Path, content: str) -> None:
        """Create a file with the given content.

        Args:
            path: Path to the file
            content: Content to write
        """
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    
    def _create_anygate_config(
        self, 
        config_path: Path, 
        model_config_path: str, 
        port: int, 
        master_key: str
    ) -> None:
        """Create anygate.yaml configuration file.

        Args:
            config_path: Path to the anygate.yaml file
            model_config_path: Path to the original model config file  
            port: Port number for the proxy server
            master_key: Master key for authentication
        """
        config_content = f"""# AnyGate Configuration
# This file stores the configuration used when creating this proxy project
# It will be used by 'llm-anygate-cli start' for default values

project:
  model_config: "{model_config_path}"
  port: {port}
  master_key: "{master_key}"
"""
        self._create_file(config_path, config_content)

    def _make_executable(self, path: Path) -> None:
        """Make a file executable (Unix/macOS only).

        Args:
            path: Path to the file
        """
        try:
            # Get current permissions
            current_permissions = os.stat(path).st_mode
            # Add execute permission for owner, group, and others
            os.chmod(path, current_permissions | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        except Exception:
            # Ignore errors on Windows
            pass

    def _get_gitignore_content(self) -> str:
        """Get .gitignore content for the proxy project.

        Returns:
            .gitignore file content
        """
        return """.env
.env.local
*.log
__pycache__/
*.py[cod]
*$py.class
.DS_Store
Thumbs.db
"""
