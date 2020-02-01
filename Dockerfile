FROM gotechnies/alpine-ssh
RUN apk add --update python3
RUN mkdir /mock_device
COPY shell.py /mock_device
COPY mocks.py /mock_device
WORKDIR /mock_device