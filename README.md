
    $ docker-compose exec app python /app/manage.py migrate
    $ docker-compose exec app python /app/manage.py collectstatic
    $ docker-compose exec app python /app/manage.py loaddata test_data.json 
    $ docker-compose exec app python /app/test_example_gogolook.py
