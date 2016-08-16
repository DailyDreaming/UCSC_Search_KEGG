from Bio.KEGG import REST

list_o_organisms = REST.kegg_list("organism").read()

# Filter all organism names for prokaryotes
all_prokaryotic_nicknames = []
for line in list_o_organisms.rstrip().split("\n"):
    entry, nickname, species, clades = line.split("\t")
    if "Prokaryotes" in clades:
        all_prokaryotic_nicknames.append(nickname)

#organism_pathways = REST.kegg_list("pathway", "rmr").read()
#print(organism_pathways)

for anickname in all_prokaryotic_nicknames:
    organism_pathways = REST.kegg_list("pathway", anickname).read()

    for line in organism_pathways.rstrip().split("\n"):
	path, propername = line.split("\t")
	pathway = REST.kegg_get(path).read()

#pathway_file = REST.kegg_get("path:rmr02030").read()
#print(pathway_file)
