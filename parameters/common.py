from util.common_config import CommonConfig


class Common(CommonConfig):

    def get_base_url(self):
        return self.cp.get("common", "base_url")
