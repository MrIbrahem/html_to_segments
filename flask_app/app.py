"""
Flask application for HTML processing service.

This module provides a REST API for processing MediaWiki HTML through
the Content Translation pipeline. It exposes endpoints for HTML text
processing and health checks.

Endpoints:
    POST /HtmltoSegments - Process HTML through the CX pipeline
    GET /health - Health check endpoint

Security Considerations:
    - Input size is limited to prevent DoS attacks
    - Content-Type validation is enforced
    - Error messages are sanitized before returning to clients

Example:
    Running the development server::

        $ python flask_app/app.py

Author: mdwikicxpy
License: GPL-3.0
Version: 1.0.0
"""

from __future__ import annotations

import logging
import os

from flask import Blueprint, Flask
from flask_cors import CORS
from route import HtmltoSegmentsRoutes

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Security constants
MAX_JSON_SIZE = 15 * 1024 * 1024  # 15MB maximum JSON payload

app = Flask(__name__)
CORS(app)

# Set maximum content length for the application
app.config["MAX_CONTENT_LENGTH"] = MAX_JSON_SIZE

bp = Blueprint('HtmltoSegments', __name__, url_prefix='/')

HtmltoSegmentsRoutes.register(bp)

app.register_blueprint(bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    debug = True  #  os.environ.get("FLASK_DEBUG", "false").lower() == "true"

    logger.info(f"Starting Flask server on port {port} (debug={debug})")
    app.run(host="0.0.0.0", port=port, debug=debug)
