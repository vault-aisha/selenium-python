import pytest
from utils.driver_factory import get_driver
from utils.logger import get_logger

@pytest.fixture
def setup(request):
    logger = get_logger(request.node.name)
    driver = get_driver()
    logger.info("Browser started")

    yield driver

    driver.quit()
    logger.info("Browser closed")
