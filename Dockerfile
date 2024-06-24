FROM python:latest

WORKDIR /eucalyptus-services

#  source  destination
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

# VOLUME [ "monvolume:/data" ]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# docker build -t eucalyptus-services:v1.0.0 .


# ----------------------------------------------------------
# Pour une DB :
# FROM postgres:latest

# ENV POSTGRES_USER=postgres
# ENV POSTGRES_PASSWORD=postgres
# ENV POSTGRES_DB=postgres

# WORKDIR "/data"

# COPY "init.sql" "/docker-entrypoint-initdb.d"

# EXPOSE 5432

# VOLUME [ "/var/postgres/pgdata:mydb_v" ]

# Et puis faire la commande dans le terminal :
# docker build -t mydb:v1.0.0 .

# ----------------------------------------------------------
# Et ensuite il faut faire un dossier qui comprend la DB et l'app et ajouter un fichier 'docker-compose.yml' avec les informations de la DB et de l'app :
# version: '1'

# networks:
#   monreseau:
#     internal: true
#     ipam :
#       driver: bridge
#       config:
#         - subnet: 10.0.0.0/16
#           ip_range: 10.0.0.0/24
#           gateway: 10.0.0.254

# services:
#   mydb:
#     container_name: db_postgres_c
#     image: mydb:v1.0.0
#     ports:
#       - "5432:5432"
#     volumes:
#       - mydb_v:/var/postgres/pgdata
#     restart: always
#     networks:
#       - monreseau:
#           ipv4_address: 10.0.0.2

#   myapp:
#     container_name: myapp_c
#     image: myapp:v1.0.0
#     ports:
#       - "8000:8000"
#     volumes:
#       - myapp_v:/data
#     depends_on:
#       - mydb
#     restart: unless-stopped
# autre option : restart: on-failure[10] pour redémarrer 10x si échec

#     networks:
#       - monreseau

# volumes:
#   mydb_v:

# Et enfin il faut faire un 'docker-compose up -d' pour build et lancer les deux containers.