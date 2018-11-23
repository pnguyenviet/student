from rest_framework import permissions, status, exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from django.contrib.auth.models import User
from django.http import HttpResponse
import jwt

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

class TokenAuthentication(BaseAuthentication):

    model = None

    def get_model(self):
        return User
    
    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b'token':
            return None
        
        if len(auth) == 1:
            msg = 'Invalid toke header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header'
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1]
            if token=='null':
                msg = 'Null token not allowed'
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters'
            raise exceptions.AuthenticationFailed(msg)
        
        return self.authenticate_credentials(token)
    
    def authenticate_credentials(self, token):
        model = self.get_model()
        payload = jwt.decode(token, "SECRET_KEY")
        email = payload['email']
        userid = payload['id']
        msg = {'Error': 'Token mismatch', 'status':'401'}
        try:
            user = User.objects.get(
                email = email,
                id = userid,
                is_active=True
            )
            if not user.token['token'] == token:
                raise exceptions.AuthenticationFailed(msg)

        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            return HttpResponse({'Error':'Token is invalid'}, status='403')
        # except IndentationError:
        #     return HttpResponse({'Error':'internal server error'}, status='500')
    
    def authenticate_header(self, request):
        return 'Token'    




