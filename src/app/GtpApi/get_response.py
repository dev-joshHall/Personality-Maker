from gptrim import trim

def get_gtp_response(user_message: str) -> str:
    return gtp_trim(user_message)

def gtp_trim(text: str) -> str:
    return trim(text)