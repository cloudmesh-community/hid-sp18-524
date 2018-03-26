# Deploying Raspberry Pi cluster with Docker Swarm

To achieve this tutorial, you will need at least two Raspberry Pi , their power supplies , as well as micro-SD card(8GB is sufficient).



### Step 1 - Install Docker on Raspberry Pi
Connect Pi in SSH and type the following command:

```
$ curl -sSL https://get.docker.com | sh
```

### Step 2 - Setting up the Raspberry Pi cluster with Docker Swarm
Initializing the cluster

First, we start by initializing the cluster, for that we execute the command docker swarm init on the Raspberry Pi Manager.
Once the command is issued, the terminal will send you instructions to add workers to your cluster.

```
$sudo docker swarm init
```
As you can see, Docker Swarm has just been initialized. To add your Raspberry Pi to the Docker cluster, we just have to connect to the second Pi (raspWorker01) in SSH and then paste the command that was given to us, here docker swarm join -token SWMTKN-1-0fomfa1ogeibc67p3fdxn4ea17g8jsvbtip52qptky3h7w5th4-8efjokb38uhtdqgvg3df874l 192.168. 1.100: 2377

```
$sudo docker swarm join --token SWMTKN-1-0fomfa1ogeibc67p3fdxn4ea17g8jsvbtip52qptky3h7w5th4-8efjokb38uhtdqgvg3idf874l 192.168.1.100:2377
```
Warning, the token that the manager gives is never the same, please copy the command given by your Raspberry Manager.
After validating the command on the worker, the terminal will inform you of the success of the addition.

```
This node joined a swarm as a worker.
```


### Step 3 - Check the status of the cluster
You can check the status of the cluster with the docker node ls command at any time, and run this command on the Manager machine.
```sh
$ sudo docker node ls
```
