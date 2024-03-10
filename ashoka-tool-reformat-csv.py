import pandas as pd

def convert_edict(info_source, info_num, info_place, sentence_number, sentence_text):
    return_string = """%s, %s, %s, %s, %s""" % (info_source, info_num, info_place, sentence_number, sentence_text)
    return return_string

df = pd.read_csv("ashoka_foreign_relations.csv")
df.dropna(axis=1, how="all")

csv_string = """source, num, place, sentence_number, sentence""" + "\n"

for index, row in df.iterrows():
    for index_column in range(1, 28):
        index_string = str(index_column)
        if not pd.isna(row[index_string]):
            csv_string += convert_edict(row["source"], row["num"], row["place"], index_string, row[index_string]) + "\n"
            
with open("ashoka_edicts_foreign_relations_by_sentence.csv", "w") as text_file:
    text_file.write(csv_string)