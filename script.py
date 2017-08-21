
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
Places.append([9,'FSGT','V4','Rene  S'])
Places.append([6,'FSGT','V4','Rene  S'])
Places.append([1,'FSGT','V4','Rene  S'])
Places.append([1,'FSGT','V4','Rene  S'])
Places.append([2,'FSGT','V4','Rene  S'])
Places.append([7,'FSGT','V4','Rene  S'])

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

Places.append([6,'FFC','PassD1','FlorianK Monaco'])

Places.append([5,'FSGT','23','FlorianK Plascassier 06'])
Places.append([1,'FSGT','23','FlorianK Sophia 06'])
Places.append([4,'FSGT','23','FlorianK Martyrs 06'])
Places.append([2,'FSGT','23','FlorianK Souvenir morra 06'])


Places.append([10,'FFC','23J','FlorianK clm piemont'])
Places.append([8,'FFC','23J','FlorianK Gerardmer'])

Places.append([10,'FFC','123J','Jerome H Steige'])

Places.append([1,'FFC','PassD1','Antoine M Buhl'])
Places.append([9,'FFC','PassD1','Jerome J Buhl'])

Places.append([6,'FFC','3J','Julien G Wintershouse'])
Places.append([8,'FFC','PassD3','Claude S Muguet'])
Places.append([10,'FFC','PassD3','Gilles E Muguet'])

Places.append([2,'FFC','3J','Julien G Wintershouse'])

Places.append([5,'FFC','23J','Daniel F Sentheim'])
Places.append([1,'FFC','PassD1','Philippe W Sentheim'])
Places.append([2,'FFC','3J','Daniel F Merkwiller'])

Places.append([1,'FFC','PassD3','Rene S Schwenheim'])
Places.append([8,'FFC','PassD3','Claude S Schwenheim'])

Places.append([4,'FFC','PassD1','Kevin E Ornans'])
Places.append([6,'FFC','PassD1','Kevin E Valdahon'])
Places.append([4,'FFC','PassD1','Kevin E Pontarlier']) 
Places.append([2,'FFC','PassD1','Kevin E Terre de Chaux'])
Places.append([2,'FFC','PassD1','Kevin E Morteaux'])
Places.append([2,'FFC','PassD1','Kevin E Noroy le bourg'])
Places.append([4,'FFC','PassD1','Kevin E Saint Remy'])

Places.append([1,'FFC','3J','Florian K Montgeron'])

Places.append([8,'FFC','PassD1','Jerome J Charmont'])
Places.append([10,'FFC','PassD1','Brieuc H Amancey'])

Places.append([6,'FFC','3J','Jerome H crit printemps'])

Places.append([10,'FFC','3J','Julien G TTB 1'])
Places.append([4,'FFC','3J','Julien G TTB  TTT'])
Places.append([3,'FFC','3J','Julien G TTB 1'])
Places.append([2,'FFC','3J','Julien G TTB general'])

Places.append([5,'FFC','23J','Julien G Saone Vingeanne'])

Places.append([9,'FFC','PassD1','Brieuc H ballon '])

Places.append([10,'FFC','23J','Julien B repes'])

Places.append([5,'FFC','23J','Jerome H Ronde Haute Saone 1'])

listeCoureurs = []
listeCoureurs.append(["Alain L.","AlainL","Pass' D1"])
listeCoureurs.append(["Alexis W.","AlexisW","J3 (FSGT)"])
listeCoureurs.append(["Antoine M.","AntoineM","3e caté"])
listeCoureurs.append(["Baptiste S.","BaptisteS","Pass' D1"])
listeCoureurs.append(["Brieuc H.","BrieucH","Pass' D1"])
listeCoureurs.append(["Cédric L.","CedricL","3e caté"])
listeCoureurs.append(["Cédric M.","CedricM","S4 (FSGT)"])
listeCoureurs.append(["Christophe D.","ChristopheD","3ème caté"])
listeCoureurs.append(["Claude S.","ClaudeS","Pass' D3"])
listeCoureurs.append(["Daniel F","DanielF","3e caté"])
listeCoureurs.append(["Eric H.","EricH","3e caté"])
listeCoureurs.append(["Florian K.","FlorianK","3 caté"])
listeCoureurs.append(["Florian V.","FlorianV","Pass' D1"])
listeCoureurs.append(["Gilles E.", "GillesE","Pass' D4"])
listeCoureurs.append(["Guillaume A.","GuillaumeA","Pass' D1"])
listeCoureurs.append(["Guillaume P.","GuillaumeP","Pass' D1"])
listeCoureurs.append(["Jérôme H.","JeromeH","Junior"])
listeCoureurs.append(["Jérôme J.","JeromeJ","Pass' D1"])
listeCoureurs.append(["José L.","JoseL","3e caté"])
listeCoureurs.append(["Julien B.","JulienB","3e caté"])
listeCoureurs.append(["Julien G.","JulienG","3e caté"])

listeCoureurs.append(["Kévin E.","KevinE","3e caté"])
listeCoureurs.append(["Lionel B.","LionelB","Pass' D3"])
listeCoureurs.append(["Lucien H.","LucienH","S4 (FSGT)"])
listeCoureurs.append(["Ludovic K.","LudovicK","2e caté"])
listeCoureurs.append(["Mathieu N.","MathieuN","3e caté"])
listeCoureurs.append(["Pascal S.","PascalS","Pass' D1"])
listeCoureurs.append(["Patrick V.","PatrickV","Pass' D4"])
listeCoureurs.append(["Philippe W.","PhilippeW","3e caté"])
listeCoureurs.append(["René S.","ReneS","Pass' D2"])
listeCoureurs.append(["Santo F.","SantoF","3ème caté"])
listeCoureurs.append(["Sébastien S","SebastienS","Pass' D3"])
listeCoureurs.append(["Stéphane M.","StephaneM","V4 (FSGT)"])
listeCoureurs.append(["Sönke W.","SonkeW","Senior (FSGT)"])
listeCoureurs.append(["Lionel B.","LionelB","Pass' D3"])

listeCoureurs.append(["Johann V.","JohannV","Cadet"])
listeCoureurs.append(["Alexandre N.","AlexandreN","Minime"])
listeCoureurs.append(["Anthony W.","AnthonyW","Cadet"])
listeCoureurs.append(["Antoine C.","AntoineC","Minime"])
listeCoureurs.append(["Clément B.","ClementB","Cadet"])

listeCoureurs.append(["Hugo Hofstetter","HugoH","Coureur professionnel - Team Cofidis"])

coureursDerniereLigne= len(listeCoureurs)%4

 


list_cates=['FFC123J','FFC23J','FFC3J','FFCPassD1','FFCPassD3','FSGT23','FSGTS4','FSGTV4','FSGTCad','FSGTMin']


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
for perf in Places: #if fsgt or ffc ?
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
rt = template.render(bilan=bilan, listeCoureurs=listeCoureurs, len = len)
ofh.write(rt)
ofh.close()

template = env.get_template('contact.jj') #nomdutemplate
ofh = codecs.open(r"C:\Users\Florian\Documents\VCS-Altkirch\\contact.html","w", encoding="utf-8")
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

