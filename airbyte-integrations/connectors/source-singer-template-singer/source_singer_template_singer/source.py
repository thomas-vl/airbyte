"""
MIT License

Copyright (c) 2020 Airbyte

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from airbyte_protocol import AirbyteConnectionStatus
from base_python import AirbyteLogger
from base_singer import SingerSource


class SourceSingerTemplateSinger(SingerSource):
    def __init__(self):
        super().__init__()

    def check(self, logger: AirbyteLogger, config_container) -> AirbyteConnectionStatus:
        raise Exception("unimplemented")

    def discover_cmd(self, logger: AirbyteLogger, config_container) -> str:
        # discover the schema with the provided config
        raise Exception("unimplemented")

    def read_cmd(self, logger: AirbyteLogger, config_path, catalog_path, state_path=None) -> str:
        raise Exception("unimplemented")
