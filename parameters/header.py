from util.common_config import CommonConfig


class Header(CommonConfig):

    def get_host(self):
        return self.cp.get("header", "Host")

    def get_connection(self):
        return self.cp.get("header", "Connection")

    def get_pragma(self):
        return self.cp.get("header", "Pragma")

    def get_cache_control(self):
        return self.cp.get("header", "Cache-Control")

    def get_user_agent(self):
        return self.cp.get("header", "User-Agent")

    def get_upgrade_insecure_requests(self):
        return self.cp.get("header", "Upgrade-Insecure-Requests")

    def get_accept(self):
        return self.cp.get("header", "Accept")

    def get_accept_encoding(self):
        return self.cp.get("header", "Accept-Encoding")

    def get_accept_language(self):
        return self.cp.get("header", "Accept-Language")