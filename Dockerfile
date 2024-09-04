FROM python:3.10
WORKDIR /K_N_B
COPY main.py main.py
CMD [ "python3","main.py" ]
