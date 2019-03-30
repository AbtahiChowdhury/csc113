import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#Modify the API call in python_repos.py so it generates a chart showing
#the most popular projects in other languages.

def getRepoLang(lang):
    """Get the most-starred GitHub repositories for the language."""

    #Make an API call, and store the response.
    url='https://api.github.com/search/repositories?q=language:'+lang.lower().replace(" ", "")+'&sort=stars'
    r=requests.get(url)
    print("Status code:", r.status_code)

    #Store API response in a variable.
    responsedict=r.json()
    print("Total repositories:", responsedict['total_count'])

    #Explore information about the repositories.
    repodicts=responsedict['items']

    names,plotdicts=[],[]
    for repodict in repodicts:
        names.append(repodict['name'])

        #Get the project description, if one is available.
        description=repodict['description']
        if not description:
            description="No description provided."

        plotdict={
            'value': repodict['stargazers_count'],
            'label': description,
            'xlink': repodict['html_url'],
        }
        plotdicts.append(plotdict)

    #Visualization the results.
    plotstyle=LS('#333366', base_style=LCS)
    plotstyle.title_font_size=24
    plotstyle.label_font_size=14
    plotstyle.major_label_font_size=18

    #Configure plot
    plotconfig=pygal.Config()
    plotconfig.x_label_rotation=45
    plotconfig.show_legend=False
    plotconfig.truncate_label=15
    plotconfig.show_y_guides=False
    plotconfig.width=1000

    #Plot data
    chart=pygal.Bar(plotconfig, style=plotstyle)
    chart.title='Most-Starred '+lang+' Projects on GitHub'
    chart.x_labels=names
    chart.add('', plotdicts)

    #Save file
    chart.render_to_file('ex01-'+lang.lower().replace(" ", "")+'-repos.svg')


#Try languages such as JavaScript, Ruby, C, Java, Perl, Haskell, and Go
getRepoLang('Java Script')
getRepoLang('Ruby')
getRepoLang('C')
getRepoLang('Java')
getRepoLang('Perl')
getRepoLang('Haskell')
getRepoLang('Go')
getRepoLang("C++")
getRepoLang("Java")
getRepoLang("Python")
