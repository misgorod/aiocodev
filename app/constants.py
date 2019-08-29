CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "port": {
            "type": "number",
            "minimum": 1025,
            "exclusiveMaximum": 65536
        },
        "db_host": {"type": "string"},
        "db_port": {
            "type": "number",
            "minimum": 1025,
            "exclusiveMaximum": 65536
        },
        "db_database": {"type": "string"},
        "log_level": {
            "type": "string",
            "enum": ["ERROR", "WARNING", "INFO", "DEBUG"]
        }
    },
    "required": [
        "port",
        "db_host",
        "db_port",
        "db_database",
        "log_level"
    ]
}
