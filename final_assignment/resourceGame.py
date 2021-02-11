import PySimpleGUI as sg
import pysd
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import os
import time

################################################################
#####    makeModel    #####
#
#   Purpose: Convert Vensim model to pysd model.
#
#   Input:   NONE
#
#   Output:  model - pysd version of the Vensim model

def makeModel():
    model = pysd.read_vensim('final.mdl')
    return model


################################################################
#####    savePlot    #####
#
#   Purpose:    Make plot for given kpi using previous values and new values.
#
#   Input:      prevStocks - Values of all stocks from previous model run
#               stocks -     Values of all stocks from most recent model run
#               kpiName -    Name of KPI to make plot of
#
#   Output:     fig -        Figure of relevent KPI

def savePlot(prevStocks,stocks,kpiName):
    if prevStocks is not None:
        
        fig, ax = plt.subplots()
        ax.plot(prevStocks['TIME'],prevStocks[kpiName])
        ax.plot(stocks['TIME'],stocks[kpiName])
        ax.legend(('previous','new'), loc=2, borderaxespad=0.)
        ax.set(xlabel='Time (years)', ylabel=kpiName,
           title=kpiName)
        ax.grid()
        fig.savefig(kpiName+".png")
        
    else:
        
        fig, ax = plt.subplots()
        ax.plot(stocks['TIME'],stocks[kpiName])

        ax.set(xlabel='time (years)', ylabel=kpiName,
           title=kpiName)
        ax.grid()
        fig.savefig(kpiName+".png")
    
    plt.close()
    return fig


################################################################
#####    generateInit    #####
#
#   Purpose: Generate initial behavior of model using intiial conditions given in Vensim model.
#
#   Input:   model -    pysd model
#            KPINames - List of relevant KPI's as written in Vensim
#
#   Output:  stocks -   Dataframe of all variable outputs from initial model run

def generateInit(model,KPINames):
    
    stocks = model.run()
    for i in KPINames:
        savePlot(None,stocks,i)
    
    return stocks


################################################################
#####    generateNew    #####
#
#     Purpose: Generate new outputs based on the outputs from the previous model run and the
#              values given by the user in the game.
#
#     Input:   prevStocks -  Values of all stocks from previous model run
#              model -       pysd model
#              newLevers -   New values for the levers taken from the game input of the user
#              endYear -     The current number of years that the model has been run so far
#              roundLength - Length of one round in the game
#              KPINames -    List of relevant KPI's as written in Vensim
#              leverNames -  List of lever names as seen in Vensim used in the game
#
#     Output:  stocks -      Dataframe of all variable outputs from new model run
#              endYear -     The updated current number of years that the model has been run so far

def generateNew(prevStocks,model,newLevers,endYear,roundLength,KPINames,leverNames):
    # Use current (most recent) model outcomes and overwrite relevant levers with user input  
    stocks = model.run(initial_condition = 'current',
                       params={leverNames[0]:newLevers[0],
                               leverNames[1]:newLevers[1]*1e9,
                               leverNames[2]:newLevers[2]*1e9,
                               leverNames[3]:newLevers[3]*1e9,
                               leverNames[4]:newLevers[4]*1e9},
                       return_timestamps=list(np.arange(endYear,endYear+roundLength,model.components.time_step())))
    
    # Keep track of most recent year of the simulation
    endYear += roundLength
    
    #Save plots for user interface
    for i in KPINames:
        savePlot(prevStocks,stocks,i)

    stocks = prevStocks.append(stocks)
    
    return stocks, endYear


################################################################
#####    makeLayout    #####
#
#     Purpose: Make the primary game layout screen. This screen is used by the player to make decisions on lever values.
#
#     Input:   scenario -   String that keeps track of the stage of the game the player is at
#              newLevers -  New values for the levers taken from the game input of the user
#              KPINames -   List of relevant KPI's as written in Vensim
#              leverNames - List of lever names as seen in Vensim used in the game
#              stocks -     Dataframe of all variable outputs from most recent model run
#              endYear -    Current number of years the game has run so far
#
#     Output:  layout -     pysimplegui layout used to make game screen
#              numBad -     number of KPIs lower than the threshold

