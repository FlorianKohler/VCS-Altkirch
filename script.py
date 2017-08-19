
# -*- coding: utf-8 -*-

import codecs
import jinja2
import collections

fsloader = jinja2.FileSystemLoader(r'C:\Users\Florian\Documents\VCS-Altkirch') #dossier ou se trouve le template
env = jinja2.Environment(loader=fsloader)

Places=[]
#ajout sous la forme [place, 'FSGT' ou 'FFC', '2-3' ou'S4' ou V4' ou 'Min' ou 'Cad' ou bien '123J','23J','3J', 'PassD1','PassD3','Min','Cad' , ' commentaire (nom et course ou date']
Places.append([10,'FSGT','23','Mathieu Nachbaur 26-03'])
Places.append([8,'FSGT','23','Mathieu Nachbaur 02-04'])
Places.append([6,'FSGT','23','Mathieu Nachbaur 08-05'])
Places.append([9,'FSGT','23','Mathieu Nachbaur 14-05'])
Places.append([5,'FSGT','23','Mathieu Nachbaur 27-05'])
Places.append([2,'FSGT','23','Mathieu Nachbaur 25-06'])
Places.append([5,'FSGT','S4','santo'])
Places.append([2,'FSGT','S4','Santo'])
Places.append([1,'FSGT','S4','Santo'])
Places.append([1,'FSGT','S4','Santo'])
Places.append([1,'FSGT','23','Julien G Montreux'])
Places.append([2,'FSGT','23','Julien G Frotey'])

Places.append([10,'FSGT','23','Julien B Frotey'])
Places.append([4,'FSGT','23','Julien B 04-06'])
Places.append([2,'FSGT','S4','Cedric L'])
Places.append([2,'FSGT','S4','Cedric L'])
Places.append([1,'FSGT','S4','Cedric L'])
Places.append([2,'FSGT','23','Eric H 02-04'])
Places.append([3,'FSGT','23','sonke '])

Places.append([4,'FSGT','S4','Antoine'])
Places.append([6,'FSGT','S4','Antoine'])
Places.append([3,'FSGT','S4','Antoine'])
Places.append([6,'FSGT','S4','Antoine'])

Places.append([9,'FSGT','S4','Lucien'])
Places.append([2,'FSGT','S4','Lucien'])
Places.append([4,'FSGT','S4','Lucien'])
Places.append([2,'FSGT','S4','Lucien'])

Places.append([1,'FSGT','23','Jerome H Seppois'])

Places.append([10,'FSGT','S4','Brieuc'])
Places.append([10,'FSGT','S4','Brieuc'])

Places.append([7,'FSGT','23','Jose L'])

Places.append([5,'FSGT','V4','Jerome J'])
Places.append([8,'FSGT','V4','Jerome J'])
Places.append([2,'FSGT','V4','Jerome J'])
Places.append([4,'FSGT','V4','Jerome J'])

Places.append([8,'FSGT','V4','Claude S'])
Places.append([3,'FSGT','V4','Claude S'])
Places.append([2,'FSGT','V4','Claude S'])
Places.append([9,'FSGT','V4','Claude S'])
Places.append([6,'FSGT','V4','Claude S'])

Places.append([7,'FSGT','V4','Stephane M'])
Places.append([7,'FSGT','V4','Stephane M'])
Places.append([7,'FSGT','V4','Stephane M'])

Places.append([6,'FSGT','V4','Sebastien S'])
Places.append([4,'FSGT','V4','Sebastien S'])
Places.append([4,'FSGT','V4','Sebastien S'])

Places.append([5,'FSGT','V4','Lionel B'])

Places.append([8,'FSGT','V4','Rene S'])
Places.append([9,'FSGT','V4','Sebastien S'])
Places.append([10,'FSGT','V4','Sebastien S'])
Places.append([1,'FSGT','V4','Sebastien S'])
Places.append([1,'FSGT','V4','Sebastien S'])
Places.append([2,'FSGT','V4','Sebastien S'])
Places.append([7,'FSGT','V4','Sebastien S'])

Places.append([4,'FSGT','Cad','Johann V'])
Places.append([8,'FSGT','Cad','Johann V'])
Places.append([6,'FSGT','Cad','Johann V'])
Places.append([5,'FSGT','Cad','Johann V'])
Places.append([9,'FSGT','Cad','Johann V'])
Places.append([5,'FSGT','Cad','Johann V'])

Places.append([1,'FSGT','Cad','Anthony W'])
Places.append([2,'FSGT','Cad','Anthony W'])
Places.append([6,'FSGT','Cad','Anthony W'])
Places.append([2,'FSGT','Cad','Anthony W'])

