FROM python:latest
EXPOSE 8080

RUN adduser --disabled-password --gecos '' appuser
USER appuser
WORKDIR /home/appuser

RUN python3 -m pip install --upgrade pip
COPY --chown=appuser:appuser requirements.txt  .
RUN pip3 install -r requirements.txt

COPY --chown=appuser:appuser server.py ./
COPY --chown=appuser:appuser diabetes-model.pkl  diabetes-model.pkl
CMD python3 server.py
