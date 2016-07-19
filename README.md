## Description

Sample project for building a GIS Django Application

## Requirements

Docker 1.9.0+
Docker Compose 1.7.0+

## Getting Started

```
docker-compose build
docker-compose up
docker-compose exec phl-play-django ./manage.py migrate
docker-compose exec createsuperuser
```

After that you will need to either add data manually in the admin interface or use the `import_data` management command to import data from the [City of Philadelphia Facilities](http://data.phl.opendata.arcgis.com/datasets/b3c133c3b15d4c96bcd4d5cc09f19f4e_0.csv) dataset available from [Open Data Philly](https://www.opendataphilly.org/dataset/city-facilities-master-facilities-database).

The application should be available at `localhost:9100` for the UI, API, and admin interface.
