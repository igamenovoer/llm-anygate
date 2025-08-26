"""CLI tool for setting up LiteLLM proxy projects."""

import argparse
import sys
from pathlib import Path

from llm_anygate.litellm_checker import check_litellm_installed
from llm_anygate.proxy_generator import ProxyGenerator


def create_command(
    project_dir: str, model_config: str, port: int = 4567, master_key: str = "sk-dummy"
) -> int:
    """Create a new LiteLLM proxy project.

    Args:
        project_dir: Path to the project directory to create
        model_config: Path to the model configuration YAML file
        port: Port number for the proxy server
        master_key: Master key for the proxy

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    try:
        # Check if litellm is installed
        is_installed, install_msg = check_litellm_installed()
        if not is_installed:
            print(f"Warning: {install_msg}")
            print("Continuing with project generation...")
            print()

        # Create the generator
        generator = ProxyGenerator()

        # Generate the project
        success = generator.create_project(
            project_dir=Path(project_dir),
            model_config_path=Path(model_config),
            port=port,
            master_key=master_key,
        )

        if success:
            print(f"Successfully created LiteLLM proxy project at: {project_dir}")
            print()
            print("To start the proxy server:")
            print(f"  cd {project_dir}")
            print("  ./start-proxy.sh  # On Unix/macOS")
            print("  .\\start-proxy.ps1  # On Windows")
            return 0
        else:
            print("Failed to create project")
            return 1

    except Exception as e:
        print(f"Error: {e}")
        return 1


def main(args: list[str] | None = None) -> int:
    """Main entry point for the CLI tool.

    Args:
        args: Command line arguments (for testing)

    Returns:
        Exit code
    """
    parser = argparse.ArgumentParser(
        prog="llm-anygate-cli", description="CLI tool for setting up LiteLLM proxy projects"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new proxy project")
    create_parser.add_argument("--project", required=True, help="Project directory to create")
    create_parser.add_argument(
        "--model-config", required=True, help="Path to the model configuration YAML file"
    )
    create_parser.add_argument(
        "--port", type=int, default=4567, help="Port number for the proxy server (default: 4567)"
    )
    create_parser.add_argument(
        "--master-key", default="sk-dummy", help="Master key for the proxy (default: sk-dummy)"
    )

    parsed_args = parser.parse_args(args)

    if not parsed_args.command:
        parser.print_help()
        return 1

    if parsed_args.command == "create":
        return create_command(
            project_dir=parsed_args.project,
            model_config=parsed_args.model_config,
            port=parsed_args.port,
            master_key=parsed_args.master_key,
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
