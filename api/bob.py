import json

def handler(request):
    try:
        body = json.loads(request.body)
        user_message = body.get("message", "")
        reply = f"Bob先生: {user_message} 🌟（テスト応答）"
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"reply": reply}),
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }
