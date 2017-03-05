FROM nginx:stable-alpine

RUN echo "This is custom image" > /usr/share/nginx/html/index.html
