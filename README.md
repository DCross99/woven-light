# woven-light

Provides an api to schedule tasks to gather the tube disruptions for given lines

## API
The Api has one endpoint `/tasks` where you can pass it a given id like so: `/tasks/<id>`

### GET Request
GET request with no id the API will return all tasks
```bash
 curl -X GET http://localhost:5555/tasks
```

GET request with id the API will return specific task
```bash
 curl -X GET http://localhost:5555/tasks/<id>
```

### POST Request
The API accepts a post request of this format:
```bash
curl -X POST -H 'Content-Type: application/json' -d '{"scheduler_time" :
"2021-11-12T17:00:00", "lines":"victoria,central"}'
http://localhost:5555/tasks
```


## Building

To build the API, DB and TFL Scraper run the following command
```bash
docker-compose up --build
```
You will then be able to make cURL calls to the endpoint

## Testing

To run the (limited) tests you use the command
```bash
python -m pytest .
```
I wanted to have expanded on the tests (especially integration-tests) but ran out of time. 
I have included in the file test_e2e.py my desired tests