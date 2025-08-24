import json

def handler(request):
    body = json.loads(request.body)
    user_message = body.get("message", "")

    # テスト用：送信された文字列に任意の文字を追加して返す
    final_reply = f"Bob先生: {user_message} 🌟（テスト応答）"

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"reply": final_reply}),
    }
