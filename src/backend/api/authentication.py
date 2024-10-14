from rest_framework.authentication import TokenAuthentication

class TokenAuthenticationBase(TokenAuthentication):
    keyword = 'Bearer'

token_auth_base = TokenAuthenticationBase