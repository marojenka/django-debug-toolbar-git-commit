from django.conf import settings
from debug_toolbar.panels import DebugPanel

from subprocess import check_output, CalledProcessError

GIT_COMMIT_COUNT = getattr(settings, 'GIT_COMMIT_COUNT', 20)
GIT_COMMIT_FIELDS = ['id', 'author_name', 'author_email', 'date', 'message']
GIT_LOG_FORMAT = ['%h', '%an', '%ae', '%cd', '%s']
GIT_LOG_FORMAT = '%x1f'.join(GIT_LOG_FORMAT) + '%x1e'

try:
    log = check_output(["git", "log", "-%i" % GIT_COMMIT_COUNT, "--format=%s" % GIT_LOG_FORMAT]).strip("\"\n")
    log = log.strip('\n\x1e').split("\x1e")
    log = [row.strip().split("\x1f") for row in log]
    GIT_LOG = [dict(zip(GIT_COMMIT_FIELDS, row)) for row in log]
except CalledProcessError, e:
    GIT_LOG = []

class GitCommitStatus(DebugPanel):
    """
    Panel that displays the latest commit date
    """
    name = "Last Commit"
    has_content = True
    template = 'panels/debug_toolbar_git_commit.html'
    
    def nav_title(self):
        return "Last Commit"
    
    def nav_subtitle(self):
        if GIT_LOG:
            return GIT_LOG[0]['id'] + '\n' + GIT_LOG[0]['author_name']
        return ""
    
    def url(self):
        return ''
    
    def title(self):
        return "Recent Commits"
    
    def process_response(self, request, response):
        self.record_stats({
            'log': GIT_LOG,
            'commit_url': getattr(settings, 'GIT_COMMIT_URL', False)
        })
