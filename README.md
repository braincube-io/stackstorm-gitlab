# Gitlab Integration Pack

Gitlab API v4 supported.

## Configuraton

```yaml
url: http://gitlab.example.com
token: private-token
verify_ssl: False
```

## Actions

### Epics

* `epic.create` - Create new Epic

### Projects

* `project.info` - Returns project information

### Issues

* `issue.info` - Returns issue information

### Pipelines

* `pipeline.list` - List all pipelines in a project
* `pipeline.trigger` - Create a new pipeline
