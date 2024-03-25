#!/usr/bin/env python

from st2common.runners.base_action import Action
import gitlab


class GitlabEpicSearch(Action):

    # Retrieve config information
    def __init__(self, config):
        super(GitlabEpicSearch, self).__init__(config=config)
        self.url = self.config.get('url')
        self.token = self.config.get('token')

    def run(self, group_id, title='', labels=[], token=None):

        # Use user token if given
        token = token or self.token

        # Initiate GitLab instance
        gl = gitlab.Gitlab(self.url, token)

        if not group_id:
            return (False, {"message": "group_id not provided"})
        
        group = gl.groups.get(group_id)

        # Search epic
        epics = group.epics.list(search=title,labels=labels)
        return (True, {"epics":  list(map(lambda e: e.to_json(sort_keys=True, indent=4), epics))})
