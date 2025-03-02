from typing import Any

import replicate
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

class ReplicateProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        """Validate the Replicate API token."""
        try:
            # Set the API token
            client = replicate.Client(api_token=credentials["replicate_api_token"])
            
            # Try to list models to verify the token
            # This will raise an error if the token is invalid
            client.models.get("black-forest-labs/flux-schnell")
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e)) 