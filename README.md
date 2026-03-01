# watertank_display
a simple watertank simulated display that can be run in a container


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
git clone https://github.com/rmoorewrs/watertank_display.git
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
In the same git project directory run the test program
```
python3 test_post_level.py
```
> Note: the test program assumes port 5000. Edit the code to change it
