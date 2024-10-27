import logging
import argparse
from app.setup import setup_csv_scraper
from csv_scraper import scrape_csv
from app.sdk.models import ProtocolEnum

def main(
    job_id: int,
    csv_url: str,
    output_path: str,
    protocol: ProtocolEnum,
    log_level: str = "INFO"
) -> None:
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=log_level)

    scraped_data_repository = setup_csv_scraper(
        job_id=job_id,
        logger=logger,
        output_path=output_path,
        protocol=protocol
    )

    scrape_csv(
        job_id=job_id,
        csv_url=csv_url,
        output_path=output_path,
        scraped_data_repository=scraped_data_repository,
        log_level=log_level
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape data from a CSV URL.")

    parser.add_argument(
        "--job-id",
        type=int,
        default=1,
        help="The job id"
    )

    parser.add_argument(
        "--csv-url",
        type=str,
        required=True,
        help="The CSV file URL to scrape"
    )

    parser.add_argument(
        "--output-path",
        type=str,
        default="stromproduktion_swissgrid.csv",
        help="The output path for the downloaded CSV"
    )

    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        help="Log level"
    )

    args = parser.parse_args()

    main(
        job_id=args.job_id,
        csv_url=args.csv_url,
        output_path=args.output_path,
        protocol=ProtocolEnum.S3,  # or `ProtocolEnum.LOCAL` based on environment
        log_level=args.log_level
    )
