# Użyj obrazu Ubuntu z graficznym środowiskiem
FROM ubuntu:22.04


# Zainstaluj zależności systemowe wymienione w dokumentacji SUMO
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:sumo/stable && \
    apt-get update


RUN apt-get install -y \
    wget \
    git \
    cmake \
    g++ \
    libxerces-c-dev \
    libfox-1.6-dev \
    libgdal-dev \
    libproj-dev \
    libgl2ps-dev \
    swig \
    python3 \
    python3-pip \
    python3-dev \
    python3-setuptools \
    libeigen3-dev \
    libopenmpi-dev \
    openmpi-bin \
    libosmpbf-dev \
    libbz2-dev \
    libz-dev \
    libtbb-dev \
    sumo \
    sumo-tools \
    sumo-doc \
    && rm -rf /var/lib/apt/lists/*

# Pobierz i zainstaluj SUMO z repozytorium Git


# Ustaw katalog roboczy
WORKDIR /workspace

# Uruchom bash jako domyślne polecenie
CMD ["bash"]