FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY cert /etc/nginx/cert/
COPY sites.conf /etc/nginx/sites-available/
RUN mkdir -p /etc/nginx/sites-enabled/ && ln -s /etc/nginx/sites-available/sites.conf /etc/nginx/sites-enabled/

CMD ["nginx", "-g", "daemon off;"]

