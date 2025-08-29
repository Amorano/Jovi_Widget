""" Jovi_Widget"""

from cozy_comfyui import \
    logger, \
    deep_merge, parse_param

from cozy_comfyui.lexicon import \
    Lexicon

from cozy_comfyui.node import \
    CozyBaseNode

# ==============================================================================
# === CLASS ===
# ==============================================================================

class ComboDynamicNode(CozyBaseNode):
    NAME = "Dynamic Combo"
    SORT = 20
    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("OUTPUT", )
    OUTPUT_TOOLTIPS = (
        "Value selected from combo dropdown",
    )
    DESCRIPTION = """
Custom user combo options.
"""

    @classmethod
    def INPUT_TYPES(cls) -> dict:
        d = super().INPUT_TYPES()
        d = deep_merge(d, {
            "optional": {
                Lexicon.SELECT: ([""], {
                    "default": "",
                    "tooltip": "Custom user options, separated per line"}),
                Lexicon.STRING: ("STRING", {
                    "default": "",
                    "multiline": True,
                    "dynamicPrompts": False,
                    "tooltip": "Custom user options, separated per line"}),
            }
        })
        return Lexicon._parse(d)

    def run(self, **kw) -> tuple[str]:
        select = kw[Lexicon.SELECT][0]
        return (select,)
