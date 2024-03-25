#!/usr/bin/env python

from st2common.runners.base_action import Action
import gitlab
import base64
from typing import Union

class GitlabFileGetContent(Action):

    # Retrieve config information
    def __init__(self, config):
        super(GitlabFileGetContent, self).__init__(config=config)
        self.url = self.config.get('url')
        self.token = self.config.get('token')

    def run(self, project_id, file_path, branch='main', decode_encoding='utf-8', token=None):

        # Use user token if given
        token = token or self.token

        # Initiate GitLab instance
        gl = gitlab.Gitlab(self.url, token)

        # Get the project with id == project_id
        project = gl.projects.get(project_id)

        f = project.files.get(file_path, ref=branch)

        if bool(decode_encoding):
            return (True, base64.b64decode(f.content).decode(decode_encoding) )
        else:
            # get the base64 encoded content
            return (True, base64.b64decode(f.content))
