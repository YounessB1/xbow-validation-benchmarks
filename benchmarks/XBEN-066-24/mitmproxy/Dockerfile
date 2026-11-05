FROM --platform=linux/amd64 mitmproxy/mitmproxy:6.0.2@sha256:82bb3e80992ab469f11087522fdecdcc621b5e0cf1aba2906030ba6b57b9d3b3

WORKDIR /app

ENTRYPOINT mitmdump --mode reverse:http://${SERVER_HOSTNAME}:${SERVER_PORT} -p 8002 --set block_global=false --no-http2