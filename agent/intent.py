def detect_intent(message: str) -> str:
    if "price" in message or "cost" in message:
        return "high_intent"
    elif "hello" in message.lower():
        return "greeting"
    return "product_inquiry"
