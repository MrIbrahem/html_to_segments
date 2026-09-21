"""
Library package for CX server.
"""

from __future__ import annotations

from .lib.processor import process_html
from .lib.mw.mw_page_loader import MWPageLoader

__all__ = [
    "MWPageLoader",
    "process_html",
]
