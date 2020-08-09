FROM node:12.18.3-slim as build-stage

WORKDIR /landing

COPY ./landing/package.json /landing/

RUN npm i

COPY ./landing /landing

RUN npm run build

RUN ls
RUN ls /landing/public

FROM nginx:alpine

WORKDIR /www

RUN apt-get install certbot python3-certbot-nginx

RUN mkdir build

COPY --from=build-stage /landing/build /www/build

RUN rm /etc/nginx/conf.d/*
COPY ./deploy/local/landing/landing.conf /etc/nginx/conf.d/

