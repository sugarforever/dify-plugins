# Replicate Flux Plugin Development Work Plan

## 1. Configuration Files

### 1.1 Provider Configuration (`/provider/replicate.yaml`)
- Define provider identity (name, author, description)
- Set up credentials configuration for Replicate API Token
- Configure icon path
- Set appropriate tags (image)
- Link to tool configuration and Python source

### 1.2 Tool Configuration (`/tools/flux_schnell.yaml`)
- Define tool identity
- Configure parameters:
  - prompt (string, required) - The image generation prompt
- Set up proper descriptions for both human and LLM
- Link to tool implementation file

## 2. Python Code Implementation

### 2.1 Provider Implementation (`/provider/replicate.py`)
- Implement ReplicateProvider class
- Add credentials validation logic
- Test Replicate API token validation

### 2.2 Tool Implementation (`/tools/flux_schnell.py`)
- Implement FluxSchnellTool class
- Add Replicate API integration
- Implement image generation logic
- Handle response and error cases
- Return appropriate output format

## 3. Dependencies

### 3.1 Required Packages
- replicate (Python client for Replicate API)
- requests (for API calls)
- dify-plugin (Dify plugin SDK)

### 3.2 Requirements File (`requirements.txt`)
```
replicate==0.22.0
requests==2.31.0
dify-plugin==0.3.8
```

## 4. Environment Configuration

### 4.1 Development Environment (`.env`)
```
INSTALL_METHOD=remote
REMOTE_INSTALL_HOST=localhost
REMOTE_INSTALL_PORT=5003
REMOTE_INSTALL_KEY=<your-debug-key>
```

### 4.2 Runtime Environment Variables
- REPLICATE_API_TOKEN (to be provided by end users)

## 5. Assets

### 5.1 Icon
- Create an SVG icon representing image generation
- Place in `_assets` folder
- Suggested name: `icon.svg`

## 6. Testing Plan

### 6.1 Local Testing
- Test credential validation
- Test image generation with sample prompts
- Verify error handling
- Check output format

### 6.2 Integration Testing
- Test plugin installation in Dify
- Verify credential input workflow
- Test image generation in Dify interface

## 7. Documentation

### 7.1 README.md
- Installation instructions
- Usage guide
- API token acquisition steps
- Example prompts

## Implementation Order
1. Set up dependencies
2. Create configuration files
3. Implement provider code
4. Implement tool code
5. Create icon and assets
6. Test locally
7. Test integration
8. Prepare documentation

## Notes
- The plugin will use the black-forest-labs/flux-schnell model from Replicate
- API Token must be handled securely
- Image generation results will be in WebP format
- Error handling should be user-friendly 