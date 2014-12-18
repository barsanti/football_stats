import pygal
from pygal.style import NeonStyle
from tkinter import *

#### Stats
RonaldoGoalsName = ('Ronaldo Goals')
RonaldoGoalsData = ([3, 4, 5, 9, 17, 31, 18, 26, 40, 46, 34, 31, 25])
RonaldoAppearancesName = ('Ronaldo Appearances')
RonaldoAppearancesData = ([25, 29, 33, 33, 34, 34, 33, 29, 34, 38, 34, 30, 14])
MessiGoalsName = ('Messi Goals')
MessiGoalsData = ([None, None, 1, 6, 14, 10, 23, 34, 31, 50, 46, 28, 13])
MessiAppearancesName = ('Messi Appearances')
MessiAppearancesData = ([None, None, 7, 17, 26, 28, 31, 35, 33, 37, 32, 31, 14])
SuarezGoalsName = ('Suarez Goals')
SuarezGoalsData = ([None, None, None, None, 10, 10, 17, 22, 35, 11, 11, 23, 31])
SuarezAppearancesName = ('Suarez Appearances')
SuarezAppearancesData = ([None, None, None, None, 27, 29, 33, 31, 33, 26, 31, 33, 7])

#### Simple Line Chart
def rvm_make_line_chart():
    rvm_comp_slc = pygal.Line()
    rvm_comp_slc.title = "Messi vs Ronaldo Goals/Appearances"
    rvm_comp_slc.x_labels = map(str, range(2002, 2015))
    rvm_comp_slc.add(RonaldoGoalsName, RonaldoGoalsData)
    rvm_comp_slc.add(RonaldoAppearancesName, RonaldoAppearancesData)
    rvm_comp_slc.add(MessiGoalsName, MessiGoalsData)
    rvm_comp_slc.add(MessiAppearancesName, MessiAppearancesData)
    rvm_comp_slc.render_to_file("Ronaldo vs Messi Comparison.html")

#### Stacked Chart
def rvm_make_stacked_chart():
    rvm_comp_stacked = pygal.StackedLine(fill=True, interpolate='cubic', style=NeonStyle)
    rvm_comp_stacked.title = "Messi vs Ronaldo Goals/Appearances"
    rvm_comp_stacked.x_labels = map(str, range(2002, 2015))
    rvm_comp_stacked.add(RonaldoGoalsName, RonaldoGoalsData)
    rvm_comp_stacked.add(RonaldoAppearancesName, RonaldoAppearancesData)
    rvm_comp_stacked.add(MessiGoalsName, MessiGoalsData)
    rvm_comp_stacked.add(MessiAppearancesName, MessiAppearancesData)
    rvm_comp_stacked.render_to_file("Ronaldo vs Messi Comparison2.html")

#### Bar Chart
def rvm_make_bar_chart():
    rvm_comp_bar = pygal.Bar(style=NeonStyle)
    rvm_comp_bar.title = "Messi vs Ronaldo Goals/Appearances"
    rvm_comp_bar.x_labels = map(str, range(2002, 2015))
    rvm_comp_bar.add(RonaldoGoalsName, RonaldoGoalsData)
    rvm_comp_bar.add(RonaldoAppearancesName, RonaldoAppearancesData)
    rvm_comp_bar.add(MessiGoalsName, MessiGoalsData)
    rvm_comp_bar.add(MessiAppearancesName, MessiAppearancesData)
    rvm_comp_bar.render_to_file("Ronaldo vs Messi Comparison3.html")

#### Custom Player Line Chart
def customplayer_make_line_chart():
    customplayer_line = pygal.Line()
    customplayer.title = "Player Comparison"
    customplayer.x_labels = map(str, range(2002, 2015))
    customplayer.add(%playerentry.get()+"GoalsName", %playerentry.get()+"GoalsData")
    customplayer.add(%playerentry.get()+"AppearancesName", %playerentry.get()+"AppearancesData")
    customplayer.add(%playerentry2.get()+"GoalsName", %playerentry2.get()+"GoalsData")
    customplayer.add(%playerentry2.get()+"AppearancesName", %playerentry2.get()+"AppearancesData")

##GUI
root = Tk()
root.title("Ronaldo vs Messi Graph Generator")
root.geometry("600x350")

rvm_line_chart_button = Button(root, text="Make Ronaldo vs Messi line chart", command=rvm_make_line_chart)
rvm_line_chart_button.pack(pady=10)
rvm_stacked_chart_button = Button(root, text="Make Ronaldo vs Messi stacked chart", command=rvm_make_stacked_chart)
rvm_stacked_chart_button.pack(pady=10)
rvm_bar_chart_button = Button(root, text="Make Ronaldo vs Messi bar chart", command=rvm_make_bar_chart)
rvm_bar_chart_button.pack(pady=10)



playerentry = Entry(root)
playerentry.pack(pady=10)

playerentry2 = Entry(root)
playerentry2.pack(pady=10)
root.mainloop()
