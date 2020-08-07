FROM node:12.18.3-slim as build-stage

WORKDIR /landing

COPY ./landing-nk/package.json /landing/

RUN npm i

COPY ./landing-nk /landing

RUN npm run build

RUN ls
RUN ls /landing/public

FROM nginx:alpine

WORKDIR /www

RUN mkdir build

COPY --from=build-stage /landing/build /www/build

RUN rm /etc/nginx/conf.d/*
COPY ./deploy/landing/landing.conf /etc/nginx/conf.d/

