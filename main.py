from jobscout.core.logger import logger
from jobscout.config.settings import settings


def main():
    logger.info("Starting JobScout AI")

    logger.info(f"Log level: {settings.log_level}")

    logger.success("Everything is working!")


if __name__ == "__main__":
    main()