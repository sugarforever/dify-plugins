from collections.abc import Generator
from typing import Any

import replicate
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class FluxSchnellTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """Generate an image using the Flux Schnell model."""
        try:
            # Initialize the Replicate client
            client = replicate.Client(api_token=self.runtime.credentials["replicate_api_token"])
            
            # Run the model
            output = client.run(
                "black-forest-labs/flux-schnell",
                input={"prompt": tool_parameters["prompt"]}
            )
            
            # The output is a list with one image URL
            if isinstance(output, list) and len(output) > 0:
                image_url = output[0]
                
                # Return the image URL in a format Dify can handle
                yield self.create_image_message(image_url=image_url)
            else:
                yield self.create_text_message("Failed to generate image: No output received from the model")
                
        except Exception as e:
            yield self.create_text_message(f"Failed to generate image: {str(e)}") 