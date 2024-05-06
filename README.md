## Redis Cleaning Sidecar

This is a sidecar container that can be used to clean up keys in a Redis database. It is designed to be used in a Kubernetes environment, but can be used in any environment that can run a Docker container.

### Building the Docker Image

To build the Docker image, run the following command:

```bash 
docker build -t localhost/caching-cleaner .
```

### Running the Docker Image

To run the Docker image, you will need to provide the following environment variables:

- `REDIS_HOST`: The hostname of the Redis server
- `REDIS_PORT`: The port of the Redis server
- `REDIS_PASSWORD`: The password of the Redis server
- `KEY_PATTERN`: The pattern of the keys to delete
- `REDIS_DATABASES`: The number of Redis databases to clean (optional, default is '0,1,2')

Here is an example of how to run the Docker image:

```bash
docker run -e REDIS_HOST=redis -e REDIS_PORT=6379 -e REDIS_PASSWORD=password -e KEY_PATTERN='test*' -e REDIS_DATABASES='0,1,2' localhost/caching-cleaner
```