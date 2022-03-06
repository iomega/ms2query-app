# ms2query-app
Web App to match and analyse large MS/MS datasets

Backend will run on [MS2Query](https://github.com/iomega/ms2query).


## Init

* Download model files: https://zenodo.org/record/6124553

* `cd ./backend`

* `docker build -t ms2query-app .`

* `cd ..`

* `docker-compose up --build`

## Useful command 

`docker-compose down -v`

