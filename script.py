import pandas
import numpy
import os
import collections
import sys
import codecs
import jinja2
import copy


dir_path=os.path.dirname(os.path.abspath(__file__))
filename = dir_path + "\\Resultats.xlsx"

content_xlsx = pandas.ExcelFile(filename)

fsloader = jinja2.FileSystemLoader(dir_path) #dossier ou se trouve les template
env = jinja2.Environment(loader=fsloader)


###Coureurs

listeCoureurs = []
listeCoureurs.append(["Alain L.","AlainL","Pass' D1"])
listeCoureurs.append(["Alexis B.","AlexisB","Pass' D1"])
listeCoureurs.append(["Alexis W.","AlexisW","Junior"])
listeCoureurs.append(["Antoine M.","AntoineM","3e caté"])
listeCoureurs.append(["Antony W.","AnthonyW","Junior"])
listeCoureurs.append(["Arnaud S.","ArnaudS","2e caté"])
listeCoureurs.append(["Baptiste S.","BaptisteS","Pass' D1"])
#listeCoureurs.append(["Boris S.","BorisS","VTT - Enduro"])
listeCoureurs.append(["Cédric L.","CedricL","3e caté"])
listeCoureurs.append(["Cédric M.","CedricM","S4 (FSGT)"])
listeCoureurs.append(["Christophe D.","ChristopheD","Pass' D1"])
listeCoureurs.append(["Claude K.","ClaudeK","V4 (FSGT)"])
listeCoureurs.append(["Claude S.","ClaudeS","Pass' D3"])
listeCoureurs.append(["Daniel F","DanielF","3e caté"])
listeCoureurs.append(["Emile C.","EmileC","2e caté"])
listeCoureurs.append(["Eric H.","EricH","3e caté"])
listeCoureurs.append(["Florian K.","FlorianK","3e caté"])
listeCoureurs.append(["Florian V.","FlorianV","Pass' D1"])
listeCoureurs.append(["Gilles E.", "GillesE","Pass' D4"])
listeCoureurs.append(["Grégory W.","GregoryW","S3 (FSGT)"])
listeCoureurs.append(["Guillaume A.","GuillaumeA","Pass' D1"])
listeCoureurs.append(["Guillaume P.","GuillaumeP","Pass' D1"])
listeCoureurs.append(["Jérôme H.","JeromeH","Junior"])
listeCoureurs.append(["Johann V.","JohannV","Junior"])
listeCoureurs.append(["José L.","JoseL","3e caté"])
listeCoureurs.append(["Julien B.","JulienB","3e caté"])
listeCoureurs.append(["Julien G.","JulienG","2e caté"])

listeCoureurs.append(["Kévin E.","KevinE","3e caté"])
listeCoureurs.append(["Lionel B.","LionelB","Pass' D3"])
listeCoureurs.append(["Lucas B.","LucasB","2e caté"])
listeCoureurs.append(["Lucien H.","LucienH","S4 (FSGT)"])
listeCoureurs.append(["Ludovic K.","LudovicK","3e caté"])
listeCoureurs.append(["Maurice C.","MauriceC","Pass' D4"])
listeCoureurs.append(["Pascal S.","PascalS","Pass' D3"])
listeCoureurs.append(["Patrick V.","PatrickV","Pass' D4"])
listeCoureurs.append(["Philippe W.","PhilippeW","Pass' D1"])
listeCoureurs.append(["René S.","ReneS","Pass' D3"])
listeCoureurs.append(["Santo F.","SantoF","3e caté"])
listeCoureurs.append(["Sébastien S.","SebastienS","Pass' D3"])
listeCoureurs.append(["Sylvie R.","SylvieR","Fem (FSGT)"])
listeCoureurs.append(["Sönke W.","SonkeW","Senior (FSGT)"])
listeCoureurs.append(["Stéphane M.","StephaneM","V4 (FSGT)"])
listeCoureurs.append(["Thomas L.","ThomasL","S4 (FSGT)"])
listeCoureurs.append(["Wessel vH.","WesselvH","VTT DH"])


