/** @odoo-module **/

import Dialog from '@web/legacy/js/core/dialog';
import { markup } from "@odoo/owl";

export default Dialog.extend({
    template: 'theme_prime.cart_confirmation_dialog',
    events: Object.assign({}, Dialog.prototype.events, {
        'dr_close_dialog': 'close',
        'click .tp-close': 'close',
        'click .s_d_product_small_block .card': '_onClickProduct'
    }),
    /**
     * @constructor
     */
    init: function (parent, options) {
        this.data = options.data;
        this.data.notification_info['order_amount_html'] = markup(this.data.notification_info.order_amount_html)
        if (this.data.accessory_product_ids.length) {
            this.data.accessory_product_ids_str = JSON.stringify(this.data.accessory_product_ids);
        }
        this._super(parent, Object.assign({}, { renderHeader: false, renderFooter: false, technical: false, size: options.size, backdrop: true }, options || {}));
    },
    /**
     * @override
     */
    start: function () {
        var sup = this._super.apply(this, arguments);
        this.$modal.find('.modal-dialog').addClass('modal-dialog-centered tp-custom-dialog d_cart_confirmation_dialog');
        this.trigger_up('widgets_start_request', {
            $target: this.$('.s_d_product_small_block'),
        });
        return sup;
    },

    // TODO: fix this hack
    _onClickProduct: function (ev) {
        window.location.href = $(ev.currentTarget).find('.d-product-name a')[0].href;
    },
});
