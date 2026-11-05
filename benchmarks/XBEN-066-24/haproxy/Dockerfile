FROM haproxy:2.0.5@sha256:5d58b57ff3fc232c57e4aec63fbd92c313ce6e65f22e729e3b1bd73c3a79095c

RUN sed -i 's/deb.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    sed -i '/buster-updates/d' /etc/apt/sources.list && \
    apt-get update && apt-get install -y curl 

COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg