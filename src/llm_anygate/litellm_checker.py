"""Check if litellm is installed and provide installation instructions."""

import importlib.util


def check_litellm_installed() -> tuple[bool, str]:
    """Check if litellm[proxy] is installed.

    Returns:
        A tuple of (is_installed, message)
    """
    # First check if litellm module is available
    litellm_spec = importlib.util.find_spec("litellm")

    if litellm_spec is None:
        return (
            False,
            "litellm is not installed.\n"
            "To install, run: pip install 'litellm[proxy]'\n"
            "Or with pixi: pixi add --pypi-dependencies 'litellm[proxy]'",
        )

    # Check if proxy extras are installed by trying to import proxy-specific modules
    try:
        # Try to import proxy server module
        proxy_spec = importlib.util.find_spec("litellm.proxy.proxy_server")
        if proxy_spec is None:
            return (
                False,
                "litellm is installed but proxy extras are missing.\n"
                "To install proxy extras, run: pip install 'litellm[proxy]'\n"
                "Or with pixi: pixi add --pypi-dependencies 'litellm[proxy]'",
            )

        return (True, "litellm[proxy] is installed")

    except Exception:
        # If we can't determine proxy extras status, assume they're missing
        return (
            False,
            "litellm is installed but proxy extras may be missing.\n"
            "To ensure proxy extras are installed, run: pip install 'litellm[proxy]'\n"
            "Or with pixi: pixi add --pypi-dependencies 'litellm[proxy]'",
        )


def get_litellm_version() -> str:
    """Get the installed litellm version.

    Returns:
        Version string or "unknown" if not installed
    """
    try:
        import litellm

        return getattr(litellm, "__version__", "unknown")
    except ImportError:
        return "not installed"
