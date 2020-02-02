# mchacks2020

1 create a venv

2 in the venv do `pip install pyats[full]`

3 #todo
```
docker build .
docker run -it -p 2222:22 -d --hostname mymock {image you just build}
genie shell --testbed-file testbed.yaml
```