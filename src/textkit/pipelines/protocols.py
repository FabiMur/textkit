import argparse
from typing import Protocol


class Pipeline(Protocol):
    def run(self, args: argparse.Namespace) -> str: ...
