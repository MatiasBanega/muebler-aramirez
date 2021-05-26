from odoo import models, fields, api


class itl_sale_referrer_id(models.Model):
     _inherit = 'sale.order'
        
     referrer_id = fields.Text('Referred ID')
     commission_plan_id = fields.Text('Commission plan id')
     commission = fields.Text('Commission')
    
   # _inherit = 'sale.subscription'
    #referrer_id = fields.Integer('referrer id')
    
class SaleOrder(models.Model):
     _name = "res.partner"
     _inherit = 'res.partner'
     commission_plan_id = fields.Text('Plan ID')
        
class SaleOrder(models.Model):
     _name = "purchase.order"
     _inherit = 'purchase.order'
     invoice_commission_count = fields.Integer('Commission count')
        
class SaleOrder(models.Model):
     _name = "account.move"
     _inherit = 'account.move'
     referrer_id = fields.Integer('referrer id')
    
class SaleOrder(models.Model):
     _inherit = "sale.subscription"
     referrer_id = fields.Integer('referrer id')
     commission_plan_assignation = fields.Integer('commission plan assignation')
     commission_plan_id = fields.Integer('commission plan id')
     commission = fields.Integer('commission')
  #   referrer_id = fields.Integer('referrer id')
    #_inherit = 'sale.res_partner'
    #commission_plan_id = fields.Text('Plan ID')