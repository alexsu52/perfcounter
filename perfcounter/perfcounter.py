# Copyright (C) 2023 Alexander Suslov
# Licensed under the Apache License, Version 2.0 (the "License");
# You may obtain a copy of the License at
# you may not use this file except in compliance with the License.
#         http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
from collections import defaultdict

from texttable import Texttable


class PerfCounter:
    """
    Manage performance counters
    """

    def __init__(self) -> None:
        self.start_time = {}
        self.total_time = defaultdict(lambda: 0)
        self.num_calls = defaultdict(lambda: 0)

    def start(self, name: str) -> None:
        self.start_time[name] = time.perf_counter()

    def end(self, name: str) -> None:
        if self.start_time[name] < 0:
            raise RuntimeError("end() method cannot be called before start()")
        self.total_time[name] += time.perf_counter() - self.start_time[name]
        self.num_calls[name] += 1
        self.start_time[name] = -1

    def report(self) -> str:
        header = ["name", "ncalls", "avg time", "wall time"]
        rows = []

        for name, wall_time in self.total_time.items():
            num_calls = self.num_calls[name]
            average_time = wall_time / num_calls
            rows.append((name, num_calls, average_time, wall_time))

        return Texttable().header(header).add_rows(rows, header=False).draw()


DEFAULT_PERF_COUNTER = PerfCounter()


def perf_start(name: str) -> None:
    DEFAULT_PERF_COUNTER.start(name)


def perf_end(name: str) -> None:
    DEFAULT_PERF_COUNTER.end(name)


def perf_report() -> str:
    return DEFAULT_PERF_COUNTER.report()
