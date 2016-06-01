FROM haproxy
COPY ./haproxy.cfg /data/
WORKDIR /data/
ENTRYPOINT ["haproxy", "-f", "haproxy.cfg"]

