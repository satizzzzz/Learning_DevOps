# Helm Details

## Helm Workflow

```
Helm is a package manager for Kubernetes. Why do we even need it?

Because application management in Kubernetes can be quite complicated. 

Helm reduces the complexity by introducing Helm Charts, reusable and configurable deployment units for Kubernetes applications.

A typical Helm workflow involves the following steps:

1️⃣ Helm Client 𝐟𝐞𝐭𝐜𝐡𝐞𝐬 Chart package from remote chart repository, such as Artifact Hub.

💲𝘩𝘦𝘭𝘮 𝘱𝘶𝘭𝘭 [𝘙𝘌𝘗𝘖𝘚𝘐𝘛𝘖𝘙𝘠]/[𝘊𝘏𝘈𝘙𝘛]

2️⃣ Helm Client 𝐜𝐨𝐧𝐯𝐞𝐫𝐭𝐬 Chart into a valid Kubernetes resource YAML.

💲𝘩𝘦𝘭𝘮 𝘵𝘦𝘮𝘱𝘭𝘢𝘵𝘦 [𝘙𝘌𝘓𝘌𝘈𝘚𝘌] [𝘊𝘏𝘈𝘙𝘛]

3️⃣ Helm Client 𝐬𝐞𝐧𝐝𝐬 raw YAML contents to the Kubernetes API server over HTTPS.

💲𝘩𝘦𝘭𝘮 𝘪𝘯𝘴𝘵𝘢𝘭𝘭 [𝘙𝘌𝘓𝘌𝘈𝘚𝘌] [𝘊𝘏𝘈𝘙𝘛]

4️⃣ Kubernetes API server 𝐚𝐩𝐩𝐥𝐢𝐞𝐬 desired resources (deployments, secrets, persistent volume claims, etc.).

```
![Helm_wf](https://github.com/satizzzzz/Learning_DevOps/assets/26127571/bf2b5070-cbb4-441c-bde4-48ec88d77f07)



