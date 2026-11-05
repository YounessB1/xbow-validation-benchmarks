FROM node:20-alpine@sha256:fb4cd12c85ee03686f6af5362a0b0d56d50c58a04632e6c0fb8363f609372293

RUN apk --no-cache add curl

WORKDIR /app
COPY . .
RUN npm install 
RUN npm run build
EXPOSE 3000
ARG FLAG
RUN sed -i s/@FLAG@/$FLAG/g .env

CMD ["npm", "start"]