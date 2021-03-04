from odoo import fields, models, api

class Weapon(models.Model):
    _name = 'csskins.weapon'

    id = fields.Char('Weapon ID', required=True)
    name = fields.Char('Weapon name', required=True)
    skins = fields.One2many('csskins.skin', 'Skins', required=True)
    wtype = fields.Char('Weapon type', required=True)

