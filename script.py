
# -*- coding: utf-8 -*-

import codecs
import jinja2

fsloader = jinja2.FileSystemLoader(r'C:\Users\Florian\Documents\VCS-Altkirch') #dossier ou se trouve le template
env = jinja2.Environment(loader=fsloader)

template = env.get_template('index.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\index.html","w", encoding="utf-8")
rt = template.render()
ofh.write(rt)
ofh.close()

template = env.get_template('nousRejoindre.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\nousRejoindre.html","w", encoding="utf-8")
rt = template.render()
ofh.write(rt)
ofh.close()

template = env.get_template('circuits.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\circuits.html","w", encoding="utf-8")
rt = template.render()
ofh.write(rt)
ofh.close()

template = env.get_template('coureurs.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\coureurs.html","w", encoding="utf-8")
rt = template.render()
ofh.write(rt)
ofh.close()

template = env.get_template('leclub.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\leclub.html","w", encoding="utf-8")
rt = template.render()
ofh.write(rt)
ofh.close()

template = env.get_template('partenaires.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\partenaires.html","w", encoding="utf-8")
rt = template.render()
ofh.write(rt)
ofh.close()

template = env.get_template('resultats.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\resultats.html","w", encoding="utf-8")
rt = template.render()
ofh.write(rt)
ofh.close()

template = env.get_template('organisations.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\organisations.html","w", encoding="utf-8")
rt = template.render()
ofh.write(rt)
ofh.close()

