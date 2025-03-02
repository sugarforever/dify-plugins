# Replicate Flux Plugin for Dify

A Dify plugin that integrates the Flux Schnell model from Replicate to generate dynamic food photography images.

## Features

- Generate high-quality food photography images
- Simple prompt-based interface
- Secure API token management
- Support for both English and Chinese interfaces

## Prerequisites

- Python 3.11 or higher
- A Replicate account and API token
- Dify platform access

## Installation

1. Clone this repository or download the plugin package
2. Install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Configuration

1. Get your Replicate API token from [https://replicate.com/account](https://replicate.com/account)
2. When installing the plugin in Dify, you'll be prompted to enter your API token

## Usage

### In Dify Platform

1. Install the plugin through Dify's plugin management interface
2. Enter your Replicate API token when prompted
3. The plugin will be available in your workflows and applications

### Example Prompts

- Basic food photo:
  ```
  A delicious chocolate cake with strawberries on top, food photography style
  ```
- Dynamic shot (like the model demo):
  ```
  black forest gateau cake spelling out the words FLUX SCHNELL, tasty, food photography, dynamic shot
  ```

## Development

To run the plugin in development mode:

1. Copy `.env.example` to `.env`
2. Set your Dify debug key and server details in `.env`
3. Run:
   ```bash
   python -m main
   ```

## Author

VerySmallWoods

## License

MIT