def makeLayout(scenario,newLevers,KPINames,leverNames,stocks,endYear):
    KPITitles = ['Debt as Percentage of GDP',
                 'HDI',
                 'Unemployment',
                 'Political Approval',
                 'Total Export Revenue',
                 'Government Income']
    
    leverTitles = ['Nationalisation Switch',
                 'Government mining research spending',
                 'Investment in wealth fund',
                 'Social spending',
                 'Human developoment spending']
    
    sitRep = ''
    
    KPIThresholds = [-0.1,0.8,-0.18,65,0.5e11]
    KPIValues = [stocks[i].iloc[-1] for i in KPINames[:-1]]
    KPIValues[0] = -KPIValues[0]
    KPIValues[2] = -KPIValues[2]
    
    isKPIBad = [KPIValues[i] < KPIThresholds[i] for i in range(5)] 
    numBad = np.sum(isKPIBad)
    
    buttonColor = 'green'
    buttonText = 'white'
    numKPIs = range(len(isKPIBad))
    
    if (scenario == 'Start'):
        storyLine = 'Welcome to your policy suite!\n\nThe sliders below represent your policy levers. By sliding your levers you can indicate the budget\nyou wish to allocate (in Local Currency Units, LCU) to each policy.\n\nBelow the policy levers you will see your KPIs graphically represented. In addition, your Government\nIncome (right) is visualized. When deciding on your policy spending, make sure you keep an eye on your\nGovernment Income, you don’t want too much debt!\n\nDo your best to make something of your new position!'

        buttonName = 'Start'
        
    elif (scenario == 'Intermediate'):        
        storyLine = 'Another five years have passed. Here is your status report, you are outside of acceptable levels on '+str(numBad)+' KPI(s).'
        buttonName = 'Next'
        
        # Make news headlines to spice the game up
        if endYear == 15:
            storyLine = storyLine+'\n\nNEWS FLASH: President of Argentina vouches to double education spending and the people love it!'
        elif endYear == 25:
            storyLine = storyLine+'\n\nNEWS FLASH: Lithium prices drop to a 10 year low, markets respond!'
    
        for i in numKPIs:
            sitRep = sitRep+KPITitles[i]+': '
            if isKPIBad[i]:
                sitRep = sitRep+'   Be careful! Outside acceptable levels.'+'\n'
            else:
                sitRep = sitRep+'   Keep it up! Within acceptable levels.'+'\n'
        
    elif (scenario == 'Penultimate'):
        storyLine = 'Keep in mind that this is your second to last opportunity to make policy changes. Choose wisely!\nHere is your status report, you are outside of acceptable levels on '+str(numBad)+' KPI(s).'
        buttonName = 'Final Turn'
        buttonColor = 'yellow'
        buttonText = 'black'
        for i in numKPIs:
            sitRep = sitRep+KPITitles[i]+': '
            if isKPIBad[i]:
                sitRep = sitRep+'   Be careful! Outside acceptable levels.'+'\n'
            else:
                sitRep = sitRep+'   Keep it up! Within acceptable levels.'+'\n'
        
    else:
        storyLine = 'Here is your final status report, you are outside of acceptable levels on '+str(numBad)+" KPI(s).\nThis is your last chance to make policy changes, let's hope it is not too late..."
        buttonName = 'End'
        buttonColor = 'red'
        for i in numKPIs:
            sitRep = sitRep+KPITitles[i]+': '
            if isKPIBad[i]:
                sitRep = sitRep+'   Be careful! Outside acceptable levels.'+'\n'
            else:
                sitRep = sitRep+'   Keep it up! Within acceptable levels.'+'\n'
    
    tabTitleBG = 'grey'
    tabTitleColor = 'white'
    wd = os.getcwd()
    
    tab1_layout = [[sg.Image(wd+'/'+KPINames[0]+'.png')]]
    tab2_layout = [[sg.Image(wd+'/'+KPINames[1]+'.png')]]
    tab3_layout = [[sg.Image(wd+'/'+KPINames[2]+'.png')]]
    tab4_layout = [[sg.Image(wd+'/'+KPINames[3]+'.png')]]
    tab5_layout = [[sg.Image(wd+'/'+KPINames[4]+'.png')]]
    tab6_layout = [[sg.Image(wd+'/'+KPINames[5]+'.png')]]
    
    sg.ChangeLookAndFeel('Reddit')

    tabTitle = 'black'
    tabBackground = tabTitleBG
    text_width = 40
    
    layout = [
        # Story element
        [sg.Text(storyLine)],
        
        # Situational report
        [sg.Text(sitRep)],
        
        #Policy levers
        [sg.Text(leverTitles[0]+' (0: no, 1: yes)', size=(text_width, 1)), sg.Slider(range=(0, 1), orientation='h', size=(20, 20), default_value=newLevers[0])],
        [sg.Text(leverTitles[1]+' [bn LCU/yr]', size=(text_width, 1)), sg.Slider(range=(0, 40), orientation='h', size=(20, 20), default_value=newLevers[1])],
        [sg.Text(leverTitles[2]+' [bn LCU/yr]', size=(text_width, 1)), sg.Slider(range=(0, 40), orientation='h', size=(20, 20), default_value=newLevers[2])],      
        [sg.Text(leverTitles[3]+' [bn LCU/yr]', size=(text_width, 1)), sg.Slider(range=(0, 40), orientation='h', size=(20, 20), default_value=newLevers[3])],
        [sg.Text(leverTitles[4]+' [bn LCU/yr]', size=(text_width, 1)), sg.Slider(range=(0, 40), orientation='h', size=(20, 20), default_value=newLevers[4])],
        
        # Plotting
        [sg.TabGroup([[sg.Tab(KPITitles[0], tab1_layout, background_color=tabBackground),
                       sg.Tab(KPITitles[1], tab2_layout, background_color=tabBackground),
                       sg.Tab(KPITitles[2], tab3_layout, background_color=tabBackground),
                       sg.Tab(KPITitles[3], tab4_layout, background_color=tabBackground),
                       sg.Tab(KPITitles[4], tab5_layout, background_color=tabBackground),
                       sg.Tab(KPITitles[5], tab6_layout, background_color=tabBackground)]],
                     title_color=tabTitle,selected_title_color=tabTitle)],
        
        # Button
        [sg.Button(buttonName)]
    ]
    
    return layout, numBad

