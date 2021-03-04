from odoo import fields, models, api

class Skin(models.Model):
    _name = 'csskins.skin'

    id = fields.Char('Skin ID', required=True)
    name = fields.Char('Skin name', required=True)
    weapon = fields.Many2one('csskins.weapon', 'Weapon', required=True)
    price = fields.Float('Skin price', required=True)
    stattrack = fields.Boolean('Skin has StatTrack', required=True)
    sfloat = fields.Float('Skin float', required=True)

