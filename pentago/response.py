# 2024-11-29 Kiri, All rights reserved.
from pentago.update import Software
from pentago.hash import reset_license_cache

class Response:
    def __init__(self, status_code: int):
        self.status_code = status_code
        self._response = None

    def __repr__(self) -> str:
        return (
            self.__class__.__qualname__ +
            f'(status_code={self.status_code!r}, '
            f'response={self.response!r}'
        )

    @property
    def response(self) -> str:
        if self.status_code == 403:
            Software().update()
            reset_license_cache()
        return self.status_code == 200