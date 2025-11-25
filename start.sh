envsubst '$PORT' < /etc/nginx/conf.d/nginx.conf.template > /etc/nginx/conf.d/default.conf
cat /etc/nginx/conf.d/default.conf
exec nginx -g 'daemon off;'