#!/bin/sh

# URL of the OpenAPI specification
OPENAPI_SPEC_URL="http://localhost:8000/openapi.json"

# Output directory for the generated SDK
OUTPUT_DIR="."

# Run the OpenAPI Generator CLI
openapi-generator-cli generate -i $OPENAPI_SPEC_URL -g python -o $OUTPUT_DIR