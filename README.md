Fooling around with Sample Data from NBS
========================================

## Workflow

The basic workflow is `Load` -> `Clean` -> `Do`
...with a little help from my `Functions`.

I'll comment gratuitously in-line, so looking at the code should be mostly self-explanatory. 

### 1. Load (NBSload.py)
Convert the data from the format in which it was provided (a bunch of csv files) into something I want to work with ([Pandas](http://pandas.pydata.org/) dataframes). 

### 2. Clean (NBSclean.py)
If I need to pre-process the data before having fun with it, I'll do it here. 

### 3. Do (NBSdo.py)
The fun stuff here. 

### F. Functions
I may move some function here to keep things clean in the other files. 

## Exploring the data
A lot of this kind of work involves just exploring the data and visualizing it, a process which is hard to capture by traditional means. To this end, I will include some ipython notebooks (.ipynb), and occasional pdf exports of the notebooks. These will be in the *docs* folder 

## Results
I'll probably add some results documentation once I have something to show, perhaps also in the form of IPython Notebooks. 

## But where's the data?
Oh, right. Sorry. This repo is for my own benefit and for anybody at NBS who might want to take a look. So the data with which I'm working is actually not available here. The data is not mine to give away in any case. 

But it may be useful to note that the data, which I have and you probably don't, is stored in a subdirectory called *data*, in comma delimited csv files. There are 150 of these csv files in the sample data set. 
