#!/usr/bin/env python

from st2common.runners.base_action import Action
import gitlab

class GitlabMergeRequestCreate(Action):

    # Retrieve config information
    def __init__(self, config):
        super(GitlabMergeRequestCreate, self).__init__(config=config)
        self.url = self.config.get('url')
        self.token = self.config.get('token')

    def run(self, project_id, source_branch, target_branch, title, description, remove_source_branch, token=None):

        # Use user token if given
        token = token or self.token

        # Initiate GitLab instance
        gl = gitlab.Gitlab(self.url, token)

        # Get the project with id == project_id
        project = gl.projects.get(project_id)

        # Create the merge request
        mr = project.mergerequests.create({
            'source_branch': source_branch,
            'target_branch': target_branch,
            'title': title,
            'description': description,
            'remove_source_branch': remove_source_branch
        })

        return (True, mr.to_json(sort_keys=True, indent=4))