################################################################
#####    textColour    #####
#
#     Purpose: Select color of text based on value of stock
#
#     Input:   stocks -     Dataframe of all variable outputs from most recent model run
#              leverNames - List of names of the policies
#
#     Output:  'red' or 'black' (text color)

def colorIndic(stocks,leverNames):
    if stocks[leverNames[0]].iloc[-1] < 1000:
        return 'red'
    else:
        return 'black'

################################################################
#####    winningScreen    #####
#
#     Purpose: Make layout of final screen if the player wins
#
#     Input:   NONE
#
#     Output:  layout - pysimplegui layout used to make game screen

def winningScreen():
    layout = [
        [sg.Text('Well done! You managed to abate the resource curse within the allotted time!\n\n'
                 +'Thank you for playing./n/n/'
                 +'Credits in alphabetical order:\n'
                 +'Daan van Beek\nErik Pronk\nIrene van Droffelaar\nPhilip Seijger')],
        [sg.Button('Quit')]
    ]    
    return layout


################################################################
#####    losingScreen    #####
#
#     Purpose: Make layout of final screen if the player loses
#
#     Input:   NONE
#
#     Output:  layout - pysimplegui layout used to make game screen

def losingScreen():
    layout = [
        [sg.Text('Better luck next time… if there is a next time. You did not manage to abate the\n'
                 +'resource curse, causing turmoil in your country.\n\n'
                 +'Credits in alphabetical order:\n'
                 +'Daan van Beek\nErik Pronk\nIrene van Droffelaar\nPhilip Seijger')],
        [sg.Button('Quit')]
    ]    
    return layout


################################################################
#####    startScreen    #####
#
#     Purpose: Make layout of start screen of the game
#
#     Input:   NONE
#
#     Output:  layout - pysimplegui layout used to make game screen

def startScreen():
    sg.ChangeLookAndFeel('Reddit')
    layout = [
        [sg.Text('Welcome! You have just been elected as the political leader of your country.\n'+
                 'Your party enjoys an overwhelming majority, giving you tremendous freedom in \n'+
                 'enacting or abolishing policies. Your goal is the betterment of your country \n'+
                 'and its inhabitants; straightforward enough…\n\n'+
                 'The latest news this morning mentions the discovery of the world 2nd largest\n'+
                 'Lithium reserve, right on your doorstep.\n\n'+
                 'What should we do?'
                 )],
        [sg.Image(os.getcwd()+'/govt_building.png')],
        [sg.Button('Begin!')]
        
    ]    
    return layout


