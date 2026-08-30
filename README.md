# Simple php with database Docker recipe

* This is a php recipe. But it's base is Ubuntu 24.04. Base the setup to a vanilla user Linux make it more friendly in caso you don't have a containerzed docker at your disposal.
* Devpod and container: this recipe is tested first together to Devpod and its containerzation schema. Look to the `.devcontainer` folder as well to see some usefull configurations to the devcontainer that is first tested with Devpod.
* PHP 8.5: most recent PHP so far. Also is usefull see how to setup an specifiv PHP version.
* Basic Linux packages to work together with PHP.
* sshd and user inside container: as to be friendly to a not containerzed environment and also in some situations where the Docker conveniences is not working, there's an user with a password and its directory inside container, along with the sshd service. So you can access the container through ssh, not having to use anything from Docker.
* "host.docker.internal:host-gateway" at the `docker-compose.yml` configuration: expose the host network environment to allow to access host resources withing container.