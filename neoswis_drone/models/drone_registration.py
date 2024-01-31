from odoo import fields, models, api


class Drone(models.Model):
	_name = 'drone.registration'
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_description = 'Drone Registration'
	_order = 'id desc'


	licence_no = fields.Char(string="Licence No", track_visibility='always', required=True)
	registration_date = fields.Date(string="Registration Date", track_visibility='always', required=True)
	expiry_date = fields.Date(string="Expiry Date", track_visibility='always')
	mfg_name = fields.Char(string="Mfg Name", track_visibility='always')
	model_no = fields.Char(string="Model No", track_visibility='always')
	country_id = fields.Many2one('res.country', string="Country Name", track_visibility='always')
	customer_id = fields.Many2one('res.partner', string="Customer Name", track_visibility='always', required=True)
	attachment_ids = fields.Many2many('ir.attachment', string='Attachments', help='Attach files here')

