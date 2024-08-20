# Dockerfile
FROM nginx:alpine
# Acepta un argumento para el folder dist
ARG DIST_FOLDER
ENV NGINX_ROOT /usr/share/nginx/html

# Elimina los archivos predeterminados de nginx
RUN rm -rf $NGINX_ROOT/*


# Copia los archivos del ambiente específico
COPY ./package*/${DIST_FOLDER}/* /usr/share/nginx/html/
COPY ./package*/${DIST_FOLDER}/*.conf etc/nginx/conf.d/default.conf 


RUN chown -R 101:101 /usr/share/nginx/html/

# Exponer el puerto de NGINX (80)
EXPOSE 80