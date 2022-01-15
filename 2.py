import csv
import time

country_name = "<http://www.kbqa.com/country_%03d> <http://www.kbqa.com/properties#country_name> \"%s\" ."

country_id ="<http://www.kbqa.com/country_%03d> <http://www.kbqa.com/properties#id> \"%s\""

total_confirm = "<http://www.kbqa.com/country_%03d> <http://www.kbqa.com/properties#total_confirm> \"%s\""

total_suspect = "<http://www.kbqa.com/country_%03d> <http://www.kbqa.com/properties#total_suspect> \"%s\""

total_heal = "<http://www.kbqa.com/country_%03d> <http://www.kbqa.com/properties#total_heal> \"%s\""

total_dead = "<http://www.kbqa.com/country_%03d> <http://www.kbqa.com/properties#total_dead> \"%s\""

total_severe = "<http://www.kbqa.com/country_%03d> <http://www.kbqa.com/properties#total_severe> \"%s\""

total_input = "<http://www.kbqa.com/country_%03d> <http://www.kbqa.com/properties#total_input> \"%s\""

today_confirm = "<http://www.kbqa.com/country_%03d> <http://www.kbqa.com/properties#today_confirm> \"%s\""

today_suspect = "<http://www.kbqa.com/country_%03d> <http://www.kbqa.com/properties#today_suspect> \"%s\""

today_heal = "<http://www.kbqa.com/country_%03d> <http://www.kbqa.com/properties#today_heal> \"%s\""

today_dead = "<http://www.kbqa.com/country_%03d> <http://www.kbqa.com/properties#today_dead> \"%s\""

today_severe = "<http://www.kbqa.com/country_%03d> <http://www.kbqa.com/properties#today_severe> \"%s\""

today_input = "<http://www.kbqa.com/country_%03d> <http://www.kbqa.com/properties#today_input> \"%s\""

triples = []

i = 0 #counter
f = open('today_world_2020_05_09.csv','r',encoding='UTF-8')
reader = csv.reader(f)
for row in reader:
    i = i + 1

    country_id_str = country_id % (i, row[0])
    triples.append(country_id_str + "^^<http://www.w3.org/2001/XMLSchema#integer> .")

    country_name_str = country_name % (i, row[1])
    triples.append(country_name_str)

    total_confirm_str = total_confirm % (i, row[2])
    triples.append(total_confirm_str + "^^<http://www.w3.org/2001/XMLSchema#integer> .")

    total_suspect_str = total_suspect % (i, row[3])
    triples.append(total_suspect_str + "^^<http://www.w3.org/2001/XMLSchema#integer> .")

    total_heal_str = total_heal % (i, row[4])
    triples.append(total_heal_str + "^^<http://www.w3.org/2001/XMLSchema#integer> .")

    total_dead_str = total_dead % (i, row[5])
    triples.append(total_dead_str + "^^<http://www.w3.org/2001/XMLSchema#integer> .")

    total_severe_str = total_severe % (i, row[6])
    triples.append(total_severe_str + "^^<http://www.w3.org/2001/XMLSchema#integer> .")

    total_input_str = total_input % (i, row[7])
    triples.append(total_input_str + "^^<http://www.w3.org/2001/XMLSchema#integer> .")

    today_confirm_str = today_confirm % (i, row[8])
    triples.append(today_confirm_str + "^^<http://www.w3.org/2001/XMLSchema#integer> .")

    today_suspect_str = today_suspect % (i, row[9])
    triples.append(today_suspect_str + "^^<http://www.w3.org/2001/XMLSchema#integer> .")

    today_heal_str = today_heal % (i, row[10])
    triples.append(today_heal_str + "^^<http://www.w3.org/2001/XMLSchema#integer> .")

    today_dead_str = today_dead % (i, row[11])
    triples.append(today_dead_str + "^^<http://www.w3.org/2001/XMLSchema#integer> .")

    today_severe_str = today_severe % (i, row[12])
    triples.append(today_severe_str + "^^<http://www.w3.org/2001/XMLSchema#integer> .")

    today_input_str = today_input % (i, row[13])
    triples.append(today_input_str + "^^<http://www.w3.org/2001/XMLSchema#integer> .")

file_name = 'today_world' + '_' + time.strftime('%Y_%m_%d', time.localtime(time.time())) + '.nt'
with open(file_name, "w+", encoding='utf-8') as fd:
    fd.write(("\n".join(triples)))
fd.close()
