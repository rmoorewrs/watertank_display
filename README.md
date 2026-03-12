# watertank_display
a simple watertank simulated display that can be run in a container
![HTTP Display](https://github.com/rmoorewrs/watertank_display/blob/main/doc_img/tank-animation.gif)

## Requirements
- docker
  - preferably membership in the docker group so you can run docker without root
- python 3.x
- python packages 
  - flask
  - flask-restful


## Instructions
1) clone this repo
```
git clone https://github.com/rmoorewrs/doc_img/tank-animation.gif
```

2) Build the container
```
cd watertank_display
docker build -t watertank .
```

3) run the container
```
# map any port that works for you to 5000 inside the container
docker run --rm -p 5000:5000 watertank
```

4) Obeserve the Tank
- Open a browser to http://localhost:5000
> Note: the container is listening on all interfaces

5) Run the test program
Run the test `cycle_drain_fill.py` program in the same directory
```
python3 cycle_drain_fill.py 
```
> Note: the test program assumes port 5000. Edit the code to change it


### Test the API using curl

#### Get tank level:
```
curl http://192.168.12.54:5000/level
```
Expected Response (example):
```
{
    "level": 26
}
```


#### Set tank level (force level):
```
curl -X POST http://192.168.12.54:5000/level -H "Content-Type: application/json" -d '{"level": 75}'
```
Expected Response (example):
```
{
    "level": 75
}
```
#### Drain water from the tank:
Example: drain 1% of the water
```
 curl -X POST http://192.168.12.53:5000/drain -H "Content-Type: application/json" -d '{"delta_level": 1}'
```
Expected Response (example):
```
{
    "level": 73,
    "mode": "drain"
}
```
#### Add water to the tank:
Example: add 1% of tank's capacity
```
 curl -X POST http://192.168.12.53:5000/fill -H "Content-Type: application/json" -d '{"delta_level": 1}'
```
Expected Response (example):
```
{
    "level": 74,
    "mode": "fill"
}
```

