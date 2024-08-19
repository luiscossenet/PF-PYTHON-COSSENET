from datetime import timedelta
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Comprueba si el usuario está autenticado
        if request.user.is_authenticated:
            now = timezone.now()
            # Si no hay una última actividad registrada, la establece
            if 'last_activity' not in request.session:
                request.session['last_activity'] = now.isoformat()
            else:
                last_activity = timezone.datetime.fromisoformat(request.session['last_activity'])
                elapsed_time = now - last_activity

                # Si el tiempo de inactividad supera el máximo permitido, cierra la sesión
                if elapsed_time > timedelta(seconds=settings.SESSION_COOKIE_AGE):
                    messages.warning(request, "Tu sesión ha expirado por inactividad.")
                    request.session.flush()  # Cierra la sesión
                    return redirect('login')  # Redirige al login (modifica según tu vista de login)
                else:
                    # Si la sesión está a punto de expirar, avisa al usuario
                    remaining_time = timedelta(seconds=settings.SESSION_COOKIE_AGE) - elapsed_time
                    if remaining_time.total_seconds() < 300:  # Muestra aviso si quedan menos de 5 minutos
                        messages.warning(request, f"Tu sesión expirará en {int(remaining_time.total_seconds() // 60)} minutos.")

                # Actualiza la última actividad
                request.session['last_activity'] = now.isoformat()

        response = self.get_response(request)
        return response
