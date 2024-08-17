import socket
import platform
from django.utils import timezone
from user_agents import parse


class UserActivity:
    def __init__(self, request):
        self.request = request

    def get_ip_public(self):
        return self.request.META.get("REMOTE_ADDR")

    def get_ip_local(self):
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)

    def get_host_name(self):
        return socket.gethostname()

    def get_os(self):
        return platform.system()

    def get_browser(self):
        user_agent = parse(self.request.META.get("HTTP_USER_AGENT", ""))
        return user_agent.browser.family

    def get_user_activity(self):
        return {
            "ip_public": self.get_ip_public(),
            "ip_local": self.get_ip_local(),
            "host_name": self.get_host_name(),
            "os": self.get_os(),
            "browser": self.get_browser(),
            "updated_at": timezone.now(),
        }