################################################################
#####    runGame    #####
#
#     Purpose: Main function to setup and run the game
#
#     Input:   NONE
#
#     Output:  NONE

def runGame():
    endYear = 5
    maxYear = 40
    roundLength = 5
    winCondition = 0
    model = makeModel()
    
    leverNames = ['nationalisation SWITCH',
                 'government mining research investment factor',
                 'Investment in wealth fund',
                 'Social spending',
                 'New HD spending']
    
    KPINames = ['Debt as percentage of GDP',
                'Human Development Index',
                'national unemployment percentage',
                'public approval rate',
                'Total exports',
                'Government income']
    
    scenario = 'Start'
    graph = os.getcwd()+'/test.png'
    defaultLever1 = 0
    defaultLever2 = 0
    defaultLever3 = 0
    defaultLever4 = 0
    defaultLever5 = 0
    values = np.ones(5)+1    
    
    stocks = generateInit(model,KPINames)
    
    numTurns = 8
    
    layout = startScreen()
    window = sg.Window('Simple Game').Layout(layout)
    button, values = window.Read()
    window.Close()
    
    # Run the game for given number of turns        
    for i in range(numTurns):
        if i==0:
            # Initiate first round of game
            scenario = 'Start'
            newLevers = np.zeros(5) # [stocks[leverNames[i]].iloc[-1] for i in range(5)]
            newLevers[3] = newLevers [3]/1e9
            layout, numBad = makeLayout(scenario,newLevers,KPINames,leverNames,stocks,endYear)
            window = sg.Window('Simple Game').Layout(layout)
            button, values = window.Read()
            newLevers = [values[0],
                        values[1],
                        values[2],
                        values[3],
                        values[4]]
            stocks, endYear = generateNew(stocks,model,newLevers,endYear,roundLength,KPINames,leverNames)
            
        elif i==numTurns-2:
            # Initiate penultimate round of game
            scenario = 'Penultimate'
            layout, numBad = makeLayout(scenario,newLevers,KPINames,leverNames,stocks,endYear)
            window.Close()
            window = sg.Window('Simple Game').Layout(layout)
            button, values = window.Read()
            newLevers = [values[0],
                        values[1],
                        values[2],
                        values[3],
                        values[4]]
            stocks, endYear = generateNew(stocks,model,newLevers,endYear,roundLength,KPINames, leverNames)
            
            # Lose condition
            if numBad==5:
                layout = losingScreen()
                window.Close()
                window = sg.Window('Simple Game').Layout(layout)
                button, values = window.Read()
                window.Close()
                winCondition = 2 # Signifies a loss
                break
        
        elif i==numTurns-1:
            # Initiate last round of the game with results (win or lose)       
            scenario = 'End'
            layout, numBad = makeLayout(scenario,newLevers,KPINames,leverNames,stocks,endYear)
            window.Close()
            window = sg.Window('Simple Game').Layout(layout)
            button, values = window.Read()

            # Win condition at the end of the game
            if numBad<2:
                layout = winningScreen()
                window.Close()
                window = sg.Window('Simple Game').Layout(layout)
                button, values = window.Read()
                window.Close()
                winCondition = 1

            # Lose condition at end of game
            else:
                layout = losingScreen()
                window.Close()
                window = sg.Window('Simple Game').Layout(layout)
                button, values = window.Read()
                window.Close()
                winCondition = 2 # Signifies a loss
                break
        
        else:
            # Initiate intermediate round of game
            scenario = 'Intermediate'
            layout, numBad = makeLayout(scenario,newLevers,KPINames,leverNames,stocks,endYear)
            window.Close()
            window = sg.Window('Simple Game').Layout(layout)
            button, values = window.Read()   
            newLevers = [values[0],
                        values[1],
                        values[2],
                        values[3],
                        values[4]]
            stocks, endYear = generateNew(stocks,model,newLevers,endYear,roundLength,KPINames,leverNames)
            
            # Lose condition
            if numBad==5:
                layout = losingScreen()
                window.Close()
                window = sg.Window('Simple Game').Layout(layout)
                button, values = window.Read()
                window.Close()
                winCondition = 2 # Signifies a loss
                break
    
    return


################################################################