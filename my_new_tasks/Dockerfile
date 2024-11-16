FROM python:3.9-bookworm

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
#  Install dependencies for GDAL and wkhtmltopdf
RUN apt-get install -y gdal-bin libgdal-dev wkhtmltopdf

# Setup user and work directory
ENV PY_USER=pyuser
ENV WORK_DIR=/app
RUN useradd -ms /bin/bash $PY_USER
ENV PATH="/home/${PY_USER}/.local/bin:${PATH}"

# Copy the current directory contents into the container at /app
WORKDIR $WORK_DIR
# Change ownership of the working directory to the non-root user
RUN chown -R $PY_USER:$PY_USER $WORK_DIR
COPY . $WORK_DIR

# Switch to the non-root user
USER $PY_USER


RUN pip install --upgrade pip
# dependency for debug and remote attach.
RUN pip install --no-cache-dir debugpy ipython python-dotenv

# Install the project requirements
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt


# CMD ["handler.lambda_handler"]
# ENTRYPOINT []
