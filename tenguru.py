import jinja2
import pdfkit
import yaml
import os

def init():
	# PDFKit
	wkhtmltopdf_path = '/usr/local/bin/wkhtmltopdf'
	pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
	
	# Jinja2
	templateLoader = jinja2.FileSystemLoader(searchpath="./")
	return jinja2.Environment(loader=templateLoader)



def populate_template(templateEnv, template_name, template_lang, data, logo):
	template_file = os.path.join('templates', template_name,template_lang+'.html' )
	template = templateEnv.get_template(template_file)
	cwd = os.getcwd()
	html = str(template.render(data))
	html=html.replace('href="','href="{0}/templates/{1}/'.format(cwd, template_name))
	html=html.replace('src="','src="{0}/custom/{1}'.format(cwd, logo))

	return html


def convert_html_to_pdf(html_as_string, pdf_filename):
	options = {
	  "enable-local-file-access": None,
	  'page-size':'A4', 
	  'dpi':400
	}
	pdfkit.from_string(html_as_string, pdf_filename, options=options)



def load_config(custom):

	config_file = os.path.join('custom',custom,'config.yaml')
	with open(config_file) as file:
		# The FullLoader parameter handles the conversion from YAML
		# scalar values to Python the dictionary format
		config = yaml.load(file, Loader=yaml.FullLoader)

	return config


def run(template_name, template_lang, data, logo):
	templateEnv = init()
	html_as_string = populate_template(templateEnv, template_name, template_lang, data, logo)
	pdf_filename = 'out.pdf'
	convert_html_to_pdf(html_as_string, pdf_filename)




if __name__ == '__main__':	
	data={'creator_company':'Mark',
		'telephone':'0904389230525',
		'email':'wegew@fggsgger.com',
		'number':'00932',
		'address':'ioewoig, wioe g, weigjhwrg gw32, weoijfew fewf(LT)',
		'date':'01-01-2021',
		'partner_company_name':'WeSell',
		'partner_carrier_name':'Ciccio'
	}
	custom = 'x'
	run('default', 'it', data, custom+'/logo.png')


