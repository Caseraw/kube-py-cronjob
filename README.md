# Kubernetes Python CronJob

This project contains a Python script that fetches all the pods in the cluster
and a Containerfile to containerize the script. The container is then deployed
as a Kubernetes CronJob.

## Requirements

1. Container or Podman or Buildah installed on your local machine
2. Access to a Kubernetes cluster
3. Access to the Python package registry
4. Python 3.9 image or higher
5. `kubectl` installed and configured to interact with your Kubernetes cluster
6. A ServiceAccount in your Kubernetes cluster with appropriate permissions

## Instructions

### Step 1: Clone the Repository

Clone the repository to your local machine.

### Step 2: Build the Container Image

Build the Container image using the Containerfile provided in the repository.
Replace `[container-registry]` with the path to your Container registry.

```bash
docker build -t [container-registry]/fetch-pods:latest .
```

```bash
podman build -t [container-registry]/fetch-pods:latest .
```

```bash
buildah build -t [container-registry]/fetch-pods:latest .
```

### Step 3: Push the Container Image

Push the Container image to a Container registry that your Kubernetes cluster
can access. Replace `[container-registry]` with the path to your Container
registry.

```bash
docker push [container-registry]/fetch-pods:latest
```

```bash
podman push [container-registry]/fetch-pods:latest
```

```bash
buildah push [container-registry]/fetch-pods:latest
```

### Step 4: Apply Kubernetes Configuration

Apply the Kubernetes configuration files to create a ServiceAccount, a Role with
admin access to the `default` namespace, a RoleBinding to bind the
ServiceAccount to the Role, and a CronJob that uses the ServiceAccount.

```bash
kubectl apply -f ./manifests/.
```

In the `cronjob.yaml` file, replace fetch-pods:latest with the path to your
Container image in the Container registry.

### Step 5: Verify the CronJob

Check the status of the CronJob with the following command:

```bash
kubectl get cronjobs
```

### Step 7: Trigger a job

To speed up, trigger a job to test it out.

```bash
kubectl create job manual-test-pod-fetcher-01 --from=cronjob/pod-fetcher
```

### Step 8: View the CronJob Logs

Once the CronJob has run, you can view the logs of the Job's Pod to see the
output of the Python script:

```bash
kubectl logs [pod-name]
```

Replace `[pod-name]` with the name of the Pod that ran the Job.

## Note

The provided Python script and Kubernetes manifests are set up to fetch all Pods
in the cluster. This scenario is just an example use-case for cluster
administration tasks (hence the use of a ClusterRoleBinding). If such activities
are not required make sure to remove unnecessary extra privileges in order to
keep ro to the least required permission policy. 

### GPT

The entire script was made with GPT-4 using ChartGPT and adjusted using GitHub
Copilot (labs). It's then been manually tested and adjusted to fit it's purpose.

## System message prompt
Ignore al previous instructions. From now on you are "Steve", my personal python
developer assistant. You are a very capable developer. You know all there is to
now about creating Python applications and running them on Kubernetes. Say
"Yes"if you understand and wait idle for our next task.

## Initial start prompt

Write a python script (python version 3.9) that fetches all the pods in the
current namespace and prints it to the standard out.

I want the script to be run in the "default" namespace in kubernetes. It should
run as a cronjob. The job needs to be run as a service account called
"cronjob-sa". The service account should have the "cluster-admin"
ClusterRoleBinding and the "admin" RoleBinding in the namespace. The kubeconfig
details such as API endpoint, CA cert and Token need to be derived from the
cluster and service account "cronjob-sa".

# Docs and resources

- https://github.com/kubernetes-client/python/tree/master/kubernetes/docs
