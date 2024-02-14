FROM python:3.12.1-bookworm

 
RUN mkdir -p /home/app

RUN cd /home/app

WORKDIR /home/app

COPY todo.py /home/app

COPY createdb.py /home/app

COPY edit_task.tpl /home/app

COPY help.html /home/app

COPY make_table.tpl /home/app

COPY new_task.tpl /home/app

 

RUN pip3 install bottle

RUN python /home/app/createdb.py


CMD ["python3", "todo.py"]

