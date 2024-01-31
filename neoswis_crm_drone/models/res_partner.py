from odoo import fields, models, api


class Respartner(models.Model):
	_inherit = 'res.partner'


	emirates_id = fields.Integer(string="Emirates ID")
	passport_no = fields.Integer(string="Passport No")
	certificate_ids = fields.One2many('certificate.details', 'res_partner_id', string='Certificate Details')
	training_ids = fields.One2many('training.details', 'res_partner_id', string='Training Details')
	drone_ids = fields.One2many('registred.drones', 'res_partner_id', string='Drone Details')


class CertificatesType(models.Model):
	_name = 'certificate.type'
	_description = "Certificate Type"


	name = fields.Char(string='Certificate Type')

class TrainingType(models.Model):
	_name = 'training.type'
	_description = "Training Type"


	name = fields.Char(string='Training Type')


class CertificateDetails(models.Model):
	_name = 'certificate.details'
	_description = "Certificate Details"


	res_partner_id = fields.Many2one('res.partner',string="Certificate Details")
	description = fields.Char(string='Description')
	date = fields.Date(string='Date')
	expiry_date = fields.Date(string='Expiry Date')
	attachment_ids = fields.Many2many('ir.attachment', string='Attachments', help='Attach files here')
	certificate_type_id = fields.Many2one('certificate.type', string='Certificate type')


class Training(models.Model):
	_name = 'training.details'
	_description = "Training Details"


	res_partner_id = fields.Many2one('res.partner',string="Training Details")
	training_type_id = fields.Many2one('training.type', string='Training type')
	description = fields.Char(string='Description')
	date = fields.Date(string='Date')

class RegistredDrones(models.Model):
	_name = 'registred.drones'
	_description = "Drone Details"


	res_partner_id = fields.Many2one('res.partner',string="Drone Details")
	licence_no = fields.Integer(string='Licence No')
	date = fields.Date(string='Reg Date')
	expiry_date = fields.Date(string='Expiry Date')
	mfg_name = fields.Char(string='Mfg Name')
	model = fields.Char(string='Model')