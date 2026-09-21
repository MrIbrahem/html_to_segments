"""
Library package for CX server.
"""

from __future__ import annotations

from .lib.processor import process_html
from .routes import HtmltoSegmentsRoutes

__all__ = [
    "HtmltoSegmentsRoutes",
    "process_html",
]