listeCoureurs.append(["Alexandre N.","AlexandreN","Cadet"])
listeCoureurs.append(["Antoine C.","AntoineC","Minime"])
listeCoureurs.append(["Clément B.","ClementB","Cadet"])
listeCoureurs.append(["Mathias G.","MathiasG","Minime"])
listeCoureurs.append(["Noah P.","NoahP","Minime"])
'''longueurmax= max([len(coureurs[0]) for coureurs in listeCoureurs])
for i in listeCoureurs:
    espaceacombler = longueurmax - len(i[0])
    for nbespaces in range(espaceacombler//2):
        i[0]="&nbsp; "+i[0]
        i[0] +="&nbsp; "
    if espaceacombler%2==1:
        i[0]+="&nbsp; " '''

listeCoureurs.append(["Hugo Hofstetter","HugoH","Coureur professionnel - Team Cofidis"])

coureursDerniereLigne= len(listeCoureurs)%4

### Tableau resultats

list_cates=['FFC123J','FFC23J','FFC3J','FFCPassD1','FFCPassD3','FSGT23','FSGTS4','FSGTV4','FSGTCad','FSGTMin']

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


    ###2017

data = content_xlsx.parse("Resultats2017")

victoires = data[(data.Place == 1)].shape[0]
top3 = data[(data.Place <= 3)].shape[0]
top10 = data[(data.Place <= 10)].shape[0]

victoires_fsgt = data[(data.Place == 1) & (data.Fédération == 'FSGT')].shape[0]
top3_fsgt = data[(data.Place <= 3) & (data.Fédération == 'FSGT')].shape[0]
top10_fsgt = data[(data.Place <= 10) & (data.Fédération == 'FSGT')].shape[0]

victoires_ffc = data[(data.Place == 1) & (data.Fédération == 'FFC')].shape[0]
top3_ffc = data[(data.Place <= 3) & (data.Fédération == 'FFC')].shape[0]
top10_ffc = data[(data.Place <= 10) & (data.Fédération == 'FFC')].shape[0]

bilan = [victoires,victoires_fsgt,victoires_ffc,top3,top3_fsgt,top3_ffc,top10, top10_fsgt, top10_ffc]


resultats = collections.OrderedDict()
for cate in list_cates:
    resultats[cate]=[0 for i in range(10)]

#print(resultats)
for numligne in range(len(data)):
    if data.iloc[numligne]['Type']== 'Route':
        cate_nom_ligne = data.iloc[numligne]['Fédération'] + str(data.iloc[numligne]['Catégorie'])
        resultats[cate_nom_ligne][data.iloc[numligne]['Place']-1]+=1

#for perf in Places: #if fsgt or ffc ?
#    resultats[perf[1]+perf[2]][perf[0]-1]+=1   # resultats [FEDEcates] [place-1 à cause de l'indexation] += 1

#print(resultats)

resultats['Total'] = [sum(resultats[cates][place] for cates in list_cates) for place in range(10)]

resultats2017 = copy.deepcopy(resultats)

   ###2018

data = content_xlsx.parse("Resultats2018")

victoires = data[(data.Place == 1)].shape[0]
top3 = data[(data.Place <= 3)].shape[0]
top10 = data[(data.Place <= 10)].shape[0]

victoires_fsgt = data[(data.Place == 1) & (data.Fédération == 'FSGT')].shape[0]
top3_fsgt = data[(data.Place <= 3) & (data.Fédération == 'FSGT')].shape[0]
top10_fsgt = data[(data.Place <= 10) & (data.Fédération == 'FSGT')].shape[0]

victoires_ffc = data[(data.Place == 1) & (data.Fédération == 'FFC')].shape[0]
top3_ffc = data[(data.Place <= 3) & (data.Fédération == 'FFC')].shape[0]
top10_ffc = data[(data.Place <= 10) & (data.Fédération == 'FFC')].shape[0]

bilan2018 = [victoires,victoires_fsgt,victoires_ffc,top3,top3_fsgt,top3_ffc,top10, top10_fsgt, top10_ffc]


resultats = collections.OrderedDict()
for cate in list_cates:
    resultats[cate]=[0 for i in range(10)]

#print(resultats)
for numligne in range(len(data)):
    if data.iloc[numligne]['Type']== 'Route':
        cate_nom_ligne = data.iloc[numligne]['Fédération'] + str(data.iloc[numligne]['Catégorie'])
        resultats[cate_nom_ligne][data.iloc[numligne]['Place']-1]+=1

