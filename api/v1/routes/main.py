import logging
import os
import sys
from core_engine import config, utils

def main():
    # Initialize logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Starting core-engine application')

    # Load configuration
    config.load_config()

    # Validate environment
    if not os.environ.get('CORE_ENGINE_ENV'):
        logging.error('CORE_ENGINE_ENV environment variable is not set')
        sys.exit(1)

    # Run application
    try:
        utils.run_application()
    except Exception as e:
        logging.error(f'Error running application: {str(e)}')
        sys.exit(1)

    logging.info('core-engine application stopped')

if __name__ == '__main__':
    main()