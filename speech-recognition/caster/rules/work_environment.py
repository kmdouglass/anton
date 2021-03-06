from dragonfly import Choice, MappingRule

from castervoice.lib.actions import Text
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails


class WorkEnvironment(MappingRule):
    mapping = {
        "gee see pee": Text("GCP"),
        "otto gee see pee": Text("AutoGCP"),
        "web gist [<size>]": Text("%(size)s"),
    }

    extras = [
        Choice(
            "size",
            {
                "small": "webgis",
                "large": "WEBGIS",
            }
        ),
    ]

    defaults = {"size": "WEBGIS"}


def get_rule():
    return WorkEnvironment, RuleDetails(name="work envy")
