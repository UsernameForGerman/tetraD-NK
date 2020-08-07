FROM node:12.18.3-slim as build-stage

WORKDIR /cms

# COPY ./cms/package.json /cms/

# RUN npm i

COPY ./cms /cms

RUN ls

# RUN NODE_ENV=production npm run build

CMD ["npm", "start", "--NODE_ENV=production"]