Places.append([9,'FSGT','Cad','Clement B'])
Places.append([5,'FSGT','Cad','Clement B'])
Places.append([6,'FSGT','Cad','Clement B'])

Places.append([1,'FSGT','Min','Alexandre N'])
Places.append([1,'FSGT','Min','Alexandre N'])
Places.append([1,'FSGT','Min','Alexandre N'])
Places.append([6,'FSGT','Min','Alexandre N'])
Places.append([6,'FSGT','Min','Alexandre N'])
Places.append([3,'FSGT','Min','Alexandre N'])
Places.append([5,'FSGT','Min','Alexandre N'])
Places.append([4,'FSGT','Min','Alexandre N'])

Places.append([9,'FSGT','Min','Antoine C'])
Places.append([8,'FSGT','Min','Antoine C'])
Places.append([2,'FSGT','Min','Antoine C'])


top3_ffc=0
top10_fsgt=0
top10_ffc=0

list_cates=['FFC123J','FFC23J','FFC3J','FFCPassD1','FFCPassD3','FFCCad','FFCMin','FSGT23','FSGTS4','FSGTV4','FSGTCad','FSGTMin']


resultats = collections.OrderedDict()
for cate in list_cates:
    resultats[cate]=[0 for i in range(10)]

affichage = {}
affichage['FFC123J']='FFC : 1-2-3-J'
affichage['FFC23J']='FFC : 2-3-J'
affichage['FFC3J']='FFC : 3-J'
affichage['FFCPassD1']='FFC : Pass\' D1/D2'
affichage['FFCPassD3']='FFC : Pass\' D3/D4'
affichage['FFCCad']='FFC : Cadets'
affichage['FFCMin']='FFC : Minimes'
affichage['FSGT23']='FSGT : 2-3'
affichage['FSGTS4']='FSGT : Seniors 4'
affichage['FSGTV4']='FSGT : Vétérans 4'
affichage['FSGTCad']='FSGT : Cadets'
affichage['FSGTMin']='FSGT : Minimes'
affichage['Total']='Total'

#print(resultats)
for perf in Places:
#if fsgt or ffc ?
    resultats[perf[1]+perf[2]][perf[0]-1]+=1   # resultats [FEDEcates] [place-1 à cause de l'indexation] += 1
    
#print(resultats)

resultats['Total'] = [sum(resultats[cates][place] for cates in list_cates) for place in range(10)]



victoires_fsgt = sum (1 for i in Places if i[0]==1 and i[1]=='FSGT')
top3_fsgt = sum (1 for i in Places if i[0]<=3 and i[1]=='FSGT')
top10_fsgt  = sum (1 for i in Places if i[0]<=10 and i[1]=='FSGT')

victoires_ffc = sum (1 for i in Places if i[0]==1 and i[1]=='FFC')
top3_ffc = sum (1 for i in Places if i[0]<=3 and i[1]=='FFC')
top10_ffc  = sum (1 for i in Places if i[0]<=10 and i[1]=='FFC')

victoires= victoires_fsgt + victoires_ffc
top3=top3_fsgt+top3_ffc
top10=top10_fsgt+top10_ffc

bilan = [victoires,victoires_fsgt,victoires_ffc,top3,top3_fsgt,top3_ffc,top10, top10_fsgt, top10_ffc]


template = env.get_template('index.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\index.html","w", encoding="utf-8")
rt = template.render(bilan=bilan)
ofh.write(rt)
ofh.close()

template = env.get_template('performances.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\performances.html","w", encoding="utf-8")
rt = template.render(resultats=resultats, bilan=bilan,affichage=affichage)
ofh.write(rt)
ofh.close()

template = env.get_template('nousRejoindre.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\nousRejoindre.html","w", encoding="utf-8")
rt = template.render(bilan=bilan)
ofh.write(rt)
ofh.close()

template = env.get_template('circuits.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\circuits.html","w", encoding="utf-8")
rt = template.render(bilan=bilan)  
ofh.write(rt)
ofh.close()

template = env.get_template('coureurs.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\coureurs.html","w", encoding="utf-8")
rt = template.render(bilan=bilan)
ofh.write(rt)
ofh.close()

template = env.get_template('leclub.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\leclub.html","w", encoding="utf-8")
rt = template.render(bilan=bilan)
ofh.write(rt)
ofh.close()

template = env.get_template('partenaires.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\partenaires.html","w", encoding="utf-8")
rt = template.render(bilan=bilan)
ofh.write(rt)
ofh.close()

template = env.get_template('resultats.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\resultats.html","w", encoding="utf-8")
rt = template.render(bilan=bilan)
ofh.write(rt)
ofh.close()

template = env.get_template('organisations.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\organisations.html","w", encoding="utf-8")
rt = template.render(bilan=bilan)
ofh.write(rt)
ofh.close()

