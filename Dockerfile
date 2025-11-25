FROM nginx:alpine

# Copiar o template
COPY nginx.conf.template /etc/nginx/conf.d/nginx.conf.template

# Usar envsubst para substituir $PORT em runtime
CMD /bin/sh -c "envsubst '\$PORT' < /etc/nginx/conf.d/nginx.conf.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"
