from django.shortcuts import render
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt


def page_not_found(request, exeption):
    return render(request, '404.html', status=404)


def index(request):
    print("\t- Index.htmL -")
    return render(request, 'index.html')


def question1(request):
    # data = pd.read_csv('data.csv')
    # code to generate diagram using pandas
    # return render(request, 'question1.html', {'diagram': diagram})
    return render(request, 'question1.html')


def question2(request):
    # Lecture de fichier csv
    df = pd.read_csv(
        r"C:\Users\user\PycharmProjects\Greta-Formation-Python-2023\jeu-de-donnes-que-faire-a-paris\que-faire-a-paris-.csv",
        sep=';', header=0)

    # Copier df to df_propre pour faire les manipulations
    df_propre = df.copy()

    # Retirer les values manquantes
    df_propre.dropna(how='all', inplace=True)

    # Verifier si values sont NaN
    df_propre.isnull().values.any()

    index_ville = df_propre[df_propre["address_city"] != "Paris"].index
    df_propre.drop(index_ville, inplace=True)

    # Garder les collonnes utiles pour manipulation suivantes
    columns_to_keep = ['id', 'title', 'date_start', 'date_end', 'tags', 'address_name', 'address_street',
                       'address_zipcode', 'lat_lon', 'price_type']
    df_propre.drop(df.columns.difference(columns_to_keep), axis=1, inplace=True)

    # Garder le premier mot sur serie de tags
    df_propre['tags'] = df_propre['tags'].str.split(';').str[0]

    liste_types_d_evenements_pas_doublane = []
    liste_types_d_evenements_doublane = []
    dict = {}

    for i in df_propre['tags']:
        liste_types_d_evenements_doublane.append(i)
        if i not in liste_types_d_evenements_pas_doublane:
            liste_types_d_evenements_pas_doublane.append(i)

    for i in liste_types_d_evenements_doublane:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    df_tags = pd.DataFrame(list(dict.items()), columns=['evenement', 'occurrences'])

    df_filtered = df_tags[df_tags['occurrences'] > 33]

    # Create the pie chart
    fig, ax = plt.subplots()

    ax.pie(df_filtered['occurrences'], labels=df_filtered['evenement'])
    # ax.pie(df_filtered['occurrences'], labels=df_filtered['evenement'], autopct='%1.1f%%')
    # Add a title
    ax.set_title('Pie Chart for Evenements')
    pie_graph_file = "static/images/q2_pie.png"
    plt.savefig(pie_graph_file)

    barplot = sns.barplot(x='occurrences', y='evenement', data=df_filtered)
    barplot.set_title('Barplot for Evenements')
    barplot_file = "static/images/q2_barplot.png"
    barplot.get_figure().savefig(barplot_file)
    # return render(request, 'question2.html', {'pie_graph_file': pie_graph_file, 'barplot_file': barplot_file})
    return render(request, 'question2.html', {'barplot_file': barplot_file})


def question3(request):
    return render(request, 'question2.html')

# df_propre['price_type'] = df_propre['price_type'].replace('gratuit sous condition', 'gratuit')

# threshold = 10
# zip_counts = df_arrondissement ["address_zipcode"].value_counts()
# valid_zips = zip_counts[zip_counts >= threshold].index
# df_valid = df_arrondissement[df_arrondissement["address_zipcode"].isin(valid_zips)]
