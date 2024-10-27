import requests
import pandas as pd
import logging
from app.sdk.scraped_data_repository import ScrapedDataRepository
from app.sdk.models import KernelPlancksterSourceData, BaseJobState, JobOutput

def download_csv(url: str, output_path: str) -> bool:
    """
    Download a CSV file from a URL.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_path, 'wb') as file:
                file.write(response.content)
            return True
        else:
            return False
    except Exception as e:
        logging.error(f"Failed to download CSV: {e}")
        return False

def scrape_csv(
    job_id: int,
    csv_url: str,
    output_path: str,
    scraped_data_repository: ScrapedDataRepository,
    log_level: str = "INFO"
) -> JobOutput:
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=log_level)

    job_state = BaseJobState.CREATED
    output_data_list = []

    try:
        # Attempt to download the CSV file
        if download_csv(csv_url, output_path):
            logger.info(f"{job_id}: Successfully downloaded CSV.")
            # Read and process the CSV
            df = pd.read_csv(output_path)
            logger.info(f"{job_id}: CSV read successfully. Processing data...")

            # Save the processed file using the scraped data repository (similar to the Telegram scraper)
            csv_data = KernelPlancksterSourceData(
                name="stromproduktion_swissgrid",
                protocol=scraped_data_repository.protocol,
                relative_path=output_path
            )

            scraped_data_repository.register_scraped_json(
                csv_data,
                job_id,
                output_path
            )

            output_data_list.append(csv_data)

            job_state = BaseJobState.FINISHED
        else:
            job_state = BaseJobState.FAILED
            logger.error(f"{job_id}: Failed to download CSV.")

    except Exception as error:
        job_state = BaseJobState.FAILED
        logger.error(f"{job_id}: Error processing CSV. {error}")

    return JobOutput(
        job_state=job_state,
        tracer_id=str(job_id),
        source_data_list=output_data_list
    )
