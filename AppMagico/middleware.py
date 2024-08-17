from django.shortcuts import redirect
from django.urls import resolve
from django.conf import settings
from django.contrib import messages


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resolver_match = resolve(request.path)
        view_name = resolver_match.view_name

        # Debugging para verificar si se está ejecutando correctamente
        print(f"Path: {request.path}")
        print(f"View Name: {view_name}")
        print(f"User Authenticated: {request.user.is_authenticated}")

        if not request.user.is_authenticated:
            # Verifica si la vista actual es una de las que requieren autenticación
            if view_name.startswith("RV_v"):
                print("Redirecting to 'inicio'")
                messages.error(
                    request,
                    "Debe iniciar sesión para acceder a esta página",
                )

                return redirect("Login")

        response = self.get_response(request)
        return response
