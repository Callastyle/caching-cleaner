import os
import redis
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Read environment variables
host = os.getenv('REDIS_HOST', 'localhost')
port = int(os.getenv('REDIS_PORT', 6379))
password = os.getenv('REDIS_PASSWORD', 'redis_password')
pattern = os.getenv('KEY_PATTERN', 'nonexistent_key_pattern*')

database_indices = os.getenv('REDIS_DATABASES', '0,1,2')  # Default is "0,1,2"
databases = [int(db.strip()) for db in database_indices.split(',')]

# Connect and process each database
for db in databases:
    try:
        logging.info(f"Connecting to Redis on {host}:{port} DB {db}")
        r = redis.Redis(host=host, port=port, password=password, db=db, decode_responses=True)

        # Scan for keys matching the pattern and delete them
        cursor = '0'
        while cursor != 0:
            cursor, keys = r.scan(cursor=cursor, match=pattern, count=100)
            if keys:
                r.delete(*keys)
                logging.info(f"Deleted {len(keys)} keys from database {db} matching pattern '{pattern}'")
            else:
                logging.debug(f"No keys to delete from database {db} on this pass.")

        logging.info(f"Deletion of keys by pattern complete in database {db}.")
    except Exception as e:
        logging.error(f"An error occurred while processing database {db}: {e}")
