#!/usr/bin/env python

from st2common.runners.base_action import Action
import gitlab

"""     
    Modify and commit files content on a GitLab project.

    self, project_id, files_to_modify, commit_message, branch, token=None

    Parameters:
        project_id (str): The ID of the GitLab project.
        files_to_modify (list): A list of dictionaries, each containing 'file_path' and 'content' keys representing files to modify.
        branch (str): The name of the branch to commit changes to.
        commit_message (str): The commit message.
        token (str): The private access token for authentication.

    Returns:
        gitlab commit json object serialized
    
"""

class GitlabFileSaveContent(Action):

    # Retrieve config information
    def __init__(self, config):
        super(GitlabFileSaveContent, self).__init__(config=config)
        self.url = self.config.get('url')
        self.token = self.config.get('token')

    def run(self, project_id, files_to_modify, commit_message, branch, token=None):
        # Use user token if given
        token = token or self.token

        # Initiate GitLab instance
        gl = gitlab.Gitlab(self.url, token)

        # Get the project with id == project_id
        project = gl.projects.get(project_id)

        # Generating commit actions
        commit_actions = list(map(lambda file_info: {'action': 'update', 'file_path': file_info['file_path'], 'content': file_info['content']}, files_to_modify))

        # Prepare commit command
        commit_create = {
                'branch': branch,
                'commit_message': commit_message,
                'actions': commit_actions
            }

        # Commit and push the modifications to the new branch
        commit = project.commits.create(commit_create)

        return (True, commit.to_json(sort_keys=True, indent=4))
