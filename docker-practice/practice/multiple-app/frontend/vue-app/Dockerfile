FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
 
COPY ./nginx-frontend.conf /etc/nginx/conf.d

RUN mv /etc/nginx/conf.d/nginx-frontend.conf /etc/nginx/conf.d/default.conf

WORKDIR /app

COPY ./dist .
 
EXPOSE 80
 
CMD ["nginx", "-g", "daemon off;"]