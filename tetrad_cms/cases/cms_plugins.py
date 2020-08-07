from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

# local
from .models import CasePluginModel

@plugin_pool.register_plugin
class CasePluginPublisher(CMSPluginBase):
    model = CasePluginModel
    module = _("Cases")
    name = _("Case Plugin")
    render_template = 'cases/case_plugin.html'

    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context
