# coding: utf-8
"""Модуль инициализации логирования в приложении"""

import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
