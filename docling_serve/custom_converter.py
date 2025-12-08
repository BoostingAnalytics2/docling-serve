"""Custom converter manager factory.

The actual custom defaults (Hunyuan OCR, EGRET_XLARGE) are now configured 
directly in docling via environment variables:

- DOCLING_USE_HUNYUAN_TABLES=true
- DOCLING_HUNYUAN_SERVER_URL=http://hunyuan-ocr-proxy:8000
- DOCLING_HUNYUAN_SCALE=3.0
- DOCLING_USE_EGRET_XLARGE_LAYOUT=true

This module provides a factory function for consistency with the rest of the codebase.
"""

import logging
import os

from docling_jobkit.convert.manager import (
    DoclingConverterManager,
    DoclingConverterManagerConfig,
)

_log = logging.getLogger(__name__)


def get_converter_manager(config: DoclingConverterManagerConfig) -> DoclingConverterManager:
    """
    Factory function to get the converter manager.
    
    Logs the configuration status for Hunyuan and EGRET_XLARGE.
    """
    hunyuan_url = os.environ.get("DOCLING_HUNYUAN_SERVER_URL")
    use_hunyuan = os.environ.get("DOCLING_USE_HUNYUAN_TABLES", "").lower() in ("true", "1", "yes")
    use_egret = os.environ.get("DOCLING_USE_EGRET_XLARGE_LAYOUT", "").lower() in ("true", "1", "yes")
    
    if use_hunyuan and hunyuan_url:
        _log.info(f"Hunyuan table structure enabled via env: {hunyuan_url}")
    
    if use_egret:
        _log.info("EGRET_XLARGE layout model enabled via env")
    
    return DoclingConverterManager(config)
