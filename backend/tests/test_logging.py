"""Logging configuration tests."""

import logging

from app.core.logging import configure_logging


def test_logging_configuration_does_not_duplicate_handlers() -> None:
    configure_logging("INFO")
    configure_logging("INFO")

    assert len(logging.getLogger().handlers) == 1
