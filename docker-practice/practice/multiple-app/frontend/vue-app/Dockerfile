FROM node:18 as build

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

RUN npm run build

FROM nginx:latest

WORKDIR /app

RUN rm /etc/nginx/conf.d/default.conf
 
COPY ./nginx-frontend.conf /etc/nginx/conf.d

RUN mv /etc/nginx/conf.d/nginx-frontend.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

COPY --from=build /app/dist .
 
CMD ["nginx", "-g", "daemon off;"]