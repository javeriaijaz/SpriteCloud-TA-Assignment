from jsonschema import validate

USER_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {"type": "array"},
    },
    "required": ["page", "per_page", "total", "total_pages", "data"],
}

def validate_json(response_json, schema):
    """Validates API response against a JSON schema."""
    validate(instance=response_json, schema=schema)
