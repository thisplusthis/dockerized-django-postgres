### Setup
1. Clone the repository.
2. Ensure docker, docker-compose, podman (optional) is installed.

### Pure Docker
    `docker-compose up -d --build`

### Podman
    `podman machine init`
    `podman machine set --rootful`
    `podman machine start`
    `docker-compose up -d --build`
 
### See stuff
Logs: `docker logs -f django`
Hello World page:  `http://localhost:8000/`
    
### Admin user deets
Url: `http://localhost:8000/restricted/admin/`  
Username: `testicles`  
Password: `motu123`

### Get into container(s)
Docker: `docker exec -ti django bash`
Podman: `podman exec -ti django bash`

### Shutdown / Clean up
1. `docker-compose down`  
2. `docker system prune --volumes`

