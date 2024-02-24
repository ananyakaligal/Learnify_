FROM python:3.11

WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        apt-utils \
        locales \
        python3-yaml \
        rsyslog systemd systemd-cron sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the PIP_INDEX_URL
ENV PIP_INDEX_URL=https://pypi.org/simple

# Upgrade pip
RUN pip3 install --upgrade pip

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set the locale to avoid encoding issues
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Run Streamlit app
CMD ["streamlit", "run", "generate.py"]
