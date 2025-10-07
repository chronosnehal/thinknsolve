"""
Base configuration and utilities for coding examples.
Self-contained LLM client implementations for OpenAI, Azure OpenAI, and OpenRouter.
"""
import os
from typing import Dict, Any, List, Optional, Iterable, Union

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # If python-dotenv is not installed, try to load manually
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value

# Self-contained LLM client implementations
class OpenAIClient:
    """OpenAI client implementation"""

    def __init__(self, api_key: str, model: str):
        try:
            from openai import OpenAI
            self.client = OpenAI(api_key=api_key)
            self.default_model = model
        except ImportError:
            raise ImportError("openai package is required. Install with: pip install openai")

    def chat(self, messages: List[Dict[str, str]], model: Optional[str] = None) -> str:
        """Send a chat completion request and return the assistant content."""
        mdl = model or self.default_model
        # Type cast to handle the OpenAI API message format
        formatted_messages = [{"role": msg["role"], "content": msg["content"]} for msg in messages]
        resp = self.client.chat.completions.create(model=mdl, messages=formatted_messages)
        return resp.choices[0].message.content or ""

    def stream_chat(self, messages: List[Dict[str, str]], model: Optional[str] = None) -> Iterable[str]:
        """Yield incremental chunks of the assistant response."""
        mdl = model or self.default_model
        try:
            # Type cast to handle the OpenAI API message format
            formatted_messages = [{"role": msg["role"], "content": msg["content"]} for msg in messages]
            stream = self.client.chat.completions.create(model=mdl, messages=formatted_messages, stream=True)
            for chunk in stream:
                delta = getattr(chunk.choices[0], 'delta', None)
                if delta and getattr(delta, 'content', None):
                    yield delta.content
        except Exception:
            yield self.chat(messages, model=model)

class AzureOpenAIClient:
    """Azure OpenAI client implementation"""

    def __init__(self, api_key: str, azure_endpoint: str, model: str, api_version: str = "2024-02-15-preview"):
        try:
            from openai import AzureOpenAI
            self.client = AzureOpenAI(
                api_key=api_key,
                azure_endpoint=azure_endpoint,
                api_version=api_version
            )
            self.default_model = model
        except ImportError:
            raise ImportError("openai package is required. Install with: pip install openai")

    def chat(self, messages: List[Dict[str, str]], model: Optional[str] = None) -> str:
        """Send a chat completion request and return the assistant content."""
        mdl = model or self.default_model
        # Type cast to handle the OpenAI API message format
        formatted_messages = [{"role": msg["role"], "content": msg["content"]} for msg in messages]
        resp = self.client.chat.completions.create(model=mdl, messages=formatted_messages)
        return resp.choices[0].message.content or ""

    def stream_chat(self, messages: List[Dict[str, str]], model: Optional[str] = None) -> Iterable[str]:
        """Yield incremental chunks of the assistant response."""
        mdl = model or self.default_model
        try:
            # Type cast to handle the OpenAI API message format
            formatted_messages = [{"role": msg["role"], "content": msg["content"]} for msg in messages]
            stream = self.client.chat.completions.create(model=mdl, messages=formatted_messages, stream=True)
            for chunk in stream:
                delta = getattr(chunk.choices[0], 'delta', None)
                if delta and getattr(delta, 'content', None):
                    yield delta.content
        except Exception:
            yield self.chat(messages, model=model)

class OpenRouterClient:
    """OpenRouter client implementation"""

    def __init__(self, api_key: str, model: str):
        try:
            from openai import OpenAI
            self.client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=api_key
            )
            self.default_model = model
        except ImportError:
            raise ImportError("openai package is required. Install with: pip install openai")

    def chat(self, messages: List[Dict[str, str]], model: Optional[str] = None) -> str:
        """Send a chat completion request and return the assistant content."""
        mdl = model or self.default_model
        # Type cast to handle the OpenAI API message format
        formatted_messages = [{"role": msg["role"], "content": msg["content"]} for msg in messages]
        resp = self.client.chat.completions.create(model=mdl, messages=formatted_messages)
        return resp.choices[0].message.content or ""

    def stream_chat(self, messages: List[Dict[str, str]], model: Optional[str] = None) -> Iterable[str]:
        """Yield incremental chunks of the assistant response."""
        mdl = model or self.default_model
        try:
            # Type cast to handle the OpenAI API message format
            formatted_messages = [{"role": msg["role"], "content": msg["content"]} for msg in messages]
            stream = self.client.chat.completions.create(model=mdl, messages=formatted_messages, stream=True)
            for chunk in stream:
                delta = getattr(chunk.choices[0], 'delta', None)
                if delta and getattr(delta, 'content', None):
                    yield delta.content
        except Exception:
            yield self.chat(messages, model=model)

class LLMClientManager:
    """Factory and manager for LLM clients across different providers"""

    @staticmethod
    def get_client_config(provider: str) -> Dict[str, Any]:
        """Get configuration for different LLM providers"""
        configs = {
            "openai": {
                "api_key": os.getenv("OPENAI_API_KEY"),
                "model": os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
            },
            "azure": {
                "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
                "azure_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
                "model": os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-35-turbo"),
                "api_version": os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
            },
            "openrouter": {
                "api_key": os.getenv("OPENROUTER_API_KEY"),
                "model": os.getenv("OPENROUTER_MODEL", "google/gemma-2-9b-it:free")
            }
        }
        return configs.get(provider, {})

    @staticmethod
    def create_client(provider: str) -> Union["OpenAIClient", "AzureOpenAIClient", "OpenRouterClient"]:
        """Create an LLM client for the specified provider"""
        config = LLMClientManager.get_client_config(provider)
        if not config:
            raise ValueError(f"Unsupported provider: {provider}")

        if provider == "openai":
            if not config["api_key"]:
                raise ValueError("OPENAI_API_KEY environment variable is required")
            return OpenAIClient(config["api_key"], config["model"])

        elif provider == "azure":
            if not config["api_key"] or not config["azure_endpoint"]:
                raise ValueError("AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT environment variables are required")
            return AzureOpenAIClient(
                config["api_key"],
                config["azure_endpoint"],
                config["model"],
                config["api_version"]
            )

        elif provider == "openrouter":
            if not config["api_key"]:
                raise ValueError("OPENROUTER_API_KEY environment variable is required")
            return OpenRouterClient(config["api_key"], config["model"])

        else:
            raise ValueError(f"Unknown provider: {provider}")

    @staticmethod
    def get_default_provider() -> str:
        """Get the default LLM provider from environment variable"""
        return os.getenv("DEFAULT_LLM_PROVIDER", "openai")

    @staticmethod
    def get_default_client() -> Union["OpenAIClient", "AzureOpenAIClient", "OpenRouterClient"]:
        """Get the default LLM client based on environment configuration"""
        provider = LLMClientManager.get_default_provider()
        return LLMClientManager.create_client(provider)
