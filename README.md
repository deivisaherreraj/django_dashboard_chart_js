## Running the Project Locally

First, clone the repository to your local machine:

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Load the data from fixtures:

```bash
python manage.py loaddata type-violent-deaths.json violent-deaths.json gender.json type-domestic-violence.json domestic-violence.json built-by.json living-place.json type-infrastructure.json state-infrastructure.json infrastructure-road.json vehicle-type.json vehicle.json
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## License

The source code is released under the [MIT License](https://github.com/Prospect121/django_dashboard_chart_js/blob/master/LICENSE.md).
