import tiktoken

def count_tokens(text: str) -> int:
    enc = tiktoken.get_encoding("cl100k_base")
    result = enc.encode(text)
    return len(result)