#for perf in Places: #if fsgt or ffc ?
#    resultats[perf[1]+perf[2]][perf[0]-1]+=1   # resultats [FEDEcates] [place-1 à cause de l'indexation] += 1

#print(resultats)

resultats['Total'] = [sum(resultats[cates][place] for cates in list_cates) for place in range(10)]

resultats2018 = copy.deepcopy(resultats)


index=True
template = env.get_template('index.html.j2') #nomdutemplate
ofh = codecs.open("index.html","w", encoding="utf-8")
rt = template.render(bilan=bilan, bilan2018 = bilan2018, index=index)
ofh.write(rt)
ofh.close()

index=False
template = env.get_template('performances.html.j2') #nomdutemplate
ofh = codecs.open("performances.html","w", encoding="utf-8")
rt = template.render(resultats2018=resultats2018, resultats2017 = resultats2017, bilan=bilan,affichage=affichage, index=index, bilan2018 = bilan2018)
ofh.write(rt)
ofh.close()

template = env.get_template('nousRejoindre.html.j2') #nomdutemplate
ofh = codecs.open("nousRejoindre.html","w", encoding="utf-8")
rt = template.render(bilan=bilan, index=index, bilan2018 = bilan2018)
ofh.write(rt)
ofh.close()

template = env.get_template('entrainements.html.j2') #nomdutemplate
ofh = codecs.open("entrainements.html","w", encoding="utf-8")
rt = template.render(bilan=bilan, index=index, bilan2018 = bilan2018)
ofh.write(rt)
ofh.close()

template = env.get_template('effectif.html.j2') #nomdutemplate
ofh = codecs.open("effectif.html","w", encoding="utf-8")
rt = template.render(bilan=bilan, listeCoureurs=listeCoureurs, len = len, index=index, bilan2018 = bilan2018)
ofh.write(rt)
ofh.close()

template = env.get_template('contact.html.j2') #nomdutemplate
ofh = codecs.open("contact.html","w", encoding="utf-8")
rt = template.render(bilan=bilan, index=index, bilan2018 = bilan2018)
ofh.write(rt)
ofh.close()

template = env.get_template('leclub.html.j2') #nomdutemplate
ofh = codecs.open("leClub.html","w", encoding="utf-8")
rt = template.render(bilan=bilan, index=index, bilan2018 = bilan2018)
ofh.write(rt)
ofh.close()

template = env.get_template('archives.html.j2') #nomdutemplate
ofh = codecs.open("archives.html","w", encoding="utf-8")
rt = template.render(bilan=bilan, index=index, bilan2018 = bilan2018)
ofh.write(rt)
ofh.close()

template = env.get_template('partenaires.html.j2') #nomdutemplate
ofh = codecs.open("partenaires.html","w", encoding="utf-8")
rt = template.render(bilan=bilan, index=index, bilan2018 = bilan2018)
ofh.write(rt)
ofh.close()

#template = env.get_template('organisations.html.j2') #nomdutemplate
#ofh = codecs.open("organisations.html","w", encoding="utf-8")
#rt = template.render(bilan=bilan, index=index, bilan2018 = bilan2018)
#ofh.write(rt)
#ofh.close()

template = env.get_template('3h-vtt.html.j2') #nomdutemplate
ofh = codecs.open("3h-vtt.html","w", encoding="utf-8")
rt = template.render(index=index)
ofh.write(rt)
ofh.close()

template = env.get_template('jettingen.html.j2') #nomdutemplate
ofh = codecs.open("jettingen.html","w", encoding="utf-8")
rt = template.render(index=index)
ofh.write(rt)
ofh.close()

template = env.get_template('saint-bernard.html.j2') #nomdutemplate
ofh = codecs.open("saint-bernard.html","w", encoding="utf-8")
rt = template.render(index=index)
ofh.write(rt)
ofh.close()

template = env.get_template('seppois.html.j2') #nomdutemplate
ofh = codecs.open("seppois.html","w", encoding="utf-8")
rt = template.render(index=index)
ofh.write(rt)
ofh.close()
