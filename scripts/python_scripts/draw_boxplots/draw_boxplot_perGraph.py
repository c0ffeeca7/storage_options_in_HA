# drawing a boxplot for data from csv
# https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/
# https://stackoverflow.com/questions/55648729/python-how-to-print-the-box-whiskers-and-outlier-values-in-box-and-whisker-plo

# Import libraries
from operator import contains
from typing import List
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.shape_base import block
import boxplot_config
import time

median: float


# graphs including 4 boxplots. set figsize to 18, 3
#graphs = [ boxplot_config.graph_groupByWeek_CPU, boxplot_config.graph_groupByWeek_Memory_hwm, boxplot_config.graph_groupByWeek_io, boxplot_config.graph_minMax_CPU, boxplot_config.graph_minMax_realtime, boxplot_config.graph_minMax_Memory_hwm, boxplot_config.graph_monSun_CPU, boxplot_config.graph_monSun_realtime, boxplot_config.graph_monSun_Memory_hwm,  boxplot_config.graph_last2_CPU,boxplot_config.graph_last2_realtime, boxplot_config.graph_last2_Memory_hwm, boxplot_config.graph_sum_CPU, boxplot_config.graph_sum_realtime, boxplot_config.graph_sum_Memory_hwm,  boxplot_config.graph_groupByMonth_CPU, boxplot_config.graph_groupByMonth_Memory_hwm, boxplot_config.graph_groupByMonth_io, boxplot_config.graph_groupByYear_CPU, boxplot_config.graph_groupByYear_Memory_hwm, boxplot_config.graph_groupByYear_io, boxplot_config.graph_groupByDay_CPU, boxplot_config.graph_groupByDay_Memory_hwm, boxplot_config.graph_groupByDay_io ]

# graphs including 4 boxplots. set figsize to 18, 2 (without groupByX)
#graphs = [boxplot_config.graph_minMax_CPU, boxplot_config.graph_minMax_realtime, boxplot_config.graph_minMax_Memory_hwm, boxplot_config.graph_monSun_CPU, boxplot_config.graph_monSun_realtime, boxplot_config.graph_monSun_Memory_hwm,  boxplot_config.graph_last2_CPU,boxplot_config.graph_last2_realtime, boxplot_config.graph_last2_Memory_hwm, boxplot_config.graph_sum_CPU, boxplot_config.graph_sum_realtime, boxplot_config.graph_sum_Memory_hwm ]

# IO graphs including 6 boxplots. set figsize to 18, 5
#graphs = [boxplot_config.graph_minMax_io, boxplot_config.graph_monSun_io, boxplot_config.graph_last2_io, boxplot_config.graph_sum_io]

# graphs for group by (16 boxplots). figsize 18, 20
graphs = [ boxplot_config.graph_AllGroupBy_CPU, boxplot_config.graph_AllGroupBy_realtime,boxplot_config.graph_AllGroupBy_realtimeNoStates,boxplot_config.graph_AllGroupBy_Memory_hwm, boxplot_config.graph_AllGroupBy_io, boxplot_config.graph_l2_min_mon_sum_CPU, boxplot_config.graph_l2_min_mon_sum_memory, boxplot_config.graph_l2_min_mon_sum_realtime, boxplot_config.graph_l2_min_mon_sum_IO ]
# graphs = [ boxplot_config.graph_AllGroupBy_io ]

def drawBoxplot(graphs: List):

    graphs: List = graphs
    graphTitle: str
    graphFilename:str
    bpTitle: str
    srcFile: str
    column: int

    for graph in graphs:
        graphTitle: str = graph["chart_title"]
        graphFilename = graph["svg_name"]
        #print(graphTitle)
        #print(graphFilename)
        ###
        #######Change figure size here!############################################
        fig = plt.figure(figsize =(18, 10))
        # 1 row, 1 column, left
        ax = fig.add_subplot(111)

       
        ylabel = []
        allData = []
        srcFile = "bla"
        colorsToSet = []
        
        with open(f"raspi_{graphFilename}.txt", "w") as statfile:
            for boxplot in graph["boxplots"]:
                bpTitle: str = boxplot["title of boxplot"]    
                srcFile: str = boxplot["filename"]
                if "influx" in srcFile:
                    colorsToSet.append('#f255e3')
                elif "measurements/states" in srcFile:
                    colorsToSet.append('#A1DBF4')
                elif "stat_" in srcFile:
                    colorsToSet.append('#6DC99A')
                elif "measurements/ts_" in srcFile:
                    colorsToSet.append('#008000')
                else:
                    colorsToSet.append('#ff0000')
                column: int = boxplot["column"]
                ylabel.append(bpTitle)
                
                #print(bpTitle)
                #print(srcFile)
                #print(column)
                
                csv = np.genfromtxt (srcFile, delimiter=",")
                #print(type(csv[:,column]))
                metricValue: np.ndarray = csv[:,column]
                # allData = np.append(allData,metricValue,)
                allData.append(metricValue)
                print(metricValue)
                median = np.median(metricValue)
                statfile.write(f"{bpTitle}: {median}\n")
        
        # Creating axes instance
        bp = ax.boxplot(allData, patch_artist = True,
                        notch ='True', vert = 0, showfliers=True, showmeans=True)
              

        if "Disk I/O" in graphTitle:
            for patch, color in zip(bp['boxes'], colorsToSet):
                patch.set_facecolor(color)
        else: 
            for patch, color in zip(bp['boxes'], colorsToSet):
                patch.set_facecolor(color)
    
        # changing color and linewidth of
        # whiskers
        for whisker in bp['whiskers']:
            whisker.set(color ='#8B008B',
                        linewidth = 2.5,
                        alpha = 1.0)
        
        # changing color and linewidth of
        # caps
        for cap in bp['caps']:
            cap.set(color ='#8B008B',
                    linewidth = 1.5)
        
        # changing color and linewidth of
        # medians
        for median in bp['medians']:
            median.set(color ='red',
                    linewidth = 1.0)
        
        # changing style of fliers
        for flier in bp['fliers']:
            flier.set(marker ='D',
                    alpha = 1.0,
                    color ='#e7298a')
           
        # y-axis labels
        ax.set_yticklabels(ylabel, fontsize = 16)
        plt.xticks(fontsize=16)
        
        # Adding title
        plt.title(graphTitle, fontsize=20, pad=10)
    
        # Removing top axes and right axes
        # ticks
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

        # saving plot as graphic
        # print(graphFilename)
        fig.savefig(f"gfx/raspi_{graphFilename}.png", format="png", dpi=200,bbox_inches='tight')

        # show plot
        plt.show(block=False)
        plt.close()
   

drawBoxplot(graphs)            
