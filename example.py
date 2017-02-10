import structlog
from pyrus import PyrusRenderer


structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        PyrusRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.PrintLoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()

logger.debug("bla bla", key="value")
logger.info("bla bla", key="value")
logger.warn("bla bla", key="value")
logger.error("bla bla", key="value", other={'hej': 'hej'})
