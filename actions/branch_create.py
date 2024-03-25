#!/usr/bin/env python

from st2common.runners.base_action import Action
import gitlab


class GitlabBranchCreate(Action):

    # Retrieve config information
    def __init__(self, config):
        super(GitlabBranchCreate, self).__init__(config=config)
        self.url = self.config.get('url')
        self.token = self.config.get('token')

    def run(self, project_id, branch, ref_branch='main', token=None):

        # Use user token if given
        token = token or self.token

        # Initiate GitLab instance
        gl = gitlab.Gitlab(self.url, token)

        # Get the project with id == project_id
        project = gl.projects.get(project_id)

        # create branch
        new_branch = project.branches.create({'branch': branch, 'ref': ref_branch})

        return (True, new_branch.to_json(sort_keys=True, indent=4))
