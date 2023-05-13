# Import the modules that are needed in this program.
import sys
import logging

# Import the modules that are needed to interact with the Kubernetes API.
from kubernetes import client, config
from kubernetes.client.rest import ApiException

def main():
    # Loads the in-cluster Kubernetes configuration.
    config.load_incluster_config()

    # Instantiates a client object.
    v1 = client.CoreV1Api()

    # Gets a list of pods.
    pods = v1.list_pod_for_all_namespaces()

    # Lists pods in all namespaces.
    while True:
        try:
            # Gets a list of pods.
            pods = v1.list_pod_for_all_namespaces()
        except ApiException as e:
            # If an exception occurs, the program terminates.
            logging.error("Exception when calling CoreV1Api->list_pod_for_all_namespaces: %s\n" % e)
            sys.exit(1)

        # Prints IP addresses for pods in all namespaces.
        for pod in pods.items:
            logging.info("%s\t%s\t%s" % (pod.status.pod_ip, pod.metadata.namespace, pod.metadata.name))

if __name__ == '__main__':
    # Sets up logging.
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")

    # Calls main().
    main()
