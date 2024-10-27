from logging import Logger
import os
from typing import Tuple
from app.sdk.scraped_data_repository import ScrapedDataRepository
from app.sdk.models import ProtocolEnum

def setup_csv_scraper(
    job_id: int,
    logger: Logger,
    output_path: str,
    protocol: ProtocolEnum
) -> ScrapedDataRepository:
    """
    Setup for the CSV scraper.
    """
    logger.info(f"{job_id}: Setting up CSV scraper.")
    # Setup the file repository and other necessary services
    file_repository = ScrapedDataRepository(protocol=protocol)

    return file_repository
