# Use an official Python runtime as a base image
FROM python:3.6

ENV FLASK_APP hello.py
ENV INSROOT /opt/app
ENV APPUSER python-docker
ENV APPDIR ${INSROOT}/${APPUSER}

RUN useradd -d ${APPDIR} ${APPUSER}

WORKDIR ${APPDIR}

EXPOSE 5000

# Copy the current directory contents into the container at ${APPDIR}
ADD hello.py ./
ADD requirements.txt ./
RUN pip install -r requirements.txt


RUN chown -R ${APPUSER}:${APPUSER} ${APPDIR}

USER ${APPUSER}

# Run flask server
CMD ["flask", "run","--host=0.0.0.0"]
