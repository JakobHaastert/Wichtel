import pandas as pd
import random as rd
import pprint as walter_junior

df_previous_matchings = pd.read_csv("previous_rounds.csv")
df_this_years_contestants = pd.read_csv(
    "contestants.csv", header=None)[0].tolist()


def matches():
    illegal_matchings = get_illegal_matchings()
    typ = False
    matches = {}
    while not typ:
        alreadyMatched = []
        matches = {}
        for friend in df_this_years_contestants:
            random_mapping = get_random_mapping(
                friend, illegal_matchings[friend], alreadyMatched)
            if not random_mapping:
                print("Kagge nochmal")
                break
            matches[friend] = random_mapping
            alreadyMatched.append(random_mapping)
            if (len(alreadyMatched) == len(df_this_years_contestants)):
                typ = True
    return matches


def get_illegal_matchings():
    previous_matchings = {item: [] for item in df_this_years_contestants}
    for index, row in df_previous_matchings.iterrows():
        schenker = row.get("Schenker")
        if schenker in previous_matchings:
            previous_matchings[schenker] = [
                row.get("Beschenkter")] + previous_matchings[schenker]
    return previous_matchings


def get_random_mapping(friend, illegal_matchings, already_Matched):
    possible_matchings = list(set(df_this_years_contestants) -
                              {friend} - set(illegal_matchings) - set(already_Matched))
    if not possible_matchings:
        return False
    return rd.choice(possible_matchings)


print("Berechne Wichtelpartner...")
mmmatches = matches()
walter_junior.pprint(mmmatches)
return_df = pd.DataFrame.from_dict(mmmatches, orient='index')
return_df.to_csv('wichtel_partner.csv', header=None)
print("Die Paarungen sind unter wichtel_partner.csv gespeichert")
input("Drücke Enter zum verlassen.")