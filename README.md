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
* `epic.search` - Search Epic

### Projects

* `project.info` - Returns project information

### Issues

* `issue.info` - Returns issue information
* `issue.create` - Create new Issue

### Pipelines

* `pipeline.list` - List all pipelines in a project
* `pipeline.trigger` - Create a new pipeline

### Branches

* `branch.create` - Create a new branch

### Files

* `file.get.content` - Get file content
* `file.save.content` - Commit a new file content
