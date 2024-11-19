import logging
import argparse
from app.setup import setup_csv_scraper
from app.sdk.models import KernelPlancksterSourceData, BaseJobState
from app.sdk.scraped_data_repository import ScrapedDataRepository
from app.setup import setup
from app.scraper import scrape_csv
from app.sdk.models import ProtocolEnum

def main(
    job_id: int,
    csv_url: str,
    output_path: str,
    protocol: ProtocolEnum,
    kp_host: str,
    kp_port: str,
    kp_auth_token: str,
    kp_scheme: str,
    log_level: str = "INFO"
) -> None:
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=log_level)

    kernel_planckster, protocol, file_repository = setup(
            job_id=job_id,
            logger=logger,
            kp_auth_token=kp_auth_token,
            kp_host=kp_host,
            kp_port=kp_port,
            kp_scheme=kp_scheme,
        )
    
    scraped_data_repository = ScrapedDataRepository(
        protocol=protocol,
        kernel_planckster=kernel_planckster,
        file_repository=file_repository,
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
        "--kp_host",
        type=str,
        default="60",
        help="kp host",
    )

    parser.add_argument(
        "--kp_port",
        type=int,
        default="60",
        help="kp port",
    )

    parser.add_argument(
        "--kp_auth_token",
        type=str,
        default="60",
        help="kp auth token",
        )

    parser.add_argument(
        "--kp_scheme",
        type=str,
        default="http",
        help="kp scheme",
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
        kp_host=args.kp_host,
        kp_port=args.kp_port,
        kp_auth_token=args.kp_auth_token,
        kp_scheme=args.kp_scheme,
        log_level=args.log_level
    )
