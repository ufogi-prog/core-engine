import logging
from core_engine.config import Config
from core_engine.database import Database
from core_engine.services import ServiceManager

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Load configuration
    config = Config()

    # Connect to database
    db = Database(config.database_url)

    # Initialize service manager
    service_manager = ServiceManager(db)

    # Start services
    service_manager.start_services()

    # Keep the program running until manually stopped
    try:
        while True:
            pass
    except KeyboardInterrupt:
        # Stop services and close database connection
        service_manager.stop_services()
        db.close()

if __name__ == '__main__':
    main()