FROM python
WORKDIR /home/myapp
COPY requirement.txt /home/myapp/
RUN pip install -r requirement.txt
COPY database.py /home/myapp/
COPY producer.py /home/myapp/
COPY scheduler.py /home/myapp/
#EXPOSE 15672
CMD python3 /home/myapp/scheduler.py