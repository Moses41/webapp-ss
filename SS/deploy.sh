# docker build -t selenium-chrome .

# docker run --rm -v "$(pwd)/screenshots:/screenshots" selenium-chrome
docker-compose down -v

docker-compose build --no-cache

docker-compose up