# devops-prova

![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)  ![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) 

A Helm chart for Kubernetes Devops Prova FIESC

# Installing the Chart

- Access a Kubernetes cluster.

- Change the values according to the need of the environment in ``devops-prova/values.yaml`` file. The [Parameters](#parameters) section lists the parameters that can be configured during installation.

- Test the installation with command:

```bash
helm upgrade --install devops-prova -f devops-prova/values.yaml devops-prova/ -n devops-prova --create-namespace --dry-run
```

- To install/upgrade the chart with the release name `devops-prova`:

```bash
helm upgrade --install devops-prova -f devops-prova/values.yaml devops-prova/ -n devops-prova --create-namespace
```

Create a port-forward with the follow command:

```bash
kubectl port-forward svc/devops-prova 3000:80 -n devops-prova
```

Open the browser and access the URL: http://localhost:3000

## Uninstalling the Chart

To uninstall/delete the `devops-prova` deployment:

```bash
helm uninstall devops-prova -n devops-prova
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Parameters

The following tables lists the configurable parameters of the chart and their default values.

Change the values according to the need of the environment in ``devops-prova/values.yaml`` file.

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` |  |
| autoscaling.enabled | bool | `false` |  |
| autoscaling.maxReplicas | int | `100` |  |
| autoscaling.minReplicas | int | `1` |  |
| autoscaling.targetCPUUtilizationPercentage | int | `80` |  |
| command | list | `[]` |  |
| configmap.enabled | bool | `false` |  |
| cron.command | list | `[]` |  |
| cron.enabled | bool | `false` |  |
| cron.image.pullPolicy | string | `"IfNotPresent"` |  |
| cron.image.repository | string | `""` |  |
| cron.image.tag | string | `""` |  |
| cron.restartPolicy | string | `"OnFailure"` |  |
| cron.schedule | string | `""` |  |
| extraEnv | list | `[]` |  |
| fullnameOverride | string | `""` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"nginx"` |  |
| image.tag | string | `""` |  |
| imagePullSecrets | list | `[]` |  |
| ingress.annotations | object | `{}` |  |
| ingress.className | string | `""` |  |
| ingress.enabled | bool | `false` |  |
| ingress.hosts[0].host | string | `"chart-example.local"` |  |
| ingress.hosts[0].paths[0].path | string | `"/"` |  |
| ingress.hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` |  |
| ingress.tls | list | `[]` |  |
| mySecret.enabled | bool | `false` |  |
| nameOverride | string | `""` |  |
| nodeSelector | object | `{}` |  |
| podAnnotations | object | `{}` |  |
| podLabels | object | `{}` |  |
| podSecurityContext | object | `{}` |  |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |
| securityContext | object | `{}` |  |
| service.port | int | `80` |  |
| service.type | string | `"ClusterIP"` |  |
| serviceAccount | object | `{"annotations":{},"automount":true,"create":true,"name":""}` | Configurations of the application. Create configMap and Secret for use in deployment as environment variable mySecret:  enabled: false  password: change-here This section builds out the service account more information can be found here: https://kubernetes.io/docs/concepts/security/service-accounts/ |
| tolerations | list | `[]` |  |
| volumeMounts | list | `[]` |  |
| volumes | list | `[]` |  |