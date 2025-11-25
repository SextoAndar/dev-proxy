FROM nginx:alpine
COPY nginx.conf.template /etc/nginx/conf.d/nginx.conf.template
COPY start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh
CMD ["start.sh"]
