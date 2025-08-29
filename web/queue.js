/**/

import { app } from "../../scripts/app.js";

const _id1 = "Dynamic Combo (JOV_WIDGET)";

app.registerExtension({
	name: 'jovi_widget.node.' + _id1,
	async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name != _id1) {
            return;
        }

        const onNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = async function () {
            const me = await onNodeCreated?.apply(this, arguments);

            const widget_string = this.widgets.find(w => w.name == 'string');
            const widget_select = this.widgets.find(w => w.name == 'select');
            widget_string.callback = () => {
                widget_select.options.values = widget_string.value
                    .split(/\r?\n/)
                    .filter(line => line.trim() !== "");

                if (!widget_select.options.values.includes(widget_select.value)) {
                    widget_select.value = null;
                }
            }

            setTimeout(() => { widget_string.callback(); }, 5);
            return me;
        }
    }
})
