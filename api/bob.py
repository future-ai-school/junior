# api/bob.py

def handle(message: str) -> str:
    """
    Bob用のテスト関数。
    message を受け取り、少し加工して返すだけのサンプル。
    """
    # 適当に文字列を加工
    reply = f"Bobからの返答: {message[::-1]}"  # 文字列を逆にして返す例
    return reply
