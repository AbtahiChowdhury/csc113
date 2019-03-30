import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

#Using the data from hn_submissions.py, make a bar chart showing the
#most active discussions currently happening on Hacker News.

#Make an API call, and store the response.
r=requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
print("Status code:",r.status_code)

#Process information about each submission.
submissionids=r.json()
submissiondicts=[]
for submissionid in submissionids[:30]:
    #Make a separate API call for each submission.
    url=('https://hacker-news.firebaseio.com/v0/item/'+str(submissionid)+'.json')
    submissionrequest=requests.get(url)
    print("Status code:",submissionrequest.status_code)
    responsedict=submissionrequest.json()

    #The height of each bar represents the number of comments
    #The label for each bar is the submission’s title
    #Each bar has a link to the page for that submission
    submissiondict={
        'label': responsedict['title'],
        'xlink': 'http://news.ycombinator.com/item?id='+str(submissionid),
        'value': responsedict.get('descendants', 0)
    }
    submissiondicts.append(submissiondict)

#Sort dictionary by number of comments
submissiondicts=sorted(submissiondicts, key=itemgetter('value'),reverse=True)

#Print each submission in decending order
for submissiondict in submissiondicts:
    print("\nTitle:", submissiondict['label'])
    print("Discussion link:", submissiondict['xlink'])
    print("Comments:", submissiondict['value'])

#Visualize the results.
plotstyle=LS('#333366', base_style=LCS)
plotstyle.title_font_size=24
plotstyle.label_font_size=14
plotstyle.major_label_font_size=18

#Configure the plot.
plotconfig=pygal.Config()
plotconfig.x_label_rotation=45
plotconfig.show_legend=False
plotconfig.truncate_label=15
plotconfig.show_y_guides=False
plotconfig.width=1000

#Plot the data
chart=pygal.Bar(plotconfig, style=plotstyle)
chart.title='Most-Commented News on Hacker News'
chart.add('', submissiondicts)

#Save file
chart.render_to_file('ex02.svg')
