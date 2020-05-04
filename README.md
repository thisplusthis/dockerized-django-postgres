### Installation
1. Clone the repository
2. Ensure docker is installed 
3. Start container:  
    `docker-compose up -d --build`
4. The entry-point script will take a few extra seconds to start the server.
5. Watch the logs to see when the server is ready...  
    `docker logs -f django`    
 
### See stuff
Hello World page:  `http://localhost:8000/` 
    
### Admin user deets
Url: `http://localhost:8000/restricted/admin/`  
Username: `testicles`  
Password: `motu123`

### Get into the container
`docker exec -ti django bash`

### Shutdown / Clean up
1. `docker-compose down`  
2. `docker system prune --volumes`

