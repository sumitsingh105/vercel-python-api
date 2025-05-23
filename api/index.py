import json
from urllib.parse import parse_qs
from data import marks_lookup

def handler(request):
    params = parse_qs(request.query_string.decode())
    names = params.get("name", [])
    marks = [marks_lookup.get(name, None) for name in names]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({"marks": marks})
    }