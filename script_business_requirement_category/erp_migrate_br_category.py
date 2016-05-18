import erppeek
import conf

server = conf.server
db = conf.db
user = conf.user
password = conf.password

br_model = conf.br_model
project_categ_model = conf.project_categ_model
br_categ_model = conf.br_categ_model

client = erppeek.Client(server, db, user, password)
br_obj = client.model(br_model)
pc_obj = client.model(project_categ_model)
brc_obj = client.model(br_categ_model)

br_b = br_obj.browse([])
pc_b = pc_obj.browse([])

for pc in pc_b:
    categ_dict = pc.read()
    br_categ = {
        'id': categ_dict['id'],
        'name': categ_dict['name']
    }
    brc_obj.create(br_categ)

for br in br_b:
    br_categs = [(6, None, [categ.id for categ in br.categ_id])]
    br.write({'business_requirement_categ_id': br_categs})
