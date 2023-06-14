# Get version at https://knative.dev/docs/install/yaml-install/serving/install-serving-with-yaml/
# 
export KNATIVE_VERSION="v1.10.1" # ensure ISTIO install matches this version too

# Install knative serving
# Ref: https://knative.dev/docs/install/yaml-install/serving/install-serving-with-yaml/#install-the-knative-serving-component
kubectl apply -f https://github.com/knative/serving/releases/download/knative-$KNATIVE_VERSION/serving-crds.yaml
kubectl apply -f https://github.com/knative/serving/releases/download/knative-$KNATIVE_VERSION/serving-core.yaml


# install istio
# Ref: https://knative.dev/docs/install/yaml-install/serving/install-serving-with-yaml/#install-a-networking-layer
kubectl apply -l knative.dev/crd-install=true -f https://github.com/knative/net-istio/releases/download/knative-$KNATIVE_VERSION/istio.yaml
kubectl apply -f https://github.com/knative/net-istio/releases/download/knative-$KNATIVE_VERSION/istio.yaml
kubectl apply -f https://github.com/knative/net-istio/releases/download/knative-$KNATIVE_VERSION/net-istio.yaml

# Confirm installed:
kubectl --namespace istio-system get service istio-ingressgateway
export KNATIVE_INGRESS_IP=$(kubectl --namespace istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

echo "Your IP Address is: $KNATIVE_INGRESS_IP"
echo "Add a cname record for your domain using the above IP address."