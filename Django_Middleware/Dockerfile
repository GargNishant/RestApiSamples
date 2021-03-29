FROM postgres:13.2
ENV POSTGRES_USER middleware
ENV POSTGRES_PASSWORD password
ENV POSTGRES_DB middleware
COPY tables.sql /docker-entrypoint-initdb.d/
