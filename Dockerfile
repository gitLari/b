FROM terrillo/python3flask:latest

# STATIC paths for file.
# Don't use flask static. Nginx is your friend
ENV STATIC_URL /static
ENV STATIC_PATH /app/static
    
# Place your flask application on the server
COPY ./app /app
WORKDIR /app
    
# NGINX setup
COPY ./nginx.sh /nginx.sh
RUN chmod +x /nginx.sh
    
ENV PYTHONPATH=/app
    
ENTRYPOINT ["/nginx.sh"]

CMD ["/start.sh"]
    
EXPOSE 80 443