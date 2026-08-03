blacklisted_tokens = set()
def add_token_to_blacklist(jti):
    blacklisted_tokens.add(jti)
    return ({
        "success": True,
        "message": "Logged out successfully",
    }),200
def is_token_blacklisted(jti):
    return jti in blacklisted_tokens