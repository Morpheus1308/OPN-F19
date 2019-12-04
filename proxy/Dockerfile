FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

COPY html /usr/share/nginx/html
RUN mkdir ssl
COPY ssl /ssl
COPY nginx.conf /etc/nginx/nginx.conf