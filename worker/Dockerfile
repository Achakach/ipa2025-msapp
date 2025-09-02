FROM python
WORKDIR /home/myapp
COPY . /home/myapp
RUN pip install -r requirements.txt
CMD python3 -u /home/myapp/worker.py
